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
| `SIM-001` | Procedural Dungeon Generation / Map Authoring | RETAIN, reassessed, **scope narrowed** | `SIM-001` (Procedural Dungeon **Layout** Generation) | Primary-text review confirms RC permits any layout method but does not supply a complete random map-layout generator — retained, narrowed explicitly to layout only. Canonical stocking/monster/treasure determination, which RC does supply, is **not** owned by this ID (`EXP-008`, `MON-*`, `TREAS-*` instead). |
| `SIM-002` | V1 Survivability Policy Specification | RETAIN, unchanged | `SIM-002` | Source-baseline-independent by design; no change in nature. |

## New Rules Cyclopedia V1 Entries With No Old-Inventory Predecessor

| New ID | Title | Why It's New |
|---|---|---|
| `CHAR-010` | Thief Skills | The Thief was excluded from v1 core under the now-superseded `DEC-0006`; now a core class under `DEC-0007`, with its own sizable percentage-table mechanic distinct enough from `CHAR-009`'s general class-ability grouping to warrant its own entry. |
| `CHAR-011` | Weapon Mastery | RC-specific optional system with no 1974 analog at all. |
| `CHAR-012` | General Skills | RC-specific optional system with no 1974 analog at all. |
| `CHAR-013` | High-Level Class Branches (Paladin/Knight/Avenger — corrected to core/conditional; Druid/Mystic — RC-optional, project-selected required) | RC-specific content; the 1974 core had no equivalent branching-class structure. **Corrected this revision:** Paladin/Knight/Avenger were initially mis-classified alongside Druid/Mystic as an undecided optional subsystem; primary-text review establishes they are core, conditional Fighter-progression content, not opt-in. Flagged as a SPLIT CANDIDATE given this now-confirmed classification difference within one ID. |
| `CHAR-014` | Aging & Character Condition Changes Over Time | Chapter 13 coverage gap identified this revision; no old-inventory or prior-draft predecessor at all. |
| `COMBAT-007` | Weapon Mastery Combat Effects | Conditional consequence of `CHAR-011`; no 1974 analog. Now required, not conditional, per `DEC-0008`. |
| `COMBAT-008` | Nonlethal Combat | Chapter 19 variant, newly required per `DEC-0008`; no 1974 analog and no prior-draft predecessor. |
| `COMBAT-009` | Mortally Wounded / Keeping Characters Alive | Chapter 19 variant, newly required per `DEC-0008`; no 1974 analog and no prior-draft predecessor. |
| `MAGIC-005` | Individual Spell Effects (Cleric, catalog closure) | Split out of the old `MAGIC-003+` grouping — see disposition above. |
| `MAGIC-006` | Individual Spell Effects (Druid, catalog closure) | Conditional consequence of `CHAR-013`'s Druid branch; no 1974 analog (Druid did not exist in the three-book core). Now confirmed required, not conditional, per `DEC-0008`. |
| `ADV-003` | Between-Expedition Resupply & Town Services | The old inventory did not give the gameplay loop's "recover/resupply" stage its own tracked entry; added for loop-closure completeness. |
| `ENC-007` | Encounter Balancing | RC-specific optional evaluative system; no 1974 analog and no prior-draft predecessor. Default OFF per `DEC-0008`. |

## Treatment of Existing Rule Cards (not revalidated this task)

- **`EXP-001` (Dungeon Wandering-Monster Check).** **Disposition corrected this revision: `REFRAME` / MATERIAL REVALIDATION**, not "likely preserved pending cadence verification." Primary-text review establishes the Rules Cyclopedia's procedure as: check every *other* dungeon turn; roll 1d6; on a 1, wandering monsters appear at the *beginning of the next turn* — materially different from the old approved-under-the-superseded-policy specification's "every turn, immediate appearance." Conceptual responsibility (a dungeon wandering-monster check exists, resolved by 1d6) is preserved; the cadence, the specific trigger value, and the timing of the resulting encounter are not. Future revalidation must address, at minimum: the every-other-turn cadence itself; the encounter-on-1 result; appearance at the beginning of the *following* turn rather than immediately; and the resulting implications for its integration with `EXP-002`'s dungeon-time accounting (a check that fires on alternating turns and resolves its consequence one turn later is a materially different integration contract than the old every-turn/immediate model). Status remains `REVALIDATION_REQUIRED`; the Rule Card itself is not rewritten this task.
- **`EXP-002` (Dungeon Turn / Time Accounting).** **Disposition: `RETAIN` / `REVALIDATE`**, unchanged in substance this revision, with a sharpened caveat: the broad ten-minute-turn, two-moves-per-turn responsibility appears to survive (corroborated as stable across the Basic lineage, including this card's own original research matching Holmes and B/X). However, the old accumulator's *every-turn consumer relationship with `EXP-001`* must **not** be assumed correct merely because the turn-length concept is similar — `EXP-001`'s now-confirmed every-other-turn, delayed-appearance cadence means the integration contract between these two cards requires its own direct reassessment during revalidation, not an assumption of continuity. The shared-ledger/progressive-boundary accounting *model* itself (Simulator Ruling content) remains expected to survive regardless, since it does not depend on which source is primary or on `EXP-001`'s specific cadence. Status remains `REVALIDATION_REQUIRED`; not touched further this task.
- **`EXP-004` (Resting Procedure).** **Disposition corrected this revision: `REFRAME`** (with a **`SPLIT CANDIDATE`** flag pending further research), retitled conceptually to "Rest / Exhaustion Procedure." Primary-text review establishes that the old mandatory-hourly-dungeon-rest state machine — the 5-qualifying-turns cadence, the `rest_overdue`/B/X-derived overdue penalty, and the associated non-stacking-debt bookkeeping — is **not** current RC-authoritative mechanics; ordinary dungeon movement/time already incorporates reasonable resting behavior without a separate mandatory state machine of that shape. The Rules Cyclopedia instead has at least two distinct, RC-native fatigue/rest concepts not to be conflated with each other or with the old mechanic: running exhaustion (a limit on sustained running, requiring rest before a character may run/fight normally again), and a separate wilderness/long-distance-travel rest procedure carrying its own cumulative consequences if ignored. Whether these two RC-native concepts are best represented as one reframed Rule Card or split into a short-term dungeon/exertion entry and a distinct wilderness-travel entry is flagged as a `SPLIT CANDIDATE` for future research, not resolved here. The old Rule Card's historical research and prior human approval record remain preserved and are not deleted; they simply do not govern RC play. Status remains `REVALIDATION_REQUIRED`; not touched further this task.

## Preliminary Assessment of `CLUSTER-001`

**Revised this pass: no longer described as "structurally plausible" without qualification.** `CLUSTER-001`'s old three-item boundary (`EXP-001` + `EXP-002` + `EXP-004`) is now **genuinely uncertain**, not merely pending verification of an open question. Three specific reasons: (1) `EXP-001` is now confirmed materially changed (cadence and timing), which may change what `EXP-002` actually needs to supply it and when; (2) `EXP-004` may be substantially reframed (from a mandatory dungeon-rest state machine to RC-native running-exhaustion and/or wilderness-travel-rest concepts) or even split into two responsibilities, either of which could change whether it belongs in the same cluster as `EXP-001`/`EXP-002` at all, belongs in a different grouping (e.g., alongside wilderness-scale procedures), or needs a different turn-consuming activity in its place to fulfill the old cluster's original purpose of demonstrating the turn counter driven by more than one activity type; (3) the dependency relationship between all three may therefore differ from the old boundary in ways not yet knowable without dedicated revalidation. `CLUSTER-001` remains `REVALIDATION_REQUIRED` and is **not redefined** by this task. Later cluster selection must be re-derived from the approved RC inventory once it reaches that state — the old three-item grouping should not be assumed to survive intact, and should not be used as a starting template without first re-deriving cluster boundaries from the (by-then-approved) inventory's own dependency graph.
