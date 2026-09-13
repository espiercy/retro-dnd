# ISSUE-012: CHAR-001 §5 Chapter 10 High-Level Generation (CLUSTER-002 Slice E)

## 1. Issue/Task Identifier and Objective

ISSUE-012 (completion-record ledger). Implement **Slice E** of
`docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` (`APPROVED` 2026-09-12,
revision 4): `CHAR-001` **§5**, the Chapter 10 above-1st-level
ability-score generation methods — implemented, pure, separately callable,
and **deliberately unwired** from ordinary 1st-level creation.

Slices A–D were human-reviewed and **ACCEPTED** before this slice began.
None was redesigned.

With this slice, **`CHAR-001` production implementation is COMPLETE** —
§1, §4, §5, §6.1 and §6.2 all now exist in code, and no `CHAR-001` source
file remains to be written.

**`CHAR-001` full approved-contract verification is PENDING SLICE F.**
Six approved `CHAR-001` cases still have their canonical ownership there:
**`S2`, `W7`, `O1`, `O2`, `O3`, `O4`**. Production completeness and
contract verification are not the same claim, and this record does not
conflate them.

**`CLUSTER-002` is NOT complete**: Slice F remains.

## 2. Approved Inputs/Specifications

- `docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` §7.8, §7.8.1, §8,
  §9.1, §9.2, §12, §14 (Slice E).
- `docs/rules/character_creation/ability_score_generation.md` (`CHAR-001`,
  `APPROVED` 2026-09-04, amended 2026-09-05) **§5** and its deterministic
  cases **H1–H6**, read directly.
- RC p. 130, Step 2, as quoted by §5: the First Method (roll `3d6` eight
  times, keep the six best, assign in any order) and the Second Method
  (`60 + 5d6`, or an equal allotment of at least 60 and at most 90, with
  the 3–18 range still applying).
- `ARCHITECTURE.md` §15.2, "Status update (2026-09-12)".

## 3. Files Created, Modified, or Deleted

**Created:**

- `src/rules/character_creation/high_level_ability_score_generation.py`
- `tests/rules/character_creation/test_high_level_ability_score_generation.py`
- This completion record.

**Modified:**

- `src/rules/character_creation/errors.py` — one addition.
- `docs/completion-records/INDEX.md`.

**Deleted:** none.

**`src/rules/character_creation/__init__.py` was deliberately left
untouched** — a bare docstring with no exports. Adding convenience imports
there would give ordinary creation code a package-level path to the
Chapter 10 module, which is exactly what H6 exists to prevent.

## 4. Behavior Actually Implemented

### Public API

```python
roll_and_keep_six(rng) -> tuple[int, ...]
assign_scores(kept_scores, assignment) -> AbilityScores
roll_point_allocation_total(rng) -> int
allocate_points(total, allocation) -> AbilityScores
```

No `HighLevelCharacterCreator`, `GenerationMethod`, `GenerationMode`, mode
flag, builder, session or player object — asserted by test.

### First Method — rolling and keeping

`roll_and_keep_six` rolls **eight** `3d6` expressions and retains the six
best. It does **not** assign them to abilities.

**Retained-score representation.** The six are returned **in their original
roll order**, the two lowest removed. RC assigns the tuple's order no
mechanical meaning, and roll order was chosen precisely *because* a
descending sort would look like an assignment rule. Where equal values
straddle the six/two cut the earlier roll is dropped — a deterministic
representation choice, not a gameplay tie-break, and the retained multiset
is identical either way.

### Assignment — separate, and the player's

`assign_scores` takes the six retained values and six `Ability`
destinations positionally. The destinations must be a **permutation of all
six abilities**, so every retained score is used exactly once: none can be
duplicated, dropped, altered or rerolled. **No assignment is chosen here**
— RC leaves the order to the player, and this function applies the one it
is given. The result is an immutable `AbilityScores`.

### Second Method — point allocation

`roll_point_allocation_total` implements the **rolled form only**:
`60 + 5d6`, one `5d6` expression.

`allocate_points(total, allocation)` is **agnostic about where `total` came
from**. The equal-allotment form needs no function — the DM's chosen total
is passed straight in — and there is **no `rng=None`, `mode`, `rolled` or
`equal_allotment` parameter**.

Validation order:

| # | Check | Error |
|---|---|---|
| 1 | `total` is an `int` and not a `bool` | `PointAllocationError` |
| 2 | `60 <= total <= 90` | `PointAllocationError` (H5) |
| 3 | `allocation` names exactly the six abilities | `PointAllocationError` |
| 4 | every allocated score is within **3–18** | **`AbilityScoreDomainError`** (H4) |
| 5 | allocated scores sum to `total` | `PointAllocationError` |

**Step 4 runs before any `AbilityScores` is constructed**, so H4 observes
the rules boundary and never the value object's guard; the constructor
remains defence in depth. **Step 4 also precedes step 5 deliberately**, so
a score of 19 is reported as an ability-score violation regardless of
whether the sum also happens to be wrong.

**The 60–90 domain is not narrowed by the rolled form.** `5d6` runs 5–30,
so `roll_point_allocation_total` produces only 65–90 — but 60–64 remain
valid caller-supplied totals under the equal allotment, and
`allocate_points` accepts them.

Nothing is normalized, padded or discarded to make an allocation fit.

## 5. Rules Provenance

**Rules Cyclopedia Explicit** throughout — §5's two methods, the eight
rolls, the six retained, the `60 + 5d6` and 60–90 allotment bounds, and the
3–18 per-ability limitation are all RC p. 130 as the card records them.

**No Simulator Ruling, Human-Approved Variant or alternate-source
completion is involved**, and none was introduced. The retained-tuple
ordering and the allocation-sum invariant are **implementation-contract
choices**, recorded as such in §4 and §10 rather than presented as rules.

## 6. Tests Added or Modified

**24 new tests.**

**Approved contract cases — 6**, the complete Chapter 10 set:

```text
runtime / executable    5   H1, H2, H3, H4, H5
static / import-graph   1   H6
                       ---
                        6
```

All six names are qualified `char001`, so they can never be confused with
`CHAR-003`'s H1–H42.

- **H1** — eight results `18,17,16,15,14,13,12,11`; the six best retained,
  `12` and `11` discarded. The test asserts the retained **multiset**, not
  fixed positions, and then assigns the same six values two different ways
  to demonstrate that **assignment order is the player's**.
- **H2** — an exact-length `ScriptedRNG` plus an exhaustion assertion
  proves **exactly 24 d6 draws**, not 18 and not more, with no reroll.
- **H3** — `5d6 = 3,3,3,3,3` → roll total 15 → point total **75**, with
  exactly five draws audited.
- **H4** — total 75 and an allocation placing **19** in one ability. The
  allocation sums to 75, so the rejection is unambiguously about the score;
  it raises **`AbilityScoreDomainError`**, not `PointAllocationError` and
  not `ValueError`.
- **H5** — totals **59** and **91** rejected with `PointAllocationError`.
- **H6** — the AST of `ability_score_generation.py` contains no import of
  this module.

**Implementation/coverage tests — 18, counted separately** under an
explicit banner: roll-order retention; equal values straddling the cutoff;
three assignment-shape rejections; the every-score-used-once property; bool
and non-integer totals; the legal **60** and **90** boundaries; malformed
allocation shape; sum mismatch; a below-range score; zero RNG for
assignment and allocation; the reverse import direction; dependency
boundaries; concrete-RNG absence; no generation-mode or orchestration
names; and the error hierarchy.

## 7. Exact Verification Commands Executed

- `uv run python scripts/verify.py`

## 8. Verification Results

- **Tests:** 414 passed, 0 failed (390 after Slice D + 24 new).
- **Coverage:** PASS — `src/rules/` 14 files, 100% required per file, met;
  core aggregate 100.00%.
- **Ruff:** clean (37 source files).
- **mypy strict:** clean.
- **Overall: PASS**, on the first run; no finding was suppressed.

## 9. Coverage Results

| File | Statements | Branches | Missing | Partial |
|---|---|---|---|---|
| **`high_level_ability_score_generation.py`** | **53/53** | **16/16** | 0 | 0 |
| `errors.py` | 10/10 | — | 0 | 0 |

Slices A–D remain at 100%/100%. No branch excluded; no configuration
weakened.

## 10. Deviations

**None from the approved plan or the card.**

**Two implementation-contract decisions, recorded rather than left
implicit:**

**(a) `assign_scores` shape violations raise `ValueError`.** The §26
guidance offered three options; this is the smallest coherent one. A wrong
number of retained scores, or a destination sequence that is not a
permutation of the six abilities, is a **structural** input error of
exactly the kind `src/rules/exploration/turn_credit.py` and
`AbilityScores.__post_init__` already raise `ValueError` for.
`PointAllocationError` was rejected as ill-fitting — these are not point
totals — and a new `AssignmentError` was rejected as an unjustified type
for a case **no approved H-case turns on**. A retained score outside 3–18
still raises `AbilityScoreDomainError`, from the value object, which is the
correct type either way.

**(b) The allocation-sum invariant.** No approved H-case names it, and it
is recorded as implementation-contract validation, **not a new Rule Card
case**. The operation cannot faithfully allocate a total it is not given,
and silently normalizing, padding or discarding points would be a rules
change.

`errors.py` gained exactly one type, `PointAllocationError`. **No
speculative Slice-F error was added** — Slice F adds no production code and
needs none.

## 11. Known Limitations/Unresolved Issues

- **Slice F remains**: `E29`, `E30`, `O1`, `O2`, `O4` executable
  composition; `E23`, `S2`, `W7`, `O3` calling-contract record; the
  non-contract `CHAR-001`→`CHAR-007` composition test; and the cluster
  completion record.
- **P1** (Druid transition) and **P3** (Chapter 13 Ability Check) remain
  `DEFER FOR HUMAN GOVERNANCE`; no Rule ID assigned.
- **`CHAR-003` W2** stays moot and **W3** stays not-V1-wired; Chapter 10
  Step 6 (hit points above 1st level) is `CHAR-003`'s §7 and is **not**
  implemented — this slice covers Step 2, the *ability-score* methods.

## 12. Architectural Consequences

**The separation H6 protects is bidirectional and structural.**
`ability_score_generation.py` does not import this module (H6), and this
module does not import `ability_score_generation.py` either — asserted by a
second, independent AST test. They are sibling pure rule modules with no
coupling in either direction and **no circular dependency**.

**Ordinary generation is unchanged.** No file from Slices A–D was modified
except `errors.py`, which gained one class. `generate_ability_scores`
remains the only 1st-level generation path.

**No Chapter 1 procedure leaks into Chapter 10.** The discard provision
(SR-4) is not imported or applied here — Chapter 10 specifies its own
generation procedures — and neither `apply_highest_score_switch` nor
`apply_trade` is invoked. Any later composition belongs to a caller or a
future approved flow.

**Dependencies, asserted from the module's own AST:** `rng` (the `RNG`
Protocol only — `SeededRNG`/`ScriptedRNG` asserted absent), `ability` and
`errors`. **No** `race_and_class_eligibility`, **no**
`ability_score_effects`, **no** `hit_points_and_hit_dice`, **no**
`rules.exploration`, **no** `random`.

**RNG boundaries:** `roll_and_keep_six` consumes 8 × `roll("3d6")` = 24 d6;
`roll_point_allocation_total` consumes 1 × `roll("5d6")` = 5 d6;
`assign_scores` and `allocate_points` consume **zero**, proved with an
empty `ScriptedRNG`.

**`CHAR-001` production implementation is complete**; its **full
approved-contract verification remains pending Slice F**, which owns
`S2`, `W7`, `O1`, `O2`, `O3` and `O4`.

**`CLUSTER-002` implementation remains IN PROGRESS** — Slice F is
outstanding, and no cluster is marked complete by this record.
