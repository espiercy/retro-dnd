# Rule Card: Hit Points & Hit Dice

## Rule ID

`CHAR-003`

## Title

Hit Points & Hit Dice

## Status

`AWAITING_APPROVAL`

> Stage-B draft, 2026-08-29. Stage-A evidence (`docs/rules/evidence/CHAR-003-evidence.md`) passed independent primary-source completeness review and human evidence review on 2026-08-29. **Not approved. Not implementable.**
>
> **This card carries one proposed resolution of a genuine RC self-contradiction** — the Elf's fixed hit-point gain at 10th level. See §4.1 and Open Question W1. Approving this card ratifies that resolution; it should be approved deliberately, not incidentally.

## Rules Domain

`character_creation`

---

## Rules Cyclopedia Source

| Page | Object | Bearing |
|---|---|---|
| p. 7 | Ch. 1, "Roll for Hit Points" | The procedure; its redirection to the p. 9 adjustment table |
| **p. 8** | **Character Class and Hit Dice Table** | Hit Die by class; Druid "Does not apply" |
| **p. 9** | **Bonuses and Penalties for Ability Scores Table** | The Constitution adjustment value — owned by `CHAR-007`, consumed here |
| p. 10 | Ch. 1, "Constitution" | The 1-hit-point floor; the high-level cut-off |
| p. 12 | Ch. 1, "Hit Dice and Hit Points" | Per-level rolling to Name level; Constitution applies only to rolled dice |
| pp. 13–31 | Ch. 2 per-class entries, "Hit Dice:" lines | Per-class restatement, incl. the contested Elf statements at p. 25 |
| **p. 129** | **Maximum Hit Points (Humans)** and **Maximum Hit Points (Demihumans)** Tables | Maximum totals; the Elf row's `+2` |
| **p. 130** | Ch. 10, **Step 6: Find Total Hit Points** + per-class box | Independent restatement; averaging conventions; the per-class fixed gains |

**Verification standard.** Pages 7, 8, 9, 10, 12, 25, 129 and 130 were read as page images.

## Rules Cyclopedia Explicitly Establishes

1. **Hit Die by class** (p. 8 table, corroborated by every Ch. 2 class entry).
2. **Starting hit points**: roll the class Hit Die once and apply the Constitution adjustment.
3. **Per-level rolling**: one Hit Die per experience level gained, through **Name level** — 9th for every class except the halfling, whose Name level and maximum level are both **8**.
4. **The Constitution adjustment applies to each rolled die**, and its magnitude is **not** stated by the hit-point procedure. RC redirects to the Bonuses and Penalties for Ability Scores Table (p. 9). This is the load-bearing cross-reference for this card.
5. **A floor of 1 hit point per roll**: *"whatever the adjustments, your hit points cannot be lowered to 0 (zero); you will have at least 1 hit point for each roll."*
6. **Above Name level, no dice are rolled.** A fixed per-class gain applies instead, and **Constitution does not modify it** — stated at p. 12, in every Ch. 2 class entry, and again at p. 130 (*"Hit point bonuses above 9th level are not modified by Constitution"*).
7. **Fixed gains per class** (p. 130 box, corroborated by the Ch. 2 entries): Cleric +1/level; Fighter +2/level; Magic-user +1/level; Thief +2/level; Dwarf +3/level up to 12th; Halfling — none; Mystic +2/level; Druid as cleric, then +1/level. **The Elf's value is contested — §4.1.**
8. **Maximum totals** (p. 129), for 18 Constitution and maximum die rolls: Cleric 54/27 → 87/97/108 at levels 15/25/36; Fighter 72/27 → 111/131/153; Magic-user 36/27 → 69/79/90; Thief 36/27 → 75/95/117; Dwarf 72/27/+9 → 108; **Elf 54/27/+2 → 83**; Halfling 48/24 → 72.
9. **No reroll provision.** None was located, and RC instructs the DM to witness the player's roll on gaining a level — which cuts against an implied reroll.
10. **Druid has no starting Hit Die** (p. 8, "Does not apply"), consistent with the class being unreachable at creation (`CHAR-002`).

## Rules Cyclopedia Leaves Undefined / Ambiguous

**W1 — The Elf's fixed hit-point gain at 10th level: RC states it as `+1` twice and as `+2` twice.**

| RC location | Object type | Value |
|---|---|---|
| p. 25, Elf stat block "Hit Dice:" line | Stat block | **+1** |
| p. 25, Elf Class Details prose | Detailed prose | **+2** ("Two additional hit points are gained at 10th level") |
| p. 129, Maximum Hit Points (Demihumans), Elf row | Table | **+2** (54 + 27 + 2 = 83) |
| p. 130, Step 6 per-class box | Procedural list | **+1** |

All four are visually verified as printed. The first two are on the **same page**. This is a genuine primary-source contradiction, not a research artifact: `SOURCE COMPLETE ≠ SOURCE UNAMBIGUOUS` (`RULE_CARD_RESEARCH_PROTOCOL.md` §10.2.2 case 3, for which this is the protocol's own named reference case).

**W2 — Whether the 1-hit-point floor governs the fixed gains.** RC states the floor in terms of *rolls*, and the fixed gains are not rolls. Every fixed gain RC states is positive, so the question is currently **moot in practice**; it would become live only if a future rule produced a negative fixed gain.

**W3 — Whether Chapter 10 Step 6 is an alternative construction or a restatement.** Its outputs agree with the level-by-level method for a maximum-level character, but it adds DM conventions (treating 1s as 2s, or averaging) that the ordinary method does not have.

---

## Alternate-Source Completion Research

**Performed, for W1 only.** Full record: `docs/rules/evidence/CHAR-003-elf-hp-alternate-source-research.md`.

**Precondition satisfied.** Object-level RC exhaustion is established (`CLUSTER-002` Stage-A completeness `INDEPENDENT REVIEW — PASS`, 2026-08-29). The gap has an unusual shape and it was stated precisely: RC does not *fail* to answer, it answers **inconsistently**, so BECMI is used to identify which RC presentation preserves the lineage mechanic — **not** as a substitute authority.

**Prior BECMI work was not used.** The earlier research produced from the invalid RC-exhaustion conclusion is `NOT VALID AS CURRENT SYNTHESIS INPUT` (human ruling). This research was performed anew from the corrected RC evidence state, and inherited no conclusion from it.

**Sources, in `SOURCE_HIERARCHY.md` §3 order:**

| Source | Object | Statement | Verified |
|---|---|---|---|
| *D&D Set 2: Expert Rules* (Mentzer, TSR, 1983), Players Manual **p. 18** | Elf class entry, "Hit Dice:" line | *"1d6 per level, 9d6 maximum; **+2 hit points at 10th level**."* | **Visually** |
| Same page | Elf Experience Table | Levels **1–10**, terminating at `10* 10th Level Lord Wizard 600,000`; footnote *"Constitution adjustments no longer apply"* | **Visually** |
| Same page | Dwarf "Hit Dice:" line | *"1d8 per level, 9d8 maximum; +3 hit points per level thereafter"* | **Visually** |
| *D&D Set 3: Companion Rules* (Mentzer, TSR, 1984), DM's Book **p. 22** | Demihuman maximum hit points | Dwarf 72/27/+9/108; **Elf 54/27/+2/83**; Halfling 48/24/–/72 | **Visually** |
| Same book, **p. 23** | Hit Roll Charts, Elf column | Attack Ranks C–M at 600/850/1,100/…/3,100 thousand XP | **Visually** |

**B/X, Holmes and OD&D were not consulted, deliberately.** BECMI is the highest-priority lineage source and answered the exact question unanimously with no internal conflict; descending further would be the broad edition browse §15 prohibits. Recorded as a scope boundary, not an omission.

**No BECMI statement of `+1` was located** after inspecting the complete Elf entry, every `Hit Dice:` line and every `10th level` occurrence in the Expert Players Manual, and the Companion's demihuman material. Stated as a research-operation claim, per Guardrail B.

## Compatibility Analysis

| Finding | Classification (`SOURCE_HIERARCHY.md` §6) |
|---|---|
| BECMI Elf `+2 hit points at 10th level` versus RC's `+2` statements | **Preserved** — RC carries the BECMI mechanic forward in two of its four statements |
| BECMI demihuman maximum-HP table versus RC p. 129 | **Preserved** — RC p. 129 reproduces BECMI Companion p. 22 number for number, including the shared `L 10-12` column header and the explanatory note |
| BECMI Elf Attack Rank thresholds versus RC p. 26 | **Preserved** — identical XP progression; corroborates direct descent, though it does not itself bear on the HP value |
| Every other class's fixed gain (Cleric +1, Fighter +2, Magic-user +1, Dwarf +3) | **Preserved** — RC matches BECMI exactly for all four; the Elf is the sole discrepancy |
| Any Evolved-Different or Conflicting finding | **None** |

No mechanic is imported. Nothing encountered incidentally in BECMI — strongholds, Clans, Combat Options, breath-weapon resistance — is used.

---

## Simulator Ruling

**Not applicable — none proposed.** W1 is resolved by lineage evidence, so §16's precondition (gap-directed research having failed) is not met. W2 and W3 do not require rulings; see Open Questions.

## Human-Approved Variant

Not applicable. Selecting the `+2` reading is **not** a departure from an explicit RC rule — it selects between two things RC itself explicitly states.

---

## Approved Mechanical Specification

### 1. Hit Die by class

| Class | Hit Die | Name level | Maximum level |
|---|---|---|---|
| Cleric | d6 | 9 | 36 |
| Fighter | d8 | 9 | 36 |
| Magic-User | d4 | 9 | 36 |
| Thief | d4 | 9 | 36 |
| Dwarf | d8 | 9 | 12 |
| Elf | d6 | 9 | **10** |
| Halfling | d6 | **8** | **8** |
| Mystic | d6 | 9 | 16 |
| Druid | *(does not apply — enters at 9th as a cleric)* | 9 | **36** |

Maximum levels are **`ADV-002`'s** authoritative property, consumed here because they bound how many fixed gains accrue. The **Elf 10** and **Druid 36** values are human adjudications (2026-08-29) and are not reopened.

### 2. First level

```text
hp = max(1, roll(class_hit_die) + con_adjustment)
```

`con_adjustment` is supplied by `CHAR-007` from the Bonuses and Penalties for Ability Scores Table. **This card does not define its magnitude** — that is the whole basis of the `CHAR-003 → CHAR-007` dependency.

**No special first-level treatment exists.** No maximum-at-first-level rule was located in any governing object; the first roll is an ordinary roll.

### 3. Levels 2 through Name level — rolled

For each level gained from 2 to Name level inclusive:

```text
hp += max(1, roll(class_hit_die) + con_adjustment)
```

- The floor applies **per roll**, not to the running total.
- `con_adjustment` is re-read at each application; if the character's Constitution has changed, the current value governs.
- Total dice ever rolled: **9** for every class except the halfling's **8**.
- **No reroll is permitted.**

### 4. Above Name level — fixed, unmodified gains

For each level gained above Name level, up to the class maximum:

```text
hp += fixed_gain(class)          # no die, no Constitution adjustment
```

| Class | Fixed gain per level above Name level | Levels it applies to |
|---|---|---|
| Cleric | +1 | 10–36 |
| Fighter | +2 | 10–36 |
| Magic-User | +1 | 10–36 |
| Thief | +2 | 10–36 |
| Dwarf | +3 | 10–12 |
| **Elf** | **+2** — *proposed, see §4.1* | **10 only** |
| Halfling | *(none — maximum level equals Name level)* | — |
| Mystic | +2 | 10–16 |
| Druid | as cleric to the point of becoming a druid, then +1 | 10–36 |

**Constitution never applies to any value in this table.**

#### 4.1 The Elf's `+2` — a proposed resolution, not a settled RC fact

RC says `+1` twice and `+2` twice (W1). **`+2` is specified here on the following basis, which the approver is ratifying:**

- BECMI is **unanimous at +2** across two independent objects in two different books, with no BECMI `+1` statement located.
- RC p. 129's demihuman table — one of the two RC `+2` statements — is a **verbatim descendant** of BECMI Companion p. 22: every number in both its tables, the shared column header, and the explanatory note are identical. Its `83` total is itself inherited and is internally consistent only with `+2`.
- RC **preserves BECMI's fixed gain unchanged for every other class checked** (Cleric, Fighter, Magic-user, Dwarf). An Elf-only change would be the sole departure.
- RC's own Elf Class Details prose states `+2` in RC's own words, contradicting the stat block **on the same page**.

**The competing reading, stated fairly:** RC may have *deliberately* reduced the Elf's gain to `+1` and failed to update the inherited p. 129 table, leaving `83` stale. That is coherent and cannot be excluded from the text alone. It is weaker because it requires an unannounced class-specific change that is the only departure from BECMI across five classes, was not propagated to the table RC reprinted from the very source being revised, and is contradicted within its own page. **But it is not impossible, and this card does not pretend otherwise.**

Neither majority-counting nor arithmetic consistency was used to select the value; the argument is genealogical, and its source facts and editorial inferences are separated in the research record.

`STOP — INTERNAL SOURCE CONFLICT REQUIRES REVIEW` is **not** triggered: §10.2.2 case 2 prohibits an agent *silently* choosing between conflicting passages. Nothing here is silent.

### 5. Constitution's boundary

| Applies to | Yes/No |
|---|---|
| Each rolled Hit Die, levels 1 through Name level | **Yes** |
| Fixed gains above Name level | **No** |
| Any total after the fact | **No** — it is applied per roll, never to a sum |

### 6. Maximum totals (informative, for verification only)

RC p. 129, for 18 Constitution (+3) and maximum die rolls. These are **check values**, not an alternative procedure.

| Class | 9 dice | Con | L15 | L25 | L36 |
|---|---|---|---|---|---|
| Cleric | 54 | 27 | 87 | 97 | 108 |
| Fighter | 72 | 27 | 111 | 131 | 153 |
| Magic-User | 36 | 27 | 69 | 79 | 90 |
| Thief | 36 | 27 | 75 | 95 | 117 |

| Class | Dice | Con | Above Name level | Maximum |
|---|---|---|---|---|
| Dwarf | 72 | 27 | +9 | 108 |
| **Elf** | 54 | 27 | **+2** | **83** |
| Halfling | 48 | 24 | — | 72 |

**The Elf row reproduces the §4.1 resolution and is consistent with it.** Under the `+1` reading this row would read 82, contradicting RC's printed total.

### 7. Above-1st-level construction (Chapter 10 Step 6) — specified, not V1-wired

When the DM creates a character starting above 1st level, RC supplies an equivalent construction: roll hit points up to Name level within the DM's sight (nine rolls for any human, dwarf or elf; eight for a halfling), optionally treating 1s as 2s (or 2s as 3s), or using the averaging convention — average per die (2½ for d4, 3½ for d6, 4½ for d8) **plus 1½**, multiplied by the number of Hit Dice. Then apply the Constitution adjustment multiplied by the number of dice rolled, and add the fixed gains for each level above Name level, unmodified by Constitution.

**W3 is unresolved**: whether this is an alternative to §2–§4 or a restatement of it. It is **not** wired to any V1 flow by this card.

### 8. Out of scope

Saving throws and saving-throw progression (`COMBAT-004`) — deliberately not pursued despite sitting adjacent to Hit Dice in every Ch. 2 entry. The Constitution adjustment table itself (`CHAR-007`). Level caps, Attack Ranks, XP (`ADV-002`, `ADV-001`). Damage, death, 0-hp consequences (`COMBAT-003`, `COMBAT-009`). Healing (`COMBAT-005`). The Chapter 19 extended demihuman/Mystic progression variant — **`NOT ENABLED` for V1** (`DEC-0008`); its own per-level hit-point figures differ and **must not** be confused with these.

---

## Deterministic Test Cases

### First level

| # | Class, Con adj., die result | Expected |
|---|---|---|
| H1 | Fighter, +0, d8 = 5 | 5 |
| H2 | Fighter, +3, d8 = 8 | 11 |
| H3 | Magic-User, −3, d4 = 1 | **1** — floor, not −2 |
| H4 | Magic-User, −3, d4 = 4 | **1** — floor, not 1… (4 − 3 = 1, floor coincides) |
| H5 | Magic-User, −2, d4 = 1 | **1** — floor |
| H6 | Cleric, −1, d6 = 1 | **1** — floor |
| H7 | Cleric, +1, d6 = 1 | 2 — floor not engaged |
| H8 | Thief, +0, d4 = 4 | 4 |

### Per-roll floor

| # | Case | Expected |
|---|---|---|
| H9 | Magic-User, Con −3, levels 1–3, d4 = `1,1,1` | **3** total (1 per level) — **not** `3 − 9` and **not** floored once at 1 |
| H10 | Same, d4 = `4,4,4` | **3** total — each roll floors independently |
| H11 | Same, d4 = `4,1,4` | **3** total |

### Rolling ceiling

| # | Case | Expected |
|---|---|---|
| H12 | Fighter advancing 1 → 12 | Exactly **9** d8 rolls consumed (levels 1–9); levels 10, 11, 12 consume **no** dice |
| H13 | Halfling advancing 1 → 8 | Exactly **8** d6 rolls; no fixed gains ever |
| H14 | Halfling at level 8 | No further hit points from any source in this card |
| H15 | Elf advancing 1 → 10 | Exactly **9** d6 rolls, then one fixed gain |

### Fixed gains and the Constitution cut-off

| # | Case | Expected |
|---|---|---|
| H16 | Fighter, Con +3, levels 10 → 12 | **+6** total (2 per level), **not** +15 — Constitution does not apply |
| H17 | Dwarf, Con −3, levels 10 → 12 | **+9** total (3 per level), **not** 0 — the penalty does not apply either |
| H18 | Cleric, levels 10 → 36 | +27 total |
| H19 | Mystic, levels 10 → 16 | +14 total |
| H20 | Dwarf at level 12 | No further gains — maximum level reached |
| H21 | Thief, levels 10 → 36 | +54 total (2 per level) — Thief is **+2**, not +1 |

### The Elf resolution (W1)

| # | Case | Expected |
|---|---|---|
| H22 | Elf advancing 9 → 10 | **+2** hit points, unmodified by Constitution |
| H23 | Elf, 18 Con, all nine d6 = 6, advanced to level 10 | **83** = 54 + 27 + 2 — reproduces RC p. 129's printed total exactly |
| H24 | Elf at level 10 | No further hit points — maximum level; Attack Ranks confer none |
| H25 | Regression guard | If §4.1 is ever changed to `+1`, H23 must fail with 82 ≠ 83 — the test exists to make the resolution's reversal visible rather than silent |

### Maximum-total regressions (RC p. 129)

| # | Case | Expected |
|---|---|---|
| H26 | Fighter, 18 Con, nine d8 = 8, level 36 | **153** = 72 + 27 + 54 |
| H27 | Cleric, 18 Con, nine d6 = 6, level 36 | **108** = 54 + 27 + 27 |
| H28 | Magic-User, 18 Con, nine d4 = 4, level 36 | **90** = 36 + 27 + 27 |
| H29 | Thief, 18 Con, nine d4 = 4, level 36 | **117** = 36 + 27 + 54 |
| H30 | Dwarf, 18 Con, nine d8 = 8, level 12 | **108** = 72 + 27 + 9 |
| H31 | Halfling, 18 Con, eight d6 = 6, level 8 | **72** = 48 + 24 |
| H32 | Cleric, 18 Con, nine d6 = 6, level 15 | **87** |
| H33 | Cleric at level 25 | **97** |

### Dependency and prohibitions

| # | Case | Expected |
|---|---|---|
| H34 | `CHAR-003` invoked without a `CHAR-007` Constitution adjustment | **Contract violation** — this card cannot produce an authoritative value alone |
| H35 | Constitution 9–12 | Adjustment 0; totals equal the raw dice sum |
| H36 | Any attempt to reroll a hit-point die | **Rejected** — no reroll provision exists |
| H37 | Druid requested at 1st level | **Rejected** — no Druid Hit Die (`CHAR-002`) |
| H38 | Druid reached from cleric at 9th, advancing to 10th | Cleric progression to that point, then +1/level |
| H39 | Chapter 19 extended-progression figures used | **Rejected** — variant `NOT ENABLED` for V1 |

## Provenance Classification

| Element | Classification |
|---|---|
| §1 Hit Dice; §2/§3 rolling; §4 fixed gains for all classes **except the Elf**; §5 Constitution boundary; §6 totals; §7 Ch. 10 construction | **Rules Cyclopedia Explicit** |
| The 1-hp floor; the 9-dice ceiling | **Rules Cyclopedia Explicit** |
| **§4.1 Elf `+2`** | **Rules Cyclopedia Explicit (contested passage), selected by closest-lineage disambiguation.** RC remains primary; BECMI identified which RC statement preserves the mechanic. **Not** an Alternate-Source Compatible Completion — RC is not silent here — and **not** a Human-Approved Variant |
| Elf maximum level 10, Druid maximum level 36 | **Human adjudication**, 2026-08-29, recorded against `ADV-002` |
| W2, W3 | **Unresolved by RC** |

---

## Open Questions

1. **W1 — the Elf's fixed gain.** §4.1 proposes `+2` on lineage grounds. **This is the one substantive interpretive call in this cluster, and approving this card ratifies it.** The competing `+1` reading is recorded in §4.1 and in the research record; test H25 exists so a future reversal is loud rather than silent. If the reviewer prefers `+1`, only §4.1, the §4 table row, §6's Elf row, and tests H22/H23 change.
2. **W2 — does the 1-hp floor govern fixed gains?** Currently **moot** — every fixed gain is positive. No specification depends on it. Revisit only if a future rule can produce a negative fixed gain.
3. **W3 — is Chapter 10 Step 6 an alternative or a restatement?** Not wired to V1, so nothing depends on it. Both readings agree on outputs for a maximum-level character; they differ only in the DM conventions Step 6 adds.

**Explicitly closed:** whether first-level hit points get special treatment (**no**); whether any reroll provision exists (**no**); whether any ability besides Constitution modifies hit points (**no**); whether the Druid's hit points differ from the cleric's (**no** — as cleric, then +1/level).

## Approval

- Approved by: `<pending>`
- Date: `<pending>`
- Notes: `<pending>`

**Approving this card ratifies the Elf `+2` resolution in §4.1.** It does not resolve W2 or W3.
