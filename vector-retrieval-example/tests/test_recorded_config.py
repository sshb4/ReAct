import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from app.agent import SOURCES
from app.ask import recorded_config


class RecordedConfigTests(unittest.TestCase):
    def test_local_embedding_digest_must_match_but_chat_can_change(self):
        embedding = {'name': 'qwen3-embedding:8b', 'digest': 'stable-embedding'}
        indexed = [embedding, {'name': 'qwen2.5:1.5b', 'digest': 'old-chat'}]
        current = [embedding, {'name': 'qwen2.5:7b', 'digest': 'new-chat'}]
        data = {'embedding_model': 'Qwen3-Embedding-8B', 'sources': [{'name': s} for s in SOURCES],
                'chunking': {'chunk_size': 1400, 'chunk_overlap': 200}, 'index_version': 'fixture',
                'runtime_profile': 'local', 'local_models': indexed}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'manifest.json'
            path.write_text(json.dumps(data))
            with patch('app.ask.RUNTIME_PROFILE', 'local'), patch('app.ask.runtime_metadata', return_value={'runtime_profile': 'local'}):
                with patch('app.local.local_model_inventory', return_value=current):
                    result = recorded_config(path, k=6, max_steps=16)
                self.assertEqual(result['local_models'], current)
                with patch('app.local.local_model_inventory', return_value=[{**embedding, 'digest': 'changed'}, current[1]]):
                    with self.assertRaisesRegex(ValueError, 'embedding model digest'):
                        recorded_config(path, k=6, max_steps=16)
            with patch('app.ask.RUNTIME_PROFILE', 'course'):
                with self.assertRaisesRegex(ValueError, 'profiles differ'):
                    recorded_config(path, k=6, max_steps=16)


if __name__ == '__main__':
    unittest.main()
