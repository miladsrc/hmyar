# Working Agreements

## Knowledge changes

- Small, purpose-specific files; cross-links and indexes.
- Distinguish approved fact / proposal / assumption / open question / observed result.
- Every change needs a traceable origin: WBS, Issue, PR, ADR, product-owner instruction, or observed execution result.
- Branch + PR; never push to `main`. No auto-merge of architecture/phase/product decisions.

## Task execution

- Find WBS/Issue id, acceptance criteria, dependencies, risks, approved active phase before starting.
- Green: proceed. Yellow: record assumption (owner, rationale, impact). Red: do not implement; record question.
- Claims of "implemented"/"tests passed" require evidence.

## Secrets

- Never commit secrets. Run `scripts/check_secrets.py` before committing.

## Conflict resolution

- Use Git reviews; do not silently overwrite another teammate's knowledge. Resolve conflicts explicitly and preserve decision history.