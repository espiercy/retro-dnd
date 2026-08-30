# Rule Card: Hit Points & Hit Dice

## Rule ID

`CHAR-003`

## Title

Hit Points & Hit Dice

## Status

`AWAITING_APPROVAL`

> Stage-B draft, 2026-08-29. Stage-A evidence (`docs/rules/evidence/CHAR-003-evidence.md`) passed independent primary-source completeness review and human evidence review on 2026-08-29. **Not approved. Not implementable.**
>
> **`NOT READY FOR APPROVAL` — 2026-08-29 (corrected).** An earlier draft of this card specified the Elf's 10th-level fixed hit-point gain as **`+2`**, on the strength of a BECMI lineage claim that has since been shown false. **That specification is withdrawn.** Corrected research found the BECMI **Master** Set states `+1`, so the lineage is split and does **not** disambiguate RC. The value is now `UNRESOLVED — HUMAN RULING REQUIRED` (§4.1, W1). **This card cannot be approved until that ruling is made.** See `docs/rules/evidence/CHAR-003-elf-hp-alternate-source-research.md` §0 for the withdrawal record.

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

**Performed, for W1 only.** Full record, including the withdrawal of the first attempt: `docs/rules/evidence/CHAR-003-elf-hp-alternate-source-research.md`.

**Precondition satisfied.** Object-level RC exhaustion is established (`CLUSTER-002` Stage-A completeness `INDEPENDENT REVIEW — PASS`, 2026-08-29). RC does not *fail* to answer, it answers **inconsistently**, so BECMI was consulted to identify which RC presentation preserves the lineage mechanic — **not** as a substitute authority.

**Prior BECMI work (pre-2026-08-29) was not used**; `NOT VALID AS CURRENT SYNTHESIS INPUT` by human ruling.

> **⚠ The first version of this research was wrong and its conclusion is withdrawn.** It inspected only the **Expert** and **Companion** sets, found them to agree, and declared the BECMI lineage *"unanimous at +2"*. **It never dispositioned the Master Set.** The corrected audit dispositions **all five** BECMI volumes.

**Corrected source inventory — every core volume accounted for:**

| Volume | Levels | Elf fixed-gain statement | Verified |
|---|---|---|---|
| **Basic** (Set 1) | 1–3 | *None* — entry states only `Hit Dice: 1d6 per level`; **zero** `10th level` occurrences in the volume | Inspected |
| **Expert** (Set 2) p. 18 | 4–14 | *"1d6 per level, 9d6 maximum; **+2 hit points at 10th level**."* | **Visually** |
| **Companion** (Set 3) DM p. 22 | 15–25 | Demihuman maximum HP: **Elf 54 / 27 / +2 / 83** (no class HP line in this set) | **Visually** |
| **Master** (Set 4) p. 12 | 26–36 | *"1d6 per level through 9th level, modified by Constitution if applicable. **Add 1 hp at 10th level**, with no Constitution effect."* | **Visually** |
| **Immortals** (Set 5) | post-36 | *None* — **zero** occurrences of "elf" in the volume | Inspected |

**BECMI is NOT unanimous.** It **revised** the rule: `+2` (Expert, Companion) → `+1` (Master). Master's Elf Experience Table also revises the Elf's spell progression in the same object, so this is a deliberate change, not a slip.

**Master additionally carries a conflict-precedence rule** (Players' Book p. 2, visually verified): *"If you discover a contradiction between this set and previous sets, the rules given here should be used."* Recorded as a source fact; **not applied to RC** — it is a BECMI-internal instruction, and RC does not incorporate it.

**B/X, Holmes and OD&D remain not consulted.** The disagreement is *inside* BECMI; a lower-priority edition cannot settle which BECMI branch RC intended.

## Compatibility Analysis

| Finding | Classification (`SOURCE_HIERARCHY.md` §6) |
|---|---|
| Expert `+2` → Companion `+2` | **Preserved** within BECMI |
| Companion `+2` → **Master `+1`** | **Evolved-Different** — a deliberate revision within the lineage |
| BECMI Companion p. 22 table → RC p. 129 | **Preserved** — reproduced number for number, header and note included; carries `+2` into RC |
| **BECMI Expert Elf Experience Table → RC p. 26** | **Preserved** — RC's level-10 spell row is `3 3 3 3 2`, matching **Expert**; Master's is `5 4 3 2 1`. **RC did not adopt Master's revised Elf table** |
| BECMI Master p. 12 → RC p. 25 stat block / RC p. 130 Step 6 | **Preserved** — carries `+1` into RC |
| Other classes' fixed gains (Cleric +1, Fighter +2, Magic-user +1, Dwarf +3) | **Preserved** — but **non-discriminating**: Expert and Master agree for those classes, so RC matching them says nothing about which Elf branch RC follows |

**Net effect: RC inherited from both branches and reconciled neither.** That explains the contradiction; it does not resolve it. **No mechanic is imported and no value is selected.**

---

## Simulator Ruling

**Not applicable — no ruling is proposed, and none may be.**

W1 now meets §16's *preconditions* (RC research complete, falsification done, gap-directed research performed and **inconclusive**). But §16 also forbids self-approval, and this question is not a gap in the rules requiring an invented mechanic — it is a choice between **two values RC itself explicitly states**. That is a **human adjudication**, of exactly the kind already made for the Elf and Druid maximum levels. It is escalated, not ruled on.

W2 and W3 require no ruling; see Open Questions.

## Human-Approved Variant

Not applicable. Selecting either RC value would not be a departure from an explicit RC rule — it would select between two things RC explicitly states.

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
| **Elf** | **`UNRESOLVED — HUMAN RULING REQUIRED`** — see §4.1. Candidate values `+1` or `+2`; **neither is specified** | **10 only** |
| Halfling | *(none — maximum level equals Name level)* | — |
| Mystic | +2 | 10–16 |
| Druid | as cleric to the point of becoming a druid, then +1 | 10–36 |

**Constitution never applies to any value in this table.**

#### 4.1 The Elf's fixed gain — `UNRESOLVED`

```text
Elf fixed HP at 10th level:  UNRESOLVED — HUMAN RULING REQUIRED
```

**No value is specified.** An implementation must treat this as an unset parameter that **fails loudly**; it must not default to either candidate.

**Both RC sides, preserved:**

| Value | RC objects |
|---|---|
| **`+1`** | p. 25 Elf **stat block**; p. 130 **Step 6** high-level procedure |
| **`+2`** | p. 25 Elf **Class Details prose**; p. 129 **Maximum Hit Points (Demihumans)** calculation (54 + 27 + 2 = 83) |

All four visually verified as printed; the p. 25 pair contradict each other **on one page**.

**Corrected lineage evidence — it does not settle the question:**

| BECMI volume | Value | Bearing |
|---|---|---|
| Expert p. 18 | `+2` | Originating statement |
| Companion DM p. 22 | `+2` | Preserved; **inherited verbatim into RC p. 129** |
| **Master p. 12** | **`+1`** | **Deliberate revision** — the same table also revises Elf spell progression |
| Master p. 2 | *precedence rule* | *"If you discover a contradiction between this set and previous sets, the rules given here should be used"* — **BECMI-internal; not incorporated by RC** |

**Why lineage does not decide it.** RC is a composite: p. 129 descends from the Companion (`+2`), the stat block and Step 6 track Master (`+1`) — and **RC p. 26's Elf Experience Table descends from *Expert*, not Master** (RC's level-10 spell row is `3 3 3 3 2`, Expert's exactly; Master's is `5 4 3 2 1`). So RC did **not** wholesale adopt Master's revised Elf, and "Master is later" does not establish what RC intends.

**Explicitly not used to select a value:** majority-counting; privileging tables over prose or prose over tables; the p. 129 arithmetic; Master's precedence rule; recency. `RULE_CARD_RESEARCH_PROTOCOL.md` §9.6 and §10.2.2 case 2 forbid an agent choosing between conflicting passages on such grounds, and the earlier draft of this card did exactly that on evidence that proved incomplete.

**Impact if ruled:** whichever value is chosen, only §4's Elf row, §6's Elf row, and tests H22–H23 change. Nothing else in this card depends on it.

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
| **Elf** | 54 | 27 | **`+2` as printed by RC** | **`83` as printed by RC** |
| Halfling | 48 | 24 | — | 72 |

**The Elf row is reproduced as RC prints it and is NOT a specification of the §4.1 value.** RC's printed total `83` is arithmetically consistent with `+2` and inconsistent with `+1` (which yields 82). **That arithmetic is recorded, not used** — this table is itself one of the four contested statements, inherited verbatim from BECMI Companion p. 22, so treating its internal consistency as decisive would beg the question W1 asks. Until W1 is ruled, the Elf row is evidence, not a check value.

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

### The Elf fixed gain (W1) — **guard tests, no value asserted**

> These were previously written as `+2` assertions. **That is withdrawn.** They are now guards, so the card cannot be approved or implemented while silently carrying either candidate.

| # | Case | Expected |
|---|---|---|
| H22 | Elf advancing 9 → 10 | **Raises/returns `UNRESOLVED`** (W1). Must **not** return 2, and must **not** return 1 |
| H23 | Elf, 18 Con, all nine d6 = 6, advanced to level 10 | **Raises/returns `UNRESOLVED`.** Neither `83` (`+2`) nor `82` (`+1`) may be produced |
| H24 | Elf at level 10 | No further hit points — maximum level; Attack Ranks confer none. **Unaffected by W1** |
| H25 | Any Elf hit-point total at level 10 hard-coded to `83` **or** `82` | **Contract violation** — a concrete total may exist only after W1 is ruled |
| H26 | Elf advancing 1 → 9 | Fully specified and testable — nine d6 rolls with Constitution. **W1 blocks only the 10th-level step** |

**After a ruling**, H22/H23 become value assertions again (`+2` → 83, or `+1` → 82) and H25 is narrowed to the rejected value. Until then, no expected total for a 10th-level Elf exists.

### Maximum-total regressions (RC p. 129)

> The **Elf row is deliberately absent** from this block — it is blocked by W1 and is covered by guard tests H22–H25 instead. Every other class is unaffected by W1 and fully testable.

| # | Case | Expected |
|---|---|---|
| H27 | Fighter, 18 Con, nine d8 = 8, level 36 | **153** = 72 + 27 + 54 |
| H28 | Cleric, 18 Con, nine d6 = 6, level 36 | **108** = 54 + 27 + 27 |
| H29 | Magic-User, 18 Con, nine d4 = 4, level 36 | **90** = 36 + 27 + 27 |
| H30 | Thief, 18 Con, nine d4 = 4, level 36 | **117** = 36 + 27 + 54 |
| H31 | Dwarf, 18 Con, nine d8 = 8, level 12 | **108** = 72 + 27 + 9 |
| H32 | Halfling, 18 Con, eight d6 = 6, level 8 | **72** = 48 + 24 |
| H33 | Cleric, 18 Con, nine d6 = 6, level 15 | **87** |
| H34 | Cleric at level 25 | **97** |

### Dependency and prohibitions

| # | Case | Expected |
|---|---|---|
| H35 | `CHAR-003` invoked without a `CHAR-007` Constitution adjustment | **Contract violation** — this card cannot produce an authoritative value alone |
| H36 | Constitution 9–12 | Adjustment 0; totals equal the raw dice sum |
| H37 | Any attempt to reroll a hit-point die | **Rejected** — no reroll provision exists |
| H38 | Druid requested at 1st level | **Rejected** — no Druid Hit Die (`CHAR-002`) |
| H39 | Druid reached from cleric at 9th, advancing to 10th | Cleric progression to that point, then +1/level |
| H40 | Chapter 19 extended-progression figures used | **Rejected** — variant `NOT ENABLED` for V1 |
| H41 | Chapter 19 **Extended Experience Table** (RC p. 266) figures used for the Elf | **Rejected** — that variant is `NOT ENABLED`, its per-level figures differ, and it **must not** be used to resolve W1 |

## Provenance Classification

| Element | Classification |
|---|---|
| §1 Hit Dice; §2/§3 rolling; §4 fixed gains for all classes **except the Elf**; §5 Constitution boundary; §6 totals; §7 Ch. 10 construction | **Rules Cyclopedia Explicit** |
| The 1-hp floor; the 9-dice ceiling | **Rules Cyclopedia Explicit** |
| **§4.1 Elf fixed gain** | **UNRESOLVED — no classification.** RC states both values explicitly and the BECMI lineage is itself split (`+2` Expert/Companion, `+1` Master), so no provenance category applies until a human ruling selects a value. It is **not** an Alternate-Source Compatible Completion (RC is not silent), **not** a Simulator Ruling (no mechanic is missing), and **not** a Human-Approved Variant (either choice is an RC value) |
| Elf maximum level 10, Druid maximum level 36 | **Human adjudication**, 2026-08-29, recorded against `ADV-002` |
| W2, W3 | **Unresolved by RC** |

---

## Open Questions

1. **W1 — the Elf's fixed gain. `HUMAN RULING REQUIRED` — this card cannot be approved until it is made.** Classification **B** (blocks Rule Card approval): the Elf is core V1 content and this is a value the specification must state. RC gives `+1` twice and `+2` twice; BECMI **also** splits (`+2` Expert/Companion → `+1` Master), and RC demonstrably inherited from both branches, so lineage does not decide it. Both cases are laid out in §4.1 and in the research record's "evidence for each choice" table. **No value is written into the specification, and none is defaulted.** Guarded by H22–H25.
2. **W2 — does the 1-hp floor govern fixed gains?** Currently **moot** — every fixed gain is positive. No specification depends on it. Revisit only if a future rule can produce a negative fixed gain.
3. **W3 — is Chapter 10 Step 6 an alternative or a restatement?** Not wired to V1, so nothing depends on it. Both readings agree on outputs for a maximum-level character; they differ only in the DM conventions Step 6 adds.

**Explicitly closed:** whether first-level hit points get special treatment (**no**); whether any reroll provision exists (**no**); whether any ability besides Constitution modifies hit points (**no**); whether the Druid's hit points differ from the cleric's (**no** — as cleric, then +1/level).

## Approval

- Approved by: `<pending>`
- Date: `<pending>`
- Notes: `<pending>`

**`NOT READY FOR APPROVAL`.** W1 must be ruled first — the card carries no Elf 10th-level value and will not silently supply one. W2 and W3 remain open but block nothing.
