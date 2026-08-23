# Stage-A Evidence: CHAR-003 — Hit Points & Hit Dice

> **This is a Stage-A evidence artifact, not a Rule Card.** Produced under `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` (`DEC-0009`). It is not mechanically authoritative, is not `APPROVED`, and authorizes nothing. Stage B was **not** begun.
>
> **⚠ This packet reports one triggered hard-stop condition** — `STOP — INTERNAL SOURCE CONFLICT REQUIRES REVIEW` (§9). It is scoped, does not affect this card's core procedure, and is escalated rather than reconciled.

## 1. Research Scope

**Investigating:** RC's HP/HD-only responsibility — starting hit points, Hit Die by class, the level-based HP/HD procedure, minimums/maxima/adjustments, and whether an ability score modifies hit points (and where that modifier's magnitude is authoritatively defined).

**Highest-priority open question** (`docs/rules/clusters/CLUSTER-002-character-foundation.md` §8, question 1): *does RC's hit-point determination incorporate an ability-score-derived modifier, and if so, is the magnitude specified by the HP procedure itself or by the general ability-score-effects material assigned to `CHAR-007`?*

**Excluded by the approved boundary:** saving throws and saving-throw progression — encountered during cross-reference and deliberately not pursued (`COMBAT-004`'s scope).

## 2. Primary-Source Access

As recorded in `CHAR-001-evidence.md` §2 (same source, access method, and session). No access failure occurred; `STOP — PRIMARY SOURCE ACCESS REQUIRED` was **not** triggered.

## 3. Research Questions

A. How are starting hit points determined?
B. What is the Hit Die by class?
C. How do hit points change with level?
D. Are there minimums, maxima, or rerolls?
E. Does an ability score modify hit points — and where is the magnitude defined?
F. Where does this responsibility end and advancement/level-cap material begin?

## 4. Evidence Map

| Question | RC Location | What RC Establishes | Provenance | Confidence |
|---|---|---|---|---|
| A. Starting HP procedure | Ch. 1, "Roll for Hit Points," p. 7 | Locate the character's class on the Character Class and Hit Dice Table, roll the die indicated to obtain starting hit points, then apply the Constitution adjustment. RC states plainly that class dramatically affects hit points received. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| B. Hit Die by class | **Character Class and Hit Dice Table, p. 8** | Cleric d6; Fighter d8; Magic-user d4; Thief d4; Dwarf d8; Elf d6; Halfling d6; Mystic d6; **Druid — marked "does not apply."** | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (table p. 8 ↔ each Ch. 2 class entry's own "Hit Dice:" line) |
| B. Druid's non-applicability explained | Character Classes and Ability Requirements Table, p. 7 | Consistent with the table's "does not apply": Druid is entered only by attaining 9th level as a cleric, so there is no 1st-level Druid Hit Die to roll. Hit points for the druid are stated as the same as those for a cleric (Ch. 10, p. 129). | Rules Cyclopedia Explicit (both facts) / Necessary Mechanical Consequence (the linkage) | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| C. Per-level rolling | Ch. 1, "Constitution," p. 10; Ch. 1, "Hit Dice and Hit Points," p. 12 | Hit Dice are rolled once per experience level gained, from 1st through **9th** level (through 8th for the halfling, whose maximum level is 8), with the Constitution adjustment applied to each roll. | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (three locations: p. 10, p. 12, and each Ch. 2 class entry) |
| C. Post-9th flat gains | Ch. 1, p. 12; Ch. 2 class entries; Ch. 10, p. 129 | From 10th level, no dice are rolled: a fixed per-class hit-point gain applies instead. Per class: Cleric +1, Fighter +2, Magic-user +1, Thief +2, Dwarf +3, Elf +1 (at 10th). Halfling has no post-cap gain (maximum level 8). | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (Ch. 2 per-class lines ↔ Ch. 1 p. 12 general statement) |
| **E. Ability modifier: YES — Constitution** | Ch. 1, p. 6 (Constitution described as affecting hit points); Ch. 1 "Roll for Hit Points," p. 7; Ch. 1 "Constitution," p. 10; **Abilities and Adjustments Table, p. 9** | Constitution modifies hit points. The Abilities and Adjustments Table names the effect precisely as **"Hit Points per Experience Level."** Three further passages independently restate it. | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (four independent locations) |
| **E. Magnitude is defined OUTSIDE the HP procedure** | Ch. 1, "Roll for Hit Points," p. 7 → **Bonuses and Penalties for Ability Scores Table, p. 9** | The HP procedure does **not** state the modifier's value. It directs the reader to look for the Bonuses and Penalties for Ability Scores Table and apply the appropriate number. The Constitution section (p. 10) repeats this redirection. The table itself is the general, all-abilities adjustment table: score 2–3 → −3; 4–5 → −2; 6–8 → −1; 9–12 → none; 13–15 → +1; 16–17 → +2; 18 → +3. | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (two redirections to one shared table) |
| D. Minimum per roll | Ch. 1, "Constitution," p. 10 | Whatever the adjustment, hit points cannot be reduced to zero — at least 1 hit point is gained **for each roll**. Stated once, at this location only. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| D/E. Modifier does not apply to flat gains | Ch. 1, p. 12; each Ch. 2 class entry; Ch. 1 p. 10 | Constitution adjustments apply **only to the Hit Dice actually rolled**; they do not apply to the fixed hit points added from 10th level onward. Every Ch. 2 class entry restates this in its own "Hit Dice:" line. | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (many independent restatements) |
| D. Maximum totals | Ch. 10, "Maximum Hit Points," p. 129; Maximum Hit Points (Humans) Table, p. 129; Maximum Hit Points (Demihumans) Table, p. 129 | RC states a maximum-possible total for any human character as the combination of nine Hit Dice rolled at maximum, Constitution bonuses, and the fixed higher-level gains; tabulated per class at levels 15/25/36, and separately for demihumans. Mystic HP follow the fighter's, capped at level 16 (stated total 113); druid HP follow the cleric's. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| D. Rerolls | *(no RC location found)* | No provision for rerolling a hit-point die was located. The DM is instructed to insist on witnessing the player's roll on gaining a level (Ch. 10, p. 129), which cuts against an implied reroll. | Unresolved by RC (negative finding) | DIRECT PRIMARY TEXT (the DM instruction) / negative search result for rerolls |
| F. Boundary with advancement | Ch. 1, "Maximum Levels and Experience Points," p. 12; Ch. 2 "Maximum Level:" lines | Level caps and Attack Rank progression are stated alongside HP/HD but govern advancement, not hit points as such — except where a cap determines how many Hit Dice are ever rolled (halfling 8, and see §9). | Rules Cyclopedia Explicit / boundary observation | DIRECT PRIMARY TEXT |

## 5. Highest-Priority Open Question — Answered at the Evidence Level

**Question:** Does RC's hit-point determination incorporate an ability-score-derived modifier, and if so, is the magnitude specified by the HP procedure itself or by the general ability-score-effects responsibility?

**Evidence-supported answer — both halves:**

1. **Yes, a modifier exists.** Constitution modifies hit points, stated in four independent RC locations, and named in the Abilities and Adjustments Table (p. 9) as an adjustment to "Hit Points per Experience Level."
2. **The magnitude is supplied by the general ability-score-effects material, not by the HP procedure.** RC's "Roll for Hit Points" step (p. 7) contains no value; it redirects the reader to the Bonuses and Penalties for Ability Scores Table (p. 9), which is the shared, all-abilities adjustment table sitting inside the material this project has assigned to `CHAR-007`. The Constitution write-up (p. 10) issues the same redirection.

**Scope qualification established at the same time:** the modifier applies only to rolled Hit Dice, never to the post-9th-level fixed gains, and never below a floor of 1 hit point per roll.

**Consequence for repository metadata — reported, not applied:** `INVENTORY.md` currently declares `CHAR-003`'s dependencies as `CHAR-002` only. On this evidence, `CHAR-003` **cannot** produce an authoritative hit-point value without the Constitution adjustment value owned by `CHAR-007`, so the current dependency row appears **incomplete**. This is exactly the possibility the cluster record preserved as an open question. Per the task's §14 and the cluster record's own instruction, **no metadata was changed** and no `CHAR-003 → CHAR-007` dependency was declared; the finding is escalated for human evidence review.

## 6. Research Questions Belonging to Other Rule Cards

- The Constitution adjustment table itself, and every other ability's effects → `CHAR-007`.
- Level caps, Attack Ranks, XP thresholds, and rate of advancement → `ADV-002` (and `ADV-001`).
- Saving throws and saving-throw progression → `COMBAT-004`. Saving-throw tables were encountered repeatedly adjacent to class Hit Dice lines in Chapter 2 and were deliberately not pursued.
- Damage, death, and 0-hit-point consequences → `COMBAT-003`/`COMBAT-009`.
- Healing and natural recovery → `COMBAT-005`.

## 7. Whole-Source Cross-Reference Pass

**Search terms used:** `Roll for Hit Points`; `Hit Dice and Hit Points`; `Character Class and Hit Dice`; `Hit Dice:`; `hit points`; `Constitution adjustment` (all hits reviewed); `Constitution adjustments no longer apply`; `hit points cannot be lowered` (1 hit); `Maximum Hit Points`; `up to 9th level`; `up to 8th level`; `pre-set number of hit points`; `Bonuses and Penalties for Ability Scores`; `maximum level`; `reroll` / `re-roll`.

**Sections inspected:** TOC; Tables index; Ch. 1 pp. 6–12 in full; Ch. 2 class entries for all seven creation-reachable classes (Requirements / Prime Requisite / Hit Dice / Maximum Level lines); Ch. 10 pp. 127–129 in full; Ch. 13 "Creating Characters"; Ch. 19 p. 266.

**Cross-references discovered:**
- **Ch. 1 p. 7 → Bonuses and Penalties for Ability Scores Table (p. 9)** — the load-bearing cross-reference for this card; the HP procedure is incomplete without it.
- Ch. 1 p. 7 table ↔ Ch. 2 per-class "Hit Dice:" lines — independently consistent for every class checked.
- Ch. 1 p. 12 ↔ Ch. 2 class entries ↔ Ch. 10 p. 129 — three-way agreement on the 9-Hit-Dice ceiling and the Constitution cut-off.
- Ch. 10 p. 129 → maximum-total tables, which fold in class HD, Constitution bonus, and post-cap gains.
- Ch. 19 p. 266 (Demihuman and Mystic Experience Levels variant) → contains its own elf hit-point statement above 9th level. This variant is **NOT ENABLED** for V1 per `DEC-0008`; noted only so a later reader does not mistake it for the core rule.

**Negative results:** no hit-point reroll provision; no ability other than Constitution was found to modify hit points; no maximum-per-die-roll cap beyond the die's own range; no HP variant in Ch. 19's enabled-for-V1 content.

## 8. Falsification Pass

**Challenge 1 — "Constitution modifies hit points."**
*Sought:* whether this applies to every character, every class, every level, and every score range. *Searched:* `Constitution adjustment` (all hits), Ch. 2 class entries, Ch. 1 pp. 10 and 12, Ch. 10 p. 129.
*Found:* a real and consistently stated limit — the adjustment applies only to rolled Hit Dice and explicitly ceases from 10th level, restated in every class entry.
**Disposition: QUALIFIED.** True, but bounded by level and by roll-versus-fixed-gain, not a blanket modifier.

**Challenge 2 — "The Constitution modifier's magnitude is part of the HP rule."**
*Sought:* any value stated within the HP procedure itself. *Searched:* Ch. 1 p. 7 read in full; Ch. 1 p. 10 Constitution section read in full.
*Found:* neither location states a value; both redirect to the shared adjustment table on p. 9.
**Disposition: REJECTED.** The magnitude is not part of the HP rule — this is the finding that drives §5's dependency conclusion.

**Challenge 3 — "Hit points could be reduced to zero or below by a Constitution penalty."**
*Sought:* a floor rule. *Searched:* `hit points cannot be lowered`, Ch. 1 p. 10 in context.
*Found:* an explicit floor of at least 1 hit point per roll.
**Disposition: REJECTED (a floor exists).** Recorded as a mechanical constraint that a naive "roll + modifier" reading would miss.

**Challenge 4 — "Hit Dice are rolled at every level."**
*Sought:* an upper bound. *Searched:* `up to 9th level`, `pre-set number of hit points`, Ch. 2 entries, Ch. 10 p. 129.
*Found:* rolling stops after 9th level (8th for halfling); fixed gains follow.
**Disposition: REJECTED as stated; replaced by the bounded finding.**

**Challenge 5 — "The per-class Hit Die values in the Ch. 1 table are complete and consistent with Chapter 2."**
*Sought:* disagreement between the p. 8 table and the class entries. *Searched:* each Ch. 2 class "Hit Dice:" line against the table.
*Found:* agreement for cleric, fighter, magic-user, thief, dwarf, elf, halfling. Druid's "does not apply" is consistent with its 9th-level-cleric entry requirement.
**Disposition: CONFIRMED.**

**Challenge 6 — "The demihuman maximum-hit-point figures are internally consistent."**
*Sought:* arithmetic agreement between Ch. 10's demihuman table and the class entries. *Searched:* Ch. 10 p. 129 table and prose; Ch. 1 p. 12; Ch. 2 elf and dwarf entries.
*Found:* **an unreconciled inconsistency** — see §9.
**Disposition: REJECTED — escalated, not reconciled.**

## 9. ⚠ Internal Source Conflict — Elf Maximum Level and Elf Maximum Hit Points

```text
STOP — INTERNAL SOURCE CONFLICT REQUIRES REVIEW
```

**The conflict, stated exactly:**

- Ch. 1, "Maximum Levels and Experience Points," p. 12 states that dwarves **and elves** may not progress beyond **12th** level.
- Ch. 2, the Elf class entry, states **Maximum Level: 10**, and the elf's own special-abilities text refers to reaching maximum level as 10th.
- Ch. 10, p. 129 prose states demihuman limits as halflings 8th, **elves 10th**, dwarves 12th.

Three locations say 10; one (Ch. 1 p. 12) says 12.

**A second, arithmetic inconsistency sits inside the same Ch. 10 table.** The Maximum Hit Points (Demihumans) Table carries a column headed for levels 10–12. Its elf row contributes +2 to a stated elf total of 83 (9 d6 Hit Dice at maximum = 54, plus a Constitution-18 bonus of 27, plus 2). But the Elf class entry grants **+1** hit point at 10th level, which — if the elf's maximum level is 10 — yields 82, not 83. The dwarf row is internally consistent on the same reading (72 + 27 + 9 = 108, over levels 10–12), and the halfling row is consistent with an 8th-level cap (48 + 24 = 72).

**Why this is not reconciled here.** RC states no precedence rule between a Chapter 1 summary and a Chapter 2 class entry, and inventing one would be a silent rules decision (`AGENTS.md` §3). The count of agreeing passages is evidence, not authority.

**Scope assessment, for the reviewer's triage:**
- The **core `CHAR-003` procedure is unaffected** — Hit Die by class, roll-per-level through the cap, the 1-hit-point floor, the Constitution adjustment and its cut-off are all consistent across every location inspected.
- The conflicting facts are the **elf level cap** (squarely `ADV-002`'s responsibility) and the **elf maximum-hit-point total** (a `CHAR-003`/`ADV-002` boundary figure).
- Stage B for `CHAR-003` should not fix elf-specific totals until this is adjudicated. Nothing else in this card is blocked.

## 10. Unresolved RC Questions

1. The elf conflict in §9 (escalated).
2. **Whether first-level hit points receive any special treatment** (e.g. maximum-at-first-level). No such provision was located; RC's text reads as a normal roll, but this is a negative finding, not an explicit RC statement.
3. **Whether the "at least 1 hit point per roll" floor also governs the post-9th fixed gains.** RC states the floor in terms of rolls, and the fixed gains are not rolls; the fixed values are all positive, so the question may be moot in practice, but RC does not address it.
4. **Whether "Creating High-Level Player Characters" (Ch. 10, p. 129) changes how a starting-above-1st-level character's hit points are generated** (rolled level-by-level versus otherwise). Not established in this pass.

`POTENTIAL COMPLETION QUESTION — NOT YET RESEARCHED` applies to items 2, 3, and 4. No alternate-source research was performed.

## 11. Alternate-Source Research Requirement

**Not established as required.** RC supplies the HP/HD procedure completely for the ordinary case. Item §9 is an internal-conflict/adjudication matter, not an RC silence; items §10.2–§10.4 would each need to be shown to be genuine RC gaps in Stage B before any gap-directed research is justified (`RULE_CARD_RESEARCH_PROTOCOL.md` §15).

## 12. Possible Simulator Ruling Areas (named, not drafted)

- The elf figures in §9, if human adjudication does not select a governing passage and no compatible source resolves it.
- The floor's applicability to fixed gains (§10.3), if it proves to matter.

Not drafted or proposed.

## 13. Legacy Rule Card Withholding

**Not applicable** — no prior `CHAR-003` Rule Card exists; none was consulted. (`INVENTORY_MIGRATION_MAP.md` records that the legacy entry's saving-throw half was already reassigned to `COMBAT-004`; that boundary was respected throughout and saving-throw material was not pursued.)

## 14. Confidence Assessment

**High** for the core procedure: Hit Die by class, per-level rolling through the 9th-level ceiling, fixed per-class gains thereafter, the Constitution adjustment and its explicit cut-off, and the 1-hit-point floor — each corroborated across two to four independent locations.

**Blocked** on elf-specific maximum figures pending §9's adjudication.

**Moderate** for §10.2–§10.4, which rest on negative searches.

## 15. Recommendation

```text
EVIDENCE READY FOR HUMAN REVIEW
```

**with one escalation the reviewer must adjudicate before Stage B:** the §9 internal source conflict. The core HP/HD procedure is ready; the elf maximum-level/maximum-hit-point figures are not, and were deliberately left unreconciled rather than resolved by agent judgement.
