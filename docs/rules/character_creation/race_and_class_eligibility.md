# Rule Card: Race & Class Eligibility

## Rule ID

`CHAR-002`

## Title

Race & Class Eligibility

## Status

`AWAITING_APPROVAL`

> Stage-B draft, 2026-08-29. Stage-A evidence (`docs/rules/evidence/CHAR-002-evidence.md`) passed independent primary-source completeness review and human evidence review on 2026-08-29. **Not approved. Not implementable.**
>
> **Stage-B correction impact (2026-08-29): NONE substantive.** The research failure and its correction concern the Elf's fixed hit-point gain (`CHAR-003`) and `CHAR-001`'s Mystic trade question. **Neither touches this card** — eligibility is decided entirely by raw-score thresholds, no hit-point value enters it, and the Elf and Druid **maximum levels** (10 and 36) are settled human adjudications the correction did not disturb.
>
> **Two documentation clarifications from human rulings on `CHAR-001`; no eligibility threshold changed by either.**
> **SR-3** — §1's input is stated explicitly as the scores **after any authorized Chapter 13 switch** and **before** the Chapter 1 trade. Former open question V1 is `RESOLVED`.
> **SR-5** — §4.1 records that this card's result is an **invariant the subsequent trade must preserve**. The adjustment procedure stays entirely with `CHAR-001`, and **no `CHAR-002 → CHAR-007` dependency is created**.
>
> **`READY FOR HUMAN RULE-CARD REVIEW`.**

## Rules Domain

`character_creation`

---

## Rules Cyclopedia Source

| Page | Object | Bearing |
|---|---|---|
| p. 6 | Ch. 1, "Choose a Character Class" | The nine classes; race/class unification; the human-class exemption |
| **p. 7** | **Character Classes and Ability Requirements Table** | The principal governing object: prime requisite(s) and Other Requirements per class |
| p. 7 | Ch. 1 per-class descriptions | Each minimum restated in prose, with its failure condition |
| p. 8 | **Character Class and Hit Dice Table** | Druid's Hit Die marked "Does not apply" — corroborates non-reachability at creation |
| p. 12 | **Experience Bonuses and Penalties Table** | Establishes what prime requisites *do*, hence what they are not (`ADV-001`) |
| **pp. 28–29** | **Complete Druid class entry** | Transition requirements beyond the p. 7 table |
| **pp. 29–31** | **Complete Mystic class entry** | Confirms p. 7 complete for Mystic *creation eligibility*; adds downstream material |
| p. 145 | Ch. 13, "Creating Characters" | DM-discretionary score switch (`CHAR-001` §6.2) |

**Verification standard.** Pages 7, 8, 12, 28, 29, 31 and 145 were read as page images. The p. 7 table was confirmed to have nine rows and three columns with **no footnotes, symbols, or columns lost** (`CLUSTER-002-completeness-audit.md` §5).

> **The p. 7 table is the *principal* governing object, not the *single* one.** That distinction is load-bearing and was won the hard way: an earlier remediation called it the single governing object while this card's own open question recorded the Druid and Mystic entries as unread, and the detailed Druid entry does add requirements (`DEC-0010` item 18, protocol §9.8). Both entries have since been read as complete units.

## Rules Cyclopedia Explicitly Establishes

1. **Nine PC classes**, grouped by RC as four human (cleric, fighter, magic-user, thief), three demihuman (dwarf, elf, halfling), and two special/optional (druid, mystic).
2. **Race and class are one choice for demihumans.** RC: demihumans are more limited in options than humans, "so the entire race can be represented by a single character class." There is no separate race-selection step.
3. **Human classes have no ability gate**, stated as a universal: *"Any new character can belong to one of the human classes (cleric, fighter, magic-user, thief), regardless of his ability scores."*
4. **Ability minimums are raw-score thresholds** on the remaining classes, per the p. 7 table and restated per class in prose with an explicit failure condition (e.g. dwarf: *"If the character you're creating has a Constitution of 8 or less, he cannot be a dwarf."*).
5. **Prime requisites are not an eligibility gate.** They govern (a) the raise-target of the `CHAR-001` trade and (b) an XP bonus/penalty (p. 12, `ADV-001`). No class is gated on a minimum prime-requisite value — the Mystic's thresholds sit in the "Other Requirements" column, and Wisdom is not a Mystic prime requisite.
6. **Eligibility is evaluated before the trade.** RC requires the class to be chosen first, and the trade may raise only a prime requisite.
7. **Druid is not reachable at creation.** RC: *"you can't start a character off as a druid. A druid character must start off as a cleric… and earn a lot of experience (up to 9th experience level) as a cleric. Only at that point can he become a druid."* Corroborated by the p. 8 Hit Dice table ("Does not apply") and by the Druid Experience Table beginning at level 9.
8. **The Druid transition has requirements beyond p. 7** (pp. 28–29) — see Scope Boundaries §B.
9. **Mystic creation eligibility is complete at p. 7** (Wisdom 13 and Dexterity 13, restated verbatim at p. 29). The rest of the Mystic entry is downstream — see §C.

## Rules Cyclopedia Leaves Undefined / Ambiguous

**V1 — Whether the Chapter 13 score switch may be used to reach a class ability minimum.** RC states the switch's trigger as a class-preference mismatch and never addresses minimums; the two provisions sit in different chapters with no cross-reference. **`RESOLVED` for this project by Simulator Ruling SR-3** (`CHAR-001`, human-granted 2026-08-29): **yes**, within the §5 envelope. The RC silence itself is real and is recorded here rather than presented as an RC answer.

**V2 — Nothing else.** Specifically **not** ambiguous, though each was tested: whether a character failing every demihuman/special requirement has any constrained outcome (RC's universal human-class availability makes the question moot — every character has at least four legal classes); whether any ability-score *maximum* gates a class (none located across the p. 7 table, all nine class entries, and Ch. 19); whether any eligibility requirement is expressed as an adjustment rather than a raw score (none located).

---

## Alternate-Source Completion Research

**Not applicable — the Rules Cyclopedia is fully explicit for this card's responsibility.** RC supplies a tabulated eligibility rule for all nine classes, corroborated by per-class prose and by the complete Druid and Mystic entries. V1 is a permission question about an RC-internal provision, not an RC silence, so the `RULE_CARD_RESEARCH_PROTOCOL.md` §15 precondition is not met.

## Compatibility Analysis

Not applicable — no alternate-source candidate was considered.

---

## Simulator Ruling

**None proposed by this card.** `CHAR-001`'s **SR-3** governs the switch's inclusion and ordering, and this card consumes its output; the ruling is recorded there, not duplicated here.

## Human-Approved Variant

Not applicable. Druid and Mystic are **Project-Selected RC Options** (`DEC-0008`) — RC itself presents them as optional and the project has selected them as required V1 content. Per `INVENTORY.md`'s vocabulary this is explicitly **not** a Human-Approved Variant: it selects among options RC sanctions rather than departing from any RC rule.

---

## Approved Mechanical Specification

### 1. Inputs

The six **eligibility scores** — i.e. `CHAR-001` §1's as-rolled scores, **after** any Chapter 13 switch the DM / simulation policy authorized at `CHAR-001` §0 step 3, and **before** the Chapter 1 trade (SR-3).

```text
as-rolled scores  →  [optional authorized Ch.13 switch]  →  ELIGIBILITY SCORES  →  this card
                                                                                       ↓
                                                                            class chosen
                                                                                       ↓
                                                                         Ch.1 2-for-1 trade
```

**Never the adjusted (post-trade) scores** — see §4. Where no switch is authorized, eligibility scores are identical to as-rolled scores.

### 2. Creation-time eligibility

```text
eligible_classes(scores) -> set of classes
```

| Class | Prime requisite(s) | Creation-time requirement | Available at creation? |
|---|---|---|---|
| Cleric | Wisdom | **None** | Always |
| Fighter | Strength | **None** | Always |
| Magic-User | Intelligence | **None** | Always |
| Thief | Dexterity | **None** | Always |
| Dwarf | Strength | Constitution ≥ 9 | If met |
| Elf | Strength, Intelligence | Intelligence ≥ 9 | If met |
| Halfling | Strength, Dexterity | Dexterity ≥ 9 **and** Constitution ≥ 9 | If both met |
| Mystic | Strength, Dexterity | Wisdom ≥ 13 **and** Dexterity ≥ 13 | If both met |
| **Druid** | Wisdom | Neutral alignment **and** 9th level as a cleric | **Never** |

**The four human classes are always available**, whatever the scores. `eligible_classes` therefore never returns the empty set.

**Druid returns `NOT_ELIGIBLE_AT_CREATION` unconditionally**, with a reason code distinguishing it from a failed ability check — its requirement is not an ability threshold and can never be satisfied by any score array.

### 3. Prime requisites are not gates

`CHAR-002` **must not** test a prime requisite against any threshold. Prime requisites are exported for `CHAR-001` §4 (trade target) and `ADV-001` (XP modifier) and are eligibility-inert here.

### 4. Ordering, and why it is fixed

```text
CHAR-001 §1    generate as-rolled scores
     ↓
CHAR-001 §6.1  discard / replacement determination        (SR-4)
     ↓
CHAR-001 §6.2  optional authorized Ch.13 switch           (SR-3)  ← eligibility-shaping
     ↓
CHAR-002       evaluate eligibility  ← THIS CARD
     ↓
               choose a class from the eligible set
     ↓
CHAR-001 §4    optional prime-requisite trade             ← post-eligibility
```

**Necessary mechanical consequence, derivation shown:** RC requires class choice before the trade, and the trade raises only a prime requisite while Constitution may not be exchanged at all. Therefore **the trade can never manufacture eligibility** — the test has already run — and evaluating on adjusted scores would be both circular (the trade needs the class) and mechanically inert.

**The switch is different, and that difference is the point.** It runs *before* the test and **can** establish a class minimum, bounded by §5.

### 4.1 This card's result is an invariant the trade must preserve (SR-5)

Human ruling **SR-5** (2026-08-29, recorded on `CHAR-001` as trade rule **R10**) makes §2's result binding **after** the subsequent adjustment as well as before it:

```text
Eligibility is established here — and must remain true
after CHAR-001's 2-for-1 trade.
```

**This card is unchanged by SR-5.** No threshold moved, no procedure was added here, and **the adjustment procedure remains entirely `CHAR-001`'s** — this section records only that `CHAR-001` R10 consumes this card's minimums as a constraint. **No `CHAR-002 → CHAR-007` dependency is created**; R10 reads raw-score minimums, not adjustment values.

The materially binding case is the **Mystic's Wisdom 13**: it is the one creation minimum sitting on an ability RC's own exchange restrictions do not protect (Constitution and Charisma cannot be exchanged; Dexterity cannot be lowered; the Elf's Intelligence is a prime requisite and can only be raised).

**The asymmetry is deliberate and must not be collapsed:** the trade cannot **establish** eligibility (§4) and cannot **destroy** it (R10).

### 5. Bounded consequence of the Chapter 13 switch (V1 — `RESOLVED` by SR-3)

The switch is **included in V1** and **may** be authorized to satisfy a class minimum. Because its destination is a *prime requisite*, what it can reach is fully determined — **the ruling does not widen this**:

| Gate | Reachable by switch? |
|---|---|
| Dwarf — Constitution 9 | **No** (prime req is Strength) |
| Elf — Intelligence 9 | **Yes** |
| Halfling — Dexterity 9 | **Yes** |
| Halfling — Constitution 9 | **No** |
| Mystic — Dexterity 13 | Yes, if the highest rolled score ≥ 13 |
| Mystic — Wisdom 13 | **No** (prime reqs are Strength, Dexterity) |

So **no authorization can ever make a Dwarf eligible on Constitution 8, a Halfling on Constitution 8, or a Mystic on Wisdom 12** — those gates are not prime requisites of their classes. The switch's reach is confined to the **Elf's Intelligence gate**, the **Halfling's Dexterity gate**, and the **Mystic's Dexterity gate**.

**When no switch is authorized, §2 evaluates as-rolled scores exactly.** Authorization is a per-character DM / simulation-policy decision, not a global toggle (`CHAR-001` §6.2).

## Scope Boundaries

### A. What this card does **not** own

Class special abilities (`CHAR-009`), thief skills (`CHAR-010`), Hit Dice (`CHAR-003`), saving throws (`COMBAT-004`), weapon/armor permissions (`CHAR-009`/`TREAS-004`), spell access (`MAGIC-*`), level caps and Attack Ranks (`ADV-002`), prime-requisite XP modifiers (`ADV-001`), alignment as a system (`CHAR-008`).

### B. Druid — creation eligibility only; the transition is **not** in this cluster

The p. 7 "Other Requirements" column is **not exhaustive** for the Druid. The complete entry (pp. 28–29) adds an **upper** bound of 29th level on the originating cleric, a requirement to find and live in a woodland home, a DM-rolled **1d4-month** meditation, being found and **tested for worthiness** and taught by a higher-level druid (usually 25th+), admission to the realm of the druids, and **ongoing** alignment and residence maintenance (losing druid benefits on leaving Neutral unless the character returns to it).

**None of this changes `CHAR-002`.** Every one of these conditions is downstream of a 9th-level cleric, and `CHAR-002` already returns `NOT_ELIGIBLE_AT_CREATION` — the Druid Experience Table beginning at level 9 **strengthens** that answer rather than altering it.

**Proposed ownership — recommendation only, not adopted, and `CLUSTER-002` is not expanded:**

| Material | Proposed owner | Rationale |
|---|---|---|
| Cleric → Druid transition procedure (9th–29th level, woodland home, 1d4 months, testing, instruction, admission) | **`CHAR-013`** | `INVENTORY.md` already lists Druid under High-Level Class Branches; this is a later class-change procedure, not creation eligibility |
| Ongoing alignment/residence maintenance | `CHAR-013` with `CHAR-008` | Ongoing conditions on retaining druid status |
| 30th-level challenge progression and the 9–36 level range | `ADV-002` | Advancement mechanics |

**The Druid maximum level is settled: 36** (standard progression 9–36; the special-challenge hierarchy begins at 30th), by human adjudication 2026-08-29, with RC Ch. 1 p. 12's "may only achieve 30th level" treated as erroneous summary text. Recorded against `ADV-002` in `INVENTORY.md`. **Not reopened by this card.**

### C. Mystic — creation eligibility is complete here; everything else is downstream

Wisdom 13 and Dexterity 13 are the whole of Mystic *creation* eligibility, confirmed by reading the complete entry. The rest of that entry is **not** absorbed into this card:

| Mystic material (RC p. 29) | Owner |
|---|---|
| Strength — not Dexterity — determines the XP bonus, because Dexterity 13 is a precondition of being a mystic at all | **`ADV-001`** |
| Never wears armor of any type; never uses protective magical devices | **`CHAR-009`** / `TREAS-004` |
| Receives XP from treasure only if donated to the needy; must tithe 10% to the cloister | **`ADV-001`** |
| Forswearing the oath → expelled, no new levels, −1 level per year away from the cloister | **`ADV-002`** |
| 75% of mystics are Lawful — a **tendency, not a requirement** | **`CHAR-008`** |
| 1d6/level to 9th, +2/level from 10th, Constitution ceases, maximum level 16 | **`CHAR-003`** |

---

## Deterministic Test Cases

Scores are given in RC's order: **Str, Int, Wis, Dex, Con, Cha**.

### Human classes are unconditional

| # | Scores | Expected |
|---|---|---|
| E1 | `3,3,3,3,3,3` | Cleric, Fighter, Magic-User, Thief **all eligible**; Dwarf, Elf, Halfling, Mystic not; Druid `NOT_ELIGIBLE_AT_CREATION` |
| E2 | `18,18,18,18,18,18` | All eight creation classes eligible; Druid still `NOT_ELIGIBLE_AT_CREATION` |
| E3 | Any array | The four human classes are always present in the result; the set is never empty |

### Demihuman boundaries

| # | Scores | Expected |
|---|---|---|
| E4 | Con **9**, others 3 | Dwarf **eligible** (boundary, inclusive) |
| E5 | Con **8**, others 18 | Dwarf **not** eligible — RC's own failure condition, and no score elsewhere compensates |
| E6 | Int **9**, others 3 | Elf **eligible** |
| E7 | Int **8**, others 18 | Elf **not** eligible |
| E8 | Dex 9, Con 9, others 3 | Halfling **eligible** (both gates at boundary) |
| E9 | Dex 9, Con **8** | Halfling **not** eligible — conjunctive, not disjunctive |
| E10 | Dex **8**, Con 9 | Halfling **not** eligible — the other conjunct |

### Mystic boundaries

| # | Scores | Expected |
|---|---|---|
| E11 | Wis 13, Dex 13, others 3 | Mystic **eligible** (both boundaries, inclusive) |
| E12 | Wis 13, Dex **12** | Mystic **not** eligible |
| E13 | Wis **12**, Dex 13 | Mystic **not** eligible |
| E14 | Wis 18, Dex 18, Str 3 | Mystic **eligible** — Strength is a prime requisite, not a gate |

### Prime requisites are inert

| # | Case | Expected |
|---|---|---|
| E15 | Wis 3, all others 18 | **Cleric eligible** — Wisdom is the Cleric's prime requisite and is not a threshold |
| E16 | Str 3, Int 9, others 12 | **Elf eligible** — Strength is a prime requisite and is not gated; only Intelligence 9 is tested |
| E17 | Any array | No eligibility decision reads the p. 12 Experience Bonuses table |

### Druid

| # | Case | Expected |
|---|---|---|
| E18 | Any array, including Wis 18 + Neutral alignment | Druid `NOT_ELIGIBLE_AT_CREATION`, reason = *requires 9th level as a cleric*, **not** *ability requirement not met* |
| E19 | Druid requested as a starting class | Rejected; no Druid Hit Die is ever rolled (`CHAR-003`) |

### Ordering

| # | Case | Expected |
|---|---|---|
| E20 | Dwarf candidate: Str 18, Con 8. Apply every legal `CHAR-001` trade first, then evaluate | Dwarf **still not eligible** — Constitution cannot be exchanged; **no trade ever changes eligibility** |
| E21 | Eligibility evaluated on adjusted (post-trade) scores | **Contract violation** — the evaluation consumes eligibility scores, never adjusted ones |
| E22 | Fighter chosen, then trade raises Str 12→13 | Eligibility result unchanged; the trade is `CHAR-001`'s and post-dates this card |
| E29 | Mystic qualified on Wis 13 / Dex 13, then `CHAR-001` trade lowers Wis to 12 | **Contract violation (SR-5 / R10)** — this card's result is an invariant the trade must preserve. Enforcement lives in `CHAR-001` (V1–V12); this case exists so the requirement is visible from the card that owns the minimum |
| E30 | Any selected class, after any legal trade | Every creation minimum of that class **still satisfied** |
| E25 | Elf candidate: as-rolled Int 8, Str 16; **switch authorized** → Int 16 | **Elf eligible.** The switch runs before this card and **can** establish a minimum (SR-3) |
| E26 | Same candidate, **switch not authorized** | **Elf not eligible** — eligibility scores equal as-rolled scores |
| E27 | Dwarf candidate: Con 8, Str 18; **switch authorized** | **Still not eligible** — the switch reaches Strength, never Constitution |
| E28 | Mystic candidate: Wis 12, Dex 11, Cha 17; **switch authorized** | **Still not eligible** — the switch reaches Dexterity, never Wisdom |

### Guard

| # | Case | Expected |
|---|---|---|
| E23 | Ch. 13 switch applied **after** a class is chosen | **Rejected** — the switch runs before this card (SR-3) |
| E24 | Druid transition requirements queried | Out of scope: directs to `CHAR-013`/`ADV-002`; **not** answered by this card |

## Provenance Classification

| Element | Classification |
|---|---|
| §2 table; the human-class exemption; Druid non-reachability; §3 | **Rules Cyclopedia Explicit** |
| §4 ordering; §5 switch envelope; "the eligible set is never empty" | **Necessary Mathematical-Mechanical Consequence** (derivations shown) |
| §B/§C ownership proposals | **Not rules** — repository responsibility recommendations, for human decision |
| §1 eligibility-score input; §5 switch permission (V1) | **Unresolved by RC**, resolved for this project by **Simulator Ruling SR-3** (recorded on `CHAR-001`). RC never composes the two provisions; this card consumes the ruling's output and asserts no RC finding of its own |

---

## Open Questions

1. **V1 — `RESOLVED`** by human ruling SR-3 (2026-08-29, recorded on `CHAR-001`). The Chapter 13 switch is **included in V1**, runs **before** eligibility, and **may** be authorized to satisfy a class minimum — bounded by §5 to three gates. **No eligibility threshold changed**; this card gained a precisely specified input, not a changed rule.
2. **Druid transition ownership** (§B) — a proposed `CHAR-013` assignment with `CHAR-008`/`ADV-002` dependencies. **Proposed, not adopted.** Assigning it is a scope decision for the human project owner, not an agent action.
3. **Mystic downstream ownership** (§C) — five items proposed against `ADV-001`, `ADV-002`, `CHAR-008`, `CHAR-009`. Recommendations only.

**Explicitly closed, recorded so they are not re-raised:** whether "Other Requirements" is exhaustive (**no** for Druid, **yes** for Mystic — both entries read as complete units); whether eligibility depends on `CHAR-007`-supplied adjustment values (**no** — every requirement is a raw-score threshold, so no `CHAR-002 → CHAR-007` dependency exists); whether any class has an ability *maximum* (none located).

## Approval

- Approved by: `<pending>`
- Date: `<pending>`
- Notes: `<pending>`

**Approving this card ratifies §1–§5. It does not adopt the §B/§C ownership proposals and does not resolve V1.**
