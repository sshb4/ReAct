import unittest
from pydantic import ValidationError
from app.agent import Action, Passage, RetrievalInput, RunResult, run
from app.required import read_questions
from app.config import PROJECT_DIR

PASSAGE = {"source": "fda-food-code-2026.pdf", "page": 42, "chunk_id": "sample-only",
           "text": "Exclude an employee who has vomiting or diarrhea."}
SEARCH = {"kind": "retrieve", "arguments": {"query": "vomiting"}}
ANSWER = {"kind": "answer", "claims": [{"text": "Exclude the employee who is vomiting.", "citations": ["sample-only"]}]}
MISSING = {"kind": "insufficient_evidence", "missing_evidence": "No current Utah adoption regulation or penalties were retrieved."}


def scripted(*actions):
    iterator = iter(actions)
    return lambda history: next(iterator)


class AgentTests(unittest.TestCase):
    def test_supported_claim_follows_substitute_passage(self):
        # Deliberately simple entailment fixture; not a claim about the live corpus.
        result = run("What happens to an employee who is vomiting?", scripted(SEARCH, ANSWER), lambda a: [PASSAGE])
        self.assertEqual(result.terminal_reason, "answer")
        self.assertEqual(result.steps, 3)
        self.assertIn("Exclude", result.evidence[0].text)
        self.assertEqual(result.claims[0].text, "Exclude the employee who is vomiting.")
        self.assertEqual(result.trace[2]["value"], [PASSAGE])

    def test_insufficient_after_retrieving_unrelated_evidence(self):
        result = run("What are current Utah penalties?", scripted(SEARCH, MISSING), lambda a: [PASSAGE])
        self.assertEqual(result.terminal_reason, "insufficient_evidence")
        self.assertFalse(result.claims)

    def test_empty_retrieval(self):
        self.assertEqual(run("q", scripted(SEARCH, MISSING), lambda a: []).terminal_reason, "insufficient_evidence")

    def test_citation_not_returned_is_rejected(self):
        result = run("q", scripted(ANSWER), lambda a: [PASSAGE])
        self.assertEqual(result.terminal_reason, "error")
        self.assertIn("not retrieved", result.message)

    def test_evidence_is_not_shared_between_runs(self):
        run("q", scripted(SEARCH, ANSWER), lambda a: [PASSAGE])
        self.assertEqual(run("q", scripted(ANSWER), lambda a: []).terminal_reason, "error")

    def test_limits_count_model_and_tool_calls(self):
        for limit in (1, 2, 3, 4):
            calls = []
            def model(history):
                calls.append("model")
                return SEARCH
            def retrieve(args):
                calls.append("tool")
                return []
            result = run("q", model, retrieve, max_steps=limit)
            self.assertEqual(result.terminal_reason, "step_limit")
            self.assertEqual(len(calls), limit)
            self.assertEqual(result.steps, limit)

    def test_final_answer_at_last_step_is_accepted(self):
        self.assertEqual(run("q", scripted(SEARCH, ANSWER), lambda a: [PASSAGE], max_steps=3).terminal_reason, "answer")

    def test_limit_validation(self):
        for limit in (0, -1, True, "3", 2.5):
            with self.assertRaises(ValueError):
                run("q", scripted(MISSING), lambda a: [], max_steps=limit)

    def test_tool_argument_validation(self):
        for args in ({"query": " "}, {"query": 3}, {"query": "q", "source": "unknown.pdf"},
                     {"query": "q", "k": 999}, {"query": "q", "filters": {"page": 1}}):
            with self.assertRaises(ValidationError):
                RetrievalInput.model_validate(args)
        self.assertEqual(RetrievalInput(query="q", source=PASSAGE["source"]).source, PASSAGE["source"])

    def test_invalid_tool_action_never_executes_tool(self):
        def forbidden(args):
            self.fail("invalid arguments reached retrieval")
        result = run("q", scripted({"kind": "retrieve", "arguments": {"query": ""}}), forbidden)
        self.assertEqual(result.terminal_reason, "error")

    def test_tool_failure_is_recorded(self):
        def broken(args):
            raise RuntimeError("substitute service failure")
        result = run("q", scripted(SEARCH), broken)
        self.assertEqual(result.terminal_reason, "error")
        self.assertIn("substitute service failure", result.message)
        self.assertEqual(result.trace[-2]["type"], "error_observation")

    def test_malformed_model_output(self):
        self.assertEqual(run("q", scripted("not JSON"), lambda a: []).terminal_reason, "error")

    def test_source_labels_required(self):
        for field in PASSAGE:
            bad = dict(PASSAGE)
            del bad[field]
            with self.assertRaises(ValidationError):
                Passage.model_validate(bad)
        with self.assertRaises(ValidationError):
            Passage.model_validate({**PASSAGE, "page": 0})

    def test_terminal_reason_and_budget_validation(self):
        for update in ({"terminal_reason": "done"}, {"steps": 4}, {"terminal_reason": "answer"},
                       {"terminal_reason": "step_limit"}):
            with self.assertRaises(ValidationError):
                RunResult.model_validate({"question": "q", "terminal_reason": "error", "steps": 0,
                                          "max_steps": 3, **update})

    def test_required_questions_are_preserved(self):
        path = PROJECT_DIR / "required-queries.md"
        questions = read_questions(path)
        self.assertEqual(len(questions), 9)
        self.assertEqual(questions[-1][1], "Who is the strongest Avenger, and what evidence establishes that ranking?")
        self.assertIn(questions[0][1], path.read_text())


if __name__ == "__main__":
    unittest.main()


class RuntimeSourceCoverageTests(unittest.TestCase):
    def test_cited_answer_cannot_omit_an_explicitly_requested_source(self):
        question = 'Using the FDA Food Code 2026 and the Bad Bug Book, explain vomiting.'
        result = run(question, scripted(SEARCH, ANSWER), lambda args: [PASSAGE])
        self.assertEqual(result.terminal_reason, 'error')
        self.assertIn('requested source evidence', result.message)


class ExactQuoteTests(unittest.TestCase):
    def test_exact_source_quote_is_accepted(self):
        answer={'kind':'answer','claims':[{'text':PASSAGE['text'],'citations':[PASSAGE['chunk_id']]}]}
        result=run('q',scripted(SEARCH,answer),lambda args:[PASSAGE],exact_quotes=True)
        self.assertEqual(result.terminal_reason,'answer')

    def test_valid_id_cannot_support_altered_quote(self):
        result=run('q',scripted(SEARCH,ANSWER),lambda args:[PASSAGE],exact_quotes=True)
        self.assertEqual(result.terminal_reason,'error')
        self.assertIn('exactly match',result.message)

    def test_quote_and_citation_must_be_paired(self):
        other={**PASSAGE,'chunk_id':'other-id','text':'A different passage.'}
        answer={'kind':'answer','claims':[{'text':PASSAGE['text'],'citations':['other-id']}]}
        result=run('q',scripted(SEARCH,answer),lambda args:[PASSAGE,other],exact_quotes=True)
        self.assertEqual(result.terminal_reason,'error')
