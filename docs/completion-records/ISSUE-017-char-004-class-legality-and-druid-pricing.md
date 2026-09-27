# ISSUE-017: CHAR-004 Class Legality & Druid Pricing (CLUSTER-003 Slice C)

## 1. Issue/Task Identifier and Objective

ISSUE-017 (completion-record ledger). Implement **Slice C** of
`docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §10: per-class mundane
equipment legality for all nine classes, and the Druid's `+50%` surcharge
for commissioned all-wooden weapons.

`CHAR-004` is now complete. **No movement code exists**, and `CHAR-005`,
`EXP-003`, `CHAR-009`, `CHAR-010` and `TREAS-004` are untouched.

**Status: awaiting human review.** Slice D is not started.

## 2. Approved Inputs/Specifications

- `docs/rules/character_creation/starting_equipment_and_expedition_preparation.md`
  §5 and §7 (`CHAR-004`, `APPROVED` 2026-09-24, amended 2026-09-26 and
  2026-09-27), carrying **`SR-7`**.
- `docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §5.5, §6.2, §6.5, §10
  (Slice C).
- Human authorization of 2026-09-27, scoped to §5, §7, cases `E26`–`E52`,
  `SR-7`, `is_legal`, `purchase_cost` and `EquipmentLegalityError`.
- Human governance decision of 2026-09-14 — `CHAR-004` is the **canonical
  owner** of equipment-facing class restrictions; `CHAR-009` must not
  become a second implementation owner.
- RC Ch. 4 pp. 62–63 (Weapons Table notes `c` and `w`), p. 65 (Nets Table),
  p. 67 (armour prose).

## 3. Files Created, Modified, or Deleted

**Created:** this completion record.

**Modified:**

- `src/rules/character_creation/equipment.py` — the §7 section.
- `src/rules/character_creation/errors.py` — `EquipmentLegalityError`.
- `tests/rules/character_creation/test_equipment.py` — `E26`–`E52`.
- `docs/completion-records/INDEX.md` — index row.

**Deleted:** none.

Committed on `cluster-003-stage-a-evidence`. **Not merged.**

## 4. Behavior Actually Implemented

### `is_legal(cls, item, *, magic_user_expanded_list=False) -> bool`

One predicate over one table (plan §5.5), not a per-class hierarchy. It
answers the question and never raises on a "no".

| Class | Armour / shield | Weapons |
|---|---|---|
| Cleric | any; shield | note `c` — RC's printed form of "no edged or pointed" |
| Fighter | any; shield | any |
| Magic-User | none | **dagger unconditionally (`SR-7`)**; note `w` only with the flag ON |
| Thief | leather only, no shield | missile, or not `2H` |
| Dwarf | any; shield | Small/Medium melee; short bow and both crossbows |
| Elf | any; shield | any |
| Halfling | any, **halfling-made** | Small melee; short bow; light crossbow; nets ≤ 6' |
| Druid | leather; wood-and-leather shield | note `c` **and** all-wooden |
| Mystic | **none, ever** | any |

Ammunition is accepted as an argument because §7's cleric prohibition names
it: arrows and quarrels are refused, sling stones are not. Gear, containers
and clothing are legal for every class — §7 restricts weapons, armour and
shields, and inventing more would be a silent rules decision.

### `purchase_cost(cls, item, *, magic_user_expanded_list=False) -> Coin`

Card §5 step 3 rejects an item not legal for the class **before** cost is
summed, so an illegal item raises `EquipmentLegalityError` rather than
returning a number a caller might spend.

The Druid's `+50%` applies to a commissioned all-wooden **weapon** and
nothing else, and is class-specific. Applied as the exact ratio `3/2`
through `Coin.scaled`, so a 3 gp club is `300 x 3 / 2 = 450 cp` — `4.5 gp`,
no float, no rounding.

### Two derived-item constructors

`commissioned(item, material)` and `made_for(item, race)` express two
qualifiers RC states for particular items rather than tabulating: note `c`'s
*"a form of this weapon with no metal or stone parts"*, and p. 67's *"armor
is normally made for a specific race"*. They follow the `net()`/`whip()`
pattern — a derived item, not a flag on the printed row.

## 5. Rules Provenance

| Element | Classification |
|---|---|
| Every §7 class restriction except the Magic-User dagger's conditionality | **Rules Cyclopedia Explicit** |
| Magic-User dagger unconditional; note `w` defective as to the dagger | **Simulator Ruling `SR-7`** (pre-existing) |
| Druid `+50%` as the exact ratio `3/2` | **Necessary Mathematical-Mechanical Consequence** of §7's "+50%" |
| A printed row is not assumed to be an all-wooden form, nor to fit a halfling | **Conservative reading**, §10.1 below |

**No new Simulator Ruling. No Compatible Completion. No Variant.**

## 6. Tests Added or Modified

Approved cases `E26`–`E52`, with case IDs in docstrings and `parametrize`
ids. `E26` + `E36` + `E37` together prove `SR-7`: the dagger is legal with
the flag both ON and OFF, while a staff is legal only with it ON. `E48`
parametrizes over every armour row.

Two Slice-B guard tests were **retired**, because Slice C is what they
guarded against: `test_slice_b_exposes_no_class_legality_or_druid_pricing`
and `test_slice_b_imports_no_character_class`. They are replaced by guards
for the boundaries that still hold — no movement symbol, no magic-item or
thief-skill behaviour, and `CharacterClass` used for legality and nothing
else.

## 7. Exact Verification Commands Executed

```text
uv run python scripts/verify.py
```

## 8. Verification Results

```text
Tests:     PASS   741 passed
Coverage:  PASS
Ruff:      PASS
mypy:      PASS
Overall:   PASS
```

## 9. Coverage Results

`src/rules/character_creation/equipment.py` — **100% branch, 0 missed**.
All 16 files under `src/rules/` at 100% branch per file.

## 10. Deviations

1. **`is_legal` accepts `Item | Ammunition`.** The authorized signature
   named `item`; `E39` requires a cleric to be refused *arrows*, which are
   an `Ammunition` and not an `Item`. The widening is the minimum `E39`
   needs.
2. **`purchase_cost` takes the policy flag too.** It must call `is_legal`
   to honour §5 step 3, and would otherwise silently price a staff as
   illegal for a Magic-User whose campaign permits it.
3. **Three optional fields added to `Item`** — `dimension_feet`,
   `material`, `made_for_race` — each because a §7 rule turns on it
   (`E47`, `E49`, `E46`). Nothing sets them but the constructor that owns
   them.
4. **Two derived-item constructors added**, not in the plan's §6.2 sketch.
   Without them `E49` and `E46` are unimplementable: RC tabulates neither
   per-row metal content nor per-row racial fit.

### 10.1 The one interpretive choice, stated plainly

**A printed catalog row is not assumed to be a druid-legal wooden form, nor
to fit a halfling.** `is_legal(DRUID, Mace)` is `False` and
`is_legal(HALFLING, Chain Mail)` is `False`; the commissioned and
halfling-made forms are legal.

This follows note `c`'s own conditional — druids may use these weapons *"if
they can find a form … with no metal or stone parts"* — and §7's pricing
rule, which exists precisely because the druid's weapons are commissioned.
It satisfies `E49` (a metal-headed mace is refused) and `E46` (dwarf-made
armour is refused), and no approved case constrains the unqualified row.

**It is a reading, not a transcription**, and is offered for correction.
The alternative — treating a printed row as legal until proven otherwise —
would fail `E49` unless RC's per-row metal content were invented, which it
does not state for any of the 40 weapon rows.

## 11. Known Limitations/Unresolved Issues

Two §7 boundaries were found and **deliberately not decided**; both are
recorded in the module and pinned by
`test_two_section_7_boundaries_are_left_undecided_and_are_recorded`.

- **A thief with a large net.** RC p. 65 makes a net's handedness depend on
  its size, but §7's thief prohibition is stated over the printed `2H`
  marker, which no net row carries. `is_legal` permits it. No approved case
  covers it.
- **A dual-role item used as a weapon.** The torch is printed in both the
  Weapons Table and the Adventuring Gear Table and is one commodity here,
  catalogued as `GEAR`, so §7's weapon restrictions do not reach it and
  every class may carry one. Plainly right for a light source; unaddressed
  by the card for a torch swung in anger.

Carried forward unchanged from Slice B: the net's `M or L` size
disjunction; bundle-row lookup names; Chapter 10 `NOT V1-WIRED`; mounts,
vehicles, ships and siege out of V1.

## 12. Architectural Consequences

No new architectural style. `equipment.py` now imports `CharacterClass`,
which Slice C required and Slice B deliberately avoided; a guard test
asserts it is used for legality only and that no Hit Die, prime requisite,
level or advancement data is attached to it — `character_class.py`'s own
docstring reserves those for other cards.

The dependency graph stays acyclic and one-directional: `equipment` imports
`rng`, `currency` and `character_class`, and nothing from `exploration`.
`CHAR-004` is complete and `src/` still contains no movement code.
