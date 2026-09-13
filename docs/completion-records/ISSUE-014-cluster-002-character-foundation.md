# ISSUE-014: CLUSTER-002 Character Foundation — Cluster Completion

## 1. Lifecycle Status

```text
implementation work:        COMPLETE ON IMPLEMENTATION BRANCH
human final branch review:  PENDING
merge to main:              PENDING
```

**`CLUSTER-002` is not landed, not merged, and not production complete.**
The completed work sits on `cluster-002-implementation`; `main` is
unchanged at the approval commit. This record summarizes the branch for
that final review — it does not authorize the merge.

`ARCHITECTURE.md` §15.2's readiness remains **`PASS`**. That is the
*authorization* gate cleared on 2026-09-12, not a completion flag, and
nothing here changes it.

## 2. Objective

ISSUE-014 (completion-record ledger). Summarize the complete
`CLUSTER-002` Character Foundation implementation — Slices A through F —
as the final artifact before human branch review, supplementing (not
substituting for) the six per-slice records.

## 3. Approved Inputs

- `docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` — `APPROVED`
  2026-09-12, revision 4.
- `ARCHITECTURE.md` §15.2, "Status update (2026-09-12)" — `CLUSTER-002`
  historical-rules implementation `AUTHORIZED`, bounded to the four-card
  boundary and that plan.
- The four `APPROVED` Rule Cards (2026-09-04; `CHAR-001` amended
  2026-09-05).

## 4. Slices A–F

| Slice | Record | Delivered |
|---|---|---|
| **A** | `ISSUE-008` | Shared primitives (`Ability`, `AbilityScores`, `CharacterClass`), the error base, and `CHAR-007` in full |
| **B** | `ISSUE-009` | `CHAR-002` eligibility; the authoritative prime-requisite and creation-minimum tables |
| **C** | `ISSUE-010` | `CHAR-003` hit points — one level-aware operation. Human-review correction `ee0aa7a` added `bool`/non-`int` level rejection |
| **D** | `ISSUE-011` | `CHAR-001` §1 generation, §6.1 discard, §6.2 switch, §4 trade under R1–R11 |
| **E** | `ISSUE-012` | `CHAR-001` §5 Chapter 10 methods — implemented, pure, unwired |
| **F** | `ISSUE-013` | Cross-card composition, calling-contract evidence, producer/consumer regression. **No production code**. Final-review correction `O2` (below) followed |

Plan **revision 4** (`45e3e76`) reclassified four `CHAR-001` cases before
Slice D, as a separate documentation commit.

**Final-review correction, 2026-09-12 — `CHAR-001` `O2` deterministic
fixture.** Slice F found during final integration that O2's approved
fixture (*"switch establishes Int 9 … then trade raises Int further"*) was
**internally impossible**: the Chapter 13 switch moves the **highest**
score, so Intelligence landing on exactly 9 requires 9 to be the maximum,
while a subsequent trade requires a donor of at least 11 (R6). Slice F
recorded the contradiction rather than reinterpreting an approved case; the
human project owner then authorized a realizable replacement fixture
(Str 16 / Int 8 → switch → Int 16 → Elf eligible → trade Wis 13 → 11,
Int 16 → 17). **No mechanic changed, no case ID changed, and no total
changed** — see `ISSUE-013` §5.2 and the Rule Card's Amendment history.

## 5. Rule Cards Implemented

| Rule Card | Production module | Status |
|---|---|---|
| `CHAR-001` Ability Score Generation | `ability_score_generation.py`, `high_level_ability_score_generation.py` | Implemented; contract verified |
| `CHAR-002` Race & Class Eligibility | `race_and_class_eligibility.py` | Implemented; contract verified |
| `CHAR-003` Hit Points & Hit Dice | `hit_points_and_hit_dice.py` | Implemented; contract verified |
| `CHAR-007` General Ability Score Effects | `ability_score_effects.py` | Implemented; contract verified |

Shared, owned by no single card: `ability.py`, `character_class.py`,
`errors.py`.

## 6. 189 Approved Cases — Final Reconciliation

**By verification kind:**

```text
EXECUTABLE PYTEST CASE (unit)                                      172
CROSS-CARD RUNTIME COMPOSITION                                       5
    E29, E30, O1, O2, O4                          ISSUE-013 / Slice F
STATIC / API-SHAPE CONFORMANCE                                       3
    CHAR-001 S1                                   ISSUE-011 / Slice D
    CHAR-003 H36                                  ISSUE-010 / Slice C
    CHAR-001 H6                                   ISSUE-012 / Slice E
DOCUMENTED CALLING-CONTRACT CONFORMANCE                              9
    E23, S2, W7, O3                               ISSUE-013 / Slice F
    CHAR-003 H38                                  ISSUE-010 / Slice C
    CHAR-001 T11, W2, W6, D7                      ISSUE-011 / Slice D
                                                                   ---
                                                                   189
```

**By Rule Card:**

```text
CHAR-001   57 (D) +  6 (E) +  6 (F)  =  69
CHAR-002   27 (B) +  3 (F)           =  30
CHAR-003   42 (C)                    =  42
CHAR-007   48 (A)                    =  48
                                       ---
                                       189
```

**Every approved case has exactly one canonical owner. Zero duplicates,
zero omissions.** The nine calling-contract cases have no pytest function
by design; their evidence is in the completion records named above, and no
runtime state was added anywhere to make them observable.

## 7. Implementation / Composition Tests

Counted **separately** from the 189: 28 (Slice A), 7 (B), 13 (C, including
two from the human-review correction), 13 (D), 18 (E), and 1
producer/consumer regression (F). Every test module states in its own
docstring which of its tests are approved cases and which are not.

## 8. Simulator Rulings Carried Into Code

| Ruling | Where it lives | How it is marked |
|---|---|---|
| **SR-1** Elf `+2` at 10th | `_FIXED_GAIN[ELF]` | An in-code comment records it as a **ruling, not an RC-explicit value**, names both printed RC readings, and names the 14-location reversal surface. `H25` fails loudly on a partial change |
| **SR-2** Mystic may raise Dexterity | *No Mystic-specific code* | Produced by the general trade machinery from `CHAR-002`'s table. `V7` asserts by AST that **no class-name literal appears in `ability_score_generation.py` at all** |
| **SR-3** Switch included in V1, before eligibility | `apply_highest_score_switch` + the §0 sequence in the module contract | Authorization stays external; `W2` is a calling contract |
| **SR-4** Discard criterion | `discard_may_be_offered` | Returns permission only; `D7` is a calling contract |
| **SR-5** Class eligibility invariant | `apply_trade` rule **R10**, `ClassMinimumViolationError` | Distinct error type because `V2` turns on distinguishing it from R6 |

**`R11` is recorded as a Necessary Mechanical Consequence**, explicitly not
RC-explicit at p. 7 and explicitly not a Simulator Ruling, in both the error
docstring and the module.

## 9. Architectural Boundaries Preserved

**No orchestration object exists anywhere in the repository.** Confirmed by
direct source audit, not only by test: no `CharacterCreationEngine`,
`CharacterCreator`, `CharacterBuilder`, `CreationSession`, `CreationState`,
`CreationPhase`, `Character` aggregate, `Player`, `Party`, `GameState`,
generic effects registry, or generic advancement API.

**No lifecycle state** — no `selected_class`, `switch_used`,
`creation_complete`, `discard_choice`, `already_rolled`,
`eligibility_checked` or phase field — was added to make any calling
contract observable.

**Dependency graph, asserted from module ASTs rather than by convention:**

```text
ability, character_class, errors        shared, owned by no card
        |
        +--> ability_score_effects            (CHAR-007)  imports no consumer
        |         ^
        |         |
        +--> hit_points_and_hit_dice          (CHAR-003)  -> CHAR-007
        |
        +--> race_and_class_eligibility       (CHAR-002)  no CHAR-007, no CHAR-001
        |         ^
        |         |
        +--> ability_score_generation         (CHAR-001)  -> CHAR-002
        |
        +--> high_level_ability_score_generation  (CHAR-001 §5)
                 no import to or from ordinary generation -- H6
```

Acyclic. `src/rules/character_creation/__init__.py` remains a bare
docstring with no exports, so no package-level path to the Chapter 10
module exists.

**No `src/domain/`, `src/models/` or `src/core/character/` layer** was
created; the domain-local shared-value precedent of
`src/rules/exploration/turn_credit.py` was followed.

**`ADV-002`'s boundary is respected:** `CHAR-003`'s Name-level and
maximum-level values are private, card-local constants with a docstring
naming `ADV-002` as the future authoritative owner that must replace or
reconcile the projection. No advancement API is exported.

## 10. Deferred Items — Unchanged

```text
P1 — Druid transition ownership          DEFER FOR HUMAN GOVERNANCE
P3 — Chapter 13 Ability Check Rule ID    DEFER FOR HUMAN GOVERNANCE
CHAR-003 W2                              MOOT
CHAR-003 W3                              NOT V1-WIRED
```

**No Rule ID was invented, and no slice resolved any of them.**

## 11. Coverage

| File | Statements | Branches |
|---|---|---|
| `ability.py` | 44/44 | 8/8 |
| `ability_score_effects.py` | 66/66 | 6/6 |
| `ability_score_generation.py` | 59/59 | 22/22 |
| `character_class.py` | 12/12 | — |
| `errors.py` | 10/10 | — |
| `high_level_ability_score_generation.py` | 53/53 | 16/16 |
| `hit_points_and_hit_dice.py` | 29/29 | 8/8 |
| `race_and_class_eligibility.py` | 32/32 | 4/4 |
| `__init__.py` | 0/0 | — |

**100% statements and 100% branches on every file.** No branch excluded, no
coverage configuration weakened, at any slice.

## 12. Verification

```text
Tests:     PASS   420 passed, 0 failed
Coverage:  PASS   src/rules/ 14 files @ 100% per file; core aggregate 100.00%
Ruff:      PASS   clean, 38 source files
mypy:      PASS   strict, clean
Overall:   PASS
```

Two real defects were caught by the gate during implementation and **fixed,
not suppressed**: `RollResult` versus `int` in `CHAR-003` (mypy, Slice C),
and a mypy enum-literal overlap in `CHAR-002` `E18` that led to a stronger
test (Slice B). One defect was caught by **human review**: the `bool` level
input in `CHAR-003`, whose ISSUE-010 justification had wrongly claimed mypy
prevented it.

## 13. Branch State

```text
branch:        cluster-002-implementation
HEAD:          Slice F commit
main:          38a25da  (unchanged; the approval / gate commit)
working tree:  clean
merged:        NO
pushed:        NO
tagged:        NO
```

Seven commits, unsquashed, in order: Slice A, Slice B, Slice C, Slice C
human-review correction, Slice-D ledger correction, Slice D, Slice E,
Slice F.

## 14. Remaining Step

**Final human review of the complete `cluster-002-implementation`
branch**, then a single `--no-ff` merge to `main`, per the approved plan
§15. On landing, `ARCHITECTURE.md` §15.2 should record `CLUSTER-002`
implementation as verified, following the `CLUSTER-001` precedent.

```text
STOP — FINAL CLUSTER REVIEW REQUIRED
```
