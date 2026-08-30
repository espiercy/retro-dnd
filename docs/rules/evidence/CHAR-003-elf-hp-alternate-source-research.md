# Stage-B Gap-Directed Alternate-Source Research: Elf Fixed Hit-Point Gain (`CHAR-003`)

> **Stage-B artifact.** Produced under `RULE_CARD_RESEARCH_PROTOCOL.md` §15 (gap-directed alternate-source research) with `DEC-0010`'s structure-first process applied, on human authorization dated 2026-08-29. It is **not** a Rule Card and authorizes nothing. Its conclusion feeds `docs/rules/character_creation/hit_points_and_hit_dice.md`, which is `AWAITING_APPROVAL`.
>
> **This research was performed anew.** The prior BECMI work produced from the invalid RC-exhaustion conclusion is `NOT VALID AS CURRENT SYNTHESIS INPUT` (human ruling, `DEC-0010` Consequences). It was not consulted, not reused, and no conclusion was inherited from it. Nothing below cites it.

## 1. Why this research is authorized

`RULE_CARD_RESEARCH_PROTOCOL.md` §15 requires a precise gap statement before alternate-source research, and `DEC-0010` item 8 requires object-level RC exhaustion first. Both preconditions are met, and the gap has an unusual shape that must be stated exactly:

```text
RC establishes:
    Elf Hit Dice are 1d6 per level through 9th level.
    Constitution adjustment applies to each rolled die and ceases thereafter.
    A fixed hit-point gain applies at 10th level, the Elf's maximum level.

RC does not establish:
    The VALUE of that fixed gain — RC states it as +1 twice and as +2 twice.

Executable simulation requires it because:
    CHAR-003 cannot compute an Elf's hit points at 10th level without it.
```

**This is not an RC silence. It is an RC self-contradiction**, and the difference matters for how the alternate source may be used. RC is not being *completed* here; it is being **disambiguated between two things RC itself says**. BECMI is therefore evidence about which RC presentation preserves the lineage mechanic — **not** a substitute authority. RC remains primary (`DEC-0007`).

**Object-level RC exhaustion is satisfied.** `docs/rules/evidence/CLUSTER-002-completeness-audit.md` records all four RC statements as visually verified on the printed page, including that the p. 25 stat block and the p. 25 Class Details prose contradict each other **on a single page**. `CLUSTER-002` Stage-A completeness passed independent human review 2026-08-29. No further RC object bears on the question.

## 2. The RC conflict being disambiguated

| RC location | Object type | Value | Verified |
|---|---|---|---|
| p. 25, Elf stat block, "Hit Dice:" line | Stat block | **+1** | Visually |
| p. 25, Elf Class Details prose | Detailed prose | **+2** ("Two additional hit points are gained at 10th level") | Visually |
| p. 129, Maximum Hit Points (Demihumans) Table, Elf row | Table | **+2** (54 + 27 + 2 = 83) | Visually |
| p. 130, Creating High-Level PCs, Step 6 per-class list | Procedural list | **+1** | Visually |

Two and two, split across two chapters, with one contradiction intra-page.

## 3. Sources consulted, and why these

`SOURCE_HIERARCHY.md` §3 orders alternate sources: **BECMI** first, then B/X, then Holmes/OD&D. The Elf's maximum level is 10, so the governing BECMI material is the **Expert** rulebook (levels 4–14) for the class entry, and the **Companion** rulebook for demihuman post-maximum-level progression.

| # | Source | Archive identifier | Role |
|---|---|---|---|
| 1 | *D&D Set 2: Expert Rules* (Mentzer, TSR, 1983) — Players Manual | `dungeons-dragons-set-2-expert-rules` | Governing Elf class entry |
| 2 | *D&D Set 3: Companion Rules* (Mentzer, TSR, 1984) — DM's Book | `dungeons-dragons-set-3-companion-set` | Demihuman maximum hit points; demihuman Attack Ranks |

**B/X, Holmes, and OD&D were NOT consulted, deliberately.** BECMI is the highest-priority lineage source and it answered the exact question unanimously, with no internal conflict. Descending further would be the broad edition browse `RULE_CARD_RESEARCH_PROTOCOL.md` §15 prohibits. This is recorded as a deliberate scope boundary, not an omission — if the human reviewer wants B/X corroboration, it is a separate, bounded request.

## 4. Method — structure-first, per `DEC-0010`

The active protocol was applied to the alternate source as well as to RC, because the failure mode `DEC-0010` exists to prevent is not RC-specific.

| Step | What was done |
|---|---|
| Source structure / finding aids | Expert Players Manual Contents inspected; "Character Classes — Demi-Human: Elf / Elf Charts and Tables" located as the governing entry |
| Governing source-object inventory | Elf prose entry; Elf Experience Table; Elf Saving Throws table; Elf "Hit Dice:" line. Companion: Elf Special Attacks/Defenses entry; Elf Attack Rank table; demihuman maximum-hit-points table |
| **Visual inspection** | **Every object below was read as a page image**, not from OCR. The Expert OCR for this region is severely degraded (mixed Cyrillic substitution in the Dwarf/Elf columns), which is precisely why §9.2 makes visual verification mandatory |
| Complete-entry inspection (§9.7) | The whole Elf entry was read as a unit — prose, saving throws, experience table, and Hit Dice line — not a search window |
| Duplicate presentations (§9.1 class I) | Searched the whole Expert book for every `Hit Dice:` line and every `10th level` occurrence, to find any second Elf HP statement. **Exactly one exists.** Companion checked independently for a second presentation |
| Negative-finding discipline (Guardrail B) | The absence of a `+1` statement is reported below as "not located after inspecting the enumerated objects", not as a bare claim that BECMI contains none |

**Pages visually verified:** Expert Players Manual p. 18 (leaf `n19`); Companion DM's Book p. 22 (leaf `n59`) and p. 23 (leaf `n60`).

## 5. Findings

### Finding E1 — BECMI Expert p. 18, Elf class entry: **+2**

Printed at the foot of the Elf column, immediately beneath the Elf Experience Table:

```text
Hit Dice: 1d6 per level, 9d6 maximum; +2 hit points at 10th level.
```

with the table's own footnote `*Constitution adjustments no longer apply.` attached to the level-10 row. The Elf Experience Table's Level column enumerates **1–10** and stops, ending `10*  10th Level Lord Wizard  600,000`. The entry's opening sentence reads "An elf may only advance to 10th level."

The adjacent Dwarf entry on the same page reads `Hit Dice: 1d8 per level, 9d8 maximum; +3 hit points per level thereafter.`

**Note the deliberate wording difference, which is itself evidence the value is considered:** the Dwarf gets its gain *per level thereafter* (10th–12th), the Elf *at 10th level* (a single event, because 10 is its cap). This is not loose phrasing; it tracks the two classes' different caps.

### Finding E2 — BECMI Companion DM's Book p. 22: **+2**, and RC p. 129 is its verbatim descendant

Under "Hit Points *Maximum*", the demihuman table reads:

| | Dice Rolls | Con. Bonus | L 10-12 | Maximum Total |
|---|---|---|---|---|
| Dwarf | 72 | 27 | +9 | 108 |
| **Elf** | **54** | **27** | **+2** | **83** |
| Halfling | 48 | 24 | - | 72 |

and the human table on the same page reads Cleric 54/27/87/97/108; Fighter 72/27/111/131/153; Magic-user 36/27/69/79/90; Thief 36/27/75/95/117.

**Every one of those numbers is identical to RC p. 129**, as independently visually verified and recorded in `CLUSTER-002-completeness-audit.md` §5 — including the shared `L 10-12` column header that RC prints as `Lvl 10-12`, and including the explanatory note about halflings, dwarves, and elves-versus-magic-users. The introductory sentence is also carried over: "Hit points for demi-humans are limited by their maximum levels (halflings 8, elves 10, dwarves 12)."

### Finding E3 — BECMI Companion DM's Book p. 23: the Elf Attack Rank progression is also inherited verbatim

The Hit Roll Charts give the Elf's post-maximum-level XP thresholds by Attack Rank: C 600,000*, D 850,000, E 1,100,000, F 1,350,000, G 1,600,000, H 1,850,000, I 2,100,000, J 2,350,000, K 2,600,000, L 2,850,000, M 3,100,000 (`*XP when maximum level is reached`).

**These are exactly the values RC p. 26's Elf Experience Table lists below its terminating level-10 row**, as visually verified in `CLUSTER-002-completeness-audit.md` §2 — the same table whose omission produced `DEC-0010`.

### Finding E4 — no BECMI statement of `+1` was located

After inspecting the objects enumerated in §4 — the complete Elf entry, every `Hit Dice:` line in the Expert Players Manual, every occurrence of `10th level` in it, and the Companion's demihuman maximum-hit-point and Attack Rank material — **no BECMI statement assigning the Elf a +1 gain at 10th level was found.** BECMI is internally consistent on this question.

Stated per Guardrail B: this is a research-operation claim about the objects inspected, not a claim that no such sentence exists anywhere in the BECMI corpus.

### Finding E5 — every other class's fixed gain is preserved unchanged in RC

| Class | BECMI Expert | RC | Match |
|---|---|---|---|
| Cleric | +1 per level | +1 | ✔ |
| Fighter | +2 per level | +2 | ✔ |
| Magic-user | +1 per level | +1 | ✔ |
| Dwarf | +3 per level | +3 | ✔ |
| **Elf** | **+2 at 10th** | **contested +1 / +2** | **the sole discrepancy** |

## 6. Lineage classification (task §13)

| BECMI statement | Classification against the RC conflict |
|---|---|
| Expert p. 18 Elf `Hit Dice:` line | **Supports +2** |
| Companion p. 22 demihuman maximum-HP table | **Supports +2** |
| Companion p. 23 Elf Attack Rank table | Not comparable *(establishes descent of RC p. 26, not the HP value)* |
| Any BECMI statement supporting +1 | **None located** (Finding E4) |
| Internally conflicting BECMI statements | **None** |

Under `SOURCE_HIERARCHY.md` §6 the relationship is **Preserved** — RC preserves the BECMI mechanic in two of its four statements.

## 7. Textual genealogy — separating source fact from editorial inference

`DEC-0010` §9.6 forbids resolving conflicts by object type, and Stage A expressly refused to use majority-counting or arithmetic to pick a value. Neither is used here. The argument is genealogical, and its two halves are labelled.

**SOURCE FACTS (each independently visually verified):**

1. BECMI Expert p. 18 states the Elf gain as **+2**.
2. BECMI Companion p. 22 states the Elf maximum-HP contribution as **+2**, total **83**.
3. RC p. 129's two maximum-hit-point tables reproduce BECMI Companion p. 22's numbers **exactly**, including the shared column header and the explanatory note.
4. RC p. 26's Elf Attack Rank thresholds reproduce BECMI Companion p. 23's **exactly**.
5. RC preserves BECMI's fixed gain **unchanged for every other class** (Finding E5).
6. RC's own Elf Class Details prose — "Two additional hit points are gained at 10th level" — is the same statement as BECMI Expert's, in RC's own words.
7. No BECMI ancestor for a `+1` Elf gain was located.

**EDITORIAL INFERENCE (reasoning, not source text):**

- RC p. 129 was carried over from BECMI Companion p. 22 rather than independently recomputed. *Basis: complete numerical identity across seven rows, two tables, a column header, and a prose note. Strong, but an inference.*
- The RC passages reading `+1` are condensation/transcription artifacts rather than a deliberate revision. *Basis: a deliberate Elf-only change would be the single exception to RC's otherwise exact preservation of every class's gain (fact 5); it would have to have been made without updating the inherited maximum-HP table (facts 2–3); and it would have to coexist with the contradicting prose on its own page (fact 6).*

**The competing story, stated fairly.** RC could instead have *deliberately* reduced the Elf's gain from +2 to +1 and simply failed to update the inherited p. 129 table, leaving `83` stale. That reading is coherent and cannot be excluded from the text alone. It is weaker because it requires an unannounced, class-specific balance change that (a) is the sole departure from BECMI across all five classes checked, (b) was not propagated to the table RC reprinted from the source being revised, and (c) was contradicted in the same paragraph block of the class entry that supposedly carries it. But it is not impossible, and the reviewer should weigh it rather than take the recommendation on trust.

## 8. Outcome

Task §14 offers three outcomes. This research reaches **A — lineage clearly supports +2**.

```text
PROPOSED:
    Elf fixed hit-point gain at 10th level = +2

PROVENANCE:
    Rules Cyclopedia internal conflict,
    disambiguated by closest-lineage (BECMI) evidence.
    RC remains primary. BECMI is not the authority for this value;
    it identifies which of RC's two statements preserves the mechanic.
```

**This is a proposal, not a decision.** The two comparable RC self-contradictions in this cluster — the Elf maximum level and the Druid maximum level — were both settled by **human adjudication**, not by agent judgement, and this one is of exactly the same kind. It is carried into `hit_points_and_hit_dice.md` as a specified value so the card is executable, and simultaneously listed among the card's Open Questions and in the Stage-B report's "Remaining Human Decisions" so that approving the card is a conscious ratification of this resolution rather than an accidental one.

`STOP — INTERNAL SOURCE CONFLICT REQUIRES REVIEW` is **not** re-triggered: protocol §10.2.2 case 2 prohibits an agent *silently* choosing between conflicting passages, and nothing here is silent. Case 3's conditions are met — every governing object inspected, both readings recorded, the resolution path explicit and auditable.

## 9. What this research does NOT establish

- It does **not** reopen the Elf maximum level (human-adjudicated at 10) or the Druid maximum level (human-adjudicated at 36).
- It does **not** license importing any other BECMI mechanic. Nothing encountered incidentally — Elf strongholds, Clans, Tree of Life, Combat Options, breath-weapon resistance at 1,600,000 XP — is imported, and none of it was researched beyond recognising it as out of scope (`RULE_CARD_RESEARCH_PROTOCOL.md` §15).
- It does **not** bear on the Chapter 19 "Demihuman and Mystic Experience Levels" variant, which is `NOT ENABLED` for V1 (`DEC-0008`) and whose own per-level hit-point figures must not be confused with the core rule (`CLUSTER-002-completeness-audit.md` Finding 8).
- It does **not** establish anything about halfling or thief fixed gains; those were not the question and were not researched.
