import unittest
from langchain_core.documents import Document
from app.retrieval import rank_candidates


class RetrievalRankingTests(unittest.TestCase):
    def test_identifier_lookup_prefers_heading_to_reference_and_generic_hit(self):
        generic = Document(page_content='Employee illness reporting and procedures.')
        reference = Document(page_content='See section 2-201.12 for details.')
        heading = Document(page_content='2-201.12 Exclusions and Restrictions.\nExclude symptomatic employees.')
        self.assertEqual(rank_candidates('What does 2-201.12 require?', [generic, reference, heading], 2),
                         [heading, reference])

    def test_table_identifier_and_ordinary_semantic_order(self):
        reference = Document(page_content='References for Table 3-A appear later.')
        heading = Document(page_content='Table 3-A Limiting Conditions\nListeria and Salmonella rows.')
        self.assertEqual(rank_candidates('Compare Table 3-A', [reference, heading], 1), [heading])
        self.assertEqual(rank_candidates('vomiting employee', [reference, heading], 1), [reference])


class SectionLinkTests(unittest.TestCase):
    def test_summary_reference_expands_to_primary_chapter_not_annex(self):
        from unittest.mock import Mock
        from app.retrieval import expand_section_links
        source = 'fda-food-code-2026.pdf'
        summary = Document(page_content='Return under 2-\n201.13(A)(1). See 2-201.13.', metadata={'chunk_id':'summary'})
        annex = 'FDA Food Code 2026 Annex 3.\n2-201.13 Public health reasons.'
        primary = 'FDA Food Code 2026  Chapter 2. Management\n2-201.13 Removal of exclusions.\nConditions.'
        store = Mock()
        store.get.return_value={'documents':[annex,primary], 'metadatas':[{'chunk_id':'annex'},{'chunk_id':'rule'}]}
        candidates, ids = expand_section_links('when may an employee return?', [summary], source, store, 6)
        self.assertEqual(ids, ['2-201.13'])
        self.assertEqual(rank_candidates('when may an employee return?',candidates,1,ids)[0].metadata['chunk_id'],'rule')
        store.get.reset_mock()
        self.assertEqual(expand_section_links('look up 2-201.13',[summary],source,store,6),([summary],()))
        store.get.assert_not_called()

    def test_non_code_sources_do_not_follow_code_references(self):
        from unittest.mock import Mock
        from app.retrieval import expand_section_links
        store=Mock()
        documents=[Document(page_content='See 2-201.13 for more.')]
        self.assertEqual(expand_section_links('employee return',documents,'handbook.pdf',store,6),(documents,()))
        store.get.assert_not_called()
