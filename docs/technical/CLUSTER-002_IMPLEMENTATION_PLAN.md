# CLUSTER-002 — Character Foundation Implementation Plan

## 1. Status / Purpose

```text
DRAFT — AWAITING HUMAN APPROVAL
```

**This plan does not authorize implementation.**

**`ARCHITECTURE.md` §15.2 step 4 remains outstanding until the human project owner approves this plan.**

This document is a technical implementation plan. It is **not** a Rule Card, **not** a new rules authority, and **not** itself an authorization to implement. It translates the four `APPROVED` Rule Cards that make up `CLUSTER-002`'s boundary into a precise, human-reviewable plan another agent can execute **without making rules decisions**, per `ARCHITECTURE.md` §15.1/§15.2 and `docs/decisions/DEC-0005-v1-rules-inventory-and-clustered-implementation.md`.

**No production code is written by this document or the task that drafted it.** `src/` and `tests/` are untouched. This plan adds no placeholder classes and no test skeletons — it specifies what those must contain.

**Mechanics cited below are extracted, not reinterpreted.** Every mechanical statement is sourced to a specific clause of an `APPROVED` Rule Card. Where this plan proposes a *representation* — a module path, a function signature, an error type — that is called out as an **implementation-shape choice**, distinguishable from rules content. No rules question is reopened, and no ambiguity is resolved here.

**Structural precedent:** `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` (human-approved 2026-08-18). Its *lifecycle, approval block, readiness gate, slice definition, verification requirements, branch discipline, scope/non-goals and completion-evidence conventions* are followed. Its *architecture* is not copied: `CLUSTER-002`'s code design follows `CLUSTER-002`'s own approved Rule Cards.

---

## 2. Authoritative Inputs

Read in full for this plan:

- `GAME_CONSTITUTION.md`, `SOURCE_HIERARCHY.md`, `AGENTS.md`, `ARCHITECTURE.md`
- `DEVELOPMENT_WORKFLOW.md`, `TESTING_STRATEGY.md`, `CLAUDE.md`
- `docs/decisions/DEC-0005`, `DEC-0008`, `DEC-0009`, `DEC-0010`, `DEC-0011`
- `docs/rules/clusters/CLUSTER-002-character-foundation.md` (boundary `APPROVED` 2026-08-23)
- `docs/rules/clusters/CLUSTER-002-stage-b-synthesis.md` (P1–P5 dispositions)
- `docs/rules/character_creation/ability_score_generation.md` — **`CHAR-001`**, `APPROVED` 2026-09-04, **amended 2026-09-05 (R11, C1–C5)**
- `docs/rules/character_creation/race_and_class_eligibility.md` — **`CHAR-002`**, `APPROVED` 2026-09-04
- `docs/rules/character_creation/hit_points_and_hit_dice.md` — **`CHAR-003`**, `APPROVED` 2026-09-04
- `docs/rules/character_creation/ability_score_effects.md` — **`CHAR-007`**, `APPROVED` 2026-09-04
- `docs/technical/RNG_CONTRACT.md`, `docs/technical/TOOLCHAIN_AND_CI.md`
- `docs/technical/CLUSTER-001_IMPLEMENTATION_PLAN.md` (structural precedent)

**Repository state inspected.** `src/` contains exactly two packages: `src/rng/` (the `RNG` Protocol, `SeededRNG`, `ScriptedRNG`, `RollResult`, dice-expression parsing, the `DiceError` hierarchy) and `src/rules/exploration/` (`CLUSTER-001`'s three modules). **There is no character-domain code of any kind**, no `src/survivability/`, and **no `conftest.py` anywhere**. `CLUSTER-002` is the second cluster to populate `src/rules/`.

---

## 3. Binding Implementation Scope

This plan covers **exactly four Rule Cards**:

| Rule Card | Responsibility | Status |
|---|---|---|
| `CHAR-001` | Ability Score Generation | `APPROVED` 2026-09-04, amended 2026-09-05 |
| `CHAR-002` | Race & Class Eligibility | `APPROVED` 2026-09-04 |
| `CHAR-003` | Hit Points & Hit Dice | `APPROVED` 2026-09-04 |
| `CHAR-007` | General Ability Score Mechanical Effects | `APPROVED` 2026-09-04 |

**Explicitly included** — the 2026-09-05 `CHAR-001` amendment:

- **`R11`** — a 2-for-1 trade may not raise its target above **18**.
- **`C1`–`C5`** — the ceiling boundary cases.
- **`§6.2.1`** — the Chapter 13 switch's explicit source/destination parameterization, its tie handling, and its degenerate-source handling.

**Explicitly included** — `CHAR-001` §5:

```text
CHAR-001 §5 Chapter 10 above-1st-level generation methods:
    IMPLEMENT as pure rules functions
    DO NOT wire into ordinary 1st-level creation
```

H1–H5 behaviour **must** be implemented; H6's unreachability **must** be preserved as the guard that §1 remains the only 1st-level generation path.

**No other Rule Card is pulled into implementation scope.**

---

## 4. Hard Non-Goals

### 4.1 No speculative orchestration

`CHAR-001` §0 states its ordering is *"rules ordering only. It specifies no orchestration object, and none may be inferred from it."* **The approved ordering is a calling contract, not an orchestration-object mandate.**

The following **must not** be created, in whole or in part, to sequence these rules:

```text
Player                  CharacterBuilder        CreationSession
Party                   GameState               CreationPhase state machine
CharacterCreationEngine Command objects         TurnManager
CharacterCreator        generic Character aggregate
```

**Future usefulness is not sufficient justification.** If a slice appears to need one of these, that is a signal to stop and report, not to build it.

### 4.2 No out-of-boundary mechanics

Not implemented, not stubbed, not designed:

```text
Druid cleric→druid transition        (P1 — DEFER FOR HUMAN GOVERNANCE)
generic Chapter 13 Ability Check     (P3 — DEFER FOR HUMAN GOVERNANCE)
combat, attack and damage resolution                 (COMBAT-002/003)
saving-throw procedure                               (COMBAT-004)
Open Doors procedure                                 (EXP-005)
reaction resolution                                  (ENC-003)
retainer behaviour                                   (CHAR-006)
initiative                                           (COMBAT-006)
damage, death, 0-hp consequences, healing            (COMBAT-003/005/009)
general advancement, XP, Attack Ranks                (ADV-001, ADV-002)
Chapter 19 extended demihuman/Mystic progression     (NOT ENABLED, DEC-0008)
alignment, languages as a system, height/weight      (CHAR-008)
starting money                                       (CHAR-004)
survivability policy of any kind                     (ARCHITECTURE.md §10)
```

### 4.3 No infrastructure invention

No event bus, no ECS, no plugin system, no generic metadata registry, no persistence layer, no `src/state/`, no `src/events/`, no `engine/`, `application/` or `presentation/` layer. All remain correctly deferred per `ARCHITECTURE.md` §13.

---

## 5. Approved Architectural Directions (binding human decisions)

### 5.1 Shared primitive location

```text
src/rules/character_creation/
```

This follows the existing **domain-local shared-value precedent** established by `src/rules/exploration/turn_credit.py`, whose own docstring records that it is *"owned by neither Rule Card individually — it is the interface between…"*. Proposing an analogous shared module here is **reuse of an existing pattern, not a new abstraction**.

**Must not be created:** `src/domain/`, `src/models/`, `src/core/character/`.

### 5.2 `CHAR-003` advancement-boundary projection

Name-level and maximum-level values needed **solely** to bound `CHAR-003`'s own hit-point behaviour may be represented as **private, card-local constants** inside `hit_points_and_hit_dice.py`.

```text
ADV-002 remains the future authoritative owner of advancement limits.

Future ADV-002 work must replace or reconcile CHAR-003's private projection.
```

`CHAR-003` §1 says so itself: maximum levels are *"`ADV-002`'s authoritative property, consumed here because they bound how many fixed gains accrue."*

**Binding constraints:**

- **No general advancement-cap API is exported** from `CHAR-003`. The constants are module-private (leading underscore) and are not re-exported from `__init__.py`.
- **Must not create** `ClassProgression`, `AdvancementRules`, `LevelTable`, or any equivalent generalized infrastructure.
- The module docstring must carry an **explicit ownership note** recording that these values are a projection of a future `ADV-002` responsibility.
- The constants establish **nothing** about advancement outside hit points.

### 5.3 Chapter 13 switch parameterization

Per `CHAR-001` §6.2.1 (recorded 2026-09-05):

```python
apply_highest_score_switch(
    scores,
    target_class,
    source_ability,
    target_prime_requisite,
)
```

Validates:

```text
source_ability's value == max(all six scores)
target_prime_requisite is a prime requisite of target_class
source_ability != target_prime_requisite
```

**Tied maxima:** any tied maximum may be supplied by the caller. **No automatic tie-break exists.** Must not add ability-order tie-breaking, random tie-breaking, or phase state.

---

## 6. Shared Primitive Design

Three primitives are proposed. **Each is justified against actual cross-card use below; none is added for future convenience.**

### 6.1 `Ability`

```text
closed Enum, six members, RC order preserved:
    STRENGTH, INTELLIGENCE, WISDOM, DEXTERITY, CONSTITUTION, CHARISMA
```

**Justification — used by all four cards.** `CHAR-001` §1 requires generation *"in the order listed"* (G4 asserts assignment follows roll order, not sorted order), and §4 names donor and target abilities. `CHAR-002` §2 expresses every creation minimum as an ability threshold. `CHAR-003` reads Constitution. `CHAR-007` §1 applies one shared table *"identically to all six abilities"* (A14). RC's declaration order is mechanically load-bearing, so the enum must preserve it; `enum.Enum` with explicit ordinal values (not `auto()`) makes the order explicit rather than incidental.

**Owned by:** the character-creation domain, not by any single card.

### 6.2 `CharacterClass`

```text
closed Enum, nine members:
    CLERIC, FIGHTER, MAGIC_USER, THIEF, DWARF, ELF, HALFLING, MYSTIC, DRUID
```

**Justification — used by three cards.** `CHAR-001` §4 needs the chosen class to determine legal trade targets; `CHAR-002` §2 enumerates exactly these nine; `CHAR-003` §1 keys the Hit Die table on them. No card may own the enum, because each owns *different data about* the same nine classes.

**Must not** carry class mechanics. The enum is an identity, nothing more:

| Data | Owner |
|---|---|
| prime requisites, creation minimums | `race_and_class_eligibility.py` (`CHAR-002`) |
| Hit Die, Name level, maximum level, fixed gain | `hit_points_and_hit_dice.py` (`CHAR-003`) |
| XP modifiers | `ADV-001` — **not implemented** |

`DRUID` is a member because `CHAR-002` §2 must return a result for it (E18/E19) and `CHAR-003` §1 lists it with *"does not apply"* (H39). Its presence is required by approved cases, not by anticipation.

### 6.3 `AbilityScores`

```text
frozen, slotted value object holding exactly six scores, one per Ability
```

**Justification — the shared subject of every operation in the cluster.** `CHAR-001` generates and transforms a six-score array; `CHAR-002` evaluates one; `CHAR-003` reads Constitution from one; `CHAR-007` is queried per scalar. A bare `dict` would be mutable and unordered relative to RC's declaration order, and a bare tuple would lose the ability names.

### 6.4 Domain semantics — **the choice is made here, not deferred**

The two approved domains are genuinely different, and the plan must not let a constructor silently redefine either:

```text
CHAR-001 creation-produced scores:            3–18
CHAR-007 adjustment-lookup accepted domain:   2–18
```

**DECISION — Approach A is adopted.**

> **`AbilityScores` represents creation-score sets and enforces `3 ≤ n ≤ 18` per ability. `CHAR-007`'s scalar adjustment lookup independently accepts `2 ≤ n ≤ 18` on a plain `int`.**

**Why A and not B.** `CHAR-007`'s lookup is a **scalar** function — it never receives an `AbilityScores`, and `A15` supplies a bare score of 1 or 19, not a score array. The 2–18 domain is therefore a property of *that function*, not of the collection type. Under Approach B the shared value object would have to accept a `2`, which **no `CLUSTER-002` operation can ever produce** (`CHAR-001` §1 generates 3–18; the switch is a permutation; the trade's floor is 9 and its ceiling is 18) — widening the creation type beyond anything an approved card permits it to hold, purely to accommodate a scalar lookup that never takes it. Approach A maps each declared domain onto exactly the artifact whose own card declares it. `CHAR-007` §1's note that *"the band starts at 2, not 3, even though 3d6 generation cannot produce a 2 — the table accommodates scores reduced below the generated range by other effects"* is preserved exactly: the table's wider domain is real, and it lives on the table's own function.

**The safeguard that keeps this from deciding a rules question.** Because `AbilityScores` refuses a 19 structurally, an implementation could accidentally surface `C2` as a constructor failure rather than as an `R11` rejection — *"the implementation type deciding the rules question"*, which `CHAR-001` §4's own R11 note forbids.

```text
MANDATORY ORDERING, enforced by test:

    apply_trade() evaluates R1–R11 in full and raises the RULES error
    BEFORE constructing any result AbilityScores.

    The constructor's 3-18 guard is defence in depth and is UNREACHABLE
    in correct code.

    C2 and C4 assert PrimeRequisiteCeilingError -- never a constructor
    ValueError. A test that passes because the constructor raised is a
    FAILED implementation of R11.
```

The same ordering applies to `R6`/`R7` (floor 9) and `R10`, whose violations also sit inside 3–18 and so never reach the constructor at all.

**Recorded consequences of Approach A:**

| Operation | Accepts | Produces |
|---|---|---|
| `generate_ability_scores` | — | `AbilityScores` (3–18) |
| `apply_highest_score_switch` | `AbilityScores` | `AbilityScores` (a permutation; range unchanged) |
| `apply_trade` | `AbilityScores` | `AbilityScores` (donor ≥ 9 if lowered, target ≤ 18) |
| `eligible_classes` / `eligibility` | `AbilityScores` | eligibility results |
| `adjustment` (`CHAR-007`) | **`int`, 2–18** | `int` |
| `roll_*_hit_points` (`CHAR-003`) | `int` Constitution score | `int` |

---

## 7. Proposed Module / File Structure

```text
src/
    rules/
        character_creation/
            __init__.py
            ability.py
            character_class.py
            errors.py
            ability_score_effects.py
            race_and_class_eligibility.py
            hit_points_and_hit_dice.py
            ability_score_generation.py
            high_level_ability_score_generation.py
```

Module names mirror the Rule Card filenames, matching the `src/rules/exploration/` ↔ `docs/rules/exploration/` convention. Every module's docstring must cite its Rule Card and carry an explicit **"It does not, and must not:"** list, following `dungeon_turn_time_accounting.py`.

### 7.1 `ability.py`

| | |
|---|---|
| **Owned responsibility** | The six abilities and the creation-score value object |
| **Rule Card(s) served** | Shared — owned by the domain, not by one card |
| **Imports** | stdlib `enum`, `dataclasses` only |
| **Public API** | `Ability` (Enum); `AbilityScores` (frozen, slotted) with per-ability access, `maximum()`, and `replace(**changes)` returning a new instance |
| **Private** | The 3–18 constructor guard |
| **Non-goals** | No class data, no adjustments, no eligibility, no dice, no mutation |

### 7.2 `character_class.py`

| | |
|---|---|
| **Owned responsibility** | The closed set of nine class identities |
| **Rule Card(s) served** | Shared |
| **Imports** | stdlib `enum` only |
| **Public API** | `CharacterClass` (Enum) |
| **Non-goals** | **No class mechanics of any kind** — no prime requisites, no minimums, no Hit Dice, no levels, no XP |

### 7.3 `errors.py`

| | |
|---|---|
| **Owned responsibility** | The cluster's error hierarchy |
| **Rule Card(s) served** | Shared |
| **Imports** | None |
| **Public API** | `CharacterCreationError` base + five subclasses (§9) |
| **Non-goals** | No error carries rules text, remediation advice, or a suggested alternative action |

**Justification for a separate module:** five error types are raised from three different modules and asserted from four test modules. This mirrors `src/rng/errors.py`'s `DiceError` hierarchy exactly. If review prefers fewer files, the alternative is defining each error in its raising module — mechanically identical, but it would force `ability_score_generation.py` to import from `ability_score_effects.py` purely for an exception type.

### 7.4 `ability_score_effects.py` — `CHAR-007`

| | |
|---|---|
| **Owned responsibility** | Ability-score **values**: the shared adjustment table, Intelligence/language effects, Charisma's three outputs |
| **Rule Card** | `CHAR-007` (§1, §3.1, §3.2) |
| **Imports** | `errors` only. **Imports no consuming procedure, ever** |
| **Public API** | `adjustment(score: int) -> int`; `language_capability(intelligence: int) -> LanguageCapability`; `charisma_effects(charisma: int) -> CharismaEffects` |
| **Private constants** | The p. 9 band table (2–3:−3, 4–5:−2, 6–8:−1, 9–12:0, 13–15:+1, 16–17:+2, 18:+3); the p. 10 Intelligence and Charisma tables |
| **Non-goals** | Combat, saving-throw procedure, Open Doors procedure, reaction resolution, retainer behaviour, initiative, generic Ability Checks, the Chapter 19 save mapping |

**Structural preservation of the value/procedure split.** `CHAR-007` owns values; downstream cards and systems own procedures. This is enforced **structurally, not by convention**: the module returns only numbers and small frozen value objects, and it imports nothing from any consumer. `COMBAT-*`, `ENC-003`, `CHAR-006`, `EXP-005` will import *from* this module; it will never import *them*. `CHAR-007` §4.1's Open Doors fragment and §4.3's five save categories appear **only in the docstring's exclusion list**, never as code.

### 7.5 `race_and_class_eligibility.py` — `CHAR-002`

| | |
|---|---|
| **Owned responsibility** | Creation-time eligibility; the authoritative statement of prime requisites and creation minimums |
| **Rule Card** | `CHAR-002` (§2, §3, §4.1) |
| **Imports** | `ability`, `character_class` |
| **Public API** | `eligibility(scores, cls) -> Eligibility`; `eligible_classes(scores) -> frozenset[CharacterClass]`; `prime_requisites(cls) -> frozenset[Ability]`; `creation_minimums(cls) -> Mapping[Ability, int]` |
| **Private constants** | The p. 7 requirements table |
| **Non-goals** | The Druid transition (P1); Mystic downstream effects; class special abilities; XP modifiers; the trade procedure |

**Eligibility rules implemented (from §2, verbatim):**

```text
Cleric / Fighter / Magic-User / Thief   always eligible, whatever the scores
Dwarf                                   Constitution >= 9
Elf                                     Intelligence >= 9
Halfling                                Dexterity >= 9  AND  Constitution >= 9
Mystic                                  Wisdom >= 13    AND  Dexterity >= 13
Druid                                   NOT_ELIGIBLE_AT_CREATION, unconditionally
```

**Smallest result/reason API.** Druid's distinct reason (E18/E19) requires only a **closed three-value enum**:

```text
Eligibility:
    ELIGIBLE
    NOT_ELIGIBLE_ABILITY_REQUIREMENT       # a score threshold was not met
    NOT_ELIGIBLE_AT_CREATION               # Druid: not an ability question at all
```

`eligible_classes(scores)` is derived from `eligibility()` and returns a `frozenset`. **No orchestration object is introduced** — the input is a value object and the output is an enum or a frozen set. `eligible_classes` never returns the empty set (§2), so no empty-set special case exists.

**Immutable views, not exported mappings.** `prime_requisites` returns a `frozenset[Ability]`; `creation_minimums` returns an immutable mapping (`types.MappingProxyType` over a module-private dict, or a fresh `dict` — the plan requires only that a caller cannot mutate the card's tables). `CHAR-001` consumes both; the tables are defined **once**, here.

### 7.6 `hit_points_and_hit_dice.py` — `CHAR-003`

| | |
|---|---|
| **Owned responsibility** | Hit-point generation: Hit Die by class, rolled gains, the per-roll floor, fixed gains above Name level |
| **Rule Card** | `CHAR-003` (§1–§5) |
| **Imports** | `ability`, `character_class`, `ability_score_effects`, `errors`, `rng` (`RNG` Protocol) |
| **Public API** | `roll_first_level_hit_points(rng, cls, constitution) -> int`; `roll_level_gain(rng, cls, constitution) -> int`; `fixed_gain(cls) -> int`; `hit_die(cls) -> int` |
| **Private constants** | `_HIT_DIE`, `_NAME_LEVEL`, `_MAXIMUM_LEVEL`, `_FIXED_GAIN` — **card-local projection, see §5.2** |
| **Non-goals** | Damage, death, 0-hp consequences, healing, saving throws, level advancement, Attack Ranks, XP, the Chapter 19 variant |

**The `CHAR-003 → CHAR-007` dependency is made structurally real.** The public API accepts a **Constitution score**, not a caller-supplied adjustment, and calls `ability_score_effects.adjustment()` internally:

```text
hp = max(1, rng.roll_die(_HIT_DIE[cls]) + ability_score_effects.adjustment(constitution))
```

This is the stronger of the two options the drafting direction offered, and it is adopted deliberately:

| | Accept an adjustment value | **Accept a Constitution score (adopted)** |
|---|---|---|
| Can a caller inject a wrong adjustment? | Yes | **No — there is no parameter for it** |
| How is `H36` enforced? | By convention and review | **Structurally — no injection point exists** |
| Is `CHAR-007` the authoritative source? | By discipline | **By construction** |

`H36` therefore becomes a **static/API-shape conformance test**: it asserts that no adjustment-injection parameter exists on any `CHAR-003` entry point, so the card cannot produce an authoritative value without `CHAR-007`. `CHAR-003` §3's requirement that *"`con_adjustment` is re-read at each application"* is satisfied naturally, because the Constitution score is supplied per call.

**`fixed_gain` takes no Constitution parameter at all** — `CHAR-003` §5 states Constitution never applies to fixed gains, and the absence of the parameter is how that is enforced (`A40`, `H-series` fixed-gain cases).

**SR-1's Elf `+2`** is one entry in `_FIXED_GAIN`, with §4.1's reversal surface referenced in a comment so any future change is visible.

### 7.7 `ability_score_generation.py` — `CHAR-001` §1, §4, §6

| | |
|---|---|
| **Owned responsibility** | Standard generation, the discard predicate, the authorized switch, the 2-for-1 trade |
| **Rule Card** | `CHAR-001` §1, §4 (R1–R11), §6.1, §6.2, §6.2.1 |
| **Imports** | `ability`, `character_class`, `race_and_class_eligibility`, `errors`, `rng` (`RNG` Protocol) |
| **Public API** | `generate_ability_scores(rng) -> AbilityScores`; `discard_may_be_offered(scores) -> bool`; `apply_highest_score_switch(scores, target_class, source_ability, target_prime_requisite) -> AbilityScores`; `apply_trade(scores, chosen_class, donor, target) -> AbilityScores` |
| **Private constants** | None — prime requisites and minimums come from `CHAR-002` |
| **Non-goals** | Any orchestration object (§4.1); Chapter 10 methods (§7.8); starting money; alignment; XP; hit points |

**Four independent operations, no engine.** Each takes values and returns values. The canonical §0 sequence is a **documented calling contract in the module docstring**, exactly as `dungeon_wandering_monster_check.py` documents its own sequencing requirement without owning it.

**The trade enforces R1–R11**, including `R10` (class eligibility invariant, SR-5) and `R11` (target ≤ 18). It **imports** `prime_requisites` and `creation_minimums` from `CHAR-002` and **must not duplicate those tables**.

**Dependency direction, stated because it is the one place a reader may reach for a mediator.** The runtime *data* flows `CHAR-001` → `CHAR-002` (generated scores are evaluated for eligibility). The *module* dependency runs `CHAR-001` → `CHAR-002` (the trade reads the class tables). These point in opposite directions, and that is correct: `CHAR-002` takes an `AbilityScores` as a plain argument and imports nothing from `CHAR-001`, so the graph is acyclic. **No mediating object is needed or permitted.**

### 7.8 `high_level_ability_score_generation.py` — `CHAR-001` §5

| | |
|---|---|
| **Owned responsibility** | The two Chapter 10 above-1st-level generation methods |
| **Rule Card** | `CHAR-001` §5 (H1–H6) |
| **Imports** | `ability`, `errors`, `rng` (`RNG` Protocol) |
| **Public API** | `roll_and_keep_six(rng) -> tuple[int, ...]`; `assign_scores(kept, assignment) -> AbilityScores`; `point_allocation_total(rng) -> int`; `allocate_points(total, allocation) -> AbilityScores` |
| **Non-goals** | **Must not be imported by `ability_score_generation.py`**, and must not be reachable from any 1st-level flow |

**A separate module is the mechanism that preserves H6.** `ability_score_generation.py` does not import this module, so *"neither Chapter 10 method is reachable — §1 is the only generation path"* is an import-graph fact a test can assert, not a convention. This also resolves the `H` prefix collision at the module level (§11).

`allocate_points` enforces the 3–18 range per ability (**H4**) and `point_allocation_total`'s equal-allotment form enforces the 60–90 bound (**H5**). Both are the same standing range limitation that `R11` applies to the trade.

### 7.9 Dependency graph

```text
                    src/rng  (existing, unchanged)
                        │  (RNG Protocol only)
        ┌───────────────┼───────────────────────────┐
        │               │                           │
   ability.py ── character_class.py ── errors.py    │   ← shared, owned by no card
        │               │                │          │
        ├───────────────┼────────────────┤          │
        ▼               ▼                ▼          ▼
  ability_score_effects.py   race_and_class_    high_level_ability_
       (CHAR-007)             eligibility.py     score_generation.py
        │       │              (CHAR-002)          (CHAR-001 §5)
        │       │                   │
        ▼       └───────────────────┼──────────┐
  hit_points_and_hit_dice.py        │          │
       (CHAR-003)                   ▼          ▼
                            ability_score_generation.py
                                 (CHAR-001 §1/§4/§6)
```

**Acyclic.** `CHAR-007` imports nothing but the primitives. `CHAR-003 → CHAR-007`. `CHAR-001 → CHAR-002`. `CHAR-002` and `CHAR-003` do not depend on each other. `high_level_ability_score_generation.py` is a leaf on the `CHAR-001` side, imported by nothing in production.

**Forbidden dependencies, everywhere in this package:** `src/survivability/` (does not exist and must not be accepted as a parameter), any presentation/narrative module, `src/rules/exploration/`, and any concrete RNG class.

---

## 8. RNG Integration

Uses `src/rng` **exactly as it exists today**. Nothing about it is redesigned, and no approved case requires a change.

- Production rules depend on the **`RNG` Protocol** (`from rng import RNG`), **never** on `SeededRNG` or `ScriptedRNG`. `dungeon_wandering_monster_check.py` sets this precedent.
- The RNG is a **call parameter**, never constructor-injected, never module state, and **never a default argument**. The campaign/simulation owns the one shared stream (`ARCHITECTURE.md` §5).
- **No `random.Random`, no global RNG, no hidden nondeterminism, no reroll/retry logic** anywhere (`RNG_CONTRACT.md` §8).

**Exactly which operations consume RNG:**

| Operation | Call | Consumption | Approved case |
|---|---|---|---|
| `generate_ability_scores` | `rng.roll("3d6")` × 6, in `Ability` order | **18 d6 draws, 6 sequence numbers** | G1–G5 (G5 pins the count and order) |
| `roll_and_keep_six` (Ch. 10 First Method) | `rng.roll("3d6")` × 8 | **24 d6 draws** | H1, H2 (H2 pins 24, not 18) |
| `point_allocation_total` (Ch. 10 Second Method, `60 + 5d6` form) | `rng.roll("5d6")` × 1 | **5 d6 draws** | H3 |
| `point_allocation_total` (equal-allotment form) | — | **zero** | H5 |
| `roll_first_level_hit_points` | `rng.roll_die(hit_die)` × 1 | **1 draw** | H-series |
| `roll_level_gain` | `rng.roll_die(hit_die)` × 1 | **1 draw** | H-series |
| `fixed_gain` | — | **zero** | H-series fixed cases (H12 pins zero dice at levels 10–12) |
| Everything in `CHAR-002` and `CHAR-007` | — | **zero, and no `RNG` parameter exists** | E-series, A-series |
| `discard_may_be_offered`, `apply_trade`, `apply_highest_score_switch`, `assign_scores`, `allocate_points` | — | **zero, and no `RNG` parameter exists** | D, T, V, C, W, M series |

`_BaseRNG.roll` assigns **one sequence number per multi-die expression** (`RNG_CONTRACT.md` §6), which is why six separate `roll("3d6")` calls satisfy G5's *"18 d6 draws consumed, in ability order"*.

**Where a `RollResult` is returned to callers:** it is not, in this cluster. Every operation above returns a plain `int` or an `AbilityScores`. RNG auditing is performed in tests via `ScriptedRNG` with exact-length queues, which fails loudly (`RollSequenceExhaustedError`, or leftover unused values) if the draw count is wrong — the same audit technique `CLUSTER-001` used. **No operation gains a `RollResult` field merely to make auditing convenient.**

---

## 9. Validation / Error Semantics

Follows the two existing repository conventions. **No new convention is invented.**

1. **Value-object validation → `ValueError` in `__post_init__`** (`turn_credit.py`), with `bool` explicitly excluded from `int` checks.
2. **Domain errors → a base `Exception` subclass with specific subclasses**, raised eagerly and *"never silently coerced, clamped, or defaulted"* (`src/rng/errors.py`).

### 9.1 The error surface — smallest defensible set

**One base and five subclasses.** Deliberately **not** one class per deterministic case: **every raise carries the violated rule ID (`R1`, `R3`, `R6`, `R10`, `R11`, …) in its message**, so tests discriminate by rule via `pytest.raises(..., match="R3")` — the repository's existing idiom (`pytest.raises(ValueError, match="positive int")`) — without a class explosion.

```text
CharacterCreationError                     (base)
    AbilityScoreDomainError                a score outside a declared domain
    IllegalTradeError                      R1, R3, R4, R5, R6, R7 — rule ID in message
    ClassMinimumViolationError             R10 (SR-5)
    PrimeRequisiteCeilingError             R11
    IllegalSwitchError                     source/destination/degenerate — reason in message
```

**Why `R10` and `R11` get their own types rather than sharing `IllegalTradeError`.** Approved cases turn on distinguishing them from the ordinary constraints. `V2`'s expectation is explicit: *"R6's floor of 9 would have permitted it; R10 is what forbids it."* `C2`'s is explicit: *"R1, R6 and R7 all permit this trade; R11 is the only rule that forbids it."* A shared type would let a wrong-rule rejection pass those tests.

### 9.2 Classification of every invalid case

**Operation-level runtime validation** — the function can observe the violation:

| Error | Cases |
|---|---|
| `AbilityScoreDomainError` | **A15** (1 or 19 into the `CHAR-007` lookup); **H4** (allocation of 19); **H5** (allotment 59 or 91) |
| `IllegalTradeError` | **T2, T3, T14** (R6/R7 floor); **T4, T5** (R3 Con/Cha donor); **T6, M3** (R4 Dex donor); **T7, M4** (R1 target not a prime requisite) |
| `ClassMinimumViolationError` | **V2, V3, V5, V6** (second trade), **V7** (R10 / SR-5) |
| `PrimeRequisiteCeilingError` | **C2, C4** (R11) |
| `IllegalSwitchError` | source is not a maximum; destination is not a prime requisite of `target_class`; `source == destination` (§5.3) |

**Statically impossible through API shape** — no runtime branch exists, and mypy strict enforces it:

| Case | Mechanism |
|---|---|
| **S1** — trade with no selected class | `apply_trade(..., chosen_class: CharacterClass, ...)` is **non-optional**. There is no call that omits it |
| **H36** — `CHAR-003` invoked without a `CHAR-007` adjustment | No adjustment-injection parameter exists on any `CHAR-003` entry point (§7.6) |
| **H6** — neither Chapter 10 method reachable from 1st-level generation | `ability_score_generation.py` does not import `high_level_ability_score_generation.py` (§7.8) — an import-graph fact |

**Calling-contract / composition violations** — the pure function *cannot* observe them:

| Case | Why |
|---|---|
| **S2** — trade after creation completes (R9) | "Completed" is not observable from six integers and a class |
| **W7 / E23** — switch attempted after a class is chosen | The switch receives scores and a destination; it has **no phase state and cannot know when it was called** |
| **O3** — trade before eligibility is evaluated | Ordering, not operation |
| **O1, O2, O4** — sequence composition | Assertions about composing real components in the §0 order |
| **E29, E30** — the eligibility invariant across cards | Enforcement lives in `CHAR-001` (V-series); `CHAR-002` E29 says so itself |

```text
PROHIBITED: adding a `phase`, `creation_state`, or `session` argument to any
pure function merely so it can detect an ordering violation it otherwise
cannot observe. That is the speculative orchestration §4.1 forbids, arriving
through the parameter list instead of through a class.
```

---

## 10. Rule-Card Composition Check

This section exists because the ability-score ceiling defect (resolved 2026-09-05) was a **composition** failure that per-card review could not catch. It is mandatory for every inter-card dependency.

### 10.1 `CHAR-001` → `CHAR-007`

| Step | Finding |
|---|---|
| **1. Upstream produced domain** | `CHAR-001` produces ability scores in **3–18**. §1 generates 3–18; the switch is a permutation; the trade's donor floor is 9 (R6) and **its target ceiling is 18 (R11)** |
| **2. Downstream accepted domain** | `CHAR-007` `adjustment()` accepts **2–18**; outside that is a contract violation with no extrapolation (A15) |
| **3. Shared invariants** | The standing RC range limitation of 3–18 for ability scores (`CHAR-001` §1, §5, R11; RC p. 6 and p. 130) |
| **4. No unconsumable result** | **Proven.** `3–18 ⊂ 2–18`. **No `CHAR-001` operation may emit 19.** Before R11 this proof failed — that was the blocker |
| **5. Enforcement ownership** | **`CHAR-001` R11** rejects the trade. `CHAR-007` A15 remains an independent input-domain guard, not the primary defence |

**Required integration test (non-contract, added for coverage of the composition itself):** no sequence of legal `CHAR-001` operations produces a score outside `CHAR-007`'s accepted domain.

### 10.2 `CHAR-001` ↔ `CHAR-002`

| Step | Finding |
|---|---|
| **1. Upstream produced** | `CHAR-001` §1/§6.2 produce **eligibility scores** (after any authorized switch). §4 produces **adjusted scores** (after the trade) |
| **2. Downstream accepted** | `CHAR-002` accepts a six-score array and returns eligibility. It consumes **eligibility scores**, never adjusted scores (`CHAR-001` §3, §0 step 4) |
| **3. Shared invariants** | Prime requisites and creation minimums, defined **once** in `CHAR-002` and imported by `CHAR-001` |
| **4. No unconsumable result** | **Proven, in both directions.** The switch runs **before** eligibility and **can** establish a minimum (W1, E25). The trade runs **after** class selection and **cannot establish** eligibility (O1, §3) — it may raise only a prime requisite (R1) and may not touch Constitution at all (R3). It **cannot destroy** the selected class's eligibility (R10). Both asymmetries are approved and both are testable |
| **5. Enforcement ownership** | Ordering: the **caller** (§0, a calling contract). R10: **`CHAR-001`**, consuming `CHAR-002`'s minimums. Eligibility itself: **`CHAR-002`** |

**Runtime data flow versus module dependency — stated so no mediator is invented:**

```text
RUNTIME DATA FLOW      CHAR-001 generates scores  ──→  CHAR-002 evaluates them
MODULE DEPENDENCY      CHAR-001 imports CHAR-002's prime requisites / minimums

These point in OPPOSITE directions, and the graph is still acyclic, because
CHAR-002 takes an AbilityScores as a plain argument and imports nothing from
CHAR-001.

NO mediating object, engine, or coordinator is required or permitted.
```

### 10.3 `CHAR-003` → `CHAR-007`

| Step | Finding |
|---|---|
| **1. Upstream produced** | `CHAR-007` `adjustment(constitution)` produces an integer in **−3 … +3** |
| **2. Downstream accepted** | `CHAR-003` §2/§3 consume it inside `max(1, roll + con_adjustment)` |
| **3. Shared invariants** | The adjustment is **read per application** (`CHAR-003` §3); the 1-hp floor applies **per roll**, never to a total (§5); Constitution **never** applies to fixed gains (§4, §5) |
| **4. No unconsumable result** | **Proven.** Every value the table can return is consumable; the `max(1, …)` floor absorbs the −3 case (H-series) |
| **5. Enforcement ownership** | **Structural.** `CHAR-003` accepts a Constitution *score* and calls `CHAR-007` internally (§7.6). **The adjustment is never recomputed independently and cannot be injected** — H36 has no injection point to test against |

### 10.4 Composition checks that found nothing

`CHAR-002` ↔ `CHAR-003`: no dependency. `CHAR-003` H39 (*"Druid requested at 1st level → rejected, no Druid Hit Die"*) references `CHAR-002`'s conclusion but `CHAR-003` §1 states Druid's Hit Die as *"does not apply"* on its own authority. **No import is created between them.**

`CHAR-002` ↔ `CHAR-007`: **none, deliberately.** `CHAR-002` §4.1 states it explicitly — R10 reads **raw-score minimums**, not adjustment values, and *"no `CHAR-002` → `CHAR-007` dependency is created."*

---

## 11. Test Module Layout

Follows existing repository conventions exactly. **No fixtures, no framework, no `conftest.py`** — none exists in this repository and none is required. Plain pytest functions with `-> None` annotations, `# --- section ---` comment banners, `pytest.raises(..., match=...)`, `dataclasses.FrozenInstanceError` for immutability, `# type: ignore[arg-type]` for deliberate type violations, and `ScriptedRNG([...])` constructed inline.

```text
tests/
    rules/
        character_creation/
            test_ability.py
            test_ability_score_effects.py
            test_race_and_class_eligibility.py
            test_hit_points_and_hit_dice.py
            test_ability_score_generation.py
            test_high_level_ability_score_generation.py
            test_cluster_002_integration.py
```

**The `H` prefix collision is resolved by module separation.** `CHAR-001` `H1`–`H6` (Chapter 10 generation) live **only** in `test_high_level_ability_score_generation.py`; `CHAR-003` `H1`–`H42` (hit points) live **only** in `test_hit_points_and_hit_dice.py`. Each test function name must additionally qualify its card (e.g. `test_char001_h2_first_method_consumes_24_draws`, `test_char003_h20_dwarf_at_level_12_no_further_gains`) so the two runs can never be confused in a failure report.

---

## 12. Exact 189-Case Ownership Ledger

**Every approved case ID appears exactly once. No omissions. No duplicates. Integration placement does not create a second contract case.**

| Test module | Owned case IDs | Count |
|---|---|---|
| `test_ability.py` | *(none — primitive validation is an implementation test, counted separately)* | **0** |
| `test_ability_score_effects.py` | A1–A48 | **48** |
| `test_race_and_class_eligibility.py` | E1–E22, E24–E28 | **27** |
| `test_hit_points_and_hit_dice.py` | H1–H35, H37–H42 *(`CHAR-003`)* | **41** |
| `test_ability_score_generation.py` | G1–G5, T1–T14, S3, M1–M5, V1–V12, W1–W6, D1–D8, **C1–C5** | **56** |
| `test_high_level_ability_score_generation.py` | H1–H6 *(`CHAR-001` §5)* | **6** |
| `test_cluster_002_integration.py` | E23, E29, E30, H36 *(`CHAR-003`)*, S1, S2, W7, O1, O2, O3, O4 | **11** |
| | **TOTAL** | **189** |

### 12.1 Reconciliation against the approved cards

```text
CHAR-001   G5 + T14 + S3 + H6 + M5 + V12 + W7 + O4 + D8 + C5   =  69
              56 unit + 6 high-level + 7 integration (S1,S2,W7,O1-O4)  =  69   OK

CHAR-002   E1-E30                                              =  30
              27 unit + 3 integration (E23,E29,E30)            =  30   OK

CHAR-003   H1-H42                                              =  42
              41 unit + 1 integration (H36)                    =  42   OK

CHAR-007   A1-A48                                              =  48
              48 unit + 0 integration                          =  48   OK
                                                                  ----
                                                                   189
```

### 12.2 Test-kind classification for the non-obvious cases

| Case | Kind | Note |
|---|---|---|
| **A15** | **Executable unit test** | Placed in `test_ability_score_effects.py`, **not** in integration. It is a scalar domain check on `adjustment()` that needs no other card to execute. The *cross-card* claim — that `CHAR-001` can never emit 19 — is a **separate non-contract integration test** (§10.1), counted separately. Recorded because the drafting direction listed A15 as a permitted integration candidate; this placement is the narrower, more accurate one |
| **S1** | **Static / API-shape conformance** | `chosen_class` is non-optional; the test asserts the call does not type-check, using `# type: ignore[call-arg]` and mypy strict as the enforcement |
| **S2** | **Calling-contract conformance** | R9's time-boxing is a caller obligation; asserted as a documented sequence in integration, not as a branch inside `apply_trade` |
| **W7, E23** | **Calling-contract conformance** | The switch has no phase state (§9.2) |
| **O1–O4** | **Cross-card integration** | Composition of real components in the §0 order |
| **E29, E30** | **Cross-card integration** | Enforcement lives in `CHAR-001` V-series; these assert the invariant holds from `CHAR-002`'s side |
| **H36** (`CHAR-003`) | **Static / API-shape conformance** | Asserts no adjustment-injection parameter exists (§7.6) |
| **H6** (`CHAR-001`) | **Static / import-graph conformance** | Asserts `ability_score_generation` does not import `high_level_ability_score_generation` |
| **C2, C4** | **Executable unit test, with an ordering assertion** | Must assert `PrimeRequisiteCeilingError`, **never** a constructor `ValueError` (§6.4) |

**No orchestration state is added anywhere to turn an ordering requirement into a runtime branch.**

---

## 13. Coverage and Verification

Per `TESTING_STRATEGY.md` §8 and `scripts/check_coverage.py`:

```text
Every new production file beneath src/rules/  ->  100% BRANCH coverage, per file
Aggregate core coverage                       ->  >= 95%
```

All eight proposed production modules land under `src/rules/`, so **all eight require 100% branch coverage individually.** This is achievable because every module is a pure function over a small closed domain; each error branch identified in §9 has a named approved case or a documented implementation test.

**After every slice, without exception:**

```powershell
uv run python scripts/verify.py
```

must report:

```text
Tests:     PASS
Coverage:  PASS
Ruff:      PASS
mypy:      PASS
Overall:   PASS
```

preserving pytest, coverage, Ruff (line-length 100; `E,F,I,UP,B,SIM`) and **mypy strict** over `src`, `tests` and `scripts`.

```text
NO SLICE MAY LAND RED.
```

A slice whose tests fail, whose coverage falls short, or whose types do not check is **not complete** and must not be merged (`DEVELOPMENT_WORKFLOW.md` §5.1).

---

## 14. Implementation Slices

Derived from the dependency graph in §7.9. Each slice is independently reviewable and leaves the tree green.

### Slice A — shared primitives + `CHAR-007`

| | |
|---|---|
| **Production files** | `src/rules/character_creation/__init__.py`, `ability.py`, `character_class.py`, `errors.py`, `ability_score_effects.py` |
| **Test files** | `tests/rules/character_creation/test_ability.py`, `test_ability_score_effects.py` |
| **Cases covered** | `CHAR-007` **A1–A48** (48) |
| **Dependencies** | None |
| **Non-goals** | Every consuming procedure; the Open Doors / save / initiative / Ability-Check material stays in the docstring exclusion list |
| **Verification** | `verify.py` — 100% branch on all four new `src/rules/` files |
| **Commit boundary** | One commit; completion record required (§16) |
| **Human review** | Reviewed and merged before Slice B begins |

**Why first:** zero dependencies, needed by every other slice, entirely deterministic (no RNG), and small enough that the 100%-branch gate on a brand-new domain package is trivially provable. It also front-loads the `AbilityScores` domain decision (§6.4) — the cheapest possible point to correct it if review disagrees.

### Slice B — `CHAR-002` eligibility

| | |
|---|---|
| **Production files** | `race_and_class_eligibility.py` |
| **Test files** | `test_race_and_class_eligibility.py` |
| **Cases covered** | **E1–E22, E24–E28** (27). E23, E29, E30 deferred to Slice F |
| **Dependencies** | Slice A primitives |
| **Non-goals** | Druid transition (P1); Mystic downstream effects; class special abilities; XP |
| **Verification** | `verify.py` — 100% branch |
| **Commit boundary** | One commit; completion record required |

### Slice C — `CHAR-003` hit points

| | |
|---|---|
| **Production files** | `hit_points_and_hit_dice.py` |
| **Test files** | `test_hit_points_and_hit_dice.py` |
| **Cases covered** | **H1–H35, H37–H42** (41). H36 deferred to Slice F |
| **Dependencies** | Slice A (`CHAR-007` adjustment — the load-bearing dependency); `src/rng` |
| **Non-goals** | Damage, death, healing, saves, advancement, Attack Ranks, Chapter 19 |
| **Verification** | `verify.py` — 100% branch; `ScriptedRNG` exact-length queues audit every draw count |
| **Commit boundary** | One commit; completion record required |

### Slice D — `CHAR-001` generation, discard, switch, trade

| | |
|---|---|
| **Production files** | `ability_score_generation.py` |
| **Test files** | `test_ability_score_generation.py` |
| **Cases covered** | **G1–G5, T1–T14, S3, M1–M5, V1–V12, W1–W6, D1–D8, C1–C5** (56) |
| **Dependencies** | Slices A and B; `src/rng` |
| **Non-goals** | Chapter 10 methods (Slice E); **no orchestration object of any kind** |
| **Verification** | `verify.py` — 100% branch; C2/C4 must assert `PrimeRequisiteCeilingError`, not a constructor error |
| **Commit boundary** | One commit; completion record required |

**Largest slice at 56 cases.** It is kept whole because R1–R11 form one contract that is easier to review together than split across two commits. If review prefers a smaller batch, the natural seam is `§1 generation + §6.1 discard` (18 cases) before `§4 trade + §6.2 switch` (38 cases); this plan does not adopt that split by default.

### Slice E — `CHAR-001` §5 Chapter 10 pure methods

| | |
|---|---|
| **Production files** | `high_level_ability_score_generation.py` |
| **Test files** | `test_high_level_ability_score_generation.py` |
| **Cases covered** | **H1–H6** (6) |
| **Dependencies** | Slice A; `src/rng` |
| **Non-goals** | **Must not be imported by `ability_score_generation.py`**; must not be reachable from any 1st-level flow |
| **Verification** | `verify.py` — 100% branch; H6 asserted as an import-graph fact |
| **Commit boundary** | One commit; completion record required |

**Kept separate from Slice D deliberately.** Combining them would put the module whose entire purpose is *to be unreachable from ordinary generation* in the same commit as ordinary generation, which is precisely the review a separate commit makes easy.

### Slice F — cross-card integration

| | |
|---|---|
| **Production files** | **None** |
| **Test files** | `test_cluster_002_integration.py` |
| **Cases covered** | **E23, E29, E30, H36, S1, S2, W7, O1–O4** (11), plus the non-contract composition tests from §10.1 |
| **Dependencies** | Slices A–E |
| **Non-goals** | **No production orchestration module** — following `CLUSTER-001`'s resolved precedent, cross-card sequencing is demonstrated by tests composing the real modules, not by a production wrapper |
| **Verification** | `verify.py` — full `Overall: PASS` for the completed cluster |
| **Commit boundary** | One commit; **cluster completion record** required, supplementing the per-slice records |

```text
Slice A ──→ Slice B ──┐
   │                  ├──→ Slice D ──┐
   ├──→ Slice C ──────┤              ├──→ Slice F
   └──→ Slice E ──────┴──────────────┘
```

---

## 15. Implementation Branch / Landing Strategy

Follows the repository's existing workflow (`DEVELOPMENT_WORKFLOW.md`; the `CLUSTER-001` precedent).

```text
Implementation branch:   cluster-002-implementation
```

**Not created by this task.**

- Each slice is **one commit** on that branch, reviewed independently.
- Every slice that changes behaviour under `src/` requires its **own completion record** before it is considered complete (`DEVELOPMENT_WORKFLOW.md` §3–§5). `CLUSTER-001`'s plan §14 records this explicitly as a correction learned there; `CLUSTER-002` adopts it from the start. Next available IDs are `ISSUE-008` onward.
- `uv run python scripts/verify.py` must report `Overall: PASS` **before** each commit.
- Final integration reaches `main` by **`--no-ff` merge** of `cluster-002-implementation`, matching `a7fc9e8` and `da3257d`.
- **Meaningful implementation history is not squashed away.** The per-slice commits are the review record.

**Proposed completion records:**

| Slice | Record |
|---|---|
| A | `ISSUE-008-cluster-002-shared-primitives-and-char-007.md` |
| B | `ISSUE-009-char-002-race-and-class-eligibility.md` |
| C | `ISSUE-010-char-003-hit-points-and-hit-dice.md` |
| D | `ISSUE-011-char-001-ability-score-generation.md` |
| E | `ISSUE-012-char-001-high-level-generation-methods.md` |
| F | `ISSUE-013-cluster-002-cross-card-integration.md` |
| Cluster | `ISSUE-014-cluster-002-character-foundation.md` |

---

## 16. Deferred Items — must stay deferred

**No implementation slice may resolve any of these.**

| Item | Disposition | Consequence for implementation |
|---|---|---|
| **P1** — Druid transition ownership | **DEFER FOR HUMAN GOVERNANCE** | `CHAR-002` §2 returns `NOT_ELIGIBLE_AT_CREATION` for Druid **unconditionally**. Nothing in this cluster evaluates a transition; the 9th-level-cleric path is unreachable from creation code. **No Rule ID may be assigned** |
| **P3** — Chapter 13 generic Ability Check Rule ID | **DEFER FOR HUMAN GOVERNANCE** | `CHAR-007` §4.4 places the check outside its scope; A46/A47 assert it is *rejected*. Implementing the rejection requires no ID. **No ID may be invented** |
| **`CHAR-003` W2** — 1-hp floor vs fixed gains | **MOOT** | Every fixed gain in `CHAR-003` §4 is positive, so the floor is unreachable on that path. Moot in code as it is on paper |
| **`CHAR-003` W3** — Ch. 10 Step 6 alternative vs restatement | **NOT V1-WIRED** | `CHAR-003` §7 is explicitly not wired to any V1 flow and **is not implemented by this plan** (contrast `CHAR-001` §5, which human direction *did* place in scope) |

**None of the four blocks any slice.**

---

## 17. Rule-Card Clarification Requirements

**None.** After the 2026-09-05 `CHAR-001` amendment, all four cards are sufficiently precise for every mechanical question this plan needed to answer.

The one composition defect that previously existed between them — `CHAR-001` §4 admitting a target of 19 while `CHAR-007` A15 rejects it — is closed by `R11`, and §10.1 records the proof. The switch tie-break question is closed by `CHAR-001` §6.2.1's determination that **no tie-break rule is required**; the caller supplies the source.

---

## 18. Risks / Remaining Human Decisions

### 18.1 Ordinary design choices — resolved here, not escalated

| Choice | Resolution | Basis |
|---|---|---|
| `AbilityScores` domain | **Approach A** (§6.4) | Each declared domain lives on the artifact whose card declares it |
| `CHAR-003` dependency shape | **Constitution score in, adjustment derived internally** (§7.6) | Makes H36 structural rather than conventional |
| Error surface size | **Base + 5, rule ID in the message** (§9.1) | Repository idiom; avoids a class per case while keeping R10/R11 distinguishable |
| Chapter 10 module separation | **Own module** (§7.8) | Makes H6 an import-graph fact and resolves the `H` collision |
| Slice D kept whole | **Yes**, with a named alternative seam (§14) | R1–R11 review better together |
| Test-case placement | **§12 ledger** | 1:1 ownership, reconciled to 189 |

### 18.2 Genuine risks, with safeguards

| Risk | Safeguard |
|---|---|
| **`C2` passes for the wrong reason** — the `AbilityScores` constructor raises before R11 is evaluated | §6.4's mandatory ordering; C2/C4 must assert `PrimeRequisiteCeilingError` specifically. A test that passes on a constructor `ValueError` is a **failed** implementation of R11 |
| **An orchestration object is introduced to satisfy an ordering case** | §9.2's prohibition; S1/S2/W7/E23/O1–O4 are classified as static or calling-contract cases **before** implementation begins, so no implementer has to decide |
| **`CHAR-003`'s private level constants leak into a general API** | §5.2's constraints: module-private names, not re-exported, with a mandatory ownership note naming `ADV-002` |
| **The value/procedure split erodes in `CHAR-007`** | §7.4: the module imports no consumer, and returns only numbers and small frozen values. Enforced by the import graph, not by review discipline |
| **A future reader treats R11 as RC-explicit** | `CHAR-001`'s provenance table classifies it as a Necessary Mechanical Consequence and preserves the rejected reading; this plan does not restate it as anything stronger |

### 18.3 Decisions requiring the human project owner

**One, and it is this document.**

```text
Approve or reject this implementation plan.
```

No rules question, no unresolved ambiguity, and no architecture decision remains open. Every other choice above is an ordinary design decision resolved from existing repository conventions and recorded so it can be reviewed rather than rediscovered.

---

## 19. Gate State

```text
ARCHITECTURE.md §15.1 cluster readiness (five criteria):   PASS
    1. behavioural scope clearly defined                   PASS  (§3)
    2. all required historical rules identified            PASS  (four APPROVED cards)
    3. all required Rule Cards APPROVED                    PASS  (2026-09-04; CHAR-001 amended 2026-09-05)
    4. external dependencies have stable approved contracts PASS  (src/rng, DEC-0002)
    5. no unresolved ambiguity for the agent to adjudicate PASS  (§17)

ARCHITECTURE.md §15.2 Rules Baseline Migration Gate:
    step 1 — V1 rules inventory approved                   PASS  (2026-08-16)
    step 2 — cluster boundary approved                     PASS  (2026-08-23)
    step 3 — all required Rule Cards approved              PASS  (2026-09-04)
    step 4 — implementation readiness (re-)approved        AWAITING HUMAN APPROVAL OF THIS PLAN

ARCHITECTURE.md §16 project-wide Pre-Code Development Gate: CLEARED (2026-08-15)
    -- necessary but not sufficient for this cluster

CLUSTER-002 IMPLEMENTATION:                                NOT AUTHORIZED
```

**Step 4 is not marked PASS by this document, and must not be marked PASS by the agent that drafted it.** Only the human project owner's approval of this plan satisfies it — and, per the `CLUSTER-001` precedent, `ARCHITECTURE.md` §15.2's status text must then be synchronized in the same task that records the approval.

---

## 20. Implementation-Readiness Assessment

- All five `DEC-0005` / `ARCHITECTURE.md` §15.1 cluster-readiness criteria are met (§19).
- `ARCHITECTURE.md` §15.2 steps 1–3 are satisfied; **step 4 is exactly what this plan is submitted for**.
- No Rule Card clarification is required (§17). No architecture decision point is open (§18).
- No production code, test skeleton, or placeholder class has been created by the task that drafted this plan.

```text
STOP — HUMAN PLAN APPROVAL REQUIRED
```

**This plan does not authorize implementation.** `CLUSTER-002` implementation begins only after the human project owner approves this document and `ARCHITECTURE.md` §15.2 is synchronized to record `CLUSTER-002` implementation readiness as re-approved.

## 21. Human Implementation-Plan Review

```text
Status:       AWAITING HUMAN APPROVAL
Reviewed by:  —
Date:         —
Outcome:      —
```

*(To be completed by the human project owner. This block must not be filled in by an agent.)*
