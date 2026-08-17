# Rule Card: Dungeon Wandering-Monster Check

> **Revalidation note (2026-08-16, Stage B).** This card has been revalidated against the Rules Cyclopedia under the Evidence-First Rule Research Protocol (`docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md`, `DEC-0009-evidence-first-rule-research-protocol.md`). Stage A produced `docs/rules/evidence/EXP-001-evidence.md`, human-accepted 2026-08-16; this Stage-B synthesis builds on that accepted evidence without redoing the primary-source search, per the protocol's RC-first/legacy-card-later ordering. The current, active specification is everything from "Rules Cyclopedia Source" below down to "Approval." It replaces the superseded 1974-primary specification as this card's authoritative content going forward, subject to human approval (see "Status" — submitted `AWAITING_APPROVAL`, not self-approved; one narrow Simulator Ruling remains explicitly pending human sign-off). The complete 1974-primary research, specification, and approval record is preserved unchanged, for provenance, under "Historical 1974-Primary Research and Specification" near the end of this document — it does not describe this card's current content.

---

## Rule ID

EXP-001

## Title

Dungeon (Underworld) Wandering-Monster Check

## Status

AWAITING_APPROVAL

## Rules Domain

exploration

---

## Rules Cyclopedia Source

*Dungeons & Dragons Rules Cyclopedia* (Allston, Aaron, ed. TSR, 1991), **Chapter 7: Encounters and Evasion**:

- **p. 91** — "Exploration and the Game Turn," the Game Turn Checklist (steps 1 and 4 govern this card).
- **p. 93** — "Wandering Monster Encounters" (the "Wandering Monsters" / "Wandering Monsters Check" prose subsection) and the Encounter Checklist (step 1, cited only to confirm round-mode suspension).

**Controlling evidence basis:** `docs/rules/evidence/EXP-001-evidence.md`, Stage-A evidence artifact, **human evidence review: ACCEPTED, 2026-08-16**. Every RC citation and quotation in this section is drawn from that accepted evidence, not re-derived; see the artifact itself for the full primary-source access method, whole-source cross-reference pass, and falsification passes. This card's own citations are carried forward from that artifact, consistent with `RULE_CARD_RESEARCH_PROTOCOL.md` §12: the evidence artifact is not a substitute for this card's own citations, and none of the RC or alternate-source citations below are asserted without a corresponding primary-text basis.

**Additional Stage-B primary-source consultation:** BECMI Basic Rules Boxed Set (Basic Player's Manual / Dungeon Master's Rulebook, TSR, 1991), full OCR transcription, `archive.org/stream/tsr01011bcorerulesddbasicrulesboxedset/…djvu.txt` — consulted only for the gap-directed questions in "Alternate-Source Completion Research" below, per `RULE_CARD_RESEARCH_PROTOCOL.md` §15 (gap-directed only, not a general browse).

## Rules Cyclopedia Explicitly Establishes

Carried forward from the accepted Stage-A evidence (`docs/rules/evidence/EXP-001-evidence.md` §4–§5), restated here as this card's own citations:

1. **Ordinary cadence.** Under ordinary turn-mode exploration, the wandering-monster check is step 4 of the Game Turn Checklist and occurs every two game turns — "The DM rolls 1d6 every other turn to check for this" (checklist step 4); "Every two turns (not every turn), the DM rolls 1d6..." ("Wandering Monster Encounters" subsection). RC does not independently establish whether encounter-credited turns participate in that same cadence (see "Rules Cyclopedia Leaves Undefined," item 1).
2. **Die and trigger (dungeon).** 1d6; a result of "1" is positive in a dungeon. Wilderness and other environments use a different trigger (terrain-dependent range), not this card's concern.
3. **Trigger and arrival are distinct procedural instants, one turn boundary apart, with no additional intervening turn.** A positive check at the end of turn *N* schedules arrival at the beginning of turn *N*+1 — not the same instant, and not separated by a full additional turn either. Checklist step 4: a positive roll means monsters "will encounter... at the beginning of the next turn." Checklist step 1 (the following iteration): "If the wandering monsters check at the end of the previous turn was positive, the monsters arrive now." Subsection: "they appear the following turn."
4. **Arrival preempts that turn's ordinary checklist flow.** Checklist step 1, on a pending positive check, directs: "Leave the Game Turn Checklist sequence and go to the Encounter Checklist, below." The arrival turn does not also perform its own step-4 check — it exits the checklist before reaching step 4 (see "Approved Mechanical Specification").
5. **No check executes during round-mode.** The Encounter Checklist's own step 1 states "Game time switches from 10-minute turns to 10-second rounds" — the Game Turn Checklist (the check's only home) is not running during that time.
6. **DM discretion to skip.** "If the Dungeon Master has already decided to have a prearranged encounter during this two-turn time period or if he has decided that the characters will have no encounter during this period, he can skip the wandering monster roll."
7. **Heightened checking, both dimensions, are RC Explicit — see the corrected-reading note below.** "Loud noises, battles, cursed items, or exploring special areas may allow the DM to check for wandering monsters every turn — and possibly with higher chances (1-2, 1-3, or 1-4 on 1d6)."
8. **Dungeon depth does not modify the check.** No RC text ties dungeon level to this check's frequency or trigger threshold (dungeon level instead modifies Number Appearing, `MON-002`'s territory, once a monster is already determined).
9. **Responsibility boundary.** Monster identity (`MON-001`), Number Appearing (`MON-002`), encounter distance (`ENC-001`), surprise (`ENC-002`), reaction (`ENC-003`), and subsequent encounter resolution are separate responsibilities this card does not perform.

**Corrected reading, established during Stage B (item 7 above).** The accepted Stage-A evidence located the clause "may allow the DM to check for wandering monsters every turn — and possibly with higher chances" directly, but recorded the numeric fragment "(1-2, 1-3, or 1-4 on 1d6)" appearing elsewhere on the same RC page as an unexplained, possibly-misplaced OCR artifact (Stage-A evidence §9, unresolved item 2) — a plausible reading given the source's OCR is known (from this same project's `EXP-002` research) to fragment sentences across page/column breaks. Stage-B's gap-directed BECMI research (below) located the intact, unfragmented parallel sentence in BECMI's own text: "...may result in a roll to check for Wandering Monsters every turn, and possibly with higher chances (1-2, 1-3, or 1-4 on 1d6)." Because RC's own numeric fragment is directly-quoted primary text already in hand (not an inference from BECMI), and BECMI's intact sentence structure confirms which RC clause that fragment completes, this card treats RC's clause as **RC Explicit once correctly reconstructed**, not as an Alternate-Source Compatible Completion — BECMI is cited as corroboration for the reconstruction, not as the source of the numbers themselves. See "Alternate-Source Completion Research" for the full BECMI passage and reasoning.

## Rules Cyclopedia Leaves Undefined / Ambiguous

1. **Whether an encounter-credited turn (per `EXP-002`'s approved `max(1, ceiling(encounter_rounds / 60))` whole-turn-credit model) participates in the every-two-turn cadence the same way an ordinary Game-Turn-Checklist iteration does.** This is the one question the accepted Stage-A evidence could not resolve from RC text alone after a real, documented search effort (Stage-A evidence §7, §9 item 1). Confirmed, on Stage-B necessity review, to require an executable answer — `EXP-002` deliberately exposes distinguishable ordinary-vs-encounter-credits specifically so a cadence-sensitive consumer could use that information, but does not itself decide how. See "Alternate-Source Completion Research" and "Simulator Ruling" below.
2. **What upstream condition/policy determines when "loud noises, battles, cursed items, or exploring special areas" apply, and which of the three heightened-chance levels (1-2, 1-3, or 1-4) a DM would choose.** RC leaves this to referee judgment; not resolved by this card (see "Open Questions").
3. **Duration of heightened checking** — how long an elevated frequency/chance condition persists once triggered. Not resolved by this card; tested for necessity and found to belong elsewhere (see "Open Questions").

## Alternate-Source Completion Research

Per `RULE_CARD_RESEARCH_PROTOCOL.md` §15 (gap-directed only) and `SOURCE_HIERARCHY.md` §3, researched only after each of the four Stage-A-preserved questions was individually tested for necessity (see "Approved Mechanical Specification" for the necessity-test results). Only Gap A required alternate-source research; Gap B turned out not to be a genuine gap at all (see the corrected reading above); Gaps C and D were determined to belong to other responsibilities without needing alternate-source research.

**BECMI Basic Rules Boxed Set** (highest-priority source per `SOURCE_HIERARCHY.md` §3 item 3), full text directly retrieved and searched:

> "During the adventure, the DM keeps track of the passage of time. To find out if Wandering Monsters appear, the DM rolls 1d6 after every two turns. If the result is a 1, one or more Wandering Monsters are approaching the party... The creature will arrive shortly (1-4 minutes) after the roll indicates Wandering Monsters. **They might arrive while another encounter is in progress!**"
>
> "Some actions or items may increase the chances of Wandering Monsters. Loud noises, battles, cursed items, or exploring special areas may result in a roll to check for Wandering Monsters every turn, and possibly with higher chances (1-2, 1-3, or 1-4 on 1d6)."

**For Gap A** (encounter-credited-turn cadence participation): BECMI's own text explicitly contemplates a triggered wandering-monster arrival occurring "while another encounter is in progress" — direct evidence that BECMI's model does not treat an encounter as freezing *all* other dungeon-time bookkeeping; concurrent/overlapping timers are expected and normal. This is genuinely relevant, directly-quoted primary-text evidence bearing on the gap. **It is not, however, a full, unambiguous resolution of the specific clause**: it establishes that a *different, already-triggered* arrival timer can run alongside an active encounter, not explicitly that the every-two-turn *check-cadence counter itself* increments through an encounter's own credited turns once ordinary play resumes. Classified below as corroborating context supporting, but not conclusively establishing, the "uniform counting" reading — insufficient on its own to classify as a full Compatible Completion; see "Simulator Ruling."

**For the corrected Gap B reading**: see "Rules Cyclopedia Explicitly Establishes," item 7 and its note above — BECMI's intact sentence is cited as corroboration for reconstructing RC's own fragmented text, not as an independent completion source.

No B/X, Holmes, or 1974 OD&D research was performed for either question — per `SOURCE_HIERARCHY.md` §3, BECMI is consulted first, and for Gap A, BECMI's evidence was found genuinely relevant but insufficient to close the gap outright, at which point the correct next step (per `RULE_CARD_RESEARCH_PROTOCOL.md` §16) is a narrowly scoped, non-bundled Simulator Ruling — not continued lineage-walking merely because BECMI's answer was incomplete rather than absent. No AD&D material was consulted.

## Compatibility Analysis

| Source | Addresses | Judgment |
|---|---|---|
| BECMI — 1d6, every-two-turns baseline, trigger on 1 | Cadence, die, trigger (dungeon) | **Preserved.** BECMI matches RC exactly; corroboration only, imports nothing new. |
| BECMI — "possibly with higher chances (1-2, 1-3, or 1-4 on 1d6)" | Corrected reading of RC's own fragmented text (item 7 above) | **Preserved / corroborating for reconstruction.** Not classified as Compatible Completion — the numbers are RC's own directly-quoted text, not imported from BECMI. |
| BECMI — arrival "might arrive while another encounter is in progress" | Gap A (encounter-credited-turn cadence) | **Insufficient for a full Compatible Completion.** Relevant, corroborating, directly-quoted evidence for the "time keeps flowing, encounters don't freeze all other bookkeeping" principle, but does not explicitly state that the every-two-turn cadence counter itself advances through encounter-credited turns. Cited as supporting rationale for the Simulator Ruling below, not adopted as a standalone completion. |

---

## Simulator Ruling

**Proposed — not yet human-approved.** Per `RULE_CARD_RESEARCH_PROTOCOL.md` §16, this card remains `AWAITING_APPROVAL` rather than self-approving this ruling.

**Exact missing behavior:** whether a whole-turn credit produced by a resolved encounter (per `EXP-002`'s approved contract) counts toward `EXP-001`'s every-two-turn wandering-check cadence the same way an ordinary Game-Turn-Checklist iteration's credit does.

**Why executable simulation requires an answer:** the campaign loop cannot determine when the next wandering-monster check is due after any encounter without deciding this — every real campaign will contain encounters, so leaving this undecided is not a rare edge case but a routine, load-bearing gap.

**Why RC does not answer it:** confirmed by the accepted Stage-A evidence's documented search (`docs/rules/evidence/EXP-001-evidence.md` §7) across both the dungeon-scale "Encounter Ends: begin play with a new turn" step and the structurally analogous wilderness-scale "Resume Travel" step; neither addresses counter continuity, and Stage B did not uncover a contradiction requiring that search to be redone.

**Why BECMI (the highest-priority compatible source) does not fully answer it:** BECMI's text confirms encounters do not freeze all dungeon-time bookkeeping (a different, already-triggered arrival timer can run concurrently with an active encounter) but does not explicitly state that the every-two-turn check-cadence counter specifically advances through an encounter's own credited turns.

**Smallest proposed ruling:**

> `EXP-001` consumes every whole-turn credit `EXP-002` produces — ordinary or encounter-derived alike — uniformly and in the order `EXP-002` supplies them, without distinguishing a credit's origin for cadence purposes. Each credit consumed advances `EXP-001`'s own internal "turns since last check" counter by exactly one; the check fires when that counter reaches two, then resets to zero.

This is the smallest ruling available: it adds no new concept, does not special-case encounter-derived credits at all, and requires no additional external input beyond what `EXP-002` already supplies (a distinguishable, ordered sequence of whole-turn credits). It is directly motivated by, but not compelled by, the BECMI evidence above (which supports "dungeon time keeps flowing through an encounter" as a design principle) and by the general project preference for the least invented behavior available. It does not contradict anything RC explicitly states.

---

## Human-Approved Variant

Not applicable.

---

## Approved Mechanical Specification

**Scope.** This procedure determines only *whether* a wandering-monster encounter check is due, performs it, and — on a positive result — schedules and signals the resulting arrival at the correct later moment. It does not determine which monster, Number Appearing, direction, distance, surprise, reaction, morale, pursuit/evasion, combat, or treasure.

**Necessity-test results for the four Stage-A-preserved questions**, per `RULE_CARD_RESEARCH_PROTOCOL.md` §15's gap-directed discipline:

| Gap | RC establishes | RC does not establish | Does `EXP-001` require an executable answer? | Why |
|---|---|---|---|---|
| A — encounter-credited-turn cadence | The check is a Game-Turn-Checklist step; it does not run during round-mode | Whether an encounter-credited turn counts toward the two-turn cadence | **YES** | Every campaign loop with an encounter needs this answer to know when the next check is due. See "Simulator Ruling." |
| B — "possibly with higher chances" magnitude | Once correctly reconstructed (see above): the heightened range is 1-2, 1-3, or 1-4 on 1d6, DM's choice among the three | Which of the three levels applies to which condition | **N/A — not a gap.** RC Explicit once correctly read; no completion needed for the magnitude itself. Which level a given situation warrants remains DM/upstream-policy discretion (see "Open Questions"). | — |
| C — duration of heightened checking | That certain conditions may trigger heightened checking | How long it persists | **NO — belongs elsewhere.** The condition that triggers heightened checking (a battle, a loud noise, a cursed item, a special area) is itself owned by another system (combat domain, a future noise/trap mechanism, item effects, dungeon-stocking/layout). That owning system is the natural place to assert *and revoke* a heightened-checking flag; `EXP-001` does not need its own duration rule and inventing one would exceed this card's evidenced scope. | — |
| D — multi-turn non-encounter activities | The checklist is iteration-based: one iteration, one possible check | How many check opportunities a bulk multi-turn activity generates | **NO — belongs elsewhere.** If a future activity-owning card (e.g., a search or rest procedure) expresses a multi-turn activity as a sequence of ordinary Game-Turn-Checklist iterations — which `EXP-002`'s own approved contract already supports one credit at a time — the ordinary per-iteration cadence model already covers it without any special rule from this card. | — |

**Dependencies:**

```text
RNG abstraction (RNG_CONTRACT.md) — the check's own 1d6 roll
EXP-002 (APPROVED)                — the exclusive source of whole-turn credits this
                                     card consumes: an absolute turn number per credit,
                                     ordinary-vs-encounter-derived origin distinguishable,
                                     strictly ordered, never produced during round-mode
```

`EXP-001` does not depend on `EXP-002`'s internal accounting mechanics (how `EXP-002` computed a credit) — only on the credit sequence itself. No incompatibility was found between `EXP-002`'s approved contract and this card's needs; **no `UPSTREAM CONTRACT REVIEW REQUIRED` flag is raised.**

**State this card maintains:**

```text
turns_since_last_check : integer, starts at 0
pending_arrival         : boolean, starts at false
heightened_checking     : externally supplied, defaults to false (see below)
heightened_chance_level : externally supplied when heightened_checking is true;
                          one of {1-in-6, 2-in-6, 3-in-6, 4-in-6}; not decided by
                          this card (see "Open Questions")
```

**Procedure — invoked once per whole-turn credit `EXP-002` produces, in the order produced:**

```text
WHEN EXP-001 receives a whole-turn credit (ordinary or encounter-derived — no
     distinction is made; see Simulator Ruling):

    IF pending_arrival is true:
        pending_arrival := false
        EMIT "wandering monster encounter begins" (arrival)
        (this turn's check — see below — is skipped entirely; the checklist
         is left before reaching it, per Rules Cyclopedia Explicit item 4)
        RETURN

    turns_since_last_check := turns_since_last_check + 1

    check_due := heightened_checking
                 OR (turns_since_last_check >= 2)
                 OR <an externally supplied "check has already been decided
                     for this period" signal is absent — see DM-discretion
                     note below>

    IF check_due AND NOT <externally supplied "DM has pre-decided this period,
                           skip the roll" signal>:

        turns_since_last_check := 0

        ROLL 1d6
            (via the approved RNG abstraction — exactly one `roll_die(6)` or
            `roll("1d6")` call; no re-rolls, no additional draws, regardless
            of outcome)

        trigger_threshold := heightened_chance_level IF heightened_checking
                              ELSE 1-in-6 (i.e., trigger only on a result of 1)

        IF the result falls within trigger_threshold:
            pending_arrival := true
            EMIT "wandering monster check: triggered, arrival pending"
        ELSE:
            EMIT "wandering monster check: no trigger"

    ELSE:
        EMIT "wandering monster check: not due this turn" (no roll performed)
```

**DM-discretion skip input.** Per Rules Cyclopedia Explicit item 6, this card accepts an externally supplied signal meaning "an encounter, or its absence, has already been decided for the current two-turn period" — when present, the roll is skipped entirely for that period (no RNG operation occurs). This card does not decide *when* that signal is asserted; it only honors it when supplied, exactly as `EXP-002` honors externally supplied activity information without deciding its source.

**Heightened-checking input.** Per Rules Cyclopedia Explicit item 7 (corrected reading), this card accepts two independent externally supplied inputs when active: (a) a frequency flag (`heightened_checking`), causing a check every credited turn instead of every two; and (b) a chance level among {1-in-6, 2-in-6 (1-2), 3-in-6 (1-3), 4-in-6 (1-4)}. **This card does not decide which upstream condition sets these inputs, or which level applies** — that determination belongs to whichever system asserts "a loud noise/battle/cursed item/special area condition exists" (see "Open Questions"). Absent an explicit input, both default to the ordinary baseline (every two turns, 1-in-6).

**Output.** One of: no-check-due (no RNG operation), a non-triggering check result, a triggering check result (`pending_arrival` set, no encounter begins yet), or an arrival (an encounter begins now, consuming no RNG operation of its own — the arrival is the deferred consequence of an earlier triggering roll, not a new roll). None of these outputs carries a monster identity, direction, distance, surprise, or reaction result — a future encounter-resolution consumer (`MON-001` onward) receives only the fact that an encounter has begun.

**No RNG owned beyond the check's own single roll.** Arrival itself consumes no additional RNG operation.

**Survivability out of scope.** This card specifies the canonical historical procedure only. It must not accept a survivability policy, and no survivability policy may alter the trigger threshold, cadence, or arrival timing, without a separately approved Rule Card or policy decision (`ARCHITECTURE.md` §10).

---

## Deterministic Test Cases

All cases use a controlled RNG (`ScriptedRNG` or equivalent) supplying a queued die value — never probabilistic sampling as the acceptance mechanism.

**Baseline 1d6 results (ordinary chance, check due):**

1. Scripted roll = 1 → triggered (`pending_arrival` set), one RNG operation.
2. Scripted roll = 2 → not triggered.
3. Scripted roll = 3 → not triggered.
4. Scripted roll = 4 → not triggered.
5. Scripted roll = 5 → not triggered.
6. Scripted roll = 6 → not triggered.

**Cadence across ordinary turns:**

7. First ordinary credit received → `turns_since_last_check` becomes 1, no check performed, no RNG operation.
8. Second ordinary credit received → check performed (per case 1–6 behavior), `turns_since_last_check` resets to 0.
9. Repeating the two-turn cycle across many credits produces exactly one check per two credits, with no drift.

**Trigger scheduling vs. immediate arrival:**

10. A triggering check (case 1) does not itself emit an arrival — only "triggered, arrival pending."
11. The *next* credit consumed after a triggering check emits arrival, and that same credit performs no check of its own (the checklist is left before reaching the check step).
12. Absent a triggering check, no arrival is ever emitted.

**Pre-decided skip:**

13. When the externally supplied "already decided for this period" signal is present on a turn where a check would otherwise be due, no roll occurs and no RNG operation is consumed.

**Heightened checking:**

14. With `heightened_checking` active, a check is performed every credited turn (not every two), using whichever externally supplied chance level is active.
15. With chance level 2-in-6 (1-2), a scripted roll of 2 triggers; a roll of 3 does not.
16. With chance level 3-in-6 (1-3), a scripted roll of 3 triggers; a roll of 4 does not.
17. With chance level 4-in-6 (1-4), a scripted roll of 4 triggers; a roll of 5 does not.
18. Absent an explicit heightened-checking input, behavior defaults to ordinary cadence and 1-in-6 — heightened checking is never silently assumed.

**`EXP-002` interface — encounter-derived credits (per the proposed Simulator Ruling):**

19. An encounter-derived credit (single-credit case, e.g., a ≤60-round encounter) advances `turns_since_last_check` identically to an ordinary credit.
20. Multiple encounter-derived credits from one long encounter (e.g., a 121-round encounter's three credits) are each consumed one at a time, in `EXP-002`'s supplied order, each independently advancing the counter — never collapsed into a single increment regardless of credit count.
21. A mixed sequence of ordinary and encounter-derived credits produces the same two-turn cadence pattern as an all-ordinary sequence of equal length, with no special-casing by origin.

**Round-mode non-execution (falls out of `EXP-002`'s own contract, tested here for `EXP-001`'s own behavior):**

22. No check, arrival, or RNG operation occurs while `EXP-002` reports no credit produced (i.e., during round-mode) — this card is simply not invoked during that interval, per `EXP-002`'s approved contract.

**RNG audit:**

23. Exactly one RNG operation per performed check, never zero-when-due and never more than one regardless of outcome.
24. Arrival consumes zero RNG operations.
25. Determinism: the same seed and call sequence via the seeded production RNG reproduce the same sequence of check/trigger/arrival outcomes.

## Provenance Classification

**Rules Cyclopedia Explicit**
- Ordinary cadence: every two turns (Game Turn Checklist step 4; "Wandering Monster Encounters" subsection).
- 1d6, trigger on 1 in a dungeon.
- Trigger and arrival are distinct instants, one turn boundary apart, no additional intervening turn.
- Arrival preempts that turn's own check step.
- No check during round-mode.
- DM discretion to skip when pre-decided.
- Heightened checking: frequency (every turn) and chance-level magnitude (1-2, 1-3, or 1-4 on 1d6), once RC's own fragmented text is correctly reconstructed (corroborated by BECMI's intact parallel sentence).
- Dungeon depth does not modify this check.
- Responsibility boundary (monster identity, Number Appearing, distance, surprise, reaction are separate).

**Necessary Mathematical / Mechanical Consequence**
- None load-bearing beyond the direct facts above.

**Alternate-Source Compatible Completion**
- Not applicable — no clause was ultimately completed *from* BECMI as an independent source; BECMI served only as corroboration for reconstructing RC's own fragmented text (Gap B) and as supporting rationale for the proposed Simulator Ruling (Gap A), neither of which is classified as a Compatible Completion in its own right.

**Simulator Ruling — proposed, narrow, awaiting human approval**
- Encounter-derived whole-turn credits are consumed uniformly with ordinary credits for cadence purposes (no origin-based distinction). See "Simulator Ruling" above for full rationale.

**Out of scope for this card**
- Which upstream condition/policy asserts heightened checking, and which of the three chance levels applies (Open Questions).
- Duration of heightened checking (belongs to the owning trigger condition).
- Multi-turn non-encounter activity expression (belongs to the activity-owning card).
- Monster identity (`MON-001`), Number Appearing (`MON-002`), encounter distance (`ENC-001`), surprise (`ENC-002`), reaction (`ENC-003`).
- `EXP-002`'s own turn-credit accounting mechanics (not reopened here).
- The `MON-001` ↔ `EXP-008` circularity (not resolved here).

---

## Open Questions

**`BLOCKS APPROVAL`**

1. Whether to approve the proposed Simulator Ruling (encounter-derived credits count toward cadence uniformly with ordinary credits) — required before this card can move past `AWAITING_APPROVAL`.

**`DOES NOT BLOCK EXP-001 APPROVAL`**

2. Which upstream condition/policy determines when heightened checking applies and which of the three chance levels (1-2, 1-3, 1-4) is appropriate. RC leaves this to DM judgment; this project's automated-simulator context may eventually need its own policy for this, but the *absence* of that policy does not prevent this card's own procedure from being correct — heightened checking simply never activates until a future system supplies the input. Not a blocker.
3. Duration of heightened checking once triggered — belongs to whichever future system asserts the triggering condition (`BELONGS TO ANOTHER RULE CARD`, effectively; not a fixed card yet).
4. Multi-turn non-encounter activity expression — belongs to a future activity-owning card (e.g., search/rest); this card's per-credit model already accommodates it once that card exists.

**`BELONGS TO ANOTHER RULE CARD`**

5. Monster identity — `MON-001`.
6. Number Appearing — `MON-002`.
7. Encounter distance — `ENC-001`.
8. Surprise — `ENC-002`.
9. Reaction — `ENC-003`.
10. The `MON-001` ↔ `EXP-008` circularity — not investigated or resolved here.

## Approval

- Approved by: *(pending — this card is `AWAITING_APPROVAL`, not approved by this task)*
- Date: *(pending)*
- Notes: Stage-A evidence accepted 2026-08-16; Stage-B synthesis complete. Only human approval of the one proposed Simulator Ruling (Open Questions, `BLOCKS APPROVAL` item 1) remains before this card can reach `APPROVED`.

---

## Historical 1974-Primary Research and Specification (preserved for provenance)

> **This section is historical and does not describe this card's current content.** Everything from here to "Status Lifecycle" is the complete 1974-primary-sourced research, specification, and human approval this card carried before the Rules Cyclopedia migration (`DEC-0007`), preserved verbatim (headers demoted one level to nest under this banner; content otherwise unchanged) for provenance — to show the reasoning that led to today's revalidated specification above, not as a statement of this card's current mechanics, dependencies, or status. In particular: **do not read anything below as saying the check happens "at the end of every turn," that a roll of 6 triggers an encounter, that arrival is immediate, or that the check is fully non-discretionary** — none of these survived this revalidation unchanged; see "Rules Cyclopedia Explicitly Establishes" and "Provenance Classification" above for what actually carries forward. This Stage-B revalidation was performed under the Evidence-First protocol: the current specification above was synthesized from the accepted Stage-A evidence *before* this historical section was consulted for comparison, per `RULE_CARD_RESEARCH_PROTOCOL.md` §13 (RC-first, legacy-card-later) — this section was not used to shape the research questions or the RC-native procedure above.

### Historical — 1974 Source

Gygax, Gary, and Dave Arneson. *Dungeons & Dragons, Volume 3: The Underworld & Wilderness Adventures.* Lake Geneva, WI: Tactical Studies Rules, 1974.

- Section **"UNDERWORLD MONSTERS"** (p. 9), paragraph **"Wandering Monsters"** (p. 10) — the operative procedure for this card.
- Section **"THE MOVE/TURN IN THE UNDERWORLD"** (p. 8) — defines the dungeon "turn" this procedure depends on (referenced, not specified, by this card — see "Dependencies" below).

**Verification method.** A digitized reproduction of the booklet was retrieved and its text extracted directly (not recalled from memory or taken from a secondary paraphrase). Page numbers were cross-checked two ways and agree: (a) the booklet's own printed page-footer sequence in the reproduction, and (b) the booklet's own table of contents, which lists "Underworld Monsters" beginning at page 9 and "Monster Determination and Level of Monster Matrix" (the table immediately following the Wandering Monsters paragraph) beginning at page 10. A secondary source (an independent OSR blog's page-by-page notes on this same booklet) was checked against the frequency finding below and agrees ("1 in 6 chance of wandering monster per turn, not every other turn") — noted here because "every other turn" is a common misattribution (it is Basic/Expert D&D's convention, not OD&D's), and this card explicitly does not import that later convention. No AD&D material was consulted.

**Exact source text (Wandering Monsters, p. 10):**

> "Wandering Monsters: At the end of every turn the referee will roll a six-sided die to see if a 'wandering monster' has been encountered. A roll of 6 indicates a wandering monster has appeared. The direction of appearance is determined by random number generation considering the number of possible entries. Distance and surprise are decided in the usual manner. The kind of monster is determined on the table below. (For wilderness encounters an entirely different table will be used)."

**Exact source text (turn definition, p. 8):**

> "Movement (distances given in Vol. 1) is in segments of approximately ten minutes. Thus it takes ten minutes to move about two moves — 120 feet for a fully-armored character. Two moves constitute a turn..."

### Historical — 1974 Explicitly Establishes

1. **Frequency.** The check is made "at the end of every turn" — every dungeon turn, without exception stated in the text (not "every other turn"; that is a later B/X-era convention, not this source's).
2. **Procedure.** One six-sided die (1d6) is rolled by the referee.
3. **Trigger.** "A roll of 6 indicates a wandering monster has appeared." A result of 1–5 does not.
4. **Scope boundary, stated by the source itself.** This is the *underworld* procedure. The same booklet contains a textually and mechanically separate "Wilderness Wandering Monsters" procedure (checked once per *day*, using a terrain-dependent matrix rather than a flat 1-in-6 roll) — the source explicitly flags this distinction ("For wilderness encounters an entirely different table will be used"). This card covers the underworld version only; the wilderness version is a distinct future Rule Card.
5. **No stated depth/level modifier to the check itself.** The Wandering Monsters paragraph states a flat, unmodified 1-in-6 roll with no dependency on dungeon level. This is treated as 1974-explicit rather than an oversight: the same booklet's treasure-type table (p. 7) *does* explicitly vary by "Level Beneath Surface" when the authors intended depth-based variation — its absence here is a meaningful contrast, not silence to be filled in.
6. **No stated referee discretion over whether to perform the check.** The clause is unqualified ("the referee will roll"). Elsewhere in the same booklet, discretionary procedures are explicitly marked as such (e.g., p. 10: "At the referee's option, Elves may be allowed the chance to sense any secret door they pass..."). The absence of equivalent qualifying language here is treated as 1974-explicit: the check is a standing procedure, not optional flavor.
7. **A dungeon turn is approximately ten minutes of game time** (p. 8), and non-movement activity is already expressed in turn units, not left outside the turn system: resting requires "one turn every hour must be spent motionless" (p. 8); searching a ten-foot section of wall "will require a full turn," with other, shorter activities (e.g., ESP'ing) "adjudged by the referee" as consuming a lesser portion of a turn (p. 8); and combat is explicitly subdivided into turns — "There are ten rounds of combat per turn" (p. 8). These references establish that "turn" is a recurring, bounded unit of dungeon time that rest, search, and combat all consume or are denominated in — not that its complete accounting semantics are defined (see "Dependencies").

### Historical — 1974 Leaves Undefined

Narrowly, within this card's scope: the 1974 text already ties rest, search, and combat to turn units (see item 7 above) — it does not leave *that* undefined. What it does not specify is the precise accounting/integration semantics a computer simulation needs: how partial-turn activities (e.g., a quarter-turn ESP check) accumulate toward a whole elapsed turn, and exactly when, relative to that accounting, the check in this card fires. This card does not resolve that narrower question — it is a dungeon-turn/exploration-turn system integration question, not a wandering-monster-check question (see "Dependencies" in the Mechanical Specification, and Open Questions).

Nothing else within this card's narrow scope (frequency, die, trigger value, procedure isolation) is left undefined by the 1974 text.

---

### Historical — Completion Research

Not applicable — 1974 is fully explicit for this card's narrow scope (frequency, die, and trigger value). The one genuine open item (precise turn-accounting/integration semantics — see "1974 Leaves Undefined") is a dependency on a not-yet-authored dungeon-turn Rule Card, not an unresolved rules *question* this card needs a later source to complete. No non-AD&D D&D-lineage research was performed beyond the single corroborating cross-check noted under "1974 Source" (confirming, not completing, the 1974 finding). No AD&D material was consulted or considered.

### Historical — Compatibility Analysis

Not applicable — no later-source completion was sought or imported into this card's mechanical specification.

---

### Historical — Simulator Ruling

Not applicable.

---

### Historical — Approved Mechanical Specification

**Scope.** This procedure determines only *whether* a wandering-monster encounter is triggered during dungeon (underworld) exploration. It does not determine which monster, number appearing, direction, distance, surprise, reaction, morale, pursuit/evasion, combat, or treasure — those belong to separate Rule Cards, invoked only when this procedure's result is triggered.

**Dependency (not specified by this card).** This procedure requires a signal that a qualifying dungeon-turn interval has elapsed, supplied by a future dungeon-turn/exploration-turn system:

```text
A qualifying dungeon-turn interval has elapsed
        ↓
Perform wandering-monster check
```

Movement, resting, searching, and combat are all already expressed in turn units by the 1974 text (see "1974 Explicitly Establishes," item 7); what this card does not define is the precise turn-accounting algorithm — how partial-turn activities accumulate toward a whole elapsed turn, and exactly when the check fires relative to that accounting — which is the responsibility of the dungeon-turn Rule Card referenced in "Open Questions." This card applies only while the party is within the underworld; the separate wilderness procedure (out of scope) uses a day-based turn unit instead.

**Procedure:**

```text
WHEN a qualifying dungeon-turn interval has elapsed

    ROLL 1d6
        (via the approved RNG abstraction — RNG_CONTRACT.md §4: a single
        `roll_die(6)` or `roll("1d6")` call. Exactly one such operation per
        check; no re-rolls, no additional draws, regardless of outcome.)

    IF the result is 6
        a wandering-monster encounter is triggered
    ELSE  (result is 1, 2, 3, 4, or 5)
        no wandering-monster encounter is triggered
```

**Output.** Exactly one of: an encounter-triggered outcome, or no encounter. The triggered outcome carries no data beyond the fact of triggering and the roll's own audit data (`RollResult`, per `RNG_CONTRACT.md` §5) — it must not itself carry a monster identity, direction, distance, surprise result, reaction result, or treasure. A future encounter-resolution Rule Card consumes the trigger fact as its input.

**Non-discretionary.** The check is performed unconditionally at the end of every qualifying turn. It is not skipped based on dungeon depth, party composition, prior results, or referee convenience — none of those exceptions are stated in the source (see "1974 Explicitly Establishes," items 5–6).

**Survivability out of scope.** This card specifies the canonical historical procedure only. Survivability is out of scope for it entirely: this procedure must not accept a survivability policy, and no survivability policy may alter this procedure's canonical 1-in-6 mechanic, without a separately approved Rule Card or policy decision specifically authorizing and defining that change (`ARCHITECTURE.md` §10). This card does not describe, authorize, or imply any mechanism by which survivability could do so.

---

### Historical — Deterministic Test Cases

All cases use a controlled RNG (`ScriptedRNG` or equivalent) supplying a specific queued die value — never probabilistic sampling as the acceptance mechanism (`RNG_CONTRACT.md` §9, `TESTING_STRATEGY.md` §3).

1. **Non-trigger, lowest value.** Scripted roll = 1 → no encounter triggered.
2. **Non-trigger, mid-range.** Scripted roll = 2 → no encounter triggered. Scripted roll = 3 → no encounter triggered. Scripted roll = 4 → no encounter triggered. (Included individually, not only as boundaries, so an off-by-one implementation — e.g., accidentally triggering on ≥5 — cannot pass by only testing the extremes.)
3. **Non-trigger, highest non-trigger value.** Scripted roll = 5 → no encounter triggered.
4. **Trigger, boundary value.** Scripted roll = 6 → encounter triggered.
5. **Exactly one RNG operation per check.** Using a scripted queue of length exactly 1, a single check invocation succeeds without exhausting or needing a second value — proving the procedure performs exactly one `roll_die(6)`/`roll("1d6")` call, never a hidden extra draw or a re-roll on any result.
6. **Procedure isolation.** On a triggered result, the produced outcome exposes only the trigger fact and the roll's own audit data — no monster, direction, distance, surprise, reaction, or treasure fields are present on it (there is no code path by which this procedure could populate them).
7. **Turn-dependency integration contract** (does not implement the turn system). Given a sequence of *N* "qualifying dungeon-turn elapsed" signals (simulated/stubbed, not the real turn system), the check procedure is invoked exactly *N* times, each consuming exactly one RNG operation — demonstrating the integration point is called once per elapsed turn, neither zero nor multiple times per signal. This is a contract test for whoever later implements the turn-system integration, not a test of turn semantics themselves.
8. **Determinism.** The same seed and call sequence via the seeded production RNG reproduce the same trigger/non-trigger outcome (`RNG_CONTRACT.md` §9's general reproducibility guarantee — this card introduces no exception to it).

### Historical — Provenance Classification

1974 Explicit.

---

### Historical — Open Questions

1. **Turn-accounting integration semantics.** Movement, rest, search, and combat are already turn-denominated per the 1974 text (see "1974 Explicitly Establishes," item 7); what a future dungeon-turn/exploration-turn Rule Card still needs to specify is the precise accounting algorithm — how partial-turn activities accumulate toward a whole elapsed turn, and exactly when, relative to that accounting, this card's "qualifying turn elapsed" signal fires. **This does not block approval of this card's own mechanical specification**, since the check procedure itself (roll, trigger, output) is fully specified independent of that answer.

---

### Historical — Approval

- Approved by: Human project owner
- Date: 2026-08-15
- Notes: Approved after historical and specification review; turn-accounting integration remains a dependency of a future dungeon-turn Rule Card and does not block this procedure.

---

## Status Lifecycle

```text
DRAFT             — being written; not yet researched to completion
      ↓
RESEARCHED        — research and compatibility analysis complete
      ↓
AWAITING_APPROVAL — submitted for human review
      ↓
APPROVED ────────────────────────────────┐   set only by a human project owner;
      ↓                                  │   authorizes implementation
IMPLEMENTED                              │
      ↓                                  │
VERIFIED — implementation's tests and    │
    required verification have passed    │
    (TESTING_STRATEGY.md §9–§10)         │
                                          │
      (from APPROVED, IMPLEMENTED, or VERIFIED,
       whenever the source hierarchy that governed
       this card's approval is superseded)
                                          ↓
                              REVALIDATION_REQUIRED
                                          ↓
                        research against the current source
                        hierarchy, human review (DEVELOPMENT_WORKFLOW.md §9.7)
                                          ↓
                              APPROVED again (loop closes)
```

Only a Rule Card explicitly set to `APPROVED` (or `IMPLEMENTED`/`VERIFIED` reached from an `APPROVED` state that has not since been superseded) by a human project owner may authorize rules implementation (`SOURCE_HIERARCHY.md` §9, `ARCHITECTURE.md` §12, `AGENTS.md` §2). An approved Rule Card does not, by itself, override the project-level Pre-Code Development Gate (`ARCHITECTURE.md` §16) or an active Rules Baseline Migration Gate (`ARCHITECTURE.md` §15.2).

`REVALIDATION_REQUIRED` is not a failure state and does not imply the card's research was wrong — see `DEVELOPMENT_WORKFLOW.md` §9.7 for its exact meaning and the revalidation workflow.
