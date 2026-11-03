"""Execute the exact supplied questions with one recorded configuration."""
import argparse
import json
import re
from pathlib import Path

from app.agent import run
from app.ask import build_clients, recorded_config, exact_quote_mode
from app.config import DEFAULT_DB_PATH, DEFAULT_MANIFEST_PATH, PROJECT_DIR, RUNTIME_PROFILE


def read_questions(path):
    text = path.read_text(encoding="utf-8")
    sections = re.findall(r"^## (Q\d+):[^\n]*\n\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if [key for key, _ in sections] != [f"Q{i}" for i in range(1, 10)]:
        raise ValueError("Expected Q1 through Q9 in supplied query file")
    # Preserve original text, including Markdown emphasis and internal newlines.
    return [(key, body.strip()) for key, body in sections]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queries", type=Path, default=PROJECT_DIR / "required-queries.md")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST_PATH)
    parser.add_argument("--output", type=Path, default=PROJECT_DIR / ("results-local" if RUNTIME_PROFILE == "local" else "results"))
    parser.add_argument("--k", type=int, default=6)
    parser.add_argument("--max-steps", type=int, default=16)
    args = parser.parse_args()
    questions = read_questions(args.queries)
    config = recorded_config(args.manifest, k=args.k, max_steps=args.max_steps)
    model, retrieve = build_clients(args.db, args.k)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "configuration.json").write_text(json.dumps(config, indent=2) + "\n")
    summary = []
    for number, question in questions:
        result = run(question, model, retrieve, max_steps=args.max_steps, exact_quotes=exact_quote_mode()).model_dump()
        expected = "insufficient_evidence" if number in ("Q8", "Q9") else "answer"
        record = {"query_id": number, "configuration": config, "expected_terminal": expected, **result}
        (args.output / f"{number}.json").write_text(json.dumps(record, indent=2) + "\n")
        summary.append({"query_id": number, "expected": expected, "actual": result["terminal_reason"],
                        "matches_expected": expected == result["terminal_reason"],
                        "claim_support_review": "pending manual review of every claim against cited passage"})
        print(number, result["terminal_reason"], flush=True)
    (args.output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")


if __name__ == "__main__":
    main()
