# Required-query evidence review - November 3, 2026

This is the fifth full local attempt. All nine exact supplied questions were run once under the frozen configuration in `configuration.json`. Raw results and runner summary are unchanged. Earlier attempts are retained separately.

**Eight of nine outcomes are satisfactory after evidence and coverage review.** Q1-Q6 contain supported requested information; Q8-Q9 correctly return insufficient evidence. Q7 ended in error after its final model call reached the 8,192-token output cap. It used five of sixteen permitted invocation steps; these are different limits.

| Query | Actual terminal | Assessment |
| --- | --- | --- |
| Q1 | answer | Exclusion and both return alternatives are present on Food Code pages 61 and 388. The exclusion citation is the summary table rather than the requested normative section; excerpts include unrelated conditional rules. |
| Q2 | answer | Handbook pages 6, 7 and 31 cover employee and manager immediate actions and return no sooner than 24 hours after symptoms end, with the table documentation alternative. |
| Q3 | answer | Bad Bug Book pages 168-170 cover the low infective dose, usual onset, symptoms and fecal-oral/vomit contamination of ready-to-eat food. No unrelated organism passage was selected. |
| Q4 | answer | The selected Table 3-A page contains both organisms and every requested value. Rows were checked visually; the answer quotes the table rather than writing a concise comparison. |
| Q5 | answer | Utah pages 4-5 include all four inspection items and ratios (1.37, 1.15, 1.50, 1.23), plus participation, classification, form-mapping, one-year and missing-reason limitations. |
| Q6 | answer | Food Code pages 59/61 supply symptom-only exclusion and both return alternatives; Bad Bug Book pages 169/170 explain low dose, shedding, RTE contamination and nursing-home spread. No diagnosis is asserted. |
| Q7 | error | The model retrieved both documents but reached its 8,192-token action-output limit at step 5. No final answer was accepted. This is the expected-answer mismatch in this attempt. |
| Q8 | insufficient_evidence | Correctly reports insufficient_evidence for current Utah adoption and penalties. It does not treat the FDA model code as adopted Utah law or invent a penalty. |
| Q9 | insufficient_evidence | Correctly reports insufficient_evidence because the food-safety passages establish no Avenger ranking. No ranking or supporting factual claims are invented. |

## Review and integrity checks

`evidence-review.json` contains a hash-bound manual assessment of every selected final passage and requested subpart. Reviewer: OpenAI Codex. This is an assistant assessment, not independent human or formal entailment certification. The Appendix Table 3-A and Utah summer table were also checked visually. All page numbers are one-based physical PDF pages.

`review-verification.json` records passing mechanical checks for all nine records and 66 retrieval observations: exact question, shared configuration, implementation hashes, review hashes, trace budgets, citation provenance, quote fidelity, parent chunk labels, and source PDF page text. Q7 passes record-integrity checks while remaining a failed query outcome. Passing these checks does not certify semantic completeness.

`summary.json` is the unmodified runner output. Its initial review-pending labels are superseded by the completed hash-bound review. `ANSWERS.md` renders the actual outputs and review labels. No successful pilot was substituted for Q7.

## Configuration and limitations

Local Ollama Qwen3-Embedding-8B Q4_K_M (4,096 dimensions), qwen3:4b Q4_K_M chat, 1,400-character chunks and 200-character overlap. Retrieval returns six derived page contexts from eighteen semantic chunk candidates, with at most two linked model-code sections. Each page context is reconstructed only from stored chunks and retains stable parent chunk IDs. The index remains unchanged. Chat context: 16,384 tokens. Action-output limit: 8,192 tokens including reasoning. Thinking is enabled after mandatory retrievals. Invocation limit: sixteen model/tool calls. Full model digests and code/prompt hashes are recorded.

All 59 offline tests passed, including in the isolated publication checkout. These test results do not establish live semantic correctness.

Q1 covers exclusion through the Food Code summary table rather than directly selecting the requested normative exclusion section. Q4 quotes the source table rather than synthesizing a comparison. Q6 quotes the appropriate symptom-only rule alongside neighboring conditional diagnosis provisions. All supported answers are verbose whole-page excerpts; some requested explanations remain implicit in the source text. Q7 has no accepted answer; the adapter records its error and preceding observations but does not retain Ollama's truncated reasoning/content.

The authorized local fallback remains a disclosed deviation from the required course services. The FDA Food Code is a model code; the handbook is older 2017-based operational guidance; the Bad Bug Book is pathogen reference; Appendix 3 is draft nonbinding scientific guidance; the Utah study is historical inspection research. These sources do not establish current Utah adoption or penalties.
