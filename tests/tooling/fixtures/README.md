# Evidence-linter fixtures

Test fixtures for `scripts/lint_evidence.py` (`DEC-0012`).

**These are not evidence.** Nothing here is Stage-A research, none of it was
researched against the Rules Cyclopedia, and no statement in it may be cited as a
source fact or a repository fact. `TEST-900` is a fictional Rule ID that does not
appear in `docs/rules/INVENTORY.md` and never will.

They live here, under `tests/`, rather than in `docs/rules/evidence/` precisely so
that a fabricated packet can never be mistaken for real research or picked up by
the linter's own directory scan. The linter scans `docs/rules/evidence/` only.

| File | Purpose |
|---|---|
| `TEST-900-evidence-compliant.md` | A **new** (non-grandfathered) packet that must lint clean. Proves a conforming post-`DEC-0012` packet passes, which a repository of only grandfathered packets cannot demonstrate. |
| `TEST-900-evidence-malformed-absence.md` | Asserts absence with no Negative Claim Record, and drops the ledger's explicit `NONE`. Must fail `E010`/`E011`. |
| `TEST-900-evidence-malformed-coverage.md` | Carries an evidence row for a page on no inspection list, and a `BLOCKED` closure item beside an `EVIDENCE READY` recommendation. Must fail `E006`/`E009`. |
| `TEST-900-evidence-malformed-skeletal.md` | A plausible-looking packet with none of the required instruments. Must fail `E001` and the ledger checks. |

The malformed fixtures are modelled on defects actually recorded in
`docs/rules/evidence/CLUSTER-004-stage-a-completeness-review*.md`, so that if a
check stops firing on the defect it was built for, a test fails.
