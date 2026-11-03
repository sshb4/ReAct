# ReAct coursework

- [U0-HW-09: Vector retrieval agent](vector-retrieval-example/README.md)
- [Vector retrieval PDF report](vector-retrieval-example/output/pdf/bates-sasha-vector-retrieval.pdf)
- Earlier Sudoku project: see below.

## ReAct Sudoku Agent

A Python command-line project for CS 4300. Development begins with contracts and black-box tests before implementation.

## Current status

Puzzle operations, classical propositional logic, typed request validation, controller policies, and the agent loop are implemented. Qwen 2.5 1.5B completed the three-empty-cell example in 18 model-selected tool requests, including fact/rule updates, three entailed queries, placements, and explicit validated submission, with no rejected requests. This verifies one near-complete puzzle, not general reliability on harder puzzles. See the [live reasoning trace](docs/evidence/model-run-kb-success.json) and [independent verification](docs/evidence/requirements-verification.json).

- [Architecture](docs/architecture.md)
- [Behavior contracts](docs/contracts.md)
- [Development plan and evidence](docs/development.md)


## Report files

- [report.md](report/report.md): the editable report, including a Mermaid component diagram.




## U0-HW-09: Vector retrieval

The separate [vector retrieval project](vector-retrieval-example/README.md) includes the complete five-document ingestion and bounded ReAct implementation, offline tests, recorded query traces, and evidence reviews. Its final report is [bates-sasha-vector-retrieval.pdf](vector-retrieval-example/output/pdf/bates-sasha-vector-retrieval.pdf). The recorded run uses the disclosed local Ollama fallback; see its report for actual outcomes and limitations.

For this assignment, run commands from `vector-retrieval-example/`. Obtain the original five PDFs from the homework materials and place them in the repository-root `documents/` folder before rebuilding. Supplied PDFs and local runtime files are excluded from Git.
