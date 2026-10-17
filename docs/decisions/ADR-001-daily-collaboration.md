# ADR-001 — Daily collaboration routine and automated memory report

- **Status:** proposed
- **Date:** 2026-10-17
- **Owner:** hmyar (Sara)
- **Related:** OQ-STATUS, OQ-PHASE; `workflows/daily-memory-update.md`; `.github/workflows/daily-report.yml`

### Context
The team (5 people: 4 developers + 1 team lead) collaborates on Hamtayar. We need a predictable daily routine to capture what the team works on, assist, and keep shared memory traceable. Task status authority is undecided (OQ-STATUS), so evidence is limited to git activity until a register is chosen.

### Options
1. Manual only — Sara runs the daily report on demand. Low automation, depends on session presence.
2. Scheduled deterministic CI report (chosen) — GitHub Actions cron at 14:31 Asia/Tehran generates `memory/daily/YYYY-MM-DD.md` and opens a PR. No LLM; no auto-merge.
3. Scheduled report with LLM summarization — requires an approved provider and secrets; deferred.

### Decision
Adopt option 2 as the baseline, with option 1 (interactive help) on top. LLM summarization stays disabled until a provider is approved (config `llm.provider`).

### Rationale
Deterministic output is reproducible and reviewable; PR-based updates preserve "never push to main" and "no auto-merge of decisions". Fixed Tehran offset (UTC+03:30, no DST) makes the cron unambiguous.

### Consequences
- A PR is opened each day the report changes; requires human review/merge.
- Status authority still open; report labels unverified items as "requires confirmation".
- If the repo is made private or access changes, the workflow's GITHUB_TOKEN permissions must be re-checked.

### Approval
- Product owner: pending.
- Team lead: pending.
