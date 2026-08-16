# V1 Rules Inventory and Dependency Map (Rules Cyclopedia)

**Status: DRAFT.** This is a scoping/backlog document, not a Rule Card — it does not resolve any individual mechanic, and nothing below may authorize implementation (`ARCHITECTURE.md` §15.2's migration gate remains in force regardless of this document's own status). It supersedes the prior inventory's active framing; the prior, 1974-primary inventory remains available through Git history and is not duplicated here — see `docs/rules/RULESET_BASELINE_MIGRATION.md` for that history and `docs/rules/INVENTORY_MIGRATION_MAP.md` for the row-by-row disposition of every entry the prior inventory contained.

This document requires human review before it may be set to `APPROVED`. Until then, no cluster may be selected or defined against it (`ARCHITECTURE.md` §15.1/§15.2).

## Source and Method

Driven by the *Dungeons & Dragons Rules Cyclopedia* (TSR 1071, 1991) as primary authority (`DEC-0007`, `SOURCE_HIERARCHY.md`), not by the retired 1974-primary inventory as a checklist. See `docs/rules/RC_V1_SCOPE_AUDIT.md` for the chapter/section coverage this document was built from, and its stated verification-method limits — citations below are chapter/section-level, not page-verified, and every entry remains subject to primary-text confirmation during its own future Rule Card research. This is a deliberately broad, shallow pass (identify and classify, not resolve) — see the assigning task for the full scope boundary.

**V1 gameplay loop** (unchanged from prior policy — reachability root, not itself RC-specific):

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

**V1 progression scope.** No 1974-era progression cap is carried forward. The Rules Cyclopedia supports character levels 1–36; V1 covers the full progression reachable through normal play under that range — higher-level classes/spells/monsters/treasure are in scope, not truncated to starting characters (see "Progression-Scope Findings" below for what this changes versus the old boundary).

**Playable-content boundary.** Rules Cyclopedia content reachable through the V1 loop above, completed by alternate non-AD&D D&D sources only where RC itself is silent or ambiguous (`SOURCE_HIERARCHY.md` §3) — not automatically the old three-book catalog, and not automatically every RC-adjacent supplement either.

## How to Read This Table

| Column | Meaning |
|---|---|
| ID | Domain-prefixed Rule ID/grouping. Existing 1974-primary IDs are reused where the underlying rules responsibility survives conceptually (`INVENTORY_MIGRATION_MAP.md`); new IDs continue each domain's existing numbering, preserving gaps left by retired IDs rather than renumbering. |
| Title | Working title under the current (RC) understanding of the responsibility — may differ from the old title where RC reframes scope. |
| RC Source | Chapter/section believed to contain this material, per `RC_V1_SCOPE_AUDIT.md`. Not page-verified unless stated. |
| Core/Optional/Conditional | `CORE` (part of RC's default rules), `OPTIONAL` (RC itself presents it as DM-choice — human decision needed before it's in or out of V1), `CONDITIONAL` (in scope only if a specific upstream decision, usually an `OPTIONAL` entry, is enabled). |
| Dependencies | Other inventory items this one needs resolved first. |
| Downstream Consumers | Other inventory items that depend on this one (kept visible in both directions per the assigning instructions' reachability-closure requirement). |
| V1 Reachable | Whether this is reachable through the loop above. |
| Status | Lifecycle status of the *inventory entry itself* — none of these are researched Rule Cards yet. |
| Risk / Notes | Ambiguity/research risk, catalog-closure requirement where applicable, and legacy-mapping pointer. |

**A note on grouping**, carried forward unchanged in principle: an inventory ID is a reserved identifier for tracking, not a permanent one-to-one Rule Card boundary. Groupings may split or merge once actual research begins (`INVENTORY_MIGRATION_MAP.md` records several likely candidates already).

---

## ⚠ Major Research-Risk Flags and Human Decisions (read first)

1. **Wandering-monster check cadence is genuinely uncertain for RC specifically.** The already-approved-but-`REVALIDATION_REQUIRED` `EXP-001` established "at the end of every turn" from the 1974 text. Secondary-source research performed both during this task and during `EXP-004`'s own earlier drafting found conflicting claims that B/X/BECMI (RC's direct lineage) use "every 2 turns" instead. This could not be confidently resolved without primary-text access (`RC_V1_SCOPE_AUDIT.md`). This is the single highest-priority item for `EXP-001`'s eventual revalidation — see "Treatment of Existing Rule Cards" below.
2. **Optional systems require explicit human decisions before V1 scope is final.** Weapon Mastery, General Skills, and the optional classes (Druid, Mystic, and apparently Paladin/Avenger as high-level Fighter branches) are all RC-presented DM-choice content, not automatically in scope merely because RC is primary authority (assigning instructions §9). See "Major Human Decisions Required" below — none of these is decided by this document.
3. **`COMBAT-003` (Damage & Death) is a confirmed, foundational, material change from the prior baseline.** RC uses per-weapon damage dice, not 1974's universal 1d6 regardless of weapon — this is one of `DEC-0007`'s own two motivating examples for the whole migration. High confidence, still not primary-verified.
4. **Spell, monster, and magic-item catalog breadth is large and now demonstrably larger than the old three-book boundary** — Magic-User spells run 9 levels, Cleric spells 7 levels, across a 1–36 character-level range (versus the old boundary's narrower three-book progression). See "Progression-Scope Findings."
5. **`SIM-001` (procedural dungeon generation) could not be confirmed resolved or unresolved by RC during this pass.** Retained as a likely-still-necessary Simulator Specification pending verification, not silently dropped or silently kept unchanged.
6. **Mandatory training-for-level-up does not appear to be part of B/X/BECMI/RC's default rules** (unlike AD&D 1e), per multiple corroborating sources. `ADV-002` is scoped accordingly — flagged so a future researcher does not import an AD&D-derived assumption.
7. **Combat-system risk is likely reduced, not increased, versus the old inventory.** RC has one unified attack-roll system (no OD&D-style "which combat system" fork), and Reaction/Morale — "unresearched, not located" under the old policy — are expected to be fully present in this single consolidated volume. See "Major Dependency Changes" in `INVENTORY_MIGRATION_MAP.md`.

---

## Domain: `character_creation` (CHAR)

| ID | Title | RC Source | Core/Opt/Cond | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `CHAR-001` | Ability Score Generation | Character Creation, Ch. 1 | CORE | — | `CHAR-002`, `CHAR-007` | Yes | Unresearched | Low. Legacy: `CHAR-001`, RETAIN/REVALIDATE. |
| `CHAR-002` | Race & Class Eligibility | Character Creation, Ch. 2 | CORE (core roster); the optional-class question is tracked separately at `CHAR-013` | `CHAR-001` | `CHAR-009`, `CHAR-010`, `MAGIC-*`, `COMBAT-*` | Yes — 4 human classes (Cleric, Fighter, Magic-User, Thief) + 3 demi-human race-classes (Dwarf, Elf, Halfling) | Unresearched | Medium. Legacy: `CHAR-002`, REFRAME — the 1974 three-class/four-race roster is superseded; RC's roster includes the Thief (previously excluded as a later-supplement class under `DEC-0006`, now core-scoped under `DEC-0007`) and a distinct race-as-class structure for demi-humans that already matches how the old inventory modeled races, easing this transition. |
| `CHAR-003` | Hit Points & Hit Dice (starting and per-level) | Character Creation / Combat | CORE | `CHAR-002` | `COMBAT-003`, `COMBAT-005` | Yes | Unresearched | Medium. Legacy: `CHAR-003` ("Starting Hit Points & Base Saving Throws"), REFRAME/SPLIT CANDIDATE — the saving-throw half of the old grouping is better owned by `COMBAT-004`'s full class/level table; this entry narrows to HP/HD specifically. |
| `CHAR-004` | Starting Equipment & Expedition Preparation | Character Creation / Equipment | CORE | `CHAR-001`–`CHAR-003` | `EXP-005` (spikes, rope, etc.), `EXP-006` (light sources), `COMBAT-002`/`COMBAT-003` (weapon/armor selection) | Yes | Unresearched | Low-medium — mostly catalog transcription (weapon list, armor list, adventuring gear, price list). Legacy: `CHAR-004`, RETAIN/REVALIDATE. |
| `CHAR-005` | Encumbrance & Movement Rate | Character Creation / Combat Movement | CORE | `CHAR-004` | `EXP-003` | Yes | Unresearched | Medium. Legacy: `CHAR-005`, RETAIN/REVALIDATE — `CLUSTER-001`'s prior exclusion of this item as a "stable external contract" needing only `EXP-002`'s fixed turn-conversion fact is expected to still hold conceptually, subject to `EXP-002`'s own revalidation. |
| `CHAR-006` | Retainers & Hirelings | Nonplayer Characters / Specialists | CORE | `CHAR-004` | — | Yes (per loop; priority question carried forward — see legacy note) | Unresearched | Low-medium. Legacy: `CHAR-006`, RETAIN/REVALIDATE. The old inventory's own flag that the core loop can plausibly function PC-only is preserved as a priority (not scope) question. |
| `CHAR-007` | Ability Score Mechanical Effects & Cross-System Dependencies | Character Creation, Ch. 1 | CORE | `CHAR-001` | `CHAR-006`, `ENC-003`, `CHAR-008`, `CHAR-002`/`CHAR-009` | Yes | Unresearched | Medium. Legacy: `CHAR-007`, RETAIN/REVALIDATE. RC's ability-modifier table is expected to differ numerically from 1974's (non-linear at the tails, per corroborated secondary description) — a concrete, bounded revalidation task, not a large one. |
| `CHAR-008` | Alignment & Languages | Character Creation | CORE | — | `ENC-003`, `CHAR-006`, `MON-*`, `MAGIC-*` | Yes, where mechanically relevant | Unresearched | Medium. Legacy: `CHAR-008`, REFRAME — RC uses the classic three-axis Law/Neutrality/Chaos alignment (not AD&D's nine-alignment grid), corroborated but not primary-verified; likely more mechanically integrated with Cleric/Druid spellcasting than the 1974 core was. |
| `CHAR-009` | Class Special Abilities & Racial Abilities/Limitations | Character Creation, Ch. 2 | CORE (core-roster abilities); touches `OPTIONAL` content via `CHAR-010`/`CHAR-013` | `CHAR-002` | `ADV-002`, `COMBAT-002`, `COMBAT-004`, `MAGIC-*` | Yes — scoped to the core roster (`CHAR-002`); no longer artificially excludes the Thief | Unresearched | Medium-high. Legacy: `CHAR-009`, REFRAME (major scope change) — RC's class-ability catalog is materially larger than the 1974 core's minimal Fighting-Man/Magic-User/Cleric feature set; the Thief's core abilities are now split out to `CHAR-010` given their distinct, sizable percentage-table mechanic. |
| `CHAR-010` | Thief Skills (Open Locks, Find/Remove Traps, Climb Sheer Surfaces, Move Silently, Hide in Shadows, Pick Pockets, Hear Noise) | Character Creation, Ch. 2 (Thief) | CORE (Thief is a core class per `CHAR-002`) | `CHAR-002`, `CHAR-009` | `EXP-005`, `EXP-007`, `ENC-002` | Yes | Unresearched | Medium — percentage-by-level table for each skill; interacts directly with `EXP-005`'s door/secret-door procedures and `EXP-007`'s trap triggers, which may need Thief-specific branching once researched. **NEW** — absent from the old inventory (the Thief was excluded from the 1974-primary roster under the now-superseded `DEC-0006`). |
| `CHAR-011` | Weapon Mastery | "Other Character Abilities" section (corroborated, not page-verified) | **OPTIONAL** — human decision needed | `CHAR-002`, `CHAR-004` (weapon selection) | `COMBAT-007` | Conditional on human decision | Unresearched | High — five mastery tiers (Basic/Skilled/Expert/Master/Grand Master), level-gated acquisition, attack/damage/AC bonuses and special maneuvers. Large optional system; do not enable without explicit approval. **NEW.** |
| `CHAR-012` | General Skills | "Other Character Abilities" section, same location as `CHAR-011` (corroborated) | **OPTIONAL** — human decision needed | `CHAR-001` (ability-score roll-under resolution) | — | Conditional on human decision | Unresearched | Medium — d20 roll-under-ability-score resolution, 4 skills at creation, more with high Intelligence. **NEW.** |
| `CHAR-013` | Optional/High-Level Class Branches (Druid from Cleric; Mystic; Paladin and Avenger as Fighter branches; any other RC-specific branch not yet confirmed) | Character Creation, Ch. 2 (optional classes) | **OPTIONAL** — human decision needed per branch | `CHAR-002`, `CHAR-009` | `MAGIC-005` (Druid spells only) | Conditional on human decision, per branch | Unresearched | Medium-high — each branch has its own prerequisites (e.g., Druid requires a Neutral Cleric) and progression; the full list of RC high-level branches is not yet confirmed complete (`RC_V1_SCOPE_AUDIT.md` flags this). **NEW**, and explicitly not a closed list yet. |

## Domain: `exploration` (EXP)

| ID | Title | RC Source | Core/Opt/Cond | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `EXP-001` | Dungeon Wandering-Monster Check | Dungeon Adventures chapter | CORE | RNG abstraction, `EXP-002` | — | Yes | **`REVALIDATION_REQUIRED`** (existing Rule Card, not revalidated this task) | **High** — see Major Research-Risk Flags item 1: cadence ("every turn" vs. "every 2 turns") is the central open question for revalidation. Legacy: `EXP-001`. |
| `EXP-002` | Dungeon Turn / Time Accounting | Dungeon Adventures chapter | CORE | — | `EXP-001`, `EXP-003`–`EXP-010`, `EXP-004` | Yes | **`REVALIDATION_REQUIRED`** (existing Rule Card, not revalidated this task) | Low-medium — the 10-minute-turn/2-moves-per-turn convention is expected to be stable across the whole Basic-lineage including RC (already corroborated during this card's own original research); likely largely preserved. Legacy: `EXP-002`. |
| `EXP-003` | Dungeon Movement, Mapping & Special Terrain | Dungeon Adventures / Combat Movement | CORE | `CHAR-005`, `EXP-002` | — | Yes | Unresearched | Medium. Legacy: `EXP-003`, RETAIN/REVALIDATE. |
| `EXP-004` | Resting Procedure | Dungeon Adventures chapter | CORE, **if retained by RC at all** — flagged | `EXP-002` | `COMBAT-*` (via `rest_overdue`, if retained) | Yes, pending verification | **`REVALIDATION_REQUIRED`** (existing Rule Card, not revalidated this task) | **High** — secondary-source research located during this card's own prior drafting suggested BECMI dropped the mandatory-rest rule entirely ("no specific rules for this kind of resting"). If confirmed for RC specifically, this entry may become MATERIALLY CHANGED or OBSOLETE rather than a simple revalidation — flagged prominently, not silently assumed either way. Legacy: `EXP-004`. |
| `EXP-005` | Searching, Listening, Doors & Secret Features | Dungeon Adventures chapter | CORE | `EXP-002`, `CHAR-010` (Thief interaction) | — | Yes | Unresearched | Low-medium; still a plausible split candidate. Legacy: `EXP-005`, RETAIN/REVALIDATE. |
| `EXP-006` | Light & Exploration Resources | Dungeon Adventures chapter | CORE | `EXP-002` | — | Yes | Unresearched | Medium. Legacy: `EXP-006`, RETAIN/REVALIDATE. |
| `EXP-007` | Traps — trigger mechanic | Dungeon Adventures chapter | CORE (trigger); catalog-closure for effects | `EXP-002`, `CHAR-010` (Thief interaction) | — | Trigger: yes. Effect catalog: separate, large. | Unresearched | High risk, same split concern as before (trigger vs. effect catalog); also carries forward the unresolved `EXP-005`/`EXP-007` overlap question, explicitly not resolved here either. Legacy: `EXP-007`, RETAIN/REVALIDATE. |
| `EXP-008` | Dungeon Stocking (monster/treasure room placement) | Dungeon Adventures chapter | CORE | `MON-001`, `MON-002`, `TREAS-001` | — | Yes | Unresearched | Low-medium. Legacy: `EXP-008`, RETAIN/REVALIDATE. |
| `EXP-009` | *(retired — see `SIM-001`)* | — | — | — | — | — | — | ID retired, not reused (legacy: `EXP-009`→`SIM-001`, already retired before this migration). |
| `EXP-010` | Party Formation & Marching Order | Dungeon Adventures / Combat | CORE | `EXP-002`, `EXP-003`, `CHAR-005` | `ENC-002`, `ENC-003`, `COMBAT-006` | Yes | Unresearched | Medium. Legacy: `EXP-010`, RETAIN/REVALIDATE. |

## Domain: `encounters` (ENC)

| ID | Title | RC Source | Core/Opt/Cond | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `ENC-001` | Encounter Distance | Encounters chapter | CORE | — | — | Yes | Unresearched | Low-medium — exact roll/formula not yet corroborated for RC specifically (the old 2d4×10ft figure is 1974-specific and not assumed to carry over). Legacy: `ENC-001`, RETAIN/REVALIDATE. |
| `ENC-002` | Surprise | Encounters chapter (corroborated as its own chapter) | CORE | `CHAR-010` (Thief interaction, e.g. Hide/Move Silently) | `COMBAT-006` | Yes | Unresearched | Low-medium. Legacy: `ENC-002`, RETAIN/REVALIDATE. |
| `ENC-003` | Reaction | Encounters chapter | CORE | `EXP-001`/`MON-001` (follows a triggered encounter), `CHAR-008` (alignment/language) | `ENC-006` | Yes | Unresearched | **Risk reduced versus old inventory** — expected fully present in this single consolidated volume, resolving the old "not located" flag. Legacy: `ENC-003`, RETAIN/REVALIDATE. |
| `ENC-004` | Monster Morale | Encounters / Monsters chapter | CORE | `ENC-003`, combat domain | — | Yes | Unresearched | **Risk reduced versus old inventory**, same reasoning as `ENC-003`. Legacy: `ENC-004`, RETAIN/REVALIDATE. |
| `ENC-005` | Retreat, Pursuit & Evasion (underworld) | Dungeon Adventures / Encounters | CORE | `EXP-002`, `EXP-003` | — | Yes | Unresearched | Medium — same underworld-vs-wilderness distinction the old inventory flagged is expected to persist; not yet confirmed whether RC unifies or keeps them separate. Legacy: `ENC-005`, RETAIN/REVALIDATE. |
| `ENC-006` | Non-Combat Resolution / Parley | Encounters chapter | CORE, possibly thin | `ENC-003` | — | Uncertain — may resolve to "governed by the reaction result" | Unresearched | Medium — same uncertainty carried forward; not assumed resolved by RC's greater completeness elsewhere. Legacy: `ENC-006`, RETAIN/REVALIDATE. |

## Domain: `monsters` (MON)

| ID | Title | RC Source | Core/Opt/Cond | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `MON-001` | Monster Determination & Level/Encounter Matrix | Dungeon Adventures / Monsters chapter | CORE | `EXP-001`, `EXP-008` | — | Yes | Unresearched | Medium — RC's own dungeon-level encounter tables expected, not yet transcribed. Legacy: `MON-001`, RETAIN/REVALIDATE. |
| `MON-002` | Number Appearing | Monsters chapter (per-monster stat block field, expected) | CORE | `MON-001` | — | Yes | Unresearched | Low-medium — likely folded directly into each monster's stat block rather than a separate table; a plausible MERGE CANDIDATE into `MON-003`'s catalog-closure entry once researched. Legacy: `MON-002`, RETAIN/REVALIDATE (merge candidate flagged). |
| `MON-003` | General Monster Statistics (catalog closure) | Monsters chapter | CORE | `MON-001`, `COMBAT-002` (attack-roll expression) | `MON-004`, `TREAS-001` | Yes — full V1-reachable monster roster, not level-capped | Unresearched | **Catalog-closure entry** — later specification work must achieve complete reachability closure over every monster the canonical dungeon-stocking/encounter procedures can produce; this entry does not itself enumerate them. High effort. Legacy: `MON-003`, RETAIN/REVALIDATE. |
| `MON-004` | Monster Special Abilities & Immunities (catalog closure) | Monsters chapter | CORE | `MON-003` | — | Yes, scoped to `MON-003`'s roster | Unresearched | **Catalog-closure entry**, same closure obligation as `MON-003`. High effort, size follows from `MON-003`'s scope. Legacy: `MON-004`, RETAIN/REVALIDATE. |

## Domain: `combat` (COMBAT)

| ID | Title | RC Source | Core/Opt/Cond | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `COMBAT-001` | Combat System (unified Attack Roll vs. Armor Class) | Combat chapter | CORE | None, but gates everything below | `COMBAT-002`–`COMBAT-007`, `MON-003` | Yes | Unresearched | **Risk resolved, not merely reduced** — RC has one system, no OD&D-style selection fork; the old "combat system selection" decision no longer exists as a question. Legacy: `COMBAT-001`, REFRAME (from a *decision* item to a *description* item). |
| `COMBAT-002` | Attack Resolution, Armor Class & To-Hit | Combat chapter | CORE | `COMBAT-001` | `MON-003`, `CHAR-011` (Weapon Mastery bonuses, if enabled) | Yes | Unresearched | Medium — **now immediately researchable**, unlike the old inventory's "blocked pending `COMBAT-001`" state; class/level attack-roll tables expected. Legacy: `COMBAT-002`, RETAIN/REVALIDATE (unblocked). |
| `COMBAT-003` | Damage & Death | Combat chapter | CORE | `COMBAT-001`, `COMBAT-002` | `ADV-001` | Yes | Unresearched | **High, confirmed material change** — per-weapon damage dice (not 1974's universal 1d6); explicit `DEC-0007` motivating example. Legacy: `COMBAT-003`, REFRAME. |
| `COMBAT-004` | Saving Throws | Combat / Character Creation | CORE | `CHAR-003` | — | Yes | Unresearched | Low-medium — five-category structure (Death Ray/Poison, Magic Wands, Paralysis/Stone, Breath Attack, Rod/Staff/Spell) corroborated across independent sources; class/level table itself not yet transcribed. Legacy: `COMBAT-004`, RETAIN/REVALIDATE. |
| `COMBAT-005` | Healing & Natural Recovery | Combat / Recovery section | CORE | — | `ADV-*` (between-expedition recovery) | Yes | Unresearched | Low. Legacy: `COMBAT-005`, RETAIN/REVALIDATE. |
| `COMBAT-006` | Combat Sequence, Initiative & Timing | Combat chapter | CORE (side-based 1d6 initiative, Movement→Missile→Magic→Melee sequence); **OPTIONAL** individual-initiative variant | `COMBAT-001` | — | Yes | Unresearched | **Risk reduced versus old inventory** — a single, corroborated default sequence exists, plus a clearly-labeled optional alternative (not an unresolved *Chainmail*-relationship question as under 1974). Legacy: `COMBAT-006`, RETAIN/REVALIDATE, risk downgraded. |
| `COMBAT-007` | Weapon Mastery Combat Effects (attack/damage/AC bonuses, multiple attacks, special maneuvers) | "Other Character Abilities" section, combat-effects portion | **CONDITIONAL** on `CHAR-011` | `CHAR-011`, `COMBAT-002`, `COMBAT-003` | — | Conditional | Unresearched | High if `CHAR-011` is enabled; not in scope at all otherwise. **NEW.** |

## Domain: `magic` (MAGIC)

| ID | Title | RC Source | Core/Opt/Cond | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `MAGIC-001` | Spell Preparation & Memorization | Spells and Spellcasting chapter | CORE | `CHAR-002` | `MAGIC-002` | Yes | Unresearched | Medium. Legacy: `MAGIC-001`, RETAIN/REVALIDATE. |
| `MAGIC-002` | Spellcasting Procedure (casting time, interruption) | Spells and Spellcasting chapter | CORE | `MAGIC-001` | `COMBAT-006` | Yes | Unresearched | Medium — interruption-by-damage-during-casting is a plausible combat-timing interaction not yet confirmed for RC. Legacy: `MAGIC-002`, RETAIN/REVALIDATE. |
| `MAGIC-003+` | Individual Spell Effects (Magic-User, catalog closure) | Spell lists, Spells and Spellcasting chapter | CORE | `MAGIC-001`, `MAGIC-002` | — | Yes — 9 spell levels across levels 1–36, not capped to starting-character range | Unresearched | **Catalog-closure entry, confirmed larger than the old three-book boundary** — see "Progression-Scope Findings." High effort. Legacy: `MAGIC-003+`, RETAIN/REVALIDATE (larger scope). |
| `MAGIC-004` | Cleric Turn Undead | Character Creation (Cleric) / Combat | CORE | `CHAR-002` | — | Yes | Unresearched | Low-medium. Legacy: `MAGIC-004`, RETAIN/REVALIDATE. |
| `MAGIC-005` | Individual Spell Effects (Cleric, catalog closure) | Spell lists, Spells and Spellcasting chapter | CORE | `MAGIC-001`, `MAGIC-002` | — | Yes — 7 spell levels across levels 1–36 | Unresearched | **Catalog-closure entry.** **NEW** — the old inventory did not separate Cleric spells from `MAGIC-003+`'s grouping; split out here because Magic-User and Cleric spell lists are historically and mechanically distinct catalogs of comparable individual size. High effort. |
| `MAGIC-006` | Druid Spells (catalog closure) | Spell lists, Spells and Spellcasting chapter | **CONDITIONAL** on `CHAR-013`'s Druid branch | `CHAR-013`, `MAGIC-001`, `MAGIC-002` | — | Conditional | Unresearched | Only in scope if Druid is enabled. **NEW.** |

## Domain: `treasure` (TREAS)

| ID | Title | RC Source | Core/Opt/Cond | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `TREAS-001` | Treasure Type Generation by Dungeon Level | Treasure chapter | CORE | `EXP-008` | — | Yes | Unresearched | Medium — the old inventory's already-transcribed 1974 table does not carry over; RC's own lettered treasure-type tables (expected, not yet confirmed identical in structure) need fresh sourcing. Legacy: `TREAS-001`, RETAIN/REVALIDATE (loses its prior sourcing head start). |
| `TREAS-002` | Gem/Jewelry/Coin Value Determination | Treasure chapter | CORE | `TREAS-001` | — | Yes | Unresearched | Medium. Legacy: `TREAS-002`, RETAIN/REVALIDATE. |
| `TREAS-003` | Magic Item Generation, Catalog & Effects (catalog closure) | Treasure chapter | CORE | `TREAS-001`, `MAGIC-003+`/`MAGIC-005` (spell-based items) | `TREAS-004` | Yes — full magic-item catalog, not level-capped | Unresearched | **Catalog-closure entry.** High effort. Legacy: `TREAS-003`, RETAIN/REVALIDATE. |
| `TREAS-004` | Magic-Item Use: Activation, Restrictions, Identification & Curses | Treasure chapter | CORE | `TREAS-003`, `CHAR-002`/`CHAR-009` | — | Yes | Unresearched | Medium-high, same unevenness concern as before. Legacy: `TREAS-004`, RETAIN/REVALIDATE. |

## Domain: `advancement` (ADV)

| ID | Title | RC Source | Core/Opt/Cond | Dependencies | Downstream Consumers | V1 Reachable | Status | Risk / Notes |
|---|---|---|---|---|---|---|---|---|
| `ADV-001` | Experience Point Awards (treasure + monsters defeated) | Experience chapter | CORE | `TREAS-001`, `COMBAT-003`, `MON-001` | `ADV-002` | Yes | Unresearched | Medium — treasure-based XP tradition expected to continue (Basic-lineage hallmark); exact ratio/formula not yet confirmed for RC. Legacy: `ADV-001`, RETAIN/REVALIDATE. |
| `ADV-002` | Level Advancement & Titles | Experience chapter | CORE | `ADV-001`, `CHAR-002` | `MAGIC-003+`/`MAGIC-005` (spell-level access), `CHAR-011` (Weapon Mastery gates), `CHAR-013` (high-level branches) | Yes — full 1–36 progression | Unresearched | **Confirmed scope expansion** (level 36 vs. the old boundary); **confirmed simplification** — no mandatory gold/time training procedure appears to exist in this lineage (Major Research-Risk Flags item 6), so this entry does not need a training sub-procedure. Legacy: `ADV-002`, RETAIN/REVALIDATE. |
| `ADV-003` | Between-Expedition Resupply & Town Services | Equipment / Nonplayer Characters (expected, not yet confirmed as a single consolidated section) | CORE | `CHAR-004`, `TREAS-004` (identification services) | — | Yes — closes the loop's "recover / resupply" stage | Unresearched | Low-medium — may be thin (largely a restatement of `CHAR-004`'s shopping loop plus `TREAS-004`'s identification services) rather than a distinct new procedure; possible MERGE CANDIDATE once researched. **NEW** — the old inventory did not give this loop stage its own entry. |

## Simulator Specifications (Non-Historical Design Requirements)

| ID | Title | Constraint Source | Dependencies | Status | Notes |
|---|---|---|---|---|---|
| `SIM-001` | Procedural Dungeon Generation / Map Authoring | Uncertain — could not confirm during this pass whether RC provides complete executable generation guidance beyond authorial advice (`RC_V1_SCOPE_AUDIT.md`) | `EXP-008` | Reassessed, not resolved — retained pending verification | Legacy: `SIM-001`, RETAIN pending the specific verification flagged above; not silently kept unchanged nor silently dropped. |
| `SIM-002` | V1 Survivability Policy Specification | `ARCHITECTURE.md` §10, `GAME_CONSTITUTION.md` §8 — source-baseline-independent | Cuts across whichever clusters implement encounters, traps, and rewards | Not researched or designed — intentionally deferred, unchanged in nature | Legacy: `SIM-002`, RETAIN unchanged — this project's survivability-isolation principle does not depend on which rules edition is primary. `COMBAT-007`'s Weapon Mastery bonuses and `CHAR-011`/`CHAR-012`'s optional systems, if enabled, are new *canonical* mechanics, not survivability mechanics — flagged here only to note they must not be conflated with `SIM-002`, not because they change its design. |

## Major Human Decisions Required

None of the following is decided by this document. Each materially affects V1 scope and must be resolved before this inventory can be `APPROVED`, or explicitly deferred to a later, dedicated decision if the human project owner prefers to approve the inventory's identification of the question without yet answering it.

1. **Weapon Mastery (`CHAR-011`, `COMBAT-007`).** RC-canonical optional content. Affects: combat resolution shape, equipment/weapon choice significance, character-sheet complexity. No recommendation offered — this is a genuine game-feel choice, not a rules-clarity question.
2. **General Skills (`CHAR-012`).** RC-canonical optional content. Affects: character-creation complexity, non-combat resolution outside `EXP-005`/`ENC-006`'s existing procedures. No recommendation offered.
3. **Druid, Mystic, Paladin/Avenger, and any other high-level class branch (`CHAR-013`, `MAGIC-006`).** RC-canonical optional/high-level content. Affects: class roster breadth, spell-catalog size (Druid), and whether `CHAR-013`'s "list not yet confirmed complete" gap needs closing before approval. Recommendation: given this project's existing preference for the full canonical roster where reachable (the Thief's inclusion under `DEC-0007` is exactly this), including the optional classes is consistent with that stance — but this is offered as a recommendation, not a decision, since the assigning task explicitly withholds this choice from the agent.
4. **Wilderness Adventures reachability boundary.** Whether any Wilderness Adventures content beyond the narrow movement/pursuit facts already folded into `EXP-003`/`ENC-005` is a genuine V1 dependency, or can remain excluded per "Proposed V1 Exclusions" below. No specific candidate was found requiring import during this pass, but the chapter was not exhaustively verified (`RC_V1_SCOPE_AUDIT.md`).
5. **Whether to approve this inventory with `EXP-004` (Resting Procedure) still flagged as possibly-obsolete**, or to prioritize a targeted verification of RC's rest rule before broader approval, given its downstream effect on `EXP-002`'s cluster and `COMBAT-*`'s `rest_overdue` touchpoint.

## Progression-Scope Findings

Two confirmed expansions versus the old three-book boundary, both directly following from `DEC-0007`: (1) Magic-User spells run 9 levels and Cleric spells 7 levels, both reachable across the full 1–36 character-level range, materially larger than the 1974 core's narrower spell-level range; (2) the character-level cap itself is 36, versus the old inventory's already-uncapped-but-narrower three-book progression. No systems outside the intended V1 loop were found to become *mechanically unavoidable* purely as a consequence of this expanded range — high-level Fighter/Cleric/Magic-User/Thief play remains dungeon-crawl-loop content; only the optional high-level *class branches* (`CHAR-013`) and Weapon Mastery's late-tier acquisitions raise genuinely optional-content questions, already surfaced above, not scope-forcing ones.

## Proposed V1 Exclusions

Re-derived from RC directly, not assumed carried over from the old exclusion list, per the assigning instructions:

- Dominion Rules — domain/stronghold management, taxation, "War Machine" mass combat.
- Naval and aerial campaign-scale combat, if distinct from ordinary dungeon/wilderness encounters (not yet confirmed as a separate RC subsystem; flagged for verification, not assumed).
- Stronghold construction and economics (Wilderness Adventures).
- Known World/Mystara and Hollow World campaign-setting material (lore, not a rules system).
- AD&D 2nd Edition conversion notes/appendix.

For each, no in-scope V1 mechanic was found during this pass to depend on it (`RC_V1_SCOPE_AUDIT.md`). If a genuine dependency later surfaces, it is to be surfaced for human review, not silently imported or silently kept excluded.

## Proposed Research Order

A proposal for human review, not a final sequence — dependency-aware, not merely chapter-ordered:

1. **Resolve the two foundational uncertainties first**, since they affect the shape of everything downstream: `EXP-001`'s wandering-check cadence and `EXP-004`'s current-RC status (Major Research-Risk Flags items 1 and 6... err 1 and the `EXP-004` note). These are revalidation tasks for existing cards, not new research, but are proposed first because `CLUSTER-001`'s own future revalidation depends on them.
2. **`CHAR-001`, `CHAR-002`, `CHAR-007`** — ability scores and race/class eligibility; needed to have a party at all, and `CHAR-002` resolves the human-decision-adjacent question of exactly which core classes exist.
3. **`CHAR-003`–`CHAR-006`** — HP/HD, equipment, encumbrance/movement, retainers.
4. **`EXP-002`–`EXP-010` revalidation/research** — now that `CHAR-005` is available; largely mirrors the old proposed order's reasoning.
5. **`COMBAT-001`–`COMBAT-006`** — no longer gated behind a foundational combat-system decision; can proceed as soon as `CHAR-003`/`CHAR-004` are available.
6. **`ENC-001`–`ENC-006`** — expected to be the fastest-moving domain given RC's completeness relative to the old inventory's biggest research-risk gap.
7. **`MON-001`, `MON-002`** — determination/number-appearing procedures, ahead of the large catalog-closure items.
8. **`TREAS-001`, `TREAS-002`** — treasure-type and value procedures, ahead of the magic-item catalog.
9. **`ADV-001`–`ADV-003`** — experience, leveling, resupply loop-closure.
10. **`CHAR-009`, `CHAR-010`** — class/racial abilities and Thief skills, once the foundational systems they cross-reference (combat, exploration) are in hand.
11. **Optional-system decisions (`CHAR-011`/`COMBAT-007`, `CHAR-012`, `CHAR-013`/`MAGIC-006`)** — resolved by human decision before or during this phase; research proceeds only for enabled systems.
12. **`MAGIC-001`–`MAGIC-006`, `TREAS-003`–`TREAS-004`, `MON-003`–`MON-004`** — the largest-volume catalog-closure items, tackled last, exactly as the old inventory proposed.

`SIM-002` remains a design task, not a research task, and is not part of this sequence. `SIM-001` depends on the verification flagged above before its own sequencing can be meaningfully proposed.

## Candidate Cluster Signals (observations only — not proposals)

Per the assigning instructions, these are dependency-graph observations, not cluster definitions, boundaries, or authorizations:

- A possible **exploration/time cluster** resembling the old `CLUSTER-001` (`EXP-001`, `EXP-002`, `EXP-004`) remains visible in the dependency graph, though its exact membership is now uncertain pending the `EXP-004` obsolescence question above — see "Preliminary Assessment of `CLUSTER-001`" in `INVENTORY_MIGRATION_MAP.md`.
- A possible **character-foundation cluster** (`CHAR-001`–`CHAR-007`) is visible as a tight, low-risk dependency group with no external blockers.
- A possible **encounter-resolution cluster** (`ENC-001`–`ENC-006`) is visible, now unusually low-risk relative to the old inventory given RC's completeness.
- A possible **combat-foundation cluster** (`COMBAT-001`–`COMBAT-006`, excluding the optional `COMBAT-007`) is visible, also unblocked (no combat-system-selection fork).

None of these is defined, bounded, or approved here.

## Explicitly Outside V1 Scope

See "Proposed V1 Exclusions" above — re-derived from RC, not carried forward from the old list unexamined.

---

## Maintenance

This document requires human review before `APPROVED`. Once approved, it is updated as entries move from unresearched → partial source → Rule Card drafted → `APPROVED` (or `OUT OF V1 SCOPE — HUMAN APPROVED`), as the optional-system human decisions above are resolved, and as cluster boundaries are (re-)selected (`ARCHITECTURE.md` §15.1/§15.2). It does not itself authorize any cluster or implementation.
