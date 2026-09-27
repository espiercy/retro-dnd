# ISSUE-019: EXP-003 Dungeon Movement and EXP-002 Integration (CLUSTER-003 Slice E)

## 1. Issue/Task Identifier and Objective

ISSUE-019 (completion-record ledger). Implement **Slice E** of
`docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §10: spend the
authoritative movement rate against the landed dungeon turn.

All three `CLUSTER-003` Rule Cards are now implemented.

**Status: accepted by the human project owner, 2026-09-27.** Slice F was
authorized on that acceptance.

## 2. Approved Inputs/Specifications

- `docs/rules/exploration/dungeon_movement.md` (`EXP-003`, `APPROVED`,
  human-approved 2026-09-24) — §1–§8, **carrying no Simulator Ruling**.
- `docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §5.6, §6.4, §9, §10
  (Slice E).
- Human authorization of 2026-09-27.
- Landed `EXP-002` `DungeonTimeAccounting` and `TurnCredit`; landed
  `CHAR-005` `MovementRate` (Slice D).
- RC Ch. 7 p. 91, Ch. 6 pp. 87–88, Ch. 8 p. 103, Ch. 13 p. 148, Ch. 17
  p. 260.

## 3. Files Created, Modified, or Deleted

**Created:**

- `src/rules/exploration/dungeon_movement.py`
- `tests/rules/exploration/test_dungeon_movement.py`
- This completion record.

**Modified:** `docs/completion-records/INDEX.md` (index row).

**Deleted:** none. Committed on `cluster-003-stage-a-evidence`, **not merged**.

## 4. Behavior Actually Implemented

### `turn_movement_allowance(party_rate) -> DungeonMovementAllowance`

Reads `party_rate.normal` and nothing else. RC Ch. 7 p. 91: *"customarily
characters will travel at their normal speed during game turns."*

**It consumes a rate and computes none.** The signature takes a whole
`MovementRate` and receives no encumbrance, class or level, so it is
structurally incapable of re-deriving a rate `CHAR-005` owns (D29), and
there is no parameter through which encounter or running speed could be
offered (D4, D5).

### `DungeonMovementAllowance`

`feet: Fraction`, plus `is_immobile` and `squares(scale_feet=10)`. Exact and
never rounded: `15'` is `1.5` squares and stays `1.5` (D9); a DM-configured
scale changes the square count and never the rate in feet (D10, D11).

### `GAME_TURN_CHECKLIST`

RC's four steps recorded as **inert data**, so the delegation is legible and
testable. **No function runs a step** — there is no `explore()`, no
`run_turn()`, no engine and no state (D21).

## 5. Rules Provenance

| Element | Classification |
|---|---|
| §2 rate used; §3 default map scale; §4 assumed actions; §5 checklist; §6 scale boundary; §7 terrain non-application; §8 exit condition | **Rules Cyclopedia Explicit** |
| §3 squares-per-turn arithmetic | **Necessary Mathematical Consequence** |
| §4 "must not double-count mapping" | **Necessary Mechanical Consequence** |

**This card carries no Simulator Ruling, no Compatible Completion and no
Human-Approved Variant, and this implementation introduces none.**

## 6. Tests Added or Modified

57 tests covering approved cases **D1–D32**, every one referenced by ID:

```text
runtime / executable   D1-D3, D6-D12, D16-D17, D22, D28, D30
static / API-shape     D4, D5, D13-D15, D18-D21, D23-D27, D29, D31, D32
```

The static cases assert the **absence** of behaviour — a mapping roll, a
terrain modifier, an orchestration loop, a quantisation step — and are the
executable form of boundaries the card draws. Several are asserted over the
**parsed module** rather than its text, so an identifier that merely
contains a forbidden word cannot mask a real violation and a later edit that
starts reading `.encounter` fails loudly.

**D28 drives the real `DungeonTimeAccounting`**, never a stub, following the
`CLUSTER-001` precedent, and asserts this module imports nothing from it.
**D29 drives the real `party_movement_rate`**.

## 7. Exact Verification Commands Executed

```text
uv run python scripts/verify.py
```

## 8. Verification Results

```text
Tests:     PASS   978 passed
Coverage:  PASS
Ruff:      PASS
mypy:      PASS
Overall:   PASS
```

Green on the first run; no defect was found and corrected during
implementation.

## 9. Coverage Results

```text
src/rules/exploration/dungeon_movement.py   33 stmts / 12 branches -- 100%, 0 missed
```

All 18 files under `src/rules/` at 100% branch per file.

## 10. Deviations

1. **`GAME_TURN_CHECKLIST` added**, not in the plan's §6.4 sketch. Six
   approved cases (D21–D26) turn on the four steps and on which of them
   belong elsewhere. It is four strings, explicitly inert, and a guard test
   asserts no orchestration symbol exists beside it. The alternative —
   leaving the checklist in prose only — would have left D21 with no
   executable form.
2. **`DungeonMovementAllowance.is_immobile` added** for D3, mirroring
   `MovementRate.is_immobile` so the two read alike.
3. **`DungeonMovementAllowance` refuses a bare `int`**, for the same reason
   `MovementRate` does: the allowance stays exact, and an `int` would invite
   a `float` through the same door.

No deviation changes a rule, and none adds a mechanic the card does not
state.

## 11. Known Limitations/Unresolved Issues

- **Spatial quantisation** of a fractional allowance is unspecified and
  unowned (card §C, Open Questions 3). `squares()` divides and does not
  round; snapping is a separate execution concern.
- **The rough/broken-terrain modifier** presupposed by RC's Mystic
  Acrobatics wording **remains unowned by express approval**. No terrain
  mechanic is created here (D18, D19).
- **`turn_movement_allowance` cannot verify that its argument is a *party*
  rate** rather than one character's, and does not pretend to: a single
  rate is a well-formed argument, and whether a group intended to stay
  together is a question `CHAR-005` §8 answers before this is called. This
  is documented on the function rather than guarded, because there is
  nothing in a `MovementRate` to inspect.
- **The exploration loop itself is unowned.** This card returns an
  allowance; who spends it, and when the loop is left, is orchestration no
  approved card assigns (plan §4.1).

## 12. Architectural Consequences

The dependency chain now executes end to end, acyclic and one-directional:

```text
equipment.py [CHAR-004] --Enc (cn)--> encumbrance_and_movement.py [CHAR-005]
                                           |  MovementRate
                                           v
                                    dungeon_movement.py [EXP-003]
                                           |  DungeonMovementAllowance
                                           v
                            dungeon_turn_time_accounting.py [EXP-002]
                                    LANDED -- consumed, not imported
```

`dungeon_movement.py` imports exactly one project module,
`encumbrance_and_movement`, for one type. It imports nothing from
`dungeon_turn_time_accounting`, `turn_credit` or `rng` — asserted over the
parsed import graph, which also means **no mapping die roll could be made
here even if someone tried to add one**.

`EXP-002`'s landed code was not touched, extended or re-implemented.
