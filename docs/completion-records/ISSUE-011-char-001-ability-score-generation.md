# ISSUE-011: CHAR-001 Ability Score Generation §1/§4/§6 (CLUSTER-002 Slice D)

## 1. Issue/Task Identifier and Objective

ISSUE-011 (completion-record ledger). Implement **Slice D** of
`docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` (`APPROVED`
2026-09-12, revision 4): `CHAR-001` §1 standard generation, §6.1 the
discard predicate, §6.2/§6.2.1 the authorized Chapter 13 switch, and §4 the
2-for-1 prime-requisite trade under rules R1–R11.

**`CHAR-001` is not wholly implemented by this record.** §5, the Chapter 10
above-1st-level generation methods, remains **Slice E**.

Slices A, B and C were human-reviewed and **ACCEPTED** before this slice
began. None was redesigned.

## 2. Approved Inputs/Specifications

- `docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` §7.7, §8, §9.1, §9.2,
  §10.1, §10.2, §12 (revision 4), §14 (Slice D).
- `docs/rules/character_creation/ability_score_generation.md` (`CHAR-001`,
  `APPROVED` 2026-09-04, **amended 2026-09-05** with trade rule `R11` and
  cases `C1`–`C5`) — the governing Rule Card, §0, §1, §4, §6.1, §6.2,
  §6.2.1, and its deterministic test table read directly.
- `docs/rules/character_creation/race_and_class_eligibility.md`
  (`CHAR-002`, `APPROVED`) — the authoritative prime-requisite and
  creation-minimum tables, consumed, never duplicated.
- `docs/technical/RNG_CONTRACT.md` and `src/rng` — the `RNG` Protocol.
- `ARCHITECTURE.md` §15.2, "Status update (2026-09-12)".

## 3. Files Created, Modified, or Deleted

**Created:**

- `src/rules/character_creation/ability_score_generation.py`
- `tests/rules/character_creation/test_ability_score_generation.py`
- This completion record.

**Modified:**

- `src/rules/character_creation/errors.py` — four additions only.
- `docs/completion-records/INDEX.md`.

**Deleted:** none. **No Slice-A, -B or -C production file was modified**
other than the shared error module.

`high_level_ability_score_generation.py` was **not created**, and no
placeholder or stub for it exists.

## 4. Behavior Actually Implemented

### Public API — four independent pure operations

```python
generate_ability_scores(rng) -> AbilityScores
discard_may_be_offered(scores) -> bool
apply_highest_score_switch(scores, target_class, source_ability,
                           target_prime_requisite) -> AbilityScores
apply_trade(scores, chosen_class, donor, target) -> AbilityScores
```

**No engine, session, state machine or orchestration object.** The module
docstring states the canonical §0 sequence explicitly and then states, just
as explicitly, that **it does not orchestrate that sequence**.

### §1 Standard generation

One `3d6` expression per ability in `Ability` declaration order, each
recorded against the ability it was rolled for: **six expressions, 18 d6
draws, six sequence numbers**. `RNG.roll()` returns a `RollResult`; `.total`
is read. No reroll, discard, sorting, reassignment, drop-lowest, switch or
trade occurs inside generation.

### §6.1 Discard predicate — SR-4

```text
no ability score is above 9   OR   at least two scores are below 6
```

Both boundaries exclusive as written: **9 is not above 9**, **6 is not below
6**. Returns `True`/`False` only. It discards nothing and rerolls nothing.

### §6.2/§6.2.1 Authorized switch — SR-3

Performs an **already-authorized** switch. Both ends are explicit: the
destination because three classes carry two prime requisites, the source
because **any tied maximum may be the authorized source** and no
ability-order, alphabetical or random tie-break exists. Operation-level
validation: the source holds the maximum; the destination is a prime
requisite of the requested class (read from `CHAR-002`); the two differ.
Exactly two abilities exchange values — asserted by test — with no free
rearrangement, copying, creation or destruction of scores.

### §4 The atomic trade — R1–R11

**One invocation is exactly one 2-for-1 exchange.** There is no `amount`,
`count`, `points`, `trade_until` or `maximize` parameter, and no production
helper loops it. RC's own p. 7 example (T13/C5) is **three calls**.

| Rule | Implementation | Error |
|---|---|---|
| **R1/R2** | `target in prime_requisites(chosen_class)` — `CHAR-002` is the authority, so two-prime-requisite classes need no branch | `IllegalTradeError` ("R1") |
| **R5** | `donor is not target` — §4's `score(D) -= 2; score(T) += 1` treats them as distinct operands, and only the target is raised | `IllegalTradeError` ("R5") |
| **R3** | donor is neither Constitution nor Charisma | `IllegalTradeError` ("R3") |
| **R4** | donor is not Dexterity — bars **lowering** only | `IllegalTradeError` ("R4") |
| **R6/R7** | `scores[donor] - 2 >= 9` | `IllegalTradeError` ("R6/R7") |
| **R11** | `scores[target] + 1 <= 18`, on the prospective value | `PrimeRequisiteCeilingError` ("R11") |
| **R10** | every `creation_minimums(chosen_class)` entry still satisfied | `ClassMinimumViolationError` ("R10") |
| **R8** | trade is optional — **caller contract**, T11 | — |
| **R9** | trade happens at this step only — **caller contract**, S2 (Slice F) | — |

**Validation ordering is load-bearing**, and reproduces every approved
discrimination: **R6/R7 precedes R11**, so `T14` reports the donor floor
even though its target would also breach the ceiling; **R11 precedes result
construction**, so `C2`/`C4` report `PrimeRequisiteCeilingError` and never
the value object's guard; **R10 is evaluated on the prospective result**,
so `V2` reports R10 where R6's floor would have permitted the trade.

A simple R1 → R5 → R3 → R4 → R6/R7 → R11 → R10 sequence reproduces all of
them. **No generic rule engine was built.**

## 5. Rules Provenance

- **Rules Cyclopedia Explicit** — §1 generation, the six abilities and
  their order, the 3–18 range; §4 rules R1–R4, R8, R9; §6.1/§6.2's
  provisions as stated.
- **Necessary Mathematical-Mechanical Consequence** — R6/R7's arithmetic
  consistency; **R11**, from RC's standing range limitation for ability
  scores (RC p. 6; p. 130). **`R11` is recorded in code as a Necessary
  Consequence, explicitly not RC-explicit at p. 7 and explicitly not a
  Simulator Ruling** — the `PrimeRequisiteCeilingError` docstring says so.
- **Simulator Ruling SR-2** — a Mystic may raise Dexterity. **No
  Mystic-specific code exists**; the general machinery produces it from
  `CHAR-002`'s prime-requisite table.
- **Simulator Ruling SR-3** — the switch is in V1, runs before eligibility,
  and may establish a reachable minimum.
- **Simulator Ruling SR-4** — the discard criterion.
- **Simulator Ruling SR-5** — rule R10.

## 6. Tests Added or Modified

**66 new tests.**

**Approved contract cases — 57**, per the revision-4 ledger:

```text
runtime / executable   52   G1-G5, T1-T10, T12-T14, S3, M1-M5, V1-V12,
                            W1, W3-W5, D1-D6, D8, C1-C5
static / API-shape      1   S1
calling-contract        4   T11, W2, W6, D7   -- no pytest functions
                       ---
                        57
```

53 pytest functions carry the runtime and static cases; the four
calling-contract cases have **none**, by design, and each is marked in the
test file at its position in the card's order with the reason.

**Implementation/coverage tests — 13, counted separately**, under an
explicit banner: switch invalid source, invalid destination and degenerate
source-equals-destination; tied-maximum acceptance from either side;
exactly-two-scores-change; donor-equals-target rejection; zero-RNG for
switch/trade/discard; error hierarchy; public surface; the Chapter 10
import-graph guard; dependency boundaries; concrete-RNG absence; and
absence of every forbidden orchestration name.

**Not implemented here:** S2, W7, O1–O4 (Slice F) and H1–H6 (Slice E).

### T11 / W2 / W6 / D7 — calling-contract evidence

**Certified for this slice. No runtime state was added to prove any of
them.**

- **T11** — *`apply_trade` is optional; not invoking it leaves the immutable
  `AbilityScores` unchanged.* The function cannot enforce a caller's
  decision not to call it, and `AbilityScores` is frozen, so an uninvoked
  trade changes nothing by construction. **No `enabled` flag exists.**
- **W2** — *authorization is external; an unauthorized switch means
  `apply_highest_score_switch` is not called.* The operation performs an
  already-authorized switch and has **no `authorized` parameter**.
- **W6** — *the operation itself performs one two-score swap; the caller or
  policy may authorize at most one switch.* The swap clause is executable
  and covered (W1, W4, W5, and `test_switch_changes_exactly_two_scores`).
  The at-most-one clause is a caller obligation the stateless function
  cannot observe — nothing stops a second invocation. **No
  `already_switched`, switch count, creation state or session state
  exists.**
- **D7** — *`discard_may_be_offered` returns permission to offer; it never
  forces a discard, and the caller or player may retain the character.* The
  predicate returns a `bool` and has **no `discard_choice` or
  `player_choice` parameter** through which acceptance could be expressed.

## 7. Exact Verification Commands Executed

- `uv run python scripts/verify.py`

## 8. Verification Results

- **Tests:** 390 passed, 0 failed (324 after Slice C + 66 new).
- **Coverage:** PASS — `src/rules/` 13 files, 100% required per file, met;
  core aggregate 100.00%.
- **Ruff:** clean (35 source files).
- **mypy strict:** clean.
- **Overall: PASS**, on the first run; no finding was suppressed.

## 9. Coverage Results

| File | Statements | Branches | Missing | Partial |
|---|---|---|---|---|
| **`ability_score_generation.py`** | **59/59** | **22/22** | 0 | 0 |
| `errors.py` | 9/9 | — | 0 | 0 |

Slices A–C remain at 100%/100%. No branch excluded; no configuration
weakened.

## 10. Deviations

**None from the approved plan or the card.**

**One implementation-contract decision with no approved case, flagged
rather than left implicit:** `apply_trade` rejects `donor is target` as an
**R5** violation. No approved case names it — `M4` is the nearest, and it is
caught earlier by R1 because Wisdom is not a Mystic prime requisite. The
rejection is read off §4's own pseudocode, which treats `D` and `T` as
distinct operands, and off R5's "only the target is raised": applying both
halves to one ability is not the specified operation. Without it, a
same-ability request would silently net −1. **A reviewer who reads it
differently should say so.**

`errors.py` gained exactly four types. **`PointAllocationError` was not
pre-stubbed**; it belongs to Slice E.

## 11. Known Limitations/Unresolved Issues

- **`CHAR-001` §5 (Chapter 10) is not implemented** — Slice E. This module
  does not import it, asserted from the module AST, which is the mechanism
  that will preserve approved case `H6`.
- **S2, W7, O1–O4** remain Slice F's.
- **P1** (Druid transition) and **P3** (Chapter 13 Ability Check) remain
  `DEFER FOR HUMAN GOVERNANCE`; no Rule ID assigned.

## 12. Architectural Consequences

**`CHAR-001` → `CHAR-002` is a real production dependency**: the module
imports `prime_requisites` and `creation_minimums` and **duplicates
neither table**. `eligibility()` is deliberately **not** imported — the raw
minimum table is sufficient for R10, and R10 preserves eligibility rather
than re-running it.

**The dependency direction is acyclic and inverted relative to the data
flow**, exactly as the plan's §10.2 predicted: scores flow `CHAR-001` →
`CHAR-002` at runtime, while the module dependency runs `CHAR-001` →
`CHAR-002`. **No mediator was added** to make the two directions agree.

**Boundaries asserted from the module's own AST:** imports `rng` (the `RNG`
Protocol only — `SeededRNG`/`ScriptedRNG` asserted absent) and
`race_and_class_eligibility`; imports **no** `ability_score_effects`, **no**
`hit_points_and_hit_dice`, **no** `high_level_ability_score_generation`,
**no** `rules.exploration`, **no** `random`.

**No orchestration object exists** — a test asserts the module namespace
contains none of `Character`, `Player`, `CharacterCreator`,
`CharacterBuilder`, `CharacterCreationEngine`, `CreationSession`,
`CreationState`, `CreationPhase` or `GameState`, and no `selected_class`,
`switch_used`, `creation_complete` or `discard_choice` field was added
anywhere.

**No class-name literal appears in the module's source at all** — asserted
by AST in `V7`, which is what makes R10 general rather than a Mystic
special case.

`CLUSTER-002` implementation remains **IN PROGRESS**. This record completes
Slice D only; **`CHAR-001` §5 remains Slice E**, and no cluster is marked
done.
