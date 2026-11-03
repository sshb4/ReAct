# First local attempt — retained failures

All nine runs ended in error using qwen2.5:1.5b. Eight attempted a final answer
without retrieval and were rejected for invented citations; Q6 hit the model
output token limit. No query in this attempt produced a supported answer.

The next implementation constrains the first model action to retrieval and
restricts generated citation IDs to controller-produced observations. Runtime
validation is retained. These are original real traces, not successful results.
