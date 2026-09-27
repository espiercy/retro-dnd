# ISSUE-020: CLUSTER-003 Cross-Card Integration and Case Reconciliation (Slice F)

## 1. Issue/Task Identifier and Objective

ISSUE-020 (completion-record ledger). Implement **Slice F** of
`docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §10: prove the chain
with real components, reconcile every approved case against exactly one
owning test, and complete the cluster records.

**This slice adds no production code.** Tests and records only.

**Status: awaiting human review.** `CLUSTER-003` implementation is complete
on `cluster-003-stage-a-evidence` and **not merged**.

## 2. Approved Inputs/Specifications

- `docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §9.2, §10 (Slice F),
  §10.1 (the worked fixture).
- The three approved Rule Cards, as amended: `CHAR-004` (2026-09-26,
  2026-09-27), `CHAR-005` (2026-09-25), `EXP-003`.
- Human authorization of 2026-09-27.
- `docs/completion-records/ISSUE-013` — the `CLUSTER-002` 189-case ledger,
  followed as precedent.

## 3. Files Created, Modified, or Deleted

**Created:** `tests/rules/test_cluster_003_integration.py`; this record.

**Modified:** `docs/rules/clusters/CLUSTER-003-equipped-dungeon-movement.md`
(new §14 Implementation Record); `docs/completion-records/INDEX.md`.

**Deleted:** none. Committed on `cluster-003-stage-a-evidence`, **not merged**.

## 4. Behavior Actually Verified

Every component below is the **real production object**. The RNG is a
`ScriptedRNG`, which exercises the same parsing and aggregation logic as
`SeededRNG`; nothing else is a stub, fake or double.

| Composition | Result |
|---|---|
| **Plan §10.1, gate closed** | A 10th-level Mystic's pack totals **482 cn** by CHAR-004's own derivations — dagger 10, backpack+rations 220, waterskin 30, belt-pouch 52 (`SR-6`), six torches 120, rope 50, clothes and shoes **worn → 0**. `482 > 400`, so `SR-9` shuts: **90' (30')**, *not* 210'. Allowance **90 feet, 9 squares**. `complete_ordinary_turn()` → `TurnCredit(1, ORDINARY)` |
| **Plan §10.1, gate open** | Drop the torches and rope (170 cn) → **312 cn** → `MV 210'`, encounter **70' exactly**, running 210'/round, allowance **210 feet, 21 squares** |
| **The gate is a threshold** | The whole chain flips on one coin weight: 400 cn → 210 feet; 401 cn → 90 feet |
| **Creation to exploration** | CHAR-001 scores → CHAR-002 `ELIGIBLE` → CHAR-003 one rolled level (7 hp) → CHAR-004 `180 gp`, a legal 66 gp selection, 632 cn carried → CHAR-005 `90' (30')` → EXP-003 90 feet / 9 squares → EXP-002 turn 1 |
| **E60 composed** | There is no path from an `Item` to a rate that does not pass through a `cn` integer |
| **M25 / M29 composed** | Suit Armor crosses the card boundary as `750` and is banded ordinarily to `90'`; adding a shield bands it to `60'`. No item-shaped path into movement exists for an override to travel along |
| **D29 composed** | A three-member party's slowest rate (60') reaches the allowance unchanged |
| **D30 composed** | A Mystic's `Fraction(130, 3)` encounter rate survives every boundary; `squares(3)` is still `130/3` |
| **D28 composed** | Three turns: the allowance does not advance time and the credit carries no distance. The caller holds both |
| **The combat boundary, both sides** | The same rate object serves exploration (120 feet/turn) and a combat round (40 feet at encounter speed), and normal speed is refused in the combat sequence |
| **Druid surcharge through the money path** | `4.5 gp` exists only as `Coin(450)`; it sums, compares against starting money and deducts like any other amount, with no float anywhere. The same object costs a non-druid `3 gp` |
| **Cleric prohibition, weapon and ammunition** | A cleric may buy neither a long bow nor arrows; encumbrance arithmetic is unaffected, because legality and weight are different questions |

**This module re-owns no approved case.** Each case's canonical owner is
recorded in §6.

## 5. Rules Provenance

**None.** This slice adds no production code and therefore no rule,
derivation, ruling or completion. It composes existing approved behaviour
and asserts that the components agree.

## 6. Exact 176-Case Reconciliation

**By card and canonical owning test module — verified programmatically, one
owner each:**

```text
CHAR-004   E1-E68    tests/rules/character_creation/test_equipment.py     68
CHAR-005   M1-M48    tests/.../test_encumbrance_and_movement.py           48
           M49-M59   NOT V1-WIRED -- plan §8                              11
           M60-M76   tests/.../test_encumbrance_and_movement.py           17
EXP-003    D1-D32    tests/rules/exploration/test_dungeon_movement.py     32
                                                                        ----
                                                                         176
```

**By verification kind — no case in two categories:**

```text
EXECUTABLE PYTEST CASE (unit)                                          138
STATIC / API-SHAPE CONFORMANCE                                          27
    CHAR-004  E59, E60
    CHAR-005  M28, M29, M62, M72, M73, M74, M75, M76
    EXP-003   D4, D5, D13, D14, D15, D18, D19, D20, D21, D23, D24,
              D25, D26, D27, D29, D31, D32
SPECIFIED BUT NOT V1-WIRED                                              11
    CHAR-005  M49-M59   -- card §7 condition modifiers, plan §8
                                                                       ----
                                                                        176
```

**Zero duplicates, zero omissions.** The absence of `M49`–`M59` from every
test module was verified programmatically: the only occurrences of `M49`
and `M59` anywhere in the suite are inside the range label `M49-M59` in the
Slice-D module docstring that records their deferral.

**The eighteen cases Slice F additionally demonstrates — `E14`, `E38`,
`E39`, `E48`, `E51`, `E52`, `E60`, `M21`, `M25`, `M26`, `M27`, `M29`,
`M34`, `M38`, `D6`, `D28`, `D29`, `D30` — are not re-owned here.** Their
canonical records are `ISSUE-016`, `ISSUE-017`, `ISSUE-018` and
`ISSUE-019`; the compositions above are supporting evidence and create no
extra Rule Card case.

### 6.1 Why eleven cases are deferred rather than implemented

`M49`–`M59` are card §7's condition movement effects — blindness,
stunning, prone, starvation — and they carry **`SR-10`**. Every causation
owner is `Unresearched`, so **no landed or approved card can produce any of
those conditions**:

| Condition | Causation owner | Status |
|---|---|---|
| Blindness | `COMBAT-*` / `EXP-006` | Unresearched |
| Stunning | `COMBAT-*` | Unresearched |
| Prone | `COMBAT-*` | Unresearched |
| Starvation | an `ADV-*` survival responsibility | Unresearched; **no Rule ID assigned** |

Plan §8 dispositions them `NOT V1-WIRED`, the established treatment for an
approved mechanic whose trigger is unreachable (precedent: `CHAR-003 W3`).
**`SR-10` remains approved and recorded on the card**, and no
simultaneous-condition composition, modifier ordering, or ordering against
the `SR-9` gate is invented. Guard tests assert that no `Condition` enum,
multiplier, pipeline or hook was built in anticipation.

## 7. Exact Verification Commands Executed

```text
uv run python scripts/verify.py
```

## 8. Verification Results

```text
Tests:     PASS   992 passed
Coverage:  PASS
Ruff:      PASS
mypy:      PASS
Overall:   PASS
```

## 9. Coverage Results

100% branch, per file, for all 18 files under `src/rules/`:

```text
src/rules/currency.py                                        46 stmts /  16 br -- 100%
src/rules/character_creation/equipment.py                   368 stmts / 154 br -- 100%
src/rules/character_creation/encumbrance_and_movement.py    132 stmts /  54 br -- 100%
src/rules/exploration/dungeon_movement.py                    33 stmts /  12 br -- 100%
```

Slice F adds no production code, so it changes no coverage figure.

## 10. Deviations

1. **The ledger carries a fourth category the plan did not name.** Plan
   §9.2 lists four verification kinds, none of which fits a case that is
   approved but deliberately unimplemented. `SPECIFIED BUT NOT V1-WIRED` is
   added rather than forcing `M49`–`M59` into "static conformance", which
   would misrepresent eleven cases as verified.
2. **`176`, not the plan's `168`.** The two human-approved `CHAR-004`
   amendments added `E61`–`E68` after the plan was written. The plan's §9.2
   was updated in place; the Pre-Code Gate's `168` is historically correct
   for 2026-09-24 and was deliberately left unchanged.

## 11. Known Limitations/Unresolved Issues

- **The cluster's chain has no orchestrator, and Slice F did not add one.**
  These tests compose public APIs in the approved order; no engine,
  creator, builder, session or state object exists, and plan §4.1 forbids
  one. Who calls the chain in a running simulation is unowned.
- **Two `CHAR-004` §7 boundaries remain undecided**, recorded in
  `ISSUE-017` §11: a thief with a large net, and a dual-role item used as a
  weapon. No approved case covers either.
- **`turn_movement_allowance` cannot verify its argument is a *party*
  rate** (`ISSUE-019` §11).
- Carried forward unchanged: `CHAR-005` §7 `NOT V1-WIRED`; Chapter 10
  `NOT V1-WIRED`; mounts, vehicles, ships and siege out of V1; spatial
  quantisation unowned; the rough/broken-terrain modifier unowned by
  express approval.

## 12. Architectural Consequences

The cluster's dependency graph is acyclic, one-directional, and has no
back-edges:

```text
rng/          currency.py [shared]        character_class.py [shared]
  |               |      |                         |
  v               v      |                         v
equipment.py [CHAR-004] -+------------------------>|
  |  Enc (cn) only                                 |
  v                                                v
encumbrance_and_movement.py [CHAR-005] <-----------+
  |  MovementRate
  v
dungeon_movement.py [EXP-003]
  |  DungeonMovementAllowance
  v
dungeon_turn_time_accounting.py [EXP-002, LANDED -- consumed, not imported]
```

`equipment` does not import `encumbrance_and_movement`; `dungeon_movement`
does not import `equipment` or anything from `EXP-002`. Each is asserted
over the parsed import graph rather than over prose.

**Nothing the cluster's §4.3 non-goals forbid was built.** No generic
equipment-movement override, no proportional Suit Armor or Mystic scaling,
no Mystic encumbrance immunity or separate Mystic table, no separate Mystic
running formula, no rounding of a Mystic encounter rate, no mapping time
cost or roll or failure state, no terrain subsystem, no second movement-rate
authority, and no spatial quantisation. Each has a guard test asserting its
absence.

`fractions.Fraction` entered the codebase in Slice D and is confined to
movement values. No `float` appears in any production module of this
cluster — asserted over parsed modules, not their text.
