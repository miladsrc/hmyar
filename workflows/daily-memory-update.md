# Daily Memory Update

1. Read latest authoritative task status, PRs, commits, test results (only what is retrievable).
2. Compare verified changes since previous report against phase files and `current-state.md`.
3. Create/update `memory/daily/YYYY-MM-DD.md` (manual or `scripts/daily_report.py`).
4. Label uncertain items as requiring confirmation.
5. Validate memory + links + secrets.
6. Branch + PR (never push to `main`).

## Modes

- **Manual:** documented command / `workflow_dispatch`.
- **Scheduled:** GitHub Actions cron at 14:31 Asia/Tehran (see `.github/workflows/daily-report.yml`). Only enable after runtime, model/provider, permissions, secrets are genuinely configured. Make schedule and time zone explicit in config. If LLM unavailable, produce deterministic report and state that model-based summarization is not configured. Do not send reports to unapproved external services.

## Team collaboration (5 people: 4 devs + 1 team lead)

1. Read latest authoritative task status, PRs, commits, test results (only what is retrievable).
2. Compare verified changes since previous report against phase files and `current-state.md`.
3. Attribute activity to team members where author info is available; label unverified attribution.
4. Identify blockers, yellow/red items, and propose next steps per `task-lifecycle.md`.
5. Create/update `memory/daily/YYYY-MM-DD.md` (manual or `scripts/daily_report.py`).
6. Label uncertain items as requiring confirmation.
7. Validate memory + links + secrets.
8. Branch + PR (never push to `main`). Record what changed, evidence, and what needs human review.

## References

- Team roster (placeholders): `docs/team.md`
- Decision: `docs/decisions/ADR-001-daily-collaboration.md`
- Task lifecycle: `workflows/task-lifecycle.md`