# Daily Memory Update

1. Read latest authoritative task status, PRs, commits, test results (only what is retrievable).
2. Compare verified changes since previous report against phase files and `current-state.md`.
3. Create/update `memory/daily/YYYY-MM-DD.md` (manual or `scripts/daily_report.py`).
4. Label uncertain items as requiring confirmation.
5. Validate memory + links + secrets.
6. Branch + PR (never push to `main`).

## Modes

- **Manual:** documented command / `workflow_dispatch`.
- **Scheduled:** only after runtime, model/provider, permissions, secrets are genuinely configured. Make schedule and time zone explicit in config. If LLM unavailable, produce deterministic report and state that model-based summarization is not configured. Do not send reports to unapproved external services.