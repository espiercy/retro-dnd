# ISSUE-008: CLUSTER-002 Slice A — Shared Primitives and CHAR-007

## 1. Issue/Task Identifier and Objective

ISSUE-008 (completion-record ledger). Implement **Slice A** of
`docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` (`APPROVED`,
human-approved 2026-09-12, revision 3): the shared character-creation
primitives — `Ability`, `CharacterClass`, `AbilityScores` — the domain
error base Slice A requires, and the complete `CHAR-007` value contract.

No other Rule Card is implemented. `CHAR-001`, `CHAR-002` and `CHAR-003`
remain unimplemented, and no placeholder for them was created.

## 2. Approved Inputs/Specifications

- `docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` §6.1–§6.4, §7.1–§7.4,
  §8, §9.1, §14 (Slice A) — the approved implementation contract
  (`APPROVED`, human-approved 2026-09-12).
- `docs/rules/character_creation/ability_score_effects.md` (`CHAR-007`,
  Status: `APPROVED`, human-approved 2026-09-04) — the governing Rule Card
  implemented here.
- `docs/rules/character_creation/ability_score_generation.md` (`CHAR-001`),
  `race_and_class_eligibility.md` (`CHAR-002`),
  `hit_points_and_hit_dice.md` (`CHAR-003`) — all `APPROVED`; consulted
  **only** to justify each shared primitive against actual cross-card use
  (plan §6). **None of their mechanics is implemented by this issue.**
- `ARCHITECTURE.md` §15.2, "Status update (2026-09-12)" — `CLUSTER-002`
  historical-rules implementation `AUTHORIZED` 2026-09-12, scoped to the
  four-card boundary and this plan.

## 3. Files Created, Modified, or Deleted

**Created:**

- `src/rules/character_creation/__init__.py` — package marker, no exports.
- `src/rules/character_creation/errors.py`
- `src/rules/character_creation/ability.py`
- `src/rules/character_creation/character_class.py`
- `src/rules/character_creation/ability_score_effects.py`
- `tests/rules/character_creation/test_ability.py`
- `tests/rules/character_creation/test_ability_score_effects.py`
- This completion record.

**Modified:** `docs/completion-records/INDEX.md` (index row).

**Deleted:** none.

Committed on `cluster-002-implementation`. **Not merged** — under the
approved plan §15 the branch stays unmerged until Slice F, and each slice
is *reviewed and accepted* rather than merged.

## 4. Behavior Actually Implemented

### Shared primitives

- **`Ability`** — a closed six-member `enum.Enum` in RC's own declaration
  order (Strength, Intelligence, Wisdom, Dexterity, Constitution,
  Charisma), with **explicit ordinals rather than `auto()`** so the order
  is a stated fact of the module and cannot become an accident of
  declaration or alphabetical sorting. Identity only.
- **`CharacterClass`** — a closed nine-member `enum.Enum` (RC p. 7).
  **Identity only**: no prime requisites, creation minimums, Hit Dice,
  Name levels, maximum levels, fixed gains, XP or special abilities.
  `DRUID` is a member because approved cases require a result for it
  (`CHAR-002` E18/E19, `CHAR-003` H39), not in anticipation of later work.
- **`AbilityScores`** — a frozen, slotted dataclass holding exactly six
  named scores, one per `Ability`, each an integer in **3–18** (plan §6.4,
  Approach A). Structural violations (non-`int`, or a `bool` masquerading
  as one) raise `ValueError`, following `turn_credit.py`; domain
  violations raise `AbilityScoreDomainError` (plan §9.1). Operations are
  the three the plan names and no more: `__getitem__` lookup by `Ability`,
  `maximum()`, and `replace(changes)` returning a new validated instance.
  `maximum()` deliberately reports a value and resolves no tie
  (`CHAR-001` §6.2.1).

### `CHAR-007` values

- **`adjustment(score)`** — the shared Bonuses and Penalties table
  (RC p. 9), domain **2–18**, applied identically to all six abilities.
  It takes **no ability parameter**, so per-ability, per-class or per-race
  variation is not expressible.
- **`language_capability(intelligence)`** — the Intelligence and Languages
  table (RC p. 10), domain **3–18**, returning a frozen
  `LanguageCapability(literacy, additional_languages)` over a closed
  four-member `Literacy` enum.
- **`charisma_effects(charisma)`** — the Charisma Adjustment table
  (RC p. 10), domain **3–18**, returning a frozen `CharismaEffects` with
  all three of RC's columns: reaction adjustment, maximum retainers,
  retainer morale.
- **`adjusted_effects(ability)`** — the Abilities and Adjustments Table
  (RC p. 10, card §2), returning a `frozenset[AbilityEffect]` over a
  **closed eleven-member** `AbilityEffect` enum, plus
  `CONDITIONAL_EFFECTS` recording that the general-skills effect alone is
  conditional on an optional system.

### The value/procedure partition, enforced structurally

`ability_score_effects.py` returns only integers and small frozen value
objects, and **imports no consumer**. Its four public functions are all
value lookups; the module exposes no procedure. Open Doors, saving
throws, reaction resolution, retainer behaviour, initiative and the
Chapter 13 ability check are named in the module docstring's exclusion
list and exist nowhere in code.

**Slice A consumes no randomness.** No module in it imports `RNG`,
`SeededRNG`, `ScriptedRNG` or `random`.

## 5. Rules Provenance

`CHAR-007`'s entire mechanical content is **Rules Cyclopedia Explicit**
(card Provenance Classification): the three tables, the per-ability effect
assignment, and the DM-side-only constraint on the reaction adjustment.
**This card owns no Simulator Ruling and no Human-Approved Variant**, and
none was introduced. The `§4` boundaries it carries are a repository
responsibility partition, not rules content, and are implemented as
absence rather than as code.

The shared primitives are not historical game rules in their own right —
they are the cross-card vocabulary the approved implementation plan
specifies (§6), analogous to `ISSUE-003`'s `TurnCredit`.

## 6. Tests Added or Modified

**76 new tests, in two clearly separated categories.**

**Approved contract cases — 48.** `tests/rules/character_creation/`
`test_ability_score_effects.py` is the canonical owner of **`CHAR-007`
A1–A48**, each appearing exactly once, under its own case ID, in the
card's order (plan §12 ledger). No case was renumbered or reinterpreted.
`A15` tests the **scalar lookup directly** — a score of 1 or 19 is a
rejected input, not a cross-card integration concern.

**Implementation/coverage tests — 28, counted separately.** 23 in
`test_ability.py` (declared there with a contract-case count of **0**) and
5 in a clearly banner-separated section of `test_ability_score_effects.py`
covering declared input domains and module structure. **None is an
approved Rule Card case**, and both files say so in their own docstrings.

## 7. Exact Verification Commands Executed

- `uv run python scripts/verify.py`

## 8. Verification Results

- **Tests:** 236 passed, 0 failed (160 pre-existing + 76 new).
- **Coverage:** PASS — differentiated gate: `src/rules/` 10 files, 100%
  required per file, met; core aggregate 100.00% (≥95% required).
- **Ruff:** clean (29 source files).
- **mypy strict:** clean.
- **Overall: PASS.**

All four checks passed on the first run; no finding was worked around.

## 9. Coverage Results

Per new file under `src/rules/`, statements and **branches** both 100%:

| File | Statements | Branches | Missing | Partial |
|---|---|---|---|---|
| `src/rules/character_creation/ability.py` | 44/44 | 8/8 | 0 | 0 |
| `src/rules/character_creation/ability_score_effects.py` | 66/66 | 6/6 | 0 | 0 |
| `src/rules/character_creation/character_class.py` | 12/12 | — | 0 | 0 |
| `src/rules/character_creation/errors.py` | 3/3 | — | 0 | 0 |
| `src/rules/character_creation/__init__.py` | 0/0 | — | 0 | 0 |

No branch was excluded and no coverage configuration was weakened.

## 10. Deviations

**One addition to the plan's §7.4 public-API list, required by approved
cases and reported rather than assumed.**

The plan's §7.4 enumerated three public functions — `adjustment`,
`language_capability`, `charisma_effects`. Implementing `CHAR-007`'s
approved cases **A33–A41, A44, A45 and A47** additionally requires the
card's **§2 per-ability effect assignment** to be queryable, so
`AbilityEffect`, `adjusted_effects()` and `CONDITIONAL_EFFECTS` were
added.

This is **not a scope change**: §2 is inside `CHAR-007`'s approved
contract, and the plan's own §7.4 "Owned responsibility" row and its
value/procedure-partition discussion both cover it — only the API
enumeration was incomplete. Without it, nine approved cases could be
expressed only as ceremonial assertions, which the plan expressly forbids
(§12.3). **No mechanic was added, reinterpreted, or invented**; the enum
reproduces RC p. 10's table and nothing else.

**No other deviation.** `AbilityScores` Approach A, the 3–18 creation
invariant, the 2–18 scalar domain, the `ValueError`-vs-domain-error split,
the "no RNG in Slice A" rule and the Slice A error-surface restriction
were all implemented as approved.

## 11. Known Limitations/Unresolved Issues

None known, and none deferred silently.

- **`errors.py` deliberately defines only two types** —
  `CharacterCreationError` and `AbilityScoreDomainError`. The plan's §9.1
  identifies six further subclasses for Slices B–E; they are **not
  pre-stubbed**, per this task's direction. Each later slice extends the
  module when its own approved rejection paths become executable. This is
  recorded in `errors.py`'s own docstring.
- **`A31`/`A32`/`A42`/`A43`/`A46`** are implemented as assertions about
  the module's public surface and its closed effect set — that CHAR-007
  exposes exactly four value lookups and no procedure. They are
  executable and they fail if a procedure is ever added; they are not
  docstring-existence checks.
- The Chapter 13 generic Ability Check remains **`P3` — DEFER FOR HUMAN
  GOVERNANCE**; no Rule ID was assigned or invented (`A46`, `A47`).

## 12. Architectural Consequences

Establishes `src/rules/character_creation/` as a populated package for the
first time, following the domain-local shared-value precedent of
`src/rules/exploration/turn_credit.py` (plan §5.1). **No `src/domain/`,
`src/models/` or `src/core/character/` layer was created.**

**No orchestration object of any kind exists or was introduced** — no
`Player`, `Party`, `CharacterCreationEngine`, `CharacterCreator`,
`CharacterBuilder`, `GameState`, `CreationSession`, creation-phase state
machine, command object or generic `Character` aggregate (plan §4.1).

No boundary or invariant in `ARCHITECTURE.md` changed. `CLUSTER-002`
implementation remains **IN PROGRESS**; this record completes Slice A
only and marks no later slice, and no cluster, as done.
