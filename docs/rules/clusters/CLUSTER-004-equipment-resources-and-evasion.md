# Cluster 4: Exploration Resources and Evasion — Stage-A Record

> **Updated 2026-09-29 for the Stage-A remediation.** The pass-1 body of this record was
> written against two evidence packets that subsequently **failed** independent completeness
> review. This document is rewritten because it is a *status* record, not an evidence artifact;
> the evidence artifacts themselves are preserved unaltered. See §12 for what changed.

## 1. Cluster ID

`CLUSTER-004`

## 2. Boundary

```text
EXP-006   Light & Exploration Resources
ENC-005   Retreat, Pursuit & Evasion (underworld)

DEFERRED, NOT IN THIS CLUSTER
    EXP-004   Rest / Exhaustion Procedure          DEFERRED / SPLIT CANDIDATE
    EXP-010   Party Formation & Marching Order     DEFERRED
```

Human-approved 2026-09-27; see `CLUSTER-004-BOUNDARY-CORRECTION.md` for the boundary and the
deferral rationale, and `CLUSTER-004-BOUNDARY-PROPOSAL.md` for the superseded original
analysis.

## 3. Status

```text
BOUNDARY                    APPROVED  2026-09-27

STAGE A (EVIDENCE)          COMPLETE -- INDEPENDENT COMPLETENESS REVIEW PASSED

    EXP-006   PRIMARY-SOURCE COMPLETENESS: PASS   (review 5)
    ENC-005   PRIMARY-SOURCE COMPLETENESS: PASS   (review 5)

    CURRENT PACKETS
        docs/rules/evidence/EXP-006-evidence-remediated.md
        docs/rules/evidence/ENC-005-evidence-remediated.md

    FIRST-PASS PACKETS, preserved unaltered as the failure record
        docs/rules/evidence/EXP-006-evidence.md          SUPERSEDED
        docs/rules/evidence/ENC-005-evidence.md          SUPERSEDED
        Committed UNALTERED at e33c4e0, BEFORE remediation, deliberately.

    REVIEW HISTORY -- five independent reviews, none retroactively relabelled
        review 1   e33c4e0   FAIL / FAIL   ...completeness-review.md
        review 2   f0d2925   FAIL / FAIL   ...completeness-review-2.md
        review 3   1b61c39   FAIL / FAIL   ...completeness-review-3.md
        review 4   e3115ff   FAIL / FAIL   ...completeness-review-4.md
        review 5             PASS / PASS   ...completeness-review-5.md

HUMAN EVIDENCE REVIEW       GIVEN 2026-09-29  -- both packets ACCEPTED
STAGE B (SYNTHESIS)         EXP-006  COMPLETE   (card APPROVED 2026-10-01)
                            ENC-005  DEFERRED   (explicit human decision; §6 Q1/Q2
                                     unsettled -- see docs/rules/evidence/
                                     ENC-005-evidence-remediated.md)
RULE CARDS                  EXP-006  APPROVED 2026-10-01
                            ENC-005  NONE DRAFTED
IMPLEMENTATION              EXP-006  AUTHORIZED per-slice; Slices A-D ACCEPTED.
                                     EXP-006-PHASE: REVIEW-5-REMEDIATED
                            CLUSTER-004 AS A WHOLE   NOT AUTHORIZED
ALTERNATE-SOURCE RESEARCH   NONE PERFORMED; one candidate question flagged (§8)
SIMULATOR RULINGS           SR-11 PROPOSED AND APPROVED 2026-10-01  (§10)
```

> **Status block corrected 2026-10-03** under independent-review finding `MED-3`. It previously
> read `HUMAN EVIDENCE REVIEW: NOT GIVEN` / `STAGE B: NOT STARTED` / `RULE CARDS: NONE DRAFTED` /
> `IMPLEMENTATION: NOT AUTHORIZED` / `SIMULATOR RULINGS: NONE PROPOSED`, every one of which had
> been overtaken by events this same record documents in §10. **No review verdict, date or
> evidence artifact above is altered** — the five Stage-A reviews and the two superseded first-pass
> packets stand exactly as recorded.

---

## 4. What Stage A found, after remediation

### 4.1 The two cards are still very different sizes — but `EXP-006` is larger than pass 1 thought

| | `EXP-006` | `ENC-005` |
|---|---|---|
| Governing objects | **6 item descriptions + 3 tables + 2 checklists** (pass 1 said: 4 item descriptions, no tables) | 1 prose section, 1 checklist, 1 table, 1 subsection |
| Governing tables | **`Encounter Distances Table` (93) — consumed, not owned**; `Starvation Table` (150) and `Timetrack Table` (149) — boundary | `Evasion Table` (99) |
| Chapters | **4, 7, 13, 14** (pass 1 said: 4 only) | 7, with an 8 boundary |
| Pages | **68–70, 91–93, 149–150, 154** | 91, 93, 98–100, with 104 for routing |
| Printed defects found | **0** (the p. 150 starvation defect is `CHAR-005`'s, already `SR-10`) | **2**, both unadjudicated |
| Hard deps on unresearched cards | 1 (`CHAR-009`, recorded not claimed) | **5** |
| Research risk (§9.4) | **High** — a mechanically significant table drives part of it | **High** |

**Pass 1 concluded `EXP-006` "turned out smaller than its title." That conclusion is
withdrawn.** The card reaches four chapters, not one.

### 4.2 `EXP-006` — the inventory's source attribution is wrong (unchanged, confirmed)

`INVENTORY.md` gives *"Dungeon Adventures chapter"*. **RC has no such chapter.** The Chapter 4
split found by pass 1 is confirmed:

```text
p. 69 TABLE        cost, encumbrance             ->  CHAR-004  [LANDED]
p. 69-70 PROSE     radius, burn time, ignition   ->  EXP-006
```

**But Chapter 4 is not the whole card.** Remediation added Chapter 7 (encounter distance by
visibility), Chapter 13 (no-light consequences; timekeeping; starvation boundary) and Chapter
14 (the blindness corroboration).

### 4.3 The two cards are connected **through the source**, not through analysis

This is the cluster's most interesting structural finding, and pass 1 could not see it because
it never opened p. 93.

```text
EXP-006  produces a party LIGHT STATE (torch/lantern 30' radius, lit or not)
              |
              v
p. 93 Encounter Distances Table, keyed on a VISIBILITY column
   Very good light 4d6x10'   Dim light 2d6x10'   No light 1d4x10'
   (** full darkness with infravision used = Dim light)
              |
              v
ENC-005 step 1 "Contact": "the DM determines the encounter distance"
```

**With one gate**: p. 92 consults that table **only when neither party is surprised**. If
either side is surprised the distance is a flat `1d4 x 10'` and light does not enter.

### 4.4 `ENC-005` — not underworld-specific, and not really unblocked (confirmed, sharpened)

RC gives **one** evasion procedure covering dungeon and wilderness together, and separates only
*naval* evasion. The title's `(underworld)` is a project narrowing, not a source boundary.
RC's own definition (p. 91) is setting-neutral: *"'Evasion' is what happens when an encounter
occurs and one side wants to escape the other."*

The dependency finding is **preserved and sharpened** from "four unresearched cards" to a
six-step table naming each provider and its RC page:

```text
step 1  encounter distance + surprise   ENC-001, ENC-002   Unresearched   pp. 92-93
step 2  surprise states                 ENC-002            Unresearched   p. 93
step 3  morale check                    ENC-004            Unresearched   p. 103
step 4  Evasion Table d100              ENC-005 ITSELF     owned          p. 99
step 5  1d6 initiative                  COMBAT-006         Unresearched   p. 102
step 5  relative speed                  MON-003            Unresearched   p. 88
step 5a morale, every 5 rounds          ENC-004            Unresearched   p. 103
step 5b combat checklist exit           COMBAT-*           Unresearched   p. 102
step 6  rest / bearings                 CHAR-005 §9 [LANDED]; dungeon-lost UNOWNED
```

**Four of six steps cannot execute without an unresearched card. Step 4 is the only step the
card fully owns.** Five distinct unresearched counterparties — against the **three** that were
judged sufficient to defer `EXP-010`.

---

## 5. Cross-card interactions

| Interaction | Direction | Disposition |
|---|---|---|
| **Light state → encounter distance** | `EXP-006` → `ENC-001` → `ENC-005` | **NEW in pass 2.** Printed, via p. 93 and p. 98. Gated on surprise (p. 92). `EXP-006` supplies the state and **owns none of the table** |
| Oil *"poured out and ignited to delay pursuit"* (p. 69) | `EXP-006` → `ENC-005` | **Recorded from both sides; RC states no mechanic** — no adjustment, no delay value, no table row. Nothing invented |
| Chase rounds vs. the 30-round running limit | `ENC-005` → landed `CHAR-005` §9 | **Open — §6 Q4, sharpened.** p. 100: *"For every round the chase lasted, the evaders moved at full running speed"* and *"they need to rest from their exertions."* RC still never links either to the 30-round maximum |
| `Retreat` / `Fighting Withdrawal` → running speed | `ENC-005` ↔ `COMBAT-*` | **NEW in pass 2:** **both** maneuvers carry the bridge, not just Fighting Withdrawal. Maneuvers routed to `COMBAT-*`; the transition is boundary evidence |
| *"Evaders rest"* (step 6) | `ENC-005` → `EXP-004` (deferred) | Followed **only to ownership**. `CHAR-005` §9 owns the 3-turn rest. **`EXP-004` not reopened** |
| Burn time in *turns* | `EXP-006` → landed `EXP-002` | Consumed. RC states hours **and** turns itself |
| Timetrack (p. 149) | `EXP-006` ↔ landed `EXP-002` | **NEW in pass 2:** a tally sheet. **No second time authority.** Its ratios corroborate `EXP-002` |
| Ration spoilage (p. 69) | `EXP-006` ↔ `CHAR-004` **[LANDED]** | **NEW in pass 2.** `CHAR-004` owns price/enc; the dungeon-conditioned duration is description prose. **Ownership not claimed** |
| Starvation (p. 150) | `EXP-006` → `CHAR-005` §7 **[LANDED]** + **unowned causation** | Boundary only. `SR-10` already governs the movement column. **Causation still has no Rule ID** |
| Torch lit/unlit damage | `EXP-006` → `COMBAT-002`, `CHAR-011` | Routed away. `EXP-006` owns whether it is lit, not what it does |
| Infravision | `EXP-006` ↔ `CHAR-009` | Recorded, **not claimed**. p. 93's `**` footnote makes it mechanically relevant |
| Magical light (`Oil of sunlight` etc., p. 146) | `EXP-006` → `MAGIC-*` | **Enumerated and routed.** Opened only to confirm chapter |

---

## 6. Open questions requiring human decision

**None of these may be answered by an implementation or Stage-B agent.**

| # | Card | Question |
|---|---|---|
| **1** | `ENC-005` | **Is the card underworld-only, or does it own RC's general evasion procedure?** RC does not separate dungeon from wilderness. Interacts with the standing Wilderness reachability decision. **Stage B cannot begin without this** |
| **2** | `ENC-005` | **Can the card be specified before its FIVE unresearched providers?** §4.4. `EXP-010` was deferred over three |
| **3** | `ENC-005` | **"Difficult terrain" is undefined.** Examples, no criterion. The second-roll escape is not executable without a DM-input flag |
| **4** | `ENC-005` | **Do chase rounds count against `CHAR-005` §9's 30-round running limit?** Sharpened by p. 100, still open |
| **5** | `ENC-005` | **Scouts: prose `−10%` vs Evasion Table `−15%`.** `INTERNAL SOURCE CONFLICT REQUIRES REVIEW` |
| **6** | `ENC-005` | **Evasion Checklist step 2 says "go to Step 2"** — a self-loop |
| **7** | `ENC-005` | **Does the `Retreat`/`Fighting Withdrawal` running-speed bridge belong here or to `COMBAT-*`?** Evidence now complete on both sides |
| **8** | `ENC-005` | **Does `CHAR-012`'s Caving skill modify step 6?** Blocked on `CHAR-012`, not on this card's coverage |
| **9** | `ENC-005` | **Who owns "lost in a dungeon"?** RC states the condition (p. 100), supplies a procedure only for wilderness (p. 91). No Rule ID |
| **10** | `EXP-006` | **How does a party's carried light map to a `Visibility` category?** ~~RC gives the default (*"normal dungeon conditions"* = `Dim light`) and the infravision case, and nothing between.~~ **SUPERSEDED — see the note below this table.** The approved card's Finding A **withdrew** the equation `normal dungeon conditions → DIM_LIGHT`, and card §Undefined 2 states RC supplies **no rule at all** connecting carried light to the p. 93 column. The question itself stands, and is **`ENC-001`'s**, not this card's. Torch and lantern radii are identical (30′) |
| **11** | `EXP-006` | **Do rations belong to this card?** Evidence now exists: a dungeon-conditioned consumable duration structurally parallel to torch burn time. **No ownership claimed** |
| **12** | `EXP-006` | **Tinderbox ignition outside *"normal (comparatively dry) circumstances"*.** `PRIMARY PROCEDURE NOT YET ESTABLISHED` |
| **13** | `EXP-006` | **What happens when a light source burns out mid-turn?** RC gives durations and a tally aid, and stops |
| **14** | both | **Starvation causation has no Rule ID anywhere in `INVENTORY.md`.** Confirmed still true. Not absorbed |

> **Question 10 corrected 2026-10-03, under review-#3 finding `LOW-7`.** This table was written on
> 2026-09-29 as part of the Stage-A body, but §3, §10 and §13 of this record have since been updated
> for current status, so an uncorrected statement here reads as live rather than historical. Q10 as
> written restated *"normal dungeon conditions = Dim light"* — precisely the inference the approved
> Rule Card's **Finding A withdrew**, and which the card lists among items "recorded so they are not
> reintroduced". Reintroducing it in a record headed *"Open questions requiring human decision"*
> risked a future agent treating it as an available default. **The surrounding Stage-A findings are
> otherwise unaltered and remain the 2026-09-29 record.**

### 6.1 Questions pass 1 raised that remediation **closed**

| Pass-1 question | Outcome |
|---|---|
| *"RC states no consequence for having no light"* | **FALSIFIED.** RC states it at p. 150, corroborated p. 154 |
| *"Is a burn-tracking procedure in scope?"* | **Premise falsified** (p. 149 exists); conclusion survives on new evidence — RC supplies a manual tally instrument, no executable procedure |
| *"Does light modify surprise / reaction / wandering-monster frequency?"* | **RESOLVED — negative**, with the objects inspected named |
| *"Is p. 100 col. 1 out of scope?"* | **FALSIFIED.** It is governing — `Regain Bearings` *is* step 6 |
| *"How is the Evasion Table resolved?"* | **RESOLVED.** Roll-**under** on `d100`, from RC's own worked example |

---

## 7. A note on the research, not only on the cards

Pass 1 was **independently reviewed and failed.** That review, its `FAIL` verdicts and its 15
numbered findings are committed unaltered at `e33c4e0`, before any remediation, and the two
failed packets carry forward-pointer banners rather than rewritten conclusions.

Three points worth keeping:

1. **The General Index caught material for the third time in this project.** Precedent `P-001`
   exists because a `CLUSTER-003` pass once skipped it. Pass 1 *cited* it and missed
   `Blindness . 150, 154` sitting in plain sight. Pass 2 **enumerated** it and used it to reach
   `Rations`, `Dehydration`, `Timekeeping`, `Starvation`, and the `Torch`/`Oil` page ranges.

2. **Pass 1 asserted two source properties it had not earned** (no no-light rule; no
   light-bearing table). Both were Guardrail-B breaches, and both were false. Negative findings
   in pass 2 name what was inspected.

3. **The project's own landed work already contained the refutation.** `CHAR-005` §7 — merged
   in `CLUSTER-003` — cites RC p. 150 for the blindness movement rates. Pass 1 transcribed
   those very multipliers into a note and then asserted the page said nothing. Checking the
   repository against a negative claim is cheap and was not done.

A fourth point, from pass 2 itself: a draft of the remediated `EXP-006` packet called the
p. 150 starvation defect a **new** third printed defect. It is not — it was already located,
escalated and adjudicated as **`SR-10`** under `CHAR-005`. The error was caught by checking the
landed card before finalizing, and it is **recorded in the packet rather than quietly
removed**, because it is the same failure mode as point 3.

---

## 8. Alternate-source research

**None performed. None authorized. One candidate flagged.**

`ENC-005`'s two printed defects (§6 Q5, Q6) are **internal RC conflicts**. Precise gap
statement, as `DEC-0011` requires:

```text
RC p. 99 prints TWO different scout adjustments -- prose "-10%", table "-15%" --
and an Evasion Checklist step 2 that directs the reader back to step 2.  The BECMI
Expert set carries an ancestor evasion procedure that may disambiguate both.
```

**Flagged as a candidate `DEC-0011` question** if the human project owner prefers lineage
disambiguation over adjudicating the conflicts as Simulator Rulings. AD&D remains excluded.

**`EXP-006` requires no alternate-source research.** Every open question on that card is either
a fully mapped RC silence or a governance decision.

---

## 9. Boundaries respected

```text
EXP-004   NOT researched as a unified card. The step-6 rest reference was followed
          only far enough to establish that CHAR-005 §9 owns the running/exertion
          half. No wilderness rest material inspected.

EXP-010   NOT absorbed. ENC-005's procedure needs party SIZE, not marching order;
          no formation, rank or order appears in the section. Confirms landed
          EXP-003 case D32.

EXP-008 / MON-001 / TREAS-001   UNTOUCHED. The wilderness, castle and city encounter
          subtables printed on pp. 96-98 -- the same pages as the evasion section --
          were excluded by name, as were Room Contents / Unguarded Treasure (261).

TERRAIN   No generic terrain mechanic created. The Evasion Table's condition column
          adjusts an evasion PERCENTAGE, not a movement rate. Terrain Effects on
          Movement (88), the Charge terrain list (154) and the previously rejected
          Mystic rough-terrain material were each enumerated and EXCLUDED BY NAME.

SURPRISE / REACTION / INITIATIVE / MORALE   Read to OWNERSHIP ONLY. ENC-002, ENC-003,
          COMBAT-006 and ENC-004 are named as providers; none is specified here.

CONDITIONS   p. 150's Deafness, Invisibility, Paralysis, Prone, Sleep and Stunning
          were read and NOT claimed. EXP-006 owns at most the darkness path into
          blindness, never the condition itself, and no generic condition
          infrastructure is proposed.

STARVATION CAUSATION   NOT absorbed. No Rule ID exists; recorded as a standing gap.

CHAR-004  NOT reopened. No price, encumbrance, Coin, quantity-pricing or legality
          fact is restated or duplicated.

EXP-002   NOT duplicated. The Timetrack Table is dispositioned as presentation/
          tracking; no second time authority is created.

EXP-003   NOT re-derived. Ordinary dungeon movement is consumed, not restated.

MAGICAL LIGHT   Oil of darkness / moonlight / sunlight (146) and the light /
          continual light spells enumerated and routed to MAGIC-*. No magical light
          mechanic transcribed.
```

---

## 10. Simulator Rulings

### `SR-11` — adverse-condition `Fire-Building` governs regardless of a tinderbox

**Owner: `EXP-006`. Human project owner, 2026-10-01.** The cluster's first and only ruling.

```text
If a character has Fire-Building and conditions are ADVERSE, the
adverse-condition Fire-Building procedure governs regardless of whether
the character possesses a tinderbox.

    skill=True, tinderbox=False, conditions=ADVERSE  ->  ROUTED_SKILL_CHECK

The ordinary no-tinderbox 1d6 procedure does not override the
adverse-condition branch.
```

**The ambiguity it resolves.** Accepted Stage-A evidence `E-36` (RC p. 83) establishes two
conditionals **in parallel, with no precedence**: *"If the character is trying to build a fire
**without** a tinderbox… `1d6` roll each round, and on a `1` or `2` he ignites"* and *"If the
character is trying to build a fire **in adverse conditions**… he must make a skill check with
penalties assigned by the DM."* The input `(skill, no tinderbox, ADVERSE)` satisfies **both**
antecedents and RC supplies nothing that chooses between them.

**Scope — narrow by construction.** It resolves **only** that intersection. The two RC-explicit
ordinary branches, the RC-explicit adverse-with-tinderbox branch, and all three RC-silence
refusals are unchanged.

**Provenance.** `Simulator Ruling` — explicitly **not** `Rules Cyclopedia Explicit` (RC states no
precedence), **not** a `Necessary Mechanical Consequence` (neither outcome is forced; the
competing branch is equally well attested), **not** a `Human-Approved Variant` and **not**
`Alternate-Source Compatible Completion` (no source was preferred over RC; no alternate edition
was consulted).

**ID allocation.** `SR-1`–`SR-10` are allocated by `CLUSTER-002` and `CLUSTER-003`. The registry
was inspected rather than assumed: the only prior textual occurrences of `SR-11` were
`CHAR-005`'s two explicit statements that **no `SR-11` exists** — denials, not allocations.

**Recorded on — five locations:** this cluster record; the `EXP-006` Rule Card §Simulator Ruling;
`INVENTORY.md`'s `EXP-006` row; `docs/technical/EXP-006_IMPLEMENTATION_PLAN.md` §11; and
`ARCHITECTURE.md` §15.2.

> **Fifth location added 2026-10-03** under review-#2 finding `LOW-10`. `ARCHITECTURE.md` §15.2
> previously **denied** that `SR-11` existed; that was corrected on 2026-10-03 under review-#1
> finding `HIGH-1`, but this registry — the place a later agent would check — was not updated to
> record the new location. A ruling's registry is only useful if it is complete, and the
> consequence is concrete: the ID-allocation procedure treats a prior textual denial as evidence
> that a number is free, which is exactly how `SR-11` was selected.

---

**No other ruling is proposed by this cluster.** Protocol §16 and `AGENTS.md` §10.7 place rulings
last, after gap-directed alternate-source research; none has been authorized or performed, and
`SR-11` arises not from a gap in RC's coverage but from an **internal ambiguity** the accepted
evidence exposed — two RC statements that overlap without a precedence rule.

Two of `ENC-005`'s open questions (§6 Q5, Q6) are **ruling candidates** if lineage research is
declined — recorded so, and no further.

`SR-10` (starvation movement progression) is **pre-existing**, owned by `CHAR-005`, and is
neither reopened nor extended by this cluster.

---

## 11. Relationship to landed clusters

| Cluster | What `CLUSTER-004` takes from it |
|---|---|
| `CLUSTER-001` — Dungeon Exploration Time | The 10-minute turn `EXP-006`'s burn durations are stated in; the Game Turn Checklist whose step 1 supplied the `Dim light` default |
| `CLUSTER-002` — Character Foundation | Nothing directly |
| `CLUSTER-003` — Equipped Dungeon Movement | `CHAR-004`'s catalogued torch/lantern/oil/tinderbox/rations rows; `CHAR-005`'s running and encounter speeds, its §7 condition multipliers (incl. `SR-10`) and its §9 exhaustion contract; `EXP-003`'s scale boundary |

---

## 12. What changed in this record

| §| Pass 1 said | Now |
|---|---|---|
| 3 | `STAGE A COMPLETE -- READY FOR HUMAN EVIDENCE REVIEW` | Pass 1 **FAILED** review; pass 2 remediated, second review recorded |
| 4.1 | `EXP-006`: 4 item descriptions, **no** governing table, Ch. 4 only | 3 tables + 2 checklists + 6 descriptions, **four chapters** |
| 4.1 | *"`EXP-006` turned out smaller than its title"* | **Withdrawn** |
| 4.3 | — | **New:** the two cards are linked through p. 93 by the source |
| 4.4 | "four unresearched cards" | **Five**, with a six-step provider table and RC pages |
| 5 | 7 interactions | 12, four of them new |
| 6 | 13 questions | 14, with 5 pass-1 questions **closed** (§6.1) |

**Not changed:** the boundary, the deferrals, `EXP-004`/`EXP-010`'s dispositions, the
`EXP-008`/`MON-001`/`TREAS-001` knot, and every guardrail in §9.

---

## 13. Next step

> **Superseded 2026-10-03** (`MED-3`). This section asked for the human evidence review that was
> subsequently **given** on 2026-09-29, and anticipated a cluster split that the human owner then
> **chose**. Its prediction held: `ENC-005` was blocked by §6 Q1/Q2 and `EXP-006` was not. The
> original text is preserved below for provenance; the live next step follows it.

```text
SUPERSEDED -- recorded as written on 2026-09-29:

HUMAN EVIDENCE REVIEW -- a hard gate under DEC-0009 §6.

Stage B may not begin without explicit human authorization, and §6 Q1 and Q2
should be settled as part of that authorization: they determine whether ENC-005
can be synthesized at all in this cluster, or whether it should join its five
unresearched counterparties in a later encounter cluster.

EXP-006 carries no such blocker. Its open questions are genuine RC silences and
one ownership question (rations), none of which prevents Stage B from beginning
on that card alone if the human owner prefers to split the cluster.
```

**Live next step.** This block is **status**, not history, and the review phase it carries is
pinned by `test_live_records_carry_the_current_phase_token` so it cannot silently go stale
again — which it did, twice, and which review #3 recorded as `MED-1`. *(Citation corrected
2026-10-03 under review-#5 `BLOCKING-3`. It previously named a test that the review-#4 remediation
had renamed, so the citation resolved to nothing — one citation, zero definitions. The superseded
identifier is deliberately not reproduced here. The protection itself was never absent, and a
guard now fails if any live record cites a test that does not exist.)*

```text
EXP-006-PHASE: REVIEW-5-REMEDIATED

EXP-006   EVERY independent final implementation review performed so far
          RETURNED FAIL, and every artifact is preserved unaltered.  The
          review history is the persisted artifact set itself:
              docs/technical/EXP-006_FINAL_IMPLEMENTATION_REVIEW*.md
          each paired with its own remediation ledger.  It is NOT restated
          as a count here -- every prose count of it has so far gone stale
          (review-#4 B-4).

          NONE found a rules-conformance defect.  Review #4 additionally
          found NO guard claiming more than its mechanism establishes.
          Review #4's remediation is the most recent work.  A further
          independent review is NOT YET AUTHORIZED, and the implementer may
          not certify its own remediation.

          Review-#3's two protected-card findings are RESOLVED, adjudicated
          and applied at a150837 as documentation-only historical
          clarifications: LOW-3 (CHAR-005's two SR-11 denials) and LOW-8
          (the EXP-006 card's pre-approval statement). No mechanic,
          provenance, case ID or approval status changed.  Corrected
          2026-10-03 under review-#4 finding B-3.

ENC-005   STAGE B REMAINS DEFERRED. §6 Q1 and Q2 are still unsettled and are
          still the deciding questions. Not authorized.

CLUSTER-004 CROSS-CARD INTEGRATION AND CLUSTER COMPLETION: NOT AUTHORIZED,
          and not reachable while ENC-005 has no card.
```
