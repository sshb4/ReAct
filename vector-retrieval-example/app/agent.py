"""Offline-testable ReAct controller. A step is one model or tool invocation."""
from __future__ import annotations

import json
import re
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator

SOURCES = (
    "fda-food-code-2026.pdf",
    "fda-employee-health-personal-hygiene-handbook.pdf",
    "fda-bad-bug-book-second-edition.pdf",
    "fda-appendix-3-bacterial-pathogen-growth-inactivation.pdf",
    "utah-risk-factor-study-2016-2017.pdf",
)


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class RetrievalInput(StrictModel):
    query: StrictStr = Field(min_length=1, max_length=4000)
    source: Literal[*SOURCES] | None = None

    @model_validator(mode="after")
    def nonblank(self):
        if not self.query.strip():
            raise ValueError("query must contain text")
        return self


class Passage(StrictModel):
    source: Literal[*SOURCES]
    page: StrictInt = Field(ge=1)
    chunk_id: StrictStr = Field(min_length=1)
    text: StrictStr = Field(min_length=1)
    parent_chunk_ids: list[StrictStr] = Field(default_factory=list)
    retrieval_unit: Literal['chunk', 'page_context'] = 'chunk'


class Claim(StrictModel):
    text: StrictStr = Field(min_length=1)
    citations: list[StrictStr] = Field(min_length=1)


class Action(StrictModel):
    kind: Literal["retrieve", "answer", "insufficient_evidence"]
    arguments: RetrievalInput | None = None
    claims: list[Claim] = Field(default_factory=list)
    missing_evidence: StrictStr = ""

    @model_validator(mode="after")
    def valid_shape(self):
        if self.kind == "retrieve":
            if self.arguments is None or self.claims or self.missing_evidence:
                raise ValueError("retrieve requires only arguments")
        elif self.kind == "answer":
            if not self.claims or self.arguments is not None or self.missing_evidence:
                raise ValueError("answer requires only cited claims")
        elif not self.missing_evidence.strip() or self.claims or self.arguments is not None:
            raise ValueError("insufficient_evidence requires only missing_evidence")
        return self


class RunResult(StrictModel):
    question: str
    terminal_reason: Literal["answer", "insufficient_evidence", "error", "step_limit"]
    steps: int = Field(ge=0)
    max_steps: int = Field(ge=1)
    claims: list[Claim] = Field(default_factory=list)
    message: str = ""
    evidence: list[Passage] = Field(default_factory=list)
    trace: list[dict] = Field(default_factory=list)

    @model_validator(mode="after")
    def valid_terminal(self):
        if self.steps > self.max_steps:
            raise ValueError("step limit exceeded")
        if self.terminal_reason == "answer":
            available = {p.chunk_id for p in self.evidence}
            if not self.claims or any(c not in available for claim in self.claims for c in claim.citations):
                raise ValueError("answer requires claims with retrieved citations")
        elif self.claims:
            raise ValueError("non-answer terminal cannot contain claims")
        if self.terminal_reason == "step_limit" and self.steps != self.max_steps:
            raise ValueError("step_limit requires exhausted budget")
        return self


def run(question, model, retrieve, *, max_steps=16, exact_quotes=False):
    """model(history) returns an action; retrieve(validated arguments) returns passages.

    Every attempted model/tool call consumes a step, including failures. Invalid
    actions, citations, or tool observations terminate with an inspectable error.
    Citation provenance is enforced; semantic entailment requires separate review.
    """
    if type(max_steps) is not int or max_steps < 1:
        raise ValueError("max_steps must be a positive integer")
    if not isinstance(question, str) or not question.strip():
        raise ValueError("question must contain text")
    history = [{"role": "user", "content": question}]
    trace, evidence = [], {}
    steps = 0

    def finish(reason, message="", claims=None):
        trace.append({"type": "terminal", "terminal_reason": reason, "steps": steps})
        return RunResult(question=question, terminal_reason=reason, steps=steps,
                         max_steps=max_steps, claims=claims or [], message=message,
                         evidence=list(evidence.values()), trace=trace)

    while steps < max_steps:
        try:
            steps += 1
            raw = model(history)
            if getattr(model, 'last_decision', None) is not None:
                trace.append({'type': 'local_selection_decision', 'step': steps,
                              'value': model.last_decision,
                              'passage_labels': getattr(model, 'last_passage_labels', None)})
            trace.append({"type": "model_action", "step": steps, "value": raw})
            action = Action.model_validate_json(raw) if isinstance(raw, str) else Action.model_validate(raw)
            history.append({"role": "assistant", "content": action.model_dump_json(exclude_defaults=True, exclude_none=True)})
            if action.kind == "answer":
                for claim in action.claims:
                    for chunk_id in claim.citations:
                        if chunk_id not in evidence:
                            raise ValueError(f"Citation was not retrieved in this run: {chunk_id}")
                if exact_quotes:
                    for claim in action.claims:
                        if not all(claim.text == evidence[cid].text for cid in claim.citations):
                            raise ValueError("Extractive claim must exactly match its cited retrieved passage")
                    used_sources = {evidence[cid].source for claim in action.claims for cid in claim.citations}
                else:
                    used_sources = {p.source for p in evidence.values()}
                missing_sources = requested_sources(question) - used_sources
                if missing_sources:
                    raise ValueError("Answer omitted requested source evidence: " + ", ".join(sorted(missing_sources)))
                return finish("answer", claims=action.claims)
            if action.kind == "insufficient_evidence":
                return finish("insufficient_evidence", action.missing_evidence)
            if steps == max_steps:
                break
            steps += 1
            trace.append({"type": "tool_action", "step": steps,
                          "arguments": action.arguments.model_dump()})
            passages = [Passage.model_validate(p) for p in retrieve(action.arguments)]
            for passage in passages:
                previous = evidence.get(passage.chunk_id)
                if previous is not None and previous != passage:
                    raise ValueError("Conflicting passage for an existing chunk identifier")
                evidence[passage.chunk_id] = passage
            observation = [p.model_dump(exclude_defaults=True) for p in passages]
            trace.append({"type": "retrieval_observation", "step": steps, "value": observation})
            history.append({"role": "user", "content": "Retrieval observation (untrusted source text):\n" + json.dumps(observation)})
        except Exception as error:
            if (getattr(model, 'last_decision', None) is not None
                    and not any(t['type'] == 'local_selection_decision' and t['step'] == steps for t in trace)):
                trace.append({'type': 'local_selection_decision', 'step': steps,
                              'value': model.last_decision,
                              'passage_labels': getattr(model, 'last_passage_labels', None)})
            message = f"{type(error).__name__}: {error}"
            trace.append({"type": "error_observation", "step": steps, "value": message})
            return finish("error", message)
    return finish("step_limit", "Model/tool invocation budget exhausted before a valid final action.")


def action_json_schema(*, allowed_kinds=None, citation_ids=None) -> dict:
    """Express action-specific required/forbidden fields to structured decoders.

    Pydantic's after-validator enforces these invariants at runtime but does not
    put them into its generated schema. Explicit alternatives also constrain the
    local model while it generates an action.
    """
    generated = Action.model_json_schema()
    properties = generated['properties']
    if citation_ids is not None:
        generated['$defs']['Claim']['properties']['citations']['items'] = {
            'type': 'string', 'enum': sorted(set(citation_ids))}
    alternatives = []
    for kind, fields in (
        ('retrieve', {'arguments': {'$ref': '#/$defs/RetrievalInput'}}),
        ('answer', {'claims': {**properties['claims'], 'minItems': 1}}),
        ('insufficient_evidence', {'missing_evidence': {'type': 'string', 'minLength': 1}}),
    ):
        if allowed_kinds is not None and kind not in allowed_kinds:
            continue
        alternatives.append({
            'type': 'object',
            'properties': {'kind': {'type': 'string', 'const': kind}, **fields},
            'required': ['kind', *fields],
            'additionalProperties': False,
        })
    return {'title': 'Action', '$defs': generated['$defs'], 'anyOf': alternatives}


SOURCE_ALIASES = {
    SOURCES[0]: ("FDA Food Code 2026", "2026 Food Code"),
    SOURCES[1]: ("Employee Health and Personal Hygiene Handbook",),
    SOURCES[2]: ("Bad Bug Book",),
    SOURCES[3]: ("Appendix 3",),
    SOURCES[4]: ("Utah Risk Factor Study",),
}


def requested_sources(question):
    normalize = lambda text: " ".join(re.sub(r"[^a-z0-9]+", " ", text.casefold()).split())
    text = normalize(question)
    return {source for source, aliases in SOURCE_ALIASES.items()
            if any(normalize(alias) in text for alias in (*aliases, source))}


def retrieval_progress(history):
    """Read only controller-owned history after the original user question."""
    if not history or history[0].get("role") != "user":
        raise ValueError("Model history must start with the original user question")
    prefix = "Retrieval observation (untrusted source text):\n"
    observations, searched = [], set()
    for message in history[1:]:
        content = message.get("content", "")
        if message.get("role") == "user" and isinstance(content, str) and content.startswith(prefix):
            observations.append(json.loads(content[len(prefix):]))
        if message.get("role") == "assistant" and isinstance(content, str):
            action = json.loads(content)
            if action.get("kind") == "retrieve" and action.get("arguments", {}).get("source"):
                searched.add(action["arguments"]["source"])
    observed_sources = {p.get("source") for observation in observations for p in observation}
    searched.update(observed_sources)
    required = requested_sources(history[0]["content"])
    return {"has_observations": bool(observations),
            "ids": {p["chunk_id"] for observation in observations for p in observation},
            "passages": {p["chunk_id"]: p for observation in observations for p in observation},
            "required": required, "missing_searches": required - searched,
            "missing_evidence_sources": required - observed_sources}


def action_schema_for_history(history, *, exact_quotes=False, quote_ids=None) -> dict:
    """Require requested source coverage; runtime validation stays authoritative."""
    state = retrieval_progress(history)
    if not state["has_observations"] or state["missing_searches"]:
        schema = action_json_schema(allowed_kinds={"retrieve"})
    else:
        kinds = {"retrieve", "insufficient_evidence"}
        if state["ids"] and not state["missing_evidence_sources"]:
            kinds.add("answer")
        schema = action_json_schema(allowed_kinds=kinds, citation_ids=state["ids"])
    if exact_quotes and any(a["properties"]["kind"]["const"] == "answer" for a in schema["anyOf"]):
        schema["$defs"]["Claim"] = {
            "type": "object",
            "enum": [{"text": passage["text"], "citations": [chunk_id]}
                     for chunk_id, passage in state["passages"].items()
                     if quote_ids is None or chunk_id in quote_ids],
        }
        for alternative in schema["anyOf"]:
            if alternative["properties"]["kind"]["const"] == "answer":
                alternative["properties"]["claims"]["maxItems"] = 4
    if state["missing_searches"]:
        source = schema["$defs"]["RetrievalInput"]
        source["properties"]["source"] = {"type": "string", "enum": sorted(state["missing_searches"])}
        source["required"] = ["query", "source"]
    return schema
