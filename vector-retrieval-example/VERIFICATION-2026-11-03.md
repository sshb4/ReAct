# Follow-up: full set completed

The subsequent full nine-query run and review are complete in results-local/. Eight outcomes are satisfactory; Q7 reached its model output-token cap. See results-local/REVIEW.md and the final PDF report for actual outcomes and limitations. No pilot was substituted into that run. The notes below document the earlier pilot verification.

---

# Verification — November 3, 2026

All 59 offline tests passed again. The output is saved in `tests-output.txt`.
No implementation changes were made for this verification.

## Earlier pilot checks

Checked the exact required question, step budget, retrieved citation provenance,
quote fidelity, and source PDF physical-page text for the saved Q3/Q5/Q6/Q7/Q8
pilots. All those mechanical checks passed. Hash-bound details are saved in
`.runtime/pilot-verification-2026-11-03.json`. These checks do not certify answer
completeness or relevance. These pilots use different implementation revisions
and cannot be combined into a single successful required-query run.

The labeled Q3 pilot selects norovirus passages from physical pages 168–170,
covering infective dose, onset, symptoms, and food-worker transmission. It does
not select the unrelated Other Viral Agents passage that weakened attempt 4.
Q6 and Q7 pilots cite both requested sources. Q8 correctly terminates with
`insufficient_evidence`. Those observations do not establish full semantic
success for Q6 or Q7.

## Q5 source and coverage check

The earlier labeled Q5 pilot is incomplete. It omits line 22's 1.37 rate ratio
and does not include the full methods/limitations discussion.

Direct extraction from the supplied Utah PDF establishes the verification targets:

- Physical page 4: line 22, proper cold holding temperatures, 1.37; line 28,
  toxic substances properly identified, stored, and used, 1.15; line 33, proper
  cooling methods used and adequate equipment for temperature control, 1.50;
  line 36, thermometers provided and accurate, 1.23.
- Physical pages 2–4: voluntary data submission, seven of thirteen local health
  departments participating, approximately 85% population coverage, and exclusion
  of inspections with no violations. The seasonal comparison is conditional on
  a violation occurring; it does not directly measure foodborne illness incidence.
- Physical pages 4–5: paper/manual collection and participation constraints;
  inconsistent establishment risk classifications and subsequent recategorization;
  inspection-form differences and line-item translation; one year of observations;
  no precise reasons for marking individual violations; and UDOH's own mapping of
  line items to risk factors/interventions.

A fresh full-page Q5 pilot completed with `answer` in three of sixteen allowed
steps, saved separately in `.runtime/page-pilot-Q5.json`. It selects physical
pages 4 and 5, includes all four item names and ratios, and covers the substantive
limitations listed on those pages. Each selected passage matches the source PDF
after whitespace normalization, each quotation matches retrieved text exactly,
and both page contexts retain their parent chunk identifiers. The exact required
question was preserved. Hash-bound checks and the manual assessment are in
`.runtime/page-pilot-Q5-verification.json`.

Assessment: satisfactory for this pilot, with verbose excerpts and extraneous
surrounding material. The additional population-coverage and zero-violation
exclusion context on earlier methods pages is not included in its answer.

The local Ollama service was stopped and was restarted for this run. No model
download, index rebuild, or application change was needed. The reviewed fourth
full run in `results-local/` remains unchanged. Next: run all nine with the current
fixed configuration and review every actual output; pilot successes are not a
substitute for that evaluation.
