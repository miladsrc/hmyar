# Project Overview — Hamtayar

Hamtayar is an enterprise AI platform for organizational knowledge and question answering, delivered in collaboration with the **Padin** framework. This overview is derived from the master build prompt and the WBS; it does not copy any proprietary source document.

## High-level flow (from prompt)

- End users interact with organizational knowledge and Q&A capabilities through the **Padin** environment.
- Organizational knowledge sources (documentation, GitLab, Jira, ...) reach Hamtayar through the organizational integration/Padin path shown in the architecture overview image. Exact connector contracts and ownership are to be established from approved documents/decisions.
- Hamtayar processes incoming content: extracts document content and semantic information; stores in vector, relational, and graph storage where required by the approved design.
- The question/search/retrieval path is distinct from the ingestion path.
- Retrieved evidence is made available to an LLM for answer generation; the response returns to the user environment through the approved integration path.

## Backlog domains (from WBS epics)

Padin integration, architecture, ingestion, text processing/NLP, code analysis and Code Graph, Embedding/Reranker/LLM, vector/graph/full-text/relational storage, knowledge lifecycle, retrieval, security and access control, RAG, agent/tool execution, API/backend, UI/UX, quality evaluation, observability, performance, DevOps/DR, testing, pilot, documentation, advanced capabilities.

## Technology stack

**Undecided.** Do not select a language, database, model, cloud service, or framework by preference. Prepare options, evaluation criteria, and evidence; record major decisions as ADRs for approval (OQ-STACK).

## Status of this document

Proposal-level. Architecture decisions require ADRs and product-owner approval before being treated as final.