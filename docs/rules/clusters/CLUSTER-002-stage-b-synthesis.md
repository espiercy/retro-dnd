# CLUSTER-002 Stage B — Synthesis Record, Legacy Comparison, and Dependency Findings

> **Stage-B artifact, 2026-08-29.** Produced under `RULE_CARD_RESEARCH_PROTOCOL.md` (`DEC-0009` as amended by `DEC-0010`, `Approved` 2026-08-29) on explicit human authorization. It records the reasoning behind the four drafted Rule Cards, the protocol-required legacy comparison, and the repository metadata findings.
>
> **This document is not a Rule Card and authorizes nothing.** The four cards it accompanies are `AWAITING_APPROVAL`. No implementation is authorized (`ARCHITECTURE.md` §15.2, §16).

## 1. What Stage B consumed, and what it refused to consume

**Consumed:** the four human-cleared Stage-A evidence packets; `CLUSTER-002-completeness-audit.md`; the approved cluster boundary; the human adjudications of 2026-08-23 and 2026-08-29.

**Refused:**

- **Prior BECMI research.** `NOT VALID AS CURRENT SYNTHESIS INPUT` by human ruling. Not opened, not cited, no conclusion inherited. The Elf research was performed anew (§4).
- **Later-edition familiarity.** No mechanic was adopted because it is familiar. The specific traps this cluster presented and rejected: "4d6 drop lowest" (RC has no such method at any level); "arrange to taste" as a baseline (RC is roll-in-place; free assignment exists **only** in the above-1st-level Chapter 10 procedure); the six-ability modifier table as the whole of ability effects (RC adds two supplementary tables and Charisma carries three outputs); "tables beat prose" as a conflict rule (expressly rejected by protocol §9.6, and the Elf case is why).
- **The superseded 1974-primary framing.** Used only for the §5 legacy comparison, never as authority.

## 2. Synthesis outcome by card

| Card | Core specification | Blocking gaps |
|---|---|---|
| `CHAR-001` Ability Score Generation | **Complete and executable** | None. Four narrow items carried as human decisions, each guarded by a test |
| `CHAR-002` Race & Class Eligibility | **Complete and executable** | None |
| `CHAR-003` Hit Points & Hit Dice | **Complete and executable** | None. Carries one proposed resolution of an RC self-contradiction (§4) |
| `CHAR-007` Ability Score Effects | **Complete and executable** | None. All five Stage-A boundary questions closed |

**No card is blocked. No `STOP —` condition is triggered.**

## 3. The two ambiguity classes, kept apart

`DEC-0010` §10.2.2 makes this distinction binding, and Stage B was disciplined about which bucket each item fell into.

**Class 1 — RC genuinely contradicts itself.** One instance survived to Stage B: the Elf's fixed HP gain. Handled in §4.

**Class 2 — RC is silent, or two RC provisions were never composed.** These are *not* conflicts and lineage research generally cannot close them, because there is no lineage statement about a composition RC itself never contemplated:

| Item | Card | Why alternate-source research was **not** justified |
|---|---|---|
| Discard criterion, two formulations | `CHAR-001` U1 | RC prints both deliberately, in consecutive paragraphs, as DM guidance. A single-formulation ancestor would say what an earlier edition said, not which of two statements RC intends to bind. The prior question — does V1 model a discretionary discard at all? — is project scope |
| Trade ↔ switch ordering | `CHAR-001` U2 | A composition question between two RC provisions RC never cross-references |
| Mystic raising Dexterity | `CHAR-001` U3 | An RC-internal under-inclusive enumeration versus an RC-internal general principle |
| Switch used to meet a minimum | `CHAR-001` U4 / `CHAR-002` V1 | Permission question about a DM-discretionary provision; the mechanics are already determined |
| Floor on fixed gains | `CHAR-003` W2 | Currently moot — every fixed gain is positive |
| Ch. 10 Step 6 alternative-or-restatement | `CHAR-003` W3 | Not wired to V1; both readings agree on outputs |

**This is a positive §15 determination, recorded so a later reviewer can check the reasoning** — not silence about work not done.

## 4. The Elf `+1`/`+2` conflict — the one gap-directed research question

Full record: `docs/rules/evidence/CHAR-003-elf-hp-alternate-source-research.md`. Summary:

**Preconditions met.** Object-level RC exhaustion established (Stage-A completeness `INDEPENDENT REVIEW — PASS`). The gap statement was written in an unusual but honest shape: RC does not fail to answer, it answers inconsistently, so BECMI disambiguates rather than completes.

**Sources, structure-first, visually verified.** BECMI Expert Players Manual p. 18 (Elf class entry, complete); BECMI Companion DM's Book pp. 22–23 (demihuman maximum hit points; Hit Roll Charts). The Expert OCR for the Elf region is severely degraded — mixed Cyrillic substitution — which is precisely why `DEC-0010` §9.2 makes visual verification mandatory rather than advisory.

**Result: BECMI is unanimous at `+2`.** Two independent objects in two books; no `+1` statement located; no internal BECMI conflict.

**Genealogy, source facts separated from inference:**

- *Fact:* RC p. 129's two maximum-hit-point tables reproduce BECMI Companion p. 22 **number for number**, including the shared column header and the explanatory note — and the Elf row's `83` is arithmetically consistent only with `+2`.
- *Fact:* RC p. 26's Elf Attack Rank thresholds reproduce BECMI Companion p. 23 exactly.
- *Fact:* RC preserves BECMI's fixed gain **unchanged for Cleric, Fighter, Magic-user and Dwarf**. The Elf is the sole discrepancy.
- *Inference:* the `+1` statements are condensation artifacts rather than a deliberate revision.

**The competing reading is recorded, not buried:** RC may have deliberately reduced the Elf to `+1` and left the inherited table stale. Weaker, but not impossible. `CHAR-003` §4.1 states it, and test H25 exists so that reversing the resolution fails loudly.

**Outcome A — lineage clearly supports `+2`**, proposed with provenance *"RC internal conflict, disambiguated by closest-lineage evidence."* **RC remains primary; BECMI is not the authority for this value.** B/X, Holmes and OD&D were deliberately not consulted — BECMI answered unanimously and descending further would be the broad browse §15 prohibits.

**This is a proposal.** The two comparable RC self-contradictions in this cluster — Elf maximum level, Druid maximum level — were both settled by **human adjudication**. This one is of the same kind and is listed in §8.

## 5. Legacy Comparison (protocol §13)

**No legacy Rule Card exists for any of the four responsibilities** — `docs/rules/character_creation/` did not exist before this task. There was nothing to withhold and nothing was consulted during Stage A. The comparison is therefore against the **prior 1974-primary inventory entries** as dispositioned in `INVENTORY_MIGRATION_MAP.md`, which is what the protocol's disposition vocabulary can meaningfully be applied to here.

| Legacy entry | Migration disposition | Stage-B finding | Classification |
|---|---|---|---|
| `CHAR-001` Ability Score Generation | RETAIN/REVALIDATE — *"RC's own generation method(s) not yet confirmed identical to 1974's straight 3d6"* | **Confirmed identical for the baseline**: 3d6 per ability, six abilities, roll-in-place, range 3–18. **But the legacy framing was incomplete**: RC adds a 2-for-1 prime-requisite trade with four constraints, two DM-discretionary Chapter 13 provisions, and two above-1st-level methods — one of them **non-random** | **PRESERVED** (baseline method) + **CHANGED** (the responsibility is materially larger than the legacy entry assumed) |
| `CHAR-002` Race & Class Eligibility | REFRAME — RC's roster materially exceeds the old three-book/four-race scope | **Confirmed.** Nine classes; race and class unified for demihumans; four human classes gated on **nothing**; Druid unreachable at creation | **CHANGED** — the reframe was correct and is now specified |
| `CHAR-003` Starting HP & Base Saving Throws | SPLIT CANDIDATE → `CHAR-003` (HP/HD) + `COMBAT-004` (saves) | **Split confirmed correct and executed.** Saving throws were encountered adjacent to Hit Dice in every Chapter 2 entry and were deliberately not pursued | **MOVED TO ANOTHER RESPONSIBILITY** (saves → `COMBAT-004`) |
| `CHAR-007` Ability Score Effects & Cross-System Dependencies | SPLIT CANDIDATE, executed narrowly 2026-08-23 → `CHAR-007` + `COMBAT-004` (Ch. 19 mapping) | **Narrowing confirmed correct.** RC's own Ch. 19 text states Wisdom is the only ability affecting a saving throw under standard rules, so the core Wisdom effect stays with `CHAR-007` and only the optional extension moves | **MOVED** (Ch. 19 mapping) + **PRESERVED** (the core Wisdom effect) |
| Legacy expectation: *"RC's specific modifier table is expected to differ numerically"* | — | **Not confirmed as a difference from anything** — no numeric comparison was made, because no legacy card carried a table. RC's table is specified from RC | **RC DOES NOT SPECIFY** any relationship to the legacy expectation; the expectation is simply retired |

**No superseded OD&D-era authority was reintroduced.** No legacy assumption altered the RC-first synthesis; where the legacy framing and RC disagreed (notably `CHAR-001`'s scope), **RC governed and the legacy framing was corrected.**

## 6. Inventory / Dependency Findings

### 6.1 Applied in this task

All are evidence-backed metadata corrections in `docs/rules/INVENTORY.md`. **No lifecycle status was invented and no Rule ID was created.**

| # | Change | Basis |
|---|---|---|
| A1 | **`CHAR-003` dependencies gain `CHAR-007`** | Binding direction 2026-08-29, and RC's own text: the "Roll for Hit Points" step states **no** modifier value and redirects to the Bonuses and Penalties table. `CHAR-003` cannot produce an authoritative value without it |
| A2 | **`CHAR-007` downstream consumers gain `CHAR-003`, `COMBAT-002`, `COMBAT-003`, `EXP-005`** | The reciprocal of A1, plus the §2 effect-assignment table in `ability_score_effects.md` |
| A3 | **`EXP-005` gains `CHAR-007` and `ENC-002` dependencies** | RC p. 147: the Open Doors procedure consumes the Strength adjustment, and **a failed attempt forfeits surprise** |
| A4 | **`CHAR-007` RC source loses "Chapter 13 (ability-check procedure)"** | The ability check is a distinct responsibility (§4.4 of the card) and no longer belongs in this entry's source list |
| A5 | **`CHAR-001` RC source corrected** to include Ch. 10 p. 130 and Ch. 13 p. 145 | Proposal P4, applied: the responsibility is materially larger than "Chapter 1", and the omission is what let a false negative finding stand in Stage A |
| A6 | **`CHAR-002` RC source corrected** to include the complete Druid and Mystic entries; note added that no `CHAR-007` dependency exists | Direct consequence of the complete-entry inspection and of the mandatory open question's negative answer |
| A7 | **Four `Status` cells: `Unresearched` → `Stage-B drafted — AWAITING_APPROVAL`**, each with its card path | Reflects reality; mirrors the card lifecycle rather than inventing a new vocabulary |

### 6.2 Proposed, **not** applied — each is a scope/governance decision

`RULE_CARD_RESEARCH_PROTOCOL.md` and `AGENTS.md` §12 reserve these for the human project owner. Assigning a new Rule ID, or moving a responsibility between cards, is not an agent action.

| # | Proposal | Detail |
|---|---|---|
| P1 | **Druid transition → `CHAR-013`**, with `CHAR-008` and `ADV-002` dependencies | The complete Druid entry adds a 29th-level upper bound, woodland residence, a DM-rolled 1d4-month meditation, testing and instruction by a higher-level druid, admission to the realm, and ongoing alignment/residence maintenance. **None is creation eligibility**; `CHAR-002` is unaffected and `CLUSTER-002` is **not** expanded |
| P2 | **Mystic downstream material** → `ADV-001` (Strength-determines-XP-bonus disambiguation; tithe-and-donate XP condition), `CHAR-009`/`TREAS-004` (never armor or protective magic), `ADV-002` (oath sanction: expelled, no new levels, −1 level/year), `CHAR-008` (75%-Lawful *tendency*, not a requirement) | Creation eligibility is complete at p. 7 and stays with `CHAR-002` |
| P3 | **Chapter 13 Ability Checks: assign a Rule ID** | Established as **not** `CHAR-007`'s (different mechanic, audience, and location). It shares its resolution mechanic with `CHAR-012` (General Skills), which should inform where it lands. `CHAR-007` does not name it |
| P4 | **`CHAR-001` scope note** | The card's real surface includes Chapter 13 DM provisions and Chapter 10 above-1st-level methods. `INVENTORY.md` lists `CHAR-001`'s RC source as "Character Creation" only; a source-location note (Ch. 1, Ch. 10 p. 130, Ch. 13 p. 145) would help the next researcher |
| P5 | **`ADV-001` structural note** | The Experience Bonuses and Penalties Table is **not uniform across classes** — the Elf uses a conjunctive two-ability rule, the Halfling distinguishes *or* from *and*, and the Mystic's penalties are halved. Recorded for `ADV-001`, whose card does not exist |

### 6.3 Explicitly **not** proposed

- **No `CHAR-002 → CHAR-007` dependency.** Every eligibility requirement RC states is a raw-score threshold, never an adjustment value. This was the mandatory open question the cluster posed, and the answer is negative.
- **No new runtime abstraction.** No `CharacterBuilder`, `CharacterCreationEngine`, `Player`, `Party`, `CreationWorkflow`, `GameState`, or `CharacterManager` is specified, named, or implied. The cards specify rules; ordering constraints are stated as constraints, not as an orchestrator.
- **No `CLUSTER-002` expansion.** The boundary remains `CHAR-001`, `CHAR-002`, `CHAR-003`, narrowed `CHAR-007`.

## 7. Simulator Rulings

**None proposed. None required.**

`RULE_CARD_RESEARCH_PROTOCOL.md` §16 permits a ruling only after RC research, the cross-reference pass, falsification, and gap-directed compatible-source research **together** fail to establish the required behavior. For every open item, an earlier gate stops the chain first:

| Item | Where the chain stops |
|---|---|
| Elf `+1`/`+2` | Gap-directed research **succeeded** (§4). No ruling needed |
| `CHAR-001` U1–U4, `CHAR-002` V1 | Gap-directed research **was not justified** (§3), so §16's precondition is unmet. These are human decisions about RC-internal composition and project scope, not missing mechanics |
| `CHAR-003` W2, W3 | Moot / not V1-wired. No specification depends on either |
| `CHAR-007` | No unresolved mechanics at all |

## 8. Remaining Human Decisions

Ordered by consequence.

| # | Decision | Where | Consequence if deferred |
|---|---|---|---|
| **1** | **Ratify or reject the Elf `+2` resolution** | `CHAR-003` §4.1, W1 | `CHAR-003` cannot be approved without a decision. Reversing it changes §4.1, one table row, §6's Elf row, and tests H22/H23 — nothing else |
| 2 | **Mystic and the Dexterity raise** (U3) | `CHAR-001` §4 | Mystic characters cannot complete the trade step. Guarded by test X2 |
| 3 | **Discard criterion**, and first: does V1 model discretionary discard at all? (U1) | `CHAR-001` §6.1 | None — the core procedure does not depend on it. Guarded by X1 |
| 4 | **Ordering and permitted use of the Chapter 13 switch** (U2, U4/V1) | `CHAR-001` §6.2–§6.4, `CHAR-002` §5 | None — default is that the switch is not applied. Scope bounded to three gates. Guarded by X3 |
| 5 | **Adopt or reject P1–P5** | §6.2 | None for this cluster; affects future cards |

**Decisions 2–4 do not block approval of any card's core specification.** Decision 1 does.

## 9. What was not done

Not performed, and not authorized: Rule Card approval; implementation planning; production implementation; implementation tests; any `src/` or `tests/` change; any merge to `main`; broad alternate-source survey; adoption of any P1–P5 proposal; assignment of any new Rule ID; expansion of `CLUSTER-002`.

```text
CLUSTER-002 Stage B:   COMPLETE — four Rule Cards drafted
Rule Card status:      AWAITING_APPROVAL (all four)
Implementation:        NOT AUTHORIZED
Next gate:             HUMAN RULE-CARD REVIEW
```
