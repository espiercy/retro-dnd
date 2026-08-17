# Rule Card: Dungeon Wandering-Monster Check

> **Revalidation note (2026-08-16, Stage B, corrected).** This card has been revalidated against the Rules Cyclopedia under the Evidence-First Rule Research Protocol (`docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md`, `DEC-0009-evidence-first-rule-research-protocol.md`). Stage A produced `docs/rules/evidence/EXP-001-evidence.md`, human-accepted 2026-08-16; this Stage-B synthesis builds on that accepted evidence without redoing the primary-source search, per the protocol's RC-first/legacy-card-later ordering. **This revision corrects the prior Stage-B draft**, per human review: Gap A's alternate-source research is now completed through the active source hierarchy rather than stopping short at an insufficient single source; the trigger-versus-arrival mechanical contract, baseline cadence logic, and pre-decided-skip bookkeeping are corrected; and software/API-shaped wording is removed in favor of mechanical requirements. The current, active specification is everything from "Rules Cyclopedia Source" below down to "Approval." It replaces the prior Stage-B draft's proposal entirely, subject to human approval (see "Status" — submitted `AWAITING_APPROVAL`, not self-approved). The complete 1974-primary research, specification, and approval record is preserved unchanged, for provenance, under "Historical 1974-Primary Research and Specification" near the end of this document — it does not describe this card's current content.

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

**Controlling evidence basis:** `docs/rules/evidence/EXP-001-evidence.md`, Stage-A evidence artifact, **human evidence review: ACCEPTED, 2026-08-16**. Every RC citation and quotation in this section is drawn from that accepted evidence, not re-derived. This card's own citations are carried forward from that artifact, consistent with `RULE_CARD_RESEARCH_PROTOCOL.md` §12: the evidence artifact is not a substitute for this card's own citations.

**Stage-B gap-directed alternate-source consultation, in source-hierarchy order (`SOURCE_HIERARCHY.md` §3):**

1. **BECMI Basic Rules Boxed Set** (Basic Player's Manual / Dungeon Master's Rulebook, TSR, 1991), full OCR transcription, `archive.org/stream/tsr01011bcorerulesddbasicrulesboxedset/…djvu.txt`.
2. **B/X — Moldvay Basic (1981)**, *Dungeons & Dragons Fantasy Adventure Game, Basic Rulebook* (TSR 1011, ed. Tom Moldvay), full page-image/OCR-searchable transcription, `anyflip.com/pejfp/myfa/basic` (pp. B1–B50 and B51–B68). Confirmed authentic 1981 Moldvay text via its own title page ("Edited by Tom Moldvay... Previous edition edited by J. Eric Holmes... © 1974,1977,1978,1981") and internal page-lettering (B1–B68) matching the known structure of this specific booklet — distinct from, and not to be confused with, the 1991 BECMI reprint consulted separately above, which restates closely related but not always identical text.
3. **1974 OD&D** (*Dungeons & Dragons, Volume 3: The Underworld & Wilderness Adventures*), already directly quoted and page-verified in this card's own preserved historical section below (no fresh fetch required — reused per `RULE_CARD_RESEARCH_PROTOCOL.md`'s general principle of not re-deriving already-established primary-text findings).

Cook Expert (1981) and Holmes Basic (1977) were not separately consulted for Gap A: B/X's Moldvay Basic volume already contains the complete underworld wandering-monster procedure at the level of detail needed, and — as detailed in "Alternate-Source Completion Research" below — the question was resolved from BECMI + B/X + 1974 OD&D's *convergent* treatment before reaching Holmes, consistent with `SOURCE_HIERARCHY.md` §8's instruction not to perform unnecessary genealogical research once a question is actually resolved. No AD&D material was consulted.

## Rules Cyclopedia Explicitly Establishes

Carried forward from the accepted Stage-A evidence (`docs/rules/evidence/EXP-001-evidence.md` §4–§5), restated here as this card's own citations:

1. **Ordinary cadence.** Under ordinary turn-mode exploration, the wandering-monster check is step 4 of the Game Turn Checklist and occurs every two game turns — "The DM rolls 1d6 every other turn to check for this" (checklist step 4); "Every two turns (not every turn), the DM rolls 1d6..." ("Wandering Monster Encounters" subsection).
2. **Die and trigger (dungeon).** 1d6; a result of "1" is positive in a dungeon. Wilderness and other environments use a different trigger (terrain-dependent range), not this card's concern.
3. **Trigger and arrival are distinct procedural instants, one turn boundary apart, with no additional intervening turn.** A positive check at the end of turn *N* schedules arrival at the beginning of turn *N*+1 — not the same instant, and not separated by a full additional turn either. Checklist step 4: a positive roll means monsters "will encounter... at the beginning of the next turn." Checklist step 1 (the following iteration): "If the wandering monsters check at the end of the previous turn was positive, the monsters arrive now." Subsection: "they appear the following turn."
4. **Arrival preempts that turn's ordinary checklist flow.** Checklist step 1, on a pending positive check, directs: "Leave the Game Turn Checklist sequence and go to the Encounter Checklist, below." The arrival turn does not also perform its own step-4 check — it exits the checklist before reaching step 4 (see "Approved Mechanical Specification").
5. **No check executes during round-mode.** The Encounter Checklist's own step 1 states "Game time switches from 10-minute turns to 10-second rounds" — the Game Turn Checklist (the check's only home) is not running during that time.
6. **DM discretion to skip.** "If the Dungeon Master has already decided to have a prearranged encounter during this two-turn time period or if he has decided that the characters will have no encounter during this period, he can skip the wandering monster roll." — the skip applies to the current, already-due two-turn period; it is not itself a trigger for an earlier or additional roll (see "Approved Mechanical Specification").
7. **Heightened checking, both dimensions, are RC Explicit — see the corrected-reading note below.** "Loud noises, battles, cursed items, or exploring special areas may allow the DM to check for wandering monsters every turn — and possibly with higher chances (1-2, 1-3, or 1-4 on 1d6)."
8. **Dungeon depth does not modify the check.** No RC text ties dungeon level to this check's frequency or trigger threshold (dungeon level instead modifies Number Appearing, `MON-002`'s territory, once a monster is already determined).
9. **Responsibility boundary.** Monster identity (`MON-001`), Number Appearing (`MON-002`), encounter distance (`ENC-001`), surprise (`ENC-002`), reaction (`ENC-003`), and subsequent encounter resolution are separate responsibilities this card does not perform.

**Corrected reading, established during Stage B (item 7 above).** The accepted Stage-A evidence located the clause "may allow the DM to check for wandering monsters every turn — and possibly with higher chances" directly, but recorded the numeric fragment "(1-2, 1-3, or 1-4 on 1d6)" appearing elsewhere on the same RC page as an unexplained, possibly-misplaced OCR artifact (Stage-A evidence §9, unresolved item 2). Stage-B's gap-directed BECMI and B/X research (below) located the intact, unfragmented parallel sentence in both sources' own text — B/X (Moldvay 1981): "...should appear more often if the party is making a lot of noise or light... The dungeon may have areas where the DM checks for Wandering Monsters every turn... certain areas where Wandering Monsters are encountered more often (such as on a roll of 1 or 2)"; BECMI: "...may result in a roll to check for Wandering Monsters every turn, and possibly with higher chances (1-2, 1-3, or 1-4 on 1d6)." Because RC's own numeric fragment is directly-quoted primary text already in hand (not an inference from an alternate source), and both BECMI's and B/X's intact sentence structures confirm which RC clause that fragment completes, this card treats RC's clause as **RC Explicit once correctly reconstructed**, not as an Alternate-Source Compatible Completion — BECMI and B/X are cited as corroboration for the reconstruction, not as the source of the numbers themselves.

## Rules Cyclopedia Leaves Undefined / Ambiguous

1. **Whether an encounter-credited turn (per `EXP-002`'s approved `max(1, ceiling(encounter_rounds / 60))` whole-turn-credit model) participates in the every-two-turn cadence the same way an ordinary Game-Turn-Checklist iteration does.** This is the one question the accepted Stage-A evidence could not resolve from RC text alone. Resolved for this card by gap-directed alternate-source research — see "Alternate-Source Completion Research" below; no longer an open RC gap requiring a Simulator Ruling.
2. **What upstream condition/policy determines when "loud noises, battles, cursed items, or exploring special areas" apply, and which of the three heightened-chance levels (1-2, 1-3, or 1-4) a DM would choose.** RC leaves this to referee judgment; not resolved by this card (see "Open Questions").
3. **Duration of heightened checking** — how long an elevated frequency/chance condition persists once triggered. Not resolved by this card; tested for necessity and found to belong elsewhere (see "Open Questions").

## Alternate-Source Completion Research

Per `RULE_CARD_RESEARCH_PROTOCOL.md` §15 (gap-directed only) and `SOURCE_HIERARCHY.md` §3/§5, researched only after each of the four Stage-A-preserved questions was individually tested for necessity (see "Approved Mechanical Specification" for the full necessity-test table). Only Gap A required alternate-source research; Gap B turned out not to be a genuine gap at all (see the corrected reading above); Gaps C and D were determined to belong to other responsibilities without needing alternate-source research.

**Gap A — the exact unresolved clause:** *Does wandering-monster check cadence continue, pause, reset, or otherwise behave specially when ordinary dungeon-turn play is interrupted by an encounter/combat that consumes one or more dungeon turns?*

**Step 1 — BECMI (highest priority, `SOURCE_HIERARCHY.md` §3 item 3).** Full text directly retrieved and searched:

> "During the adventure, the DM keeps track of the passage of time. To find out if Wandering Monsters appear, the DM rolls 1d6 after every two turns. If the result is a 1, one or more Wandering Monsters are approaching the party... The creature will arrive shortly (1-4 minutes) after the roll indicates Wandering Monsters. **They might arrive while another encounter is in progress!**"

*Finding:* directly-quoted primary text confirming BECMI's model does not treat an encounter as freezing all other dungeon-time bookkeeping — a separate, already-triggered arrival timer is explicitly expected to run concurrently with an unrelated active encounter. *Classification:* relevant, directly-quoted, but **does not by itself explicitly state** that the every-two-turn cadence counter specifically advances through an encounter's own credited turns. **Insufficient alone to resolve the clause** — research continued to the next source per `SOURCE_HIERARCHY.md` §3, rather than stopping at an incomplete answer.

**Step 2 — B/X, Moldvay Basic (1981)**, the next source in priority order. Full text directly retrieved and searched (authenticity confirmed — see "Rules Cyclopedia Source" above). Two directly relevant passages:

> **"Order of Events in One Game Turn"** (p. B23): "1. The DM rolls for wandering monsters (1d6; see page B53). 2. The party moves, enters room, listens, and searches. 3. If monsters are not encountered, the turn ends. If monsters are encountered, the DM rolls for the Number Appearing... [steps 4–7: distance, surprise, initiative, reaction, and — if combat begins — the Combat Sequence] ... 8. End of Turn. Where necessary, the DM should check the character's remaining hit points, whether or not they need rest..., their encumbrance..., their sources of light, the durations of any spells in progress, and the total time the party has spent in the dungeon."
>
> **"Wandering Monsters"** (p. B53): "At the end of every 2 turns, the DM should check for Wandering Monsters. To do so, roll 1d6: a result of 1 indicates that the party will encounter a Wandering Monster in the next turn... The dungeon may have areas where the DM checks for Wandering Monsters every turn... Wandering Monsters should appear more often if the party is making a lot of noise or light."

*Finding:* B/X's own text contains a genuine internal structural difference from RC's own model, not merely a restatement of it. B/X's "Order of Events in One Game Turn" places the wandering-monster roll at **step 1** (before the party's own actions) and folds any resulting encounter — including its combat, via the Combat Sequence — **into the same single numbered "Game Turn,"** with end-of-turn bookkeeping (step 8) occurring afterward, still within that one turn. B/X's structural model, as evidenced by this chart, does not appear to have a concept of an encounter generating *additional*, separately-counted turns at all — everything from the triggering roll through full combat resolution and its own bookkeeping is treated as occurring within one ordinary turn-numbered cycle, after which the *next* numbered turn's own "Order of Events" begins, continuing the same two-turn counting rhythm uninterrupted. (This is a different question from — and does not reopen — RC's own explicit "arrival at the beginning of the next turn" delayed-arrival finding, preserved unchanged above; B/X's step-1 placement concerns a different structural choice than RC's own step-4/step-1 split and is noted only for what it shows about encounter-turn accounting.) *Classification:* **Evolved/Different**, not Compatible Completion in its own right, relative to RC's specific "an encounter guarantees at least one full turn regardless of round count" model (`EXP-002`'s approved contract) — B/X does not share that specific mechanic. However, B/X's structural choice is directly relevant corroboration for the *narrower* Gap A question: it reinforces, via an independent and materially different implementation of the same underlying design problem, that this lineage's design philosophy does not carve encounter-time out as a specially-exempted or separately-tracked category for cadence-counting purposes — if anything, B/X goes further than RC by not separately counting encounter-consumed time as extra turns at all.

**Step 3 — 1974 OD&D**, already directly quoted and page-verified in this card's own preserved historical section (Vol. 3, p. 8; no fresh fetch required):

> "Melee is fast and furious. There are ten rounds of combat per turn."

*Finding:* 1974's own explicit ratio converts combat rounds directly and proportionally into the *same* undifferentiated dungeon-turn count that movement, rest, and search all feed into — with no separate "minimum one turn per encounter" concept and no special-casing of encounter time as a distinct accounting category. *Classification:* **Evolved/Different** relative to RC's own "at least one full turn regardless of round count" minimum (which 1974 does not share — this project's own prior `EXP-002` research already established this), but directly relevant corroboration for the same narrower point B/X's evidence supports.

**Convergent finding across all three sources consulted.** BECMI, B/X, and 1974 OD&D each treat the underworld wandering-monster procedure differently in various respects (this project has already documented several such differences elsewhere), but **none of the three** — independently, across three different stages of the lineage — introduces a concept of encounter-consumed time being specially exempted, paused, or reset for cadence-counting purposes relative to ordinary time. BECMI explicitly shows concurrent timers running through an encounter; B/X folds encounter time directly into the same turn-numbered cycle without separate accounting; 1974 OD&D converts combat rounds directly and proportionally into the same continuous turn count. This is a **Compatible Completion** under `SOURCE_HIERARCHY.md` §6: it supplies the executable detail RC itself does not state (whether an `EXP-002`-style encounter-credited turn counts toward `EXP-001`'s cadence), and it does not contradict anything RC explicitly establishes — RC's own explicit facts (the check is step 4 of turn-mode iterations; the check does not run during round-mode; an encounter guarantees at least one full turn) are all fully preserved by treating every whole-turn credit uniformly for cadence-counting purposes, regardless of whether `EXP-002` produced it from an ordinary iteration or from a resolved encounter.

## Compatibility Analysis

| Source | Addresses | Judgment |
|---|---|---|
| BECMI — 1d6, every-two-turns baseline, trigger on 1 | Cadence, die, trigger (dungeon) | **Preserved.** BECMI matches RC exactly; corroboration only, imports nothing new. |
| BECMI — "possibly with higher chances (1-2, 1-3, or 1-4 on 1d6)"; B/X — "on a roll of 1 or 2" / "every turn" | Corrected reading of RC's own fragmented text (item 7 above) | **Preserved / corroborating for reconstruction.** Not classified as Compatible Completion — the numbers are RC's own directly-quoted text, not imported from an alternate source. |
| BECMI — arrival "might arrive while another encounter is in progress" | Gap A (encounter-credited-turn cadence), step 1 of the lineage walk | **Preserved/corroborating, insufficient alone.** Relevant but did not, by itself, resolve the clause; research continued per `SOURCE_HIERARCHY.md` §3. |
| B/X (Moldvay 1981) — "Order of Events in One Game Turn" folds an entire encounter into one numbered turn, with no separate encounter-turn accounting | Gap A, step 2 | **Evolved/Different** relative to RC's own "at least one full turn" model — not adopted wholesale — but directly relevant corroboration for the narrower cadence-continuity question. |
| 1974 OD&D — "ten rounds of combat per turn," direct proportional conversion into the same turn count | Gap A, step 3 | **Evolved/Different** relative to RC's minimum-turn model — not adopted wholesale — but directly relevant corroboration for the same narrower point. |
| **Convergent finding: none of BECMI/B-X/1974-OD&D specially exempts encounter time from ordinary cadence-counting** | Gap A, resolved | **Compatible Completion.** Adopted — see "Alternate-Source Completion Research" and "Approved Mechanical Specification." Supersedes the prior Stage-B draft's Simulator Ruling proposal, which is withdrawn (see "Simulator Ruling" below). |

---

## Simulator Ruling

**Not applicable — withdrawn.** The prior Stage-B draft proposed a narrow Simulator Ruling for Gap A after finding BECMI evidence "relevant but insufficient." Per `RULE_CARD_RESEARCH_PROTOCOL.md` §16 and `SOURCE_HIERARCHY.md` §3, an insufficient single source requires continuing the lineage walk, not proceeding directly to a Simulator Ruling. That continuation (B/X, then 1974 OD&D — see "Alternate-Source Completion Research") produced a convergent, compatible completion; no Simulator Ruling is required for Gap A, and none remains proposed by this card.

---

## Human-Approved Variant

Not applicable.

---

## Approved Mechanical Specification

**Scope.** This procedure determines only *whether* a wandering-monster encounter check is due, performs it, and — at the correct later procedural moment — signals the resulting arrival. It does not determine which monster, Number Appearing, direction, distance, surprise, reaction, morale, pursuit/evasion, combat, or treasure. **This card does not prescribe a software event/API architecture** — the mechanical descriptions below state what the simulator must accurately expose and honor, not how it is implemented.

**Necessity-test results for the four Stage-A-preserved questions**, per `RULE_CARD_RESEARCH_PROTOCOL.md` §15's gap-directed discipline:

| Gap | RC establishes | RC does not establish | Does `EXP-001` require an executable answer? | Resolution |
|---|---|---|---|---|
| A — encounter-credited-turn cadence | The check is a Game-Turn-Checklist step; it does not run during round-mode | Whether an encounter-credited turn counts toward the two-turn cadence | **YES** | **Alternate-Source Compatible Completion** (BECMI + B/X + 1974 OD&D convergent finding) — see above. |
| B — "possibly with higher chances" magnitude | Once correctly reconstructed: the heightened range is 1-2, 1-3, or 1-4 on 1d6, DM's choice among the three | Which of the three levels applies to which condition | **N/A — not a gap.** RC Explicit once correctly read. | Which level a given situation warrants remains DM/upstream-policy discretion (see "Open Questions"). |
| C — duration of heightened checking | That certain conditions may trigger heightened checking | How long it persists | **NO — belongs elsewhere.** | The condition that triggers heightened checking (a battle, a loud noise, a cursed item, a special area) is owned by another system, which is the natural place to assert and revoke a heightened-checking flag. |
| D — multi-turn non-encounter activities | The checklist is iteration-based: one iteration, one possible check | How many check opportunities a bulk multi-turn activity generates | **NO — belongs elsewhere.** | `EXP-002`'s existing per-credit contract already accommodates this once a future activity-owning card expresses a multi-turn activity as ordinary iterations. |

**Dependencies:**

```text
An exact rules-visible 1d6 roll (RNG_CONTRACT.md) — the check's own roll
EXP-002 (APPROVED)                — the source of completed whole-turn credits:
                                     an absolute turn number per credit,
                                     ordinary-vs-encounter-derived origin
                                     distinguishable, strictly ordered, never
                                     produced during round-mode
A "new Game Turn is beginning" procedural moment — supplied by whatever governs
                                     Game-Turn-Checklist execution generally (not
                                     yet a designed system); a distinct
                                     mechanical input from a completed credit,
                                     needed only to sequence arrival correctly
                                     before that turn's own Actions/Results/check
                                     (see "Two procedural moments" below)
```

`EXP-001` does not depend on `EXP-002`'s internal accounting mechanics — only on the credit sequence itself. **`EXP-002`'s approved contract remains sufficient as the sole source of completed-credit information; it is not modified, and no `UPSTREAM CONTRACT REVIEW REQUIRED` flag is raised.** The additional "new Game Turn beginning" input identified below was never `EXP-002`'s responsibility to supply — `EXP-002` deals only in completed credits — and its absence from `EXP-002`'s contract is not an incompatibility, only a reminder that a future Game-Turn-Checklist orchestration concern (not yet designed) will need to supply it.

**Two procedural moments, corrected from the prior Stage-B draft.** RC's own checklist structure has the check (step 4) at the *end* of turn *N*, and arrival resolution (step 1) at the *beginning* of turn *N*+1 — these are two separate checklist invocations, not the same moment. This card accordingly defines two distinct mechanical inputs, not one:

```text
END OF TURN N:
    step 4 wandering check may occur (if due)
        ↓
BEGINNING OF TURN N+1:
    step 1 — if a check at the end of turn N was positive, wandering
             monsters arrive now, before this turn's own Actions/Results/
             check-4 proceed
```

A completed whole-turn credit (from `EXP-002`) is the correct input for the *first* moment — it tells `EXP-001` a turn has ended, letting it advance its cadence counter and, if due, perform the check. It is **not**, by itself, the correct input for the *second* moment — resolving a pending arrival requires knowing that a *new* turn is *beginning*, which is a distinct procedural fact from "the previous turn's credit was just completed." This card treats them as two separate mechanical inputs (below), leaving how the wider simulation sequences and exposes them to a future implementation-time design.

**State this card maintains:**

```text
turns_since_last_check : integer, starts at 0
pending_arrival         : boolean, starts at false
heightened_checking     : externally supplied, defaults to false (see below)
heightened_chance_level : externally supplied when heightened_checking is true;
                          one of {1-in-6, 2-in-6 (1-2), 3-in-6 (1-3), 4-in-6 (1-4)};
                          not decided by this card (see "Open Questions")
```

**Procedure A — invoked once per completed whole-turn credit `EXP-002` produces, in the order produced (this is the "end of turn *N*" moment):**

```text
WHEN a completed whole-turn credit is received (ordinary or encounter-derived
     — no distinction is made; see "Alternate-Source Completion Research"):

    turns_since_last_check := turns_since_last_check + 1

    check_due := heightened_checking OR (turns_since_last_check >= 2)

    IF check_due:
        turns_since_last_check := 0
            (the due two-turn period is considered complete regardless of
            whether the roll below is performed or skipped — see next)

        IF an externally supplied "already decided for this period" signal
           is present:
            the mechanical outcome is: check skipped for this period
            (no roll is performed; no RNG operation is consumed)
        ELSE:
            perform exactly one rules-visible 1d6 roll
            trigger_threshold := heightened_chance_level IF heightened_checking
                                  ELSE 1-in-6 (result of 1 only)
            IF the result falls within trigger_threshold:
                pending_arrival := true
                the mechanical outcome is: check triggered, arrival pending
            ELSE:
                the mechanical outcome is: check performed, no trigger
    ELSE:
        the mechanical outcome is: no check due this turn (no roll performed)
```

**Procedure B — invoked once at the beginning of each new Game Turn, before that turn's own Actions/Results/step-4 check occur (this is the "beginning of turn *N*+1" moment):**

```text
WHEN a new Game Turn begins, before its own Actions, Results, and
     wandering-monster check step:

    IF pending_arrival is true:
        pending_arrival := false
        the mechanical outcome is: wandering-monster encounter begins now
        (this Game Turn's own Actions/Results/check-4 do not occur — the
        Game Turn Checklist is left for the Encounter Checklist before
        reaching them, per Rules Cyclopedia Explicit item 4; no additional
        RNG operation is consumed by arrival itself)
    ELSE:
        no action; this Game Turn's own Actions/Results/check proceed
        normally under Procedure A once its own credit later completes
```

**DM-discretion skip input.** Per Rules Cyclopedia Explicit item 6, this card accepts an externally supplied signal meaning "an encounter, or its absence, has already been decided for the current two-turn period." When present at a due check, the roll is skipped for that period and `turns_since_last_check` still resets to zero — the skip consumes the due period; it does not cause an earlier or additional roll, and the next ordinary check is not due again until a fresh two-turn period completes. This card does not decide *when* that signal is asserted; it only honors it when supplied.

**Heightened-checking input.** Per Rules Cyclopedia Explicit item 7 (corrected reading), this card accepts two independent externally supplied inputs when active: (a) a frequency flag (`heightened_checking`), causing a check every credited turn instead of every two; and (b) a chance level among {1-in-6, 2-in-6, 3-in-6, 4-in-6}. **This card does not decide which upstream condition sets these inputs, or which level applies** — that determination belongs to whichever system asserts a loud-noise/battle/cursed-item/special-area condition (see "Open Questions"). Absent an explicit input, both default to the ordinary baseline (every two turns, 1-in-6).

**Output.** One of: no-check-due, a skipped check, a non-triggering check, a triggering check (arrival pending, no encounter begins yet), or an arrival (an encounter begins now). None of these outputs carries a monster identity, direction, distance, surprise, or reaction result — a future encounter-resolution consumer (`MON-001` onward) receives only the fact that an encounter has begun.

**RNG usage.** Exactly one rules-visible 1d6 roll / RNG operation per performed check; none when a check is not due or is skipped; none for arrival itself. The approved RNG contract (`RNG_CONTRACT.md`) governs how that roll is actually made; this card does not name a specific call or API.

**Survivability out of scope.** This card specifies the canonical historical procedure only. It must not accept a survivability policy, and no survivability policy may alter the trigger threshold, cadence, or arrival timing, without a separately approved Rule Card or policy decision (`ARCHITECTURE.md` §10).

---

## Deterministic Test Cases

All cases require exactly the stated number of rules-visible 1d6 rolls, using a controlled/scripted die result — never probabilistic sampling as the acceptance mechanism.

**Baseline 1d6 results (ordinary chance, check due):**

1. Scripted roll = 1 → triggered (arrival pending), one roll performed.
2. Scripted roll = 2 → not triggered.
3. Scripted roll = 3 → not triggered.
4. Scripted roll = 4 → not triggered.
5. Scripted roll = 5 → not triggered.
6. Scripted roll = 6 → not triggered.

**Baseline cadence, corrected:**

7. **Turn 1 — no baseline roll.** First completed credit received → `turns_since_last_check` becomes 1; `check_due` is false; no roll performed.
8. **Turn 2 — baseline roll due.** Second completed credit received → `turns_since_last_check` reaches 2; `check_due` is true; a roll is performed (per cases 1–6); `turns_since_last_check` resets to 0.
9. Repeating the two-turn cycle across many credits produces exactly one check per two credits, with no drift.

**Pre-decided skip, corrected cadence bookkeeping:**

10. **Turn 2, pre-decided signal present.** Second completed credit received, check due, pre-decided "already decided for this period" signal present → check skipped; no RNG operation consumed; `turns_since_last_check` resets to 0 exactly as it would for a performed roll.
11. **Next ordinary roll is not due until the next two-turn period completes.** Following case 10, a third completed credit → `turns_since_last_check` becomes 1, not due; a fourth completed credit → `turns_since_last_check` reaches 2, due again — confirming the skip did not cause an earlier or additional roll, and did not leave the counter primed to fire on the very next credit.

**Trigger scheduling vs. arrival, corrected:**

12. A triggering check (case 1) does not itself signal arrival — only "triggered, arrival pending." No arrival occurs at the moment of the triggering roll.
13. **Arrival is tested at the beginning of the immediately following Game Turn, not at the next completed credit.** Given a triggering check at the end of turn *N* (Procedure A), the beginning of turn *N*+1 (Procedure B, invoked as its own distinct procedural moment, before that turn's own Actions/Results/check-4) signals arrival.
14. **No extra roll occurs merely because arrival happens.** When Procedure B resolves a pending arrival, turn *N*+1's own Procedure A (its own step-4 check) does not occur for that same turn — the Game Turn Checklist is left before reaching it. Zero rolls are performed on an arrival turn.
15. Absent a triggering check, Procedure B never signals arrival, regardless of how many turns begin.

**Heightened checking:**

16. With `heightened_checking` active, a check is performed every completed credit (not every two), using whichever externally supplied chance level is active.
17. With chance level 2-in-6 (1-2), a scripted roll of 2 triggers; a roll of 3 does not.
18. With chance level 3-in-6 (1-3), a scripted roll of 3 triggers; a roll of 4 does not.
19. With chance level 4-in-6 (1-4), a scripted roll of 4 triggers; a roll of 5 does not.
20. Absent an explicit heightened-checking input, behavior defaults to ordinary cadence and 1-in-6 — heightened checking is never silently assumed.

**`EXP-002` interface — encounter-derived credits (per the adopted Compatible Completion):**

21. An encounter-derived credit (single-credit case, e.g., a ≤60-round encounter) advances `turns_since_last_check` identically to an ordinary credit.
22. Multiple encounter-derived credits from one long encounter (e.g., a 121-round encounter's three credits) are each consumed one at a time, in `EXP-002`'s supplied order, each independently advancing the counter — never collapsed into a single increment regardless of credit count.
23. A mixed sequence of ordinary and encounter-derived credits produces the same two-turn cadence pattern as an all-ordinary sequence of equal length, with no special-casing by origin.

**Round-mode non-execution (falls out of `EXP-002`'s own contract, tested here for `EXP-001`'s own behavior):**

24. No check, arrival, or roll occurs while `EXP-002` reports no credit produced (i.e., during round-mode) — Procedure A is simply not invoked during that interval, per `EXP-002`'s approved contract.

**RNG audit:**

25. Exactly one roll per performed check, never zero-when-due-and-not-skipped and never more than one regardless of outcome.
26. Arrival (Procedure B) consumes zero rolls.
27. Determinism: the same seed and call sequence via the seeded production RNG reproduce the same sequence of check/trigger/arrival outcomes.

## Provenance Classification

**Rules Cyclopedia Explicit**
- Ordinary cadence: every two turns (Game Turn Checklist step 4; "Wandering Monster Encounters" subsection).
- 1d6, trigger on 1 in a dungeon.
- Trigger and arrival are distinct instants, one turn boundary apart, no additional intervening turn.
- Arrival preempts that turn's own check step.
- No check during round-mode.
- DM discretion to skip when pre-decided; the skip applies to the current due period only.
- Heightened checking: frequency (every turn) and chance-level magnitude (1-2, 1-3, or 1-4 on 1d6), once RC's own fragmented text is correctly reconstructed (corroborated by BECMI's and B/X's intact parallel sentences).
- Dungeon depth does not modify this check.
- Responsibility boundary (monster identity, Number Appearing, distance, surprise, reaction are separate).

**Necessary Mathematical / Mechanical Consequence**
- None load-bearing beyond the direct facts above.

**Alternate-Source Compatible Completion**
- **Encounter-derived whole-turn credits participate in the every-two-turn cadence uniformly with ordinary credits.** Sourced from the convergent treatment across BECMI (concurrent timers not frozen by an encounter), B/X/Moldvay 1981 (an encounter folds into the same numbered turn with no separate accounting), and 1974 OD&D (combat rounds convert directly and proportionally into the same continuous turn count) — none of the three lineage sources consulted, independently, treats encounter time as a specially exempted accounting category. See "Alternate-Source Completion Research."

**Simulator Ruling**
- Not applicable — withdrawn; see "Simulator Ruling" above.

**Out of scope for this card**
- Which upstream condition/policy asserts heightened checking, and which of the three chance levels applies (Open Questions).
- Duration of heightened checking (belongs to the owning trigger condition).
- Multi-turn non-encounter activity expression (belongs to the activity-owning card).
- Monster identity (`MON-001`), Number Appearing (`MON-002`), encounter distance (`ENC-001`), surprise (`ENC-002`), reaction (`ENC-003`).
- `EXP-002`'s own turn-credit accounting mechanics (not reopened here).
- The `MON-001` ↔ `EXP-008` circularity (not resolved here).

---

## Open Questions

**`DOES NOT BLOCK EXP-001 APPROVAL`**

1. Which upstream condition/policy determines when heightened checking applies and which of the three chance levels (1-2, 1-3, 1-4) is appropriate. RC leaves this to DM judgment; this project's automated-simulator context may eventually need its own policy for this, but the *absence* of that policy does not prevent this card's own procedure from being correct — heightened checking simply never activates until a future system supplies the input. Not a blocker.
2. Duration of heightened checking once triggered — belongs to whichever future system asserts the triggering condition (`BELONGS TO ANOTHER RULE CARD`, effectively; not a fixed card yet).
3. Multi-turn non-encounter activity expression — belongs to a future activity-owning card (e.g., search/rest); this card's per-credit model already accommodates it once that card exists.
4. Exactly how the wider simulation will expose the "beginning of a new Game Turn" procedural moment to this card, distinct from `EXP-002`'s completed-credit signal. This is a future implementation-time design question, not a rules-content question — this card requires only that the moment be exposed accurately enough for Procedure B to run before that turn's own Actions/Results/check, per "Approved Mechanical Specification."

**`BELONGS TO ANOTHER RULE CARD`**

5. Monster identity — `MON-001`.
6. Number Appearing — `MON-002`.
7. Encounter distance — `ENC-001`.
8. Surprise — `ENC-002`.
9. Reaction — `ENC-003`.
10. The `MON-001` ↔ `EXP-008` circularity — not investigated or resolved here.

No `BLOCKS APPROVAL` questions remain — the prior draft's one blocking question (approval of the proposed Simulator Ruling) is resolved by this revision's Compatible Completion finding, which requires no separate human ruling to adopt (it is ordinary alternate-source research, not a Simulator Ruling).

## Approval

- Approved by: *(pending — this card is `AWAITING_APPROVAL`, not approved by this task)*
- Date: *(pending)*
- Notes: Stage-A evidence accepted 2026-08-16; Stage-B synthesis corrected per human review 2026-08-16. Gap A is resolved as an Alternate-Source Compatible Completion, not a Simulator Ruling — no ruling-specific approval item remains. This card is ready for ordinary human Rule Card approval.

---

## Historical 1974-Primary Research and Specification (preserved for provenance)

> **This section is historical and does not describe this card's current content.** Everything from here to "Status Lifecycle" is the complete 1974-primary-sourced research, specification, and human approval this card carried before the Rules Cyclopedia migration (`DEC-0007`), preserved verbatim (headers demoted one level to nest under this banner; content otherwise unchanged) for provenance — to show the reasoning that led to today's revalidated specification above, not as a statement of this card's current mechanics, dependencies, or status. In particular: **do not read anything below as saying the check happens "at the end of every turn," that a roll of 6 triggers an encounter, that arrival is immediate, or that the check is fully non-discretionary** — none of these survived this revalidation unchanged; see "Rules Cyclopedia Explicitly Establishes" and "Provenance Classification" above for what actually carries forward. This Stage-B revalidation was performed under the Evidence-First protocol: the current specification above was synthesized from the accepted Stage-A evidence *before* this historical section was consulted for comparison, per `RULE_CARD_RESEARCH_PROTOCOL.md` §13 (RC-first, legacy-card-later) — this section was not used to shape the research questions or the RC-native procedure above. Its "There are ten rounds of combat per turn" passage was, however, directly reused (not re-derived) as this card's third gap-directed alternate-source consultation for Gap A, per `SOURCE_HIERARCHY.md` §3 item 5 and the protocol's principle of not re-fetching already-established primary-text findings.

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
APPROVED          — set only by a human project owner; authorizes implementation
      ↓
IMPLEMENTED       — mechanical specification implemented per DEVELOPMENT_WORKFLOW.md
      ↓
VERIFIED          — implementation's tests and required verification have passed
                     (TESTING_STRATEGY.md §9–§10)
```

Only a Rule Card explicitly set to `APPROVED` (or a later status) by a human project owner may authorize rules implementation (`SOURCE_HIERARCHY.md` §9, `ARCHITECTURE.md` §12, `AGENTS.md` §2). An approved Rule Card does not, by itself, override the project-level Pre-Code Development Gate (`ARCHITECTURE.md` §16).
