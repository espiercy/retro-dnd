# ISSUE-015: Shared Currency Primitive (CLUSTER-003 Slice A)

## 1. Issue/Task Identifier and Objective

ISSUE-015 (completion-record ledger). Implement **Slice A** of
`docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §10: the shared
exact-money primitive `CHAR-004` needs now and `TREAS-*`/`ADV-003` are
expected to need later.

**Representation only.** No prices, no items, no class rules, no
starting-gold generation.

**Status: accepted by the human project owner, 2026-09-25**, subject to two
housekeeping items that were completed the same day.

## 2. Approved Inputs/Specifications

- `docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §5.1, §6.1, §10
  (Slice A) — the approved implementation contract.
- `docs/rules/character_creation/starting_equipment_and_expedition_preparation.md`
  §4 (`CHAR-004`, `APPROVED`) — RC's conversion line, the only rules input.
- `ARCHITECTURE.md` §15.2 step 4 — implementation-readiness re-approval.
- RC Ch. 4 p. 62 — `1 pp = 5 gp = 10 ep = 50 sp = 500 cp`.

## 3. Files Created, Modified, or Deleted

**Created:** `src/rules/currency.py`, `tests/rules/test_currency.py`, this
completion record.

**Modified:** `docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` (§6.1
conversion-note correction), `docs/completion-records/INDEX.md`.

**Deleted:** none.

Committed on `cluster-003-stage-a-evidence` (`eda2378`, housekeeping
`0fdc4a0`). **Not merged.**

## 4. Behavior Actually Implemented

- `Denomination` — the five RC coin names, identity only.
- `IN_COPPER` — each denomination's worth in copper, derived from RC's
  single conversion statement: PP 500, GP 100, EP 50, SP 10, CP 1.
  Public, because it *is* the approved RC conversion; immutable.
- `Coin` — a frozen, slotted value object storing one non-negative `int`
  of copper pieces. Addition, subtraction, integer multiplication,
  `scaled(numerator, denominator)`, and ordering.

**No floating point is used, produced or accepted.** `scaled()` is exact
or refused: a ratio that would not land on a whole copper piece raises
rather than rounding, because RC names no smaller unit. Non-negative by
construction, since RC states no negative price or debt in any approved V1
rule. `bool` is excluded explicitly at every entry boundary.

## 5. Rules Provenance

| Element | Classification |
|---|---|
| The five denominations and `IN_COPPER` | **Rules Cyclopedia Explicit** (Ch. 4 p. 62) |
| Copper as the stored unit; exact-or-refuse scaling | **Implementation choice**, plan §5.1. Changes no rule |

**No Simulator Ruling, no Compatible Completion, no Variant.**

## 6. Tests Added or Modified

`tests/rules/test_currency.py` — 64 tests: exact representation
(`4.5 gp = 45 sp = 450 cp`), the Druid surcharge's exactness, arithmetic,
ordering, immutability, `IN_COPPER` immutability, rejection of non-`int`
and `bool`, and an ownership-boundary guard asserting the module exposes
no catalog, price or purchasing symbol.

## 7. Exact Verification Commands Executed

```text
uv run python scripts/verify.py
```

## 8. Verification Results

```text
Tests:     PASS
Coverage:  PASS
Ruff:      PASS
mypy:      PASS
Overall:   PASS
```

## 9. Coverage Results

`src/rules/currency.py` — **100% branch, 0 missed**.

## 10. Deviations

1. **`IN_COPPER` values** were derived from RC's authoritative conversion
   line rather than the plan's inline note, which was garbled
   (`"pp=500 ep=10 gp=10 sp=10 cp=1"`). A plan-prose defect, not a
   behavioural deviation; the plan text was corrected in `0fdc4a0`.
2. **`Coin.of()`** rather than the plan's `Coin.from_()`.
3. **`IN_COPPER` public** rather than the plan's `_IN_COPPER`.
4. **No new error type** — plain `ValueError` per the `turn_credit.py`
   shared-value-object precedent. The plan's §6.5 list belongs to Slices
   B–D.

All four were reviewed and approved by the human project owner on
2026-09-25.

## 11. Known Limitations/Unresolved Issues

- **Negative amounts are not representable.** If a debt mechanic is ever
  approved, it is a rules question for its own card, not a representation
  this primitive should have pre-built.
- **A price is not always one `Coin`.** Discovered in Slice B and resolved
  there by `CHAR-004` §4.1's price-specification forms. `Coin` was
  deliberately **not** changed.

## 12. Architectural Consequences

One new shared primitive, owned by no single Rule Card, following the
`character_class.py` / `turn_credit.py` precedent. It introduced no new
architectural style: a frozen slotted value object with pure integer
operations, matching `RollResult` and `TurnCredit`.

## 13. Acceptance

- Accepted by: **Human project owner**
- Date: **2026-09-25**
- Notes: Accepted subject to two housekeeping items — confirm `IN_COPPER`
  immutability (already immutable; a test was added) and correct the
  implementation plan's conversion note (done). The design decisions listed
  in §10 were explicitly approved and are not to be reopened without a
  genuine contradiction.
