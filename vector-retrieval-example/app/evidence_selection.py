"""Compact local decisions; quote text always comes from observed passages."""
from __future__ import annotations

import copy


def selection_schema(action_schema, passages, required_sources):
    schema = copy.deepcopy(action_schema)
    by_source = {}
    for passage in passages:
        by_source.setdefault(passage['source'], []).append(passage['chunk_id'])
    ids = [p['chunk_id'] for p in passages]
    for alternative in schema['anyOf']:
        if alternative['properties']['kind']['const'] != 'answer':
            continue
        alternative['properties'] = {
            'kind': {'type': 'string', 'const': 'answer'},
            'coverage': {
                'type': 'array', 'minItems': 1, 'maxItems': 12,
                'items': {
                    'type': 'object',
                    'properties': {
                        'requirement': {'type': 'string', 'minLength': 1},
                        'basis': {'type': 'string', 'minLength': 1},
                        'chunk_ids': {'type': 'array', 'minItems': 1,
                                      'items': {'type': 'string', 'enum': ids}},
                    },
                    'required': ['requirement', 'basis', 'chunk_ids'],
                    'additionalProperties': False,
                },
            },
            'selections': {
                'type': 'object',
                'properties': {
                    source: {'type': 'array', 'minItems': 1, 'maxItems': 8,
                             'items': {'type': 'string', 'enum': source_ids}}
                    for source, source_ids in by_source.items()
                },
                'required': sorted(required_sources),
                'additionalProperties': False,
            },
        }
        alternative['required'] = ['kind', 'coverage', 'selections']
    schema['$defs'].pop('Claim', None)
    return schema


def expand_selection(decision, passages, required_sources):
    """Validate structural coverage and expand IDs, without judging entailment."""
    if decision.get('kind') != 'answer':
        return decision
    if set(decision) != {'kind', 'coverage', 'selections'}:
        raise ValueError('Selection answer requires coverage and selections only')
    available = {p['chunk_id']: p for p in passages}
    selections = decision['selections']
    if not isinstance(selections, dict) or not required_sources <= selections.keys():
        raise ValueError('Selection omitted a requested source')
    chosen = []
    for source, ids in selections.items():
        if not isinstance(ids, list) or not 1 <= len(ids) <= 8:
            raise ValueError('Select one to eight IDs per included source')
        for cid in ids:
            if cid not in available or available[cid]['source'] != source:
                raise ValueError('Selected ID was not observed under that source')
            if cid in chosen:
                raise ValueError('Duplicate evidence selection')
            chosen.append(cid)
    coverage = decision['coverage']
    if not chosen or not isinstance(coverage, list) or not 1 <= len(coverage) <= 12:
        raise ValueError('Answer needs selections and a requirement coverage assessment')
    referenced = set()
    for item in coverage:
        if not isinstance(item, dict) or set(item) != {'requirement', 'basis', 'chunk_ids'}:
            raise ValueError('Invalid requirement assessment')
        if any(not isinstance(item[k], str) or not item[k].strip() for k in ('requirement', 'basis')):
            raise ValueError('Requirement and evidence basis must be nonblank')
        if not isinstance(item['chunk_ids'], list) or not item['chunk_ids']:
            raise ValueError('Each requirement needs selected evidence')
        if any(cid not in chosen for cid in item['chunk_ids']):
            raise ValueError('Assessment cites an unselected ID')
        referenced.update(item['chunk_ids'])
    if referenced != set(chosen):
        raise ValueError('Every selected passage must support an assessed requirement')
    return {'kind': 'answer', 'claims': [
        {'text': available[cid]['text'], 'citations': [cid]} for cid in chosen
    ]}
