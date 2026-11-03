Unit U0: ReAct agents, tool use, vector databases, and document retrieval
Due: October 29, 2026, at 9:30 a.m. MDT
Submission cutoff: November 5, 2026, at 9:30 a.m. MST
Points: 10

Purpose And Learning Outcomes
This assignment extends your prior ReAct-agent work with document retrieval. You will ingest supplied source documents into ChromaDB and give an agent a retrieval tool that it can use to answer questions from those documents.

By completing this assignment, you will:

construct a persistent vector index from a multi-document corpus;
expose semantic retrieval through a validated, typed agent tool;
enforce evidence and termination policies in a bounded ReAct controller;
distinguish supported answers from insufficient-evidence outcomes; and
test the system without requiring live model services.
Materials
Download and extract the U0-HW-09 materials package. It contains:

README.md, which identifies the source documents and explains their roles;
U0-HW-09-required-queries.md, which defines the nine required runs;
model-service.env.example, which provides the course service settings; and
documents/, which contains the five PDFs to ingest.
Use the complete supplied corpus. Do not replace the documents with excerpts. The corpus contains 1,110 PDF pages, so a clean build can take several minutes. Do not commit the supplied PDFs to your project repository.

Task
Build a ReAct agent that uses a Chroma vector store to answer questions from the supplied source-document corpus. Use Qwen3-Embedding-8B to embed document chunks and queries.

There is no direct starter code. Your previous assignments contain ReAct-loop and tool-use implementations. The Lecture 170 vector-retrieval example demonstrates PDF ingestion, chunking, embedding, ChromaDB persistence, retrieval, and environment configuration. You may adapt those materials or implement your own design.

Your system must:

ingest all five supplied PDFs into a persistent Chroma vector store;
preserve the source filename or title, one-based physical PDF page, and a stable chunk identifier in each chunk's metadata;
expose retrieval as a validated, typed agent tool;
return passage text and source, page, and chunk labels in each retrieval observation;
limit final claims and citations to retrieved evidence;
report when the retrieved documents do not support an answer;
record an inspectable action-observation trace; and
enforce a configurable model/tool step limit and record whether execution ended with an answer, insufficient evidence, an error, or the step limit.
Use the model-service configuration in the supplied model-service.env.example, which matches the Lecture 170 vector-retrieval example. Use Qwen3-Embedding-8B for document and query embeddings. Provide a vector-store rebuild command. Keep API keys, .env, supplied PDFs, generated database files, and other local runtime files out of Git.

The application must validate tool arguments, citations, the step limit, and the terminal reason. A citation is valid only if its chunk identifier was returned by retrieval during that run. Citation matching establishes chunk provenance. Evaluate whether each claim follows from its cited passage in your tests and required-query results.

Required Queries
Run every query in U0-HW-09-required-queries.md exactly as provided, using one recorded configuration, and retain each complete action-observation trace and final result. The set includes document-specific, cross-document, insufficient-evidence, and off-topic cases. Q1 through Q7 should end with source-supported answers. Q8 and Q9 should end with insufficient-evidence results.

Record the embedding model, chunk size and overlap, retrieval result count, and model/tool step limit used for all required runs.

Use source roles and publication versions accurately. The FDA Food Code is a model code, the employee-health handbook is guidance based on an earlier Food Code edition, the Bad Bug Book is pathogen reference material, Appendix 3 is draft nonbinding scientific guidance, and the Utah study reports historical inspection observations. The supplied corpus does not identify a current Utah adoption rule or its penalties.

Automated Tests
Provide passing automated tests that run without live model or embedding services. At minimum, test:

ingestion metadata for source, one-based physical PDF page, and stable chunk identifier;
retrieval-tool argument validation and source-labeled results;
rejection of a citation that retrieval did not return;
enforcement of the model/tool step limit;
all four terminal reasons; and
at least one supported run and one insufficient-evidence run using scripted model actions and substitute retrieval results.
Required Submission
Submit one PDF through Canvas. The PDF supplies the URL for a Git repository that remains available to the instructor. Together, the submission consists of:

Git repository: Include the complete project, automated tests, required-query results and traces, and instructions for configuring and running the system. State the required Python version, dependency-installation command, vector-store rebuild command, query command, and test command. Do not commit credentials, .env, supplied PDFs, or generated Chroma data.
PDF report: Include the repository URL and a concise description of the agent's task, tools, vector-store design, source-attribution method, test results, required-query outcomes, and observed limitations. Include the recorded configuration and identify any query that did not end with the expected supported or insufficient-evidence outcome.
Name the report lastname-firstname-vector-retrieval.pdf. It must contain selectable text, semantic headings, logical reading order, and scoped headers for any data table. Include an AI-assistance disclosure with one bullet per tool naming the tool, its material effect, and how you verified its contributions, or the exact statement No AI assistance used.

Late Work
The due time is October 29, 2026, at 9:30 a.m. MDT. Canvas remains available until November 5, 2026, at 9:30 a.m. MST for the course's limited late/correction window. Submissions during this window remain subject to the course late-work policy; the open window does not waive a penalty. Work after the cutoff is accepted only under university policy or an approved accommodation.

U0-HW-09: ReAct Agent With Vector Retrieval Rubric
Criteria	Ratings	Points
Vector Retrieval System

Meets criterion
Provides a functional, reproducible system that ingests the complete supplied corpus into persistent Chroma storage with Qwen3-Embedding-8B, preserves the required source, page, and chunk metadata, and retrieves relevant source-labeled passages through a validated typed tool.
3 pts

Partially meets
Provides a usable ingestion and retrieval system, but substantial defects in corpus completeness, persistence, metadata, tool validation, retrieval quality, attribution, or rebuild instructions limit its reliability or reproducibility.
1.5 pts

No demonstrated achievement
Provides no usable vector-store ingestion and retrieval system.
0 pts
/3 pts
Agent Control And Evidence Use

Meets criterion
Implements a bounded ReAct agent that validates tool arguments and citations, returns passage text with source, page, and chunk labels, records inspectable action-observation traces, enforces a configurable model/tool step limit, records explicit terminal reasons, produces source-supported answers, and returns appropriate insufficient-evidence results.
3 pts

Partially meets
Implements a recognizable model-tool loop, but substantial defects in tool or citation validation, retrieval observations, tracing, step-limit enforcement, termination, claim support, or insufficient-evidence behavior reduce its reliability.
1.5 pts

No demonstrated achievement
Provides no functional bounded agent that uses retrieved evidence to control its answers.
0 pts
/3 pts
Required Query Results

Meets criterion
Runs all nine required queries exactly as written under one configuration that records the embedding model, chunk size and overlap, retrieval result count, and model/tool step limit; retains each trace; produces passage-supported answers for Q1-Q7 with accurate source-role and version distinctions; and returns insufficient evidence for Q8-Q9.
2 pts

Partially meets
Provides reviewable results for most required queries, but missing traces or configuration fields, inconsistent settings, unsupported claims, source-role errors, or incorrect evidence outcomes materially weaken the result set.
1 pts

No demonstrated achievement
Provides no reviewable required-query result set.
0 pts
/2 pts
Testing, Repository, And Report

Meets criterion
Provides meaningful offline automated tests of ingestion, retrieval, controller, citation, and step-limit behavior, all four terminal reasons, and scripted supported and insufficient-evidence runs; a complete and secure repository with reproducible setup and run instructions; and an accessible PDF report that accurately describes the system, results, tests, and limitations and includes the required AI-assistance disclosure.
2 pts

Partially meets
The tests, repository, and report make the project substantially reviewable, but missing required coverage, artifacts, instructions, security controls, report content, AI-assistance disclosure, or accessibility features materially limit verification or reproducibility.
1 pts

No demonstrated achievement
The project cannot be meaningfully tested or reviewed, or the required repository and report are absent.
0 pts
/2 pts
