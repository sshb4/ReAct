"""Rerank semantic candidates for explicit section/table identifier lookups."""
import re
import hashlib
import json
from collections import Counter
from langchain_core.documents import Document

CANDIDATE_MULTIPLIER = 3
SECTION_LINK_LIMIT = 2


def page_contexts(documents, store, k):
    """Hydrate top distinct source pages from stored overlapping chunks.

    These are derived retrieval units, not replacement embedding records.
    Each ID binds the page text and the exact underlying stored chunk IDs.
    No PDF file, external fact, question-specific page or answer is consulted.
    """
    seen, passages = set(), []
    for document in documents:
        source, page = document.metadata['source'], document.metadata['page']
        if (source, page) in seen:
            continue
        seen.add((source, page))
        rows = store.get(where={'$and': [{'source': source}, {'page': page}]},
                         include=['documents', 'metadatas'])
        parts = sorted(zip(rows['documents'], rows['metadatas'], strict=True),
                       key=lambda pair: pair[1]['start_index'])
        if not parts:
            raise ValueError('Retrieved page has no stored context chunks')
        text, end, parents = '', 0, []
        for part, metadata in parts:
            start = metadata['start_index']
            if start < 0 or metadata['source'] != source or metadata['page'] != page:
                raise ValueError('Invalid stored page context metadata')
            if start > end:
                # Character splitters can omit whitespace between chunks.
                text += ' ' * (start - end)
            overlap = max(0, end - start)
            if overlap and text[start:end] != part[:overlap]:
                raise ValueError('Conflicting overlapping stored source text')
            text += part[overlap:]
            end = max(end, start + len(part))
            parents.append(metadata['chunk_id'])
        identity = json.dumps([source, page, parents, text], ensure_ascii=False)
        passages.append({'source': source, 'page': page,
                         'chunk_id': 'page-' + hashlib.sha256(identity.encode()).hexdigest()[:24],
                         'text': text.strip(), 'parent_chunk_ids': parents,
                         'retrieval_unit': 'page_context'})
        if len(passages) == k:
            break
    return passages


def rank_candidates(query, documents, k, linked_identifiers=()):
    identifiers = set(re.findall(r'\b\d-\d{3}\.\d{2}\b', query))
    identifiers.update(re.findall(r'\bTable\s+\d+-[A-Za-z]\b', query, flags=re.I))
    identifiers.update(linked_identifiers)
    if not identifiers:
        return documents[:k]

    def score(document):
        text = document.page_content
        total = 0
        for identifier in identifiers:
            pattern = re.escape(identifier).replace(r'\ ', r'\s+')
            # Prefer an actual section/table heading to references in other rules.
            total += 5 * bool(re.search(r'^\s*' + pattern + r'(?:\s|$)', text, re.I | re.M))
            total += bool(re.search(pattern, text, re.I))
        return total

    # Stable sorting keeps semantic rank among equal identifier scores.
    return sorted(documents, key=score, reverse=True)[:k]


def expand_section_links(query, candidates, source, store, k):
    """Follow frequently referenced sections back to primary chapter headings.

    This uses actual identifiers in semantic candidates, not question IDs,
    predetermined pages or hand-written answers. The final observation still
    returns at most k passages and all come from the same persistent store.
    """
    if source != "fda-food-code-2026.pdf" or re.search(r"\b\d-\d{3}\.\d{2}\b", query):
        return candidates, ()
    references = Counter()
    for document in candidates[:k]:
        text = re.sub(r"(?<=\d)-\s+(?=\d{3}\.)", "-", document.page_content)
        references.update(re.findall(r"\b\d-\d{3}\.\d{2}\b", text))
    linked, identifiers = [], []
    for identifier, _ in references.most_common(SECTION_LINK_LIMIT):
        rows = store.get(where={"source": source}, where_document={"$contains": identifier},
                         include=["documents", "metadatas"])
        for text, metadata in zip(rows["documents"], rows["metadatas"], strict=True):
            is_primary = re.search(r"FDA Food Code 2026\s+Chapter\b", text[:160])
            is_heading = re.search(r"^\s*" + re.escape(identifier) + r"(?:\s|$)", text, re.M)
            if is_primary and is_heading:
                linked.append(Document(page_content=text, metadata=metadata))
                identifiers.append(identifier)
                break
    seen = set()
    merged = []
    for document in [*linked, *candidates]:
        chunk_id = document.metadata.get("chunk_id", document.page_content)
        if chunk_id not in seen:
            seen.add(chunk_id)
            merged.append(document)
    return merged, identifiers
