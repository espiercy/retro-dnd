# V1 Rules Inventory and Dependency Map

**Status: DRAFT — submitted for human review.** This is a scoping/backlog document, not a Rule Card. It identifies the Rule Cards (or coherent groupings) needed to close the V1 Rules-Corpus Completion Gate (`ARCHITECTURE.md` §15.1, `docs/decisions/DEC-0004-full-v1-rules-corpus-before-implementation.md`) — it does not resolve any of them. Per that decision, no historical-rules implementation begins until every item below is either `APPROVED` or explicitly marked `OUT OF V1 SCOPE — HUMAN APPROVED`.

This inventory was produced without deep-researching most items (per the assigning instructions). Two items — `EXP-001` and, incidentally, several of its neighbors in *The Underworld & Wilderness Adventures* — were already researched or partially sourced while drafting `EXP-001`; that head start is noted explicitly where it applies. Everything else is unresearched, and any domain-structure claims below not attributed to a specific extracted quote should be read as "expected, based on the three-volume set's known organization" rather than "verified."

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

---

## ⚠ Major Research-Risk Flags (read first)

These six items are more consequential than the rest of the table and are called out separately because each blocks or shapes a large downstream portion of the inventory. None of them is resolved by this document.

1. **Combat system selection (`COMBAT-001`).** OD&D 1974 does not mandate one combat system — Volume 1 (*Men & Magic*) presents the default Chainmail-based man-to-man system and an "Alternative Combat System." `SOURCE_HIERARCHY.md` §3 lists *Chainmail* as an explicit dependency "where the 1974 rules explicitly depend upon it," but choosing between the two systems is a foundational fork with major downstream consequences (armor class meaning, to-hit resolution, everything in the `COMBAT-*` and much of `MON-*` domains). This is a human decision, not an implementation-agent inference.
2. **Dungeon generation / map authoring (`EXP-009`).** The 1974 text is explicit that dungeon layout is hand-authored by the referee: "Before it is possible to conduct a campaign of adventures in the mazey dungeons, it is necessary for the referee to sit down with pencil in hand and draw these labyrinths on graph paper" (Vol. 3, p. 4). No 1974 procedural/random dungeon-layout generation algorithm has been located. This is distinct from *dungeon stocking* (`EXP-008`, populating an already-drawn dungeon with monsters/treasure), which *is* explicitly procedural and already substantially sourced. Whether v1 uses hand-authored/static test dungeons, or whether a procedural generator requires a Simulator Ruling (with the attendant risk of drifting toward later-edition or AD&D-adjacent conventions if not handled carefully), is an open question for human decision.
3. **Reaction (`ENC-003`) and Monster Morale (`ENC-004`) have not yet been located** in the material consulted so far (Volume 3 only). These are expected to live in Volume 1 or Volume 2, neither of which has been retrieved yet. Flagged as unresearched, not merely unresolved.
4. **Spell, monster, and magic-item breadth is a shared, open-ended scoping question.** `MAGIC-003+` (individual spell effects), `MON-003`/`MON-004` (general monster stats and special abilities), and `TREAS-003` (magic-item catalog) are each large, expandable catalogs rather than single discrete rules. Recommend one overarching human scoping decision (e.g., "v1 covers only 1st-level spells and monsters/treasure reachable on dungeon levels 1–3, expandable later") rather than three separate open-ended asks.
5. **Core class roster.** OD&D's original three booklets define exactly three classes — Fighting-Man, Magic-User, Cleric — and four playable races (human, dwarf, elf, hobbit) with class restrictions. A Thief class does not exist in the 1974 core; it first appears in Supplement I: *Greyhawk* (still non-AD&D lineage, per `SOURCE_HIERARCHY.md` §3 item 3, but not part of the core three booklets). Whether v1 targets core-only or includes early supplement material is a scope decision, not assumed here.
6. **Retainers/hirelings (`CHAR-006`) priority.** Included per the assigned taxonomy, but the core dungeon-crawl loop (§14) can plausibly function with PC-only parties. Flagged for a priority/sequencing decision, not proposed for removal from scope.

---

## Domain: `exploration` (EXP)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `EXP-001` | Dungeon Wandering-Monster Check | Vol. 3, p. 10 | RNG abstraction | Yes | **APPROVED** | None — resolved. |
| `EXP-002` | Dungeon Turn / Time Accounting | Vol. 3, p. 8 ("THE MOVE/TURN IN THE UNDERWORLD") | — | Yes | Partial source in hand | **High priority** — `EXP-001` already depends on this (its own Open Questions item). Partial text already extracted: a turn ≈ 10 minutes ≈ two moves; resting consumes one full turn per hour; searching a 10' wall section takes a full turn, shorter activities a referee-adjudged portion; combat is ten rounds per turn. The precise accounting *algorithm* for a computer simulation (how partial-turn activities accumulate, exact check-firing timing) is not yet specified. |
| `EXP-003` | Dungeon Movement & Mapping | Vol. 3 p. 8; Vol. 1 (movement rates) — Vol. 1 not yet retrieved | `EXP-002`, `CHAR-005` | Yes | Partial source in hand | Medium. |
| `EXP-004` | Resting Procedure | Vol. 3, p. 8 | `EXP-002` | Yes | Partial source in hand ("one turn every hour must be spent motionless") | Low. |
| `EXP-005` | Searching, Listening, Doors & Secret Features | Vol. 3, p. 10 | `EXP-002` | Yes | Substantial source in hand | Low-medium. Already sourced: secret doors 1–2 on d6 (elves 1–4; referee-optional passive sensing 1–2 for elves); forcing doors 1–2 on d6; listening 1 on d6 (elves/dwarves/hobbits 1–2); trap/pit trigger 1–2 on d6. Mostly needs formalizing into a card, not fresh research. |
| `EXP-006` | Light & Exploration Resources | Vol. 3, p. 10 | `EXP-002` | Yes | Partial source in hand | Medium — illumination/detection behavior is sourced (torches let monsters see the party; wind can extinguish a torch; monsters have infravision), but resource *consumption rate* (how many turns a torch/lantern lasts) has not yet been located. |
| `EXP-007` | Traps — trigger mechanic only | Vol. 3, p. 10 | `EXP-002` | Trigger mechanic: yes. Trap *effect* catalog: separate, large. | Partial source in hand (trigger: 1–2 on d6) | **High risk** — recommend splitting the trigger mechanic (small, in-scope, already sourced) from a trap-effect catalog (large, scattered, likely needs its own scoping decision similar to spells/monsters). |
| `EXP-008` | Dungeon Stocking (monster/treasure room placement) | Vol. 3 (near p. 7, "Distribution of Monsters and Treasure" per the booklet's table of contents) | `MON-001`, `MON-002`, `TREAS-001` | Yes | Substantial source in hand | Low-medium. Already sourced: monster present in a room on a 1–2 (d6); of monster-occupied rooms, treasure present on 1–3 (d6); of unoccupied rooms, treasure present on 1 (d6). |
| `EXP-009` | Dungeon Generation / Map Authoring | Vol. 3, p. 4 | Blocks meaningful end-to-end testing of `EXP-008` and dungeon entry generally | **Undetermined** | Unresearched; no procedural source found | **Critical — see Major Research-Risk Flags item 2.** |

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
| `MON-003` | General Monster Statistics (core roster) | *Monsters & Treasure* (Vol. 2) — not yet retrieved | `MON-001`, and likely `COMBAT-001` for how stats are expressed | Yes, scope tied to chosen dungeon-level range | **Unresearched, Vol. 2 not yet retrieved** | High effort — large catalog; recommend scoping to monsters reachable at low dungeon levels first (see Major Research-Risk Flags item 4). |
| `MON-004` | Monster Special Abilities (v1-reachable) | Vol. 2 | `MON-003` | Yes, scoped to `MON-003`'s roster | **Unresearched** | High effort, size follows from `MON-003`'s scope. |

## Domain: `combat` (COMBAT)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `COMBAT-001` | Combat System Selection | Vol. 1 (*Men & Magic*, both systems referenced); *Chainmail* (1971, explicit external dependency per `SOURCE_HIERARCHY.md` §3) | None, but gates everything below | Yes | **Unresearched — foundational decision, not made** | **Critical — see Major Research-Risk Flags item 1.** |
| `COMBAT-002` | Attack Resolution, Armor Class & To-Hit | Depends entirely on `COMBAT-001`'s outcome | `COMBAT-001` | Yes | Blocked | Shape and size unknown until `COMBAT-001` resolves. |
| `COMBAT-003` | Damage & Death | Vol. 1 / Vol. 2 | `COMBAT-001`, `COMBAT-002` | Yes | Unresearched | Medium. |
| `COMBAT-004` | Saving Throws | Vol. 1 | `CHAR-003` | Yes | Unresearched | Medium — class/level matrix, needs full sourcing. |
| `COMBAT-005` | Healing & Natural Recovery | Vol. 3 (table of contents lists "Healing Wounds," p. 34; not yet extracted) | — | Yes | Located in table of contents, not yet extracted | Low. |

## Domain: `magic` (MAGIC)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `MAGIC-001` | Spell Preparation & Memorization | Vol. 1 | `CHAR-002` | Yes | Unresearched | Medium. |
| `MAGIC-002` | Spellcasting Procedure (casting time, interruption) | Vol. 1 | `MAGIC-001` | Yes | Unresearched | Medium. |
| `MAGIC-003+` | Individual Spell Effects (grouped by class + level) | Vol. 1 spell lists | `MAGIC-001`, `MAGIC-002` | Yes, scope = spell levels reachable by v1 starting characters | **Unresearched — large, open-ended** | **High — see Major Research-Risk Flags item 4.** |
| `MAGIC-004` | Cleric Turn Undead | Vol. 1 | `CHAR-002` | Yes, if clerics are in v1 (expected) | Unresearched | Low-medium. |

## Domain: `treasure` (TREAS)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `TREAS-001` | Treasure Type Generation by Dungeon Level | Vol. 3, p. 7 (full table already extracted) | `EXP-008` | Yes | **Substantial source in hand** — complete silver/gold/gems/magic-percentage table by level band already captured verbatim while researching `EXP-001` | Low — best-positioned item in this domain. |
| `TREAS-002` | Gem/Jewelry/Coin Value Determination | Vol. 2 — not yet retrieved | `TREAS-001` | Yes | Unresearched | Medium. |
| `TREAS-003` | Magic Item Generation & Catalog | Vol. 2 | `TREAS-001`, `MAGIC-003+` | Yes, scope tied to the same breadth decision as `MAGIC-003+` | **Unresearched — large, open-ended** | **High — see Major Research-Risk Flags item 4.** |

## Domain: `character_creation` (CHAR)

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `CHAR-001` | Ability Score Generation | Vol. 1 | — | Yes | Unresearched | Low — likely straightforward, needs primary verification (not assumed here). |
| `CHAR-002` | Race & Class Eligibility | Vol. 1 | `CHAR-001` | Yes | Unresearched | Medium — demi-human ability minimums/level caps need precise sourcing; also see Major Research-Risk Flags item 5 (class roster scope). |
| `CHAR-003` | Starting Hit Points & Base Saving Throws | Vol. 1 | `CHAR-002` | Yes | Unresearched | Medium — interacts with `COMBAT-004`. |
| `CHAR-004` | Starting Equipment & Expedition Preparation | Vol. 1 | `CHAR-001`–`CHAR-003` | Yes | Unresearched | Low-medium — mostly catalog transcription. |
| `CHAR-005` | Encumbrance & Movement Rate | Vol. 1, cross-referenced with Vol. 3 | `CHAR-004`, `EXP-003` | Yes | Unresearched | Medium. |
| `CHAR-006` | Retainers & Hirelings | Vol. 3 (table of contents: "Specialists," "Men-at-Arms" sections) | `CHAR-004` | Yes (per taxonomy) — see Major Research-Risk Flags item 6 for priority | Unresearched | Low-medium. |

## Domain: `advancement` (ADV) — proposed new domain

`ARCHITECTURE.md` §12's suggested `docs/rules/` domain list does not currently include an XP/leveling domain; this inventory proposes adding `advancement` alongside the existing seven. Flagged for confirmation, not assumed.

| ID | Title / Grouping | Key Source | Dependencies | V1 Required | Status | Risk Flags |
|---|---|---|---|---|---|---|
| `ADV-001` | Experience Point Awards (gold + monsters defeated) | Vol. 1 (expected) | `TREAS-001`, `COMBAT-003`, `MON-001` | Yes | Unresearched | Medium. |
| `ADV-002` | Level Advancement & Titles | Vol. 1 (per-class XP tables, expected) | `ADV-001`, `CHAR-002` | Yes | Unresearched | Medium. |

## Not a Rule Card: Survivability Policy Constraint

Survivability policy (`ARCHITECTURE.md` §10, `GAME_CONSTITUTION.md` §8) is a standing structural constraint every card above must respect — no card may accept a survivability parameter unless a separately approved policy explicitly authorizes it. It is already documented at the architecture level and does not need its own inventory entry or research.

## Explicitly Outside V1 Scope (unless a v1 procedure depends on them)

Per the assigned taxonomy: wilderness campaign procedures, the Outdoor Survival map procedure, naval combat, aerial combat, stronghold/domain construction and management, taxation/barony rules, large-scale domain warfare, and other endgame campaign systems unrelated to the dungeon expedition loop. If any of these turns out to be a genuine dependency of an in-scope item, that dependency should be surfaced for human review rather than silently pulled into scope.

---

## Proposed Research Order

This is a proposal for human review, not a final sequence.

1. **`EXP-002`** (dungeon turn/time accounting) — `EXP-001` already depends on it; it also gates `EXP-003`–`EXP-008`.
2. **`COMBAT-001`** (combat system selection) — foundational fork; also needed before `MON-003`/`MON-004` can express monster stats meaningfully.
3. **Resolve the `EXP-009` flag** (dungeon-generation approach) — needed before the exploration loop can be exercised end-to-end, though `EXP-008`'s stocking *mechanic* can be researched independently of it.
4. **`CHAR-001`–`CHAR-004`** (core character creation) — needed to have a party at all.
5. **`EXP-003`–`EXP-008`** (remaining exploration procedures) — substantial source material already in hand for most of these.
6. **`ENC-001`, `ENC-002`** (distance, surprise) — already sourced; quick to formalize.
7. **`ENC-003`, `ENC-004`** (reaction, morale) — dedicated fresh research needed (Vol. 1/Vol. 2).
8. **`MON-001`, `MON-002`** (monster determination, number appearing) — table already partially in hand.
9. **`TREAS-001`** (treasure by level) — already substantially in hand.
10. **`COMBAT-002`–`COMBAT-005`** — after `COMBAT-001` resolves.
11. **`ADV-001`, `ADV-002`** (experience, leveling).
12. **`ENC-005`, `ENC-006`** (pursuit/evasion, non-combat resolution) — likely thinner sourcing; tackle after the core loop's more central pieces.
13. **`CHAR-005`, `CHAR-006`** (encumbrance, retainers) — refine after the core loop is otherwise proven out.
14. **`MAGIC-001`–`MAGIC-004`, `TREAS-002`, `TREAS-003`, `MON-003`, `MON-004`** — the largest-volume items; tackle last, and pending the human scoping decision on spell/monster/item breadth (Major Research-Risk Flags item 4).

---

## Maintenance

This document should be updated as items move from unresearched → partial source → Rule Card drafted → `APPROVED` (or → `OUT OF V1 SCOPE — HUMAN APPROVED`), and as grouping/numbering is refined during actual drafting. It is the durable tracking artifact `ARCHITECTURE.md` §15.1's gate refers to; the gate clears when every row above (and any rows added later) reaches one of those two terminal states.
