# V1 Rules Inventory and Dependency Map

**Status: DRAFT — submitted for human review.** This is a scoping/backlog document, not a Rule Card. It identifies the Rule Cards (or coherent groupings) reachable from the v1 dungeon-crawl loop and makes their dependency relationships visible, per `ARCHITECTURE.md` §15.1 and `docs/decisions/DEC-0005-v1-rules-inventory-and-clustered-implementation.md` — it does not resolve any of them. Historical-rules work proceeds in dependency-complete clusters selected from this inventory once it is reviewed and accepted (§15.1); it does not require every item below to be `APPROVED` before any cluster may begin.

This inventory was produced without deep-researching most items (per the assigning instructions). Two items — `EXP-001` and, incidentally, several of its neighbors in *The Underworld & Wilderness Adventures* — were already researched or partially sourced while drafting `EXP-001`; that head start is noted explicitly where it applies. Everything else is unresearched, and any domain-structure claims below not attributed to a specific extracted quote should be read as "expected, based on the three-volume set's known organization" rather than "verified."

**V1 progression scope.** This inventory covers the full playable progression reachable through normal v1 play under the 1974 three-book core — not an arbitrary low-level or low-dungeon-level cap. If normal play can advance a character to a higher supported level, the rules and content reachable at that level (higher-level class progression, higher-level spells, deeper dungeon encounter content, treasure and magic items reachable through the canonical procedures, and the monsters/special abilities reachable through those procedures) remain part of this inventory. Cluster-based *implementation* (`ARCHITECTURE.md` §15.1) may still proceed incrementally — an early cluster reasonably starting with low-level content is a sequencing choice, not a catalog boundary — but this document itself must not silently truncate what's catalogued. See `docs/decisions/DEC-0006-v1-playable-content-scope.md`.

**Playable-content boundary.** For initial v1 playable content, the 1974 three-book core (*Men & Magic*, *Monsters & Treasure*, *The Underworld & Wilderness Adventures*) is the content boundary — the classes, spells, monsters, and magic items catalogued here are drawn only from those three books. Later non-AD&D D&D sources remain available through `SOURCE_HIERARCHY.md` for *compatible completion* of an incomplete or ambiguous 1974 mechanic; they do not automatically enlarge this catalog. A class, spell, monster, or item that exists only in a later supplement (e.g., the Thief, from Supplement I: *Greyhawk*) is tracked as future supplement-expansion scope (see "Future Scope: Supplement Expansion" below), not included here. See `docs/decisions/DEC-0006-v1-playable-content-scope.md`.

## How to Read This Table

| Column | Meaning |
|---|---|
| ID | Proposed, reserved Rule ID (domain prefix + number). Not yet drafted unless marked otherwise. Grouping and numbering may shift once actual drafting starts. |
| Title / Grouping | Working title. |
| Key Source | Where 1974 material is expected or known to live. "Not yet retrieved" means the source volume hasn't been fetched during this project yet — only *The Underworld & Wilderness Adventures* (Vol. 3) has been consulted so far. |
| Dependencies | Other inventory items this one needs resolved first (mechanically, not just for drafting convenience). |
| V1 Required | Whether the taxonomy this inventory was built from marks this as reachable from the v1 dungeon-crawl loop. |
| Status | `APPROVED` / partial-source-in-hand / unresearched / blocked. |
| Risk Flags | Known or suspected difficulty, ambiguity, or scope-decision needs. |

**A note on grouping.** An inventory ID is a proposed, reserved identifier for tracking purposes — not a permanent one-to-one Rule Card boundary. A grouping such as `EXP-005` ("Searching, Listening, Doors & Secret Features") may split into multiple Rule Cards once research reveals distinct historical procedures, separate dependencies, racial modifiers, independent ambiguity, or independently testable behavior. This inventory defines the complete rules surface; detailed research determines the final Rule Card boundaries.

---

## ⚠ Major Research-Risk Flags (read first)

These seven items are more consequential than the rest of the table and are called out separately because each blocks or shapes a large downstream portion of the inventory. None of them is resolved by this document.

1. **Combat system selection (`COMBAT-001`).** OD&D 1974 does not mandate one combat system — Volume 1 (*Men & Magic*) presents the default Chainmail-based man-to-man system and an "Alternative Combat System." `SOURCE_HIERARCHY.md` §3 lists *Chainmail* as an explicit dependency "where the 1974 rules explicitly depend upon it," but choosing between the two systems is a foundational fork with major downstream consequences (armor class meaning, to-hit resolution, everything in the `COMBAT-*` and much of `MON-*` domains). This is a human decision, not an implementation-agent inference.
2. **Dungeon generation / map authoring — reclassified as a Simulator Specification, not an unresolved historical rule.** The 1974 text is explicit that dungeon layout is hand-authored by the referee: "Before it is possible to conduct a campaign of adventures in the mazey dungeons, it is necessary for the referee to sit down with pencil in hand and draw these labyrinths on graph paper" (Vol. 3, p. 4). No 1974 procedural/random dungeon-layout generation algorithm has been located, and none is expected to exist historically. This is distinct from *dungeon stocking* (`EXP-008`, populating an already-drawn dungeon with monsters/treasure), which *is* explicitly procedural and already substantially sourced. Rather than track this indefinitely as an undefined historical rule, it is now `SIM-001` — a simulator-authored design requirement, constrained by historical guidance but not itself a historical rule (see "Simulator Specifications" below).
3. **Reaction (`ENC-003`) and Monster Morale (`ENC-004`) have not yet been located** in the material consulted so far (Volume 3 only). These are expected to live in Volume 1 or Volume 2, neither of which has been retrieved yet. Flagged as unresearched, not merely unresolved.
4. **Spell, monster, and magic-item breadth is large, not indefinite — full 1974-core progression, not level-capped.** `MAGIC-003+` (individual spell effects), `MON-003`/`MON-004` (general monster stats and special abilities), and `TREAS-003`/`TREAS-004` (magic-item catalog and use) each span the full playable progression the 1974 core supports — not truncated to starting characters or low dungeon levels (see "V1 progression scope" above; `DEC-0006`). This is a genuine research-*volume* concern, not a scoping-decision one: cluster-based implementation (`ARCHITECTURE.md` §15.1) may still reasonably tackle lower-level content in an earlier cluster, but the inventory itself must catalog the full three-book-core breadth.
5. **Core class roster — resolved this revision.** OD&D's original three booklets define exactly three classes — Fighting-Man, Magic-User, Cleric — and four playable races (human, dwarf, elf, hobbit) with class restrictions. `CHAR-002`, `CHAR-009`, and related items are scoped to this three-book roster only. A Thief class does not exist in the 1974 core; it first appears in Supplement I: *Greyhawk* (still non-AD&D lineage, per `SOURCE_HIERARCHY.md` §3 item 3, but not part of the core three booklets) and is tracked under "Future Scope: Supplement Expansion" below, not included in v1 core (`DEC-0006`).
6. **Retainers/hirelings (`CHAR-006`) priority.** Included per the assigned taxonomy, but the core dungeon-crawl loop (§14) can plausibly function with PC-only parties. Flagged for a priority/sequencing decision, not proposed for removal from scope.
7. **Combat sequence, initiative, and timing — newly flagged, historically high-risk.** Melee timing, missile timing, spellcasting timing, and movement during combat are given their own inventory visibility (`COMBAT-006`) rather than being absorbed into attack resolution (`COMBAT-002`). This is likely one of the more historically ambiguous areas in the whole inventory: OD&D's relationship to *Chainmail*'s turn/initiative structure, and any differences in sequencing between the default and "Alternative" combat systems, are not yet researched. Depends directly on `COMBAT-001`.

---

## Domain: `exploration` (EXP)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `EXP-001` | Dungeon Wandering-Monster Check | Vol. 3, p. 10 | RNG abstraction | Yes | **APPROVED** | None — resolved. |
| `EXP-002` | Dungeon Turn / Time Accounting | Vol. 3, p. 8 ("THE MOVE/TURN IN THE UNDERWORLD") | — | Yes | Partial source in hand | **High priority** — `EXP-001` already depends on this (its own Open Questions item). Partial text already extracted: a turn ≈ 10 minutes ≈ two moves; resting consumes one full turn per hour; searching a 10' wall section takes a full turn, shorter activities a referee-adjudged portion; combat is ten rounds per turn. The precise accounting *algorithm* for a computer simulation (how partial-turn activities accumulate, exact check-firing timing) is not yet specified. |
| `EXP-003` | Dungeon Movement, Mapping & Special Terrain | Vol. 3 p. 8; Vol. 1 (movement rates) — Vol. 1 not yet retrieved | `CHAR-005`, `EXP-002` | Yes | Partial source in hand | Medium. Scope now explicitly includes special-terrain movement as a research concern, flagged but not resolved: underground water/aquatic movement (underground lakes, flooded areas, or similar terrain that authored dungeons or `SIM-001` may produce). Not assumed at inventory stage to need an independent Rule Card — may split out later only if research or `SIM-001`'s eventual design justifies it (see "A note on grouping"). No aquatic mechanics are specified here. |
| `EXP-004` | Resting Procedure | Vol. 3, p. 8 | `EXP-002` | Yes | Partial source in hand ("one turn every hour must be spent motionless") | Low. |
| `EXP-005` | Searching, Listening, Doors & Secret Features | Vol. 3, p. 10 | `EXP-002` | Yes | Substantial source in hand | Low-medium. Already sourced: secret doors 1–2 on d6 (elves 1–4; referee-optional passive sensing 1–2 for elves); forcing doors 1–2 on d6; listening 1 on d6 (elves/dwarves/hobbits 1–2); trap/pit trigger 1–2 on d6. Mostly needs formalizing into a card, not fresh research. |
| `EXP-006` | Light & Exploration Resources | Vol. 3, p. 10 | `EXP-002` | Yes | Partial source in hand | Medium — illumination/detection behavior is sourced (torches let monsters see the party; wind can extinguish a torch; monsters have infravision), but resource *consumption rate* (how many turns a torch/lantern lasts) has not yet been located. |
| `EXP-007` | Traps — trigger mechanic only | Vol. 3, p. 10 | `EXP-002` | Trigger mechanic: yes. Trap *effect* catalog: separate, large. | Partial source in hand (trigger: 1–2 on d6) | **High risk** — recommend splitting the trigger mechanic (small, in-scope, already sourced) from a trap-effect catalog (large, scattered, likely needs its own scoping decision similar to spells/monsters). |
| `EXP-008` | Dungeon Stocking (monster/treasure room placement) | Vol. 3 (near p. 7, "Distribution of Monsters and Treasure" per the booklet's table of contents) | `MON-001`, `MON-002`, `TREAS-001` | Yes | Substantial source in hand | Low-medium. Already sourced: monster present in a room on a 1–2 (d6); of monster-occupied rooms, treasure present on 1–3 (d6); of unoccupied rooms, treasure present on 1 (d6). |
| ~~`EXP-009`~~ → `SIM-001` | Dungeon Generation / Map Authoring | Vol. 3, p. 4 | Blocks meaningful end-to-end testing of `EXP-008` and dungeon entry generally | N/A — not a historical Rule Card | **Reclassified** as a Simulator Specification — see `SIM-001` under "Simulator Specifications" below, and Major Research-Risk Flags item 2. |
| `EXP-010` | Party Formation & Marching Order | Not yet located; expected Vol. 3 (dungeon movement/encounter context) and/or Vol. 1 | `EXP-002`, `EXP-003`, `CHAR-005` | Yes | Unresearched | Medium — tracks mechanical relevance to dungeon movement, who is exposed first to hazards and traps where formation matters, `ENC-002` (surprise) and `ENC-003` (reaction) positioning/targeting, and possible `COMBAT-006` (sequence/timing) target-exposure implications. Dependencies and research surface only — specific mechanics not decided here; may split later per "A note on grouping" if research justifies it. |

## Domain: `encounters` (ENC)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `ENC-001` | Encounter Distance | Vol. 3, p. 10 | — | Yes | Source in hand (2d4 → 20–80 feet) | Low. |
| `ENC-002` | Surprise | Vol. 3, p. 10 | — | Yes | Source in hand (1–2 on d6 per side; 10–30 ft distance if surprised) | Low. |
| `ENC-003` | Reaction | Not yet located (expected Vol. 1 or Vol. 2) | Follows a triggered encounter (`EXP-001`, `MON-001`) | Yes | **Unresearched, not located** | **High — see Major Research-Risk Flags item 3.** |
| `ENC-004` | Monster Morale | Not yet located (expected Vol. 2) | `ENC-003`, combat domain | Yes | **Unresearched, not located** | **High — see Major Research-Risk Flags item 3.** |
| `ENC-005` | Retreat, Pursuit & Evasion (underworld) | Vol. 3 has a *wilderness* pursuit/evasion procedure (found); an underworld-specific equivalent has not yet been confirmed | `EXP-002`, `EXP-003` | Yes | Unresearched (wilderness analog only) | Medium-high — may reuse a similar mechanic, may be silent (candidate for Simulator Ruling). |
| `ENC-006` | Non-Combat Resolution / Parley | Not yet located; may be thin in 1974 beyond the reaction result itself | `ENC-003` | Uncertain — may resolve to "governed almost entirely by the reaction result, no separate mechanical card needed" | Unresearched | Medium — possible Simulator Ruling candidate if 1974 doesn't mechanize this further. |

## Domain: `monsters` (MON)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `MON-001` | Monster Determination & Level Matrix | Vol. 3, pp. 10–11 (table located, not transcribed) | `EXP-001`, `EXP-008` | Yes | Table located, untranscribed | Medium — needs a careful, complete, verified transcription. |
| `MON-002` | Number Appearing | Vol. 3, p. 11 (found: "based on a single creature, modified by type ... and the number of adventurers in the party") | `MON-001` | Yes | Partial source in hand | Medium. |
| `MON-003` | General Monster Statistics (core roster) | *Monsters & Treasure* (Vol. 2) — not yet retrieved | `MON-001`, and likely `COMBAT-001` for how stats are expressed | Yes — full 1974-core monster roster reachable through canonical procedures, not level-capped (see "V1 progression scope") | **Unresearched, Vol. 2 not yet retrieved** | High effort — large catalog; cluster-based implementation may still reasonably tackle lower-level monsters in an earlier cluster (see Major Research-Risk Flags item 4). |
| `MON-004` | Monster Special Abilities (v1-reachable) | Vol. 2 | `MON-003` | Yes, scoped to `MON-003`'s full roster | **Unresearched** | High effort, size follows from `MON-003`'s scope. |

## Domain: `combat` (COMBAT)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `COMBAT-001` | Combat System Selection | Vol. 1 (*Men & Magic*, both systems referenced); *Chainmail* (1971, explicit external dependency per `SOURCE_HIERARCHY.md` §3) | None, but gates everything below | Yes | **Unresearched — foundational decision, not made** | **Critical — see Major Research-Risk Flags item 1.** |
| `COMBAT-002` | Attack Resolution, Armor Class & To-Hit | Depends entirely on `COMBAT-001`'s outcome | `COMBAT-001` | Yes | Blocked | Shape and size unknown until `COMBAT-001` resolves. |
| `COMBAT-003` | Damage & Death | Vol. 1 / Vol. 2 | `COMBAT-001`, `COMBAT-002` | Yes | Unresearched | Medium. |
| `COMBAT-004` | Saving Throws | Vol. 1 | `CHAR-003` | Yes | Unresearched | Medium — class/level matrix, needs full sourcing. |
| `COMBAT-005` | Healing & Natural Recovery | Vol. 3 (table of contents lists "Healing Wounds," p. 34; not yet extracted) | — | Yes | Located in table of contents, not yet extracted | Low. |
| `COMBAT-006` | Combat Sequence, Initiative & Timing (melee/missile/spell/movement ordering) | Vol. 1 (*Men & Magic*); relationship to *Chainmail*'s turn structure not yet researched | `COMBAT-001` | Yes | Unresearched | **High — see Major Research-Risk Flags item 7.** Historically ambiguous; kept explicitly visible rather than folded into `COMBAT-002`. |

## Domain: `magic` (MAGIC)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `MAGIC-001` | Spell Preparation & Memorization | Vol. 1 | `CHAR-002` | Yes | Unresearched | Medium. |
| `MAGIC-002` | Spellcasting Procedure (casting time, interruption) | Vol. 1 | `MAGIC-001` | Yes | Unresearched | Medium. |
| `MAGIC-003+` | Individual Spell Effects (grouped by class + level) | Vol. 1 spell lists | `MAGIC-001`, `MAGIC-002` | Yes — full spell-level progression reachable under the 1974 core, not capped to starting-character spell levels (see "V1 progression scope") | **Unresearched — large** | **High — see Major Research-Risk Flags item 4.** |
| `MAGIC-004` | Cleric Turn Undead | Vol. 1 | `CHAR-002` | Yes, if clerics are in v1 (expected) | Unresearched | Low-medium. |

## Domain: `treasure` (TREAS)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `TREAS-001` | Treasure Type Generation by Dungeon Level | Vol. 3, p. 7 (full table already extracted) | `EXP-008` | Yes | **Substantial source in hand** — complete silver/gold/gems/magic-percentage table by level band already captured verbatim while researching `EXP-001` | Low — best-positioned item in this domain. |
| `TREAS-002` | Gem/Jewelry/Coin Value Determination | Vol. 2 — not yet retrieved | `TREAS-001` | Yes | Unresearched | Medium. |
| `TREAS-003` | Magic Item Generation, Catalog & Effects | Vol. 2 | `TREAS-001`, `MAGIC-003+` (spell-based items depend on spell definitions) | Yes — full magic-item catalog reachable under the 1974 core, not level-capped (see "V1 progression scope") | **Unresearched — large** | **High — see Major Research-Risk Flags item 4.** |
| `TREAS-004` | Magic-Item Use: Activation, Restrictions, Identification & Curses | Vol. 1 / Vol. 2 (expected) | `TREAS-003`, `CHAR-002`/`CHAR-009` (class/race restrictions) | Yes | Unresearched | Medium-high — likely uneven across items (some may just require wearing/wielding, others need explicit activation or charge-tracking); identification-of-function and curse behavior need dedicated research once `TREAS-003`'s catalog exists. |

## Domain: `character_creation` (CHAR)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `CHAR-001` | Ability Score Generation | Vol. 1 | — | Yes | Unresearched | Low — likely straightforward, needs primary verification (not assumed here). |
| `CHAR-002` | Race & Class Eligibility | Vol. 1 | `CHAR-001` | Yes — scoped to the 1974 three-book core roster only (Fighting-Man, Magic-User, Cleric; human/dwarf/elf/hobbit) | Unresearched | Medium — demi-human ability minimums/level caps need precise sourcing. Eligibility only; see `CHAR-009` for special/racial abilities and restrictions. Class-roster scope resolved this revision — see Major Research-Risk Flags item 5 and `DEC-0006`. |
| `CHAR-003` | Starting Hit Points & Base Saving Throws | Vol. 1 | `CHAR-002` | Yes | Unresearched | Medium — interacts with `COMBAT-004`. |
| `CHAR-004` | Starting Equipment & Expedition Preparation | Vol. 1 | `CHAR-001`–`CHAR-003` | Yes | Unresearched | Low-medium — mostly catalog transcription. |
| `CHAR-005` | Encumbrance & Movement Rate | Vol. 1, cross-referenced with Vol. 3 | `CHAR-004` | Yes | Unresearched | Medium. Precedes `EXP-003` (dungeon movement consumes this item's movement-rate output) — see Proposed Research Order. |
| `CHAR-006` | Retainers & Hirelings | Vol. 3 (table of contents: "Specialists," "Men-at-Arms" sections) | `CHAR-004` | Yes (per taxonomy) — see Major Research-Risk Flags item 6 for priority | Unresearched | Low-medium. |
| `CHAR-007` | Ability Score Mechanical Effects & Cross-System Dependencies | Vol. 1 | `CHAR-001`; touches `CHAR-006` (retainers), `ENC-003` (reaction), `CHAR-008` (languages), `CHAR-002`/`CHAR-009` (class progression) | Yes | Unresearched | Medium — needs to enumerate Strength/Intelligence/Wisdom/Constitution/Charisma effects individually (not just ability generation) and their downstream dependencies; may split per-ability once researched (see "A note on grouping"). |
| `CHAR-008` | Alignment & Languages | Vol. 1 | Touches `ENC-003` (reaction), `CHAR-006` (retainers), `MON-*` (monster alignment/language), `MAGIC-*` (alignment-relevant spells) | Yes, where mechanically relevant | Unresearched | Medium — how much alignment is mechanically governed (vs. roleplaying guidance) in the 1974 core specifically needs verification; may be thinner than later editions. |
| `CHAR-009` | Class Special Abilities & Racial Abilities/Limitations | Vol. 1 | `CHAR-002`; cross-references `ADV-002` (advancement), `COMBAT-002` (attack progression), `COMBAT-004` (saves), `MAGIC-001`/`002`/`003+` (spell progression), `MAGIC-004` (turn undead) | Yes — scoped to the three-book core roster only, no later-supplement classes (`DEC-0006`) | Unresearched | Medium-high — consolidates class restrictions (e.g., Magic-User weapon/armor limits, Cleric edged-weapon prohibition) and racial abilities/limits (infravision, resistance, level caps, dual-class rules) not otherwise captured by `CHAR-002`'s eligibility focus. |

## Domain: `advancement` (ADV) — proposed new domain

`ARCHITECTURE.md` §12's suggested `docs/rules/` domain list does not currently include an XP/leveling domain; this inventory proposes adding `advancement` alongside the existing seven. Flagged for confirmation, not assumed.

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `ADV-001` | Experience Point Awards (gold + monsters defeated) | Vol. 1 (expected) | `TREAS-001`, `COMBAT-003`, `MON-001` | Yes | Unresearched | Medium. |
| `ADV-002` | Level Advancement & Titles | Vol. 1 (per-class XP tables, expected) | `ADV-001`, `CHAR-002` | Yes | Unresearched | Medium. |

## Simulator Specifications (Non-Historical Design Requirements)

These two items are not historical Rule Cards — no amount of further 1974-source research resolves them, because they are not questions the historical text answers or leaves ambiguous. They are simulator-authored design requirements, constrained by historical guidance where it exists, tracked here so they are not forgotten rather than left to be improvised during implementation.

| ID | Title | Constraint Source | Dependencies | Status | Notes |
|---|---|---|---|---|---|
| `SIM-001` | Procedural Dungeon Generation / Map Authoring | Historical guidance only: Vol. 3, p. 4 (referee hand-authors the map; no procedural algorithm given) | `EXP-008` (stocking consumes an already generated/authored map) | Unresearched / undesigned | The game requires generated dungeon environments even though the 1974 books do not provide a complete random map-generation algorithm. Historical guidance constrains the eventual design (room/passage character, level-depth conventions) without prescribing an algorithm. Kept explicitly distinct from the historically defined procedures around it: dungeon stocking (`EXP-008`), monster generation (`MON-001`/`MON-002`), treasure generation (`TREAS-001`–`TREAS-004`), traps (`EXP-007`), and other exploration procedures — none of those are reclassified, only map layout itself. |
| `SIM-002` | V1 Survivability Policy Specification | `ARCHITECTURE.md` §10, `GAME_CONSTITUTION.md` §8 (structural constraint, already documented) | Cuts across whichever clusters implement encounters, traps, and rewards | Not researched or designed — intentionally deferred | Must eventually define: which accommodations are exposed to players; which canonical results they may modify; which they may not modify (treasure/XP procedures never accept a survivability parameter — architecturally enforced, `ARCHITECTURE.md` §10); interaction with trap lethality/telegraphing and encounter severity. This inventory revision does not research or design these controls — it only ensures the requirement is tracked and not silently dropped. |

`ARCHITECTURE.md` §10's structural isolation of treasure/XP from survivability remains in force regardless of `SIM-002`'s eventual content — `SIM-002` specifies *what survivability may touch*, never treasure or XP generation.

## Explicitly Outside V1 Scope (unless a v1 procedure depends on them)

Per the assigned taxonomy: wilderness campaign procedures, the Outdoor Survival map procedure, naval combat, aerial combat, stronghold/domain construction and management, taxation/barony rules, large-scale domain warfare, and other endgame campaign systems unrelated to the dungeon expedition loop. If any of these turns out to be a genuine dependency of an in-scope item, that dependency should be surfaced for human review rather than silently pulled into scope.

This exclusion list is about *game subsystems* and is independent of the three-book playable-content boundary above: a subsystem can be in scope (the dungeon-crawl loop) while still being limited to three-book-core content, and a subsystem can be out of scope regardless of which book its source material would come from.

## Future Scope: Supplement Expansion

The 1974 three-book core is the v1 playable-content boundary (see "Playable-content boundary" above; `DEC-0006`). This is not a permanent rejection of later OD&D-era supplement material. The intended long-term model is:

```text
1974 three-book core
        ↓
faithful v1 dungeon-crawler baseline
        ↓
later explicitly authorized D&D supplement expansions
```

Future, separately authorized expansion phases may introduce additional classes (e.g., the Thief, Supplement I: *Greyhawk*), spells, monsters, magic items, or rules options drawn from later non-AD&D D&D-era supplements, subject to the same source-hierarchy and Rule Card approval process as everything else. This is a placeholder note, not a detailed supplement inventory — a supplement-content inventory is a future task, not part of this revision.

---

## Proposed Research Order

This is a proposal for human review, not a final sequence.

1. **`EXP-002`** (dungeon turn/time accounting) — `EXP-001` already depends on it; it also gates `EXP-003`–`EXP-008`.
2. **`COMBAT-001`** (combat system selection) — foundational fork; also needed before `MON-003`/`MON-004`/`COMBAT-006`/`CHAR-009` can be expressed meaningfully.
3. **Resolve `SIM-001`** (dungeon-generation approach — design, not historical research) — needed before the exploration loop can be exercised end-to-end, though `EXP-008`'s stocking *mechanic* can be researched independently of it.
4. **`CHAR-001`, `CHAR-007`** (ability scores and their mechanical effects) — natural pair; needed to have a party at all.
5. **`CHAR-002`, `CHAR-009`** (race/class eligibility, special/racial abilities) — `CHAR-009` may need revisiting once `COMBAT-001`/`ADV-002` resolve.
6. **`CHAR-003`, `CHAR-004`, `CHAR-005`** (starting HP/saves, equipment, encumbrance & movement rate) — `CHAR-005` moved up from its previous position so character/party movement capability is resolved *before* `EXP-003` and the other movement- and time-dependent exploration procedures, not after.
7. **`EXP-003`–`EXP-008`** (remaining exploration procedures, including the special-terrain concerns now flagged in `EXP-003`) — substantial source material already in hand for most of these; now correctly sequenced after `CHAR-005`.
8. **`EXP-010`** (party formation & marching order) — natural follow-on once movement and the core exploration procedures are in hand.
9. **`CHAR-008`** (alignment & languages) — moved up from its previous position so it precedes, or is available as an explicit dependency for, communication-dependent encounter research rather than following it.
10. **`ENC-001`, `ENC-002`** (distance, surprise) — already sourced; quick to formalize.
11. **`ENC-003`, `ENC-004`** (reaction, morale) — dedicated fresh research needed (Vol. 1/Vol. 2); now correctly sequenced after `CHAR-008`.
12. **`MON-001`, `MON-002`** (monster determination, number appearing) — table already partially in hand.
13. **`TREAS-001`** (treasure by level) — already substantially in hand.
14. **`COMBAT-002`–`COMBAT-006`** (attack resolution, damage, saves, healing, sequence/timing) — after `COMBAT-001` resolves.
15. **`ADV-001`, `ADV-002`** (experience, leveling).
16. **`ENC-005`, `ENC-006`** (pursuit/evasion, non-combat resolution/parley) — likely thinner sourcing; `ENC-006` (parley) also benefits from `CHAR-008` already being resolved by this point.
17. **`CHAR-006`** (retainers) — refine after the core loop is otherwise proven out.
18. **`MAGIC-001`–`MAGIC-004`, `TREAS-002`–`TREAS-004`, `MON-003`, `MON-004`** — the largest-volume items, spanning the full three-book-core progression (Major Research-Risk Flags item 4); tackle last. `SIM-002` (survivability) is a design task, not a research task, and is not part of this research sequence at all.

---

## Maintenance

This document should be updated as items move from unresearched → partial source → Rule Card drafted → `APPROVED` (or → `OUT OF V1 SCOPE — HUMAN APPROVED`), as grouping/numbering is refined during actual drafting, and as cluster boundaries are chosen and completed (`ARCHITECTURE.md` §15.1). It is the durable tracking artifact clusters are selected from — a cluster becomes ready for implementation when its own scope is dependency-complete (§15.1's five readiness criteria), not when this entire inventory is resolved.
