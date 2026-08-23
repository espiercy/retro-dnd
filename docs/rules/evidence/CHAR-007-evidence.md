# Stage-A Evidence: CHAR-007 — General Ability Score Mechanical Effects

> **This is a Stage-A evidence artifact, not a Rule Card.** Produced under `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` (`DEC-0009`). It is not mechanically authoritative, is not `APPROVED`, and authorizes nothing. Stage B was **not** begun.
>
> **⚠ This packet flags one finding that bears on an approved ownership boundary** (§6). It is escalated for human review, not acted upon.

## 1. Research Scope

**Investigating** the narrowed `CHAR-007` responsibility only (`docs/rules/clusters/CLUSTER-002-character-foundation.md` §5): which ability scores have general mechanical effects, where RC defines them, whether tables or prose govern, whether effects apply directly or through downstream systems, and which effects create dependencies into other cards.

**Mandatory ownership question** (cluster record §8, question 3): *are the general ability-score-effects material and the Chapter 13 general ability-check procedure one coherent `CHAR-007` responsibility, or should the ability-check procedure be separately owned?*

**Explicitly excluded by the approved boundary:** the Chapter 19 ability-modifier-to-saving-throw mapping, owned solely by `COMBAT-004`. Researched **only** to the extent needed to establish the responsibility boundary, per the task's §9 — see §6.

## 2. Primary-Source Access

As recorded in `CHAR-001-evidence.md` §2 (same source, access method, and session). No access failure occurred; `STOP — PRIMARY SOURCE ACCESS REQUIRED` was **not** triggered.

## 3. Research Questions

A. Which ability scores have general mechanical effects, and where are they defined?
B. Do tables or prose govern, and is there one shared table or several?
C. Do effects apply directly, or only through downstream systems?
D. Which effects create dependencies into other Rule Cards?
E. Do any apparently "general" effects belong wholly inside another subsystem?
F. Chapter 13 ability checks — same responsibility, or distinct?

## 4. Evidence Map

| Question | RC Location | What RC Establishes | Provenance | Confidence |
|---|---|---|---|---|
| A/B. The shared adjustment table | **Bonuses and Penalties for Ability Scores Table, p. 9** (Ch. 1, "Note Adjustments for Ability Scores") | **One** table maps a score to an adjustment for **all six** abilities uniformly: 2–3 → −3; 4–5 → −2; 6–8 → −1; 9–12 → no adjustment; 13–15 → +1; 16–17 → +2; 18 → +3. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| A/D. The effect-assignment table | **Abilities and Adjustments Table, p. 9** | Names what each ability's adjustment applies to: **Strength** → attack rolls (melee and unarmed combat), damage rolls (melee and thrown weapons), opening doors; **Intelligence** → languages, general skills (optional); **Wisdom** → saving throws vs. spells; **Dexterity** → attack rolls (thrown and missile weapons), Armor Class; **Constitution** → hit points per experience level; **Charisma** → reactions from NPCs. | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (table ↔ the per-ability prose immediately following it) |
| B. Additional per-ability tables | **Intelligence and Languages Table, p. 10**; **Charisma Adjustment Table, p. 10** | Two abilities carry their own supplementary tables beyond the shared adjustment: Intelligence maps score bands to literacy and additional-language counts; Charisma maps score bands to a reaction adjustment **plus** a maximum retainer count **plus** a retainer morale score. So the shared table is **not** the whole of the general-effects material. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| C. Strength — direct application | Ch. 1, "Strength," p. 9 | The adjustment is added to melee attack rolls and to melee/thrown damage. Also applies to the Open Doors roll (1d6, success on 5–6, adjustment applied to the die result), with an explicit override: an unmodified natural 6 always opens a door regardless of penalties. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| C. Dexterity — direct application | Ch. 1, "Dexterity," p. 10 (and the Armor Class discussion it back-references) | Applies to missile/thrown attack rolls, and to Armor Class — RC states the AC application as an inversion: each +1 on the table subtracts 1 from armor class. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| C. Constitution — applies per roll, bounded | Ch. 1, "Constitution," p. 10 | Applies to each hit-point roll; hit points cannot be reduced to zero (floor of 1 per roll); applies at every level gain **while dice are still rolled**, and ceases once fixed per-level gains begin. | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (see `CHAR-003-evidence.md`) |
| C/E. Charisma — DM-side only | Ch. 1, "Charisma," p. 10 | Affects how NPCs/monsters react **only when the character is talking to them**. RC states the reaction adjustment never adjusts rolls the player makes — it modifies rolls the DM makes. Retainer count and retainer morale are separate columns of the Charisma Adjustment Table. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| C/E. Intelligence — partly optional-system-gated | Ch. 1, "Intelligence," p. 10; Intelligence and Languages Table, p. 10 | Governs literacy and known/additional languages directly. Its general-skills effect is explicitly conditional on the DM using the optional general skills rules (Ch. 5, p. 81 — project-selected REQUIRED per `DEC-0008`, a project configuration fact, not an RC one). | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| C. Wisdom — narrow | Ch. 1, "Wisdom," p. 10; Abilities and Adjustments Table, p. 9 | The **only** RC-core saving-throw effect of any ability: Wisdom adjusts saving throws vs. spells. The Wisdom write-up carries no other effect. | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (table ↔ prose ↔ Ch. 19's own characterisation, §6) |
| D. Dependencies created | pp. 9–10, as above | Effects reach into: `COMBAT-002` (attack rolls), `COMBAT-003` (damage), Armor Class (`COMBAT-002`), `COMBAT-004` (saves vs. spells), `CHAR-003` (hit points), `ENC-003` (NPC reactions), `CHAR-006` (retainer count/morale), `CHAR-008` (languages/literacy), `CHAR-012` (general skills), `EXP-005` (opening doors). | Rules Cyclopedia Explicit (the effects) / boundary observation (the card assignments) | DIRECT PRIMARY TEXT |
| E. Open Doors — a candidate mis-assignment | Ch. 1, "Strength," p. 9; Ch. 13, "Doors," p. 147 | The Open Doors procedure itself (die, target, natural-6 override) is stated **inside** the Strength write-up, not only referenced from it. A separate Ch. 13 "Doors" entry also exists. Whether the procedure belongs to `CHAR-007` or to `EXP-005` is a boundary question this packet does not decide — see §9. | Rules Cyclopedia Explicit (the procedure) / Unresolved (its ownership) | DIRECT PRIMARY TEXT (procedure) / NOT YET VERIFIED (Ch. 13 "Doors" not read in full) |
| F. Ability checks | **Ch. 13, "Ability Checks," p. 143** | A DM-facing general resolution procedure for actions "not explained in these rules": roll 1d20 against the pertinent **raw ability score**; equal-or-under succeeds, over fails. The DM may add a bonus or penalty to the d20 roll for exceptionally easy or difficult tasks. Cross-references General Skills (Ch. 5) as an alternative resolution route. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| F. Ability checks do **not** use the adjustment table | Ch. 13, p. 143 (read in full) | The check's target number is the raw ability score. The Bonuses and Penalties for Ability Scores Table is neither referenced nor used; the DM's situational modifier is applied to the die roll and is not derived from the score. | Rules Cyclopedia Explicit (negative finding, from full-passage reading) | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |

## 5. Mandatory Ownership Question — Chapter 13 Ability Checks

**Question:** one coherent `CHAR-007` responsibility, or a distinct one?

**Reported finding: the evidence suggests a DISTINCT responsibility.** Three independent grounds, all from primary text:

1. **Different mechanic.** `CHAR-007`'s general effects convert a score into an adjustment (−3…+3) applied to other rolls. The ability check uses the **raw score as a target number** on 1d20. They share the ability score as an input and nothing else — the adjustment table plays no part in the check.
2. **Different purpose and audience.** The general-effects material is player-facing, enumerated, and closed: a fixed set of named effects recorded on the character sheet at creation (Ch. 1). The ability check is DM-facing and explicitly open-ended — a catch-all for actions RC does not otherwise cover (Ch. 13).
3. **Different location and framing.** RC places them in different chapters, and the ability check is grouped with other DM adjudication procedures (aging, alignment changes, doors, listening, thief abilities), not with character-creation material. RC never cross-references one to the other.

**Recorded as an evidence-supported observation, not a decision.** No new Rule ID was created, no scope was changed, and `CHAR-007`'s approved boundary is untouched. Note also that Ch. 13's ability check cross-references General Skills (`CHAR-012`), which `INVENTORY.md` already records as sharing this resolution mechanic — so a future separate owner, if the reviewer chooses one, would have an existing relationship to consider.

## 6. ⚠ Boundary Finding Bearing on `CHAR-007` / `COMBAT-004`

**Flagged for human review, per the task's §9 instruction; scope was not changed.**

RC Chapter 19's "Ability Scores and Saving Throws" variant (p. 266) opens by stating that **in the standard rules the only ability score affecting a saving throw is Wisdom**, adjusting saves vs. spells — and then offers the DM the *option* of extending ability adjustments to other saving throws, mapping Strength → paralysis and turn to stone; Intelligence → mind attacks; Wisdom → spells; Dexterity → wands and dragon breath; Constitution → poison but not death ray; Charisma → none, with a combined-modifier cap of ±3 on the starred entries.

**What this means for the approved ownership decision:**

- **The decision is substantially confirmed.** The Chapter 19 mapping is a distinct, optional, DM-selected system — exactly the thing assigned to `COMBAT-004`, and it plainly cannot be specified without `COMBAT-004`'s save categories.
- **But there is a genuine one-row overlap.** The Wisdom → saves-vs-spells effect is **RC Core**, sits inside `CHAR-007`'s own Chapter 1 material (Abilities and Adjustments Table, p. 9; Wisdom write-up, p. 10), and is **also restated** inside the Chapter 19 variant assigned to `COMBAT-004`. So one effect appears on both sides of the boundary, in two different RC classifications.

**Adjudication needed (not made here):** whether `CHAR-007` retains the RC-core Wisdom → saves-vs-spells effect as part of its general-effects table, with `COMBAT-004` owning only the Chapter 19 *extension*; or whether all ability-to-saving-throw effects consolidate under `COMBAT-004`. Nothing in this packet assumes either outcome, and no metadata was changed.

**Out-of-scope observation, recorded once and not pursued:** RC's Table of Contents names only three Chapter 19 sections (Ability Scores and Saving Throws; Demihuman and Mystic Experience Levels; Nonlethal Combat), but the chapter body also contains the permanent-death and mortally-wounded/keeping-characters-alive material under their own in-body headings. This resolves an uncertainty `RC_V1_SCOPE_AUDIT.md` recorded about those two variants. It belongs to `COMBAT-008`/`COMBAT-009`, not to this cluster, and is noted only so the observation is not lost.

## 7. Whole-Source Cross-Reference Pass

**Search terms used:** `Note Adjustments for Ability Scores`; `Bonuses and Penalties for Ability Scores` (all hits reviewed); `Abilities and Adjustments Table`; `Intelligence and Languages Table`; `Charisma Adjustment Table`; `ability check` (10 hits); `Ability Checks`; `Open Doors` (7 hits); `prime requisite`; `Chapter 19`; `Ability Scores and Saving Throws`; `saving throws vs. spells`; per-ability terms (`Strength`, `Intelligence`, `Wisdom`, `Dexterity`, `Constitution`, `Charisma`) read in their Ch. 1 write-ups.

**Sections inspected:** TOC; Tables index; Ch. 1 pp. 9–12 in full (the entire "Note Adjustments for Ability Scores" block and all six per-ability write-ups); Ch. 13 "Ability Checks" in full and the Ch. 13 section list; Ch. 19 p. 266 "Ability Scores and Saving Throws" in full; Ch. 5 references (not read in depth — `CHAR-011`/`CHAR-012` scope).

**Cross-references discovered:**
- The four redirections **into** this material from elsewhere: hit points (Ch. 1 p. 7), Armor Class, saving throws vs. spells, and the Constitution write-up — each sending the reader to the shared adjustment table. This card is a hub other procedures depend on.
- **Ch. 19 p. 266** — the boundary finding in §6.
- **Ch. 13 p. 143** — ability checks, the ownership question in §5.
- Ch. 5 "General Skills" (p. 81) — referenced from both the Intelligence write-up and the ability-check entry.
- Ch. 13 "Doors" (p. 147) — adjacent to the Open Doors procedure carried in the Strength write-up (§9).

**Negative results:** no seventh ability; no alternative adjustment table; no per-class or per-race variation of the shared adjustment table was located; no ability-score effect on initiative was located in this pass; Charisma was confirmed to have **no** saving-throw effect even under the Chapter 19 variant.

## 8. Falsification Pass

**Challenge 1 — "The familiar six-ability modifier model applies; the shared table is all there is."**
*Sought:* per-ability material beyond the shared table. *Searched:* all six Ch. 1 write-ups read in full; Tables index scanned for ability-related tables.
*Found:* two further tables (Intelligence and Languages; Charisma Adjustment), and Charisma carries three distinct outputs rather than one.
**Disposition: REJECTED as stated.** The responsibility is a shared table **plus** ability-specific supplementary tables and prose — not a single modifier table. This is precisely the assumption the task warned against carrying in from prior D&D knowledge.

**Challenge 2 — "Every listed effect applies directly to the character's own rolls."**
*Sought:* effects that are not player-applied. *Searched:* the Charisma and Intelligence write-ups in full.
*Found:* Charisma's reaction adjustment modifies **DM-made** rolls and never the player's; Intelligence's general-skills effect is gated on an optional system being in use.
**Disposition: QUALIFIED.** Application mode varies by ability and cannot be treated uniformly.

**Challenge 3 — "Wisdom's saving-throw effect belongs to the Chapter 19 variant, so it is `COMBAT-004`'s."**
*Sought:* whether the Wisdom effect is core or variant. *Searched:* Ch. 1 p. 9 table and p. 10 write-up; Ch. 19 p. 266 opening sentence.
*Found:* Chapter 19 itself characterises Wisdom → saves vs. spells as the **standard** rule, and the effect is listed in the Chapter 1 core table.
**Disposition: REJECTED.** The Wisdom effect is RC Core and sits in `CHAR-007`'s material — which is what produces the one-row overlap escalated in §6.

**Challenge 4 — "Ability checks are part of the general ability-score-effects responsibility."**
*Sought:* any mechanical linkage between the check and the adjustment table. *Searched:* Ch. 13 p. 143 read in full; `ability check` (all 10 hits reviewed in context).
*Found:* none. The check uses the raw score; the DM's modifier is situational and not score-derived.
**Disposition: REJECTED.** Grounds for the §5 finding.

**Challenge 5 — "The Open Doors procedure is Strength's effect, so it is `CHAR-007`'s."**
*Sought:* whether the procedure is defined here or elsewhere. *Searched:* `Open Doors` (7 hits); Ch. 13 section list.
*Found:* the full procedure (die, target, natural-6 override) is stated inside the Ch. 1 Strength write-up, while a separate Ch. 13 "Doors" entry (p. 147) also exists and was **not** read in full.
**Disposition: QUALIFIED — unresolved.** See §9.

## 9. Unresolved RC Questions

1. **Ownership of the Open Doors procedure** — stated within `CHAR-007`'s Chapter 1 material but plainly an exploration/door mechanic (`EXP-005`). Ch. 13 "Doors" (p. 147) was not read in full and may qualify or relocate it. This is a live boundary question between `CHAR-007` and `EXP-005`.
2. **Whether the Chapter 1 Armor Class discussion** that the Dexterity write-up back-references belongs to `CHAR-007` or to `COMBAT-002`. RC states the AC application inside Ch. 1; the AC system itself is combat-domain.
3. **Whether Charisma's retainer-count and retainer-morale columns** belong to `CHAR-007` (they sit in `CHAR-007`'s own table) or to `CHAR-006` (whose subject they are). RC does not partition its own table.
4. **Whether any ability affects initiative or other combat timing** — not located, but Ch. 8 was not exhaustively searched for ability-score references.
5. The `CHAR-007` / `COMBAT-004` Wisdom overlap (§6).

`POTENTIAL COMPLETION QUESTION — NOT YET RESEARCHED` does **not** apply to items 1–3 and 5, which are internal responsibility-partition questions rather than RC silences. It applies conditionally to item 4 only if a genuine RC gap is later shown.

## 10. Alternate-Source Research Requirement

**Not established as required.** RC defines the general ability-score effects explicitly and completely for all six abilities. Every unresolved item in §9 is a repository-side partition question or an unfinished search — not an RC silence — and none currently justifies gap-directed alternate-source research (`RULE_CARD_RESEARCH_PROTOCOL.md` §15).

## 11. Possible Simulator Ruling Areas (named, not drafted)

**None identified.** RC's general ability-score effects are explicit; the open items are ownership boundaries for human adjudication, not missing mechanics.

## 12. Legacy Rule Card Withholding

**Not applicable** — no prior `CHAR-007` Rule Card exists; none was consulted. The narrowing recorded in `INVENTORY.md` and the `CLUSTER-002` record was used only to fix this task's **scope**, never as evidence of what RC says.

## 13. Confidence Assessment

**High** for the substance: two governing tables at p. 9, six per-ability write-ups read in full, and the Chapter 19 boundary text read directly rather than inferred.

**Moderate** for the responsibility partition: four of the five items in §9 are boundary questions this evidence stage deliberately does not decide, and two rest on sections not exhaustively read (Ch. 13 "Doors"; Ch. 8 for ability references).

## 14. Recommendation

```text
EVIDENCE READY FOR HUMAN REVIEW
```

**with two items requiring reviewer adjudication before Stage B:** the Chapter 13 ability-check ownership question (§5 — evidence suggests distinct), and the `CHAR-007` / `COMBAT-004` Wisdom overlap (§6). Neither was resolved by agent judgement.
