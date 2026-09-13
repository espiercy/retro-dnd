# ISSUE-009: CHAR-002 Race & Class Eligibility (CLUSTER-002 Slice B)

## 1. Issue/Task Identifier and Objective

ISSUE-009 (completion-record ledger). Implement **Slice B** of
`docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` (`APPROVED`,
human-approved 2026-09-12, revision 3): the complete `CHAR-002` creation-time
eligibility contract, and — as the single `CLUSTER-002` owner of both — the
authoritative **creation minimum** and **prime requisite** tables that
`CHAR-001` will consume in Slice D.

Slice A was human-reviewed and **ACCEPTED** before this slice began. No
Slice-A public contract was changed.

## 2. Approved Inputs/Specifications

- `docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` §7.5, §7.9, §9.2,
  §10.2, §10.4, §12, §14 (Slice B) — the approved implementation contract.
- `docs/rules/character_creation/race_and_class_eligibility.md` (`CHAR-002`,
  Status: `APPROVED`, human-approved 2026-09-04) — the governing Rule Card,
  §1–§5 and its Scope Boundaries §A–§C.
- `ARCHITECTURE.md` §15.2, "Status update (2026-09-12)" — `CLUSTER-002`
  implementation `AUTHORIZED`, scoped to the four-card boundary and the
  approved plan.
- Slice A (`ISSUE-008`) — `Ability`, `AbilityScores`, `CharacterClass`,
  reused unchanged.

## 3. Files Created, Modified, or Deleted

**Created:**

- `src/rules/character_creation/race_and_class_eligibility.py`
- `tests/rules/character_creation/test_race_and_class_eligibility.py`
- This completion record.

**Modified:** `docs/completion-records/INDEX.md` (index row).

**Deleted:** none. **No Slice-A file was modified.**

Committed on `cluster-002-implementation`. **Not merged** — under the
approved plan §15 the branch stays unmerged until Slice F.

## 4. Behavior Actually Implemented

### Creation eligibility (card §2)

```text
Cleric, Fighter, Magic-User, Thief   always eligible, whatever the scores
Dwarf                                Constitution >= 9
Elf                                  Intelligence >= 9
Halfling                             Dexterity >= 9  AND  Constitution >= 9
Mystic                               Wisdom >= 13    AND  Dexterity >= 13
Druid                                NOT_ELIGIBLE_AT_CREATION, unconditionally
```

No additional minimum exists, and no prime requisite is tested against any
threshold.

### Public API

- `eligibility(scores, cls) -> Eligibility`
- `eligible_classes(scores) -> frozenset[CharacterClass]`
- `prime_requisites(cls) -> frozenset[Ability]`
- `creation_minimums(cls) -> Mapping[Ability, int]`

`Eligibility` is a closed three-value enum: `ELIGIBLE`,
`NOT_ELIGIBLE_ABILITY_REQUIREMENT`, `NOT_ELIGIBLE_AT_CREATION`.

**Ineligibility is a normal rules result, never an exception.** This module
imports no error type and raises nothing — a fact visible in its import
list.

### The Druid's distinct reason

`eligibility(any_scores, DRUID)` returns **`NOT_ELIGIBLE_AT_CREATION`**, not
`NOT_ELIGIBLE_ABILITY_REQUIREMENT`. The distinction is mechanically
significant and approved: the demihuman and Mystic gates are ability
thresholds a different score array could satisfy, while the Druid's
requirement — Neutral alignment and 9th level as a cleric — is not an
ability threshold at all and no array can ever satisfy it.

### Single source of truth

`eligible_classes` is **derived from `eligibility`**, so the thresholds
exist in exactly one implementation path. `_CREATION_MINIMUMS` and
`_PRIME_REQUISITES` are each defined once, at module level, and are the only
place either table appears.

**Immutability.** `prime_requisites` returns a `frozenset`;
`creation_minimums` returns a `types.MappingProxyType`, and the outer table
is proxied too. A caller cannot mutate this module's authoritative tables —
asserted by test.

**The Druid's empty minimum table is documented, not left to inference.**
Emptiness there means "its requirement is not an ability threshold", not
"no requirement"; `eligibility` decides the Druid *before* consulting any
minimum, so an empty table can never be read as eligible.

## 5. Rules Provenance

Per the card's Provenance Classification:

- **Rules Cyclopedia Explicit** — the §2 table, the human-class exemption
  (RC states it as a universal), Druid non-reachability, and §3's statement
  that prime requisites are not gates.
- **Necessary Mathematical-Mechanical Consequence** — "the eligible set is
  never empty", which follows from the human-class exemption.
- **`CHAR-002` owns no Simulator Ruling.** `SR-3`'s consequences (the
  eligibility-score input, and the switch's bounded reach) are consumed
  here and owned by `CHAR-001`; nothing was re-ratified.

No mechanic was inferred from another edition, from downstream rules, or
from memory. The prime-requisite table was transcribed from the card's §2
table in full, including the cases that matter most: the **Dwarf's** prime
requisite is Strength while its gate is Constitution 9, and the **Mystic's**
are Strength and Dexterity while its gates are Wisdom 13 and Dexterity 13 —
so Wisdom gates the Mystic without being one of its prime requisites.

## 6. Tests Added or Modified

**34 new tests, in two clearly separated categories.**

**Approved contract cases — 27.**
`tests/rules/character_creation/test_race_and_class_eligibility.py` is the
canonical owner of **E1–E22 and E24–E28**, each appearing exactly once,
under its own case ID, in the card's order. Verified by extraction: the
implemented IDs are exactly `e1…e22, e24…e28`.

**E23, E29 and E30 are deliberately absent**, and the module docstring says
so. Their canonical owners remain the Slice F cross-card work.

Threshold boundaries are exercised on both sides, as required: Dwarf Con
8/9 (E4, E5), Elf Int 8/9 (E6, E7), Halfling Dex 8/9 and Con 8/9 including
both together (E8, E9, E10), Mystic Wis 12/13 and Dex 12/13 including both
together (E11, E12, E13). Human classes stay eligible at prime-requisite 3
(E14, E15, E16). `eligible_classes` is never empty and never contains the
Druid (E3, E19).

**Implementation/coverage tests — 7, counted separately** and under an
explicit banner: full prime-requisite table, full creation-minimum table,
caller-immutability of the minimums, the closed three-value result, and the
two dependency-boundary assertions (no `CHAR-007`, no RNG). **None is an
approved Rule Card case**, and the file's docstring says so.

### How the cross-card cases were kept inside this slice

E20, E21, E22 and E25–E28 reference `CHAR-001`'s trade and switch. **No
`CHAR-001` import was added.** Each is tested as the eligibility-side fact
it actually is:

- **E20/E27** — Constitution is the Dwarf's only gate and is *not* one of
  its prime requisites, so it can never be a trade target or switch
  destination; Con 8 stays ineligible with every other score at 18.
- **E21** — `eligibility` takes exactly `(scores, cls)` with no stage or
  provenance parameter, and the module's **AST contains no import of
  `ability_score_generation`**, so it cannot obtain adjusted scores at all.
- **E22** — Fighter eligibility is identical before and after a Strength
  12→13 change, evaluated directly on two score sets.
- **E25/E26** — the post-switch and un-switched arrays are evaluated
  directly; the switch itself stays `CHAR-001`'s.
- **E28** — Wisdom is not a Mystic prime requisite, so a switch reaching
  Dexterity leaves Wisdom 12 and the Mystic ineligible.

## 7. Exact Verification Commands Executed

- `uv run python scripts/verify.py`

## 8. Verification Results

- **Tests:** 270 passed, 0 failed (236 after Slice A + 34 new).
- **Coverage:** PASS — differentiated gate: `src/rules/` 11 files, 100%
  required per file, met; core aggregate 100.00% (≥95% required).
- **Ruff:** clean (31 source files).
- **mypy strict:** clean.
- **Overall: PASS.**

Two findings surfaced on the first run and were **fixed rather than
suppressed**: a Ruff `SIM300`-style comparison ordering
(`_HUMAN_CLASSES <= available` → `available >= _HUMAN_CLASSES`), and a mypy
`comparison-overlap` on E18, where asserting `result is not <the other enum
literal>` after already narrowing `result` to one literal is statically
vacuous. E18 was rewritten to demonstrate the distinction properly — the
Druid reports `NOT_ELIGIBLE_AT_CREATION` while a genuinely ability-gated
class (Dwarf, Con 8) reports `NOT_ELIGIBLE_ABILITY_REQUIREMENT` — which is
a stronger test than the one mypy rejected.

## 9. Coverage Results

| File | Statements | Branches | Missing | Partial |
|---|---|---|---|---|
| `src/rules/character_creation/race_and_class_eligibility.py` | 32/32 | **4/4** | 0 | 0 |

Slice A's four files remain at 100%/100% (44/44 + 8/8, 66/66 + 6/6, 12/12,
3/3). No branch was excluded and no coverage configuration was weakened.

## 10. Deviations

**None.** The API, the result enum, the ownership of both tables, the
immutability requirement and the dependency boundaries were all implemented
exactly as approved.

No `EligibilityEngine`, `ClassSelector`, `CharacterCreator`,
`CharacterBuilder`, mediator or coordinator was created.

## 11. Known Limitations/Unresolved Issues

None known, and none deferred silently.

- **E23, E29, E30** are not implemented in this slice by design; they are
  Slice F's, per the approved ledger.
- **P1 (Druid transition ownership)** remains `DEFER FOR HUMAN GOVERNANCE`.
  No Rule ID was assigned, and no part of the transition — the 9th-level
  cleric path, the 29th-level upper bound, the woodland home, the 1d4-month
  meditation, the testing, the admission, or the ongoing maintenance
  conditions — is implemented or discoverable through this module. A test
  asserts the public surface exposes nothing of the kind.
- **P2's Mystic pointers** remain pointers. No Mystic combat, armour
  prohibition, movement, skills, special ability, XP condition, oath
  sanction or alignment tendency is implemented.

## 12. Architectural Consequences

**Dependency boundaries held, and are asserted structurally rather than by
convention.** Tests parse the module's own AST and confirm it imports:

- **no `ability_score_effects`** — every gate is a raw score; a score of 13
  means 13, never adjustment +1. The approved "no `CHAR-002` → `CHAR-007`
  dependency" holds.
- **no `ability_score_generation`** — preserving the approved acyclic
  direction in which `CHAR-001` will import `CHAR-002` in Slice D, never the
  reverse. **No mediator was added** to make the runtime data flow resemble
  the module dependency direction.
- **no `rng` package and no `random`** — eligibility contains no randomness.

**Slice A's public surface is unchanged.** `Ability`, `AbilityScores`,
`CharacterClass`, `AbilityEffect` and `CHAR-007` are used as accepted; none
was broadened, wrapped, duplicated or redesigned. `AbilityScores` remains
the creation-score value object.

No boundary or invariant in `ARCHITECTURE.md` changed. `CLUSTER-002`
implementation remains **IN PROGRESS**; this record completes Slice B only
and marks no later slice, and no cluster, as done.
