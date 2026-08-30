# Rule Card: General Ability Score Mechanical Effects

## Rule ID

`CHAR-007`

## Title

General Ability Score Mechanical Effects

## Status

`AWAITING_APPROVAL`

> Stage-B draft, 2026-08-29. Stage-A evidence (`docs/rules/evidence/CHAR-007-evidence.md`) passed independent primary-source completeness review and human evidence review on 2026-08-29. **Not approved. Not implementable.**
>
> **Stage-B correction and human-ruling impact (2026-08-29): NONE.** Neither the research correction nor human rulings SR-1 through SR-4 touches this card:
>
> - **SR-1** (Elf `+2`) governs a *fixed* gain to which **Constitution expressly does not apply**; the p. 9 adjustment value this card owns was never in dispute.
> - **SR-2** (Mystic may raise Dexterity) is a `CHAR-001` trade rule. This card supplies **no** trade rule and **no** prime-requisite logic.
> - **SR-3** (Chapter 13 switch) relocates *which scores* reach eligibility; this card maps a score to an adjustment and is indifferent to how the score arose.
> - **SR-4** (discard criterion) operates on raw scores before any adjustment is read.
>
> No mechanical content changed. **Candidate for approval.**

## Rules Domain

`character_creation`

---

## Rules Cyclopedia Source

| Page | Object | Bearing |
|---|---|---|
| **p. 9** | **Bonuses and Penalties for Ability Scores Table** | The shared score → adjustment mapping for all six abilities |
| p. 9 | Ch. 1, "Strength" | Melee attack, melee/thrown damage, Open Doors adjustment and the natural-6 override |
| p. 9 | Ch. 1, "High Wisdom and Saving Throws" | The `bonus to **one of** his saving throws` framing; saves vs. spells |
| **p. 10** | **Abilities and Adjustments Table** | Which effect each ability's adjustment applies to |
| **p. 10** | **Intelligence and Languages Table** | Literacy and additional-language counts |
| **p. 10** | **Charisma Adjustment Table** | Reaction adjustment, maximum retainers, retainer morale |
| p. 10 | Ch. 1 per-ability write-ups (all six) | Application mode per ability |
| p. 102 | Ch. 8, "Dexterity Adjustments (Optional)" | Boundary: individual initiative only |
| p. 143 | Ch. 13, "Ability Checks" | Boundary: a different mechanic entirely |
| p. 147 | Ch. 13, "Open Doors" Ability / Doors | Boundary: the Open Doors *procedure* |
| p. 266 | Ch. 19, "Ability Scores and Saving Throws" | Boundary: the optional extended save mapping |

**Verification standard.** Pages 9, 10, 102, 147, 148 and 266 were read as page images.

> **Citation correction carried in.** Stage A cited the Abilities and Adjustments Table at p. 9. **It is on p. 10**; p. 9 carries the Bonuses and Penalties table and the Strength write-up. The table's *content* was confirmed correct in every row — only the page reference was wrong, and RC's own cross-reference at p. 130 Step 3 ("the Bonuses and Penalties for Ability Scores table in Chapter 1 (page 9)") independently confirms the split.

## Rules Cyclopedia Explicitly Establishes

1. **One shared adjustment table** maps a score to an adjustment for **all six** abilities uniformly (p. 9).
2. **A per-ability assignment table** names what each adjustment applies to (p. 10).
3. **Two abilities carry supplementary tables of their own** — Intelligence (languages) and Charisma (reaction, retainers, morale). The shared table is therefore **not** the whole of this responsibility.
4. **Charisma carries three distinct outputs**, not one.
5. **Application mode varies by ability.** Charisma's reaction adjustment modifies **DM-made** rolls and never the player's; Intelligence's general-skills effect is conditional on an optional system being in use.
6. **Wisdom is the only ability with a core saving-throw effect**, and RC frames it narrowly: a Wisdom of 13+ gives *"a bonus to **one of** his saving throws"* (8 or less, a penalty), affecting saving throws vs. spells. Chapter 19 confirms this by stating that in the standard rules Wisdom is the only ability affecting a saving throw.
7. **The Open Doors roll is 1d6, success on 5–6**, with the Strength adjustment applied to the die result, and *"a natural, unmodified '6' … will always open a door, despite any penalties to the contrary."*

## Rules Cyclopedia Leaves Undefined / Ambiguous

**None that block this card.** Every item Stage A carried as unresolved was a **responsibility-partition question**, not an RC silence, and all five are settled below (§4) by the cluster boundary and by the human adjudications of 2026-08-29. RC defines the general ability-score effects explicitly and completely for all six abilities.

---

## Alternate-Source Completion Research

**Not applicable — the Rules Cyclopedia is fully explicit.** No RC gap exists for this responsibility, so `RULE_CARD_RESEARCH_PROTOCOL.md` §15's precondition is not met and no alternate-source research was performed.

## Compatibility Analysis

Not applicable.

---

## Simulator Ruling

**Not applicable — none proposed, and none identified as needed.**

## Human-Approved Variant

Not applicable.

---

## Approved Mechanical Specification

### 1. The shared adjustment table (RC p. 9)

```text
adjustment(score) ->
```

| Ability Score | Adjustment |
|---|---|
| **2–3** | **−3** |
| 4–5 | −2 |
| 6–8 | −1 |
| 9–12 | **0** (no adjustment) |
| 13–15 | +1 |
| 16–17 | +2 |
| 18 | +3 |

- Applies **identically to all six abilities**. There is no per-class or per-race variation.
- The band starts at **2**, not 3, even though 3d6 generation cannot produce a 2 — the table accommodates scores reduced below the generated range by other effects. *(The Intelligence and Charisma supplementary tables in §3 begin at 3, and that difference is RC's, faithfully reproduced.)*
- Domain outside 2–18 is **not specified by RC** and must not be extrapolated.

### 2. Effect assignment (RC p. 10)

| Ability | Adjustment applies to | Value owned by | Procedure owned by |
|---|---|---|---|
| **Strength** | Attack rolls (melee weapons and unarmed combat) | `CHAR-007` | `COMBAT-002` |
| | Damage rolls (melee and thrown weapons) | `CHAR-007` | `COMBAT-003` |
| | Opening doors | `CHAR-007` | **`EXP-005`** — see §4.1 |
| **Intelligence** | Languages (literacy and additional languages) | `CHAR-007` (§3.1) | `CHAR-008` |
| | General skills *(optional system; project-selected REQUIRED by `DEC-0008`)* | `CHAR-007` | `CHAR-012` |
| **Wisdom** | Saving throws vs. spells | `CHAR-007` | **`COMBAT-004`** — see §4.3 |
| **Dexterity** | Attack rolls (thrown and missile weapons) | `CHAR-007` | `COMBAT-002` |
| | Armor Class | `CHAR-007` | `COMBAT-002` |
| **Constitution** | Hit points per experience level | `CHAR-007` | **`CHAR-003`** |
| **Charisma** | Reactions from NPCs | `CHAR-007` (§3.2) | `ENC-003` |
| | Maximum number of retainers; retainer morale | `CHAR-007` (§3.2) | `CHAR-006` |

**The governing principle of this card: `CHAR-007` may own an adjustment value without owning the procedure that consumes it.** Every row above is an instance.

### 3. Supplementary per-ability tables

#### 3.1 Intelligence and Languages Table (RC p. 10)

| Intelligence | Use of languages |
|---|---|
| 3 | Has trouble speaking; cannot read or write |
| 4–5 | Cannot read or write Common |
| 6–8 | Can write simple Common words |
| 9–12 | Reads and writes native languages (usually two) |
| 13–15 | Native languages, **+1** additional language |
| 16–17 | Native languages, **+2** additional languages |
| 18 | Native languages, **+3** additional languages |

A character of average Intelligence (9–12) knows two languages — the Common tongue and an alignment tongue — and can read and write them. Demihumans usually know additional languages, as described in each demihuman class entry (`CHAR-009`). Which specific languages are available, and their selection, is **`CHAR-008`'s**.

#### 3.2 Charisma Adjustment Table (RC p. 10)

| Charisma | Reaction adj. | Max. no. retainers | Retainer morale |
|---|---|---|---|
| 3 | −3 | 1 | 4 |
| 4–5 | −2 | 2 | 5 |
| 6–8 | −1 | 3 | 6 |
| 9–12 | No adj. | 4 | 7 |
| 13–15 | +1 | 5 | 8 |
| 16–17 | +2 | 6 | 9 |
| 18 | +3 | 7 | 10 |

**The reaction adjustment applies only while the character is talking to the creature**, and RC is explicit that it *"never adjust[s] any rolls **you** make; they only affect rolls made by the Dungeon Master."* This is a genuine mechanical constraint, not flavour: a player-side application of the Charisma reaction adjustment is a **rules violation**.

Retainer count and retainer morale are **carried here because they are columns of `CHAR-007`'s own table**, and exported to `CHAR-006`, which owns what they do.

### 4. Boundaries — settled

#### 4.1 Open Doors — value here, procedure to `EXP-005`

RC states the procedure inside the Strength write-up (p. 9): 1d6, success on 5–6, Strength adjustment applied to the die result, natural unmodified 6 always opens. Chapter 13 p. 147 carries a dedicated **"Open Doors" Ability** section which **adds two rules Chapter 1 omits**: the attempt may be made **once per round per character**, and **a failed attempt forfeits surprise** (*"monsters on the other side of the door cannot be surprised; they have heard the noise"*).

**Disposition:** `CHAR-007` owns the **Strength adjustment value only**. The complete procedure — die, target, natural-6 override, once-per-round limit, surprise forfeiture — belongs to **`EXP-005`**, where p. 147 sits alongside Doors, Secret Doors, Special Doors and Listening. `EXP-005` thereby acquires a dependency on **`ENC-002`** (surprise).

The p. 9 procedure fragment is reproduced here **only** so `EXP-005`'s future researcher finds it and does not mistake p. 147 for the whole rule. **This card does not specify or implement Open Doors.**

#### 4.2 Dexterity and initiative — out of scope

RC p. 102 carries **"Dexterity Adjustments (Optional)"**: at DM option, Dexterity modifies the **individual** initiative roll, and *"does not affect the party's roll in group initiative."* Individual initiative is itself optional and is **declined for V1** (`DEC-0008`, which selects group initiative). Owner: **`COMBAT-006`**.

**`CHAR-007` must not enable this rule merely because the modifier exists.** The V1 effect list in §2 is correct and complete without it.

#### 4.3 Wisdom and saving throws — the one-row overlap, resolved

| Effect | Owner |
|---|---|
| Wisdom score → adjustment value; the **fact** that it applies to saving throws vs. spells | **`CHAR-007`** |
| The saving-throw procedure, its five categories, and the application of any modifier | **`COMBAT-004`** |
| The Chapter 19 optional extension mapping other abilities to other save categories | **`COMBAT-004`, solely** |

This follows the approved `CLUSTER-002` boundary, which made `COMBAT-004` sole owner of the Chapter 19 mapping. RC's five save categories (Poison or Death Ray; Magic Wand; Turning to Stone or Paralysis; Dragon Breath; Spells or Magic Staff) are named at p. 9 and are recorded here **as a boundary marker only** — `COMBAT-004` owns them.

**Wording precision carried in from the completeness audit:** RC p. 9 says high Wisdom gives *"a bonus to **one of** his saving throws."* `CHAR-007` records that narrowed framing and does not broaden it to saving throws generally.

#### 4.4 Chapter 13 Ability Checks — a separate responsibility, not this card

RC p. 143's general ability check — roll 1d20 against the **raw ability score**, equal-or-under succeeds — is **not** part of this responsibility, per binding direction of 2026-08-29. Three independent grounds from primary text support that boundary:

1. **Different mechanic.** This card converts a score into an adjustment (−3…+3) applied to other rolls. The check uses the **raw score as a target number**. The adjustment table plays no part in it, and the DM's situational modifier is applied to the die and is not score-derived.
2. **Different audience and purpose.** This card's effects are player-facing, enumerated, closed, and recorded at creation. The check is DM-facing and explicitly open-ended — a catch-all for actions RC does not otherwise cover.
3. **Different location and grouping.** RC places the check with DM adjudication procedures (aging, alignment changes, doors, listening, thief abilities), and never cross-references the two.

**No new Rule ID is assigned by this card.** Creating one is a scope/governance decision for the human project owner (see Inventory Recommendations). The check's existing relationship to `CHAR-012` (General Skills shares the resolution mechanic) should inform that decision.

### 5. Out of scope

Armor Class as a system (`COMBAT-002`); attack and damage resolution (`COMBAT-002`/`COMBAT-003`); saving-throw procedure (`COMBAT-004`); hit-point application (`CHAR-003`); reaction resolution (`ENC-003`); retainers (`CHAR-006`); languages and alignment (`CHAR-008`); general skills (`CHAR-012`); door procedures (`EXP-005`); initiative (`COMBAT-006`); the Chapter 19 save mapping (`COMBAT-004`).

---

## Deterministic Test Cases

### Shared adjustment table — every band and every boundary

| # | Score | Expected |
|---|---|---|
| A1 | 2 | −3 |
| A2 | 3 | −3 |
| A3 | 4 | −2 |
| A4 | 5 | −2 |
| A5 | 6 | −1 |
| A6 | 8 | −1 |
| A7 | 9 | **0** |
| A8 | 12 | **0** |
| A9 | 13 | +1 |
| A10 | 15 | +1 |
| A11 | 16 | +2 |
| A12 | 17 | +2 |
| A13 | 18 | +3 |
| A14 | Same score, queried for each of the six abilities | **Identical** adjustment — one shared table |
| A15 | Score 19 or 1 | **Unspecified** — must not extrapolate |

### Intelligence and Languages

| # | Intelligence | Expected |
|---|---|---|
| A16 | 3 | Trouble speaking; cannot read or write |
| A17 | 5 | Cannot read or write Common |
| A18 | 8 | Can write simple Common words |
| A19 | 9 | Native languages (usually two); **0** additional |
| A20 | 12 | Same as A19 — band boundary |
| A21 | 13 | **+1** additional language |
| A22 | 16 | **+2** |
| A23 | 18 | **+3** |
| A24 | Intelligence 18 | Adjustment `+3` **and** `+3` additional languages — coincidence of value, two distinct tables; the language count is **not** derived from the adjustment |

### Charisma — three outputs

| # | Charisma | Reaction | Max retainers | Morale |
|---|---|---|---|---|
| A25 | 3 | −3 | 1 | 4 |
| A26 | 8 | −1 | 3 | 6 |
| A27 | 9 | 0 | 4 | 7 |
| A28 | 12 | 0 | 4 | 7 |
| A29 | 13 | +1 | 5 | 8 |
| A30 | 18 | +3 | 7 | 10 |

| # | Case | Expected |
|---|---|---|
| A31 | Player-made roll with the Charisma reaction adjustment applied | **Rules violation** — it modifies DM-made rolls only |
| A32 | Character not talking to the creature | Reaction adjustment **not** applied |

### Per-ability assignment

| # | Case | Expected |
|---|---|---|
| A33 | Strength +2, melee attack roll | Adjustment supplied |
| A34 | Strength +2, **missile** attack roll | **Not** supplied — that is Dexterity's |
| A35 | Dexterity +2, thrown weapon attack roll | Supplied |
| A36 | Strength +2, thrown weapon **damage** roll | **Supplied** — Strength covers melee *and thrown* damage |
| A37 | Wisdom +1, saving throw vs. spells | Supplied |
| A38 | Wisdom +1, saving throw vs. dragon breath | **Not** supplied under core rules (Ch. 19 variant is `COMBAT-004`'s) |
| A39 | Constitution +2, hit-point roll | Supplied (`CHAR-003`) |
| A40 | Constitution +2, fixed gain above Name level | **Not** supplied (`CHAR-003` §5) |
| A41 | Intelligence +1 with general skills disabled | Language effect applies; general-skills effect does not |

### Boundary guards

| # | Case | Expected |
|---|---|---|
| A42 | Open Doors resolved by `CHAR-007` | **Boundary violation** — procedure belongs to `EXP-005`; this card supplies only the Strength adjustment |
| A43 | Once-per-round / surprise-forfeiture rules sought in `CHAR-007` | Absent by design; directs to `EXP-005` (with `ENC-002`) |
| A44 | Dexterity applied to an initiative roll | **Rejected** for V1 — optional individual initiative is declined (`DEC-0008`); owner `COMBAT-006` |
| A45 | Any ability other than Wisdom applied to a saving throw | **Rejected** under core rules |
| A46 | Ability check (1d20 vs. raw score) requested from `CHAR-007` | **Out of scope** — different mechanic, different responsibility (§4.4) |
| A47 | Ability check attempts to use the adjustment table | **Contract violation** — the check uses the raw score; the table plays no part |
| A48 | Retainer count/morale requested | Value supplied; **use** belongs to `CHAR-006` |

## Provenance Classification

| Element | Classification |
|---|---|
| §1 shared table; §2 assignment; §3.1/§3.2 supplementary tables; the DM-side-only constraint; the "one of his saving throws" framing; the Open Doors fragment | **Rules Cyclopedia Explicit** |
| §4 boundaries | **Repository responsibility partition**, following the approved `CLUSTER-002` boundary and the 2026-08-29 direction — not rules content |
| Anything else | None — no completion, ruling, or variant is claimed |

---

## Open Questions

**None blocking.** All five Stage-A items are closed:

| Stage-A item | Disposition |
|---|---|
| Open Doors ownership | **Closed** — value here, procedure to `EXP-005`, new `ENC-002` dependency (§4.1) |
| Armor Class application | **Closed** — `COMBAT-002` (§2) |
| Charisma retainer columns | **Closed** — values here, use to `CHAR-006` (§3.2) |
| Any ability effect on initiative | **Closed** — p. 102 inspected; optional individual initiative only; `COMBAT-006`; declined for V1 (§4.2) |
| `CHAR-007` / `COMBAT-004` Wisdom overlap | **Closed** — value and fact here, procedure and Ch. 19 extension to `COMBAT-004` (§4.3) |

**Carried forward as a governance decision, not a rules question:** whether the Chapter 13 ability check receives its own Rule ID. §4.4 establishes it is not `CHAR-007`'s; **assigning an ID is for the human project owner** (see the Stage-B report's Inventory Recommendations).

## Approval

- Approved by: `<pending>`
- Date: `<pending>`
- Notes: `<pending>`
