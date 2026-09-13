# ISSUE-013: CLUSTER-002 Cross-Card Integration (Slice F)

## 1. Issue/Task Identifier and Objective

ISSUE-013 (completion-record ledger). Implement **Slice F** of
`docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` (`APPROVED` 2026-09-12,
revision 4): the cross-card composition tests, the calling-contract
conformance evidence, and the producer/consumer composition regression that
close the last nine approved `CLUSTER-002` cases.

Slices A–E were human-reviewed and **ACCEPTED** before this slice began.

**This slice adds no production mechanics, and no `src/` file changed.**

## 2. Approved Inputs/Specifications

- `docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` §10.1, §10.2, §12
  (revision 4), §14 (Slice F).
- `docs/rules/character_creation/race_and_class_eligibility.md`
  (`CHAR-002`) — approved cases **E23, E29, E30**, read directly.
- `docs/rules/character_creation/ability_score_generation.md`
  (`CHAR-001`) — approved cases **S2, W7, O1, O2, O3, O4**, read directly.
- The accepted Slice A–E production modules, composed through their real
  public APIs.

## 3. Files Created, Modified, or Deleted

**Created:**

- `tests/rules/character_creation/test_cluster_002_integration.py`
- This completion record.
- `docs/completion-records/ISSUE-014-cluster-002-character-foundation.md`

**Modified:**

- `docs/completion-records/ISSUE-012-…md` — lifecycle-wording correction
  only (§4 below).
- `docs/completion-records/INDEX.md`.
- `docs/rules/clusters/CLUSTER-002-character-foundation.md` and
  `ARCHITECTURE.md` §15.2 — implementation-progress wording only.

```text
src/ :  NO CHANGES
```

**No production defect was found**, so no corrective production work was
needed or performed. Had one surfaced, the instruction was to stop and
report rather than fix it inside this slice.

## 4. ISSUE-012 Lifecycle-Wording Correction

`ISSUE-012` claimed *"`CHAR-001` is implemented in full against its
approved contract."* **Production** completeness and **contract
verification** are not the same claim, and six approved `CHAR-001` cases —
`S2`, `W7`, `O1`, `O2`, `O3`, `O4` — still had their canonical ownership
here. Corrected to:

```text
CHAR-001 production implementation:        COMPLETE
CHAR-001 approved-contract verification:   PENDING SLICE F
```

No Rule Card case, mechanic, test count or implementation changed.

## 5. Behavior Actually Verified

### Executable cross-card composition — 5 cases

| Case | Composition | Result |
|---|---|---|
| **E29** | A Mystic qualified on Wis 13 / Dex 13 (`CHAR-002` says `ELIGIBLE`), then `CHAR-001`'s trade lowers Wisdom | **`ClassMinimumViolationError` (R10)**. `CHAR-002`'s result is an invariant the trade must preserve; the enforcement lives in `CHAR-001`, and this case makes the requirement visible from the card that owns the minimum |
| **E30** | **Exhaustive**: for each of the eight selectable classes, every donor × target pair (8 × 36 = **288 attempts**), every trade `CHAR-001` permits is re-checked by `CHAR-002` | Every permitted trade leaves the class still `ELIGIBLE`. The Druid is excluded because `CHAR-002` makes it unselectable at creation, so *"any selected class"* cannot include it |
| **O1** | Constitution 8; Fighter chosen; trade raises Str 12 → 13; Dwarf eligibility re-tested | Still `NOT_ELIGIBLE_ABILITY_REQUIREMENT`. **The trade establishes nothing** — contrast W1, where the *switch* can |
| **O2** | Int 8 (Elf ineligible) → authorized switch establishes the Intelligence minimum → Elf `ELIGIBLE` → trade raises Intelligence further | Legal. The switch established eligibility; the trade then operated as an ordinary post-eligibility adjustment, and eligibility still holds |
| **O4** | Generation yields a discard-qualifying array → discarded → generation restarts → the **replacement** proceeds to eligibility and trade | The discarded array reaches no later step. Only the replacement is carried forward |

**O2, recorded precisely.** The card writes *"switch establishes Int 9"*.
The switch must move the **highest** score, so a construction in which
Intelligence lands on exactly 9 would require the maximum to be 9 — leaving
no donor at 11 or above for the subsequent trade. *"Int 9"* therefore
denotes the Elf's **Intelligence-9 minimum**, which the switch establishes.
This is stated in the test rather than silently resolved.

**No rule logic is duplicated in any test.** Each composes the real public
APIs; each would fail if `CHAR-001` permitted a trade violating a selected
class's minimum, or if `CHAR-002`'s view of the resulting scores disagreed
with the approved invariant.

### Documented calling-contract conformance — 4 cases

**No pytest function was written for any of them, and no fake negative test
was created to make a policy statement look executable.**

| Case | Approved requirement | Why the pure primitive cannot observe a violation | Where the obligation is documented | Forbidden state **not** introduced | Positive executable evidence |
|---|---|---|---|---|---|
| **E23** | A Chapter 13 switch applied **after** a class is chosen is rejected — the switch runs before `CHAR-002` (SR-3) | `apply_highest_score_switch` receives scores, a class, a source and a destination. Nothing in those four arguments records whether class selection has happened | `CHAR-001` module docstring's canonical sequence (switch at step 3, eligibility at step 4); `CHAR-002` §4's ordering diagram; the switch function's own docstring | No `class_selected` flag, no `CreationPhase`, no `CreationState`, no selected-class field anywhere in production | **O2** — the switch runs before eligibility and the sequence produces the approved result |
| **S2** | A trade attempted **after creation completes** is rejected (R9: *"No such adjustments can be made later"*) | "Creation is complete" is not derivable from six integers and a class. Observing it would require lifecycle state | **R9 is stated in `apply_trade`'s own docstring** as a caller contract, and in the module docstring's sequence | No `creation_complete` flag, no session, no phase parameter. `apply_trade`'s signature is exactly `(scores, chosen_class, donor, target)` | **O1, O2, O4** — the trade occurring in its approved position produces the approved results |
| **W7** | A switch attempted **after** a class is chosen is rejected — it runs at §0 step 3 | Identical unobservability to E23, seen from `CHAR-001`'s side | Same artifacts as E23 | Same as E23: the switch module holds **no creation-phase state at all** | **O2** |
| **O3** | A trade attempted **before** eligibility is evaluated is rejected — §0 step 6 follows step 5 | `apply_trade` cannot observe whether `CHAR-002` has run. It never calls `eligibility()` and has no parameter through which the answer could arrive | `CHAR-001` module docstring's canonical sequence; `apply_trade`'s docstring | No `eligibility_checked` flag, no phase, no creation state, and **no Slice-F production wrapper** was introduced to enforce the order | **O1, O2, O4** — eligibility and class choice precede the trade, and the composed sequence works |

Each row is inspectable: the artifacts named exist in the committed source
and can be read.

### Non-contract composition regression — not an approved case

Implementation plan §10.1's producer/consumer proof:

```text
CHAR-001 produced domain   3-18
CHAR-007 accepted domain   2-18
3-18 ⊆ 2-18
```

The test feeds every score of five real `CHAR-001` outputs — three
generations (all-3s, all-18s, mixed), a switch result, and a trade landing
exactly on 18 — into `CHAR-007`'s `adjustment()`, and every lookup answers.
It then shows the boundary that caused the Pre-Code blocker from both
sides: **`R11` rejects the trade that would produce 19**, and
`adjustment(19)` would indeed have raised.

**Slice F was kept narrow.** No broad integration suite was written merely
because all the modules now exist, and `H36` and the comprehensive unit
tests were not duplicated.

## 6. Exact 189-Case Reconciliation

**By verification kind — no case in two categories:**

```text
EXECUTABLE PYTEST CASE (unit)                                      172
CROSS-CARD RUNTIME COMPOSITION                                       5
    E29, E30, O1, O2, O4                              <- this slice
STATIC / API-SHAPE CONFORMANCE                                       3
    S1 (Slice D), CHAR-003 H36 (Slice C), CHAR-001 H6 (Slice E)
DOCUMENTED CALLING-CONTRACT CONFORMANCE                              9
    E23, S2, W7, O3                                   <- this slice
    CHAR-003 H38                                      <- ISSUE-010
    CHAR-001 T11, W2, W6, D7                          <- ISSUE-011
                                                                   ---
                                                                   189
```

**By Rule Card and slice:**

```text
CHAR-001   Slice D  57
           Slice E   6
           Slice F   6   S2, W7, O1, O2, O3, O4
                    ---
                     69

CHAR-002   Slice B  27
           Slice F   3   E23, E29, E30
                    ---
                     30

CHAR-003   Slice C  42
CHAR-007   Slice A  48
                    ---
           TOTAL   189
```

**Zero duplicates, zero omissions.** Supporting executable assertions —
O1/O2/O4 standing as positive evidence for E23/S2/W7/O3 — create no extra
Rule Card case.

**`H38`, `T11`, `W2`, `W6` and `D7` are not re-owned here.** Their canonical
completion records are `ISSUE-010` (Slice C) and `ISSUE-011` (Slice D);
`ISSUE-014` references them in the cluster reconciliation.

## 7. Exact Verification Commands Executed

- `uv run python scripts/verify.py`

## 8. Verification Results

- **Tests:** 420 passed, 0 failed (414 after Slice E + 6 new).
- **Coverage:** PASS — `src/rules/` 14 files, 100% required per file, met;
  core aggregate 100.00%.
- **Ruff:** clean (38 source files).
- **mypy strict:** clean.
- **Overall: PASS**, on the first run.

Every `src/rules/` file remains at its required threshold; because no
production code changed, the per-file figures are unchanged from Slice E.

## 9. Dependency Composition Results

| Boundary | Result |
|---|---|
| **`CHAR-001` → `CHAR-007`** | **Proven executably.** Every score five real `CHAR-001` outputs contain is accepted by `adjustment()`; `R11` keeps 19 out of the output range |
| **`CHAR-001` ↔ `CHAR-002`** | **Proven in both directions.** The switch *can* establish a minimum (O2); the trade *cannot establish* one (O1) and *cannot destroy* one (E29, E30). The asymmetry the cards describe holds in code |
| **`CHAR-003` → `CHAR-007`** | Already structural and covered by `H36`; **not duplicated here**, because a composition test would add no information |

## 10. Deviations

**None.** No production code was written, no orchestration object or
test-only coordinator was introduced, and no approved case was rewritten.

## 11. Known Limitations/Unresolved Issues

Deferred items are untouched and unresolved by this slice:

```text
P1 — Druid transition ownership          DEFER FOR HUMAN GOVERNANCE
P3 — Chapter 13 Ability Check Rule ID    DEFER FOR HUMAN GOVERNANCE
CHAR-003 W2                              MOOT
CHAR-003 W3                              NOT V1-WIRED
```

**No Rule ID was invented.**

## 12. Architectural Consequences

**No application layer was created.** The integration tests compose four
public functions from `CHAR-001`, two from `CHAR-002` and one from
`CHAR-007`, directly, in the approved order. There is no
`CharacterCreationEngine`, `CharacterCreator`, `CharacterBuilder`,
`CreationSession`, `CreationState`, `CreationPhase`, `Character` aggregate,
test-only orchestration class or fake coordinator anywhere in the
repository.

**No lifecycle state was introduced to make a calling contract
observable** — the point of classifying those four cases as calling
contracts in the first place.

**Remaining step: final human review of the complete
`cluster-002-implementation` branch, then a single `--no-ff` merge to
`main`.** This record does **not** mark the branch merged, and the merge is
not authorized by it.
