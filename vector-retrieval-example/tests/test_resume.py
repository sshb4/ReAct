"""Interrupted builds resume without paying for previously stored embeddings."""
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch

from langchain_core.documents import Document
from app.agent import SOURCES
from app.ingest import ingest


class SubstituteStore:
    def __init__(self):
        self.records = {}
        self.successful_ids = []
        self.deleted = []
        self.fail_after = 1
        self.add_calls = 0
        self._collection = SimpleNamespace(name='fixture', count=lambda: len(self.records))

    def get(self, ids=None, where=None, include=None):
        selected = {key: value for key, value in self.records.items()
                    if (ids is None or key in ids)
                    and (where is None or all(value.metadata.get(k) == v for k, v in where.items()))}
        return {'ids': list(selected), 'embeddings': [[0.1, 0.2] for _ in selected]}

    def delete(self, ids):
        self.deleted.extend(ids)
        for key in ids:
            del self.records[key]

    def add_documents(self, chunks, ids):
        if self.fail_after is not None and self.add_calls >= self.fail_after:
            raise RuntimeError('substitute interrupted service')
        self.add_calls += 1
        self.successful_ids.extend(ids)
        self.records.update(zip(ids, chunks, strict=True))


class ResumeTests(unittest.TestCase):
    def test_resume_skips_stored_vectors_and_rejects_changed_sources(self):
        with tempfile.TemporaryDirectory() as directory, ExitStack() as stack:
            root = Path(directory)
            for name in SOURCES:
                (root / name).write_bytes(b'substitute corpus')
            pages = dict(zip(SOURCES, (732, 45, 292, 23, 18), strict=True))
            chunks = [Document(page_content=f'passage {i}', metadata={'source': SOURCES[0], 'page': 1})
                      for i in range(40)]
            ids = [f'fixture-{i}' for i in range(40)]
            store = SubstituteStore()
            stack.enter_context(patch('app.ingest.RUNTIME_PROFILE', 'course'))
            stack.enter_context(patch('app.ingest.PdfReader', side_effect=lambda path: SimpleNamespace(pages=[None] * pages[path.name])))
            stack.enter_context(patch('app.ingest.chunk_sources', return_value=(chunks, ids)))
            stack.enter_context(patch('app.ingest.open_store', return_value=store))
            manifest = root / 'manifest.json'
            args = ([root], root / 'db', manifest, False, 1400, 200)
            with self.assertRaisesRegex(ValueError, 'no matching build journal'):
                ingest(*args, resume=True)
            with self.assertRaisesRegex(RuntimeError, 'interrupted'):
                ingest(*args)
            self.assertEqual(len(store.records), 32)
            self.assertFalse(manifest.exists())
            self.assertTrue((root / 'manifest.building.json').exists())
            store.fail_after = None
            result = ingest(*args, resume=True)
            self.assertEqual(result['record_count'], 40)
            self.assertEqual(store.successful_ids, ids)
            self.assertEqual(store.deleted, [])
            # Matching completed builds also resume without any embedding calls.
            calls = store.add_calls
            ingest(*args, resume=True)
            self.assertEqual(store.add_calls, calls)
            (root / SOURCES[0]).write_bytes(b'changed source')
            with self.assertRaisesRegex(ValueError, 'no matching build journal'):
                ingest(*args, resume=True)


if __name__ == '__main__':
    unittest.main()
