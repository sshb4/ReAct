# Second local attempt — reviewed limitations

This is the actual nine-query Qwen3 4B run with reasoning disabled. All seven
document questions returned answer; Q8 incorrectly returned answer; Q9 returned
insufficient_evidence. Matching terminal reasons alone do not establish success.

Passage review found Q1 and Q4 fully supported, and Q9 an appropriate evidence
boundary. Q2, Q3 and Q5 had coverage/citation weaknesses. Q6 conflated medical
clearance conditions and never retrieved the Bad Bug Book. Q7 asserted handbook
alignment without handbook evidence. Q8 improperly inferred current legal
non-adoption from a historical study. See evidence-review.json and raw traces.

The next version adds mandatory named-source retrieval, explicit subpart
coverage/temporal/diagnosis instructions, and reasoning after source retrieval.
The full embedding index is reused; these failures have not been relabeled.
