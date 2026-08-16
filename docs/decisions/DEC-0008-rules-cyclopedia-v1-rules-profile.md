# DEC-0008: Rules Cyclopedia V1 Rules Profile

## Decision ID
DEC-0008

## Title
Rules Cyclopedia V1 Rules Profile — Selected Core/Optional Systems

## Status
Approved

## Date
2026-08-16

## Context

`DEC-0007-rules-cyclopedia-primary-rules-authority.md` established the Rules Cyclopedia as the simulator's primary rules authority. During the resulting V1 Rules Inventory rebuild (`docs/rules/INVENTORY.md`), several Rules Cyclopedia systems were identified as **RC Optional** — presented by the Rules Cyclopedia itself as DM-choice content, not part of its own default rules (Weapon Mastery, General Skills, the Druid and Mystic classes, and the four major Chapter 19 "Variant Rules": Ability-Based Saving Throw adjustments, Permanent Death/no-resurrection, Mortally Wounded/Keeping Characters Alive, and extended demihuman/Mystic level-36 progression). A fifth area, encounter balancing, and a sixth, individual initiative, were also identified as RC-optional configuration points.

Selecting which RC-optional systems belong in this simulator's authoritative V1 configuration is a game-design decision distinct from the source-authority question `DEC-0007` settled. This record captures that decision as a single, durable, project-wide artifact rather than leaving it scattered across inventory-row edits with no central reference.

**These are not Human-Approved Variants** (`SOURCE_HIERARCHY.md` §7). A Human-Approved Variant is a deliberate deviation from an explicit Rules Cyclopedia rule. Every selection below chooses among options the Rules Cyclopedia itself explicitly offers as legitimate play — RC Core, or one of RC's own named optional/variant systems. None of them contradicts or replaces an RC rule; they configure which of RC's own supported options this project's V1 uses.

## Decision

**Required/Enabled — part of the authoritative V1 configuration:**

- Morale (RC Optional system, project-selected: REQUIRED — not a player toggle)
- Weapon Mastery (RC Optional/Additional system, project-selected: REQUIRED)
- General Skills (RC Optional/Additional system, project-selected: REQUIRED)
- Druid class (RC Optional class, project-selected: REQUIRED)
- Mystic class (RC Optional class, project-selected: REQUIRED)
- Chapter 19 Nonlethal Combat (RC Optional variant, project-selected: REQUIRED)
- Chapter 19 Ability-Based Saving Throw adjustments (RC Optional variant, project-selected: REQUIRED)
- Chapter 19 Mortally Wounded / Keeping Characters Alive (RC Optional variant, project-selected: REQUIRED)
- Standard Rules Cyclopedia demihuman/Mystic progression (level cap followed by Attack Rank-style continued advancement, per each class's own structure) — the RC default, not a Chapter 19 variant; explicitly retained rather than extended.

**Disabled / Not Selected for V1:**

- Chapter 19 Permanent Death / no-resurrection variant — the simulator retains standard RC resurrection/restoration availability where otherwise applicable. Reviewed and declined, not a Human-Approved Variant (nothing is contradicted; RC's own default already permits resurrection).
- Chapter 19 extended demihuman/Mystic level-36 progression — not enabled for V1. **Not a permanent rejection** — recorded as a future optional-variant candidate (see Consequences).

**Conditional Configurability — default behavior set now; whether both options are ever supported is an implementation-design question, not decided here:**

- Encounter Balancing (RC Optional system): default **OFF** for V1 — canonical/generated encounter difficulty is preserved rather than automatically balanced. May become a player/campaign-configurable toggle later only if implementation analysis shows this is low-cost and architecturally clean; not a V1 requirement or blocker either way.
- Initiative (RC): canonical **group/side initiative** is the V1 default. RC's optional individual-initiative variant (and any Dexterity-based individual-initiative adjustment that depends on it) may become a configurable campaign option later under the same low-cost condition as encounter balancing; not a V1 requirement or blocker.

**Future Required Project Scope, Outside V1:**

- Immortality (Rules Cyclopedia Chapter 15 and related material). Standard demihuman/Mystic progression, as selected above, does not block the path to Immortality — the Rules Cyclopedia supports demihuman/Mystic Immortality candidacy through a distinct experience-based prerequisite independent of the extended level-36 progression variant. Immortality is explicitly **not** unwanted, irrelevant, or permanently excluded — it is deferred, and a later major-version inventory expansion is expected to cover it. See `docs/rules/RC_V1_SCOPE_AUDIT.md` for the Chapter 15 coverage entry recording this.

**Future Optional Variant Candidate:**

- Chapter 19 extended demihuman/Mystic level-36 progression, for a possible future deliberately-overpowered/unbalanced campaign mode. Not architected, designed, or scheduled by this decision.

## Rationale

Consolidating these selections into one decision record — rather than leaving them implicit in inventory-row edits — gives the project a single, citable answer to "what does this simulator's V1 actually play like" that survives independent of any one inventory revision. Distinguishing RC Core / RC Optional / Project-Selected RC Option from Human-Approved Variant (`SOURCE_HIERARCHY.md` §7) matters because the two categories have different governance weight: a Human-Approved Variant documents a deliberate departure from RC's own rule and should remain rare and visible as such; a Project-Selected RC Option is simply this project choosing among RC's own sanctioned choices, which RC itself invites every table to do. Conflating the two would either inflate the Human-Approved Variant list with routine configuration choices or under-document genuine departures — this record keeps them separate.

Declining the extended-progression and permanent-death variants while keeping the door open on the former (but not proposing to revisit the latter, since nothing in this record's Context motivates it) reflects the project owner's stated intent: the completed project should retain room for deliberately unbalanced campaign modes, without that ambition displacing the intended default V1 experience.

## Consequences

- `docs/rules/INVENTORY.md` reflects each selection above against its corresponding entry (`ENC-004`, `CHAR-011`/`COMBAT-007`, `CHAR-012`, `CHAR-013`, `MAGIC-006`, and new entries `COMBAT-008` Nonlethal Combat and `COMBAT-009` Mortally Wounded / Keeping Characters Alive), each labeled with both its RC classification and its Project Selection, per this record.
- `docs/rules/RC_V1_SCOPE_AUDIT.md` records Chapter 19's individual variants (not a wholesale chapter classification) and the corrected Chapter 15 Immortals coverage.
- None of these selections authorizes implementation on its own — they configure future Rule Card research scope; the historical-rules implementation freeze (`ARCHITECTURE.md` §15.2) is unaffected by this record.
- No architecture, configuration framework, strategy interface, or runtime ruleset switcher is authorized or implied by the "Conditional Configurability" items — `ARCHITECTURE.md` §13's existing prohibition on a generic multi-ruleset engine remains in force unchanged. Whether encounter-balancing/individual-initiative toggles are ever built is a future implementation-design question, not resolved here.
- This record does not by itself constitute Rule Card research, alternate-source completion research, or a Simulator Ruling for any of the newly-required systems (Weapon Mastery, General Skills, Druid, Mystic, Nonlethal Combat, Ability-Based Saves, Mortally Wounded) — each still requires its own future research and human approval before implementation, exactly as any other inventory entry does.

## Supersedes

None.

## Superseded By

None.

This decision **complements** `DEC-0007` — it does not revise, reopen, or supersede the source-authority decision `DEC-0007` established. It operates one level below it: `DEC-0007` decided which source governs; this record decides which of that source's own offered configurations this project's V1 uses.
