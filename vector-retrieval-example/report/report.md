# ReAct Agent with Vector Retrieval

Sasha Bates | U0-HW-09 | November 3, 2026

## Repository and task

https://github.com/sshb4/ReAct

Project folder: vector-retrieval-example/. The agent answers food-safety questions using the five complete supplied PDFs. Persistent Chroma storage contains 2,652 chunks from 1,110 physical PDF pages. The project includes code, offline tests, exact required-query traces, evidence reviews, and reproducible setup instructions. The existing Sudoku project is preserved.

## Tools, storage and source attribution

A typed retrieve tool accepts a nonblank query and an optional validated source filename. PDF chunks preserve source, one-based physical page, character offset and stable chunk ID. Local retrieval ranks semantic candidates, follows at most two referenced model-code sections, and reconstructs each returned physical page from its stored chunks. Page-context IDs bind source, page, text and parent chunk IDs; original vector records are unchanged.

The bounded ReAct controller records actions, observations and terminal status. One step is one model or tool invocation. Terminal reasons are answer, insufficient_evidence, error and step_limit. Tool arguments and citations are validated. In this local extractive mode, the model selects evidence and assesses requested subparts; the adapter copies selected text verbatim. A valid citation and exact quote establish provenance and fidelity, not relevance or completeness. Every actual output was reviewed against its cited source context.

## One recorded configuration

Embedding: Qwen3-Embedding-8B via local Ollama qwen3-embedding:8b, Q4_K_M, 4,096 dimensions. Chat: qwen3:4b, Q4_K_M. Chunk size/overlap: 1400/200 characters. Retrieval: 6 page contexts from 18 semantic chunk candidates. Budget: 16 model/tool invocations. Chat context: 16,384 tokens; output cap: 8,192 tokens per action, including reasoning. Thinking enabled after mandatory retrievals. Model digests, index version and code/prompt hashes are retained in configuration.json.

This authorized local fallback replaces the required course services and is a disclosed assignment-compliance limitation. No course-service run is claimed.

## Offline tests

All 59 tests passed on November 3, including in the isolated publication checkout. Coverage includes source/page/stable-ID ingestion metadata, typed retrieval arguments and labeled results, rejection of unobserved citations, invocation limits, all four terminal reasons, scripted supported and insufficient-evidence runs, exact quotes, source coverage, page-context lineage and resume integrity. Command: python -m unittest discover -s tests -v. No live model or embedding service is used by these tests.

---

# Required-query outcomes

All nine questions were run exactly as supplied, once each in this fifth full attempt, under the same frozen configuration. Previous attempts are preserved; successful pilots were not substituted. 8 of 9 are satisfactory after evidence and coverage review; 8 of 9 match the expected terminal reason. These are different measures. Complete raw traces and hash-bound per-query assessments are in results-local/.

Q1: answer; complete with attribution weakness. Exclusion and both return alternatives are present on Food Code pages 61 and 388. The exclusion citation is the summary table rather than the requested normative section; excerpts include unrelated conditional rules.

Q2: answer; complete. Handbook pages 6, 7 and 31 cover employee and manager immediate actions and return no sooner than 24 hours after symptoms end, with the table documentation alternative.

Q3: answer; complete. Bad Bug Book pages 168-170 cover the low infective dose, usual onset, symptoms and fecal-oral/vomit contamination of ready-to-eat food. No unrelated organism passage was selected.

Q4: answer; complete with presentation limitation. The selected Table 3-A page contains both organisms and every requested value. Rows were checked visually; the answer quotes the table rather than writing a concise comparison.

Q5: answer; complete. Utah pages 4-5 include all four inspection items and ratios (1.37, 1.15, 1.50, 1.23), plus participation, classification, form-mapping, one-year and missing-reason limitations.

Q6: answer; complete with presentation limitation. Food Code pages 59/61 supply symptom-only exclusion and both return alternatives; Bad Bug Book pages 169/170 explain low dose, shedding, RTE contamination and nursing-home spread. No diagnosis is asserted.

Q7: error; failed: output token limit. The model retrieved both documents but reached its 8,192-token action-output limit at step 5. No final answer was accepted. This is the expected-answer mismatch in this attempt.

Q8: insufficient_evidence; complete: insufficient evidence. Correctly reports insufficient_evidence for current Utah adoption and penalties. It does not treat the FDA model code as adopted Utah law or invent a penalty.

Q9: insufficient_evidence; complete: insufficient evidence. Correctly reports insufficient_evidence because the food-safety passages establish no Avenger ranking. No ranking or supporting factual claims are invented.

Physical page numbers in the review refer to the PDF file, not printed page labels. Mechanical verification checks the exact question, shared configuration, code hashes, trace budget, review hashes, citation provenance, quote fidelity and source-page text. Manual semantic review was performed by OpenAI Codex; it is an assistant assessment, not independent human certification.

---

# Reproduction, limitations and disclosure

## Reproduction

Use Python 3.11 or newer (tested on 3.14.7). From vector-retrieval-example/, install dependencies with uv sync --locked. Obtain the original five PDFs and place them in the repository-root documents/ folder. Copy .env.example to .env for the course configuration, or local.env.example to .env.local for the disclosed local configuration. Keep assigned credentials private.

Course rebuild: uv run python -m app.ingest --source ../documents --rebuild --chunk-size 1400 --chunk-overlap 200. Local rebuild: prefix the same command with HW09_ENV_FILE=.env.local, with Ollama and the configured models installed. An index must match its embedding provider and weights; the local database cannot be reused for a course-service run.

Query: uv run python -m app.ask "your question" --k 6 --max-steps 16. Required set: uv run python -m app.required --k 6 --max-steps 16. Prefix either command with HW09_ENV_FILE=.env.local for local inference. Review verification: python scripts/verify_results.py --results results-local --sources ../documents. The README includes setup, model installation, storage paths and report-generation commands.

## Observed limitations and source roles

The small local model may select irrelevant passages, omit requested details, or misjudge evidence sufficiency. Whole-page excerpts improve table and limitations coverage but are verbose, include unrelated neighboring provisions, and can leave the requested explanation implicit. A pilot passing does not establish whole-suite reliability. Older failed attempts document these weaknesses, and the report identifies any remaining failures in the current attempt.

The 2026 Food Code is an FDA model code, not proof of Utah adoption. The employee-health handbook is operational guidance based on the 2017 edition. The Bad Bug Book is pathogen reference material; Appendix 3 is draft, nonbinding scientific guidance; the Utah study reports historical inspections. The corpus supplies no current Utah adoption regulation or penalties. Character extraction can disrupt tables, so the pathogen table and Utah summer table were also checked visually. Blank pages produce no chunks while preserving physical page numbering.

## AI-assistance disclosure

- OpenAI Codex: materially assisted with implementation, validation, tests, model-run orchestration, source/evidence review, documentation, publication preparation and this report. Verification performed in this work includes 59 offline tests, complete saved model traces, mechanical integrity checks, passage-by-passage PDF comparisons, and PDF layout/structure checks. No independent student code-review confirmation is claimed.
- Ollama chat models (qwen3:4b for the submitted attempt; qwen2.5:1.5b in earlier failed work): selected retrieval actions and final evidence or insufficiency outcomes. Contributions were checked against the exact supplied queries, retrieved passages and source PDF context; failures were retained rather than edited into success.
- Qwen3-Embedding-8B via Ollama: embedded document chunks and search queries for Chroma retrieval. Contributions were checked through full-corpus record/page counts, 4,096-dimensional vector validation, model-digest consistency, retrieved source labels and source-page evidence review.
