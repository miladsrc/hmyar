# Task Lifecycle

1. **Intake** — identify WBS/Issue id, acceptance criteria, dependencies, risks, approved active phase.
2. **Eligibility** — green: proceed; yellow: record assumption; red: stop and record question.
3. **Plan** — small implementation plan with verification steps.
4. **Branch** — `task/<wbs-id>` or `knowledge/<topic>`.
5. **Implement** — focused changes.
6. **Test** — run relevant tests; record command + output.
7. **Review** — diff review; security check.
8. **Record** — update memory/daily, phase file, decisions as needed.
9. **PR** — open PR with summary, rationale, changed files, tests, risks, approvals.
10. **Handoff** — propose next step. Never auto-merge.