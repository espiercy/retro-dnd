# ISSUE-010: CHAR-003 Hit Points & Hit Dice (CLUSTER-002 Slice C)

## 1. Issue/Task Identifier and Objective

ISSUE-010 (completion-record ledger). Implement **Slice C** of
`docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` (`APPROVED`,
human-approved 2026-09-12, revision 3): the complete `CHAR-003` hit-point
contract as one authoritative, level-aware operation, plus the two CHAR-003
error types.

Slices A and B were human-reviewed and **ACCEPTED** before this slice began.
Neither was redesigned.

## 2. Approved Inputs/Specifications

- `docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` §5.2, §7.6, §7.6.1,
  §8, §9.1, §9.2, §10.3, §12, §14 (Slice C) — the approved implementation
  contract.
- `docs/rules/character_creation/hit_points_and_hit_dice.md` (`CHAR-003`,
  Status: `APPROVED`, human-approved 2026-09-04) — the governing Rule Card,
  §1–§5 and §8, and its deterministic test table H1–H42, read directly
  rather than reconstructed.
- `docs/rules/character_creation/ability_score_effects.md` (`CHAR-007`,
  `APPROVED`) — the authoritative Constitution adjustment, consumed, never
  reimplemented.
- `docs/technical/RNG_CONTRACT.md` and `src/rng` — the `RNG` Protocol,
  consumed unchanged.
- `ARCHITECTURE.md` §15.2, "Status update (2026-09-12)".

## 3. Files Created, Modified, or Deleted

**Created:**

- `src/rules/character_creation/hit_points_and_hit_dice.py`
- `tests/rules/character_creation/test_hit_points_and_hit_dice.py`
- This completion record.

**Modified:**

- `src/rules/character_creation/errors.py` — two additions only (§10).
- `docs/completion-records/INDEX.md` (index row).

**Deleted:** none. **No other Slice-A or Slice-B file was modified.**

Committed on `cluster-002-implementation`. **Not merged.**

## 4. Behavior Actually Implemented

### The authoritative operation

```python
hit_point_gain(rng: RNG, cls: CharacterClass, level: int, constitution: int) -> int
```

`level` is the level being gained or entered, and the operation decides
which rule governs it — nothing is pushed onto a caller:

```text
level < 1, or > class maximum        -> HitPointLevelError
Druid at a rolled level              -> HitDieNotApplicableError
1 <= level <= Name level             -> ROLLED
Name level < level <= class maximum  -> FIXED
```

**Rolled branch:** `max(1, one_hit_die.total + adjustment(constitution))`.
The Constitution adjustment is obtained by calling **`CHAR-007`'s
`adjustment()` on every application** — never cached, never reimplemented —
so a changed Constitution governs the next roll (card §3). Exactly one die
is drawn and a low result is never rerolled.

**Fixed branch:** the approved fixed gain, with **zero RNG draws and no
call to `CHAR-007` at all**. Constitution is not merely ignored
arithmetically; the branch never consults it, which is observable: a
Constitution of 19 or 1 — values `CHAR-007` rejects — produces the normal
fixed gain rather than an error.

**Rejection branches:** zero RNG draws; raised before any draw.

**One invocation is one level.** There is deliberately no
`total_hit_points`, `gain_levels` or `advance_to_level`, and no batch
operation of any kind.

### Class table implemented (card §1, §4)

| Class | Hit Die | Name | Max | Fixed gain |
|---|---|---|---|---|
| Cleric | d6 | 9 | 36 | +1 (10–36) |
| Fighter | d8 | 9 | 36 | +2 (10–36) |
| Magic-User | d4 | 9 | 36 | +1 (10–36) |
| Thief | d4 | 9 | 36 | +2 (10–36) |
| Dwarf | d8 | 9 | 12 | +3 (10–12) |
| Elf | d6 | 9 | **10** | **+2 at 10 — SR-1** |
| Halfling | d6 | **8** | **8** | *(none — no post-Name band)* |
| Mystic | d6 | 9 | 16 | +2 (10–16) |
| Druid | *(does not apply)* | 9 | 36 | +1 (10–36) |

### Private advancement-boundary projection

`_HIT_DIE`, `_NAME_LEVEL`, `_MAXIMUM_LEVEL` and `_FIXED_GAIN` are
module-private `MappingProxyType` tables. The module docstring states, in
its own words:

> **ADV-002 remains the future authoritative owner of general advancement
> limits. Future ADV-002 work must replace or reconcile this projection.**

`__all__` is exactly `["hit_point_gain"]`. **No `maximum_level()`,
`name_level()`, `class_progression()` or advancement table is exported**,
and no `ClassProgression`, `AdvancementRules` or `LevelTable` type exists —
asserted by test.

## 5. Rules Provenance

Per the card's Provenance Classification:

- **Rules Cyclopedia Explicit** — the Hit Die table, the per-roll
  1-hit-point floor, Constitution applying per rolled die and not to fixed
  gains, and the fixed-gain values for every class but the Elf.
- **Simulator Ruling SR-1** — the **Elf's `+2` at 10th level**. It is
  recorded in code as a ruling, not as an RC-explicit value: the
  `_FIXED_GAIN` Elf entry carries a comment stating that RC prints **both**
  `+1` (p. 25 stat block, p. 130 Step 6) and `+2` (p. 25 Class Details,
  p. 129), that the human project owner adjudicated, and that reversal
  changes this entry **and** the fourteen other normative locations card
  §4.1 enumerates. **The historical conflict is not reopened**, and nothing
  in the code asserts the sources agree.
- **Human adjudications of 2026-08-29** — the Elf maximum 10 and Druid
  maximum 36, consumed as given.

No value was substituted from another edition, and no case was rewritten to
fit the implementation.

## 6. Tests Added or Modified

**52 new tests.**

**Approved contract cases — 42**, the complete `CHAR-003` contract, owned
entirely by this slice:

```text
runtime / executable   40   H1-H35, H37, H39-H42
static / API-shape      1   H36
calling-contract        1   H38   -- no pytest function
                       ---
                        42
```

41 pytest functions carry `H1`–`H37` and `H39`–`H42`; H38 has none, by
design. Verified by extraction. Every name is qualified `char003` because
`CHAR-001` also has H-numbered cases, in a different module.

**Implementation/coverage tests — 11, counted separately**, under an
explicit banner: level below 1; Druid rejected at every rolled level; Druid
past maximum as a *level* rejection rather than a hit-die one; `CHAR-007`
domain rejection propagating unchanged; the fixed branch never consulting
Constitution; every fixed-gain level consuming zero dice; the one-operation
public surface; no advancement API; error hierarchy; and two AST-based
import-boundary assertions.

### H36 — static / API-shape evidence

`inspect.signature(hit_point_gain).parameters` is asserted to be exactly
`["rng", "cls", "level", "constitution"]`, and no parameter name contains
`adjust`, `modifier` or `bonus`. **A caller cannot supply an arbitrary
Constitution adjustment, because no parameter exists for one.** The test
additionally asserts, from the module's own AST, that
`ability_score_effects` **is** imported — so the dependency is real, not
merely un-bypassable.

### H38 — calling-contract evidence

**Certified for this slice:**

- **No reroll helper exists.** `__all__` is exactly `["hit_point_gain"]`,
  and the only other callable in the module is the private `_rolled_gain`.
- **No automatic retry exists.** `_rolled_gain` draws once
  (`rng.roll_die(...)`) and returns `max(1, …)`; there is no loop, no
  conditional redraw and no exception-driven retry anywhere in the module.
- **No Slice-C production code invokes the HP-gain operation repeatedly to
  replace an established roll.** `hit_point_gain` calls nothing but
  `_rolled_gain`, `adjustment()` and the RNG; it never calls itself, and no
  other production module in this slice calls it at all.
- **Repeated invocation for an already-resolved level is outside the pure
  operation's observable state and is prohibited by the calling contract.**
  The module docstring states the roll-once contract explicitly. No
  character state, level history, `already_rolled` flag or advancement
  state was added to detect it, per the approved plan §12.3.1.

**Executable support:** H12 (Fighter 1→12, exactly 9 d8), H13 (Halfling
1→8, exactly 8 d6), H15 (Elf 1→10, exactly 9 d6 then one fixed gain) and
H26 (Elf 1→9, exactly 9 d6) each use an exact-length `ScriptedRNG` queue
and then assert the queue is exhausted — an extra draw raises
`RollSequenceExhaustedError`, a missing one leaves a value and fails the
exhaustion assertion. One rolled level consumes exactly one die.

**No ceremonial pytest function was written for H38.**

## 7. Exact Verification Commands Executed

- `uv run python scripts/verify.py`

## 8. Verification Results

- **Tests:** 322 passed, 0 failed (270 after Slice B + 52 new).
- **Coverage:** PASS — differentiated gate: `src/rules/` 12 files, 100%
  required per file, met; core aggregate 100.00% (≥95% required).
- **Ruff:** clean (33 source files).
- **mypy strict:** clean.
- **Overall: PASS.**

**One real defect was caught by mypy on the first run and fixed, not worked
around.** `RNG.roll_die()` returns a `RollResult`, not an `int`; the first
draft wrote `rng.roll_die(...) + adjustment(...)`. mypy reported
`Unsupported operand types for + ("RollResult" and "int")`, and 28 tests
failed on the same cause. Corrected to read `roll.total`. This is exactly
the class of error the strict type gate exists to catch, and it was caught
before any commit.

## 9. Coverage Results

| File | Statements | Branches | Missing | Partial |
|---|---|---|---|---|
| **`hit_points_and_hit_dice.py`** | **27/27** | **6/6** | 0 | 0 |
| `errors.py` | 5/5 | — | 0 | 0 |

Its six branches are the two arcs each of the level-range check, the
rolled-versus-fixed check, and the Druid hit-die check.

Slice A and B files remain at 100%/100%: `ability.py` 44/44 + 8/8,
`ability_score_effects.py` 66/66 + 6/6, `race_and_class_eligibility.py`
32/32 + 4/4, `character_class.py` 12/12. **No branch was excluded and no
coverage configuration was weakened.**

## 10. Deviations

**None from the approved plan or the card.**

`errors.py` was extended with exactly two types — `HitPointLevelError` and
`HitDieNotApplicableError` — and nothing else. The five subclasses the plan
identifies for Slices D–E (`IllegalTradeError`,
`ClassMinimumViolationError`, `PrimeRequisiteCeilingError`,
`IllegalSwitchError`, `PointAllocationError`) were **not pre-stubbed**, and
the module docstring was updated to say so. The existing hierarchy was not
redesigned.

**One conscious implementation choice, recorded rather than left implicit:**
`hit_point_gain` does not add an `int`/`bool` type guard on `level` or
`constitution`. No approved case requires one, mypy strict prevents the
case in typed callers, and a `bool` Constitution resolves to 0 or 1 — both
outside `CHAR-007`'s accepted domain — and is therefore rejected naturally
by the existing path. Adding an unrequested third error surface would have
been scope creep.

## 11. Known Limitations/Unresolved Issues

None known, and none deferred silently.

- **The Druid rejection at rolled levels 2–9** is a necessary consequence of
  card §1's unqualified "does not apply", flagged as such in the approved
  plan §7.6.1 and covered by an implementation test rather than presented
  as an approved case. H39 names level 1.
- **Chapter 10 Step 6** (card §7, the above-1st-level construction, and its
  open item W3) is **not V1-wired and not implemented**, as the card states.
- **`CHAR-003` W2** (whether the 1-hp floor governs fixed gains) remains
  moot: every fixed gain in §4 is positive, so the floor is unreachable on
  that branch in code exactly as on paper.
- **P1** (Druid transition) remains `DEFER FOR HUMAN GOVERNANCE`. No Rule
  ID assigned; no part of the transition is implemented or discoverable.

## 12. Architectural Consequences

**`CHAR-003` → `CHAR-007` is a real production dependency**, not a
convention: the module imports `adjustment` and calls it on every rolled
application. The Constitution adjustment table is **not duplicated**.

**The Constitution score is a scalar, deliberately.** `AbilityScores` is the
creation-score set (3–18); hit points accrue across later levels, so this
card consumes the **current** Constitution as an `int` and lets `CHAR-007`
own the authoritative accepted domain (2–18). A score outside it raises
`CHAR-007`'s own `AbilityScoreDomainError`, which is allowed to **propagate
unchanged** — it is not caught, wrapped or reinterpreted.

**Import boundaries, asserted from the module's own AST:** it imports `rng`
(the `RNG` Protocol only — `SeededRNG` and `ScriptedRNG` are asserted
absent), `ability_score_effects`, `character_class` and `errors`. It imports
**no** `AbilityScores`, **no** `race_and_class_eligibility`, **no**
`ability_score_generation`, **no** `rules.exploration` and **no** `random`.
No additional dependency proved necessary.

`ScriptedRNG` appears only in tests.

No boundary or invariant in `ARCHITECTURE.md` changed. `CLUSTER-002`
implementation remains **IN PROGRESS**; this record completes Slice C only
and marks no later slice, and no cluster, as done.
