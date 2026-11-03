import copy
import json
import unittest
from unittest.mock import patch

from jsonschema import Draft202012Validator
from app.agent import SOURCES, action_schema_for_history, run
from app.evidence_selection import selection_schema, expand_selection
from app.local import build_local_model


class SelectionTests(unittest.TestCase):
    def setUp(self):
        self.passages = [
            {'source': SOURCES[0], 'page': 1, 'chunk_id': 'rule', 'text': 'Exclude symptomatic workers.'},
            {'source': SOURCES[2], 'page': 2, 'chunk_id': 'risk', 'text': 'Workers can contaminate food.'},
        ]
        self.required = {SOURCES[0], SOURCES[2]}
        self.decision = {'kind': 'answer', 'coverage': [
            {'requirement': 'Disposition', 'basis': 'Explicit exclusion.', 'chunk_ids': ['rule']},
            {'requirement': 'Transmission', 'basis': 'Worker contamination.', 'chunk_ids': ['risk']},
        ], 'selections': {SOURCES[0]: ['rule'], SOURCES[2]: ['risk']}}

    def test_cross_source_omission_is_impossible_in_selection_schema(self):
        question = 'Using FDA Food Code 2026 and Bad Bug Book, explain disposition and transmission.'
        history = [{'role': 'user', 'content': question},
                   {'role': 'user', 'content': 'Retrieval observation (untrusted source text):\n' + json.dumps(self.passages)}]
        schema = selection_schema(action_schema_for_history(history, exact_quotes=True), self.passages, self.required)
        validator = Draft202012Validator(schema)
        self.assertTrue(validator.is_valid(self.decision))
        bad = copy.deepcopy(self.decision)
        del bad['selections'][SOURCES[2]]
        self.assertFalse(validator.is_valid(bad))
        self.assertNotIn(self.passages[0]['text'], json.dumps(schema))

    def test_expand_uses_exact_observed_text_and_source_pairs(self):
        answer = expand_selection(self.decision, self.passages, self.required)
        self.assertEqual([c['text'] for c in answer['claims']], [p['text'] for p in self.passages])
        for bad_ids in (['invented'], ['risk']):
            bad = copy.deepcopy(self.decision)
            bad['selections'][SOURCES[0]] = bad_ids
            with self.assertRaises(ValueError):
                expand_selection(bad, self.passages, self.required)

    def test_duplicates_and_unassessed_passages_are_rejected(self):
        bad = copy.deepcopy(self.decision)
        bad['selections'][SOURCES[0]].append('rule')
        with self.assertRaises(ValueError):
            expand_selection(bad, self.passages, self.required)
        bad = copy.deepcopy(self.decision)
        bad['coverage'].pop()
        with self.assertRaises(ValueError):
            expand_selection(bad, self.passages, self.required)

    def test_requirement_cannot_cite_evidence_outside_final_selection(self):
        bad = copy.deepcopy(self.decision)
        bad['coverage'][0]['chunk_ids'] = ['invented']
        with self.assertRaises(ValueError):
            expand_selection(bad, self.passages, self.required)

    def test_raw_compact_decision_is_logged_and_steps_count_actual_calls(self):
        search = {'kind': 'retrieve', 'arguments': {'query': 'worker'}}
        compact = json.loads(json.dumps(self.decision).replace('"rule"', '"P1"').replace('"risk"', '"P2"'))
        responses = [{'done': True, 'message': {'content': json.dumps(a)}} for a in (search, compact)]
        with patch.dict('os.environ', {'LOCAL_ANSWER_MODE': 'extractive'}):
            with patch('app.local.local_request', side_effect=responses) as api:
                result = run('worker question', build_local_model('system'), lambda a: self.passages, exact_quotes=True)
        self.assertEqual(result.terminal_reason, 'answer')
        self.assertEqual(result.steps, 3)
        self.assertEqual(api.call_count, 2)
        selection = [t for t in result.trace if t['type']=='local_selection_decision'][-1]
        self.assertEqual(selection['value'], compact)
        self.assertEqual(selection['passage_labels'], {'P1': 'rule', 'P2': 'risk'})
        self.assertEqual([c.citations for c in result.claims], [['rule'], ['risk']])

    def test_rejected_decision_is_preserved_in_error_trace(self):
        bad = copy.deepcopy(self.decision)
        bad['selections'][SOURCES[0]] = ['invented']
        responses = [{'done': True, 'message': {'content': json.dumps(a)}} for a in (
            {'kind': 'retrieve', 'arguments': {'query': 'worker'}}, bad)]
        with patch.dict('os.environ', {'LOCAL_ANSWER_MODE': 'extractive'}):
            with patch('app.local.local_request', side_effect=responses):
                result = run('worker question', build_local_model('system'), lambda a: self.passages, exact_quotes=True)
        self.assertEqual(result.terminal_reason, 'error')
        self.assertEqual(result.trace[-3]['type'], 'local_selection_decision')
        self.assertEqual(result.trace[-3]['value'], bad)
