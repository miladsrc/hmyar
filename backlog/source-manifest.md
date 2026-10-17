# Source Manifest

Records where authorized source material lives. The original files are **not** committed (classification/permission not yet approved).

| ID | Source | Location (local) | Type | Classification | In Git? |
|---|---|---|---|---|---|
| SRC-WBS-001 | Hamtayar Backlog WBS | `C:\Users\m.barani\Downloads\Hamtayar_Backlog_WBS.xlsx` | xlsx (4 sheets) | Internal — permission to commit not confirmed | No (normalized export only) |
| SRC-ARCH-001 | Hamtayar Enterprise AI Architecture Platform | `C:\Users\m.barani\Downloads\Hamtayar Enterprise AI Architecture Platform.png` | png 1536x1024 | Internal — permission not confirmed | No |
| SRC-ARCH-002 | Hamtayar Production Architecture Diagram | `C:\Users\m.barani\Downloads\Hamtayar Production Architecture Diagram.png` | png 1536x1024 | Internal — permission not confirmed | No |
| SRC-ARCH-003 | Hamtayar architecture v2 (HD) | `C:\Users\m.barani\Downloads\hamtayar_architecture_v2_HD_3072.png` | png 3072x1865 | Internal — permission not confirmed | No |
| SRC-ARCH-004 | Hamtayar Knowledge Workflow Diagram | `C:\Users\m.barani\Downloads\Hamtayar_Knowledge_Workflow_Diagram.png` | png 2752x1536 | Internal — permission not confirmed | No |
| SRC-ARCH-005 | Hemtayar AI Platform Architecture | `C:\Users\m.barani\Downloads\Hemtayar AI Platform Architecture.png.jpeg` | jpeg 1500x1000 | Internal — permission not confirmed | No |
| SRC-REF-001 | Sahba cloud-platform docs (25 md) | `C:\Users\m.barani\Downloads\milad\PROJECT_DOCUMENTATION\` | md | Reference only — not Hamtayar | No |
| SRC-REF-002 | Sahba service repos | `C:\Users\m.barani\IdeaProjects\{cloud-platform,companiesservicesbackend,generalservicebackend,reportbakcend,framework}` | git | Reference only | No |

## Notes

- Until classification/permission is confirmed, only minimal non-sensitive summaries and normalized exports are committed. The original workbook and images are never committed.
- To regenerate the normalized export: `python scripts/ingest_wbs.py --source <path> --out backlog/normalized`.