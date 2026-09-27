# ISSUE-018: CHAR-005 Encumbrance & Movement Rate (CLUSTER-003 Slice D)

## 1. Issue/Task Identifier and Objective

ISSUE-018 (completion-record ledger). Implement **Slice D** of
`docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §10: the **single**
authoritative numerical movement system — normal, encounter and running
rates, the six encumbrance bands, the Mystic level-dependent `MV` with its
`SR-9` gate, the §5 combat-sequence boundary, group movement, exhaustion,
and units.

**`EXP-003` is not implemented and no dungeon movement code exists.**
`CHAR-009`, `CHAR-010` and `TREAS-004` are untouched.

**Status: awaiting human review.** Slice E is not started.

## 2. Approved Inputs/Specifications

- `docs/rules/character_creation/encumbrance_and_movement_rate.md`
  (`CHAR-005`, `APPROVED` 2026-09-24, **amended 2026-09-25**), carrying
  **`SR-8`**, **`SR-9`** and **`SR-10`**, and two determinations that are
  expressly **not** rulings (Q4 running speed; Q6 exact fractional
  encounter movement, incl. §6.1 Mystic running).
- `docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §5.2, §6.3, §6.5, §8,
  §9, §10 (Slice D).
- Human authorization of 2026-09-27, limited to the approved `CHAR-005`
  movement scope.
- RC Ch. 6 pp. 87–89, Ch. 8 p. 103, Ch. 2 p. 31, Ch. 4 p. 68.

## 3. Files Created, Modified, or Deleted

**Created:**

- `src/rules/character_creation/encumbrance_and_movement.py`
- `tests/rules/character_creation/test_encumbrance_and_movement.py`
- This completion record.

**Modified:**

- `src/rules/character_creation/errors.py` — `MovementLevelError`,
  `MovementNotPermittedError`.
- `docs/completion-records/INDEX.md` — index row.

**Deleted:** none. Committed on `cluster-003-stage-a-evidence`, **not merged**.

## 4. Behavior Actually Implemented

### `movement_rate(cls, level, total_encumbrance_cn) -> MovementRate`

The single entry point. Validates, chooses a **normal speed** by one of two
paths, and derives everything else by one rule:

```text
1. validate level        §1.1 — int, not bool, 1..maximum
2. validate encumbrance  int, not bool, >= 0
3. Mystic AND enc <= 400  ->  MYSTIC_MV[level]        SR-9
4. otherwise              ->  the standard band       §3
5. normal -> encounter, running                       §4, §6.1
```

### `MovementRate`

**Stores only the normal speed**; `encounter` (`normal / 3`, feet per round)
and `running` (the normal number, feet per round) are derived. Case M17 —
*"encounter × 3 equals running, at every band"* — therefore holds **by
construction**, and no caller can build a rate whose parts contradict each
other. Ordered by normal speed, which supplies §8's slowest-member
comparison.

### Exact rationals

Every rate is a `fractions.Fraction`. A Mystic at `MV 130'` has an encounter
rate of exactly `130/3`, and nothing rounds it in any direction (M42, M46,
M47). **No `float` is used, produced or accepted** — asserted over the
parsed module, not its text.

### The rest of the surface

`party_movement_rate` (slowest member, §8); `combat_movement` and
`may_attack_in_the_same_round` (§5's scale boundary); `run_for`,
`is_rested`, `ExhaustionPenalty`, `MAXIMUM_RUNNING_ROUNDS`,
`REQUIRED_REST_TURNS` (§9); `Setting` (§10); `SUIT_ARMOR_ENCUMBRANCE_CN`
re-exported from CHAR-004's catalog.

## 5. Rules Provenance

| Element | Classification |
|---|---|
| §3 table; §4 rate definitions; §5 scale boundary; §6 `MV` values; §8 group rule; §9 exhaustion; §10 units | **Rules Cyclopedia Explicit** |
| Q4 — Ch. 8's "3 × normal movement" as 3 × encounter | **RC Explicit interpretation/correction**, reinforced by necessary consequence. **NOT a ruling** |
| `encounter = MV ÷ 3`, exact fractions retained | **RC Explicit** (the ratio) + **Necessary Mathematical Consequence** (exactness). **NOT a ruling** |
| §6.1 Mystic running = `MV` per round | **Necessary Mathematical/Mechanical Consequence**, expressly approved 2026-09-24. **NOT a ruling** |
| Suit Armor has no special rate; `750 cn` only | **Simulator Ruling `SR-8`** |
| Mystic `MV` gated on the unencumbered band | **Simulator Ruling `SR-9`** |
| Suit Armor alone → `90' (30')` | **Necessary Mechanical Consequence** of `SR-8` + the table |

**No new Simulator Ruling. `SR-8`, `SR-9`, `SR-10` unchanged and
unrenumbered. No Compatible Completion. No Variant.**

## 6. Tests Added or Modified

168 tests: approved cases **M1–M48** and **M60–M76**, with case IDs in
docstrings and `parametrize` ids.

**M49–M59 appear nowhere, deliberately** — card §7's condition modifiers are
`NOT V1-WIRED` (plan §8). Guard tests assert no condition parameter, enum,
multiplier or pipeline was built in anticipation, and that no starvation
fraction appears in the module.

Guard cases M28/M29/M30 (Suit Armor), M37/M38 (no Mystic scaling, no
immunity), M46/M47 (no rounding, no lossy float), M72–M76 (no racial-armour
number, no monster system, no quantisation, no possessions limit, no
terrain) are all present and assert **absence**.

## 7. Exact Verification Commands Executed

```text
uv run python scripts/verify.py
```

## 8. Verification Results

```text
Tests:     PASS   910 passed
Coverage:  PASS
Ruff:      PASS
mypy:      PASS
Overall:   PASS
```

## 9. Coverage Results

```text
src/rules/character_creation/encumbrance_and_movement.py   129 stmts / 54 branches -- 100%, 0 missed
```

All 17 files under `src/rules/` at 100% branch per file.

## 10. Deviations

1. **`MovementRate` stores one field, not three.** The plan's §6.3 sketch
   listed `normal`, `encounter` and `running` as fields. Storing only
   `normal` and deriving the rest makes an inconsistent rate
   *unrepresentable* and turns M17 into a structural guarantee rather than a
   test. The public shape is unchanged — all three are still read as
   attributes.
2. **`MovementNotPermittedError` added**, beyond the plan's §6.5 list, which
   named only `MovementLevelError` for this card. The plan's §6.3 sketch
   carried no §5 scale-boundary API at all, and M21, M24 and M64 all require
   a refusal. Recorded in the error's own docstring as a deliberate
   departure.
3. **A §5 API exists at all** — `MovementMode`, `combat_movement`,
   `may_attack_in_the_same_round` — which §6.3 did not sketch. M21–M24 are
   approved cases and §5 is inside Slice D's clause list.
4. **`MovementRate` refuses a bare `int`.** Rates stay exact rationals, and
   accepting an `int` would invite a `float` through the same door.
5. **`ExhaustionPenalty` records and applies nothing**, per plan §7's
   ownership audit. There is deliberately no `damage_after_exhaustion()`:
   M68's *"minimum 1"* is the recorded `minimum_damage` floor, and applying
   it to a damage roll is COMBAT-003's.

### 10.1 One reading of §1.1, stated plainly

§1.1 says level must be *"<= the applicable per-class maximum"*. **Only the
Mystic's 16 is enforced.** For every other class, level is validated as an
`int` ≥ 1 with no upper bound.

The reason is the one §6.6 itself raises: the per-class maxima remain
**`ADV-002`'s** property, projected privately by `hit_points_and_hit_dice.py`
to bound *hit-point* accrual. This card indexes exactly one level-dependent
table — the Mystic's — so projecting all nine maxima here would create a
second projection of data this card does not consume, for no behavioural
difference. `movement_rate(FIGHTER, 36, 0)` and `movement_rate(FIGHTER, 99,
0)` both return `120'`, because level does not reach a non-Mystic's rate.

**It is a reading, and it is offered for correction.** If you want the full
per-class bound enforced here, it is a table and three lines.

## 11. Known Limitations/Unresolved Issues

- **Card §7 condition modifiers — `NOT V1-WIRED`** (plan §8). `SR-10`
  remains approved and recorded on the card; nothing in §7 is implemented,
  and no composition, ordering or gate-interaction question is invented.
- **Open Question 2 (prone → standing, stated twice)** is untouched: no
  mechanic here turns on the difference, exactly as the card records.
- **Spatial quantisation** is unowned and not provided (M74).
- **M73's monster/mount two-band system** is guarded by absence rather than
  by a runtime rejection — nothing in a `cn` integer identifies its bearer
  as a monster, so there is no input to detect.

## 12. Architectural Consequences

`fractions.Fraction` enters the codebase for the first time, as plan §5.2
approved: standard library, no dependency, exact arithmetic **and** exact
comparison, the latter mattering for §8's slowest-member rule.

The dependency graph stays acyclic and one-directional. This module imports
`character_class`, `errors`, and — for one integer — `equipment`, aliased
privately so `SUIT_ARMOR_ENCUMBRANCE_CN` is the only thing that crosses. It
imports nothing from `rules.exploration`, which a test asserts over the
parsed import graph.

`CHAR-004` and `CHAR-005` are both complete. `src/` still contains no
dungeon movement code.
