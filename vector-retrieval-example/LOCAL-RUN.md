# Local fallback with Ollama

This profile uses local Qwen3-Embedding-8B (Ollama's quantized
`qwen3-embedding:8b`) and an installed local chat model. It **does not fulfill the
assignment's instruction to use the supplied course-service configuration**.
The manifest and every query result disclose the runtime, actual model tags,
digests and quantization. Local embeddings must not be mixed with a Golem index.

The course `.env` and credentials are preserved. Local adapters never use the
course API keys. No source passages are sent to external inference services.

## Start and configure

Use Python 3.11+ and the locked dependencies from the main README. Ollama must
be installed separately. On this Mac the CLI is bundled with the app:

```sh
/Applications/Ollama.app/Contents/Resources/ollama serve
```

Keep that Terminal open. From another Terminal, in this project directory:

```sh
cp local.env.example .env.local
HW09_ENV_FILE=.env.local .venv/bin/python -u -m app.local_setup
```

The setup command downloads the 8B embedding model (about 4.7 GB) and requires
at least 7 GiB free on the project volume. Ollama normally stores models in
`~/.ollama/models`; if configured to use a different volume, check that volume's
space too. The local chat default is now `qwen3:4b`. The earlier Sudoku model
`qwen2.5:1.5b` did not reliably follow the evidence policy, and its failed
required-query traces are retained in `results-local-attempt-1/`. Install the
stronger chat model separately (the embedding index can be reused):

```sh
HW09_ENV_FILE=.env.local .venv/bin/python -u -m app.local_setup --model qwen3:4b
```

Qwen3 4B is another disclosed difference from the course setup. Reasoning is
enabled after the initial and required-source retrievals; it is disabled while
mandatory source searches are still missing. Assess the actual recorded runs; a larger model
alone does not establish evidence support.

## Build and run

Current local retrieval returns up to six **physical-page contexts**, reconstructed
only from all stored chunks on each ranked page. Each context retains the parent
chunk IDs and receives a stable `page-*` identifier binding its source, physical
page, parent IDs and text. The vector index itself is unchanged. Course-mode
retrieval continues to return chunks.

The model sees up to eight deduplicated contexts, preserving at least the first
two from each requested source. For each action it selects short labels such as
`P1`; the adapter restores the observed stored identifiers in the accepted action.
Both the compact decision and label map are retained in the trace. Structural
requirement-coverage validation does not establish semantic completeness.

```sh
HW09_ENV_FILE=.env.local .venv/bin/python -u -m app.ingest \
  --source ../documents --rebuild --chunk-size 1400 --chunk-overlap 200

HW09_ENV_FILE=.env.local .venv/bin/python -u -m app.required \
  --k 6 --max-steps 16
```

Output locations: `chroma_local/`, `manifest.local.json`, and `results-local/`.
The database and manifest stay out of Git; reviewed result traces should be
committed. All nine runs use one recorded configuration. Expected terminal
reasons alone do not prove claim support: inspect every citation's passage.

A local query uses an instruction prefix recommended by the Qwen model card;
source passages are embedded without that prefix. The exact prefix is recorded.
The adapter rejects truncated embeddings, wrong dimensions, nonfinite vectors,
and incomplete or truncated chat responses. Chat actions are generated with the
same action invariants enforced by the controller. In extractive mode the model
selects observed chunk IDs grouped by source and gives a per-requirement coverage
assessment. The adapter validates the selection, then copies the retrieved text
into the canonical action. Both the compact decision and expanded action are
logged; a compact decision is not an extra model call. No semantic correctness
is implied by the model's own assessment. The context limit is 16,384 tokens
and output limit is 8,192 tokens per action, including model reasoning. Query embeddings and chat calls
unload their model after completion to fit the 16 GB Mac. Document ingestion
keeps the embedding model loaded between batches of eight passages.

## Offline tests and returning to Golem

```sh
.venv/bin/python -m unittest discover -s tests -v
```

Tests substitute local API responses; they do not start Ollama or download models.
To return to the original course configuration, omit `HW09_ENV_FILE=.env.local`.
Course runs then use `.env`, `chroma_db/`, `manifest.json`, and `results/`. Rebuild
with the course embedding service; do not reuse the local vectors.

References: [Ollama embedding model](https://ollama.com/library/qwen3-embedding),
[embedding API](https://docs.ollama.com/api/embed),
[structured chat API](https://docs.ollama.com/api/chat),
[Qwen model card and query instructions](https://huggingface.co/Qwen/Qwen3-Embedding-8B).

## Long-running builds, recovery, and queued query runs

The local 8B embedding build may take roughly 1-2 hours on this 16 GB M4;
actual time depends on memory pressure and other work. Keep the Mac awake while
it runs. Chroma persists successful batches as they complete.

To queue the nine runs while an index is still building, use a separate Terminal:

```sh
HW09_ENV_FILE=.env.local .venv/bin/python -u -m app.local_pipeline
```

This waits for a complete 1,110-page local-index manifest, then runs Q1-Q9 with
k=6 and a 16-invocation limit. Its state and log are in `.runtime/`. The stage
`queries_recorded` means traces exist, not that answers passed evidence review.
Inspect progress without contacting model services:

```sh
.venv/bin/python -m app.local_status
```

If the computer restarts or ingestion is interrupted, restart Ollama, then resume
with the **same** source files, embedding weights and chunk settings:

```sh
HW09_ENV_FILE=.env.local .venv/bin/python -u -m app.ingest \
  --source ../documents --resume --chunk-size 1400 --chunk-overlap 200
```

`--resume` validates the saved build identity and skips stored chunk IDs. It
rejects changed sources, embedding weights, paths or chunk settings. Restart the
queue in another Terminal if it also stopped. Use `--rebuild` only when you want
to discard existing vectors and begin again.

## Action generation safeguards

The first generated action must retrieve. After a retrieval observation exists,
the action schema allows a final answer only if passages were returned, and its
citation values are restricted to chunk IDs in observations from that run. The
original question cannot spoof an observation. The current schema is both sent
to Ollama's decoder and included in its prompt. Runtime validation remains in
the controller. These checks enforce provenance; manual review still checks
whether every claim follows from its cited passages.

The configured `LOCAL_THINKING=true` and `LOCAL_OUTPUT_TOKENS=8192` are
recorded with each run. Named-source coverage is enforced in generation and
checked again by the controller before an answer is accepted. The static system
prompt and controller/local-adapter code hashes are recorded for reproducibility.
Original failed/partial runs are retained in numbered `results-local-attempt-*`
directories. They are development evidence, not passing results. New run outcomes
must be reviewed before claiming success.

Compact selections require at least one excerpt from every explicitly requested
source, reject duplicate IDs, and require each selected excerpt to appear in a
requirement assessment. Up to eight excerpts per included source can be chosen,
so split tables and distinct limitations do not compete for a fixed four-excerpt
budget. These are structural safeguards; relevance and full coverage remain
manual review responsibilities. `local_selection_decision` trace entries retain
the unedited model assessment, including candidates that fail validation.

The local retrieval result count (`k=6`) now counts distinct physical-page
contexts. Semantic ranking still uses the original 1,400/200-character chunk
embeddings; for each selected page, the retriever reads all its stored chunks,
checks overlaps and reconstructs page text. Derived `page-...` identifiers bind
the source, page, complete text and ordered `parent_chunk_ids`. These IDs are
returned in the retrieval observation and are the citation IDs for that run;
underlying embedding records and IDs remain unchanged. Course-service retrieval
continues returning individual chunks. This difference is recorded explicitly.

The model sees short labels such as P1 and P2, with the corresponding source,
physical page and complete text. Each decision's label-to-stored-passage map is
saved in the trace; final citations use the actual returned `page-...` IDs.
The compact context retains eight passages (or at least two per requested
source), with the first two per requested source pinned. Exact quotation and
provenance still do not certify the model's coverage assessment.

## Linked model-code rules

For an explicit section or table identifier, semantic candidates are reranked
to prefer the matching heading. For Food Code queries without a section ID,
the tool can follow up to two frequently cited section references in the top
semantic results to primary chapter headings in the SAME stored Food Code.
This brings abbreviated table conditions back to their normative section text.
It reads stored passages; it does not insert hand-written answers or external
sources. The semantic candidate count, link limit, and returned result count are
recorded. Every returned passage still has its stored source/page/chunk labels.

Automated semantic judging was tested against known good and bad answers but
misclassified control cases. It is not used as an acceptance gate. Review final
claims manually against their own cited passages, and record missing subparts
even when the terminal reason is `answer`.
