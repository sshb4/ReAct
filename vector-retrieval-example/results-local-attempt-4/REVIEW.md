# Required-query evidence review - November 2, 2026

All nine exact questions were run once under the configuration in
`configuration.json`. The raw `Q1.json` through `Q9.json` results and traces
are unchanged. This is the fourth full local attempt, using exact excerpts.

**Four of nine outcomes are satisfactory after relevance and coverage review.**
Six of nine match the expected terminal reason; that count includes incomplete
answers and must not be reported as six fully passing queries.

| Query | Actual terminal | Evidence and coverage assessment |
| --- | --- | --- |
| Q1 | answer | Satisfactory. Food Code pages 59 and 61 cover exclusion and both return alternatives. Extra neighboring diagnosis provisions make the response verbose. |
| Q2 | answer | Satisfactory. Handbook pages 6 and 7 correctly require stopping, reporting, and leaving immediately, then return no sooner than 24 hours after symptoms end. The previous timing inversion is absent. |
| Q3 | answer | Partial. Three norovirus excerpts cover dose, usual onset, symptoms, and ill-worker handling. A fourth excerpt is from **Other Viral Agents**, page 185, and introduces inapplicable onset/duration information. |
| Q4 | answer | Satisfactory. Table 3-A values and oxygen footnote match visual inspection of Appendix 3 pages 3-4. Background and bibliography excerpts are unnecessary. |
| Q5 | answer | Partial. All four item labels appear, but line 22's rate ratio **1.37 is missing**. Other ratios are correct. Limitations are incomplete and one excerpt is duplicated. |
| Q6 | error | Failed. Both sources were retrieved, but the candidate cited only Food Code excerpts. The controller rejected omission of Bad Bug Book evidence. No final answer was accepted. |
| Q7 | error | Failed. Both sources were retrieved, but the candidate omitted handbook citations and did not explain its older guidance role. The controller rejected it. |
| Q8 | answer | Failed. Generic Food Code passages establish neither a current Utah adoption regulation nor Utah penalties. Required terminal: insufficient_evidence. |
| Q9 | insufficient_evidence | Satisfactory evidence boundary. No ranking is asserted; food-safety observations cannot establish the requested ranking. |

Page numbers above are one-based physical PDF pages.

## Review and verification

`evidence-review.json` records the manual assessment of every query and requested
subpart, bound to each raw result's SHA-256. The reviewer was OpenAI Codex;
this is an assistant assessment, not an independent human or formal entailment
certification. Appendix Table 3-A and the Utah summer table were also inspected
visually; surrounding source text was checked for context and study limitations.

`review-verification.json` records mechanical checks of the exact supplied query
text, shared configuration, result/review hashes, retrieved citation provenance,
quote fidelity, source/page text, step budgets, and recorded code/prompt hashes.
Passing those checks does not establish relevance or complete answers. Error
results contain rejected candidates in their traces, not accepted final claims.

`summary.json` is the unchanged runner output. Its initial review-pending labels
are superseded by the hash-bound assessment in `evidence-review.json`.
`ANSWERS.md` renders the actual outputs with their completed review labels.

## Configuration and limitations

Local Ollama Qwen3-Embedding-8B Q4_K_M; chat qwen3:4b; 1,400-character
chunks with 200-character overlap; six returned passages from 18 semantic
candidates; at most two linked Food Code sections; 16 model/tool invocations;
16,384-token chat context; 4,096-token action output limit; thinking disabled;
up to four verbatim answer excerpts. Full model digests and hashes are recorded.
All 50 offline tests passed again on November 2, 2026.

The exact-excerpt check prevents altered quotations but does not ensure correct
passage selection, coverage, cross-source citation, or abstention. Q3, Q5, Q6,
Q7, and Q8 still need improvement or explicit disclosure as failures. No answers
were edited into successful outputs and no cherry-picked reruns were substituted.

The local fallback remains a disclosed deviation from the required course
services. The FDA Food Code is a model code; the handbook is older guidance,
the Bad Bug Book is pathogen reference material, Appendix 3 is draft nonbinding
guidance, and the Utah study is historical observation. This run does not
establish current Utah law. No repository publication or final PDF was performed.
