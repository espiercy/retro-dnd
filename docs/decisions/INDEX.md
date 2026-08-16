# Decision Log Index

Durable architectural and process decisions for the Retro D&D Simulator project. This index is a scan-only summary — see the individual records for full content; do not duplicate decision content here.

| ID | Title | Status | Date |
|----|-------|--------|------|
| [DEC-0001](DEC-0001-project-foundation-baseline.md) | Project Foundation Baseline | Approved | 2026-08-15 |
| [DEC-0002](DEC-0002-rng-contract.md) | RNG Contract — Single-Stream, Rules-Facing Dice Abstraction | Approved | 2026-08-15 |
| [DEC-0003](DEC-0003-python-toolchain-and-ci.md) | Python Toolchain and CI Enforcement Model | Approved | 2026-08-15 |
| [DEC-0004](DEC-0004-full-v1-rules-corpus-before-implementation.md) | Full V1 Rules Corpus Required Before Historical-Rules Implementation | Superseded by DEC-0005 | 2026-08-15 |
| [DEC-0005](DEC-0005-v1-rules-inventory-and-clustered-implementation.md) | V1 Rules Inventory and Dependency-Complete Implementation Clusters | Approved | 2026-08-15 |
| [DEC-0006](DEC-0006-v1-playable-content-scope.md) | V1 Playable-Content Scope: Full 1974-Core Progression, Three-Book Boundary | Superseded by DEC-0007 | 2026-08-15 |
| [DEC-0007](DEC-0007-rules-cyclopedia-primary-rules-authority.md) | Rules Cyclopedia as Primary Rules Authority | Approved | 2026-08-16 |

## Adding a Decision Record

- Assign the next sequential, zero-padded four-digit ID (`DEC-0002`, `DEC-0003`, ...). IDs are never reused, even for an abandoned or rejected decision.
- Use the format defined in `DEVELOPMENT_WORKFLOW.md` §9.3 (Decision ID, Title, Status, Date, Context, Decision, Rationale, Consequences, Supersedes, Superseded By).
- Add a row to the table above.
- Approved decision records are historical. Do not rewrite one because the project later decides differently — supersede it instead (`DEVELOPMENT_WORKFLOW.md` §9.4) and update both records' `Supersedes` / `Superseded By` fields and this table's `Status` column.
