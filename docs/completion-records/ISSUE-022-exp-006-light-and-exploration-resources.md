# ISSUE-022 — `EXP-006` Light & Exploration Resources — Implementation

```text
STATUS:      IMPLEMENTATION COMPLETE -- pending a passing independent final review
BRANCH:      cluster-004-exp-006-stage-b   (unmerged, unpushed)
CARD:        EXP-006, APPROVED 2026-10-01, carrying SR-11
PLAN:        docs/technical/EXP-006_IMPLEMENTATION_PLAN.md, APPROVED 2026-10-01
GATE:        EXP-006 PRE-CODE GATE: PASS 2026-10-01, revalidated (ignition portion) same day
```

> **This record does not represent the issue as complete.** `DEVELOPMENT_WORKFLOW.md` §5.1 forbids
> that while required verification is outstanding, and **the first independent final
> implementation review returned `FAIL`**. A second independent review is required, and completion
> is a human act.

## 1. What was built

| Artifact | Lines | Contents |
|---|---|---|
| `src/rules/exploration/light_and_exploration_resources.py` | ~640 | value model, depletion, contribution, ignition selector (`SR-11`), `CHAR-004` identity binding |
| `src/rules/exploration/errors.py` | ~125 | `IgnitionNotDefinedError`, `IgnitionAttemptLimitError`, `LanternRefuelNotDefinedError` |
| `tests/rules/exploration/test_light_and_exploration_resources.py` | ~1200 | the 53-case ledger, behaviour, invariants and the structural guard suite |

## 2. Current state of record — all artifacts agree

```text
Rule Card            APPROVED            2026-10-01
Pre-Code Gate        PASS + REVALIDATED  2026-10-01
Implementation Plan  APPROVED            2026-10-01
Slice A              ACCEPTED            2026-10-01
Slice B              ACCEPTED            2026-10-01   (incl. two bounded corrections)
Slice C              ACCEPTED            2026-10-01   (incl. one bounded correction)
Slice D              ACCEPTED            2026-10-03
Implementation       COMPLETE -- pending independent final review PASS
SR-11                ALLOCATED and registered in four places
```

**`SR-11` registration** — Rule Card §Simulator Ruling; `CLUSTER-004` cluster record §10;
`INVENTORY.md`'s `EXP-006` row; implementation plan §11. `ARCHITECTURE.md` §15.2 previously
**denied** it and was corrected 2026-10-03 (`HIGH-1`).

## 3. Chronology — preserved, not rewritten

| Date | Event | Outcome |
|---|---|---|
| 2026-09-29 | Stage A accepted after **five** independent completeness reviews | 4 × `FAIL`, then `PASS` |
| 2026-10-01 | Rule Card remediation (Findings A–C), then approval | `APPROVED` |
| 2026-10-01 | Pre-Code Gate, then bounded revalidation of the ignition portion | `PASS` |
| 2026-10-01 | Slices A–C, with three bounded corrections | accepted |
| 2026-10-03 | Slice D | accepted |
| 2026-10-03 | **Independent final implementation review #1** | **`FAIL`** — 2 HIGH, 4 MED, 8 LOW |
| 2026-10-03 | Bounded remediation of all 14 findings | this record |
| — | Independent final implementation review #2 | pending |

**No past `FAIL` or `PASS` event is relabelled.** The `FAIL` review artifact is preserved
unaltered, and the four Stage-A `FAIL` reviews likewise stand.

## 4. Deterministic cases

**53**, enumerated from the card rather than counted forward: 20 implemented behavior,
5 implemented invariant, 26 architectural guard, 2 routed/non-owned. The categories were
**recomputed from the actual mechanisms** during the 2026-10-03 remediation rather than carried
over — the previous split overclaimed what several guards established.

## 5. Verification

`uv run python scripts/verify.py` — tests, coverage, Ruff, mypy strict, Evidence, policy: **all
PASS**. Per-file coverage **100% statement and branch** on both production modules.

## 6. Known-incomplete behavior

**None within the card's scope.** Seven RC silences are named and guarded rather than filled, by
express approval. One adjacent governance gap is recorded and deliberately unresolved:

```text
GLOBAL COMPLETE-DARKNESS WORLD-STATE PREDICATE
    Owner:   unresolved
    Rule ID: none settled
    Not an EXP-006 dependency; binds before ENC-001 / darkness-related COMBAT-*.
```

**Rations** and **starvation causation** remain deliberately unassigned.

## 7. Not authorized by this record

Merge, push, `CLUSTER-004` implementation, `ENC-005` Stage B, and any new Stage-A card.
