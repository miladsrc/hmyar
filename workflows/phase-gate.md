# Phase Gate

A phase is approved only when:

- Its exit criteria are met with verified evidence (file path, commit/PR, command output, test result).
- The product owner explicitly approves phase completion.
- Completion of a few tasks does not by itself imply phase approval.

Phase status values: `not started` | `in progress` | `exit criteria met (pending approval)` | `approved` | `blocked`.