# Inventory Migration Map: 1974-Primary → Rules Cyclopedia-Primary

This is a migration aid, not rules authority. It maps every entry in the retired 1974-primary inventory (preserved in Git history and summarized in `docs/rules/RULESET_BASELINE_MIGRATION.md`) to its disposition in the rebuilt `docs/rules/INVENTORY.md`. Nothing here approves, resolves, or implements anything.

## Disposition Legend

- **RETAIN/REVALIDATE** — the same fundamental rules responsibility exists under RC; ID reserved for revalidation, content not yet re-researched.
- **REFRAME** — the same broad responsibility exists, but RC changes its scope enough that the description materially changes; ID preserved.
- **SPLIT CANDIDATE** — RC research is expected to reveal multiple distinct responsibilities previously grouped together; not split yet.
- **MERGE CANDIDATE** — RC is expected to consolidate previously separated concepts; not merged yet.
- **RETIRE/HISTORICAL** — the old responsibility no longer belongs in active RC V1 scope; ID not reused.
- *(New entries with no old predecessor are listed separately at the end.)*

## Domain: `character_creation` (CHAR)

| Old ID | Old Title | Disposition | New/Current Entry | Reason |
|---|---|---|---|---|
| `CHAR-001` | Ability Score Generation | RETAIN/REVALIDATE | `CHAR-001` | Same responsibility; RC's own generation method(s) not yet confirmed identical to 1974's straight 3d6. |
| `CHAR-002` | Race & Class Eligibility | REFRAME | `CHAR-002` | RC's roster (4 human classes including Thief + 3 demi-human race-classes, plus optional branches) materially exceeds the old three-book/four-race scope. |
| `CHAR-003` | Starting Hit Points & Base Saving Throws | SPLIT CANDIDATE | `CHAR-003` (HP/HD only) + `COMBAT-004` (saves) | The saving-throw half is better owned by `COMBAT-004`'s full class/level table (already the old inventory's stated dependency direction); this migration narrows `CHAR-003` accordingly rather than duplicating saves in two places. |
| `CHAR-004` | Starting Equipment & Expedition Preparation | RETAIN/REVALIDATE | `CHAR-004` | Same responsibility. |
| `CHAR-005` | Encumbrance & Movement Rate | RETAIN/REVALIDATE | `CHAR-005` | Same responsibility; `CLUSTER-001`'s prior treatment of this as a stable external contract is expected to still hold conceptually. |
| `CHAR-006` | Retainers & Hirelings | RETAIN/REVALIDATE | `CHAR-006` | Same responsibility. |
| `CHAR-007` | Ability Score Mechanical Effects & Cross-System Dependencies | RETAIN/REVALIDATE | `CHAR-007` | Same responsibility; RC's specific modifier table is expected to differ numerically. |
| `CHAR-008` | Alignment & Languages | REFRAME | `CHAR-008` | RC's three-axis alignment is corroborated as more mechanically integrated (Cleric/Druid spellcasting) than the thinner 1974 treatment. |
| `CHAR-009` | Class Special Abilities & Racial Abilities/Limitations | REFRAME | `CHAR-009` | Materially larger catalog under RC; Thief abilities specifically split out (see below) given their size and distinct mechanic. |

## Domain: `exploration` (EXP)

| Old ID | Old Title | Disposition | New/Current Entry | Reason |
|---|---|---|---|---|
| `EXP-001` | Dungeon Wandering-Monster Check | RETAIN/REVALIDATE (not revalidated this task) | `EXP-001` | Existing `REVALIDATION_REQUIRED` Rule Card stays as-is; see "Treatment of Existing Rule Cards" below for the cadence-uncertainty finding. |
| `EXP-002` | Dungeon Turn / Time Accounting | RETAIN/REVALIDATE (not revalidated this task) | `EXP-002` | Existing `REVALIDATION_REQUIRED` Rule Card stays as-is; turn/move conventions expected largely preserved. |
| `EXP-003` | Dungeon Movement, Mapping & Special Terrain | RETAIN/REVALIDATE | `EXP-003` | Same responsibility. |
| `EXP-004` | Resting Procedure | RETAIN/REVALIDATE (not revalidated this task), **flagged possibly MATERIALLY CHANGED or OBSOLETE** | `EXP-004` | Existing `REVALIDATION_REQUIRED` Rule Card stays as-is; secondary-source research suggests the mandatory-rest rule may not exist in BECMI/RC's default rules at all — see "Treatment of Existing Rule Cards" below. |
| `EXP-005` | Searching, Listening, Doors & Secret Features | RETAIN/REVALIDATE | `EXP-005` | Same responsibility; still a plausible future split candidate, unchanged assessment. |
| `EXP-006` | Light & Exploration Resources | RETAIN/REVALIDATE | `EXP-006` | Same responsibility. |
| `EXP-007` | Traps — trigger mechanic only | RETAIN/REVALIDATE | `EXP-007` | Same responsibility; the old `EXP-005`/`EXP-007` overlap question remains unresolved, carried forward explicitly rather than silently fixed (out of scope for this task, as previously flagged). |
| `EXP-008` | Dungeon Stocking | RETAIN/REVALIDATE | `EXP-008` | Same responsibility. |
| `EXP-009` (already retired → `SIM-001`) | Dungeon Generation / Map Authoring | RETIRE/HISTORICAL (already retired before this migration) | `SIM-001` | No change from the prior retirement; `SIM-001` itself is reassessed, not this retired ID. |
| `EXP-010` | Party Formation & Marching Order | RETAIN/REVALIDATE | `EXP-010` | Same responsibility. |

## Domain: `encounters` (ENC)

| Old ID | Old Title | Disposition | New/Current Entry | Reason |
|---|---|---|---|---|
| `ENC-001` | Encounter Distance | RETAIN/REVALIDATE | `ENC-001` | Same responsibility; specific roll/formula not assumed carried over. |
| `ENC-002` | Surprise | RETAIN/REVALIDATE | `ENC-002` | Same responsibility. |
| `ENC-003` | Reaction | RETAIN/REVALIDATE, **risk resolved** | `ENC-003` | Same responsibility; the old "unresearched, not located" risk is expected to disappear entirely, since RC is a single consolidated volume rather than a not-yet-retrieved second/third booklet. |
| `ENC-004` | Monster Morale | RETAIN/REVALIDATE, **risk resolved** | `ENC-004` | Same reasoning as `ENC-003`. |
| `ENC-005` | Retreat, Pursuit & Evasion (underworld) | RETAIN/REVALIDATE | `ENC-005` | Same responsibility; underworld-vs-wilderness distinction carried forward as an open question, not assumed resolved. |
| `ENC-006` | Non-Combat Resolution / Parley | RETAIN/REVALIDATE | `ENC-006` | Same responsibility and same "may be thin" uncertainty. |

## Domain: `monsters` (MON)

| Old ID | Old Title | Disposition | New/Current Entry | Reason |
|---|---|---|---|---|
| `MON-001` | Monster Determination & Level Matrix | RETAIN/REVALIDATE | `MON-001` | Same responsibility; loses its prior "table located, untranscribed" head start since that table was 1974-specific. |
| `MON-002` | Number Appearing | RETAIN/REVALIDATE, **MERGE CANDIDATE flagged** | `MON-002` | Likely folded directly into each monster's own stat block under RC rather than a standalone table — a plausible future merge into `MON-003`, not executed here. |
| `MON-003` | General Monster Statistics (core roster) | RETAIN/REVALIDATE | `MON-003` | Same responsibility, explicitly reframed as a catalog-closure entry per this task's structural requirement. |
| `MON-004` | Monster Special Abilities (v1-reachable) | RETAIN/REVALIDATE | `MON-004` | Same responsibility, catalog-closure. |

## Domain: `combat` (COMBAT)

| Old ID | Old Title | Disposition | New/Current Entry | Reason |
|---|---|---|---|---|
| `COMBAT-001` | Combat System Selection | REFRAME | `COMBAT-001` | RC has one unified system — the *selection* question this ID tracked no longer exists; the ID is repurposed to describe that single system instead of retired, since the underlying "what determines to-hit" responsibility persists. |
| `COMBAT-002` | Attack Resolution, Armor Class & To-Hit | RETAIN/REVALIDATE, **unblocked** | `COMBAT-002` | Same responsibility; no longer gated behind an unresolved foundational fork. |
| `COMBAT-003` | Damage & Death | REFRAME | `COMBAT-003` | Confirmed material change — per-weapon damage dice, not universal 1d6 (`DEC-0007`'s own motivating example). |
| `COMBAT-004` | Saving Throws | RETAIN/REVALIDATE | `COMBAT-004` | Same responsibility; now also absorbs `CHAR-003`'s old saving-throw half (see `CHAR-003` above). Five-category structure corroborated. |
| `COMBAT-005` | Healing & Natural Recovery | RETAIN/REVALIDATE | `COMBAT-005` | Same responsibility. |
| `COMBAT-006` | Combat Sequence, Initiative & Timing | RETAIN/REVALIDATE, **risk reduced** | `COMBAT-006` | Same responsibility; a corroborated single default sequence plus a labeled optional variant replaces the old *Chainmail*-relationship ambiguity. |

## Domain: `magic` (MAGIC)

| Old ID | Old Title | Disposition | New/Current Entry | Reason |
|---|---|---|---|---|
| `MAGIC-001` | Spell Preparation & Memorization | RETAIN/REVALIDATE | `MAGIC-001` | Same responsibility. |
| `MAGIC-002` | Spellcasting Procedure | RETAIN/REVALIDATE | `MAGIC-002` | Same responsibility. |
| `MAGIC-003+` | Individual Spell Effects (grouped by class + level) | SPLIT CANDIDATE, executed narrowly | `MAGIC-003+` (Magic-User) + `MAGIC-005` (Cleric, new ID) | The old grouping nominally covered both classes' spells together; split here because Magic-User and Cleric spell catalogs are historically and mechanically distinct lists of comparable size, each independently a large catalog-closure effort. |
| `MAGIC-004` | Cleric Turn Undead | RETAIN/REVALIDATE | `MAGIC-004` | Same responsibility. |

## Domain: `treasure` (TREAS)

| Old ID | Old Title | Disposition | New/Current Entry | Reason |
|---|---|---|---|---|
| `TREAS-001` | Treasure Type Generation by Dungeon Level | RETAIN/REVALIDATE | `TREAS-001` | Same responsibility; loses its prior "already transcribed" head start, since that table was 1974-specific. |
| `TREAS-002` | Gem/Jewelry/Coin Value Determination | RETAIN/REVALIDATE | `TREAS-002` | Same responsibility. |
| `TREAS-003` | Magic Item Generation, Catalog & Effects | RETAIN/REVALIDATE | `TREAS-003` | Same responsibility, catalog-closure. |
| `TREAS-004` | Magic-Item Use: Activation, Restrictions, Identification & Curses | RETAIN/REVALIDATE | `TREAS-004` | Same responsibility. |

## Domain: `advancement` (ADV)

| Old ID | Old Title | Disposition | New/Current Entry | Reason |
|---|---|---|---|---|
| `ADV-001` | Experience Point Awards | RETAIN/REVALIDATE | `ADV-001` | Same responsibility; treasure-based XP tradition expected to continue. |
| `ADV-002` | Level Advancement & Titles | RETAIN/REVALIDATE, **scope expanded, one sub-concern removed** | `ADV-002` | Progression now spans level 1–36 (see "Progression-Scope Findings" in `INVENTORY.md`); the mandatory-training sub-procedure a naive AD&D-informed reading might expect does not appear to exist in this lineage, simplifying rather than complicating this entry. |

## Simulator Specifications

| Old ID | Old Title | Disposition | New/Current Entry | Reason |
|---|---|---|---|---|
| `SIM-001` | Procedural Dungeon Generation / Map Authoring | RETAIN, reassessed | `SIM-001` | Whether RC supplies complete executable generation guidance could not be confirmed this pass — retained pending verification, not silently dropped or silently kept unchanged. |
| `SIM-002` | V1 Survivability Policy Specification | RETAIN, unchanged | `SIM-002` | Source-baseline-independent by design; no change in nature. |

## New Rules Cyclopedia V1 Entries With No Old-Inventory Predecessor

| New ID | Title | Why It's New |
|---|---|---|
| `CHAR-010` | Thief Skills | The Thief was excluded from v1 core under the now-superseded `DEC-0006`; now a core class under `DEC-0007`, with its own sizable percentage-table mechanic distinct enough from `CHAR-009`'s general class-ability grouping to warrant its own entry. |
| `CHAR-011` | Weapon Mastery | RC-specific optional system with no 1974 analog at all. |
| `CHAR-012` | General Skills | RC-specific optional system with no 1974 analog at all. |
| `CHAR-013` | Optional/High-Level Class Branches (Druid, Mystic, Paladin/Avenger, etc.) | RC-specific optional/high-level content; the 1974 core had no equivalent branching-class structure. |
| `COMBAT-007` | Weapon Mastery Combat Effects | Conditional consequence of `CHAR-011`; no 1974 analog. |
| `MAGIC-005` | Individual Spell Effects (Cleric, catalog closure) | Split out of the old `MAGIC-003+` grouping — see disposition above. |
| `MAGIC-006` | Druid Spells (catalog closure) | Conditional consequence of `CHAR-013`'s Druid branch; no 1974 analog (Druid did not exist in the three-book core). |
| `ADV-003` | Between-Expedition Resupply & Town Services | The old inventory did not give the gameplay loop's "recover/resupply" stage its own tracked entry; added for loop-closure completeness. |

## Treatment of Existing Rule Cards (not revalidated this task)

- **`EXP-001` (Dungeon Wandering-Monster Check).** Conceptual responsibility (a dungeon wandering-monster check exists, resolved by 1d6) is **likely preserved** in broad shape. The **exact cadence is uncertain** — the approved-under-the-old-policy specification uses "every turn"; secondary-source research (both this task and `EXP-004`'s own prior drafting) repeatedly surfaced claims that the B/X/BECMI lineage RC compiles uses "every 2 turns" instead. This is the single most consequential open question for this card's eventual revalidation, since it would change `EXP-002`'s integration cadence, not just this card's own die-roll mechanics. Status remains `REVALIDATION_REQUIRED`; not touched further this task.
- **`EXP-002` (Dungeon Turn / Time Accounting).** **Likely preserved** — the 10-minute-turn, two-moves-per-turn convention is corroborated as stable across the entire Basic-lineage including (by extension) RC, and was already independently corroborated during this card's own original research (Holmes and B/X both matched OD&D's figures). Lower revalidation risk than `EXP-001` or `EXP-004`. The shared-ledger/progressive-boundary *accounting model* itself (Simulator Ruling content) does not depend on which source is primary at all and is expected to survive unchanged regardless of what the cadence-number revalidation finds. Status remains `REVALIDATION_REQUIRED`; not touched further this task.
- **`EXP-004` (Resting Procedure).** **Possibly materially changed or obsolete** — this is the most significant single finding of this migration pass regarding the existing cards. Secondary-source research located during this card's own prior drafting found a specific claim that BECMI dropped the mandatory-rest rule ("no specific rules for this kind of resting," with the party instead assumed to take breathers implicitly during ordinary movement). If confirmed true for RC specifically, `EXP-004`'s entire mandatory-rest/overdue/penalty state machine could become either unnecessary (if RC has no equivalent rule at all) or need substantial rework (if RC has a materially different equivalent). This is flagged prominently rather than resolved, per this task's explicit scope limit. Status remains `REVALIDATION_REQUIRED`; not touched further this task.

## Preliminary Assessment of `CLUSTER-001`

`CLUSTER-001`'s old three-item boundary (`EXP-001` + `EXP-002` + `EXP-004`) remains **structurally plausible** as a candidate — all three responsibilities still exist conceptually in the RC-driven inventory, and the dependency shape between them (`EXP-002` supplies `EXP-001`'s signal; `EXP-004` depends on `EXP-002`'s turn definition) is unchanged in the new inventory. However, its exact final membership and internal specification cannot be confirmed stable until: (1) `EXP-001`'s cadence question is resolved (may or may not change the cluster's own integration-test assumptions); (2) `EXP-004`'s possible-obsolescence question is resolved (if `EXP-004` turns out not to correspond to any real RC rule, the cluster could shrink to two items, or gain a different second turn-consuming activity in its place). This is a preliminary, non-binding assessment — formal cluster revalidation or redefinition is explicitly out of scope for this task and remains `CLUSTER-001`'s own `REVALIDATION_REQUIRED` status until a dedicated task addresses it.
