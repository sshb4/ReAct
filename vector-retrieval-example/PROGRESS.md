# Final package - November 3, 2026

The fifth frozen full run and evidence review are COMPLETE. Q1-Q6 have supported answers, Q8-Q9 correctly report insufficient evidence, and Q7 ends in an output-token-limit error. Eight of nine outcomes are satisfactory. All nine records passed mechanical verification over 66 retrieval observations, with source PDF comparison. Raw outputs and runner summary are unchanged; attempt 4 is archived in results-local-attempt-4/.

All 59 offline tests passed, including in the isolated GitHub checkout. The three-page tagged report is output/pdf/bates-sasha-vector-retrieval.pdf; all rendered pages and PDF structure links were checked. The editable source and audit evidence are in report/. Intended publication: https://github.com/sshb4/ReAct under vector-retrieval-example/. Existing Sudoku files are preserved. The local course-service deviation and Q7 failure are disclosed. Canvas upload remains the student's final submission step. Earlier entries below are historical checkpoints.

---

# Final run, publication and report — November 3, 2026

User explicitly authorized the full nine-query run, review, GitHub publication
and final PDF report. Work is ACTIVE. No further publication confirmation needed.

- Full frozen run is exec session 14103, command app.required --k 6 --max-steps 16
  --output results-local-attempt-5, HW09_ENV_FILE=.env.local. Q1–Q4 have completed
  with answer. Their manual hash-bound assessments are being saved progressively
  in results-local-attempt-5/evidence-review.json. All four satisfactory with
  attribution/presentation caveats. Q5 now running. Do not alter app/*.py/settings
  during this run. All remaining questions must come from THIS run, not pilots.
- Ollama daemon session 68576. Local inference is slow (several minutes per query).
  The existing reviewed results-local/ still contains attempt 4 unchanged.
- Isolated GitHub checkout: ../submission-repo, cloned from public sshb4/ReAct.
  gh access works with escalation; sandbox gh auth status misleadingly said
  invalid token. Existing repo is Sudoku project: preserve all existing files.
  New project belongs in vector-retrieval-example/ subfolder. Root README has a
  new link section; root .gitignore now excludes supplied documents/*.pdf.
- Prepared source files copied into checkout; 59 tests PASS there as well as in
  original. Credential scan of prepared files passed (no values printed).
- Added scripts/verify_results.py (offline integrity checks), build_report.py
  (tagged PDF + rendering), write_report_source.py (requires complete reviews
  with per-query report_summary). These are documentation/review helpers only;
  frozen app implementation unchanged. Copy helpers again at final packaging.
- PDF skill read. Isolated artifact deps installed in /private/tmp/hw09-pdf-deps;
  use PYTHONPATH=/private/tmp/hw09-pdf-deps .venv/bin/python scripts/build_report.py.
  Source table PNGs in tmp/pdfs/ inspected: Appendix physical pp3–4 and Utah p4.
  Final PDF must be visually inspected before delivery. Report builder writes
  output/pdf/bates-sasha-vector-retrieval.pdf + report/accessibility-check.json.
- report/corpus-index-audit.json verifies actual DB 2,652 records and all five
  source hashes/page counts. No downloads/reindex. Last available disk ~470MiB
  while inference swaps; don't download models/delete user files.
- NEXT: finish remaining runs, read each actual answer and assess each requested
  subpart. Finish evidence-review.json status=complete and report_summary per Q.
  Archive original results-local/ as results-local-attempt-4/, promote new
  results-local-attempt-5/ to results-local/ without editing raw result JSON.
  Run scripts/verify_results.py --results results-local --sources ../documents;
  fix verifier issues honestly if needed. Render ANSWERS.md. Write REVIEW.md,
  update TEST-RESULTS/README/PROGRESS. Compose report source with helper, build,
  inspect all PNGs and record visual review. Copy project/results/report/artifact
  into checkout excluding .env, PDFs corpus, chroma, runtime, venv and tmp. Retain
  earlier attempts. Include only intended final report PDF. Run final tests and
  secret/artifact scan, commit scoped files and push main. Verify remote commit
  and report availability. User must upload final PDF to Canvas manually.

---

# Verification checkpoint — November 3, 2026

User requested verification. Completed: 59 offline tests pass again; fresh
tests-output.txt saved. Earlier pilot citation/quote/source-page checks pass,
with hash-bound details in .runtime/pilot-verification-2026-11-03.json.

Fresh full-page Q5 pilot completed in 3/16 steps with answer. All four ratios
(1.37, 1.15, 1.50, 1.23) and substantive limitations appear in selected Utah
physical pages 4–5. Exact question, citations, quote fidelity, PDF text, and
parent chunk lineage checked. Saved .runtime/page-pilot-Q5.json and
.runtime/page-pilot-Q5-verification.json. See VERIFICATION-2026-11-03.md for
assessment and limits. No application changes. Current results-local/ remains
the unchanged reviewed fourth full attempt; full revised Q1–Q9 evaluation is
still outstanding. Next: run all nine with one fixed current configuration and
review every output; archive attempt 4 before replacing results-local/.

Ollama was stopped and restarted in exec session 68576. Q5 process completed.
No downloads or reindex performed. Free disk at check: approximately 4 GiB.

---

# Active improvement work - November 2, 2026

User said "ok lets go" after the reviewed fourth full attempt had five weak cases.
Goal: fix those cases, run ALL NINE together under one fixed configuration, and
review every output. No repository publication or final PDF is currently requested.

- 59 offline tests PASS, current tests-output.txt saved.
- Implemented compact local selection decisions with requirement coverage analysis,
  short P1/P2 labels, required per-source selection fields, duplicate/unselected-ID
  checks, exact text expansion, and raw decision plus label-map trace entries.
- app/evidence_selection.py is new; its hash and retrieval.py hash are now recorded.
- Added local whole-physical-page retrieval contexts reconstructed only from stored
  chunks. Stable page-* IDs bind source/page/text/parent_chunk_ids; original vector
  records are unchanged. k=6 now counts local page contexts. Course mode stays chunk
  retrieval. Eight visible contexts with at least first two per requested source.
- Actual reconstruction of Utah pp4/5, Bad Bug pp168/169/170/185, Food Code pp59/61
  matches source PDF text after whitespace normalization. Tests cover overlap conflicts,
  stable lineage IDs, source coverage, quote mapping, duplicates and trace accounting.
- .env.local and local.env.example: thinking=true, output8192, timeout600, ctx16384.
  Required Qwen3 8B embeddings and qwen3:4b chat; NO downloads/reindex done.
- Earlier compact pilots .runtime/compact-pilot-Q6.json and Q8.json improve their
  prior failures, but Q5 still incomplete. Labeled pilots: Q5 still incomplete;
  Q7 succeeds with both sources and 2017/2026 distinction.
- The OLD labeled-pilot process (exec session 78343) is still finishing Q3. It loaded
  code BEFORE page-context retrieval was added; its config hashes correctly reflect
  that earlier code. Poll it; do not treat its outputs as the new full-page run.
- Ollama daemon session 53615 runs on loopback. Server is active but local inference
  is slow. Last checked free storage only ~703MiB; do NOT download models/delete files.
- NEXT: finish inspecting labeled Q3; run a NEW full-page Q5 pilot with fresh Python.
  If needed improve generically (no question IDs/fixed answers/pages in policy).
  Once pilot evidence covers all Q5 ratios AND full study limitations, preserve
  results-local/ as results-local-attempt-4/, start app.local_pipeline for all nine
  using the current frozen implementation. No cherry-picked per-query substitution.
- Then review ALL outputs against their source pages, record hash-bound
  evidence-review.json, review-verification.json, REVIEW.md, render ANSWERS.md,
  and update pipeline semantic_review and this checkpoint. Current results-local/
  still contains the unchanged reviewed FOURTH full run (4 satisfactory, Q3/Q5
  partial, Q6/Q7 errors, Q8 wrong terminal). Do not overwrite without archiving.
- PDF skill was read and used earlier; Appendix Table3-A/Utah table were visually
  checked from .runtime/pdf-review/*.jpg. Source text cache in
  .runtime/evidence-source-text/. No external law should be substituted into Q8.

---

# Current checkpoint - November 2, 2026

User requested steps 1 and 2 only: full revised run and evidence review.
Both are COMPLETE. No repository publication or final PDF was performed.

- All nine exact queries completed with ONE fixed extractive local configuration.
- Current results are in results-local/; older attempts remain unchanged.
- Manual relevance/coverage review is COMPLETE and SHA-256 bound to each result.
- Satisfactory: Q1, Q2, Q4, Q9 (4/9).
- Partial: Q3 selects an Other Viral Agents excerpt as norovirus evidence;
  Q5 omits line 22 ratio 1.37 and several limitations, with a duplicate excerpt.
- Errors: Q6 omits Bad Bug Book citations; Q7 omits handbook citations.
  Both sources were retrieved in each case; the controller rejected the candidates.
- Wrong terminal: Q8 answers with generic model-code material instead of
  insufficient_evidence about Utah adoption and penalties.
- Six of nine expected terminal matches is NOT six fully passing answers.
- All 50 offline tests passed again. Mechanical checks passed for all nine
  original question texts, one shared configuration, result/review hashes,
  citation provenance, exact quotes, 72 observed passage source/page matches,
  step budgets, and unchanged recorded controller/adapter/prompt hashes.
- Read results-local/REVIEW.md, evidence-review.json, review-verification.json,
  and ANSWERS.md. summary.json retains original review-pending labels; the
  hash-bound review supersedes them. Pipeline state now says review complete.
- Index remains complete: 2,652 chunks; do not rebuild. No code/prompt/config
  changes were made during this run and no per-query replacements substituted.
- Configuration: qwen3:4b, exact excerpts (up to 4), thinking false, context
  16384, output 4096, chunk 1400/200, k=6 (18 candidates), max_steps=16.
- Local fallback deviation remains disclosed. Pending work: improve the five
  unsatisfactory cases if desired, then repository and final PDF submission.

---

# Current fixed-configuration run — October 31, 2026

INDEX COMPLETE. Do not rebuild. 2,652 stored chunks; required embeddings unchanged.

- New full nine-query run is active in exec session 90659 (app.local_pipeline).
- Current code and prompt are FROZEN for this run; do not change them mid-run.
- 44 offline tests PASS (tests-output.txt). Tested named-source coverage in
  generation and runtime, reasoning after retrieval, and same-source section links.
- Chat: qwen3:4b, reasoning enabled only after initial/required-source searches,
  4,096 max output tokens, 32,768 context. Saved .env.local and public sample match.
- Retrieval: 18 semantic candidates for k=6; up to 2 stored primary Food Code
  section headings followed from references; six returned passages. No external
  facts, fixed answers, or hard-coded query IDs/pages added to retrieval.
- Record configuration includes system-prompt, controller and local-adapter hashes.
- Earlier attempts retained under results-local-attempt-1/ and
  results-local-attempt-2/. Attempt 2 has honest evidence-review.json identifying
  weaknesses despite mostly matching terminal reasons.
- Reasoning Q6 pilot (.runtime/reasoning-pilot-Q6.json) uses both requested sources
  and no longer applies diagnosed-norovirus return rules; it omitted a documented
  noninfectious-condition alternative, motivating linked normative-rule retrieval.
- Separate local model reviewer probe was UNRELIABLE (misclassified Q1 and Q6)
  and is NOT deployed or trusted as evidence verification. Do not claim otherwise.
- New results-local/ is the CURRENT run; wait for all nine and manually evaluate
  every claim and requested subpart. Raw model outputs must not be edited into
  successful answers. Add evidence-review.json/REVIEW.md bound to result hashes.
- User freed storage; chat model downloaded successfully. Last free space about
  5.2 GiB. No further model downloads or network troubleshooting currently needed.
- No Git publication/final PDF done. Existing intended repo URL from user file is
  https://github.com/sshb4/ReAct. Ancestor home repo exists; don't stage home files.

---

# Current live run — October 31, 2026

- User freed space: verified 9.9 GiB before downloading.
- qwen3:4b was downloaded successfully with SHA verification.
- .env.local and local.env.example now select LLM_MODEL=qwen3:4b; course .env untouched.
- No embedding rebuild: same complete 2,652-record Qwen3-Embedding-8B index.
- 37 offline tests PASS, latest output saved in tests-output.txt.
- Current full Q1-Q9 run is active in exec session 98700 via app.local_pipeline.
  New results will be in results-local/. Prior first-attempt failures remain in
  results-local-attempt-1/ and pilot failures in .runtime/.
- Pilot Q1 with Qwen3 was factually correct but included one overly broad citation.
  Pilot Q9 correctly stated that the docs do not establish the ranking but used
  answer rather than insufficient_evidence. Both issues were addressed in the
  prompt before the CURRENT full run; do not claim current set passed until checked.
- Current retrieval uses semantic candidate pool k*3 (18 for k=6), with a generic
  exact section/table identifier heading boost before returning six passages.
  This policy is recorded in configuration; it does not hardcode question answers.
- Local action schema enforces retrieve before any final and limits citation IDs
  to retrieved observations. Dynamic schema also appears in the model prompt.
- Explicit policy now distinguishes insufficient support from substantive answers.
- Qwen3 uses think:false, context 32768, max output 2048 per model action.
- Next: inspect all actual query outcomes and claim support. Preserve failed attempts.
- No new model download, reindex, Git publication or final PDF is needed to inspect
  current progress. Run `.venv/bin/python -m app.local_status` to see saved results.

---

# Current checkpoint — October 31, 2026

INDEXING IS COMPLETE: all 2,652 chunks from 1,110 physical pages are saved in
chroma_local/. manifest.local.json is present. DO NOT REBUILD the index for a
chat-model upgrade; embedding weights/digest are unchanged.

- First nine real runs completed October 30 but all ended in error. Preserved
  as results-local-attempt-1/ (renamed from results-local/). Eight attempted
  answers before retrieval and were rejected for invented citations. Q6 hit
  the model output token limit. These are not passing query results.
- Fixed local generation to require retrieval before a final action and restrict
  citation enums to observed IDs. Runtime provenance validation is retained.
- Found/fixed another adapter issue: include dynamic JSON schema in system
  prompt as well as decoder format, per official Ollama structured-output docs.
- Pilot .runtime/pilot2-Q1.json now gives a correct, source-supported exclusion
  and 24-hour/noninfectious-medical-documentation answer.
- Pilot .runtime/pilot2-Q9.json still hallucinates an Avenger ranking, citing
  unrelated real Food Code passage IDs. Valid provenance is not entailment;
  this is a FAILED semantic review, not a passing answer.
- 35 offline tests PASS; tests-output.txt is current. Includes evidence-aware
  generation, original-question spoof rejection, schema grounding and Qwen3
  thinking-off payload.

NEXT CHAT MODEL: qwen3:4b, official Ollama size ~2.5 GB. Native adapter now
supports think:false for qwen3 chat and stronger food-safety-only instruction.
app.local_setup accepts --model qwen3:4b and checks disk headroom. Existing
.env.local STILL selects qwen2.5:1.5b until new model is downloaded successfully.
Do not claim the new chat model has been installed or tested yet.

BLOCKER: storage dropped to 1.7 GiB free. Asked user asynchronously to free about
5 GB more; answer pending. Do not delete personal files or existing models.
When enough storage is verified, run (with appropriate escalation):
`env HW09_ENV_FILE=.env.local .venv/bin/python -u -m app.local_setup --model qwen3:4b`.
Then change only LLM_MODEL in .env.local to qwen3:4b, smoke-test, and rerun all
nine with one configuration. Preserve actual failures and manually review all
claim/passages. No source-embedding rebuild is needed.

No Golem network retries needed. Local fallback remains explicitly authorized
and disclosed as a deviation from the course-service requirement. Course .env
is untouched. No final report or Git publication has been performed. Note:
`git status` from this workspace resolves an ancestor home-directory repository;
do not stage unrelated home files or publish from that ancestor repo. Use a
project-specific checkout if publication is later requested.

---

# Latest continuation check

User requested continuing indexing. The original ingestion job (session 37127)
and query queue (session 15102) are still running; no duplicate jobs were started.
Last verified saved count: 1,440 / 2,652 chunks (about 54%). Complete manifest
is not present yet. Queue remains waiting_for_index and will launch the nine
local queries after indexing completes. Build recovery journal is present.

---

# Current running jobs — October 30, 2026, about 2:15 p.m. MDT

LOCAL SETUP IS WORKING. Real embedding and structured chat smoke checks passed.
32 offline tests pass; latest tests-output.txt is saved.

- Full 2,652-chunk index build is running in exec session 37127; last observed count 256.
- Ollama daemon runs in exec session 79228, serving loopback only.
- Automatic query queue runs in exec session 15102. It waits for the full manifest, then runs Q1-Q9 under one configuration and writes results-local/.
- Queue state: .runtime/local-pipeline-state.json; log: .runtime/local-pipeline.log.
- Inspect actual progress with `.venv/bin/python -m app.local_status` from the project directory.
- Estimated total local indexing time at observed pace: about 1-2 hours. This is an estimate, not a completion claim.
- New resume support is implemented and tested. A matching manifest.local.building.json journal was saved for the CURRENT running build. An interruption can resume without re-embedding stored chunks.
- After restart: start Ollama, run `HW09_ENV_FILE=.env.local .venv/bin/python -u -m app.ingest --source ../documents --resume --chunk-size 1400 --chunk-overlap 200`, then restart app.local_pipeline in another session.
- Downloaded embedding digest: 64b933495768fbd3b87c20583d379728a07471e0c66733a9df87cd1901b3c44b. The installed GGUF quantization is Q4_K_M. Existing chat is qwen2.5:1.5b.
- Model output generation uses a mutually exclusive three-variant action schema; Action runtime validation also remains enforced.
- Source-table visual review: rendered Appendix 3 physical page 3 and Utah study physical page 4 using pypdf + native sips JPEG rendering, then inspected images. Temporary artifacts in .runtime/pdf-review/.
- No required-query results or full index completion have been claimed. When queue finishes, inspect every result/trace and review claim support, especially Q4 table fields and Q5 rate ratios. The small chat model may need replacement after actual result assessment.
- User has authorized local fallback; do not repeat Golem troubleshooting or ask user to contact other people.
- Golem .env remains untouched. Local fallback is disclosed as a deviation from the required course service configuration.

---

# Live local setup status — October 30, 2026

- Download completed and SHA verified for qwen3-embedding:8b (digest 64b933495768fbd3b87c20583d379728a07471e0c66733a9df87cd1901b3c44b).
- Real embedding smoke check PASSED: 4096 dimensions, unit norm.
- Real qwen2.5:1.5b chat smoke check PASSED after strengthening the action generation schema.
- Action schema now expresses three mutually exclusive object shapes; runtime Action validation remains enforced.
- 30 offline tests PASSED, latest output saved in tests-output.txt.
- Full local ingestion has started (1400 chars / 200 overlap); not yet confirmed complete.
- Ollama daemon started in exec session 79228; ingestion exec session 37127. If sessions no longer exist, check local server and manifest/database state rather than assume completion.
- Next: finish ingestion, run actual required queries with one recorded configuration, evaluate small chat model and review every citation.
- Current .runtime/local-smoke.json is a real smoke-check artifact, not one of the required-query results.

---

# Latest checkpoint — local setup resumed October 30, 2026

- Storage after restart: 24 GiB free (download started only after verifying this).
- Ollama 0.40.6 daemon started on 127.0.0.1:11434 with absolute bundled CLI.
- Qwen3 embedding 8B download currently running via app.local_setup (not yet verified complete).
- 29 offline tests now pass; tests-output.txt contains latest output.
- Added dedicated tests for local embedding batches/vectors, schema chat, no credential leakage, loopback isolation, stable inventory order, and manifest/digest validation.
- Sorted inventory; chat model may be changed without rebuilding vectors when embedding digest is unchanged.
- Added Qwen's recommended query instruction prefix; exact prefix and runtime settings are recorded.
- Added LOCAL-RUN.md and app.local_setup download helper.
- Next: finish download, real local embedding/chat smoke tests, full ingestion, nine recorded runs and claim review.
- Golem .env remains unchanged. No new network troubleshooting or user contact requests needed.

---

# HW-09 checkpoint — October 30, 2026

## Current user direction

The user authorized a local fallback after Golem repeatedly timed out. They understand that local execution differs from the required course-service configuration and is not fully compliant as written. They are freeing at least 8 GB and are restarting their Mac. Resume local setup after the restart; do not repeat the full network troubleshooting sequence.

## Saved files and credentials

Project: `vector-retrieval-example/`.

- Original course credentials/settings remain in the ignored `.env`. Never print keys.
- New local settings are in ignored `.env.local`, with a public `local.env.example`.
- Select local mode with `HW09_ENV_FILE=.env.local` before launching Python.
- Local mode uses separate `chroma_local/`, `manifest.local.json`, and `results-local/` paths.
- No Git commit or publication has been performed in this workspace.
- User-created `bates-sasha-vector-retrieval.md` says intended repository is https://github.com/sshb4/ReAct; do not overwrite this file or assume anything has been published.

## Finished before local fallback

Bounded ReAct controller, strict action/tool/citation validation, all four terminal reasons, action-observation traces, complete-corpus ingestion, and exact nine-query runner implemented.

21 offline tests passed, including real Chroma persistence with substitute embeddings. They passed again immediately after introducing the local profile. See project tests and existing TEST-RESULTS.md. Actual full-corpus extraction found 1,110 physical pages and 2,652 chunks at 1400-character size / 200 overlap. No real embedding index or required-query runs have been completed.

## Local fallback changes just saved

- `app/local.py`: native loopback-only Ollama embedding/chat adapters; no Golem credentials used; Qwen3 embedding model forced to `qwen3-embedding:8b`; validates finite 4096-dimensional vectors; batched ingestion; structured JSON chat with Action schema; unloading between query embedding/chat calls.
- `app/config.py`: selects env file with HW09_ENV_FILE; explicit course/local runtime profiles; separate database/manifest paths; safe runtime metadata and configuration-deviation disclosure.
- `app/store.py`: selects local embeddings in local mode; canonical embedding model remains Qwen3-Embedding-8B.
- `app/ask.py`: selects local native chat adapter; records profile, actual service model and digests; rejects manifest/profile mismatches.
- `app/ingest.py`: records local model metadata and prints batch progress.
- `app/required.py`: local results default to results-local/.
- `.gitignore`: local DB/manifest excluded; env files already ignored.

These local changes need dedicated offline tests and documentation before the first real build. The local model inventory comparison currently preserves API ordering; sort by model name to prevent false mismatch when /api/tags ordering changes. Consider adding the Qwen-recommended query instruction prefix and record it in runtime metadata. Do not claim the original offline tests fully cover the new adapter.

## Machine and storage

Mac: Apple M4, 16 GB RAM (verified outside sandbox).

Ollama app exists, but `ollama` is not on PATH. CLI:
`/Applications/Ollama.app/Contents/Resources/ollama`

CLI `list` reported daemon not running. No daemon has been started during local setup. Existing installed model manifest: `~/.ollama/models/manifests/registry.ollama.ai/library/qwen2.5/1.5b` (~940 MB model files). Local profile currently selects this existing Sudoku chat model.

Required local embedding model has NOT been downloaded. Official Ollama `qwen3-embedding:8b` download is about 4.7 GB (quantized Q4, not the course server weights). Record actual quantization/digest in results rather than imply exact vector equivalence to Golem.

Last storage check showed only ~756 MiB available. User said they will free at least 8 GB. Recheck disk after restart BEFORE downloading. Do not delete personal files or models without authorization.

## Next steps

1. Recheck free storage. If insufficient, wait for user to finish freeing space; do not start a model download.
2. Finish local adapter tests, sort model inventory, and document local commands/profile differences.
3. Start Ollama using the absolute CLI (`.../ollama serve`) with appropriate sandbox escalation. This writes runtime state outside the workspace and needs tool approval. Keep it loopback-only.
4. Verify existing qwen2.5:1.5b model via list/API.
5. Once sufficient disk is available, download `qwen3-embedding:8b` using absolute CLI with appropriate escalation (authorized by user's local-fallback request; do not ask again whether they want local mode).
6. Smoke-test both real local adapters.
7. From project directory, build: `HW09_ENV_FILE=.env.local .venv/bin/python -m app.ingest --source ../documents --rebuild --chunk-size 1400 --chunk-overlap 200`.
8. Run: `HW09_ENV_FILE=.env.local .venv/bin/python -m app.required --k 6 --max-steps 16`.
9. Review actual answers against retrieved passages; Q1-Q7 expected answer, Q8-Q9 insufficient_evidence. Retain failures honestly. Existing 1.5B chat model may be too weak; assess actual results before choosing a larger model/download.
10. Submission report/repository work remains. No final PDF has been made.

## Connectivity findings (do not overstate cause)

Golem port 4000 timed out from tool processes, user's own Terminal, campus student Wi-Fi, and GlobalProtect. User also reported a timeout on a different computer on a different Wi-Fi. This does NOT establish a school-wide outage or a specific local fault. Credentials have never reached authentication, so no basis to call the key invalid.

Configured GlobalProtect portal is vpn.utahtech.edu, matching Utah Tech instructions. User confirmed Connected, and route/DNS checks confirmed active utun5. macOS firewall disabled, no active proxy, no Golem /etc/hosts override. Both campus DNS servers resolve golem.cs.utahtech.edu to 144.38.198.100. VPN's golem.sgc.local returns 144.38.198.100 and 100.64.0.1. Both IPv4 and mapped IPv6 connection attempts timed out, including actual configured embedding/chat SDK calls.

Tailscale installed but stopped; no Golem peer found. User does not know of a school SSH account and does not want to email instructor or compare with classmates. Respect that and proceed with the authorized local fallback.
