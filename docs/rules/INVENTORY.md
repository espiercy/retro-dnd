# V1 Rules Inventory and Dependency Map (Rules Cyclopedia)

**Status: APPROVED** — human-approved 2026-08-16 (commit `c6e843f`). This is a scoping/backlog document, not a Rule Card — it does not resolve any individual mechanic, and nothing below may authorize implementation (`ARCHITECTURE.md` §15.2's migration gate remains in force regardless of this document's own status). It supersedes the prior inventory's active framing; the prior, 1974-primary inventory remains available through Git history and is not duplicated here — see `docs/rules/RULESET_BASELINE_MIGRATION.md` for that history and `docs/rules/INVENTORY_MIGRATION_MAP.md` for the row-by-row disposition of every entry the prior inventory contained.

Approval of this inventory authorizes cluster (re-)selection to proceed against it, per `ARCHITECTURE.md` §15.1/§15.2 — it does not itself select or define a cluster, revalidate any Rule Card, or reauthorize historical-rules implementation, each of which remains a separate, explicitly authorized future task. This revision incorporates primary-text corrections and explicit V1 rules-profile decisions from human review of the first draft (commit `dde84ee`) — see `docs/decisions/DEC-0008-rules-cyclopedia-v1-rules-profile.md` for the durable record of the selections applied throughout this document.

## Source and Method

Driven by the *Dungeons & Dragons Rules Cyclopedia* (TSR 1071, 1991) as primary authority (`DEC-0007`, `SOURCE_HIERARCHY.md`). This revision incorporates corrections from the human project owner's own direct primary-text review, layered on top of this project's earlier chapter/section-level secondary-source corroboration (`docs/rules/RC_V1_SCOPE_AUDIT.md` — see its "Verification Method" section for exactly which findings in this document rest on which evidentiary basis). This remains a deliberately broad, shallow pass — identify and classify, not resolve — see the assigning tasks for the full scope boundary.

**V1 gameplay loop** (unchanged — reachability root, not itself RC-specific):

```text
Create / maintain party
        ↓
Prepare and equip expedition
        ↓
Enter dungeon
        ↓
Explore under dungeon procedures
        ↓
Encounter monsters / traps / features
        ↓
Negotiate / evade / fight / otherwise resolve
        ↓
Find and recover treasure
        ↓
Exit dungeon
        ↓
Award XP / advance / recover / resupply
        ↓
Begin another expedition
```

**V1 progression scope (corrected this revision).** V1 supports the **full standard Rules Cyclopedia progression for each included class** — not a flat "levels 1–36 for everything." This includes, per class: conventional advancement to level 36 for the four human classes (Cleric, Fighter, Magic-User, Thief); each demihuman race-class's own lower level cap followed by Attack Rank progression (Dwarf, Elf, Halfling); and the Mystic's own level cap and progression structure. See "Progression-Scope Findings" below for what this corrects from the prior draft's oversimplified statement, and `docs/decisions/DEC-0008-rules-cyclopedia-v1-rules-profile.md` for the standard-vs-extended-progression selection.

**Playable-content boundary.** Rules Cyclopedia content reachable through the V1 loop above, completed by alternate non-AD&D D&D sources only where RC itself is silent or ambiguous (`SOURCE_HIERARCHY.md` §3), plus the explicit RC-optional systems selected as required V1 content by `DEC-0008` (Morale, Weapon Mastery, General Skills, Druid, Mystic, and three Chapter 19 variants).

## Vocabulary

Three distinct concepts, used consistently throughout this document (do not conflate them):

- **RC Core** — part of the Rules Cyclopedia's own default rules; no selection decision needed.
- **RC Optional / Variant** — a rule the Rules Cyclopedia itself explicitly presents as DM-choice, additional, or variant content.
- **Project-Selected RC Option** — an RC Optional/Variant rule the human project owner has chosen as part of this simulator's authoritative V1 configuration (`DEC-0008`). **This is not a Human-Approved Variant** (`SOURCE_HIERARCHY.md` §7) — it selects among options RC itself sanctions; it does not contradict or replace any RC rule. A Human-Approved Variant remains reserved for an actual deliberate departure from an explicit RC rule, which no decision in this document constitutes.

## How to Read This Table

| Column | Meaning |
|---|---|
| ID | Domain-prefixed Rule ID/grouping. Existing IDs are reused where the underlying rules responsibility survives conceptually (`INVENTORY_MIGRATION_MAP.md`); new IDs continue each domain's existing numbering, preserving gaps left by retired IDs. |
| Title | Working title under the current RC understanding of the responsibility. |
| RC Source | Chapter/section believed to contain this material, per `RC_V1_SCOPE_AUDIT.md`. Citation confidence varies by entry — see that document. |
| RC Classification / Project Selection | Per the Vocabulary above — `RC Core`, or `RC Optional → Project-Selected: REQUIRED/NOT ENABLED`, or `RC Optional Ch.19 variant → Project-Selected: ...`. |
| Dependencies | Other inventory items this one needs resolved first. |
| Downstream Consumers | Other inventory items that depend on this one. |
| V1 Reachable | Whether this is reachable through the loop above, given the Project Selections in force. |
| Status | Lifecycle status of the *inventory entry itself* — none of these are researched Rule Cards yet. |
| Risk / Notes | Ambiguity/research risk, catalog-closure requirement where applicable, and legacy-mapping pointer. |

---

## ⚠ Major Research-Risk Flags and Corrected Findings (read first)

1. **`EXP-001` was materially changed, not merely uncertain.** Primary-text review established the Rules Cyclopedia's dungeon wandering-monster procedure as: check every *other* dungeon turn; roll 1d6; on a 1, wandering monsters appear at the *beginning of the next turn* (not immediately). This differs from the old 1974-derived Rule Card's "every turn, immediate appearance" specification in both cadence and timing. **Revalidation has since completed: `EXP-001` is now `APPROVED`** (human-approved 2026-08-18, including Simulator Rulings A–C) — see `docs/rules/exploration/dungeon_wandering_monster_check.md` for the authoritative specification.
2. **`EXP-004`'s old mandatory-hourly-rest state machine does not appear to survive as RC canon.** Primary-text review indicates RC's dungeon-time/movement handling already incorporates ordinary resting behavior, rather than a separate one-turn-in-six mandatory state machine with overdue penalties. RC instead has distinct fatigue/rest concepts — running exhaustion, and a separate long-distance-travel rest procedure with its own cumulative consequences — that must not be conflated with the old OD&D-derived mechanic. `EXP-004` remains `REVALIDATION_REQUIRED`, reframed around RC's actual rest/exhaustion responsibility — see below and `INVENTORY_MIGRATION_MAP.md`.
3. **Five RC-optional systems are now required V1 content by explicit human decision** (`DEC-0008`): Morale, Weapon Mastery, General Skills, Druid, Mystic. Three Chapter 19 variants are also required: Nonlethal Combat, Ability-Based Saving Throws, Mortally Wounded/Keeping Characters Alive. Two Chapter 19 variants are explicitly declined for V1: Permanent Death, and extended demihuman/Mystic progression (the latter kept open as a future variant candidate). None of this is undecided any longer — see "Major Human Decisions Required" for what genuinely remains open.
4. **Paladin, Knight, and Avenger are corrected from "optional subsystem" to core, conditional high-level Fighter progression** — not equivalent to Druid/Mystic's opt-in status. See `CHAR-013`.
5. **Immortality (Chapter 15) exists in the Rules Cyclopedia** (the prior draft incorrectly suggested this material was absent) and is explicit **future required project scope, outside V1** — not excluded from the intended final product, only deferred. See "Future Scope: Immortality" below.
6. **`COMBAT-003` (Damage & Death) remains a confirmed, foundational, material change** from the prior baseline — per-weapon damage dice, not 1974's universal 1d6 (`DEC-0007`'s own motivating example). Unchanged from the prior draft.
7. **`SIM-001`'s scope is corrected and narrowed.** RC permits dungeon layout to be designed by any method but does not supply a complete random map-layout generator — `SIM-001` remains a required Simulator Specification for *layout generation specifically*. It does **not** own canonical stocking/monster/treasure determination, which RC does supply as historical rules (`EXP-008`, `MON-*`, `TREAS-*`) — the prior draft's wording risked blurring this boundary.
8. **Chapter 13 contains V1-relevant DM procedures not adequately covered in the first pass** — ability checks, doors, listening, special character conditions, thief-skill resolution, aging, and alignment change. Mapped to existing and one new entry below; see "Chapter 13 Coverage."

---

## Domain: `character_creation` (CHAR)

| ID | Title | RC Source | RC Classification / Project Selection | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `CHAR-001` | Ability Score Generation | Character Creation, Ch. 1 | RC Core | — | `CHAR-002`, `CHAR-007` | Yes | Unresearched | Low. |
| `CHAR-002` | Race & Class Eligibility | Character Creation, Ch. 2 | RC Core (Cleric, Fighter, Magic-User, Thief, Dwarf, Elf, Halfling); Druid/Mystic tracked separately at `CHAR-013` | `CHAR-001` | `CHAR-009`, `CHAR-010`, `MAGIC-*`, `COMBAT-*` | Yes | Unresearched | Medium. |
| `CHAR-003` | Hit Points & Hit Dice (starting and per-level) | Character Creation / Combat | RC Core | `CHAR-002` | `COMBAT-003`, `COMBAT-005` | Yes | Unresearched | Medium. Saving-throw content owned by `COMBAT-004`, not duplicated here. |
| `CHAR-004` | Starting Equipment & Expedition Preparation | Character Creation / Equipment | RC Core | `CHAR-001`–`CHAR-003` | `EXP-005`, `EXP-006`, `COMBAT-002`/`COMBAT-003` | Yes | Unresearched | Low-medium. |
| `CHAR-005` | Encumbrance & Movement Rate | Character Creation / Combat Movement | RC Core | `CHAR-004` | `EXP-003` | Yes | Unresearched | Medium. |
| `CHAR-006` | Retainers & Hirelings | Nonplayer Characters / Specialists | RC Core | `CHAR-004` | — | Yes | Unresearched | Low-medium. |
| `CHAR-007` | Ability Score Mechanical Effects & Cross-System Dependencies | Character Creation, Ch. 1; Chapter 13 (ability-check procedure) | RC Core; the *specific ability-modifier-to-saving-throw* mapping is a **Project-Selected RC Option** (Chapter 19 Ability-Based Saving Throws, `DEC-0008`: REQUIRED) | `CHAR-001` | `CHAR-006`, `ENC-003`, `CHAR-008`, `COMBAT-004` (ability-based save adjustments), `CHAR-012` (General Skills reuses the same ability-check resolution) | Yes | Unresearched | Medium-high — now must cover both the standard ability-score-effects table *and* the selected Chapter 19 save-adjustment mapping (which abilities modify which saving-throw categories); the latter is not yet transcribed. |
| `CHAR-008` | Alignment & Languages | Character Creation; Chapter 13 (alignment change procedure) | RC Core | — | `ENC-003`, `CHAR-006`, `CHAR-013` (Paladin/Druid alignment prerequisites), `MON-*`, `MAGIC-*` | Yes, where mechanically relevant | Unresearched | Medium — now explicitly includes Chapter 13's alignment-change-over-play procedure, not just initial selection. |
| `CHAR-009` | Class Special Abilities & Racial Abilities/Limitations (core roster + Mystic) | Character Creation, Ch. 2; Chapter 13 (thief-skill resolution touchpoint) | RC Core | `CHAR-002` | `ADV-002`, `COMBAT-002`, `COMBAT-004`, `MAGIC-*` | Yes | Unresearched | Medium-high — Thief's own abilities are owned by `CHAR-010` instead; Mystic's class abilities and unarmed-combat interactions are in scope here given Mystic's required status (`DEC-0008`). |
| `CHAR-010` | Thief Skills (Open Locks, Find/Remove Traps, Climb Sheer Surfaces, Move Silently, Hide in Shadows, Pick Pockets, Hear Noise) | Character Creation, Ch. 2; Chapter 13 (DM-facing resolution procedure) | RC Core | `CHAR-002`, `CHAR-009` | `EXP-005`, `EXP-007`, `ENC-002`, `COMBAT-002`/`003` (backstab) | Yes | Unresearched | Medium — percentage-by-level table per skill; explicit combat touchpoint (backstab) now flagged alongside the exploration touchpoints already noted; flag likely future splitting if the umbrella card grows unwieldy. |
| `CHAR-011` | Weapon Mastery | "Other Character Abilities" section | RC Optional/Additional system → **Project-Selected: REQUIRED** (`DEC-0008`) | `CHAR-002`, `CHAR-004` | `COMBAT-007` | Yes | Unresearched | **High** — five mastery tiers (Basic/Skilled/Expert/Master/Grand Master), level-gated acquisition, attack/damage/AC bonuses, multiple attacks, and special maneuvers must all achieve full Rule Card coverage; flagged as high research/integration risk given its breadth of effect on combat. Not researched this task. |
| `CHAR-012` | General Skills | "Other Character Abilities" section; Chapter 13 (ability-check procedure, shared mechanic) | RC Optional/Additional system → **Project-Selected: REQUIRED** (`DEC-0008`) | `CHAR-001`, `CHAR-007` (shared ability-check resolution) | — | Yes | Unresearched | Medium-high — skill acquisition/progression procedure, ability-check relationship, and a catalog-closure obligation over the V1-reachable general-skill list; catalog itself not enumerated this task. |
| `CHAR-013` | High-Level Class Branches | Character Creation, Ch. 2 (optional classes); progression material for Fighter sub-paths | **Mixed — see split below** | `CHAR-002`, `CHAR-009`, `CHAR-008` (alignment prerequisites) | `MAGIC-006` (Druid spells) | Yes | Unresearched | **SPLIT CANDIDATE**, not executed this task — see the two distinct sub-groups immediately below. |
| — *(within `CHAR-013`)* | Paladin, Knight, Avenger — high-level Fighter progression paths | Corrected classification | **RC Core / conditional on character progression and alignment** — not an opt-in subsystem | `CHAR-002` (Fighter), `CHAR-008` (alignment) | `COMBAT-002`/`004` (path-specific abilities) | Yes | Unresearched | Corrected this revision — previously mis-classified alongside Druid/Mystic as optional. Future research must cover: when each path becomes available; alignment prerequisites; the land-owning/traveling Fighter choice; resulting abilities/restrictions. |
| — *(within `CHAR-013`)* | Druid, Mystic — optional class paths | Character Creation, Ch. 2 | RC Optional class → **Project-Selected: REQUIRED** (`DEC-0008`) | `CHAR-002` (Cleric, for Druid's prerequisite) | `MAGIC-006` | Yes | Unresearched | Druid requires a Neutral Cleric prerequisite (not yet fully detailed); Mystic uses its own level-cap/progression structure (see "Progression-Scope Findings"). |
| `CHAR-014` | Aging & Character Condition Changes Over Time | Chapter 13 | RC Core | `CHAR-001` (ability-score effects of aging) | — | Yes | Unresearched | Low-medium. **NEW** — Chapter 13 coverage gap identified this revision; natural and magical aging affecting ability scores over the course of play was not tracked at all in the prior draft. |

## Domain: `exploration` (EXP)

| ID | Title | RC Source | RC Classification / Project Selection | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `EXP-001` | Dungeon Wandering-Monster Check | Ch. 7 Encounters and Evasion — Game Turn Checklist; Wandering Monster Encounters | RC Core | RNG abstraction, `EXP-002` | — | Yes | **`APPROVED`** (human-approved 2026-08-18) | Rules Cyclopedia-revalidated and human-approved 2026-08-18; see `docs/rules/exploration/dungeon_wandering_monster_check.md` for the authoritative specification and approved Simulator Rulings A–C. |
| `EXP-002` | Dungeon Turn / Time Accounting | Ch. 6 Movement; Ch. 7 Encounters and Evasion; Ch. 13 Dungeon Master Procedures / Timekeeping | RC Core | — | `EXP-001`, `EXP-003`–`EXP-010`, `EXP-004` | Yes | **`APPROVED`** (human-approved 2026-08-16, including its long-encounter Simulator Ruling) | Low — Rules Cyclopedia-revalidated and approved; see `docs/rules/exploration/dungeon_turn_time_accounting.md` for the full specification (discrete whole-turn credit model; `encounter_turn_cost = max(1, ceiling(encounter_rounds / 60))` for encounters exceeding 60 rounds). |
| `EXP-003` | Dungeon Movement, Mapping & Special Terrain | Dungeon Adventures / Combat Movement | RC Core | `CHAR-005`, `EXP-002` | — | Yes | Unresearched | Medium. |
| `EXP-004` | Rest / Exhaustion Procedure | Dungeon Adventures chapter (running exhaustion); Wilderness Adventures (long-distance travel rest) | RC Core | `EXP-002` | `COMBAT-*` (exertion/fatigue interactions, if any) | Yes | **`REVALIDATION_REQUIRED`** (existing Rule Card, not revalidated this task) | **High, reframed** — the old mandatory-hourly-dungeon-rest state machine (5-qualifying-turns cadence, overdue penalties, non-stacking debt logic) is **not** current RC-authoritative mechanics. RC instead has (a) running-exhaustion limits requiring rest before a character may run/fight normally again, and (b) a distinct wilderness/travel-scale rest procedure with its own cumulative ignored-rest consequences. These must not be conflated with each other or with the old dungeon-rest mechanic. Whether this remains one responsibility or needs to split between a short-term dungeon/exertion entry and the wilderness-travel entry is flagged as a possible **SPLIT CANDIDATE** for future research, not resolved here. |
| `EXP-005` | Searching, Listening, Doors & Secret Features | Dungeon Adventures chapter; Chapter 13 | RC Core | `EXP-002`, `CHAR-010` | — | Yes | Unresearched | Low-medium; still a plausible split candidate. |
| `EXP-006` | Light & Exploration Resources | Dungeon Adventures chapter | RC Core | `EXP-002` | — | Yes | Unresearched | Medium. |
| `EXP-007` | Traps — trigger mechanic | Dungeon Adventures chapter | RC Core (trigger); catalog-closure for effects | `EXP-002`, `CHAR-010` | — | Trigger: yes. Effect catalog: separate, large. | Unresearched | High risk, same split concern and unresolved `EXP-005`/`EXP-007` overlap as before. |
| `EXP-008` | Dungeon Stocking (canonical content/monster/treasure determination) | Dungeon Adventures chapter | RC Core | `MON-001`, `MON-002`, `TREAS-001` | — | Yes | Unresearched | Low-medium. **Scope boundary clarified this revision:** this entry owns RC's canonical random *content/stocking* procedure (what occupies an already-laid-out room); it does not own map/layout generation, which belongs to `SIM-001` alone (Major Research-Risk Flags item 7). |
| `EXP-009` | *(retired — see `SIM-001`)* | — | — | — | — | — | — | ID retired, not reused. |
| `EXP-010` | Party Formation & Marching Order | Dungeon Adventures / Combat | RC Core | `EXP-002`, `EXP-003`, `CHAR-005` | `ENC-002`, `ENC-003`, `COMBAT-006` | Yes | Unresearched | Medium. |

## Domain: `encounters` (ENC)

| ID | Title | RC Source | RC Classification / Project Selection | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `ENC-001` | Encounter Distance | Encounters chapter | RC Core | — | — | Yes | Unresearched | Low-medium. |
| `ENC-002` | Surprise | Encounters chapter | RC Core | `CHAR-010` | `COMBAT-006` | Yes | Unresearched | Low-medium. |
| `ENC-003` | Reaction | Encounters chapter | RC Core | `EXP-001`/`MON-001`, `CHAR-008` | `ENC-006` | Yes | Unresearched | Low — fully present in this single consolidated volume. |
| `ENC-004` | Monster Morale | Encounters / Monsters chapter | RC Optional system → **Project-Selected: REQUIRED, no player toggle** (`DEC-0008`) | `ENC-003`, combat domain | — | Yes | Unresearched | Low — RC presents morale as DM-optional; this project selects it as mandatory V1 behavior, not a configurable option. Must not be mislabeled as mandatory RC canon — it is RC-optional content the project has chosen to require. |
| `ENC-005` | Retreat, Pursuit & Evasion (underworld) | Dungeon Adventures / Encounters | RC Core | `EXP-002`, `EXP-003` | — | Yes | Unresearched | Medium. |
| `ENC-006` | Non-Combat Resolution / Parley | Encounters chapter | RC Core, possibly thin | `ENC-003` | — | Uncertain | Unresearched | Medium. |
| `ENC-007` | Encounter Balancing | Encounters / Monsters chapter (evaluative/adjustment step, distinct from generation) | RC Optional system → **Project-Selected: OFF by default for V1**; conditional future configurability only if low-cost (`DEC-0008`) | `MON-001`, `EXP-001` (consumes canonical generation output; does not replace it) | — | Not reachable while OFF | Unresearched | **NEW.** Must remain conceptually distinct from canonical/random encounter generation — never silently fed into all random encounter output. If later made configurable, it is a clearly selected campaign policy, not a default behavior change. |

## Domain: `monsters` (MON)

| ID | Title | RC Source | RC Classification / Project Selection | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `MON-001` | Monster Determination & Level/Encounter Matrix | Dungeon Adventures / Monsters chapter | RC Core | `EXP-001`, `EXP-008` | `ENC-007` (optional balancing input only) | Yes | Unresearched | Medium. |
| `MON-002` | Number Appearing | Monsters chapter (per-monster stat-block field, expected) | RC Core | `MON-001` | — | Yes | Unresearched | Low-medium — plausible merge candidate into `MON-003`. |
| `MON-003` | General Monster Statistics (catalog closure) | Monsters chapter | RC Core | `MON-001`, `COMBAT-002` | `MON-004`, `TREAS-001` | Yes — full V1-reachable roster, not level-capped | Unresearched | **Catalog-closure entry.** High effort. |
| `MON-004` | Monster Special Abilities & Immunities (catalog closure) | Monsters chapter | RC Core | `MON-003` | — | Yes, scoped to `MON-003` | Unresearched | **Catalog-closure entry.** High effort. |

## Domain: `combat` (COMBAT)

| ID | Title | RC Source | RC Classification / Project Selection | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `COMBAT-001` | Combat System (unified Attack Roll vs. Armor Class) | Combat chapter | RC Core | None, but gates everything below | `COMBAT-002`–`COMBAT-009`, `MON-003` | Yes | Unresearched | Risk resolved — one unified system, no selection fork. |
| `COMBAT-002` | Attack Resolution, Armor Class & To-Hit | Combat chapter | RC Core | `COMBAT-001` | `MON-003`, `CHAR-011` | Yes | Unresearched | Medium — unblocked. |
| `COMBAT-003` | Damage & Death | Combat chapter | RC Core | `COMBAT-001`, `COMBAT-002` | `ADV-001`, `COMBAT-009` | Yes | Unresearched | **High, confirmed material change** — per-weapon damage dice. |
| `COMBAT-004` | Saving Throws | Combat / Character Creation; Chapter 19 (ability-based adjustment) | RC Core (class/level progression); ability-modifier adjustment is a **Project-Selected RC Option** (`DEC-0008`: REQUIRED) | `CHAR-003`, `CHAR-007` (ability-based adjustment mapping) | — | Yes | Unresearched | Medium — five-category structure (Death Ray/Poison, Magic Wands, Paralysis/Stone, Breath Attack, Rod/Staff/Spell) corroborated; must now also specify which ability modifies which category per the selected Chapter 19 variant, not treated as an optional future possibility. |
| `COMBAT-005` | Healing & Natural Recovery | Combat / Recovery section | RC Core | — | `ADV-*`, `COMBAT-009` | Yes | Unresearched | Low. |
| `COMBAT-006` | Combat Sequence, Initiative & Timing | Combat chapter | RC Core (group/side 1d6 initiative, Movement→Missile→Magic→Melee sequence) — **project default**; RC's optional individual-initiative variant (and any dependent Dexterity adjustment) is **Project-Selected: not required for V1**, conditional future configurability only if low-cost (`DEC-0008`) | `COMBAT-001` | — | Yes (group initiative); individual initiative not in V1 scope | Unresearched | Medium — corroborated default sequence; do not architect a toggle for the optional variant now. |
| `COMBAT-007` | Weapon Mastery Combat Effects (attack/damage/AC bonuses, multiple attacks, special maneuvers) | "Other Character Abilities" section, combat-effects portion | RC Optional/Additional system → **Project-Selected: REQUIRED** (`DEC-0008`) | `CHAR-011`, `COMBAT-002`, `COMBAT-003` | — | Yes | Unresearched | High — full effect breadth (attack/damage/AC/maneuvers) must achieve Rule Card coverage; not researched this task. |
| `COMBAT-008` | Nonlethal Combat | Chapter 19 (Variant Rules) | RC Optional Ch. 19 variant → **Project-Selected: REQUIRED** (`DEC-0008`) | `COMBAT-002`, `COMBAT-003` | `COMBAT-009` (recovery interaction) | Yes | Unresearched | Medium-high — full executable procedure (actual vs. nonlethal damage tracking, recovery implications) required for future coverage; not researched this task. **NEW** — given independent visibility rather than folded into `COMBAT-003`, per instruction, so it cannot be silently omitted later. |
| `COMBAT-009` | Mortally Wounded / Keeping Characters Alive | Chapter 19 (Variant Rules) | RC Optional Ch. 19 variant → **Project-Selected: REQUIRED** (`DEC-0008`) | `COMBAT-003`, `COMBAT-005`, `COMBAT-004` (recurring save interaction, if any) | — | Yes | Unresearched | Medium-high — the RC procedure for characters at or below the relevant HP/death threshold, including whatever recurring saving-throw/healing interaction the variant establishes, needs full future specification. **Not** `SIM-002` — this is a selected RC-authored rule, part of the canonical configured ruleset, not a simulator-authored survivability accommodation (though it gives future `SIM-002` design a stronger canonical foundation to build on). **NEW.** |

## Domain: `magic` (MAGIC)

| ID | Title | RC Source | RC Classification / Project Selection | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `MAGIC-001` | Spell Preparation & Memorization | Spells and Spellcasting chapter | RC Core | `CHAR-002` | `MAGIC-002` | Yes | Unresearched | Medium. |
| `MAGIC-002` | Spellcasting Procedure (casting time, interruption) | Spells and Spellcasting chapter | RC Core | `MAGIC-001` | `COMBAT-006` | Yes | Unresearched | Medium. |
| `MAGIC-003+` | Individual Spell Effects (Magic-User, catalog closure) | Spell lists, Spells and Spellcasting chapter | RC Core | `MAGIC-001`, `MAGIC-002` | — | Yes — 9 spell levels, full progression | Unresearched | **Catalog-closure entry.** High effort. |
| `MAGIC-004` | Cleric Turn Undead | Character Creation (Cleric) / Combat | RC Core | `CHAR-002` | — | Yes | Unresearched | Low-medium. |
| `MAGIC-005` | Individual Spell Effects (Cleric, catalog closure) | Spell lists, Spells and Spellcasting chapter | RC Core | `MAGIC-001`, `MAGIC-002` | — | Yes — 7 spell levels | Unresearched | **Catalog-closure entry.** High effort. |
| `MAGIC-006` | Individual Spell Effects (Druid, catalog closure) | Spell lists, Spells and Spellcasting chapter | RC Optional class content → **Project-Selected: REQUIRED** (`DEC-0008`, Druid enabled) | `CHAR-013` (Druid), `MAGIC-001`, `MAGIC-002` | — | Yes | Unresearched | **Catalog-closure entry**, now confirmed in scope (Druid is required, not conditional). High effort. |

## Domain: `treasure` (TREAS)

| ID | Title | RC Source | RC Classification / Project Selection | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `TREAS-001` | Treasure Type Generation by Dungeon Level | Treasure chapter | RC Core | `EXP-008` | — | Yes | Unresearched | Medium. |
| `TREAS-002` | Gem/Jewelry/Coin Value Determination | Treasure chapter | RC Core | `TREAS-001` | — | Yes | Unresearched | Medium. |
| `TREAS-003` | Magic Item Generation, Catalog & Effects (catalog closure) | Treasure chapter | RC Core | `TREAS-001`, `MAGIC-003+`/`MAGIC-005`/`MAGIC-006` | `TREAS-004` | Yes | Unresearched | **Catalog-closure entry.** High effort. |
| `TREAS-004` | Magic-Item Use: Activation, Restrictions, Identification & Curses | Treasure chapter | RC Core | `TREAS-003`, `CHAR-002`/`CHAR-009` | — | Yes | Unresearched | Medium-high. |

## Domain: `advancement` (ADV)

| ID | Title | RC Source | RC Classification / Project Selection | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `ADV-001` | Experience Point Awards (treasure + monsters defeated) | Experience chapter | RC Core | `TREAS-001`, `COMBAT-003`, `MON-001` | `ADV-002` | Yes | Unresearched | Medium. |
| `ADV-002` | Level Advancement & Titles | Experience chapter | RC Core | `ADV-001`, `CHAR-002` | `MAGIC-*` (spell-level access), `CHAR-011` (Weapon Mastery gates), `CHAR-013` (high-level branches) | Yes — full standard progression per class, see "Progression-Scope Findings" | Unresearched | No mandatory gold/time training procedure appears to exist in this lineage; progression is now correctly stated per-class rather than a flat 1–36. |
| `ADV-003` | Between-Expedition Resupply & Town Services | Equipment / Nonplayer Characters | RC Core | `CHAR-004`, `TREAS-004` | — | Yes | Unresearched | Low-medium; possible merge candidate once researched. |

## Simulator Specifications (Non-Historical Design Requirements)

| ID | Title | Constraint Source | Dependencies | Status | Notes |
|---|---|---|---|---|---|
| `SIM-001` | Procedural Dungeon **Layout** Generation | RC permits any layout method but does not supply a complete random map-layout generator (corrected this revision — see Major Research-Risk Flags item 7) | `EXP-008` (stocking consumes an already-laid-out map) | Reassessed and confirmed still required | **Scope narrowed this revision:** owns layout/map generation only. Does **not** own canonical room-content stocking (`EXP-008`) or monster/treasure determination (`MON-*`/`TREAS-*`), all of which RC supplies as historical rules — these must not be silently absorbed into `SIM-001`. |
| `SIM-002` | V1 Survivability Policy Specification | `ARCHITECTURE.md` §10, `GAME_CONSTITUTION.md` §8 — source-baseline-independent | Cuts across whichever clusters implement encounters, traps, and rewards | Not researched or designed — intentionally deferred, unchanged in nature | Kept explicitly distinct from `COMBAT-009` (Mortally Wounded — a selected RC-authored rule, part of canonical configuration, not a `SIM-002` accommodation) and from `EXP-004`'s RC-native rest/exhaustion rules. `SIM-002` is not eliminated by any RC-native survivability-friendly rule being selected; it may later build on that stronger canonical foundation. |

## Chapter 19 Variants — Individually Tracked

Chapter 19 ("Variant Rules") is not classified wholesale. Each major variant identified during this revision:

| Variant | RC Classification | Project Selection | Inventory Entry |
|---|---|---|---|
| Ability-Based Saving Throws | RC Optional Ch. 19 variant | **REQUIRED / ENABLED** | `CHAR-007`, `COMBAT-004` |
| Nonlethal Combat | RC Optional Ch. 19 variant | **REQUIRED / ENABLED** | `COMBAT-008` |
| Mortally Wounded / Keeping Characters Alive | RC Optional Ch. 19 variant | **REQUIRED / ENABLED** | `COMBAT-009` |
| Permanent Death / No Resurrection | RC Optional Ch. 19 variant | **NOT ENABLED** — standard RC resurrection/restoration availability retained | Reviewed, not implemented; no inventory entry (nothing to research for a declined variant) |
| Extended Demihuman/Mystic Level-36 Progression | RC Optional Ch. 19 variant | **NOT ENABLED for V1** — future optional variant candidate, not permanently rejected | Noted in "Progression-Scope Findings" and `DEC-0008`; no inventory entry while out of V1 scope |

No other major Chapter 19 variant was identified during this revision beyond the five above. If a future, more detailed Chapter 19 review finds another, it is to be surfaced for human review, not silently enabled or excluded.

## Chapter 13 Coverage

Chapter 13's DM-facing referee procedures, previously unreviewed, are mapped as follows:

| Chapter 13 Topic | Disposition |
|---|---|
| Ability checks (general d20-roll-under-ability procedure) | Existing entry, dependency added — `CHAR-007`/`CHAR-012` (the shared resolution mechanic General Skills uses). |
| Doors | Existing entry, source location added — `EXP-005`. |
| Listening | Existing entry, source location added — `EXP-005`. |
| Special character conditions | Existing entry, dependency/notes added — `COMBAT-003` (poison, disease, paralysis, level drain, and similar status effects are treated as combat/damage-adjacent for now); **flagged as a plausible future split into its own entry** once the exact RC procedure set is researched — this project's own independent verification of Chapter 13's exact contents here remains partial (see `RC_V1_SCOPE_AUDIT.md`). |
| Thief abilities (DM-facing resolution) | Existing entry, source location added — `CHAR-010`. |
| Aging | **New entry** — `CHAR-014`. |
| Alignment changes | Existing entry, dependency added — `CHAR-008`. |

## Major Human Decisions Required (revised — settled items removed)

Weapon Mastery, General Skills, Druid, Mystic, Morale, Nonlethal Combat, Ability-Based Saving Throws, Mortally Wounded/Keeping Characters Alive, Permanent Death, and extended demihuman/Mystic progression are **settled** by `DEC-0008` and removed from this list. Genuinely unresolved items:

1. **Whether any newly discovered RC optional system (beyond those already reviewed) should be enabled.** No such system was found during this revision's Chapter 13/15/19 review beyond what is already tracked, but the review is not claimed exhaustive (`RC_V1_SCOPE_AUDIT.md`).
2. **Wilderness Adventures reachability boundary** — unchanged from the prior draft; still open.
3. **Whether encounter-balancing or individual-initiative configurability prove low-cost enough during later implementation-design work to actually build both options.** Does not block inventory approval — the defaults (`ENC-007` OFF; `COMBAT-006` group initiative) are already clear and are what V1 uses regardless of the outcome of that later assessment.
4. **`CHAR-013`'s split-candidate status** — whether Paladin/Knight/Avenger and Druid/Mystic should become separate Rule IDs once research begins, given their now-corrected, materially different classifications (core-conditional vs. project-selected-optional).
5. **`EXP-004`'s exact scope once researched** — whether the RC-native running-exhaustion and wilderness-travel-rest concepts remain one Rule Card or split, per the SPLIT CANDIDATE flag above.

## Progression-Scope Findings (corrected)

The prior draft's "full 1–36 level range" statement is corrected: V1 supports the **full standard Rules Cyclopedia progression for each included class**, which is not identical across classes. The four human classes (Cleric, Fighter, Magic-User, Thief) advance conventionally to level 36. Each demihuman race-class (Dwarf, Elf, Halfling) has its own lower level cap, followed by continued advancement via Attack Rank progression rather than further character levels — independently corroborated this revision (multiple sources confirm demihumans "have level limits, but still have ways to improve with experience"). The Mystic class has its own level cap and progression structure, standard (not extended) for V1 per `DEC-0008`. Standard progression for every included class — including the demihuman Attack Rank structure and the Mystic's own cap — does **not** block eventual Immortality candidacy: the Rules Cyclopedia supports demihuman/Mystic Immortality through a distinct experience-based prerequisite independent of Chapter 19's extended-progression variant, so declining that variant for V1 does not foreclose the project's longer-term Immortality ambition (see "Future Scope: Immortality" below). Magic-User spells still run 9 levels and Cleric 7 (both confirmed, unchanged from the prior draft); Druid's spell-level range is not yet confirmed and is flagged for `MAGIC-006`'s own future research.

## Future Scope: Immortality (Post-V1)

Immortality (Rules Cyclopedia Chapter 15 and related material) is **explicit future required project scope**, not V1, and not excluded from the intended final product — see `DEC-0008`. The prior draft's scope audit incorrectly suggested Immortals material was absent from the book; this is corrected in `RC_V1_SCOPE_AUDIT.md`. A later major-version inventory expansion is expected to cover the Immortality rules surface in the same depth this document covers V1; that expansion is not performed here.

## Future Scope: Extended Demihuman/Mystic Progression

Chapter 19's extended level-36 demihuman/Mystic progression variant is not enabled for V1 but is retained as a **future optional variant candidate** (`DEC-0008`) — e.g., for a deliberately overpowered/unbalanced campaign mode. Not a V1 requirement, not an implementation blocker, not architected now.

## Future Scope: Supplement Expansion

Unchanged from the prior draft in principle, now framed against RC rather than the 1974 core: content from later, separately-authorized D&D-lineage supplements beyond the Rules Cyclopedia's own scope remains a future, separately governed expansion phase, not part of this inventory.

## Explicitly Outside V1 Scope

Unchanged from the prior draft: Dominion Rules (mass combat/domain rulership), naval/aerial campaign-scale combat (if distinct from ordinary encounters — still unconfirmed), stronghold construction/economics, Known World/Hollow World campaign-setting material, AD&D conversion notes. No in-scope V1 mechanic was found to depend on any of these.

## Proposed Research Order

Unchanged in overall shape from the prior draft, with two insertions: `CHAR-014` (Aging) follows naturally alongside `CHAR-007`/`CHAR-008`; `COMBAT-008`/`COMBAT-009` (the required Chapter 19 variants) are proposed alongside `COMBAT-002`–`COMBAT-006` rather than deferred, since they are now required V1 content, not optional research. Full order:

1. **Resolve the `EXP-001`/`EXP-004` foundational uncertainties first** via dedicated revalidation (not performed this task) — both now have concrete, materially-changed findings to revalidate against, rather than open uncertainties to investigate from scratch.
2. **`CHAR-001`, `CHAR-002`, `CHAR-007`, `CHAR-008`, `CHAR-014`** — ability scores, race/class eligibility, mechanical effects (including the selected ability-based-save mapping), alignment (including change-over-time), aging.
3. **`CHAR-003`–`CHAR-006`** — HP/HD, equipment, encumbrance/movement, retainers.
4. **`EXP-002`–`EXP-010` revalidation/research**, with `EXP-004` prioritized given its reframed scope.
5. **`COMBAT-001`–`COMBAT-009`** — no longer gated behind a foundational fork; includes the required Nonlethal Combat and Mortally Wounded variants alongside the core sequence.
6. **`ENC-001`–`ENC-006`**, including `ENC-004` Morale as required content (not optional research).
7. **`MON-001`, `MON-002`** — determination/number-appearing, ahead of catalog closure.
8. **`TREAS-001`, `TREAS-002`** — treasure-type and value, ahead of the magic-item catalog.
9. **`ADV-001`–`ADV-003`** — experience, leveling (per-class progression), resupply.
10. **`CHAR-009`, `CHAR-010`, `CHAR-011`/`COMBAT-007`, `CHAR-012`, `CHAR-013`** — class/racial abilities, Thief skills, and the required Weapon Mastery/General Skills/high-level-branch content, now that foundational combat/exploration systems are in hand.
11. **`MAGIC-001`–`MAGIC-006`, `TREAS-003`–`TREAS-004`, `MON-003`–`MON-004`** — the largest-volume catalog-closure items, tackled last.
12. **`ENC-007`** — only if/when encounter-balancing configurability is later pursued; not required for a functioning V1 loop given its default-OFF status.

`SIM-002` remains a design task, not a research task. `SIM-001` may now proceed in parallel with `EXP-008` given its narrowed, confirmed scope.

## Candidate Cluster Signals (observations only — not proposals)

Unchanged in shape from the prior draft, with the caveat below now stated more strongly: a possible exploration/time cluster, character-foundation cluster, encounter-resolution cluster, and combat-foundation cluster remain visible in the dependency graph. **The exploration/time cluster's membership is genuinely uncertain, not merely pending verification** — `EXP-001`'s cadence has materially changed and `EXP-004`'s scope has been substantially reframed, and their dependency relationship to each other and to `EXP-002` may differ from the old three-item `CLUSTER-001` boundary as a result. See "Preliminary Assessment of `CLUSTER-001`" in `INVENTORY_MIGRATION_MAP.md`. None of these signals is defined, bounded, or approved here; later cluster selection must be re-derived from this approved inventory once it reaches that state, not assumed to inherit the old boundary.

---

## Maintenance

Now `APPROVED` (2026-08-16). It is updated as entries move from unresearched → partial source → Rule Card drafted → `APPROVED` (or `OUT OF V1 SCOPE — HUMAN APPROVED`), and as cluster boundaries are (re-)selected (`ARCHITECTURE.md` §15.1/§15.2). It does not itself authorize any cluster or implementation.
