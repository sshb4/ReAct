"""Ingest PDF and text files into a persistent local Chroma collection."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

from app.config import DEFAULT_DB_PATH, DEFAULT_MANIFEST_PATH, RUNTIME_PROFILE, setting, runtime_metadata
from app.store import open_store
from app.agent import SOURCES

SUPPORTED_SUFFIXES = {".pdf", ".txt"}


def discover_sources(inputs: list[Path]) -> list[Path]:
    """Expand files and directories into a stable list of supported files."""
    sources: set[Path] = set()
    for input_path in inputs:
        path = input_path.expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"Source does not exist: {input_path}")
        if path.is_file():
            if path.suffix.lower() not in SUPPORTED_SUFFIXES:
                raise ValueError(f"Unsupported file type: {input_path}")
            sources.add(path)
        else:
            sources.update(
                candidate
                for candidate in path.rglob("*")
                if candidate.is_file()
                and candidate.suffix.lower() in SUPPORTED_SUFFIXES
            )
    if not sources:
        raise ValueError("No .pdf or .txt files were found")
    return sorted(sources)


def read_source(path: Path) -> list[Document]:
    """Extract page-aware documents from one source file."""
    source_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    common = {
        "source": path.name,
        "source_path": str(path),
        "source_hash": source_hash,
        "media_type": "application/pdf" if path.suffix.lower() == ".pdf" else "text/plain",
    }
    if path.suffix.lower() == ".txt":
        return [
            Document(
                page_content=path.read_text(encoding="utf-8"),
                metadata={**common, "page": 1},
            )
        ]

    documents: list[Document] = []
    for page_number, page in enumerate(PdfReader(path).pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            documents.append(
                Document(
                    page_content=text,
                    metadata={**common, "page": page_number},
                )
            )
    return documents


def chunk_sources(
    sources: list[Path], chunk_size: int = 800, chunk_overlap: int = 120
) -> tuple[list[Document], list[str]]:
    """Split sources and assign IDs that remain stable for unchanged content."""
    if type(chunk_size) is not int or chunk_size <= 0 or type(chunk_overlap) is not int or not 0 <= chunk_overlap < chunk_size:
        raise ValueError("Require chunk_size > 0 and 0 <= chunk_overlap < chunk_size")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True,
    )
    chunks: list[Document] = []
    ids: list[str] = []
    for source in sources:
        for chunk in splitter.split_documents(read_source(source)):
            identity = "|".join(
                [
                    chunk.metadata["source"],
                    chunk.metadata["source_hash"],
                    str(chunk.metadata["page"]),
                    str(chunk.metadata["start_index"]),
                    chunk.page_content,
                ]
            )
            chunk_id = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:24]
            chunk.metadata["chunk_id"] = chunk_id
            chunks.append(chunk)
            ids.append(chunk_id)
    if not chunks:
        raise ValueError("The source files contained no extractable text")
    return chunks, ids


def build_identity(sources, db_path, chunk_size, chunk_overlap, local_models):
    """Only vector-producing settings; a chat-model change does not alter vectors."""
    embedding_tag = setting("LOCAL_EMBEDDING_MODEL", "qwen3-embedding:8b")
    runtime = runtime_metadata()
    return {
        "db_path": str(db_path.resolve()),
        "runtime_profile": RUNTIME_PROFILE,
        "embedding_model": setting("EMBEDDING_MODEL", "Qwen3-Embedding-8B"),
        "embedding_base_url": runtime["embedding_base_url"],
        "embedding_weights": [{"name": m["name"], "digest": m["digest"]}
                              for m in (local_models or []) if m["name"] == embedding_tag],
        "chunk_size": chunk_size, "chunk_overlap": chunk_overlap,
        "sources": [{"name": source.name, "sha256": hashlib.sha256(source.read_bytes()).hexdigest()}
                    for source in sources],
    }


def ingest(
    source_inputs: list[Path],
    db_path: Path,
    manifest_path: Path,
    rebuild: bool,
    chunk_size: int,
    chunk_overlap: int,
    resume: bool = False,
) -> dict[str, object]:
    """Build the collection and return an inspectable ingestion manifest."""
    if resume and rebuild:
        raise ValueError("Choose either resume or rebuild")
    if RUNTIME_PROFILE == "local":
        from app.local import local_model_inventory
        local_models = local_model_inventory()
    else:
        local_models = None
    sources = discover_sources(source_inputs)
    if chunk_overlap >= chunk_size:
        raise ValueError("Chunk overlap must be smaller than chunk size")
    if {source.name for source in sources} != set(SOURCES) or len(sources) != 5:
        raise ValueError("Ingest exactly the five supplied homework PDFs")
    if setting("EMBEDDING_MODEL", "Qwen3-Embedding-8B") != "Qwen3-Embedding-8B":
        raise ValueError("This assignment requires Qwen3-Embedding-8B")
    page_counts = {source.name: len(PdfReader(source).pages) for source in sources}
    expected_pages = dict(zip(SOURCES, (732, 45, 292, 23, 18), strict=True))
    if page_counts != expected_pages:
        raise ValueError(f"Corpus page counts differ from supplied corpus: {page_counts}")
    chunks, ids = chunk_sources(sources, chunk_size, chunk_overlap)

    identity = build_identity(sources, db_path, chunk_size, chunk_overlap, local_models)
    journal = manifest_path.with_name(manifest_path.stem + ".building.json")
    if resume:
        if not journal.exists() or json.loads(journal.read_text()) != identity:
            raise ValueError("Cannot resume: no matching build journal (source, vector model, path or chunk settings changed)")
    if rebuild and db_path.exists():
        shutil.rmtree(db_path)
    store = open_store(db_path)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    journal.write_text(json.dumps(identity, indent=2) + "\n")
    if resume:
        existing = set(store.get(include=[])["ids"])
        if not existing.issubset(set(ids)):
            raise ValueError("Cannot resume: database contains unexpected chunk identifiers")
    else:
        existing = set()
        # Replace prior chunks for each source before adding the current version.
        for source in sources:
            old = store.get(where={"source": source.name}, include=[])
            if old["ids"]:
                store.delete(ids=old["ids"])
    pending = [(chunk, chunk_id) for chunk, chunk_id in zip(chunks, ids, strict=True)
               if chunk_id not in existing]
    if resume:
        print(f"Resuming with {len(existing)}/{len(chunks)} chunks already stored", flush=True)
    for start in range(0, len(pending), 32):
        batch = pending[start:start + 32]
        store.add_documents([chunk for chunk, _ in batch], ids=[chunk_id for _, chunk_id in batch])
        print(f"Indexed {len(existing) + min(start + 32, len(pending))}/{len(chunks)} chunks", flush=True)

    stored_ids = store.get(include=[])["ids"]
    sample = store.get(ids=[ids[0]], include=["embeddings"])["embeddings"]
    embedding_dimension = len(sample[0]) if sample is not None and len(sample) else None
    index_version = hashlib.sha256(
        "\n".join(sorted(stored_ids)).encode("utf-8")
    ).hexdigest()[:16]

    manifest: dict[str, object] = {
        **runtime_metadata(),
        "local_models": local_models,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "physical_page_count": sum(page_counts.values()),
        "embedding_model": setting("EMBEDDING_MODEL", "Qwen3-Embedding-8B"),
        "embedding_dimension": embedding_dimension,
        "collection": store._collection.name,
        "index_version": index_version,
        "record_count": store._collection.count(),
        "ingested_chunk_count": len(chunks),
        "chunking": {
            "chunk_size": chunk_size,
            "chunk_overlap": chunk_overlap,
        },
        "parsers": {"pypdf": importlib.metadata.version("pypdf"),
                    "fonttools": importlib.metadata.version("fonttools"), "text": "utf-8"},
        "sources": [
            {
                "name": source.name,
                "path": str(source),
                "physical_pages": page_counts[source.name],
                "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            }
            for source in sources
        ],
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        nargs="+",
        type=Path,
        required=True,
        help="One or more PDF/TXT files or directories",
    )
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--rebuild", action="store_true")
    mode.add_argument("--resume", action="store_true", help="Continue a matching interrupted build without re-embedding stored chunks")
    parser.add_argument("--chunk-size", type=int, default=800)
    parser.add_argument("--chunk-overlap", type=int, default=120)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest = ingest(
        args.source,
        args.db,
        args.manifest,
        args.rebuild,
        args.chunk_size,
        args.chunk_overlap,
        resume=args.resume,
    )
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
