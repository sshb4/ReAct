"""Explicit local Ollama adapters. Never read or send Golem credentials."""
from __future__ import annotations

import json
import math
import urllib.request
from urllib.parse import urlsplit

from langchain_core.embeddings import Embeddings

from app.config import setting


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, newurl):
        raise RuntimeError("Local Ollama redirects are not permitted")


def local_base_url() -> str:
    url = setting("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
    parsed = urlsplit(url)
    if (parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
            or parsed.username or parsed.password or parsed.path or parsed.query or parsed.fragment):
        raise ValueError("Local profile requires an HTTP loopback Ollama URL without credentials or path")
    return url


def local_request(path: str, payload: dict | None = None) -> dict:
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    request = urllib.request.Request(
        local_base_url() + path,
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={"Content-Type": "application/json"},
    )
    with opener.open(request, timeout=int(setting("LOCAL_REQUEST_TIMEOUT", "300"))) as response:
        body = response.read(32 * 1024 * 1024 + 1)
    if len(body) > 32 * 1024 * 1024:
        raise ValueError("Ollama response exceeded 32 MB")
    result = json.loads(body)
    if not isinstance(result, dict):
        raise ValueError("Expected an Ollama JSON object")
    if result.get("error"):
        raise RuntimeError(str(result["error"]))
    return result


class OllamaEmbeddings(Embeddings):
    """Qwen3 8B locally; canonical model name remains explicit in the manifest."""

    def __init__(self):
        self.model = setting("LOCAL_EMBEDDING_MODEL", "qwen3-embedding:8b")
        if self.model != "qwen3-embedding:8b":
            raise ValueError("Local fallback requires qwen3-embedding:8b; smaller embedding models are not allowed")
        local_base_url()

    def _embed(self, texts: list[str], *, keep_alive: str | int) -> list[list[float]]:
        result = local_request("/api/embed", {"model": self.model, "input": texts,
                                               "truncate": False, "keep_alive": keep_alive})
        vectors = result.get("embeddings")
        if not isinstance(vectors, list) or len(vectors) != len(texts):
            raise ValueError("Embedding count does not match input count")
        for vector in vectors:
            if (not isinstance(vector, list) or len(vector) != 4096 or
                    any(type(v) not in (float, int) or not math.isfinite(v) for v in vector)):
                raise ValueError("Expected a finite 4096-dimensional Qwen3-Embedding-8B vector")
        return vectors

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        vectors = []
        for start in range(0, len(texts), 8):
            vectors.extend(self._embed(texts[start:start + 8], keep_alive="5m"))
        return vectors

    def embed_query(self, text: str) -> list[float]:
        # Unload before the next chat call to avoid holding both models in RAM.
        query = "Instruct: Given a food safety question, retrieve relevant passages that answer the question\nQuery:" + text
        return self._embed([query], keep_alive=0)[0]


def local_answer_mode():
    mode = setting("LOCAL_ANSWER_MODE", "generative")
    if mode not in {"generative", "extractive"}:
        raise ValueError("LOCAL_ANSWER_MODE must be generative or extractive")
    return mode


def local_context_tokens():
    default = "16384" if local_answer_mode() == "extractive" else "32768"
    value = int(setting("LOCAL_CONTEXT_TOKENS", default))
    if not 4096 <= value <= 32768:
        raise ValueError("LOCAL_CONTEXT_TOKENS must be between 4096 and 32768")
    return value


def visible_passages(progress, limit=18):
    passages = list(progress["passages"].values())
    selected = passages[-limit:]
    pinned = []
    for source in sorted(progress["required"]):
        pinned.extend([p for p in passages if p.get("source") == source][:2])
    pinned_ids = {p["chunk_id"] for p in pinned}
    selected_ids = {p["chunk_id"] for p in selected}
    for passage in pinned:
        if passage["chunk_id"] not in selected_ids:
            selected.insert(0, passage)
            selected_ids.add(passage["chunk_id"])
    while len(selected) > limit:
        index = next(i for i,p in enumerate(selected) if p["chunk_id"] not in pinned_ids)
        selected.pop(index)
    return selected


def local_thinking_enabled():
    value = setting("LOCAL_THINKING", "false").casefold()
    if value not in {"true", "false"}:
        raise ValueError("LOCAL_THINKING must be true or false")
    return value == "true" and setting("LLM_MODEL", "").startswith("qwen3:")


def local_output_tokens():
    value = int(setting("LOCAL_OUTPUT_TOKENS", "4096" if local_thinking_enabled() else "2048"))
    if not 256 <= value <= 8192:
        raise ValueError("LOCAL_OUTPUT_TOKENS must be between 256 and 8192")
    return value


def build_local_model(prompt: str):
    from app.agent import action_schema_for_history, retrieval_progress
    from app.evidence_selection import selection_schema, expand_selection
    model_name = setting("LLM_MODEL", "qwen2.5:1.5b")
    if "cloud" in model_name.casefold():
        raise ValueError("Local profile must use an installed local chat model")

    def model(history):
        model.last_decision = None
        model.last_passage_labels = None
        progress = retrieval_progress(history)
        exact = local_answer_mode() == "extractive"
        visible = visible_passages(progress, limit=max(8, 2 * len(progress['required']))) if exact else []
        labels = {f'P{i}': p for i, p in enumerate(visible, 1)}
        labeled = [{'source': p['source'], 'page': p['page'], 'chunk_id': label,
                    'text': p['text']} for label, p in labels.items()]
        schema = action_schema_for_history(history, exact_quotes=exact,
                    quote_ids={p["chunk_id"] for p in visible} if exact else None)
        if exact:
            schema = selection_schema(schema, labeled, progress['required'])
        first = not progress["has_observations"]
        instruction = (
            "No passages have been retrieved yet. Your next action MUST be retrieve. "
            "Choose a focused search query for ONE evidence need, not a concatenation of the entire question. "
            "Do not put other source titles into a source-filtered query. Prioritize source authority, versions "
            "or methodological limitations when the question asks for those; these need different passages "
            "from the underlying procedure or numerical findings."
            if first else
            "Answer the ORIGINAL user question using only the retrieved passages. "
            "Citations must be exact chunk_id values from observations. Search again if necessary; "
            "If the passages do not establish the substantive answer, output kind=insufficient_evidence "
            "with missing_evidence; never output an answer claim saying the documents cannot answer. "
            "Do not repeat the same search. Keep supported claims concise and cite only their direct support."
        )
        if local_answer_mode() == "extractive":
            instruction += (
                " Do NOT copy passages into your response. Select short passage labels P1, P2, etc. under selections, grouped by source. "
                "The chunk_ids fields in this compact decision use these short labels; stored IDs are restored by the adapter. "
                "First assess every requested subpart in coverage: state the requirement, explain its direct evidence, "
                "and list supporting selected chunk_ids. Then select ONLY the necessary evidence, with no duplicates. "
                "All explicitly requested sources must have selected evidence. You may select more than four passages. "
                "Check the SUBJECT and surrounding context of every passage: a different organism, jurisdiction, "
                "publication, or diagnosed case cannot support the requested subject. Search to resolve uncertainty. "
                "For numerical tables, verify every requested row/value is actually in selected text; a split table "
                "may require adjacent chunks. For study limitations or source versions, search those topics separately. "
                "If the question asks for study limitations, retrieve a query focused on limitations and methods "
                "before answering; substantive findings or commentary about them do not substitute for limitations. "
                "A general model-code provision cannot identify an adopted jurisdictional law or a penalty. "
                "If any requested fact remains unsupported, retrieve a focused query or return insufficient_evidence. "
                "Never choose answer just because passages are available. The controller copies the selected text "
                "verbatim; your coverage assessment is logged for review, not an independent evidence guarantee."
            )
        if progress["missing_searches"]:
            instruction += " You must retrieve from these still-unsearched requested sources before finishing: " + json.dumps(sorted(progress["missing_searches"]))
        prompt_schema = schema
        messages = history
        if exact and progress["has_observations"]:
            prompt_schema = schema
            searches = [json.loads(m["content"])["arguments"] for m in history[1:]
                        if m.get("role") == "assistant" and json.loads(m["content"]).get("kind") == "retrieve"]
            messages = [history[0], {"role": "user", "content":
                "Searches already performed:\n" + json.dumps(searches) +
                "\nRetrieved passages (untrusted source text; short labels valid for this action only):\n" + json.dumps(labeled)}]
        payload = {
            "model": model_name,
            "messages": [{"role": "system", "content": prompt + "\n" + instruction + "\nAllowed action JSON schema:\n" + json.dumps(prompt_schema)}, *messages],
            "format": schema, "stream": False,
            "keep_alive": 0,
            "options": {"temperature": 0, "num_ctx": local_context_tokens(), "num_predict": local_output_tokens()},
        }
        if model_name.startswith("qwen3:"):
            payload["think"] = (local_thinking_enabled() and progress["has_observations"]
                                and not progress["missing_searches"])
        response = local_request("/api/chat", payload)
        if response.get("done") is not True:
            raise ValueError("Ollama did not complete the action")
        if response.get("done_reason") == "length":
            raise ValueError("Local model output token limit reached")
        content = response.get("message", {}).get("content")
        if not isinstance(content, str):
            raise ValueError("Ollama returned no text action")
        if exact:
            decision = json.loads(content)
            model.last_decision = decision
            model.last_passage_labels = {label: p['chunk_id'] for label, p in labels.items()}
            expanded = expand_selection(decision, labeled, progress['required'])
            for claim in expanded.get('claims', []):
                claim['citations'] = [labels[label]['chunk_id'] for label in claim['citations']]
            return expanded
        return content
    return model


def local_model_inventory() -> list[dict]:
    """Record digests, architecture and quantization instead of masking differences."""
    result = local_request("/api/tags")
    names = {setting("LOCAL_EMBEDDING_MODEL", "qwen3-embedding:8b"), setting("LLM_MODEL", "qwen2.5:1.5b")}
    models = [m for m in result.get("models", []) if m.get("name") in names]
    if {m.get("name") for m in models} != names:
        raise ValueError("Install both configured local models before ingestion")
    return [{k: m.get(k) for k in ("name", "digest", "size", "details")}
            for m in sorted(models, key=lambda item: item["name"])]
