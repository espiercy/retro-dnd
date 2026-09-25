# CLUSTER-003 — Equipped Dungeon Movement Implementation Plan

## 1. Status / Purpose

```text
STATUS:  DRAFT / AWAITING HUMAN APPROVAL
```

> **This plan authorizes nothing.** It is the input to `ARCHITECTURE.md` §15.2 **step 4** — implementation-readiness re-approval — which is a human act and has **not** been given for `CLUSTER-003`. No production code exists for this cluster and none may be written until that approval lands.

Drafted 2026-09-25 on explicit human authorization, following the `CLUSTER-003` Pre-Code Gate `PASS` (2026-09-24, `docs/technical/CLUSTER-003_PRE_CODE_GATE.md`) and the human-approved `CHAR-005` amendment of 2026-09-25.

**Scope:** implementation of three approved Rule Cards.

| Card | Title | Status |
|---|---|---|
| `CHAR-004` | Starting Equipment & Expedition Preparation | `APPROVED` 2026-09-24 |
| `CHAR-005` | Encumbrance & Movement Rate | `APPROVED` 2026-09-24, **amended 2026-09-25** |
| `EXP-003` | Dungeon Movement | `APPROVED` 2026-09-24 |

## 2. Authoritative Inputs

| Input | Artifact |
|---|---|
| `CHAR-004` specification | `docs/rules/character_creation/starting_equipment_and_expedition_preparation.md` |
| `CHAR-005` specification | `docs/rules/character_creation/encumbrance_and_movement_rate.md` (incl. §1.1, amended) |
| `EXP-003` specification | `docs/rules/exploration/dungeon_movement.md` |
| Human adjudications, `SR-6`–`SR-10` | `docs/rules/clusters/CLUSTER-003-stage-b-synthesis.md` |
| Pre-Code Gate findings | `docs/technical/CLUSTER-003_PRE_CODE_GATE.md` |
| Governing process | `ARCHITECTURE.md` §12, §15.1, §15.2; `TESTING_STRATEGY.md`; `DEVELOPMENT_WORKFLOW.md` |
| Structural precedent | `docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` |

**The Rule Cards are the specification. This plan may not add, soften or reinterpret a single mechanical clause.** Where it makes a choice the cards leave to implementation, it says so explicitly (§5).

## 3. Binding Implementation Scope

```text
CHAR-004   starting money; free starting kit; the mundane equipment
           catalogs (weapons, ammunition, nets, armour, adventuring
           gear) with cost and Enc; container capacity and the derived
           encumbrance cases; per-class mundane equipment legality for
           all nine classes; Druid +50% wooden-weapon pricing; the
           unlisted-item procedure's executable behaviour

CHAR-005   total carried encumbrance; the six RC encumbrance bands;
           normal / encounter / running movement and their units and
           time scales; slowest-member group movement; running duration
           and exhaustion; Suit Armor as ordinary 750 cn; Mystic
           level-dependent MV with the SR-9 gate and exact fractional
           encounter movement; SS6.1 Mystic running

EXP-003    dungeon movement allowance per turn; indoor distance units;
           the default 10' map scale; the Game Turn Checklist behaviour
           this card owns; integration with landed EXP-002
```

## 4. Hard Non-Goals

### 4.1 No speculative orchestration

No `GameState`, `Party`, `Character`, `Inventory` aggregate, `ExplorationEngine`, `TurnManager`, `Command`, `Session` or `ApplicationService`. `CLUSTER-001` and `CLUSTER-002` landed as **pure functions and small frozen value objects over explicit inputs**, and this cluster extends that, it does not replace it.

### 4.2 No out-of-boundary mechanics

```text
NOT IMPLEMENTED -- not in the cluster
    CHAR-006 retainers        CHAR-008 alignment
    CHAR-009 class abilities  EXP-010 party formation
    CHAR-010 thief skills     CHAR-011 weapon mastery
    CHAR-012 general skills   TREAS-* magic items
    EXP-005/006/007           ENC-002/003/005
    COMBAT-*                  ADV-*

NOT IMPLEMENTED -- out of V1 by human decision
    mounts, vehicles, ships, siege equipment
    Chapter 10 high-level equipment provisioning  [NOT V1-WIRED]

NOT IMPLEMENTED -- deferred by this plan (SS9)
    CHAR-005 SS7 condition movement modifiers     [NOT V1-WIRED]
```

### 4.3 No abstraction invented to accommodate a source defect

**This is the cluster's single most important non-goal**, because its history is full of temptations to violate it:

```text
MUST NOT EXIST after this cluster lands:

    a generic "specific equipment movement overrides general
        encumbrance" framework                       [SR-8 forbids]
    proportional Suit Armor movement scaling         [SR-8 forbids]
    proportional Mystic MV scaling under encumbrance [SR-9 forbids]
    Mystic encumbrance immunity                      [SR-9 forbids]
    a separate Mystic encumbrance table              [SR-9 forbids]
    a separate Mystic running formula                [SS6.1 forbids]
    any rounding of Mystic encounter movement        [Q6 forbids]
    a mapping time cost, roll or failure state       [EXP-003 SS4 forbids]
    a terrain subsystem                              [EXP-003 SS7 forbids]
    a second movement-rate authority                 [EXP-003 SSC forbids]
    spatial/grid quantisation                        [unowned; not here]
```

Each has a guard test (§12).

### 4.4 No infrastructure invention

The RNG abstraction, error conventions, `CharacterClass`, immutability style and test layout already exist. **Reuse them.** The one genuinely new primitive this cluster needs is a currency type (§6.1), and it is new because nothing comparable exists — not because the cards are detailed.

## 5. Implementation Choices Made Here (not rules decisions)

Recorded explicitly so a reviewer can see what the plan decided versus what the cards specify.

| # | Choice | Rationale |
|---|---|---|
| **5.1** | **Currency is an integer count of copper pieces**, with RC's `1 pp = 5 gp = 10 ep = 50 sp = 500 cp` as the conversion table | Pre-Code caution 3. `4.5 gp` must be exact; `450 cp` is. Mirrors `CHAR-005`'s approved requirement that fractional movement never become a lossy float. **No rule changes** |
| **5.2** | **Movement rates are `fractions.Fraction`**, not `float` | Q6 requires `130/3` exactly and forbids rounding. `Fraction` gives exact arithmetic **and** exact comparison — the latter matters for §8's slowest-member rule, which must compare `43⅓` against `40` unambiguously. Standard library; no dependency added |
| **5.3** | **Encumbrance is an integer count of `cn`** | Every RC value is integral and every derived case (§6.2) yields an integer. `CHAR-005` M14 already rejects non-integers |
| **5.4** | **Equipment catalogs are module-level frozen tables**, `MappingProxyType` over frozen dataclasses | Exactly how `_HIT_DIE`, `_NAME_LEVEL`, `_MAXIMUM_LEVEL` and the `CHAR-007` tables already land |
| **5.5** | **Class legality is a predicate function over `(CharacterClass, item)`**, not a per-class type hierarchy | §14 audit: a class-rule architecture invented for Druid/Mystic exceptions is exactly the over-abstraction §4.3 forbids. Nine classes, one table, one predicate |
| **5.6** | **`EXP-003` returns an allowance; it does not own a loop** | The card owns the movement spend, not orchestration (§4.1) |

## 6. Type and Module Design

### 6.1 New primitive — `Coin` (currency)

```text
src/rules/currency.py                        NEW -- shared primitive

    class Denomination(Enum)      PP EP GP SP CP
    IN_COPPER: Mapping            PP=500 cp  GP=100 cp  EP=50 cp
                                  SP=10 cp   CP=1 cp
                                  (from RC 1 pp = 5 gp = 10 ep
                                   = 50 sp = 500 cp)

    @dataclass(frozen=True, slots=True)
    class Coin
        copper: int               the ONLY stored field
        @classmethod of(cls, amount: int, d: Denomination) -> Coin
        def __add__ / __sub__ / __mul__(int) -> Coin
        def __lt__ / __le__ ...   exact ordering
        def scaled(numerator, denominator) -> Coin    exact; Druid +50%
```

**Location.** `src/rules/currency.py`, **not** under `character_creation/`. Following the `character_class.py` precedent: a primitive no single Rule Card owns. `CHAR-004` needs it now; `TREAS-*` and `ADV-003` will need the same one. **It carries conversion and arithmetic and nothing else** — no prices, no items, no class rules.

**Why new.** No currency representation exists anywhere in `src/`. This is genuine novelty, not parallel-framework invention.

**Druid `+50%`:** `Coin.of(3, GP).scaled(3, 2)` → `450 cp`. Exact, no float, no rounding question.

### 6.2 New — `CHAR-004` equipment

```text
src/rules/character_creation/equipment.py    NEW -- CHAR-004

  identity and data
    class ItemCategory(Enum)      WEAPON AMMUNITION ARMOR SHIELD
                                  GEAR CONTAINER CLOTHING
    class WeaponSize(Enum)        SMALL MEDIUM LARGE
    class WeaponTrait(Enum)       the RC note codes this card uses:
                                  CLERIC_PERMITTED, MAGIC_USER_OPTIONAL,
                                  TWO_HANDED, HAND_OR_TWO_HANDED,
                                  EDGED_OR_POINTED, METAL, THROWN, ...
    @dataclass(frozen=True, slots=True)
    class Item
        name, category, cost: Coin, encumbrance_cn: int,
        size: WeaponSize | None, traits: frozenset[WeaponTrait],
        capacity_cn: int | None         containers only

  catalogs (frozen, module-level)
    WEAPONS / AMMUNITION / ARMOR / ADVENTURING_GEAR

  derived encumbrance -- SS6.2 of the card
    def filled_container_encumbrance(container, contents_cn) -> int
    def clothing_encumbrance(item, worn: bool) -> int
    def ammunition_encumbrance(row, shots: int) -> int
    def net(side_feet: int) -> Item
    def whip(length_feet: int) -> Item

  money and kit
    def starting_gold(rng: RNG) -> Coin          3d6 x 10 gp
    FREE_STARTING_KIT: tuple[Item, ...]

  legality -- SS7 of the card
    def is_legal(cls, item, *, magic_user_expanded_list: bool = False)
        -> bool
    def purchase_cost(cls, item) -> Coin         applies Druid +50%
```

**Ownership:** every symbol here is `CHAR-004`'s. **This module never computes a movement rate** — guard case E60.

### 6.3 New — `CHAR-005` movement

```text
src/rules/character_creation/encumbrance_and_movement.py   NEW -- CHAR-005

    @dataclass(frozen=True, slots=True)
    class MovementRate
        normal: Fraction      feet per TURN
        encounter: Fraction   feet per ROUND
        running: Fraction     feet per ROUND

    _ENCUMBRANCE_BANDS: tuple[...]    the six RC bands
    _MYSTIC_MV: Mapping[int, int]     levels 1..16 -> 120..320
    _MYSTIC_MAXIMUM_LEVEL: Final = 16

    def movement_rate(cls, level, total_encumbrance_cn) -> MovementRate
    def party_movement_rate(rates) -> MovementRate     slowest member
    SUIT_ARMOR_ENCUMBRANCE_CN: Final = 750             re-exported value

    running/exhaustion (SS9):
    MAXIMUM_RUNNING_ROUNDS: Final = 30
    REQUIRED_REST_TURNS: Final = 3
    class ExhaustionPenalty(frozen dataclass)
```

**`movement_rate` is the single authoritative entry point.** It:

1. validates `level` per amended §1.1 (int, not bool, `1 <= level <= max`);
2. validates `total_encumbrance_cn` (int, not bool, `>= 0`);
3. if `cls is MYSTIC` **and** `total_encumbrance_cn <= 400` → `MV` path (`SR-9`);
4. otherwise → band-table path;
5. derives all three rates from the resulting normal speed by the **one** shared rule.

**Steps 3–5 are why there is no separate Mystic subsystem**: the gate chooses a *normal speed*, and one derivation follows. `SR-9`, §6.1 and Q4 are all satisfied by the same three lines.

### 6.4 New — `EXP-003` dungeon movement

```text
src/rules/exploration/dungeon_movement.py    NEW -- EXP-003

    DEFAULT_MAP_SCALE_FEET: Final = 10

    @dataclass(frozen=True, slots=True)
    class DungeonMovementAllowance
        feet: Fraction                  per 10-minute turn
        def squares(self, scale_feet: int = DEFAULT_MAP_SCALE_FEET)
            -> Fraction                 EXACT; never rounded (D9)

    def turn_movement_allowance(party_rate: MovementRate)
        -> DungeonMovementAllowance     consumes .normal; computes nothing
```

**`turn_movement_allowance` reads `party_rate.normal` and nothing else.** It cannot recompute a rate because it never receives encumbrance, class or level. **The type system enforces the ownership boundary** — that is deliberate, and it is why `EXP-003` takes a `MovementRate` rather than raw inputs.

**Time stays with `EXP-002`.** This module imports nothing from `dungeon_turn_time_accounting`; the integration is demonstrated in Slice E by a test that drives the real landed `DungeonTimeAccounting.complete_ordinary_turn()` alongside an allowance.

### 6.5 Errors

```text
src/rules/character_creation/errors.py       EXTENDED

    class EquipmentLegalityError(CharacterCreationError)    NEW
    class EncumbranceError(CharacterCreationError)          NEW
    class MovementLevelError(CharacterCreationError)        NEW
    class UnlistedItemError(CharacterCreationError)         NEW
```

Extension of the landed hierarchy, not a parallel one. Each message names the violated clause, so tests discriminate by `match=` — the established idiom. **`MovementLevelError` deliberately mirrors `HitPointLevelError`**: one parameter, one error, covering both the structural and domain case, for exactly the reasons that docstring already records.

### 6.6 Reuse / extension / new — the §13 audit

| Concern | Disposition | Detail |
|---|---|---|
| Class identity | **REUSE** | `CharacterClass` unchanged. Its docstring already says equipment restrictions are *not* its business — this cluster adds data *about* classes elsewhere, as `CHAR-002`/`CHAR-003` do |
| Level validation | **REUSE the pattern** | `HitPointLevelError`'s structural+domain shape, including the explicit `bool` exclusion |
| Per-class maximum level | **REUSE the pattern** | `_MAXIMUM_LEVEL` is a *private card-local projection* of `ADV-002`'s property. `CHAR-005` does the same for the Mystic's 16, with the same recorded justification |
| Immutable domain data | **REUSE** | `@dataclass(frozen=True, slots=True)` + `MappingProxyType` |
| Error handling | **EXTEND** | Four subclasses on `CharacterCreationError` |
| RNG | **REUSE** | `rng.roll("3d6")` for starting money; `RollResult.total` (the Slice-C lesson) |
| Turn credit | **REUSE, CONSUME ONLY** | Landed `TurnCredit` / `DungeonTimeAccounting`, untouched |
| Testing conventions | **REUSE** | `pytest`, `ScriptedRNG`, `pytest.raises(..., match=)`, per-card test modules + an integration module |
| **Currency** | **NEW** | §6.1. Nothing comparable exists |
| **Exact rationals** | **NEW (stdlib)** | `fractions.Fraction`. No project convention existed because nothing needed one |
| **Item/catalog data** | **NEW** | §6.2 |

### 6.7 Dependency graph

```text
        rng/                      currency.py         character_class.py
          |                          |    |                   |
          |          +---------------+    |                   |
          v          v                    v                   v
    equipment.py  [CHAR-004] -------------------------------->|
          |  Enc (cn) only                                    |
          v                                                   v
    encumbrance_and_movement.py  [CHAR-005] <------------------+
          |  MovementRate
          v
    dungeon_movement.py  [EXP-003]
          |  DungeonMovementAllowance
          v
    dungeon_turn_time_accounting.py  [EXP-002, LANDED -- consumed, not imported]
```

**Acyclic, one direction, no back-edges.** `equipment` does not import `encumbrance_and_movement`; `dungeon_movement` does not import `equipment`.

## 7. Ownership Audit (§14)

| Module / API | Owning card | Duplication challenge | Verdict |
|---|---|---|---|
| `currency.Coin` | **none — shared primitive** | Could `CHAR-004` own it? | **No.** `TREAS-*`/`ADV-003` will need the same type. `character_class.py` precedent |
| `equipment.Item`, catalogs, derived encumbrance | `CHAR-004` | Does equipment calculate movement? | **No.** No movement symbol is importable from it. Guard E60 |
| `equipment.is_legal` / `purchase_cost` | `CHAR-004` | Does this duplicate `CHAR-009`? | **No.** Human Decision 1 assigns mundane legality here; `CHAR-009` is unresearched and referenced nowhere |
| `MovementRate`, `movement_rate` | `CHAR-005` | Does dungeon movement calculate encumbrance? | **No.** `EXP-003` receives a `MovementRate`; encumbrance is not in its signature |
| `_MYSTIC_MV` | `CHAR-005` | Mystic behaviour leaking into equipment? | **No.** `equipment.py` contains no Mystic symbol except the armour-prohibition legality row, which is equipment legality |
| Class legality table | `CHAR-004` | A general class-rule architecture for Druid/Mystic? | **No** — §5.5. One table, one predicate |
| `turn_movement_allowance` | `EXP-003` | Does `EXP-003` own time? | **No.** It imports nothing from `EXP-002` and returns no turn |
| Exhaustion penalties | `CHAR-005` | Combat mechanics leaking in? | **Recorded, not applied.** `CHAR-005` §A already notes they are `COMBAT-002`/`003` as combat mechanics; the card owns them as the consequence of a movement choice, and the value object carries them without resolving an attack |

**Knowledge required from a deferred card:** none. The one place it was nearly required — the `MV` level input — was resolved by the 2026-09-25 amendment making level a validated caller input rather than an `ADV-*` dependency.

## 8. `CHAR-005` §7 — condition modifiers, `NOT V1-WIRED`

**Disposition (human-accepted Pre-Code caution 1):**

```text
CHAR-005 SS7 condition movement modifiers:
    SPECIFIED BUT NOT V1-WIRED
```

**Demonstration, not assertion.** Every causation owner is `Unresearched`, so no landed or approved card can produce blindness, stunning, prone or starvation:

| Condition | Causation owner | Status |
|---|---|---|
| Blindness | `COMBAT-*` / `EXP-006` | Unresearched |
| Stunning | `COMBAT-*` | Unresearched |
| Prone | `COMBAT-*` | Unresearched |
| Starvation | an `ADV-*` survival responsibility | Unresearched; **no Rule ID assigned** |

**Precedent:** `CHAR-003 W3` — *"NOT V1-WIRED"* — the established treatment for an approved mechanic whose trigger is unreachable.

```text
IMPLEMENTED:      nothing in SS7
PRESERVED:        SR-10 remains APPROVED and recorded on the card
NOT INVENTED:     simultaneous-condition composition
                  ordering between condition modifiers
                  ordering between conditions and the SR-9 gate
```

**No speculative condition infrastructure is built** — no `Condition` enum, no modifier pipeline, no hook. `movement_rate()` takes no condition parameter. When a causation card lands, it will arrive with its own composition question answered by whoever owns it.

## 9. Test Strategy and Traceability

### 9.1 Layout

```text
tests/rules/test_currency.py                                  NEW
tests/rules/character_creation/test_equipment.py              NEW
tests/rules/character_creation/test_encumbrance_and_movement.py  NEW
tests/rules/exploration/test_dungeon_movement.py              NEW
tests/rules/test_cluster_003_integration.py                   NEW
```

Mirrors the landed `test_cluster_001_integration.py` / `test_cluster_002_integration.py` convention.

### 9.2 Traceability

**168 approved cases** — `CHAR-004` 60 (`E1`–`E60`), `CHAR-005` 76 (`M1`–`M76`), `EXP-003` 32 (`D1`–`D32`).

Not one case per test function. Each case ID appears in a test's docstring or in a `pytest.mark.parametrize` id, so `grep -r "E17" tests/` locates its coverage. A ledger in the Slice F completion record reconciles **all 168 against exactly one owning test each**, following the `CLUSTER-002` 189-case ledger precedent.

**Every case is accounted for as one of:** executable pytest unit · cross-card runtime composition · static API-shape conformance · documented calling-contract conformance.

### 9.3 Required coverage, explicitly

| Area | Cases |
|---|---|
| Every encumbrance band boundary, both sides | `M1`–`M14` — `400/401`, `800/801`, `1200/1201`, `1600/1601`, `2400/2401` |
| Belt pouch arithmetic (`SR-6`) | `E5`–`E7` — **`52`, never `55`** |
| Container behaviour | `E8`–`E13` incl. capacity as a hard limit |
| Worn vs. packed clothing | `E14`–`E16` |
| Ammunition inverse rates | `E20`–`E24` |
| Dimension-dependent gear | `E17`–`E19` |
| Class equipment legality | `E26`–`E50`, all nine classes, both directions |
| Druid `+50%` pricing | `E51`–`E52` — **exact `Coin`, no float** |
| Suit Armor through ordinary encumbrance | `M25`–`M30` |
| Mystic `SR-9` threshold | `M31`–`M40` — `400` on, `401` off |
| Exact fractional Mystic encounter movement | `M41`–`M47` |
| Mystic running | `M48` |
| Ordinary / encounter / running unit distinctions | `M15`–`M24`, `M70`–`M71` |
| Dungeon movement consumes, never recomputes | `D1`–`D11`, `D29` |
| Dungeon-time integration | `D28` + Slice E integration test |
| No extra mapping cost | `D12`–`D17` |
| No invented terrain subsystem | `D18`–`D20`, `M76` |

### 9.4 Guard tests — architectural boundaries

These assert the **absence** of behaviour and must not be dropped as "negative tests that pass trivially". Each is the executable form of a §4.3 prohibition.

```text
M29  no generic equipment movement-override pathway
M28  no Suit Armor-specific rate
M30  Suit Armor is exactly 750 cn, unscaled
M37  no proportional Mystic scaling
M38  no Mystic encumbrance immunity
M46  no rounding of Mystic encounter movement
M47  exact representation, not a lossy float
M75  no "personal possessions" ownership restriction
M76  no terrain modifier reachable from CHAR-005
D13  no mapping roll        D14  no mapping failure state
D15  no mapping penalty     D18/D19  no dungeon terrain modifier
D31  EXP-003 does not round a fractional rate
E58  mounts/vehicles/ships/siege refused
E59  Chapter 10 provisioning refused
E60  CHAR-004 cannot be asked for a movement rate
```

## 10. Implementation Slices

Six slices, each independently reviewable and landable, none requiring an unfinished abstraction from a later one.

---

### Slice A — shared currency primitive

| | |
|---|---|
| **Responsibility** | Exact integral currency and RC conversions |
| **Files** | `src/rules/currency.py` (new); `tests/rules/test_currency.py` (new) |
| **Card clauses** | `CHAR-004` §4 conversions; the exactness requirement behind `E51` |
| **Dependencies** | None |
| **Tests** | Conversions in both directions; `scaled(3,2)` on odd `cp` totals; ordering; `Coin` immutability; rejection of non-int and `bool` |
| **Verification** | `verify.py` PASS; 100% branch coverage on the new file |
| **Excludes** | No prices, no items, no class rules |
| **After** | One new shared primitive. Nothing else changes |

---

### Slice B — `CHAR-004` catalogs, money, derived encumbrance

| | |
|---|---|
| **Responsibility** | Item data, starting money, free kit, and the four derived-encumbrance cases |
| **Files** | `src/rules/character_creation/equipment.py` (new); `errors.py` (extend: `EncumbranceError`, `UnlistedItemError`); `tests/.../test_equipment.py` (new) |
| **Card clauses** | `CHAR-004` §2, §3, §4, §6.1, §6.2, §8 |
| **Dependencies** | Slice A; landed `rng` |
| **Tests** | `E1`–`E25`, `E53`–`E57`. **`E6` (`52 cn`) and `E12` (quiver total `10`, not `15`) are the two that most easily land wrong** |
| **Verification** | `verify.py` PASS; 100% branch on `equipment.py` |
| **Excludes** | Legality (Slice C); all movement |
| **After** | Equipment data and encumbrance arithmetic complete and tested; no legality, no movement |

---

### Slice C — `CHAR-004` class legality and Druid pricing

| | |
|---|---|
| **Responsibility** | Per-class mundane equipment legality; the Druid surcharge |
| **Files** | `equipment.py` (extend); `errors.py` (extend: `EquipmentLegalityError`); `test_equipment.py` (extend) |
| **Card clauses** | `CHAR-004` §5, §7, incl. **`SR-7`** |
| **Dependencies** | Slices A–B; landed `CharacterClass` |
| **Tests** | `E26`–`E52`, `E58`–`E60`. **`E26` + `E36` + `E37` together prove `SR-7`**: the dagger is legal with the expanded-list flag both ON and OFF, while a staff is legal only with it ON |
| **Verification** | `verify.py` PASS; 100% branch |
| **Excludes** | Magic-item restrictions (`TREAS-004`); thief-skill prerequisites (`CHAR-010`) |
| **After** | `CHAR-004` complete. `src/` has no movement code |

---

### Slice D — `CHAR-005` movement

| | |
|---|---|
| **Responsibility** | The **single** authoritative numerical movement system |
| **Files** | `src/rules/character_creation/encumbrance_and_movement.py` (new); `errors.py` (extend: `MovementLevelError`); `tests/.../test_encumbrance_and_movement.py` (new) |
| **Card clauses** | `CHAR-005` §1 + **§1.1 (amended)**, §2–§6, §6.1, §8–§11, incl. **`SR-8`**, **`SR-9`** |
| **Dependencies** | Slices A–C (for `SUIT_ARMOR_ENCUMBRANCE_CN` as data); `CharacterClass` |
| **Tests** | `M1`–`M51`, `M60`–`M76`, **minus** the §7 condition cases (§9 of this plan) |
| **Verification** | `verify.py` PASS; 100% branch. **Additionally: no `float` appears in any movement value** |
| **Excludes** | **§7 condition modifiers — `NOT V1-WIRED`.** `movement_rate()` takes no condition parameter |
| **After** | Movement authoritative and complete for reachable V1 behaviour |

---

### Slice E — `EXP-003` dungeon movement and `EXP-002` integration

| | |
|---|---|
| **Responsibility** | Spend the authoritative rate against the landed dungeon turn |
| **Files** | `src/rules/exploration/dungeon_movement.py` (new); `tests/rules/exploration/test_dungeon_movement.py` (new) |
| **Card clauses** | `EXP-003` §1–§8 |
| **Dependencies** | Slice D; landed `EXP-002` `DungeonTimeAccounting` |
| **Tests** | `D1`–`D32`. The integration test drives the **real** `complete_ordinary_turn()`, never a stub — the `CLUSTER-001` precedent |
| **Verification** | `verify.py` PASS; 100% branch |
| **Excludes** | Turn accounting (`EXP-002` owns it); wandering checks (`EXP-001`); mapping mechanics; terrain; quantisation |
| **After** | The full chain executes end to end |

---

### Slice F — cross-card integration and cluster records

| | |
|---|---|
| **Responsibility** | Prove the chain with real components; reconcile all 168 cases; write completion records |
| **Files** | `tests/rules/test_cluster_003_integration.py` (new); `docs/completion-records/ISSUE-015`…`ISSUE-020` + `INDEX.md`; cluster record |
| **Card clauses** | Cross-card composition; the calling-contract cases |
| **Dependencies** | Slices A–E |
| **Tests** | The authoritative chain, using **real** production components throughout: create a character (landed `CHAR-001`/`002`/`003`) → equip legally (`CHAR-004`) → total `cn` → rate (`CHAR-005`) → allowance (`EXP-003`) → `complete_ordinary_turn()` (`EXP-002`) |
| **Verification** | `verify.py` PASS; **168/168 reconciled, exactly one owner each** |
| **Excludes** | **No production code.** Tests and records only |
| **After** | `CLUSTER-003` implementation complete on the branch, ready for human final review |

---

### 10.1 Worked integration fixture (Slice F)

The chain must be shown, not asserted. The plan names one concrete fixture now so a reviewer can check the arithmetic before any code exists:

```text
A 10th-level Mystic, legally equipped.

  CHAR-004   Mystic may wear NO armour (E48). Carries dagger (10 cn),
             backpack 20 + 200 cn rations = 220, waterskin filled 30,
             belt-pouch filled 52, torches(6) 120, rope 50.
             clothes and shoes WORN -> 0  (E14)
             total = 10 + 220 + 30 + 52 + 120 + 50 = 482 cn

  CHAR-005   482 > 400  ->  SR-9 gate CLOSED
             -> standard band 401-800  ->  90' (30'), running 90'
             NOT 210'. The Mystic is not immune (M34/M38).

  EXP-003    allowance = 90 feet per turn; 9 squares at the default
             10' scale.

  EXP-002    complete_ordinary_turn() -> TurnCredit(turn_number=1,
                                                    ORDINARY)

Then drop the torches and rope (170 cn):
             total = 312 cn  ->  gate OPEN  ->  MV 210'
             encounter = 70' exactly; running = 210'/round
             allowance = 210 feet; 21 squares
```

**This single fixture exercises `SR-9` in both directions, the worn-clothing rule, `SR-6`, the exact-fraction path and the `EXP-002` boundary.**

## 11. Branch / Landing Strategy

```text
branch:  cluster-003-implementation   (from cluster-003-stage-a-evidence
                                       after the plan is approved)

one commit per slice, each with verify.py PASS
human review after EACH slice, before the next begins
final human branch review
single --no-ff merge to main  -- SEPARATELY AUTHORIZED, not by this plan
```

Mirrors `CLUSTER-002`'s landing, which caught three defects at slice boundaries that a single large commit would have buried.

## 12. Coverage and Verification

```text
per slice:   uv run python scripts/verify.py    must PASS
             tests, differentiated coverage, Ruff, mypy strict

coverage:    100% branch, PER FILE, for every new file under src/rules/
             (scripts/check_coverage.py enforces it)

typing:      mypy strict over src, tests, scripts
             bool excluded explicitly wherever an int is expected
             -- static typing does NOT prevent it
```

## 13. Deferred Items — must stay deferred

| Item | Status |
|---|---|
| `CHAR-005` §7 condition modifiers | **`NOT V1-WIRED`** (§8). `SR-10` preserved on the card |
| Chapter 10 high-level equipment | **`NOT V1-WIRED`**. Guard `E59` |
| Mounts, vehicles, ships, siege | **Out of V1.** Guard `E58` |
| Spatial / grid quantisation | **Unowned.** Guard `D31` |
| Rough/broken-terrain modifier | **Unowned.** Guards `M76`, `D18`/`D19` |
| `CHAR-006`, `CHAR-008`, `CHAR-009`, `EXP-010` | **Outside the cluster** |
| Endurance skill (`CHAR-012`) | Named by `CHAR-005` §9, **specifies nothing**; base 30-round limit is complete without it |

## 14. Risks / Review Hotspots

### 14.1 Ordinary design choices — resolved here, not escalated

`Fraction` over a hand-rolled rational; `cp` as the currency base; catalogs as frozen module tables; legality as a predicate not a hierarchy; `EXP-003` taking a `MovementRate` rather than raw inputs.

### 14.2 Genuine risks, with safeguards

| Risk | Safeguard |
|---|---|
| **A `float` reaches a movement value**, silently reintroducing rounding Q6 forbids | Slice D verification adds an explicit no-`float` check; `M47` asserts exact representation; `Fraction` makes the failure loud rather than silent |
| **`SR-9` implemented as a multiplier** rather than a threshold — the single most likely misreading of the whole cluster | `M34` (401 cn → `90'`, not a scaled `210'`) and `M37` are guard tests; §6.3 step 3 is a branch, structurally incapable of scaling |
| **Suit Armor special-cased** somewhere, recreating the override `SR-8` refused | `M28`/`M29` assert the pathway does not exist; Suit Armor appears in `src/` only as an integer in a catalog row |
| **`EXP-003` recomputing a rate** under integration pressure | Its signature accepts `MovementRate` and never encumbrance/class/level — the boundary is type-enforced, not merely documented |
| **A condition parameter added "while we're here"** | §8; `movement_rate()`'s signature is fixed by this plan and any addition is a plan deviation requiring human approval |
| **`bool` passed where `int` is expected** — the exact defect that reached `CLUSTER-002`'s Slice C | Explicit `isinstance(..., bool)` exclusion at every entry boundary, following `hit_points_and_hit_dice.py` |

### 14.3 Decisions requiring the human project owner

1. **Approve this plan** (`ARCHITECTURE.md` §15.2 step 4).
2. **Confirm `src/rules/currency.py` as a shared primitive** rather than `CHAR-004`-local. The plan recommends shared, on the `character_class.py` precedent; the alternative is defensible and is a placement decision, not a rules one.
3. **Confirm the six-slice boundary and the review-after-each-slice cadence.**

**Nothing else is escalated. No rules question remains open.**

## 15. Gate State

```text
ARCHITECTURE.md SS16   Pre-Code Development Gate   CLEARED (project-wide)
ARCHITECTURE.md SS15.1 five readiness criteria     ALL SATISFIED
ARCHITECTURE.md SS15.2 step 1 inventory            SATISFIED
                       step 2 boundary             SATISFIED  2026-09-14
                       step 3 cards APPROVED       SATISFIED  2026-09-24
                       step 4 implementation
                              readiness            NOT GIVEN

CLUSTER-003 Pre-Code Gate                          PASS  2026-09-24
    caution 1  CHAR-005 SS7          -> NOT V1-WIRED (SS8 of this plan)
    caution 2  level input           -> RESOLVED by amendment 2026-09-25
    caution 3  currency              -> RESOLVED by SS5.1/SS6.1

CLUSTER-003 IMPLEMENTATION                         NOT AUTHORIZED
```

## 16. Implementation-Readiness Assessment

**This plan is complete and internally consistent for the approved three-card scope.** All three Pre-Code cautions are dispositioned: one deferred with a demonstrated precedent, one closed by approved amendment, one closed by a representation decision that changes no rule.

**Implementation may not begin on the strength of this document.** It requires the human project owner's §15.2 step-4 implementation-readiness re-approval, given after review of this plan.

## 17. Human Implementation-Plan Review

- Reviewed by: `<pending>`
- Date: `<pending>`
- Result: `<pending>`
- Notes: `<pending>`
