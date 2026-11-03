from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from app.ingest import chunk_sources, discover_sources, read_source


class IngestTests(unittest.TestCase):
    def test_discovers_supported_files_recursively(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "nested").mkdir()
            (root / "a.txt").write_text("alpha", encoding="utf-8")
            (root / "nested" / "b.pdf").write_bytes(b"placeholder")
            (root / "ignored.md").write_text("ignored", encoding="utf-8")

            self.assertEqual(
                [path.name for path in discover_sources([root])], ["a.txt", "b.pdf"]
            )

    def test_text_source_has_traceable_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "policy.txt"
            path.write_text("Late work has a 48 hour limit.", encoding="utf-8")

            document = read_source(path)[0]

            self.assertEqual(document.metadata["source"], "policy.txt")
            self.assertEqual(document.metadata["page"], 1)
            self.assertEqual(len(document.metadata["source_hash"]), 64)

    def test_chunk_ids_are_stable_for_unchanged_text(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "policy.txt"
            path.write_text("A stable policy paragraph.", encoding="utf-8")

            _, first_ids = chunk_sources([path])
            _, second_ids = chunk_sources([path])

            self.assertEqual(first_ids, second_ids)


if __name__ == "__main__":
    unittest.main()


class PhysicalPageTests(unittest.TestCase):
    def test_blank_pdf_pages_do_not_renumber_later_pages(self):
        from unittest.mock import patch
        from types import SimpleNamespace
        pages = [SimpleNamespace(extract_text=lambda: ""),
                 SimpleNamespace(extract_text=lambda: "Page two policy text. " * 20)]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.pdf"
            path.write_bytes(b"substitute PDF bytes")
            with patch("app.ingest.PdfReader", return_value=SimpleNamespace(pages=pages)):
                chunks, ids = chunk_sources([path], chunk_size=100, chunk_overlap=20)
                _, again = chunk_sources([path], chunk_size=100, chunk_overlap=20)
            self.assertEqual(ids, again)
            self.assertEqual(len(ids), len(set(ids)))
            self.assertTrue(all(d.metadata["page"] == 2 for d in chunks))
            self.assertTrue(all(d.metadata["source"] == "test.pdf" for d in chunks))
            self.assertTrue(all(d.metadata["chunk_id"] == i for d, i in zip(chunks, ids)))

    def test_chunk_parameter_validation(self):
        for size, overlap in ((0, 0), (100, -1), (100, 100)):
            with self.assertRaises(ValueError):
                chunk_sources([], size, overlap)
