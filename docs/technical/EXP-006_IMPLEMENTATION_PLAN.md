# `EXP-006` — Implementation Plan

## 1. Status / Purpose

```text
STATUS:     APPROVED -- human project owner, 2026-10-01
CARD:       EXP-006 Light & Exploration Resources, APPROVED 2026-10-01
GATE:       EXP-006 PRE-CODE GATE: PASS, 2026-10-01
SCOPE:      SINGLE-CARD slice.  ENC-005 is Stage-B DEFERRED and is NOT in this plan.
AUTHORIZES: nothing.  This document is a plan; implementation remains a separate human act
            under ARCHITECTURE.md §15.2 step 4.
```

`EXP-006` is planned as a single-card slice on the Pre-Code Gate's finding that **its only
consumed dependencies are landed and implemented** (`EXP-002`, `CHAR-004`), and that every
unresearched dependency is a **downstream consumer** that need not exist for `EXP-006` to be
implemented.

**No new Rules Cyclopedia research was performed for this plan, and the approved Rule Card is not
reinterpreted anywhere in it.**

### 1.1 Human implementation-plan review — `APPROVED` 2026-10-01

Approved subject to two architectural adjudications, both of which **confirm** the plan's
recommendation and close the two items §17 flagged for judgement:

> **`CHAR-004` identity access.** `CHAR-004` is **not** to be modified to export `Lantern`, `Oil`
> or `Tinder box` constants. `TORCH`'s export rationale is its cross-catalog ambiguity and does
> not generalize. Use `catalog_item(...)`, with the canonical names centralized in **one** private
> `EXP-006` location. **No landed `CHAR-004` production code changes in this slice.** §9.2's
> flagged candidate amendment is therefore **declined**, and the plan's handling stands as written.

> **`EXP-002` elapsed-turn input.** Do **not** import `turn_credit.py` or `TurnCredit`. `EXP-006`
> consumes `elapsed_turns: int` from its caller, documented as authoritative. **`EXP-006` owns the
> numeric domain, not provenance** — integer required, `bool` rejected, negative rejected. **No
> fake provenance wrapper** whose type cannot actually prove origin. The orchestration question
> (§8.2) is a frontier concern and is **not** solved in this slice.

**Error-hierarchy constraint added by the same review:** a domain-local refusal type may be
introduced **only if a slice actually requires it**. No exploration-wide exception framework is to
be built, and nothing is generalized for hypothetical future cards. **Consequence for Slice A:**
see §14 Slice A — it requires none, and introduces none.

### 1.2 Implementation authorization

```text
SLICE A   ACCEPTED   2026-10-01   -- light-source value/state model
SLICE B   ACCEPTED   2026-10-01   -- depletion + mundane-light contribution
SLICE C   ACCEPTED   2026-10-01   -- ignition branch/outcome model, carrying SR-11
SLICE D   ACCEPTED   2026-10-03   -- CHAR-004 identity binding + final guards

IMPLEMENTATION  CODE COMPLETE; NOT FINALLY ACCEPTED.
EXP-006-PHASE: REVIEW-4-REMEDIATED

                Every independent final review returned FAIL and is
                preserved unaltered.  NONE found a rules-conformance
                defect.  The review history is the persisted artifact set
                itself -- docs/technical/EXP-006_FINAL_IMPLEMENTATION_
                REVIEW*.md, each paired with its own remediation ledger --
                and is NOT restated as a count here, because every prose
                count of it has so far gone stale (review-#4 B-4).

                LOW-3 and LOW-8 are RESOLVED (applied at a150837).

                See ISSUE-022 for the authoritative current status.
```

**Slice B's accepted semantics** include `expended lantern + new flask → remaining_turns = 24,
lit = False, no illumination until separately ignited`, and `partial refill → REFUSE, with no
top-up or additive arithmetic`.

## 2. Authoritative inputs

| Input | Role |
|---|---|
| `docs/rules/exploration/light_and_exploration_resources.md` (`APPROVED`) | The sole rules authority. Every behavior below cites a §/case |
| `docs/technical/EXP-006_PRE_CODE_GATE.md` (`PASS`) | Readiness findings and three cautions this plan absorbs |
| `docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` | Structural precedent; the AST-guard lesson |
| `src/rules/character_creation/equipment.py` (`CHAR-004`, landed) | Item identity |
| `src/rules/exploration/dungeon_turn_time_accounting.py`, `turn_credit.py` (`EXP-002`, landed) | Elapsed-turn authority |
| `ARCHITECTURE.md`, `TESTING_STRATEGY.md`, `DEVELOPMENT_WORKFLOW.md` | Conventions |

## 3. Binding implementation scope

Exactly the thirteen approved mechanics, and nothing else:

```text
mundane light-source state                 §2, §6
torch 30' contribution                     §2         L1, L3
lantern 30' contribution                   §2         L2
torch six-turn duration                    §3         L6
lantern 24-turn-per-flask duration         §3         L7
depletion using EXP-002 elapsed turns      §4         L8, L10, L11
exhausted source ceases contributing       §4         L9, L12, L15a
oil as lantern fuel, as approved           §3, §4     L7, L12
tinderbox ordinary-condition ignition      §5         L17, L18, L19
Fire-Building branch selection             §5         L20, L21
routed skill-check request (adverse)       §5         L22
deterministic refusal of undefined paths   §5         L23, L24
mundane-light contribution output          §6         L27, L28, L34
```

## 4. Hard non-goals — **no placeholder implementation for any of these**

```text
global/world darkness          encounter Visibility        encounter distance
surprise                       blindness determination     blindness penalties
infravision possession         magical light/darkness      CHAR-012 skill resolution
dungeon-time advancement       equipment pricing           equipment encumbrance
equipment legality             rations                     starvation causation
torch weapon behavior          oil missile behavior        pursuit-delay mechanics
```

Not stubbed, not `NotImplementedError`, not a parameter reserved "for later". **Absent.** §13's
guard strategy makes several of these mechanically checkable rather than merely asserted.

## 5. Architecture placement

| Question | Recommendation |
|---|---|
| **Module path** | **`src/rules/exploration/light_and_exploration_resources.py`** — one new module |
| **Extend an existing module instead?** | **No.** `dungeon_movement.py` (`EXP-003`) and `dungeon_turn_time_accounting.py` (`EXP-002`) are single-card modules; the package convention is **one module per Rule Card, named after the card's document**. Extending either would couple two cards' lifecycles and blur the §4 non-goals |
| **Type placement** | All public types in that one module. **No new package, no `types.py`, no shared abstraction** |
| **Import direction** | `exploration.light_and_exploration_resources` → `character_creation.equipment` (identity only). **Nothing imports it** in this slice: its consumers are unresearched |
| **New error module** | **`src/rules/exploration/errors.py`** — see §10 |

**Deliberately not created:** no illumination interface/protocol, no light-source registry, no
"environment" or "world state" type, no plugin seam for magical light. `ENC-001`, `COMBAT-*` and
`MAGIC-*` are unresearched; an abstraction shaped for them now would be speculation, and the
approved card's §B forbids the behavior such an abstraction would exist to host.

## 6. State model — recommendation

### 6.1 The gate's open modelling question, answered

> Does exhaustion set `lit = false`, or can `lit` remain historical state while illumination
> contribution also requires `remaining_turns > 0`?

**Recommendation: exhaustion sets `lit = False`, *and* the pair `(lit=True, remaining_turns=0)` is
rejected by a construction invariant.** The two halves together are what make this safe — the
first makes the transition explicit, the second makes the bad state **unconstructible by anyone**,
including a future caller this plan cannot see.

```python
@dataclass(frozen=True, slots=True)
class LightSource:
    kind: LightSourceKind
    remaining_turns: int
    lit: bool

    def __post_init__(self) -> None:
        # structural: ValueError, per the exploration convention (§10)
        # INVARIANT: an exhausted source is never lit.
        if self.lit and self.remaining_turns == 0:
            raise ValueError(...)
```

**Why this representation over the alternatives:**

| Criterion | Finding |
|---|---|
| **Impossible-state reduction** | The one state the approved card forbids — an exhausted source contributing light — **cannot be constructed**. This is the strongest available form of §6's requirement, which accepts "impossible **or** explicitly rejected"; this is both |
| **Clarity** | `lit` answers "is it burning?", `remaining_turns` answers "for how much longer?". Neither silently encodes the other |
| **Type/API simplicity** | One frozen value object, two fields plus a kind. No wrapper, no result union for state |
| **Testability** | `L15a` (two torches, one expires) and `L9` are direct constructions; the invariant itself is a one-line `pytest.raises` |
| **Repository consistency** | Matches `TurnCredit` and `MovementRate` exactly: frozen, slotted, `__post_init__` validation, `bool`-excluded ints |

**Why an unlit source must remain representable** (and so why the simpler "a `LightSource` is
always lit" model is rejected): approved case **`L11`** — *"**Unlit** torch, `3` elapsed turns →
`6` remaining — unlit sources do not deplete"* — requires an unlit source that **carries duration
state**. A model that only represented lit sources could not express `L11` at all.

**`bool` exclusion.** `remaining_turns` rejects `bool` explicitly, following
`turn_credit.py`/`rng.py`/`equipment.py`: `bool` is a subtype of `int`, so static typing permits
`True` and it would read as `1`.

### 6.2 Kinds

```python
class LightSourceKind(Enum):
    TORCH = auto()
    LANTERN = auto()
```

Closed, two-valued. **No `MAGICAL` member, no `OTHER`, no extension point** — §B excludes magical
light, and `L41` guards it.

## 7. Public API

```python
__all__ = [
    "LANTERN_TURNS_PER_FLASK",       # 24
    "MUNDANE_LIGHT_RADIUS_FEET",     # 30   -- one constant; RC states no torch/lantern difference
    "TORCH_TURNS",                   # 6
    "IgnitionConditions",
    "IgnitionOutcome",
    "LightSource",
    "LightSourceKind",
    "MundaneLightContribution",
    "deplete",
    "ignition_outcome",
    "mundane_light_contribution",
    "refuel_lantern",
]
```

### 7.1 The contribution contract — naming is the safety mechanism

```python
@dataclass(frozen=True, slots=True)
class MundaneLightContribution:
    """What EXP-006's OWN sources contribute. NOT a statement about the world."""
    lit_sources: tuple[LightSource, ...]
    any_mundane_source_lit: bool
    max_mundane_radius_feet: int | None
```

Every name carries the word **`mundane`** or **`source`**. A consumer cannot write
`if not contribution.any_mundane_source_lit: → darkness` without the identifier itself
contradicting them. The type name is `MundaneLightContribution`, **not** `LightState`,
`Illumination`, `Visibility` or `WorldLight` — each of which would invite exactly the
misreading the card's Finding B withdrew.

`max_mundane_radius_feet` is `None` — **not `0`** — when nothing is lit. `0` reads as "a radius of
zero", which is a claim about illumination; `None` reads as "this card contributes no radius",
which is the truth.

**A single radius constant.** `MUNDANE_LIGHT_RADIUS_FEET = 30` serves both kinds. Two constants
would permit them to drift, and `L4`/`L5` exist precisely to forbid a torch/lantern distinction
RC does not state.

## 8. `EXP-002` integration

### 8.1 Recommended: consume a plain whole-turn count

```python
def deplete(sources: Iterable[LightSource], elapsed_turns: int) -> tuple[LightSource, ...]
```

`EXP-006` holds no `DungeonTimeAccounting`, calls no `complete_ordinary_turn()`, and
**imports nothing from `turn_credit.py` or `dungeon_turn_time_accounting.py`**.

### 8.2 Why not `TurnCredit` — an architectural finding

`turn_credit.py`'s own module docstring states:

> *"No production module beyond EXP-002 and EXP-001 needs to import this module."*

That is a deliberate scoping of a **two-party interface**, and `EXP-006` is not a party to it.
Three further reasons agree:

1. **`EXP-006` needs the count, not the identity.** A turn is a turn for burning; `turn_number`
   and `origin` are meaningless here.
2. **`origin` is a trap.** `ORDINARY` vs `ENCOUNTER_DERIVED` is `EXP-001`'s discriminator. A
   module holding `TurnCredit` would be one line away from branching on something that is not its
   business.
3. **Import-graph provability.** Taking an `int` lets `L13`/`L14` be proven by an import-graph
   assertion — *this module imports no time machinery* — rather than by reasoning about use.

**The consequence, stated honestly.** A bare `int` carries no provenance guarantee: a caller could
pass any number. That responsibility lands on **whatever orchestrates the dungeon turn**, which is
a **known unowned frontier item** (carried forward from `CLUSTER-003`). This plan does **not**
invent that orchestrator. `EXP-006`'s contract is "subtract the authoritative count you are
given"; it is not positioned to audit its caller, and the approved card does not ask it to.

## 9. `CHAR-004` integration

### 9.1 Identities to reuse — exactly these

| Item | Reachable as | Notes |
|---|---|---|
| **Torch** | `equipment.TORCH` | A module-level `Item`, exported in `__all__` |
| **Lantern** | `equipment.catalog_item("Lantern")` | `ADVENTURING_GEAR` row |
| **Oil** | `equipment.catalog_item("Oil")` | `ADVENTURING_GEAR` row. **Not** `"Oil, Burning"`, which is the `WEAPONS` row and is `COMBAT-*`'s |
| **Tinderbox** | `equipment.catalog_item("Tinder box")` | Note RC's spelling: **two words** |

**No duplicate constants are created.** `EXP-006` defines no item names, prices, encumbrances or
catalog rows of its own.

### 9.2 The ergonomic asymmetry — identified, not papered over

`TORCH` has a named export; `Lantern`, `Oil` and `Tinder box` do not, so three of the four
identities must be fetched by **string literal**. `TORCH` is exported only because it is the one
commodity appearing in **both** `WEAPONS` and `ADVENTURING_GEAR` and needed disambiguation — not
because of a general convention.

**Recommended handling:** confine the three strings to **one private module-level mapping** in
`EXP-006`, so they appear exactly once:

```python
_CATALOG_NAMES: Final = {LightSourceKind.LANTERN: "Lantern", ...}
```

**Flagged, not actioned:** exporting `LANTERN`, `OIL` and `TINDERBOX` constants from
`equipment.py` would be the cleaner long-term fix. That is **production code in a landed,
approved card's module** and is **outside this plan's authorization**. It is recorded as a
candidate `CHAR-004` ergonomic amendment requiring its own authorization — **not** done here, and
**not** worked around by duplicating the data.

### 9.3 What `EXP-006` must never read from an `Item`

Consuming `Item` exposes `.price` and `.encumbrance_cn`, which §C forbids this card to emit.
**Guard G-4 (§13) asserts by AST that this module accesses neither attribute.** This is the
concrete mechanism behind `L42`, and it is stronger than a value check: it fails even if the value
is read and discarded.

## 10. Error and refusal representation

### 10.1 The repository already has the pattern; `src/rules/exploration/` has not yet needed it

| Convention | Where established |
|---|---|
| **Plain `ValueError`** for *structural* violations — non-`int`, `bool`, negative | `turn_credit.py`, `dungeon_movement.py`, `rng.py`. **Every current exploration rejection is of this kind** |
| **A domain base + specific subclasses** for *rules* rejections | `character_creation/errors.py`, whose docstring states the distinction explicitly |

**`EXP-006` is the first exploration card with genuine *rules* refusals.** `L23` and `L24` reject
because **RC defines no procedure**, which is a domain rejection, not a malformed input.

**Add `src/rules/exploration/errors.py`.** It **instantiates the established pattern at the
correct scope**, and is explicitly **not** a new global error framework: `CharacterCreationError`
is scoped by name to character creation, and reusing it from an exploration module would cross a
domain boundary the existing docstring draws.

> **This recommendation is superseded; the shipped taxonomy is below.** Corrected 2026-10-03 under
> review-#2 finding `MED-3`. This subsection previously recommended a domain base
> `ExplorationError` plus one subclass and asserted *"One base plus one subclass — no hierarchy is
> built ahead of need."* The human adjudication of 2026-10-01 dropped the base, and two further
> concrete types were later adjudicated, so the recommendation disagreed with both §11 and the
> code. The superseded sketch is not restored.

**The shipped error taxonomy — authoritative, and the only version in force:**

```text
IgnitionNotDefinedError        RC supplies no ignition procedure
LanternRefuelNotDefinedError   RC supplies no partial-refill procedure
IgnitionAttemptLimitError      RC explicitly prohibits another attempt this round
ValueError                     malformed structural input

No base class. Exploration has three domain rejections, which does not
require a hierarchy; a base would be the speculative framework the
2026-10-01 adjudication forbade.
```

### 10.2 Mapping

| Case | Condition | Representation |
|---|---|---|
| **`L23`** | no skill + tinderbox + **adverse** | `IgnitionNotDefinedError`, message naming *"RC qualifies the 1d6 to normal (comparatively dry) circumstances"* |
| **`L24`** | no skill + no tinderbox | `IgnitionNotDefinedError`, message naming *"no procedure stated"* |
| **`L45`** | torch resolved as a weapon | **No API exists to call.** `EXP-006` exposes no weapon operation; `COMBAT-*`/`CHAR-004` own it. Proven by API shape + guard G-5, not by an exception |
| **`L46`** | oil as missile / pursuit delay | **No API exists to call.** Same mechanism |
| **`L19`** | second ignition attempt in one round | **`IgnitionAttemptLimitError`.** *Corrected 2026-10-03 (`MED-3`); this row read `ValueError` — "a caller-protocol violation, not a rules gap" — which was wrong and disagreed with the shipped code. RC's once-per-round rule is exactly what rejects it, so the rejection is a rules rejection* |
| **`L12a`** | refuel requested for a **valid lantern** that has not reached zero | **`LanternRefuelNotDefinedError`.** *Row added 2026-10-03 (`MED-3`): "the card states no arithmetic for a partial refill" is a card silence, not a structural violation. **Scope corrected later the same day** (`LOW-9`): this row briefly read "or for a torch", which bundled two different categories and did not match the card — `L12a` is worded "**refuelling a lantern that has not reached zero**" and never covered a non-lantern* |
| *(not a case)* | **non-lantern** supplied to `refuel_lantern` | **`ValueError`.** *Human adjudication 2026-10-03 (`LOW-9`): `refuel_lantern` is a lantern operation, so another source kind is an invalid **argument**. The approved card states no case for it, and none is implied — reporting it as a source silence would assert that RC failed to define how to refuel a torch, which it did not; the operation does not apply to that kind* |
| `L34` | light state queried with no surprise state | **Not an error — succeeds.** There is no surprise parameter to omit |
| Structural | non-`int`, `bool`, negative `remaining_turns`/`elapsed_turns`; a non-`LightSource` member; a non-enum `kind`/`conditions`; a non-`bool` flag | plain `ValueError` |

**`L45` and `L46` are deliberately *not* exceptions.** An exception would require an entry point
that accepts the request, and the approved card's position is that no such entry point exists.
Absence is the stronger guarantee.

## 11. Ignition model

```python
class IgnitionConditions(Enum):
    ORDINARY = auto()
    ADVERSE  = auto()          # DM-supplied; the card states RC gives no test

class IgnitionOutcome(Enum):
    AUTOMATIC            = auto()   # skill + tinderbox + ordinary
    ROLL_1D6_IGNITE_1_2  = auto()   # the 1d6 branch
    ROUTED_SKILL_CHECK   = auto()   # emit a request; CHAR-012 resolves

def ignition_outcome(...) -> IgnitionOutcome: ...   # full signature at §11's matrix below
```

Typed outcomes, **no magic strings** — consistent with `CheckOutcome` in
`dungeon_wandering_monster_check.py`. **Returns an outcome, never a `LightSource`:** selecting a
branch is not the same as lighting a source, and applying a successful ignition to a source is
**not authorized by this plan** in any slice.

> **Error type, narrowed 2026-10-01 by human adjudication.** This section originally called for
> `ExplorationError` (a domain base) **plus** `IgnitionNotDefinedError`. The adjudication directs
> that concrete types be preferred where they suffice, and no speculative exploration-wide
> hierarchy be built. The base is dropped.
>
> **Final shipped surface — three concrete types, no base** (corrected 2026-10-03, `LOW-9`; this
> paragraph previously read *"`IgnitionNotDefinedError` only"* and so disagreed with the code):
> `IgnitionNotDefinedError` (RC supplies no ignition procedure), `IgnitionAttemptLimitError` (RC
> forbids a second same-round attempt) and `LanternRefuelNotDefinedError` (RC supplies no
> partial-refill procedure — human adjudication 2026-10-03). Structural violations remain plain
> `ValueError`. Recorded as a deliberate departure from the approved plan sketch rather than an
> unnoticed one.

> **Matrix corrected 2026-10-01.** The original used `any`/`—` wildcards in two rows that
> overlapped at `(✓, ✗, ADVERSE)` and prescribed two incompatible outcomes — a plan defect, recorded
> at §19.1. **All eight combinations are now enumerated explicitly; no wildcard remains.**

```python
def ignition_outcome(
    *,
    has_fire_building: bool,
    has_tinderbox: bool,
    conditions: IgnitionConditions,
    attempt_already_made_this_round: bool,
) -> IgnitionOutcome: ...
```

| `has_skill` | `has_tinderbox` | conditions | Outcome | Provenance | Case |
|---|---|---|---|---|---|
| ✓ | ✓ | `ORDINARY` | `AUTOMATIC` | RC Explicit | `L20` |
| ✓ | ✓ | `ADVERSE` | `ROUTED_SKILL_CHECK` | RC Explicit | `L22` |
| ✓ | ✗ | `ORDINARY` | `ROLL_1D6_IGNITE_1_2` | RC Explicit | `L21` |
| ✓ | ✗ | `ADVERSE` | `ROUTED_SKILL_CHECK` | **`SR-11`** | `L22` |
| ✗ | ✓ | `ORDINARY` | `ROLL_1D6_IGNITE_1_2` | RC Explicit | `L17`, `L18` |
| ✗ | ✓ | `ADVERSE` | **`IgnitionNotDefinedError`** | RC silence | `L23` |
| ✗ | ✗ | `ORDINARY` | **`IgnitionNotDefinedError`** | RC silence | `L24` |
| ✗ | ✗ | `ADVERSE` | **`IgnitionNotDefinedError`** | RC silence | `L24` |

**`ignition_outcome` is a pure branch selector. It performs no roll and consumes no RNG.** The
`1d6` is executed by the caller against the project RNG once the branch is known; `ROUTED_SKILL_CHECK`
is **emitted, not resolved** — the DM-assigned penalty is an input to `CHAR-012`'s check, never a
value `EXP-006` produces (`L25`).

### 11.1 One attempt per round — a caller-supplied precondition

> **Corrected 2026-10-01.** The original text called this *"a caller-protocol constraint"* with
> `L19` as *"a contract test on that protocol"* — but `L19` requires **detecting** a second
> attempt, which needs round state the plan forbids. The plan named no parameter carrying it. Plan
> defect, recorded at §19.2.

```text
attempt_already_made_this_round: bool        caller-supplied, authoritative

    False  ->  evaluate the branch normally; the card records nothing
    True   ->  ERROR -- another attempt is not permitted this round
```

**The same API boundary as `elapsed_turns`** (§8): `EXP-006` **enforces** the rule from
authoritative state it is **given**; it does not become the authority that **tracks** that state.
It holds no round counter, no clock, no mutable cross-call state, and never mutates the flag.
Guard `L19b` asserts this. **No orchestrator and no action-economy framework is created** — which
component supplies the truthful value is a frontier concern, deliberately unanswered here.

## 12. Deterministic-case mapping — all 53

> **Count corrected twice on 2026-10-01: 50 → 51 → 53**, both times by post-plan human
> adjudication, and both verified by enumerating the card's IDs rather than by arithmetic.
>
> - **`L12a`** — refuelling a lantern that has not reached zero is **REFUSED** (consistency
>   correction, `5594907`). Classified **internal invariant guard**.
> - **`L19a`** — ignition with `attempt_already_made_this_round = False` evaluates normally and
>   records nothing. Classified **unit behavior**.
> - **`L19b`** — this card tracking rounds or mutating the attempt flag **MUST NOT OCCUR**.
>   Classified **ownership/boundary guard**.
>
> `L19` itself is restated, not added. No other case mapping is changed.
>
> **HISTORICAL — the split figures that accompanied this note are superseded.** The note
> originally continued *"Running totals: unit behavior 19, ownership guard 19, internal invariant
> guard 12, routed dependency 3"*, and the paragraph beneath it asserted *"Counts re-derived from
> the approved card for this plan, not assumed from the gate; they match: 18 / 18 / 11 / 3"*.
> Review #2 (`MED-4`) found that **three mutually inconsistent totals** stood in this one section
> — 53 in the heading, 53 in the blockquote, 50 in the "re-derived … they match" line, and 51 in
> the table, whose rows also **omitted `L19a` and `L19b` entirely**, the two cases the blockquote
> says were added. A "re-derived and they match" assertion that matched nothing was the defect,
> not the arithmetic. All of those figures are withdrawn; none is preserved for continuity.

**Where the split lives — deliberately NOT here.**

> **This plan no longer publishes a category split.** Corrected 2026-10-03 under review-#4 finding
> `B-1`. This section previously reproduced a table of counts under the assertion *"It is computed,
> not transcribed… `test_the_case_category_counts_are_recomputed_not_carried_over` asserts these
> exact numbers, so this table cannot drift from the code without a red test."* **That protection
> did not exist.** The test asserts the counts it computes from `CASE_DISCHARGE` against its own
> literals; it never reads this plan. The table then drifted — it still showed the split that
> review-#3's remediation had explicitly **withdrawn** (`behavior 23 / invariant 5 / surface 23 /
> reviewed 1 / routed 1`, with thirteen of the fifty-three rows misclassified) — and the whole suite
> stayed green, which is precisely the defect class the assertion claimed to prevent.
>
> The withdrawn figures are **not** restated here with corrected values, and no hand-maintained
> numeric split replaces them. That would only restart the drift.

The 53 Rule Card cases are reconciled by **`CASE_DISCHARGE`** in
`tests/rules/exploration/test_light_and_exploration_resources.py`. The **current category split is
derived from `CASE_DISCHARGE` and verified by the test suite**
(`test_the_case_category_counts_are_recomputed_not_carried_over` and
`test_every_approved_case_is_accounted_for`); **it is not duplicated normatively in this plan.**

The **case total** is likewise not owned here: it is enumerated from the approved Rule Card's own
case tables and checked by `test_the_approved_case_total_is_still_what_the_records_claim` in
`tests/rules/exploration/test_exp_006_record_consistency.py`.

The classification vocabulary is the claim-kind vocabulary that replaced the original labels,
because those did not distinguish a machine-proved property from a reviewed boundary:

```text
behavior   machine-enforced behavior                   (claim B)
invariant  machine-enforced refusal                    (claim B)
surface    machine-enforced OBSERVED surface           (claim A)
reviewed   reviewed architectural ownership boundary,
           NOT machine proof                           (claim C)
routed     not owned by this card at all
```

**Documentation-only assertions: none.** Every case is accounted for by a named mechanism, and
which mechanism discharges which case is stated per-case in `CASE_DISCHARGE` rather than summarised
here.

### 12.1 Cases discharged by the shape of the public surface

A substantial group needs **no** runtime value assertion, because the API offers nothing to
violate — no such type, parameter, member or operation exists. Which cases those are, and whether
each rests on a machine-enforced observed surface (`surface`) or on a reviewed ownership boundary
(`reviewed`), is recorded **per case in `CASE_DISCHARGE`**; it is not enumerated here, for the same
reason the split is not.

> **Enumeration removed 2026-10-03 (`B-1`).** This subsection listed `L31`, `L32`, `L33`, `L34`,
> `L40`, `L43`, `L44`, `L45` and `L46` as "provable by API shape". That list was written against the
> original classification and went stale when review-#3's remediation reclassified twelve rows from
> `surface` to `reviewed`.

Each is still **recorded as a test**, because API shape can regress silently and a test is what
makes the regression loud.

### 12.2 Genuinely requiring automated architecture tests

See §13. `L13`, `L14`, `L36`, `L38`, `L39`, `L41`, `L42` cannot be proven by shape alone — they
forbid *behavior inside* functions that legitimately exist.

## 13. Architectural guard strategy

**Absorbing the `CLUSTER-003` lesson directly** (gate Caution 2): that cluster's guard tests were
first written as substring checks over source text and produced false positives — `"round("`
matched `may_attack_in_the_same_round`, `"dungeon"` matched docstring prose. The project moved to
**AST and import-graph assertions over the parsed module**. This plan adopts that from the start.

| Guard | Technique | Enforces |
|---|---|---|
| **G-1** | **Import graph** — the module's resolved imports contain no `turn_credit`, no `dungeon_turn_time_accounting` | `L13`, `L14` — no second clock |
| **G-2** | **Import graph** — no import from any `enc_*`/encounter, combat, magic or infravision module | `L36`, `L39`, `L41` |
| **G-3** | **AST** — no numeric literal `4`/`2`/`1` paired with `d6`/`d4` dice construction; no RNG import at all | `L33` — no distance dice, and no RNG in this module |
| **G-4** | **AST** — no `Attribute` access named `price` or `encumbrance_cn` anywhere in the module | `L42` — the `CHAR-004` seam |
| **G-5** | **Namespace** — `__all__` and the module namespace contain no name matching `visibility|darkness|blind|surprise|ration|starvation|weapon|missile` | `L29`–`L32`, `L37a`, `L43`–`L46` |
| **G-6** | **AST** — `MundaneLightContribution` construction sites are reachable only where `lit_sources` was filtered on `remaining_turns > 0` | `L15b`, `L26` |

**G-6 is the only guard whose AST form is non-trivial.** If it proves brittle in implementation,
the fallback is the §6 construction invariant, which already makes the state unconstructible —
the guard is defence in depth, not the primary mechanism, and **must not be allowed to become a
reason to weaken the invariant**.

## 14. Implementation slices

Four slices. **No slice may silently begin the next**, and each ends at a human review checkpoint.

### Slice A — value model and illumination constants

```text
FILES     src/rules/exploration/light_and_exploration_resources.py   (new)
          tests/rules/exploration/test_light_and_exploration_resources.py (new)
BEHAVIOR  LightSourceKind, LightSource (+ the exhausted-never-lit invariant),
          MUNDANE_LIGHT_RADIUS_FEET, TORCH_TURNS, LANTERN_TURNS_PER_FLASK
CASES     L1, L2, L3, L4, L5, L6, L7, L16
CONSUMES  nothing
CHECKPOINT  Is the invariant right, and is the radius genuinely one constant?
INDEPENDENT  Yes -- a pure value module, readable without any other slice
```

### Slice B — depletion and the contribution output

```text
FILES     same two files
BEHAVIOR  deplete(), refuel_lantern(), MundaneLightContribution,
          mundane_light_contribution()
CASES     L8, L9, L10, L11, L12, L15, L15a, L15b, L27, L28, L34, L37
CONSUMES  an int elapsed-turn count (§8).  NO EXP-002 import
CHECKPOINT  Does L15a pass -- two torches, one expires, any_mundane_source_lit
            still True?  Is max_mundane_radius_feet None rather than 0?
INDEPENDENT  Yes -- depends only on Slice A
```

### Slice C — ignition

```text
FILES     same two files; src/rules/exploration/errors.py (new)
BEHAVIOR  IgnitionConditions, IgnitionOutcome, ignition_outcome(),
          IgnitionNotDefinedError, IgnitionAttemptLimitError
          -- the sketched ExplorationError base is DROPPED; see SS10.1
CASES     L17, L18, L19, L19a, L19b, L20, L21, L22, L23, L24, L25, L26
CONSUMES  nothing
CHECKPOINT  Are both refusals genuinely unreachable-by-default rather than
            defaulted?  Is ROUTED_SKILL_CHECK emitted, never resolved?
INDEPENDENT  Yes -- orthogonal to A and B; could in principle land first
```

### Slice D — `CHAR-004` identity binding and architectural guards

```text
FILES     same module; guards placed in the SINGLE existing test module
          rather than a new test_light_guards.py (deliberate departure,
          recorded 2026-10-03 per LOW-10: one module keeps the 53-case
          ledger and the guards that discharge it in one place)
BEHAVIOR  the private _CATALOG_NAMES mapping; no new rules behavior
CASES     L13, L14, L29-L33, L35, L36, L38-L47   (guards G-1..G-6)
CONSUMES  CHAR-004 identity only
CHECKPOINT  Do the AST/import-graph guards pass, and does G-4 actually fail
            when a .price access is introduced deliberately?
INDEPENDENT  Yes -- guards are reviewable separately from the behavior they protect
```

**Deliberately absent: an integration slice.** `CLUSTER-003` ended with a cross-card integration
fixture because three cards had to compose. `EXP-006` composes with **no researched consumer** —
an integration fixture would have to invent one, which §4 forbids. Slice D's identity binding is
the whole of its outward integration.

## 15. Governance frontier — recorded, not solved

```text
GLOBAL COMPLETE-DARKNESS WORLD-STATE PREDICATE
    Owner:    UNRESOLVED
    Rule ID:  none currently settled
    Status:   NOT an EXP-006 implementation dependency
```

`EXP-006` is implementable with this unanswered, and this plan depends on it nowhere. It becomes
binding before work begins on consumers that need to know whether a location is dark — **`ENC-001`**
(encounter `Visibility`) and **darkness-related `COMBAT-*`** (the p. 150 penalties).

**No Rule Card is created and no owner is assigned here.** It is already recorded in the approved
card's Open Question 7 and in the `EXP-006` Pre-Code Gate §7, which is the existing governance
place for unresolved frontier items; this plan adds a third pointer rather than a fourth artifact.

## 16. Plan falsification

| # | Challenge | Result |
|---|---|---|
| 1 | **Duplicate time authority** | **PASS.** `deplete()` takes an `int`; the module imports no time machinery (G-1); holds no counter, clock or accumulator |
| 2 | **Duplicate equipment/catalog facts** | **PASS.** Four identities reached through `CHAR-004`'s own API; **zero** item names, prices or encumbrances defined here. The ergonomic asymmetry is **flagged, not worked around** (§9.2) |
| 3 | **Hidden world-darkness state** | **PASS.** No field, type or return value represents world illumination. G-5 forbids the vocabulary |
| 4 | **Hidden Visibility state** | **PASS.** No `Visibility` type, no category, no classification function. Not expressible in the API |
| 5 | **Hidden blindness logic** | **PASS.** No blindness predicate, parameter or return. `L37` is satisfied by **absence** |
| 6 | **Hidden `CHAR-012` implementation** | **PASS.** `ROUTED_SKILL_CHECK` is an enum member. No `1d20`, no ability score, no penalty arithmetic |
| 7 | **Magical-light scope creep** | **PASS.** `LightSourceKind` is closed at two members with no extension point (G-5) |
| 8 | **Ration/starvation scope creep** | **PASS.** No type, operation or constant. G-5 forbids the names |
| 9 | **Exhausted source still contributing light** | **PASS** — and this is the strongest result. The state is **unconstructible** (§6.1 invariant), not merely untested; `L15a` proves the scoping is source-local, not party-wide |
| 10 | **Speculative abstractions for future cards** | **PASS.** No interface, protocol, registry, plugin seam or "environment" type. One module, three concrete error types with no base, and a pinned public surface. §5 records what was deliberately not created |

## 17. Blockers

```text
NONE.

No "IMPLEMENTATION-PLAN BLOCKER -- NOT ESTABLISHED" condition was reached.
Every decision above is either fixed by the approved Rule Card, or an ordinary
implementation-representation choice explicitly permitted by the Pre-Code Gate.
```

Two items are **flagged for the reviewer's judgement** and neither blocks:

1. **`CHAR-004` ergonomic asymmetry** (§9.2) — three identities fetched by string. Handled
   without duplication; the cleaner fix needs separate authorization for a landed module.
2. **Elapsed-turn provenance** (§8.2) — a bare `int` carries no authoritative-origin guarantee.
   That responsibility belongs to the unowned turn orchestrator, which this plan does not invent.

## 19. Slice-C blockers — **recorded 2026-10-01, RESOLVED 2026-10-01**

```text
SLICE C READY  -- both blockers resolved by human adjudication.
                  The defects below are retained as the record of what was wrong
                  and how it was settled; they are NOT erased.
```

**Resolutions**, applied to §11 and to the Rule Card:

- **19.1 →** `SR-11`. Where a character has `Fire-Building` and conditions are `ADVERSE`, the
  adverse-condition procedure governs **regardless of a tinderbox**. The wildcard rows are gone;
  all eight combinations are enumerated, and `(✓, ✗, ADVERSE)` appears once → `ROUTED_SKILL_CHECK`.
- **19.2 →** `attempt_already_made_this_round: bool`, caller-supplied. `L19` is restated against
  it; `L19a` and `L19b` added. `EXP-006` gains no round state.

Both are **human adjudications**, not implementer choices, and the Pre-Code Gate is revalidated
for the ignition portion at `EXP-006_PRE_CODE_GATE.md` §8a — with its original misses recorded
rather than erased.

Found by a pre-Slice-C audit. **Both are defects in this plan**, not in the approved Rule Card's
evidence, and neither may be resolved by an implementer choosing a precedence.

### 19.1 Defect 1 — §11's ignition matrix is internally contradictory

```text
| ✓ | ✗ | any     | ROLL_1D6_IGNITE_1_2 | L21 |
| ✓ | — | ADVERSE | ROUTED_SKILL_CHECK  | L22 |
```

Row 2's `any` **includes** `ADVERSE`; row 3's `—` **includes** no-tinderbox. At
`(has_skill=True, has_tinderbox=False, ADVERSE)` the matrix therefore prescribes **two
incompatible outcomes**. The approved Rule Card §5 carries the same overlap in its own two rows.

**The accepted evidence does not resolve it.** `E-36` quotes two parallel conditionals —
*"If the character is trying to build a fire **without** a tinderbox… `1d6`…"* and *"If the
character is trying to build a fire **in adverse conditions**… skill check…"* — with **no stated
precedence**. The evidence packet's own §5.8 synthesis block does not contain a
skill-plus-no-tinderbox branch at all; that row entered at Stage B from E-36's raw quote and was
never reconciled against the adverse branch.

**Disposition: `NOT ESTABLISHED BY CURRENT APPROVED EVIDENCE`.**

### 19.2 Defect 2 — `L19` requires state §11 forbids

§11 states that one-attempt-per-round *"is a caller-protocol constraint. `EXP-006` holds no round
state… the caller makes at most one call per round, and `L19` is a contract test on that
protocol."*

But `L19` is **`Two ignition attempts in one round → ERROR`**. Detecting a *second* attempt
requires knowing an attempt already happened this round — round state, which §11 correctly
forbids as a second clock. **The plan names no caller-supplied parameter that would carry it**, so
as written `L19` is not implementable without either a hidden counter or a contract the plan does
not specify.

**Disposition: `NOT ESTABLISHED BY CURRENT APPROVED PLAN`.** Resolving it is a design decision
(an explicit caller-supplied precondition, or a restatement of `L19`), not an implementer's call.

## 18. Gate state

```text
EXP-006 Rule Card              APPROVED        2026-10-01
EXP-006 PRE-CODE GATE          PASS            2026-10-01
EXP-006 IMPLEMENTATION PLAN    APPROVED       2026-10-01
EXP-006 IMPLEMENTATION         CODE COMPLETE; NOT FINALLY ACCEPTED
EXP-006-PHASE: REVIEW-4-REMEDIATED
EXP-006 LOW-3 / LOW-8          RESOLVED  (applied at a150837)
CLUSTER-004 IMPLEMENTATION     NOT AUTHORIZED  (ARCHITECTURE.md §15.2 step 4)
CLUSTER-004                    NOT AUTHORIZED
ENC-005 Stage B                DEFERRED -- not in this plan
```
