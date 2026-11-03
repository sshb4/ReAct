# HW-09: ReAct agent with vector retrieval

This implementation adapts the supplied Lecture 170 example. It ingests the five
complete homework PDFs into persistent Chroma using Qwen3-Embedding-8B, then
executes a bounded model/action/retrieval loop. Source text is evidence, not agent
instructions. The assignment requirements are described in the materials package's
`req.md` (included as `assignment-requirements.md` in the published project).

## Authorized local fallback

The separately configured Ollama fallback is documented in [LOCAL-RUN.md](LOCAL-RUN.md).
It preserves the required embedding-model family, but changes the inference
services, quantization, and chat model; these differences are disclosed in its
recorded configuration. It is not a fully compliant course-service run.

## Setup

Python **3.11 or newer** is required (verified with Python 3.14). Install `uv`, then
run from `vector-retrieval-example/`:

```sh
uv sync --locked
cp .env.example .env
```

Set both API keys in your local `.env` to your assigned course credential. Keep
the supplied embedding and chat endpoints and models. Connect to the approved
course network; these are classroom HTTP services. Never put credentials in
query text, traces, or source control.

Keep the complete supplied PDFs in `../documents/`. Do not use the lecture's
unrelated sample-document download list. This repository excludes PDFs, `.env`,
virtual environments, Chroma storage, and generated ingestion manifests.

## Rebuild the complete corpus

```sh
uv run python -m app.ingest --source ../documents --rebuild \
  --chunk-size 1400 --chunk-overlap 200
```

This checks all five filenames and their expected physical page counts (1,110
total), extracts every page, and embeds nonempty page text in batches of 32.
Chunks never cross physical pages. Metadata includes source filename, one-based
physical PDF page, source hash, character offset, and a stable chunk identifier
hashed from filename, source hash, page, offset, and text. Blank pages retain
their physical position but produce no chunks. The manifest records the actual
embedding model, chunk settings, source hashes, page counts, and index version.
`--rebuild` replaces the database at the selected `--db` path.

Default runtime paths are `chroma_db/` and `manifest.json` inside this project.
Rebuild after changing chunk settings or source documents.

## Ask a question

```sh
uv run python -m app.ask \
  "According to the Bad Bug Book, what are the characteristic symptoms of norovirus?" \
  --k 6 --max-steps 16 --output results/example.json
```

`retrieve` has a typed query and optional exact source filename. Result count
is fixed by the run configuration; the model cannot change it. Each passage
contains text, source, page, and chunk ID. The model returns schema-validated
JSON actions: `retrieve`, `answer` (one or more cited claims), or
`insufficient_evidence` (missing evidence). Multiple searches permit cross-source
questions. All model actions, tool arguments, observations, errors, and the
terminal reason are recorded in JSON.

One step means one attempted model call or retrieval call. The default budget
is 16 total invocations, including failures. The controller stops before an
operation would exceed the budget. Terminal reasons are exactly `answer`,
`insufficient_evidence`, `error`, and `step_limit`. Invalid JSON/actions, tool
arguments/results, unknown citations, and service failures produce `error`.

Each answer claim must cite a chunk returned during that specific run. The
returned evidence maps those IDs to filenames and physical PDF pages. This
checks provenance, **not semantic entailment**. Review every claim against the
cited passage; a valid chunk ID alone does not prove a claim is supported.

## Run all required queries

Use the same corpus build and configuration for all nine:

```sh
uv run python -m app.required --k 6 --max-steps 16
```

This preserves each question's supplied text, including internal line breaks
and Markdown emphasis. It saves `results/Q1.json` through `results/Q9.json`,
`configuration.json`, and `summary.json`. Traces include complete passage text.
Commit the real results after review. The summary compares actual and expected
terminal reasons but deliberately marks semantic claim review as pending.
Q1–Q7 should answer; Q8–Q9 should report insufficient evidence. Do not relabel
failed runs or invent successful traces.

When reviewing, check all of the following:

- Q1: Both requested 2026 model-code sections, including return conditions.
- Q2: Employee and manager actions and earliest return from the older handbook.
- Q3: Dose, incubation, symptoms, and ready-to-eat contamination mechanisms.
- Q4: Both organisms and every requested Table 3-A parameter and unit. PDF table
  extraction can scramble columns; compare against the source PDF visually.
- Q5: All four inspection line items, their rate ratios, and study limitations.
- Q6: Symptom-based exclusion and return conditions in a nursing home; do not
  invent a norovirus diagnosis or apply diagnosis-only rules.
- Q7: 2026 FDA model code controls that model-code question; handbook remains
  operational guidance based on the 2017 edition.
- Q8: Corpus does not establish current Utah adoption or penalties.
- Q9: Corpus does not establish an Avenger ranking.

Appendix 3 is draft nonbinding scientific guidance; Bad Bug Book is pathogen
reference; Utah results are historical observations. The FDA model code is not
itself proof of Utah law.

## Offline tests

```sh
uv run python -m unittest discover -s tests -v
```

These tests need installed dependencies but never call live model or embedding
services. They cover metadata and stable IDs, blank physical pages, tool
validation and labeled observations, citations scoped to a run, both invocation
bounds, malformed output/service errors, all four terminal reasons, and
scripted supported and insufficient-evidence cases. The supported fixture has
an intentionally explicit passage/claim pair for human-verifiable entailment.
It is a substitute fixture, not a real homework query result.

## Completion status and limitations

The local corpus index is complete: 2,652 chunks from all 1,110 physical pages.
All 59 offline tests passed on November 3, 2026. Recorded local results, complete
traces, hash-bound evidence assessments and review checks are included in
`results-local/`. The result directory's `REVIEW.md` is authoritative about
which answers are complete and supported; expected terminal reasons alone do
not establish semantic success. Earlier full attempts are retained separately.

These results use the explicitly authorized local fallback and do not establish
compliance with the required course-service configuration. A course-service run
requires assigned keys, course-network access, and a separately built index.
Semantic retrieval can miss needed sections; character chunking
can divide tables and rules; the model may output invalid JSON or unsupported
claims. The controller enforces provenance and bounds but cannot establish
semantic correctness automatically.

The final submission also needs an instructor-accessible Git repository and an
accessible PDF named `lastname-firstname-vector-retrieval.pdf`, with the repository
URL, actual configuration, test results, all nine observed outcomes, limitations,
and AI-assistance disclosure. The final report is saved under
`output/pdf/bates-sasha-vector-retrieval.pdf`, with its editable source in
`report/report.md`. Canvas submission must be completed by the student.

## Recheck recorded results

After installing dependencies, verify the result records offline:

```sh
python scripts/verify_results.py --results results-local --sources ../documents
python -m app.render_results --results results-local
```

The first command checks the exact questions, configuration, implementation
hashes, trace accounting, citation provenance, quote fidelity, source-page text,
and review hashes. Omit `--sources` if the supplied PDFs are unavailable; it will
then explicitly record that PDF text was not checked. It does not independently
judge whether a passage answers the question.

To rebuild the report, separately install `reportlab`, `pypdf`, `pymupdf`, and
`pillow`, then run `python scripts/build_report.py`. Report generation is optional
and does not change the application lockfile.
