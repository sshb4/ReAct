"""Render saved query outputs without changing model results or grading them."""
import argparse
import hashlib
import json
from pathlib import Path
import time

PROJECT = Path(__file__).resolve().parent.parent


def load_json(path, default=None):
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def render(directory):
    directory.mkdir(parents=True, exist_ok=True)
    records = []
    for number in range(1, 10):
        path = directory / f'Q{number}.json'
        data = load_json(path)
        if data is not None:
            records.append((path, data))
    config = load_json(directory / 'configuration.json', {})
    if records and any(data['configuration'] != config for _, data in records):
        raise ValueError('Query results do not share the recorded configuration')
    review = load_json(directory / 'evidence-review.json', {}).get('queries', {})
    lines = ['# Required-query results', '', f'Recorded: {len(records)} of 9 queries.', '',
             'These are actual model outputs. An answer terminal reason does not certify relevance or completeness.', '']
    if config:
        lines += ['## Recorded configuration', '']
        for key in ('runtime_profile','answer_mode','embedding_model','embedding_service_model',
                    'llm_model','chunk_size','chunk_overlap','retrieval_k','retrieval_candidate_k',
                    'section_link_expansion_limit','max_steps','chat_context_tokens',
                    'chat_thinking','chat_output_tokens_per_action','index_version'):
            if key in config:
                lines.append(f'- {key}: `{config[key]}`')
        if config.get('configuration_deviation'):
            lines += ['', config['configuration_deviation']]
        lines += ['']
    if config.get('answer_mode') == 'extractive':
        lines += ['Final answer passages are copied verbatim and checked against their cited retrieved chunks.',
                  'This verifies quote fidelity and provenance. Relevance and coverage are reviewed separately.', '']
    for path, data in records:
        lines += [f"## {path.stem}: {data['terminal_reason']}", '', data['question'], '',
                  f"Steps: {data['steps']}/{data['max_steps']}. [Complete action-observation trace]({path.name}).", '']
        check = review.get(path.stem)
        if check and check.get('result_sha256') == hashlib.sha256(path.read_bytes()).hexdigest():
            lines += [f"Review: {check.get('support', 'see review')} / {check.get('coverage', 'see review')}.", '']
        else:
            lines += ['Passage-by-passage relevance and coverage review: pending.', '']
        if data['message']:
            lines += [data['message'], '']
        evidence = {item['chunk_id']: item for item in data['evidence']}
        for index, claim in enumerate(data['claims'], 1):
            lines += [f'### Evidence {index}', '']
            for chunk_id in claim['citations']:
                item = evidence[chunk_id]
                lines += [f"Source: `{item['source']}`, physical PDF page {item['page']}, chunk `{chunk_id}`.", '']
            if config.get('answer_mode') == 'extractive':
                lines += ['```text', claim['text'], '```', '']
            else:
                lines += [claim['text'], '']
    destination = directory / 'ANSWERS.md'
    temporary = destination.with_suffix('.md.tmp')
    temporary.write_text('\n'.join(lines) + '\n')
    temporary.replace(destination)
    return len(records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', type=Path, default=PROJECT / 'results-local')
    parser.add_argument('--watch', action='store_true')
    args = parser.parse_args()
    previous = None
    deadline = time.monotonic() + 6 * 60 * 60
    while True:
        signature = [(p.name, p.stat().st_mtime_ns) for p in sorted(args.results.glob('*.json'))]
        if signature != previous:
            count = render(args.results)
            print(f'Rendered {count}/9 results to {args.results / "ANSWERS.md"}', flush=True)
            previous = signature
        else:
            count = sum((args.results / f'Q{i}.json').exists() for i in range(1, 10))
        if not args.watch or (count == 9 and (args.results / 'summary.json').exists()):
            break
        if time.monotonic() > deadline:
            raise TimeoutError('Result watch exceeded six hours; saved outputs remain available')
        time.sleep(10)


if __name__ == '__main__':
    main()
