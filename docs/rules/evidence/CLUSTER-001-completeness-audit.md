# Primary-Source Completeness Audit: CLUSTER-001 (EXP-001, EXP-002)

> **Retrospective audit artifact** produced under `docs/decisions/DEC-0010-primary-source-completeness-audit.md` and `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` §9.1–§9.4, §10.1.
>
> This is **not** a Rule Card, not a synthesis, and not authorization to change anything. No Rule Card, `src/` module, test, or completion record was modified. `CLUSTER-001` remains `VERIFIED` with respect to its approved specification and its 2026-08-18 implementation verification.

## 1. Audit Scope and Method

**Responsibilities audited:** `EXP-001` (Dungeon Wandering-Monster Check), `EXP-002` (Dungeon Turn / Time Accounting).

**Method.** The object inventory below was built **independently from the Rules Cyclopedia itself** — from its Table of Contents and its Tables Index — not from `docs/rules/evidence/EXP-001-evidence.md` or from the approved Rule Cards. The prior evidence packet's list was deliberately **not** used as a completeness inventory, per `RULE_CARD_RESEARCH_PROTOCOL.md` §10.1.

**Visual verification.** Page images were obtained from the same archive.org item used for the original research, at full scan resolution, via `archive.org/download/TSR1071TheDDRulesCyclopedia/page/n{leaf}.jpg` (leaf = printed page − 1, established by inspection). Every page listed as *visually verified* below was read as an image, not as OCR text.

`STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED` was **not** triggered.

## 2. Primary-Source Object Inventory — EXP-001

| # | Object | Class (§9.1) | Location | Status |
|---|---|---|---|---|
| 1 | Chapter 7: Encounters and Evasion | A (TOC) | p. 91 ff. | **Visually verified** (pp. 91, 92, 93) |
| 2 | "Exploration and the Game Turn" | F (prose) | p. 91 | **Visually verified** |
| 3 | **Game Turn Checklist** | D/E (structured checklist) | p. 91 | **Visually verified** — 4 steps, matches approved card |
| 4 | "Wandering Monsters" section | F | p. 91 | **Visually verified** |
| 5 | "Wandering Monsters Check" subsection | F | p. 91 | **Visually verified** — every-two-turns, 1d6 |
| 6 | "Important Note" (DM skip provision) | E | p. 91 | **Visually verified** |
| 7 | "Leaving the Game Turn" | F | p. 91 | **Visually verified** — newly inspected |
| 8 | **Game Day Checklist** | D/E | p. 91 | **Visually verified** — wilderness parallel, out of scope |
| 9 | **Chance of Encounter Table** | B/C (named table) | p. 92 | **Visually verified** |
| 10 | "Encounter Distance" | F | p. 92 | **Visually verified** |
| 11 | **Encounter Distances Table** | B/C | p. 93 | **Visually verified** — newly inspected |
| 12 | **Encounter Checklist** | D/E | p. 93 | **Visually verified** |
| 13 | **Monster Reactions Table** | B/C | p. 93 | **Visually verified** — `ENC-003` scope, boundary only |
| 14 | "Wandering Monster Encounters" | F | p. 93 | **Visually verified** |
| 15 | Dungeon Encounters Levels 1-10 Tables | B | p. 94 | Excluded — `MON-001` scope (which monster), not `EXP-001` (whether) |
| 16 | Surprise section / rules | F | p. 92 | Inspected; `ENC-002` scope |
| 17 | Evasion and Pursuit | A | p. 98 | Excluded — `ENC-005` scope, no wandering-check content |
| 18 | Balancing Encounters (Optional) | A | p. 100 | Excluded — `ENC-007`, default OFF per `DEC-0008` |

## 3. Primary-Source Object Inventory — EXP-002

| # | Object | Class (§9.1) | Location | Status |
|---|---|---|---|---|
| 1 | Chapter 6: Movement — "Time" | A/F | p. 87 | **Visually verified** |
| 2 | "Rounds, Turns, and Days" | F | p. 87 | **Visually verified** |
| 3 | **Measurements of Game Time Table** | B/C | p. 87 | **Visually verified** — see §4 Finding 1 |
| 4 | "Skipped Time" | F | p. 87 | **Visually verified** — newly inspected |
| 5 | "Assumed and Defined Actions" | F | p. 87 | **Visually verified** — newly inspected |
| 6 | Encounter Checklist step 1 (turn→round switch) | D/E | p. 93 | **Visually verified** |
| 7 | **Encounter Checklist step 6** ("at least one full turn") | D/E | p. 93 | **Visually verified** — the RC-explicit basis of `max(1, …)` |
| 8 | "Feet vs. Yards", Map Scales, Miniatures | F | p. 87 | Inspected; spatial, not time accounting |
| 9 | Movement rates / Terrain Effects on Movement Table | B/C | pp. 87–88 | Excluded — `EXP-003`/`CHAR-005` scope |
| 10 | Game Day Checklist | D/E | p. 91 | Inspected; day-scale, out of dungeon-turn scope |

## 4. Findings

### Finding 1 — `1 day = 144 turns` was never recorded
**Category: B — INCOMPLETE BUT NON-CONTRADICTORY.**

The **Measurements of Game Time Table** (p. 87) has three rows, not two:

| Measure | Equals | Activities Measured This Way |
|---|---|---|
| 1 round | 10 seconds | Combat, some spell durations |
| 1 turn | 10 minutes | Noncombat movement, some spell durations, exploration of dungeons |
| **1 day** | **144 turns** | Long-distance movement (miles/day), spell research, magical item creation |

`EXP-002`'s evidence and Rule Card record the round and turn rows and omit the day row. The omitted row is arithmetically consistent (24 h × 6 turns/h = 144), so it does **not** contradict or qualify the approved whole-turn credit mechanic, which is dungeon-scoped.

It becomes relevant only if day-scale accounting later enters scope (wilderness travel, `EXP-004` rest, `ADV-003` downtime). No specification or implementation change is implied.

### Finding 2 — "when traveling" qualifier on the dungeon check
**Category: B — INCOMPLETE BUT NON-CONTRADICTORY.**

The **Chance of Encounter Table** (p. 92) dungeon row reads: roll 1d6 every two turns **when traveling**, and roll 1d12 once during the night; on a 1 an encounter occurs.

The approved `EXP-001` card and its evidence record the every-two-turns 1d6 and the trigger-on-1 without the "when traveling" qualifier. Since `EXP-001` consumes an externally-supplied ordinary turn credit and does not itself classify party activity, the qualifier does not change the implemented mechanic. Recorded so a future reader does not mistake its absence for a finding that RC states the rule unconditionally.

### Finding 3 — the dungeon nighttime 1d12 check is unimplemented
**Category: B — INCOMPLETE BUT NON-CONTRADICTORY**, with a flagged upgrade path.

The same table's "Dungeon and city" row specifies a **1d12 roll once during the night** in addition to the 1d6 every-two-turns check. The `EXP-001` evidence packet did record this. The approved Rule Card and `WanderingMonsterCadence` implement only the Game-Turn-Checklist step-4 1d6 path.

This is consistent with the approved card's stated scope (the Game Turn Checklist), and the simulator models neither day/night nor overnight camping, so no currently reachable behavior is wrong. **It would become Category C** if the simulator ever models a party resting overnight in a dungeon. Flagged, not repaired.

### Finding 4 — encounter distance is visibility-dependent
**Category: B — INCOMPLETE BUT NON-CONTRADICTORY.** Belongs to `ENC-001`.

The `EXP-001` evidence packet records arrival distance as 2d6 × 10 feet, citing p. 91. The **Encounter Distances Table** (p. 93) — a named table the packet never inspected — gives three dungeon values by visibility: very good light 4d6 × 10′, dim light 2d6 × 10′, no light 1d4 × 10′.

These reconcile: p. 91's "under normal dungeon conditions… 2d6 × 10′" is the dim-light row. No contradiction. `EXP-001` correctly does not determine distance, so nothing in its specification or implementation is affected. Recorded for `ENC-001`'s future research.

### Finding 5 — the core `EXP-001` mechanic is confirmed
**Category: A — COMPLETE.**

Visually verified on p. 91, the Game Turn Checklist is exactly as the approved card specifies: (1) previously-triggered wandering monsters arrive now, leave the checklist for the Encounter Checklist; (2) Actions; (3) Results; (4) wandering-monster check, 1d6 **every other turn**, dungeon trigger on **1**, monsters encountered **at the beginning of the next turn**. The DM skip provision and the heightened-checking provision ("loud noises, battles, cursed items, or exploring special areas may allow the DM to check… every turn — and possibly with higher chances") are both present as recorded.

### Finding 6 — the `EXP-002` minimum-turn rule is confirmed
**Category: A — COMPLETE.**

Encounter Checklist step 6 (p. 93), visually verified: *"After the encounter ends, begin play with a new turn. Always assume that an encounter takes at least one full turn to resolve."* This is the RC-explicit basis for the `max(1, …)` term in `encounter_turn_cost`, and it is correctly represented in the approved card and implementation.

## 5. Category Summary

| Category | Count | Items |
|---|---|---|
| **A — COMPLETE** | 2 | Findings 5, 6 (core mechanics of both cards confirmed) |
| **B — INCOMPLETE BUT NON-CONTRADICTORY** | 4 | Findings 1, 2, 3, 4 |
| **C — SPECIFICATION-AFFECTING OMISSION** | **0** | None |
| **D — NEW INTERNAL SOURCE CONFLICT** | **0** | None |

**No `APPROVED CONTRACT INCOMPATIBILITY` was found.** No `src/` module, test, Rule Card, or completion record requires change on the strength of this audit.

## 6. Independent Completeness Pass

Performed after the first pass, starting from the RC Table of Contents and Tables Index rather than from the evidence packets or from §2/§3 above.

**What the first audit inspected:** Chapter 7 pp. 91–93 in full; Chapter 6 p. 87 in full.

**What it could plausibly have missed:** Tables-Index entries whose titles do not contain the terms "wandering", "turn", or "time"; restatements of the mechanic in later DM-facing chapters; the monster-side encounter tables.

**Additional objects found by the second pass:**

- `Measurements of Game Time Table . 87` — located via Tables Index; produced Finding 1.
- `Encounter Distances Table . 93` — located via Tables Index; produced Finding 4.
- `Monster Reactions Table . 93` — located via Tables Index; confirmed `ENC-003` scope, no `EXP-001` content.
- `Dungeon Encounters Levels 1-10 Tables . 94` — located via Tables Index; confirmed `MON-001` scope.
- `Evasion Table . 99` — located via Tables Index; confirmed `ENC-005` scope.
- "Leaving the Game Turn", "Skipped Time", "Assumed and Defined Actions" — prose sections adjacent to the governing text, newly read in full; no mechanical effect on either card.

**Did any new material change the evidence picture?** No mechanic changed. Four Category-B completeness gaps were added to the record (Findings 1–4), one of which (Finding 3) carries a flagged upgrade path to Category C under a future scope expansion.

**Not certified on keyword grounds.** This pass is certified on the basis that every Tables Index entry in the relevant chapters was read and dispositioned, and every page carrying an operative object was read as an image.

## 7. Why the Original CLUSTER-001 Research Fared Better Than CLUSTER-002's

Recorded because it is diagnostic, not exculpatory.

`EXP-001`/`EXP-002`'s governing content is carried in **prose and in named checklists that OCR linearizes acceptably** — the Game Turn Checklist and Encounter Checklist survived as readable numbered text. The original keyword-driven method therefore happened to reach the decisive material.

`CHAR-003`'s governing content for the escalated question was carried in a **tabular object whose meaning lies in where its rows stop**. The same method could not reach it, and did not.

The difference is a property of the source objects, not of researcher diligence on either occasion. That is precisely why `DEC-0010` makes object enumeration and visual verification mandatory rather than advisory: the method's blind spot is invisible from inside the method.

## 8. Status After This Audit

**`CLUSTER-001 PRIMARY-SOURCE COMPLETENESS: INDEPENDENT REVIEW — PASS`.**

**Lifecycle of this result, in order (none of these steps is rewritten):**

| Date | State | By |
|---|---|---|
| 2026-08-23 | `PASS` — self-issued | original researcher (**not a valid certification**) |
| 2026-08-23 | **Downgraded** to `CANDIDATE PASS — PREPARED FOR INDEPENDENT REVIEW` | original researcher, under proposed `DEC-0010` item 14 / protocol §10.1.2 |
| **2026-08-29** | **`INDEPENDENT REVIEW — PASS`** | **human reviewer** |

> **Recorded 2026-08-29.** The human project owner completed the independent primary-source completeness review required by `DEC-0010` item 14 and protocol §10.1.2, and returned `INDEPENDENT REVIEW — PASS`. The candidate pass is thereby certified by a party other than the researcher that gathered the evidence. **The certification is the human reviewer's, not this artifact's** — the intermediate `CANDIDATE PASS` step above is retained deliberately, because the ordering is the point of `DEC-0010`.

```text
CLUSTER-001 approved specification:      unchanged
CLUSTER-001 implementation:              unchanged, remains VERIFIED
CLUSTER-001 primary-source completeness: INDEPENDENT REVIEW — PASS
                                         (human, 2026-08-29)
Category C specification-affecting omissions: none
Category D new internal source conflicts:     none
Rule Card corrections required:               none
Implementation corrections required:          none
Test corrections required:                    none
```

**The four Category-B completeness gaps (Findings 1–4) remain open and are unaffected by this pass.** They are recorded non-contradictory gaps, not defects; Finding 3 retains its flagged upgrade path to Category C under a future scope expansion.

**Relationship to the 2026-08-18 verification.** `CLUSTER-001`'s `VERIFIED` status was granted on 2026-08-18 against its approved specification and its implementation's passing verification. That history is unchanged and is **not** retroactively rewritten: this completeness audit did not exist at that time, and the original verification is not represented as having included it. This audit is a **later, separate** check of a different question — whether the underlying primary-source evidence was complete — and it passed.
