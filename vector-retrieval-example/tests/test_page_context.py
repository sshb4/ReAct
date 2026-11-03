import unittest
from langchain_core.documents import Document
from app.retrieval import page_contexts


class PageContextTests(unittest.TestCase):
    def test_overlaps_are_merged_and_parent_ids_and_page_identity_preserved(self):
        source = 'utah-risk-factor-study-2016-2017.pdf'
        class Store:
            def get(self, **kwargs):
                return {'documents': ['ratio 1.37', '1.37; limitations'], 'metadatas': [
                    {'source': source, 'page': 4, 'start_index': 0, 'chunk_id': 'table'},
                    {'source': source, 'page': 4, 'start_index': 6, 'chunk_id': 'limits'},
                ]}
        first = Document(page_content='ratio', metadata={'source': source, 'page': 4})
        result = page_contexts([first, first], Store(), 6)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['text'], 'ratio 1.37; limitations')
        self.assertEqual(result[0]['parent_chunk_ids'], ['table', 'limits'])
        self.assertEqual(result[0]['page'], 4)
        self.assertEqual(result, page_contexts([first], Store(), 6))
        self.assertTrue(result[0]['chunk_id'].startswith('page-'))

    def test_conflicting_overlap_is_rejected_instead_of_silently_altering_text(self):
        source = 'fda-food-code-2026.pdf'
        class Store:
            def get(self, **kwargs):
                return {'documents': ['exclude now', 'stay here'], 'metadatas': [
                    {'source': source, 'page': 1, 'start_index': 0, 'chunk_id': 'a'},
                    {'source': source, 'page': 1, 'start_index': 8, 'chunk_id': 'b'},
                ]}
        with self.assertRaisesRegex(ValueError, 'Conflicting'):
            page_contexts([Document(page_content='x', metadata={'source': source, 'page': 1})], Store(), 6)

    def test_changed_parent_identity_changes_derived_passage_identity(self):
        source = 'fda-food-code-2026.pdf'
        class Store:
            parent = 'original'
            def get(self, **kwargs):
                return {'documents': ['text'], 'metadatas': [
                    {'source': source, 'page': 1, 'start_index': 0, 'chunk_id': self.parent}]}
        store = Store()
        doc = Document(page_content='text', metadata={'source': source, 'page': 1})
        before = page_contexts([doc], store, 6)[0]['chunk_id']
        store.parent = 'different-source-hash'
        self.assertNotEqual(before, page_contexts([doc], store, 6)[0]['chunk_id'])
