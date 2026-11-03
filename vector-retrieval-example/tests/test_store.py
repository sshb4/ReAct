"""Real local Chroma integration with deterministic substitute embeddings."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from langchain_core.embeddings import Embeddings
from app.agent import RetrievalInput
from app.ask import build_clients
from app.store import open_store


class SubstituteEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return [self.embed_query(text) for text in texts]

    def embed_query(self, text):
        return [1.0, float("vomiting" in text.lower()), 0.5]


class StoreTests(unittest.TestCase):
    def test_persistence_filter_and_agent_observation_labels(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch("app.store.build_embeddings", return_value=SubstituteEmbeddings()):
                store = open_store(Path(directory))
                store.add_texts(
                    ["Exclude an employee who has vomiting.", "Historical study observations."],
                    metadatas=[
                        {"source": "fda-food-code-2026.pdf", "page": 42, "chunk_id": "code-chunk"},
                        {"source": "utah-risk-factor-study-2016-2017.pdf", "page": 3, "chunk_id": "study-chunk"}],
                    ids=["code-chunk", "study-chunk"])
                reopened = open_store(Path(directory))
                self.assertEqual(reopened._collection.count(), 2)
                with patch("langchain_openai.ChatOpenAI"), patch("app.ask.require_api_key", return_value="unused"):
                    _, retrieve = build_clients(Path(directory), 6)
                observations = retrieve(RetrievalInput(query="vomiting", source="fda-food-code-2026.pdf"))
                self.assertEqual(observations, [{"source": "fda-food-code-2026.pdf", "page": 42,
                                                "chunk_id": "code-chunk", "text": "Exclude an employee who has vomiting."}])


if __name__ == "__main__":
    unittest.main()
