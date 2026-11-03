"""Shared configuration for embedding, storage, and chat services."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_DIR = Path(__file__).resolve().parent.parent
# Select the env file before loading it; the Golem .env is never overwritten.
load_dotenv(PROJECT_DIR / os.getenv("HW09_ENV_FILE", ".env"))
RUNTIME_PROFILE = os.getenv("RUNTIME_PROFILE", "course")
if RUNTIME_PROFILE not in {"course", "local"}:
    raise ValueError("RUNTIME_PROFILE must be course or local")
DEFAULT_DB_PATH = PROJECT_DIR / ("chroma_local" if RUNTIME_PROFILE == "local" else "chroma_db")
DEFAULT_MANIFEST_PATH = PROJECT_DIR / ("manifest.local.json" if RUNTIME_PROFILE == "local" else "manifest.json")
COLLECTION_NAME = "hw09_documents_local" if RUNTIME_PROFILE == "local" else "hw09_documents"


def setting(name: str, default: str) -> str:
    """Read a setting while keeping classroom endpoint defaults visible."""
    return os.getenv(name, default)


def require_api_key(name: str) -> str:
    """Return an API key and reject the documented placeholder."""
    value = os.getenv(name, "")
    if not value or value == "student-should-use-their-own":
        raise RuntimeError(
            f"Set {name} in .env to the API key assigned to you. "
            "See .env.example."
        )
    return value


def runtime_metadata() -> dict:
    """Safe settings for traces; never includes API keys."""
    if RUNTIME_PROFILE == "local":
        from app.local import local_base_url, local_thinking_enabled, local_output_tokens, local_answer_mode, local_context_tokens
        return {
            "runtime_profile": "local",
            "embedding_provider": "ollama",
            "action_generation": "retrieval and named-source coverage required before final action; citations constrained to observed chunk IDs",
            "answer_mode": local_answer_mode(),
            "maximum_answer_excerpts_per_source": 8,
            "local_decision_format": "short passage labels grouped by source with per-requirement coverage assessment; raw decision and label-to-stored-ID map logged; adapter copies quotes",
            "maximum_context_passages": "8, or two per requested source if greater",
            "retrieval_unit": "page_context; all stored chunks from each selected physical page; parent IDs retained",
            "model_history": "original question, search arguments, deduplicated passages; first two passages per requested source retained",
            "chat_thinking": local_thinking_enabled(),
            "thinking_policy": "enabled after the initial and requested-source retrievals; disabled while required sources are missing",
            "chat_context_tokens": local_context_tokens(),
            "chat_output_tokens_per_action": local_output_tokens(),
            "document_embedding_batch_size": 8,
            "query_embedding_instruction": "Instruct: Given a food safety question, retrieve relevant passages that answer the question\nQuery:",
            "embedding_service_model": setting("LOCAL_EMBEDDING_MODEL", "qwen3-embedding:8b"),
            "embedding_base_url": local_base_url(),
            "llm_base_url": local_base_url(),
            "configuration_deviation": "Local Ollama Q4 embedding weights and local chat model replace the required course services; not a fully compliant course-service run.",
        }
    return {"runtime_profile": "course", "embedding_provider": "course",
            "embedding_base_url": setting("EMBEDDING_BASE_URL", "http://golem.cs.utahtech.edu:4000/v1"),
            "llm_base_url": setting("LLM_BASE_URL", "http://golem:4000/v1"),
            "configuration_deviation": None}
