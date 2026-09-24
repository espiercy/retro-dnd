# CLUSTER-003 Stage B — Human Adjudications, Synthesis Record, and Provenance Separation

> **Stage-B artifact, 2026-09-24.** Produced under `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` (`DEC-0009`, as amended by `DEC-0010` and `DEC-0011`) on explicit human authorization, after Stage-A primary-source research, independent completeness review, `DEC-0011` BECMI gap-directed research, its remediation, and human adjudication of the seven blocking source defects and ambiguities.
>
> **This document is not a Rule Card and authorizes nothing.** The three cards it accompanies are `AWAITING_APPROVAL`:
>
> ```text
> CHAR-004  Starting Equipment & Expedition Preparation
> CHAR-005  Encumbrance & Movement Rate
> EXP-003   Dungeon Movement
> ```
>
> **Implementation is NOT authorized.** The Pre-Code Gate was not begun and no implementation plan exists.

---

## 0. Status

```text
CLUSTER-003 Stage A:        COMPLETE -- RC primary + DEC-0010 completeness PASS
CLUSTER-003 DEC-0011:       COMPLETE -- BECMI, seven authorized questions,
                                       remediation 1 applied
Human adjudication:         COMPLETE -- 2026-09-24, seven rulings (SS1)
CLUSTER-003 Stage B:        COMPLETE -- three Rule Cards drafted
Human Rule Card review:     PENDING
Implementation:             NOT AUTHORIZED
Pre-Code Gate:              NOT BEGUN
```

## 1. The Seven Human Adjudications, 2026-09-24

The human project owner reviewed the Stage-A evidence, the `DEC-0011` BECMI package and its remediation, and issued seven determinations. **Five are Simulator Rulings; two are not.** That distinction is the single most important thing in this document and is preserved everywhere below.

| Q | Question | Decision | Provenance | Ruling ID |
|---|---|---|---|---|
| **Q1** | Belt pouch: `2 + 50 = 52` vs. the printed `55 cn` | **A fully loaded belt pouch weighs `52 cn`.** Empty `2 cn` and capacity `50 cn` are preserved independently. The printed `55 cn` worked total is **erroneous** | **Simulator Ruling** | **SR-6** |
| **Q2** | Magic-user dagger: Ch. 2 *"Dagger only"* vs. Ch. 4 note `w` | **A Magic-User may use a dagger unconditionally.** The expanded list stays optional under DM/simulation-policy discretion. Ch. 4's note, **insofar as it makes the dagger itself discretionary**, is a compilation defect | **Simulator Ruling informed by BECMI lineage evidence** | **SR-7** |
| **Q3** | Suit Armor: `750 cn → 90' (30')` vs. the printed `30' (10')` | **Do not apply the Suit Armor-specific rate.** Suit Armor contributes its printed **`750 cn`** to total encumbrance; movement is then read normally from the standard table | **Simulator Ruling** | **SR-8** |
| **Q4** | Running speed: Ch. 6 vs. Ch. 8 p. 103 *"3 × normal movement"* | **The Ch. 6 table governs.** Ch. 8's `3 ×` applies to the **per-round (encounter)** rate, in the historically evidenced sense | **Rules Cyclopedia Explicit interpretation/correction**, reinforced by **Necessary Mechanical Consequence** and BECMI lineage evidence. **NOT a Simulator Ruling** | — |
| **Q5** | Mystic `MV` × encumbrance composition | **Enhanced `MV` applies only while the Mystic is in the ordinary normal-movement encumbrance state.** Once encumbrance would reduce an ordinary character below `120'`, read movement from the standard table instead | **Simulator Ruling** | **SR-9** |
| **Q6** | Mystic encounter movement; BECMI's defective `320'(80')` | **Do not import `80'`.** `encounter = MV × 1/3`, **retained exactly, including fractional thirds** | **Rules Cyclopedia Explicit** (the ⅓ relationship) + **Necessary Mathematical Consequence** (exact fractional retention). **NOT a Simulator Ruling** | — |
| **Q7** | Starvation movement column: `×3/4 → ×1/2 → ×3/4` | **The final `×3/4` is a printed defect.** Use `×3/4 → ×1/2 → ×1/4` | **Simulator Ruling** | **SR-10** |

### 1.1 Simulator Ruling register — continuation of the project sequence

`CLUSTER-002` established **SR-1** through **SR-5**. `CLUSTER-003` continues the same sequence; **no identifier is reused**.

```text
SR-6   Belt pouch filled encumbrance = 52 cn           CHAR-004
SR-7   Magic-User dagger is unconditional              CHAR-004
SR-8   Suit Armor has no special movement rate;
       it is 750 cn and nothing else                   CHAR-005 (value from CHAR-004)
SR-9   Mystic enhanced MV is gated on remaining in
       the unencumbered band                           CHAR-005
SR-10  Starvation movement progression 3/4, 1/2, 1/4   CHAR-005
```

**Q4 and Q6 create no Simulator Ruling and must not be summarised as though they did.** Q4 is an interpretation of an explicit RC rule against a defective restatement of it; Q6 is an explicit RC ratio plus the arithmetic that follows from it. Recording either as a project adjudication would overstate what the project decided and understate what the source says.

### 1.2 What each Simulator Ruling rejected — preserved deliberately

A ruling that does not record the reading it rejected is not auditable.

| Ruling | Rejected reading | Why the rejection is not obvious |
|---|---|---|
| **SR-6** | That the printed `55 cn` governs, and one of the two component values is wrong | RC prints three numbers and only two can be simultaneously true with the stated rule. The ruling keeps the **two independently stated values** and discards the **derived total**. The opposite choice — keep `55`, infer an empty weight of `5 cn` — is equally available on the page and was not taken |
| **SR-7** | That Ch. 4's note `w` governs and the dagger is DM-discretionary | Chapter 4's table is the *operative equipment data*, so preferring Chapter 2 is not automatic. The ruling rests on Ch. 2 stating the baseline **and separately** naming the optional list — a structure BECMI corroborates |
| **SR-8** | That the Suit Armor line is a flat override of the encumbrance table | **BECMI's own precedence rule selected the `30'` value**, so this is *not* a case of discarding an unsupported number. It is discarding a **historically genuine** one, because RC supplies no rule for composing it with additional carried weight, and preserving it would require inventing one |
| **SR-9** | That `MV` scales proportionally under encumbrance, **or** that the Mystic is immune to encumbrance | Both are coherent and both were available. The ruling takes neither: it treats exceptional mobility as a **benefit of remaining unburdened**, which is a threshold, not a curve |
| **SR-10** | That the printed `×3/4` at the worst band governs | The table prints it plainly; it is not an OCR artefact. The ruling overrides a **visually verified printed value** on monotonicity grounds and on the quarter-step progression, and says so |

### 1.3 Alternate-source evidence used only to interpret a defect

**BECMI is not authority anywhere in this cluster** (`SOURCE_HIERARCHY.md` §3; `DEC-0011` item 10). It was used in exactly three places, each time to **interpret** an RC defect rather than to supply a mechanic:

| Where | What BECMI contributed | What it did **not** do |
|---|---|---|
| **Q4** | Expert Rulebook's worked pursuit example (war horse `180'/turn` = `60'/round`, pursuit `180'/round`) establishes that the `3 ×` operation applies to the per-round value | It did not supply the rule. RC Ch. 6 already states it; BECMI disambiguates RC Ch. 8's truncated restatement |
| **Q2** | Basic's *"a magic-user can only use a dagger"* and Master's *"the DM may… **widen**"* corroborate RC Ch. 2's two-tier structure | It did not decide the question. The RC text was already sufficient; BECMI raised confidence |
| **Q3** | Master Players' Book p. 2 precedence rule shows the `30'` value has genuine ancestry and won BECMI's internal conflict | **It did not travel.** The ruling explicitly declines to import BECMI's resolution, because its precedence instrument is scoped to boxed sets and the RC has no such structure |

**No `Alternate-Source Compatible Completion` is claimed anywhere in this cluster.** Nothing mechanical was imported from BECMI.

### 1.4 Constraints the rulings impose on drafting — recorded so they cannot be lost

```text
FROM SR-8   Do NOT invent a generic "specific equipment movement
            overrides general encumbrance" rule.
            Do NOT create proportional scaling for Suit Armor.
            Suit Armor is 750 cn for movement/encumbrance purposes
            and nothing else.

FROM SR-9   Do NOT proportionally scale Mystic MV under encumbrance.
            Do NOT make the Mystic immune to encumbrance.
            Later-edition Monk design is comparative evidence only and
            MUST NOT appear as mechanical provenance.

FROM Q6     Do NOT round Mystic encounter movement -- not up, not down,
            not to nearest. Retain exact fractions.
            Any later snapping to map/grid units is a separate spatial
            execution concern and must not silently change the
            authoritative rate.

STANDING    Do not expand into CHAR-006, CHAR-008, EXP-010.
            Do not import later-edition Monk mechanics.
            Do not convert the Mystic "personal possessions" flavour
            into an ownership restriction.
            Do not add terrain mechanics from Mystic Acrobatics wording.
```

## 2. Architecture Note — fractional movement (Q6)

The authoritative movement allowance is a **rational quantity**. `130' ÷ 3 = 43⅓'` is the rate, not an approximation of one.

```text
AUTHORITATIVE LAYER     movement rate, exact rational value
                        owned by CHAR-005
        |
        v
SPATIAL EXECUTION       any snapping to 10' map squares, grid cells,
                        or miniature inches
                        NOT owned by CHAR-005, NOT specified here,
                        and MUST NOT silently alter the value above
```

This mirrors the project's standing separation of canonical simulation from presentation (`GAME_CONSTITUTION.md`, `AGENTS.md` §6). `EXP-003` consumes the rate; it does not quantise it. **No spatial-execution rule is drafted by this cluster.**

## 3. Cards Drafted

| Card | File | Status | Owns |
|---|---|---|---|
| `CHAR-004` | `docs/rules/character_creation/starting_equipment_and_expedition_preparation.md` | `AWAITING_APPROVAL` | Money, catalogs, cost, encumbrance values, container capacities, per-class mundane equipment legality, unlisted-item procedure |
| `CHAR-005` | `docs/rules/character_creation/encumbrance_and_movement_rate.md` | `AWAITING_APPROVAL` | The authoritative numerical movement rate: normal, encounter, running; encumbrance derivation; Mystic `MV`; condition movement effects |
| `EXP-003` | `docs/rules/exploration/dungeon_movement.md` | `AWAITING_APPROVAL` | Spending the normal-speed rate against the landed `EXP-002` dungeon turn |

### 3.1 Ownership constraints carried forward from earlier human decisions

Unchanged by this Stage B, and restated on each card:

- **`CHAR-004`** owns personal mundane equipment, containers, weapons, armour, ammunition, adventuring gear, **equipment-facing class restrictions / permission predicates**, and **equipment-specific class pricing** needed for mundane legality. **V1 excludes** mounts, vehicles, ships, siege equipment. Chapter 10 high-level equipment behaviour is **preserved, researched, `NOT V1-WIRED`**.
- **`CHAR-005`** owns the authoritative numerical character movement rate, including Mystic level-dependent `MV` and the movement effect of conditions whose causation is owned elsewhere.
- **`CHAR-009`** may *reference* equipment restrictions and Mystic movement but **must not become a second canonical implementation owner** of either.
- **`EXP-003`** is **Dungeon Movement** only. **Mapping owns no separate time procedure, roll, failure mechanic or movement penalty.** No generic "special terrain" subsystem is created here.

## 4. Open Questions That Became Moot — closed, not deleted

`DEC-0010`/`DEC-0011` expect auditable history. Each item below is marked closed **with the reason**, and the research that raised it is left intact in its original artifact.

| Item | Raised in | Now |
|---|---|---|
| Belt-pouch `52` vs `55` | `CHAR-004-evidence.md` §10 Defect 1 | **CLOSED by SR-6.** The source conflict is *not* resolved — the printed page still disagrees with itself. Only the simulator's behaviour is settled |
| Magic-User dagger contradiction | remediation §6 Defect 8 | **CLOSED by SR-7**, same qualification |
| Suit Armor movement contradiction | `CHAR-005-evidence.md` §10 Conflict 1 | **CLOSED by SR-8.** Note that BECMI *did* resolve this internally and the ruling still declines to follow it — see §1.2 |
| Running-speed factor-of-3 | remediation §6 Defect 10 | **CLOSED by Q4** — as an interpretation, not a ruling |
| Mystic `MV` × encumbrance | `CHAR-005-evidence.md` §10 Gap 2 | **CLOSED by SR-9.** Previously flagged as the cluster's most likely Stage-B blocker; it is no longer a blocker |
| Mystic encounter rounding | BECMI research §8 | **CLOSED by Q6** — exact fractions, no rounding rule needed because none is applied |
| Starvation non-monotonic column | `CHAR-005-evidence.md` §10 Conflict 2 | **CLOSED by SR-10** |
| `EXP-003` title / scope | `EXP-003-evidence.md` §7 | **CLOSED 2026-09-14** by the earlier governance decision; the card is drafted as **Dungeon Movement** |
| `CHAR-004` → `CHAR-009` whole-card dependency | Stage-A remediation §9 | **CLOSED 2026-09-14** by ownership Decision 1. No whole-card dependency exists |
| `CHAR-005` → `CHAR-009` whole-card dependency | Stage-A remediation §9 | **CLOSED 2026-09-14** by ownership Decision 2 |

### 4.1 Items that remain genuinely open — and do not block approval

| Item | Why it does not block |
|---|---|
| **`CHAR-004` chapter scope** — whether mounts, vehicles, ships and siege equipment ever enter the card | **V1 excludes them explicitly.** The cards are complete for V1 without them |
| **Chapter 10 high-level equipment pathway** | **`NOT V1-WIRED`** by decision. Preserved as research; no executable clause depends on it |
| **Racial-armour movement penalty** (RC Ch. 4 p. 67) | RC **delegates it to DM discretion by design** — established during remediation as *not* a gap. The cards record it as a DM-discretionary input, not a missing rule |
| **Rough/broken-terrain modifier presupposed by Mystic Acrobatics** | **Unowned and deliberately so.** `EXP-003` no longer claims Special Terrain, and no terrain mechanic is invented from the Acrobatics wording |
| **Mystic *"personal possessions"* framing** | Recorded as flavour the source's own rules do not implement. **Not converted into a restriction** |
| **Mystic running speed under enhanced `MV`** | A **derivation**, flagged on `CHAR-005` for human confirmation — see §5 |

## 5. One Derivation Flagged for Human Confirmation

The rulings specify the Mystic's **normal** movement (SR-9 gating) and **encounter** movement (Q6, `MV ÷ 3` exact). They do **not** explicitly address the Mystic's **running** movement.

```text
RC Ch. 6 general rule:   running speed = the normal-speed NUMBER,
                         expressed per round ( = 3 x encounter speed )

Applied to an active Mystic MV of 130':
    normal     130' per turn
    encounter  130/3 = 43 1/3' per round        [Q6, explicit]
    running    130' per round                    [DERIVED]
```

This is a direct application of an explicit RC rule to the Mystic's normal speed, so it is classified **Necessary Mechanical Consequence** rather than a new ruling. **It is flagged rather than assumed**, because the human rulings enumerated normal and encounter movement and stopped there. A reviewer who intends something different should say so at approval; the card records the derivation visibly rather than burying it.

## 6. Provenance Separation — the whole cluster at a glance

| Classification | Where it appears |
|---|---|
| **Rules Cyclopedia Explicit** | Money procedure; every catalog value (cost, `Enc`, capacity, AC); the six-band movement table; normal/encounter/running definitions; the slowest-member rule; running limit and exhaustion consequences; Ch. 8's scale boundary; Mystic `MV` values; the ⅓ encounter ratio; the dungeon turn's use of normal speed; the `10'` default map square; that normal speed already includes mapping |
| **Necessary Mathematical / Mechanical Consequence** | Ammunition `Enc` as an inverse rate; derived container/net/whip encumbrance; exact fractional retention of Mystic encounter movement; Mystic running movement (§5); the consequence that Suit Armor at 750 cn alone yields `90' (30')` |
| **Alternate-source evidence used only to interpret a defect** | BECMI in exactly three places, §1.3. **Never** as authority; **no** Compatible Completion claimed |
| **Simulator Ruling** | **SR-6, SR-7, SR-8, SR-9, SR-10** — and nothing else |
| **Intentionally deferred / not V1-wired** | Chapter 10 high-level equipment; mounts/vehicles/ships/siege; spatial quantisation of fractional movement; the unowned rough-terrain modifier |

**No clause anywhere in the three cards is classified `Human-Approved Variant`.** None deviates from an explicit RC rule the project intends to keep — the three that depart from printed values (SR-6, SR-8, SR-10) do so because the printed values are **internally inconsistent with other printed values**, which is a defect adjudication, not a deliberate variance from a coherent rule.

## 7. Provenance

| Item | Value |
|---|---|
| Stage-A evidence | `CHAR-004-evidence.md`, `CHAR-005-evidence.md`, `EXP-003-evidence.md` |
| Completeness audit | `CLUSTER-003-completeness-audit.md` |
| Stage-A remediation | `CLUSTER-003-remediation-pass-1.md` |
| `DEC-0011` alternate-source research | `CLUSTER-003-becmi-gap-research.md` (remediation 1 applied) |
| Cluster boundary record | `docs/rules/clusters/CLUSTER-003-equipped-dungeon-movement.md` |
| Process precedents | `docs/rules/RESEARCH_PROCESS_PRECEDENTS.md` (`P-001`, `P-002`) |
| Human adjudications | 2026-09-24, seven determinations, §1 |
| Stage B drafted | 2026-09-24 |

```text
CLUSTER-003 STAGE B:  COMPLETE -- THREE RULE CARDS DRAFTED
                      AWAITING_APPROVAL

IMPLEMENTATION:       NOT AUTHORIZED
PRE-CODE GATE:        NOT BEGUN
```
