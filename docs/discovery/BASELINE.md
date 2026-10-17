# Discovery Baseline

Date: 2026-10-17
Author: Sara (hmyar bootstrap)
Status: Stage A — Discovery and baseline

## 1. Environment

- Working directory: `C:\Users\m.barani\IdeaProjects\hmyar`
- OS: Windows (win32), PowerShell 5.1.
- This directory is a git repository with remote `https://github.com/miladsrc/hmyar.git` (branch `main`, one commit `bdd24d3 Initial commit` containing only `README.md`).
- GitHub authentication works via Windows Credential Manager (user `miladsrc`, 40-char token). `gh` CLI is **not** installed.
- Git config: `user.name=m.barani`, `user.email=baranimilad14@gmail.com`. Credential helper = `manager`.
- Available tools: `git 2.55`, `python 3.12`, `node`/`npm`, `java 26`, `mvn 3.9.6`, `docker`, `code` (VS Code), `curl`.
- Python packages installed: `openpyxl 3.1.5`, `pillow 13.0.0`, `pyyaml`. **Not** installed: `pandas`, `python-docx`, `markdown`, `jsonschema`. (Installed openpyxl and pillow during this bootstrap; documented here.)
- Model/LLM runtime: Ollama is installed on the host with `qwen2.5-coder:7b` available (per prior session memory). Not used by hmyar yet; provider adapter is `none` by default.
- Sara v2 Gateway (`http://127.0.0.1:8800`) is **down** during this session; direct execution disclosed.

## 2. Project inputs

### 2.1 WBS workbook

- Path: `C:\Users\m.barani\Downloads\Hamtayar_Backlog_WBS.xlsx`
- Sheets (4): `Backlog (WBS)`, `خلاصه اپیک‌ها` (Epic Summary), `سؤالات باز از کارفرما` (Open Questions), `راهنمای رنگ‌ها` (Color Legend).
- Validated counts:
  - Epics: 24
  - Features: 98
  - Tasks: 442
  - Task phase distribution: Phase 0: 62, Phase 1: 276, Phase 2: 51, Phase 3: 29, Phase 4: 9, Phase 5: 5, Proposed ideas: 10. (Matches the expected baseline exactly.)
  - Task proposed priority: P0: 313, P1: 90, P2: 39. (Matches expected baseline.)
  - All 442 tasks status = "انجام نشده" (not started).
  - Open questions: 11.
  - Color legend: green (proceed), yellow (proceed with recorded assumption), red (wait).
- Epic 24 = "Proposed Ideas (Outside the RFP, Approval Required)" — kept separate from committed scope.
- The workbook is **not** committed to this repository (confidentiality/storage policy not yet approved). Stored locally; only a minimal normalized export is committed. See `backlog/source-manifest.md`.

### 2.2 Architecture overview image

Candidate images found in `C:\Users\m.barani\Downloads\`:
- `Hamtayar Enterprise AI Architecture Platform.png` (1536x1024)
- `Hamtayar Production Architecture Diagram.png` (1536x1024)
- `hamtayar_architecture_v2_HD_3072.png` (3072x1865) — highest resolution
- `Hamtayar_Knowledge_Workflow_Diagram.png` (2752x1536)
- `Hemtayar AI Platform Architecture.png.jpeg` (1500x1000)
- `Cognia_Process_Map_FA.png` / `.svg`, `Enterprise_Knowledge_Workflow_Architecture_Diagram.png`, `Production Architecture with Custom Connector.png`, `Knowledge_Workflow_Architecture_Diagram.png`

No vision/OCR tool is available in this environment to transcribe image content into text. Architecture documentation below is based on the prompt's high-level description plus the Sahba/cloud-platform docs where applicable. The architecture image is recorded in the source manifest; it is **not** committed (pending classification approval).

## 3. Capabilities

| Capability | Status |
|---|---|
| Git (clone/pull/branch/commit/push) | Available; push to `origin` verified via `git ls-remote`. |
| GitHub repository creation | Not needed — repo exists (`miladsrc/hmyar`). |
| GitHub Issues / PRs | No `gh` CLI. PRs can be created via the GitHub REST API using the stored credential (manual/scripted). Branch + push works; PR creation is a manual step unless scripted. |
| Scheduled execution | Not configured. GitHub Actions `workflow_dispatch` is the realistic manual trigger; cron schedule is configurable but only enable after secrets/runtime are set. |
| LLM invocation | Ollama available on host; hmyar defaults to `provider: none` (deterministic) until approved. |
| Test execution | pytest available once installed; Python stdlib + openpyxl + pyyaml + pillow. |
| WBS ingestion | Implemented in `scripts/ingest_wbs.py` (Stage C). |
| Memory validation | Implemented in `scripts/validate_memory.py`. |
| Link checking | Implemented in `scripts/check_links.py`. |
| Secret scanning | Implemented in `scripts/check_secrets.py`. |
| Daily report | Implemented in `scripts/daily_report.py` (deterministic; no LLM). |

## 4. Existing contracts / documentation

- No prior Hamtayar code or specs exist in this repository (only `README.md`).
- Reference material (read-only, not copied): `C:\Users\m.barani\Downloads\milad\PROJECT_DOCUMENTATION\` (25 markdown files describing the Sahba cloud-platform: OBS/CBAC access management, Spring Boot 2.5.6, PostgreSQL, Liquibase, gateway/oauth/user/cache/log services). Used only as an example of a documented enterprise platform; **not** assumed to be Hamtayar's stack.
- Sahba service repos exist under `C:\Users\m.barani\IdeaProjects\` (cloud-platform, companiesservicesbackend, generalservicebackend, reportbakcend, framework) — reference only.

## 5. Shared knowledge location

- Primary: this Git repository (`https://github.com/miladsrc/hmyar.git`), branch `main`.
- All team members with repo access clone/pull and read committed knowledge.
- Task execution status authority: **not yet decided** (GitHub Issues/Projects vs Jira). Recorded as open question OQ-STATUS. WBS references Jira; no bulk Issue creation without approval.

## 6. Blockers / decisions needed

See `backlog/open-questions.md`. Key blockers:
- OQ-STATUS: authoritative task status source (GitHub Issues/Projects vs Jira) and sync policy.
- OQ-VISIBILITY: repository is currently **public**; prompt default is private. Decision needed (admin access available).
- OQ-STACK: technology stack (language, DB, model, cloud, framework) undecided — do not choose by preference.
- OQ-CLASSIFICATION: confidentiality/permission to store the WBS and architecture image in Git.<|end|>