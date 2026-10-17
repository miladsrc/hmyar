# Open Questions

Traceable list of decisions and unknowns. Never delete a question. Status: `open` | `answered` | `deferred`.

## From WBS (`سؤالات باز از کارفرما`)

| # | Topic | Question | Impact | Blocking severity | Owner | Status | Answer date |
|---|---|---|---|---|---|---|---|
| OQ-1 | SLA/Performance | Target latency (P95/P99), RPS, and concurrency are undefined. | Technology choice, scalability, performance testing. | High | Product owner / customer | open | — |
| OQ-2 | Data volume | Number of documents, repositories, lines of code, and annual growth? | Vector DB choice, sharding, hardware. | High | Product owner / customer | open | — |
| OQ-3 | LLM | Which approved external LLM service? Cloud or on-prem? Security protocol and token cost? | RAG path design and security. | High | Product owner / customer | open | — |
| OQ-4 | Padin | Padin tech stack, API protocol, plugin model, ACL format, access-change events? | API contracts and integration. | High | Product owner / customer | open | — |
| OQ-5 | Infrastructure | Allocated server resources and GPU? Air-gapped environment? Internet access for model downloads? | Model choice, deployment. | High | Product owner / customer | open | — |
| OQ-6 | Code | Required programming languages? Graph depth (imports only vs full call graph)? | Code-graph effort. | Medium | Product owner / customer | open | — |
| OQ-7 | Quality | Acceptance thresholds for retrieval quality (Recall@K, MRR, NDCG)? Does customer provide a Golden Set? | Phase 2 acceptance criteria. | Medium | Product owner / customer | open | — |
| OQ-8 | Security | Need for PII detection, confidentiality classification, customer-mandated security standards? | Security and audit. | Medium | Product owner / customer | open | — |
| OQ-9 | Schedule | Duration of each phase and expected pilot date? | Resource planning. | Medium | Product owner / customer | open | — |
| OQ-10 | Language | Ratio of Persian/English content? Scanned documents (OCR) present? | Model and OCR choice. | Medium | Product owner / customer | open | — |
| OQ-11 | Sync | Source-change sync speed (real-time vs minute-level)? | Event-driven architecture. | Medium | Product owner / customer | open | — |

## Project-level (added during bootstrap)

| ID | Topic | Question | Impact | Blocking severity | Owner | Status | Answer date |
|---|---|---|---|---|---|---|---|
| OQ-STATUS | Task status authority | Is execution status authoritative in GitHub Issues/Projects, Jira, or another register? Sync policy? | Bulk Issue creation, reporting. | High | Product owner + team | open | — |
| OQ-VISIBILITY | Repo visibility | Repository is currently public; prompt default is private. Change to private? | Access control, confidentiality. | Medium | Product owner | open | — |
| OQ-STACK | Technology stack | Language, database, model, cloud, framework undecided. Prepare options; do not choose by preference. | Entire implementation. | High | Product owner + architects | open | — |
| OQ-CLASSIFICATION | Source storage policy | Permission to store WBS and architecture images in Git? | What gets committed. | Medium | Product owner | open | — |
| OQ-PHASE | Approved active phase | Which phase is approved to start? (WBS marks all tasks not started.) | Work selection. | High | Product owner | open | — |
Callout: WBS color legend — green items may proceed independently; yellow require a recorded reversible assumption; red must wait.