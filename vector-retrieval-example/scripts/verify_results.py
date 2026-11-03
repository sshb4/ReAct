"""Verify saved run integrity offline; semantic assessments remain separate.

Run from this project: python scripts/verify_results.py --results results-local
Add --sources ../documents to check passages against the supplied PDFs.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app.agent import RunResult, RetrievalInput, SOURCES
from app.ask import SYSTEM
from app.required import read_questions


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', type=Path, default=ROOT / 'results-local')
    parser.add_argument('--sources', type=Path)
    args = parser.parse_args()
    directory = args.results
    config = json.loads((directory / 'configuration.json').read_text())
    assert config['runtime_profile'] == 'local', 'This verifier checks recorded local page-context runs'
    local_prompt = SYSTEM + '\nSources: ' + json.dumps(SOURCES)
    assert config['system_prompt_sha256'] == hashlib.sha256(local_prompt.encode()).hexdigest()
    review = json.loads((directory / 'evidence-review.json').read_text())
    questions = dict(read_questions(ROOT / 'required-queries.md'))
    readers = {}
    checks = {}
    hashes = {'controller_sha256': 'agent.py', 'local_adapter_sha256': 'local.py',
              'evidence_selection_sha256': 'evidence_selection.py', 'retrieval_sha256': 'retrieval.py'}
    for key, filename in hashes.items():
        assert config[key] == digest(ROOT / 'app' / filename), (key, 'implementation changed')
    for number, question in questions.items():
        path = directory / f'{number}.json'
        data = json.loads(path.read_text())
        result = RunResult.model_validate({k: data[k] for k in RunResult.model_fields})
        assert data['configuration'] == config and result.question == question
        assert data['expected_terminal'] == ('insufficient_evidence' if number in ('Q8', 'Q9') else 'answer')
        assert result.max_steps == config['max_steps']
        assert review['queries'][number]['result_sha256'] == digest(path)
        assert result.trace[-1] == {'type': 'terminal', 'terminal_reason': result.terminal_reason,
                                    'steps': result.steps}
        observed, observations, steps = {}, 0, set()
        for event in result.trace:
            if 'step' in event:
                assert 1 <= event['step'] <= result.steps
                steps.add(event['step'])
            if event['type'] == 'tool_action':
                RetrievalInput.model_validate(event['arguments'])
            if event['type'] == 'retrieval_observation':
                assert len(event['value']) <= config['retrieval_k']
                for passage in event['value']:
                    observations += 1
                    cid = passage['chunk_id']
                    assert cid not in observed or observed[cid] == passage
                    observed[cid] = passage
                    assert passage['parent_chunk_ids'] and passage['retrieval_unit'] == 'page_context'
                    if args.sources:
                        from pypdf import PdfReader
                        source = passage['source']
                        if source not in readers:
                            readers[source] = PdfReader(args.sources / source)
                        source_text = readers[source].pages[passage['page'] - 1].extract_text()
                        # Stored character splitters may omit boundary whitespace.
                        assert ''.join(passage['text'].split()) == ''.join(source_text.split()), (number, source, passage['page'])
            if event['type'] == 'model_action' and result.terminal_reason == 'answer':
                action = event['value']
                if isinstance(action, str):
                    action = json.loads(action)
                for claim in action.get('claims', []):
                    for cid in claim['citations']:
                        assert cid in observed and claim['text'] == observed[cid]['text']
        assert steps == set(range(1, result.steps + 1))
        assert {e.chunk_id for e in result.evidence} == set(observed)
        for claim in result.claims:
            for cid in claim.citations:
                assert cid in observed and claim.text == observed[cid]['text']
        checks[number] = {'result_sha256': digest(path), 'passed': True,
                          'observations_checked': observations, 'terminal': result.terminal_reason,
                          'semantic_assessment': review['queries'][number]['coverage']}
    output = {'mechanical_checks_passed': True, 'source_pdf_checked': bool(args.sources),
              'semantic_review_is_separate': True, 'configuration_sha256': digest(directory / 'configuration.json'),
              'queries': checks}
    (directory / 'review-verification.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
