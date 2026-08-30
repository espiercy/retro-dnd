# CLUSTER-002 Stage B — Synthesis Record, Legacy Comparison, and Dependency Findings

> **Stage-B artifact, 2026-08-29.** Produced under `RULE_CARD_RESEARCH_PROTOCOL.md` (`DEC-0009` as amended by `DEC-0010`, `Approved` 2026-08-29) on explicit human authorization. It records the reasoning behind the four drafted Rule Cards, the protocol-required legacy comparison, and the repository metadata findings.
>
> **This document is not a Rule Card and authorizes nothing.** The four cards it accompanies are `AWAITING_APPROVAL`. No implementation is authorized (`ARCHITECTURE.md` §15.2, §16).

---

## 0a. Human rulings recorded 2026-08-29 — Stage B complete, cards ready for review

The human project owner reviewed the corrected remediation and issued four binding rulings. **All executable ambiguity in this cluster is now either resolved transparently or explicitly deferred.**

| Ruling | Question | Decision | Provenance |
|---|---|---|---|
| **SR-1** | Elf fixed HP at 10th level | **`+2`** | **Simulator Ruling** |
| **SR-2** | May a Mystic raise Dexterity through the 2-for-1 trade? | **Yes** — ordinary two-prime-requisite rule; no Mystic-specific exception | **Simulator Ruling** |
| **SR-3** | Chapter 13 score switch | **Included in V1**; runs **before** eligibility; **may** establish a class minimum; the trade runs after and **never** can | **Simulator Ruling** + project scope decision |
| **SR-4** | Discard criterion | **No score above 9 OR two scores below 6**; player may keep the character anyway | **Simulator Ruling** |
| **SR-5** | May the post-selection trade breach a selected class's creation minimum? | **No.** Eligibility is established before the trade and **must remain true after it** — trade rule **R10** | **Simulator Ruling** |

**SR-5 closes an edge case SR-3's ordering exposed** and which earlier drafts had recorded as accepted behaviour: a character could qualify as a Mystic on Wisdom 13, select Mystic, then trade Wisdom to 12 and finish creation as a Mystic who fails the Mystic requirements. RC's exchange restrictions protect Constitution, Charisma and Dexterity but **not** Wisdom, and RC never composes the trade with the requirements table. The Mystic's Wisdom is the **only** materially binding case. The asymmetry is deliberate: the trade can neither **establish** eligibility nor **destroy** it.

**None is classified as `Rules Cyclopedia Explicit`, `Necessary Mechanical Consequence`, or `Alternate-Source Compatible Completion`.** Each is a project adjudication of a question the sources leave open, and each records the reading it rejected. **The historical conflicts are not resolved by these rulings — only the simulator's behaviour is.**

**Full three-stage history of the Elf value, preserved deliberately:**

```text
Stage-B draft 1   +2         WITHDRAWN — rested on a false claim of BECMI unanimity
Correction        UNRESOLVED research outcome INCONCLUSIVE; BECMI itself split
Human ruling      +2         Simulator Ruling over sources that demonstrably disagree
```

**The final `+2` is not the withdrawn `+2` restored.** The first asserted the sources agreed; this one adjudicates sources that do not. That distinction is the whole governance value of the episode and must not be flattened in later summaries.

**Governance outcome:** the alternate-source failure is converted into durable governance rather than institutional memory — `DEC-0011` (`PROPOSED — AWAITING HUMAN APPROVAL`) with a drafted, **not-in-force** `RULE_CARD_RESEARCH_PROTOCOL.md` §15.1.

## 0. ⚠ CORRECTED 2026-08-29 — the research failure this cluster exposed

**A material Stage-B research failure was found by independent human review after the first version of this record.**

The first version stated:

```text
BECMI is unanimous at +2.  No +1 statement located.  No internal BECMI conflict.
Outcome A — lineage clearly supports +2.
```

**That is withdrawn.** BECMI is a **five**-volume lineage; the research inspected **two**, found them to agree, and generalised to the lineage. The **Master Set** (Players' Book p. 12) states the Elf gains **`+1` hp at 10th level**, and Master p. 2 carries an explicit conflict-precedence rule. **BECMI is not unanimous — it was revised.**

| | Withdrawn | Corrected |
|---|---|---|
| BECMI lineage | unanimous `+2` | `+2` (Expert, Companion) → **`+1` (Master)** — **NOT UNANIMOUS** |
| Elf outcome | **A** — `+2` proposed and written into `CHAR-003` | **C** — inconclusive → **`HUMAN RULING REQUIRED`**; no value specified |
| `CHAR-003` | ready for approval | **NOT READY** |
| `CHAR-001` | "four non-blocking questions" | **NOT READY** — U3 blocks (Mystic, required V1 content); U2 needs a scope decision |
| Stage B | **COMPLETE** | **NOT COMPLETE — remediation required** |

Corrections applied: §4 (rewritten), §7 (Simulator Rulings — the "none required" framing was misleading), §8 (blocking status), plus §10 postmortem and §11 proposed guardrail. **§5 legacy comparison and §6 dependency findings are unaffected and stand.** `CHAR-002` and `CHAR-007` are **materially unaffected**.

**RC Stage-A source completeness is NOT reopened** (`INDEPENDENT REVIEW — PASS`). The defect was Stage-B alternate-source incompleteness. The Elf and Druid **maximum-level** adjudications are untouched.

## 1. What Stage B consumed, and what it refused to consume

**Consumed:** the four human-cleared Stage-A evidence packets; `CLUSTER-002-completeness-audit.md`; the approved cluster boundary; the human adjudications of 2026-08-23 and 2026-08-29.

**Refused:**

- **Prior BECMI research.** `NOT VALID AS CURRENT SYNTHESIS INPUT` by human ruling. Not opened, not cited, no conclusion inherited. The Elf research was performed anew (§4).
- **Later-edition familiarity.** No mechanic was adopted because it is familiar. The specific traps this cluster presented and rejected: "4d6 drop lowest" (RC has no such method at any level); "arrange to taste" as a baseline (RC is roll-in-place; free assignment exists **only** in the above-1st-level Chapter 10 procedure); the six-ability modifier table as the whole of ability effects (RC adds two supplementary tables and Charisma carries three outputs); "tables beat prose" as a conflict rule (expressly rejected by protocol §9.6, and the Elf case is why).
- **The superseded 1974-primary framing.** Used only for the §5 legacy comparison, never as authority.

## 2. Synthesis outcome by card

*(Corrected 2026-08-29.)*

*(Updated 2026-08-29 after the human rulings.)*

| Card | Core specification | Open blocking gaps | Ratifies on approval |
|---|---|---|---|
| `CHAR-001` Ability Score Generation | **Complete and executable** — U1–U4 resolved; Mystic Wisdom edge case closed by SR-5 | **None** | SR-2, SR-3, SR-4, **SR-5** |
| `CHAR-002` Race & Class Eligibility | **Complete and executable** | **None** | — (consumes SR-3's output; its result is SR-5's invariant) |
| `CHAR-003` Hit Points & Hit Dice | **Complete and executable** | **None** — W1 resolved | SR-1 |
| `CHAR-007` Ability Score Effects | **Complete and executable** | **None**. All five Stage-A boundary questions closed | — |

**All four are ready for human Rule Card review.** Note the sequence this record has been through: the first version claimed no card was blocked (wrong — it used *non-blocking* for questions that left required V1 behaviour unspecified); the correction found two blocked; the human rulings unblocked both. **The middle step was not a detour** — it is what made the rulings explicit rather than assumed.

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

**Rewritten 2026-08-29.** Full record, including the withdrawal: `docs/rules/evidence/CHAR-003-elf-hp-alternate-source-research.md`.

**Corrected source inventory — all five BECMI volumes dispositioned, none on assumption:**

| Volume | Levels | Elf fixed gain | How dispositioned |
|---|---|---|---|
| Basic (Set 1) | 1–3 | *none* | **Inspected** — entry gives only `Hit Dice: 1d6 per level`; zero `10th level` occurrences |
| **Expert** (Set 2) p. 18 | 4–14 | **`+2`** | **Visually verified** |
| **Companion** (Set 3) DM p. 22 | 15–25 | **`+2`** | **Visually verified** |
| **Master** (Set 4) p. 12 | 26–36 | **`+1`** | **Visually verified — missed entirely by the first pass** |
| Immortals (Set 5) | post-36 | *none* | **Inspected** — zero occurrences of "elf" in the volume |

**BECMI is NOT unanimous. It was REVISED:** `+2` → `+1` at Master. Master's Elf Experience Table also revises the Elf's spell progression in the same object, so this was deliberate. Master p. 2 additionally carries a precedence rule: *"If you discover a contradiction between this set and previous sets, the rules given here should be used."*

**Genealogy — RC is a composite that inherited from both branches:**

- *Fact:* RC p. 129's maximum-hit-point tables reproduce BECMI **Companion** p. 22 number for number, header and note included — carrying `+2` into RC.
- *Fact:* RC p. 25's stat block and RC p. 130 Step 6 track **Master**'s `+1`, the stat block closely echoing Master's phrasing.
- *Fact:* **RC p. 26's Elf Experience Table matches EXPERT, not Master** — RC's level-10 spell row is `3 3 3 3 2` (Expert's exactly); Master's is `5 4 3 2 1`.
- *Inference (well-supported, explanatory only):* RC absorbed both branches and never reconciled them. This explains all four RC statements and the same-page contradiction — but knowing **how** RC became inconsistent does not establish **which** value it intends.
- *Retired:* the first pass's "RC matches BECMI for every other class" argument is **non-discriminating** — Expert and Master agree for those classes.

**Master's precedence rule does not settle it.** It is a BECMI-internal instruction for using the boxed sets together. RC is a later consolidating product that does not incorporate it, and `SOURCE_HIERARCHY.md` gives no basis for importing an alternate source's meta-rule into interpretation of the primary source. Treating "Master is later, therefore `+1`" as decisive would be the mirror image of the error being corrected. It is recorded as an argument available to the adjudicator.

**Outcome C — inconclusive.** Alternate-source research **does not cleanly disambiguate RC**.

```text
Elf fixed HP at 10th level:  UNRESOLVED — HUMAN RULING REQUIRED
```

Neither value is written into `CHAR-003`. The card's Elf gain is unset and its tests are guards (H22–H25). Both cases are laid out for the adjudicator in the research record §8.

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

**Dispositioned 2026-08-29 on human direction. Each is `ADOPT NOW`, `DEFER`, or `REJECT`.**

| # | Proposal | Disposition | Rationale (one sentence) |
|---|---|---|---|
| **P1** | Druid transition → `CHAR-013`, with `CHAR-008` / `ADV-002` dependencies | **DEFER FOR HUMAN GOVERNANCE** | Moving a whole transition procedure into `CHAR-013` is a scope decision about what that entry owns, not a metadata correction, and `CHAR-013` is already flagged `SPLIT CANDIDATE` — the evidence is recorded on `CHAR-002` §B so nothing is lost by waiting. |
| **P2** | Mystic downstream material → `ADV-001`, `ADV-002`, `CHAR-008`, `CHAR-009`/`TREAS-004` | **ADOPT NOW** | These are pointer notes onto **existing** entries for material RC plainly locates outside creation eligibility; no new ID, no scope change, and a future `ADV-001` researcher would otherwise have to rediscover the tithe/donation XP condition. |
| **P3** | Assign a Rule ID to the Chapter 13 general Ability Check | **DEFER FOR HUMAN GOVERNANCE** | Creating a new Rule ID is exactly the meaningful scope decision that must not be silently invented; `CHAR-007` §4.4 already establishes it is *not* `CHAR-007`'s, which is all this task needed to settle. |
| **P4** | `CHAR-001` RC source-location note | **ADOPTED — already applied** | Pure factual correction of a source citation (Ch. 1 + Ch. 10 p. 130 + Ch. 13 p. 145), and the omission is precisely what let a false negative finding stand in Stage A. |
| **P5** | `ADV-001` structural note on the Experience Bonuses and Penalties Table | **ADOPT NOW** | Records a verified structural fact — the table is **not** uniform (Elf conjunctive; Halfling distinguishes *or* from *and*; Mystic penalties halved) — onto an existing entry, as a warning against reading it as a single rule. |

**Adopted in this task: P2, P4, P5** (all onto existing entries). **Deferred: P1, P3** — both would assign or materially redefine ownership of a Rule ID.

### 6.3 Explicitly **not** proposed

- **No `CHAR-002 → CHAR-007` dependency.** Every eligibility requirement RC states is a raw-score threshold, never an adjustment value. This was the mandatory open question the cluster posed, and the answer is negative.
- **No new runtime abstraction.** No `CharacterBuilder`, `CharacterCreationEngine`, `Player`, `Party`, `CreationWorkflow`, `GameState`, or `CharacterManager` is specified, named, or implied. The cards specify rules; ordering constraints are stated as constraints, not as an orchestrator.
- **No `CLUSTER-002` expansion.** The boundary remains `CHAR-001`, `CHAR-002`, `CHAR-003`, narrowed `CHAR-007`.

## 7. Simulator Rulings

**Corrected 2026-08-29.** The first version said *"None proposed. None required"* while simultaneously recording that U3 "blocks Mystic trades". **Those were inconsistent**, and the wording hid a real approval gate behind the phrase *non-blocking*.

**No Simulator Ruling is drafted or self-approved** — §16 forbids both. But two questions now leave **required V1 behaviour unspecified** and are escalated as blocking:

| Item | Chain status | Blocking? |
|---|---|---|
| **`CHAR-003` W1 — Elf fixed gain** | Gap-directed research **performed and INCONCLUSIVE** (§4). Not a missing mechanic — a choice between two values RC states. **Human adjudication**, like the Elf and Druid level caps | **YES — blocks `CHAR-003`** |
| **`CHAR-001` U3 — Mystic Dexterity raise** | RC does not establish it; lineage research **cannot** — the Mystic is not a BECMI core class (Master p. 2 offers it as a DM conversion suggestion). Meets §16's preconditions; escalated as a question with alternatives, **not drafted, not self-approved** | **YES — blocks `CHAR-001`** |
| `CHAR-001` U2 — Ch. 13 switch scope/ordering | A **project scope decision** (does V1 include the switch?) before it is a rules question | **YES — blocks `CHAR-001`** until scoped |
| `CHAR-001` U4 / `CHAR-002` V1 | Contingent on U2; mechanically bounded already | No |
| `CHAR-003` W2, W3 | Moot / not V1-wired | No |
| `CHAR-007` | No unresolved mechanics | No |

**Rule applied going forward:** a question may be called *non-blocking* only if the card remains fully executable for **all required V1 content** without it. U3 fails that test, and the earlier draft should not have called it non-blocking.

## 8. Remaining Human Decisions

Ordered by consequence.

*(Corrected 2026-08-29 — three decisions block approval, not one.)*

| # | Decision | Where | Blocking | Notes |
|---|---|---|---|---|
| **1** | **Elf fixed HP at 10th level — `+1` or `+2`** | `CHAR-003` §4.1, W1 | **Blocks `CHAR-003`** | RC 2-v-2; BECMI split (Expert/Companion `+2` → Master `+1`); RC inherited from both. Evidence for each side in the research record §8. **No default exists** — guarded by H22–H25 |
| **2** | **May a Mystic raise Dexterity through the trade?** (U3) | `CHAR-001` §4 | **Blocks `CHAR-001`** | Mystic is required V1 content, so this is not optional behaviour. Lineage cannot help — Mystic is not a BECMI core class. Guarded by X2 |
| **3** | **Does V1 include the Chapter 13 score switch at all?** (U2) | `CHAR-001` §6.2–§6.4 | **Blocks `CHAR-001`** | A **scope** decision. Deciding "no" closes U2 **and** U4/V1 at once without resolving any RC ambiguity. Guarded by X3 |
| 4 | Discard criterion, and whether V1 models discard at all (U1) | `CHAR-001` §6.1 | No | Class A. If V1 omits it, the threshold never needs deciding. Guarded by X1 |
| 5 | Adopt or reject P1–P5 | §6.2 | No | Affects future cards, not this cluster |
| 6 | Adopt or reject the proposed **alternate-source completeness guardrail** | research record §11 | No | Governance; prevents recurrence of this failure |

**`CHAR-002` and `CHAR-007` require no decision from this list** and are candidates for approval on their own merits.

## 9. What was not done

Not performed, and not authorized: Rule Card approval; implementation planning; production implementation; implementation tests; any `src/` or `tests/` change; any merge to `main`; broad alternate-source survey; adoption of any P1–P5 proposal; assignment of any new Rule ID; expansion of `CLUSTER-002`.

```text
CLUSTER-002 Stage B:   COMPLETE — human rulings SR-1..SR-5 recorded 2026-08-29
Rule Card status:      AWAITING_APPROVAL (all four)
    CHAR-001           ready for review — ratifies SR-2, SR-3, SR-4, SR-5
    CHAR-002           ready for review
    CHAR-003           ready for review — ratifies SR-1
    CHAR-007           ready for review
Governance:            DEC-0011  PROPOSED — AWAITING HUMAN APPROVAL
                       protocol §15.1  DRAFTED, NOT IN FORCE
Deferred:              P1 (Druid transition owner), P3 (Ability Check Rule ID)
Implementation:        NOT AUTHORIZED
Next gate:             HUMAN DEC-0011 AND RULE-CARD REVIEW
```

## 10. Postmortem and 11. Proposed guardrail

Both live in `docs/rules/evidence/CHAR-003-elf-hp-alternate-source-research.md` §10 and §11, alongside the evidence they concern, rather than being duplicated here.

**§10 — postmortem**, in one line each: research stopped at the point of *apparent confirmation* rather than *coverage*; volume selection was driven by where the answer was expected (level 10 ∈ Expert's 4–14) rather than by what the lineage contains, so Master was filed as "levels 26–36, not relevant" and never tested; "unanimous" rested on two positive hits plus a **volume-scoped** negative search generalised to the lineage — Guardrail B's error committed one level up; **no alternate-source completeness checklist exists** (`DEC-0010` §9.3 requires one only for the primary source), so object-level rigour was applied *within* chosen volumes and none at all to *choosing* them; and yes, "closest source that answers the question" was mistaken for "complete relevant lineage". Compounding it, the deliberate, reasoned decision **not** to consult B/X, Holmes and OD&D created an appearance of considered completeness while an unexamined volume of the same higher-priority source sat undispositioned. The adversarial self-review could not catch it because it restarted from the objects *within the already-chosen volumes* — the same lesson `DEC-0010` §10.1.2 drew for primary sources.

**§11 — proposed guardrail (NOT adopted).** A minimal `RULE_CARD_RESEARCH_PROTOCOL.md` §15.1: enumerate and disposition **every core volume** of a named multi-volume lineage before calling it exhaustive, unanimous, consistent or silent; scope-based exclusions must be **verified, not assumed**; lineage-level negative findings are source-property claims under Guardrail B; a later volume restating an earlier class entry is a **duplicate presentation** (§9.1 class I) and must be inspected; and a later volume's **conflict-precedence rule is a mandatory source object** whose scope must be stated — it governs its own lineage and does **not** by itself determine what a later consolidating product intends. **No new decision record is proposed** — this extends `DEC-0010`'s existing principle rather than adding one.
