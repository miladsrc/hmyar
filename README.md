# hmyar

`hmyar` is the engineering agent and shared knowledge base for the **Hamtayar** enterprise AI project.

It is a standalone repository. It is **not** a subdirectory or branch of `ai-swe-engine` and does not depend on it at runtime.

## What this repository is

- The **durable, version-controlled, shared knowledge base** for the Hamtayar project and for the agent itself.
- A small, deterministic toolchain for ingesting the Hamtayar WBS, validating shared memory, and producing daily reports.
- The place where approved facts, decisions (ADRs), open questions, phase plans, and lessons learned live — reviewable via Git and Pull Requests.

## What this repository is not

- Not a generic chatbot. `hmyar` is a controlled engineering teammate.
- Not the system of record for task execution status. Task status authority is decided by the team (see `backlog/README.md`).
- Not a place for secrets, customer data, proprietary source documents, or the original WBS workbook.

## Repository layout

See the top-level directories:

- `docs/` — discovery baseline, architecture notes, working agreements, ADRs, runbooks.
- `backlog/` — WBS source manifest, normalized (reproducible) exports, open questions.
- `memory/` — current state, phase roadmap, per-phase files, decisions, daily reports, lessons learned.
- `workflows/` — task lifecycle, daily memory update, phase gate.
- `scripts/` — ingestion, validation, daily report, link/secret checks.
- `tests/` — pytest tests for ingestion and validation.
- `.github/` — issue/PR templates and CI.

## Quick start

```powershell
# 1. Clone
git clone https://github.com/miladsrc/hmyar.git
cd hmyar

# 2. (Optional) Python environment for scripts
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 3. Validate shared memory
python scripts/validate_memory.py

# 4. Ingest the WBS (source workbook is NOT committed; place it locally first)
python scripts/ingest_wbs.py --source "C:\path\to\Hamtayar_Backlog_WBS.xlsx" --out backlog/normalized

# 5. Generate a daily report (deterministic; no LLM required)
python scripts/daily_report.py --date (Get-Date -Format yyyy-MM-dd)
```

## Configuration

Copy `config/hmyar.example.yaml` to `config/hmyar.yaml` (gitignored) and fill in local values.
Never commit `config/hmyar.yaml`.

## Contributing knowledge

1. Read `AGENTS.md` and `docs/working-agreements.md`.
2. Branch from `main`: `git checkout -b knowledge/<short-topic>`.
3. Update the relevant small files; add cross-links.
4. Run `python scripts/validate_memory.py` and `python scripts/check_links.py`.
5. Open a Pull Request. Do not push to `main`.

## License

Internal project. License TBD by product owner.