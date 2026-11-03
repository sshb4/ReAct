# Latest verification - November 3, 2026

All **59 offline tests passed**, including in the isolated publication checkout. The complete fifth local run and evidence review are finished: **8/9 satisfactory**, with Q7 failing at its 8,192-token action-output cap. All nine records passed integrity checks across 66 retrieval observations, including comparison with source PDF text. See [the current review](results-local/REVIEW.md) for semantic assessments and caveats. Previous checkpoints below are historical; the fourth full attempt is preserved in results-local-attempt-4/.

---

# Latest verification - November 2, 2026

All **50 offline tests passed** again (`.venv/bin/python -m unittest discover -s tests -v`).
All nine revised local runs and manual evidence reviews are complete. Only Q1,
Q2, Q4 and Q9 are satisfactory; do not equate passing offline tests or matching
terminal reasons with supported, complete required-query answers. See
[the current evidence review](results-local/REVIEW.md). All nine mechanical
record/provenance/quote/source-page checks passed across 72 observations.

---

# Latest checks — October 31, 2026

**44 offline tests pass.** Full local index: 2,652 chunks from all 1,110 pages.
Two earlier model attempts are preserved and their weaknesses documented. A new
nine-query run is in progress using source-coverage enforcement, linked primary
rules, Qwen3 4B reasoning, and one recorded configuration. Do not treat a returned
answer or terminal-reason match as completed semantic review.

---

# Latest verification — October 31, 2026

**35 offline tests pass.** Full local ingestion is complete: 2,652 chunks from
all 1,110 physical corpus pages. The first nine model runs all failed and are
preserved in results-local-attempt-1. After adapter fixes, a Q1 pilot correctly
cites exclusion and return conditions, but Q9 still makes an unsupported claim
with a real, irrelevant citation. Thus the required-query set has NOT passed.
A stronger chat model and a new complete recorded run are pending storage space.

---

# Latest verification — October 30, 2026

**32 offline tests pass** with no live service calls. `tests-output.txt` contains
the latest output. New tests cover structured action alternatives, local model
adapters, completed-index readiness, and interruption/resume without duplicate
embedding work.

Real local smoke checks also passed for Qwen3-Embedding-8B (4,096 dimensions,
unit norm) and a schema-valid qwen2.5:1.5b action. The full index build and nine
required-query runs are still in progress/queued; these smoke checks do not
establish required-query success or semantic claim support.

---

# Verification — October 28, 2026

Environment: Python 3.14.7, dependencies from `uv.lock`.

Command: `python -m unittest discover -s tests -v` (project virtual environment).

Result: **21 tests passed**, no live model or embedding calls. Includes a real
local Chroma persistence/source-filter test with deterministic substitute
embeddings, as well as the controller and ingestion tests described in README.

A separate local extraction check read all five supplied PDFs with 1,400-character
chunks and 200-character overlap. It confirmed 1,110 physical pages, 2,652 chunks,
unique chunk identifiers, and one-based physical page metadata. Food Code had
729 pages with extractable text out of 732 physical pages; all pages of the other
four sources had text. The Utah PDF initially warned that fonttools was missing.
After adding the dependency, its extraction was rechecked: 31 chunks across all
18 pages, with no font parser warning.

These checks do not demonstrate live embedding quality or required-query answer
quality. No course-service ingestion or required query runs have been performed.
Those require the assigned credentials and course-network access. Claims in
actual required-query results still require review against their cited passages.

## Local fallback verification — October 30, 2026

After adding the explicit local profile, 29 offline tests pass (see tests-output.txt).
New coverage verifies loopback-only URLs, no Golem credential use, structured
chat schema, embedding batch size and validation, query instruction/unloading,
model inventory ordering, profile isolation, and embedding digest matching.
These offline tests do not constitute real model-query results.
