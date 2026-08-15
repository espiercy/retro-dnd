# Rule Card: Resting Procedure

---

## Rule ID

EXP-004

## Title

Resting Procedure

## Status

AWAITING_APPROVAL

## Rules Domain

exploration

---

## 1974 Source

Gygax, Gary, and Dave Arneson. *Dungeons & Dragons, Volume 3: The Underworld & Wilderness Adventures.* Lake Geneva, WI: Tactical Studies Rules, 1974.

- Section **"THE MOVE/TURN IN THE UNDERWORLD"** (p. 8) — the operative text for this card's mandatory-rest requirement, already partially quoted and relied upon by `EXP-002`.

**Verification method.** Consistent with `EXP-001`/`EXP-002`: the same digitized, page-verified extraction of Vol. 3 was re-consulted directly rather than relied upon from memory, and searched independently (not merely re-reading the passage already quoted in `EXP-002`) for every other occurrence of "rest," "motionless," "hour," "fatigue," and "exhaust" in the booklet, to confirm no other underworld-scale rest text exists and to positively identify what else in the source uses similar language. No AD&D material was consulted.

**Exact source text (p. 8, already the basis of `EXP-002`'s rest-related facts, re-confirmed here):**

> "Time must be taken to rest, so one turn every hour must be spent motionless, and double the rest period must be taken after a flight/pursuit takes place."

**Adjacent material found and excluded as out of scope.** The search located three other passages using similar vocabulary, none of which govern underworld dungeon-turn rest and none of which are adopted by this card:

1. **Wilderness movement rest** (p. 17): "Rest: All creatures must rest after six days of movement. Rest must be at least one full day. Exception: Dragons who travel for three weeks must sleep one full week if their mode of travel was walking, and they must sleep for three full weeks if their mode of travel was flight." This is explicitly a *wilderness*-scale rule — the same section states "Each move will constitute one day. Each day is considered a turn" (p. 17), a completely different time granularity (a wilderness "turn" = one day) from the underworld turn (≈ 10 minutes) this card concerns. Not the same procedure; not used here.
2. **Wilderness pursuit rest** (p. 20): "For each hex moved in pursuit, a party must spend one-half day resting (remember, a day equals one turn). During a day at rest two dice are thrown for determining if wandering monsters are encountered, rather than but one." Also wilderness-day-scale, and a distinct mechanism (doubling the *number of dice thrown* per rest period, not the *number of rest turns*) from the underworld doubled-rest-period clause this card addresses. Not adopted, but noted below as a thematically relevant, non-binding data point (see "Compatibility Analysis").
3. **Healing Wounds** (p. 35): "As noted previously, energy levels can only be regained by fresh experience, but common wounds can be healed with the passage of time (or the use of magics already explained). On the first day of complete rest no hit points will be regained, but every other day thereafter one hit point will be regained until the character is completely healed." This is an explicit, *separate*, day-granularity hit-point-recovery system, textually and mechanically distinct from the turn-granularity "motionless" requirement at p. 8. It directly informs "1974 Leaves Undefined" item 5 and "Central Question F" below: 1974 itself does not connect the underworld mandatory rest turn to hit-point recovery. This system belongs to a future healing/downtime Rule Card, not `EXP-004`.

## 1974 Explicitly Establishes

1. **A recurring mandatory rest requirement exists.** "One turn every hour must be spent motionless" (p. 8) is stated as an obligation ("must be"), not as an optional or referee-discretionary activity.
2. **The baseline rest period is one turn**, consuming dungeon time exactly as any other turn-costed activity (already fixed by `EXP-002`'s per-activity-type table — not reopened here).
3. **A flight/pursuit episode doubles the required rest period.** "Double the rest period must be taken after a flight/pursuit takes place" (p. 8) — i.e., two turns rather than one (already fixed by `EXP-002`'s per-activity-type table as "Rest, while in a flight/pursuit state = 2 turns" — not reopened here).
4. **The approximate ratio between the mandatory-rest cadence and elapsed time is fixed by arithmetic, though not by an explicit discrete counting rule.** A turn is "approximately ten minutes" (`EXP-002`, p. 8); an hour is therefore approximately six turns; "one turn every hour" therefore implies, as a matter of arithmetic, roughly one rest turn per six-turn cycle. The text does not itself say "after five turns" or "on the sixth turn" — see "1974 Leaves Undefined," item 1.
5. **What triggers or ends a flight/pursuit state is not specified by this passage** — that remains `ENC-005`'s concern, exactly as `EXP-002` already established for the movement-doubling half of the same sentence. This card, like `EXP-002`, treats "a flight/pursuit episode has occurred" as an external event it consumes, not one it resolves.
6. **Hit-point recovery is governed by a separate, day-granularity system** (p. 35, "Healing Wounds") that the p. 8 passage does not reference and does not depend on. 1974 does not connect the underworld motionless-rest turn to wound healing.

## 1974 Leaves Undefined

Consistent with `EXP-002`'s own treatment of adjacent gaps, each item below is stated as narrowly as possible.

1. **The exact discrete cadence.** 1974 gives a ratio ("one turn every hour"), not an executable counting rule. An implementation agent cannot determine from this text alone *which* turn must be the rest turn, or how a running count of elapsed turns is meant to trigger it.
2. **What kinds of elapsed dungeon time count toward the requirement.** The text says "every hour," without stating whether that hour is measured only in movement time, or in all dungeon-turn time regardless of activity type.
3. **Whether rest time itself counts toward triggering the next mandatory rest.** Not addressed at all — a bookkeeping question 1974's authors had no occasion to consider, but one an executable specification cannot avoid.
4. **The exact moment mandatory rest takes effect, and what enforcement (if any) applies once it is due.** The text states an obligation, not an enforcement mechanism. It does not say what happens if the party does not comply.
5. **What "motionless" permits or excludes.** The text gives no boundary between "motionless" and other simultaneous referee-adjudicated activity (listening, standing watch, handling equipment, etc.).
6. **Whether resting before the mandatory threshold is arrived at satisfies or resets the requirement**, or is mechanically inert.
7. **How a flight/pursuit episode's doubled-rest requirement interacts with any ordinary rest debt already outstanding or accumulating**, and whether successive flight/pursuit episodes before the doubled rest is taken compound the requirement.
8. **What happens to the rest requirement if a mandatory or voluntary rest turn is interrupted** (e.g., by a wandering-monster encounter triggered during that turn) before it completes.

---

## Completion Research

Per `SOURCE_HIERARCHY.md` §8, this is treated as a consequential ambiguity (it gates enforcement behavior across the entire exploration loop) and researched with the full lineage walk rather than stopping at the first available later text, while staying bounded to underworld mandatory rest specifically — no broader fatigue, wilderness-travel, or healing-system research was performed, per the assigning instructions.

**Holmes Basic D&D (1977) and B/X D&D — Moldvay Basic (1981) / Cook Expert.** Verified via `WebSearch`, cross-checked against multiple independent secondary sources (Dragonsfoot forum threads discussing the rule directly, Zenopus Archives' Holmes-specific scholarship already used for `EXP-002`, and an EN World "Let's Read" thread quoting Moldvay's text):

- **Cadence.** Multiple independent sources converge on the same figure: OD&D, Holmes, and B/X are all described as using a "rest 1 turn in 6" cadence — equivalently stated by one source specifically for B/X as "after moving for 5 turns, the party must rest for 1 turn." This is arithmetically identical to the ratio 1974's own numbers already imply (turn ≈ 10 min → hour ≈ 6 turns → 1 of those 6 is rest, leaving 5) — the same corroboration pattern `EXP-002` already used for the same underlying arithmetic. It supplies the one thing 1974 itself does not state directly: an explicit discrete count ("5" non-rest turns, not merely "≈ 1 in 6").
- **Consequence of not resting.** B/X is specifically and consistently described as imposing "a −1 penalty to all hit and damage rolls until rest is taken" for skipping the mandatory rest turn — not a hard block on further activity. This directly addresses 1974's silence on enforcement (item 4 above).
- **Hit-point recovery.** Holmes is independently corroborated as using its own day-granularity healing rule ("1–3 points... every 24 hours of full rest"), structurally the same *kind* of separate system as 1974's own p. 35 "Healing Wounds" passage — reinforcing, not contradicting, the conclusion that turn-scale motionless rest and day-scale wound healing are different systems throughout this lineage.
- **BECMI / Rules Cyclopedia.** Multiple sources agree this specific mandatory-rest rule was **dropped** in BECMI and is not restated in the Rules Cyclopedia ("no specific rules for this kind of resting"; the party is instead assumed to take breathers implicitly during ordinary dungeon movement). No useful completion material was found here, and none was expected to be, once B/X was found to fully address the two open questions (cadence, consequence) `SOURCE_HIERARCHY.md` §3 sends research forward to resolve.
- **Interrupted rest.** No reliable, clearly-attributed non-AD&D lineage source was found addressing whether an interrupted mandatory rest turn must restart. Search results touching "interrupted rest" were dominated by unrelated modern-edition material (5th-edition long-rest interruption rules) and by a different classic-era mechanic entirely — the multi-hour rest required for spell-memorization, which is not the same "motionless" dungeon-turn rest this card concerns and is out of this card's scope. This question remains unresolved by the lineage; see "Simulator Ruling."
- **Voluntary/early rest and doubled-rest stacking.** No source found — lineage or 1974 — addresses either question directly. Both remain unresolved by history; see "Simulator Ruling."

**Verification caveat**, consistent with the standard already applied in `EXP-002`'s research: these findings rest on `WebSearch` results drawing on named, identifiable secondary sources (Dragonsfoot forum discussion, Zenopus Archives, EN World) rather than this agent's own page-by-page reading of the Holmes or Moldvay booklets. The specific "−1 to hit and damage" figure and the "5 turns" figure should be treated as well-corroborated (multiple independent sources agree) but not independently page-verified by this agent, and are flagged here for a human reviewer's attention before final approval, exactly as `EXP-002`'s B2 citation was flagged before its own verification.

## Compatibility Analysis

| Source | Addresses | Judgment |
|---|---|---|
| Holmes/B-X — "rest 1 turn in 6" / "after 5 turns, rest 1 turn" | Exact cadence (1974 Leaves Undefined, item 1) | **Adopted as a compatible completion.** Reproduces the same ratio 1974's own numbers already imply and supplies only the missing discrete counting rule; does not change the underlying 1:6 relationship 1974 establishes. |
| B/X — "−1 to hit and damage until rest is taken" | Consequence of not resting (item 4) | **Presented as an alternative completion, not adopted as the primary proposal.** Does not contradict any explicit 1974 statement (1974 states no consequence at all), but it introduces a specific combat-mechanical penalty 1974 never mentions, and applying it would reach into combat-domain territory (`COMBAT-002`/`COMBAT-006`) that this card does not otherwise touch. See "Simulator Ruling" for the full treatment and the preferred alternative. |
| BECMI / Rules Cyclopedia — rule dropped entirely | Cadence, consequence | **Not adopted.** Removing an explicit-enough historical procedure is a revision by omission, not a compatible completion, per `SOURCE_HIERARCHY.md` §6. Its absence there is noted, not imported. |
| Wilderness pursuit-rest (p. 20) — doubled monster-check exposure (two dice, not one) during pursuit-related rest | Whether resting parties get an exception from `EXP-001` checks (see "Rest and Wandering-Monster Checks" below) | **Not adopted directly** — different scale (wilderness day-turns) and different mechanism (extra dice, not extra dungeon turns). **Used only as corroborating context**: it shows this source's own design instinct, elsewhere in the same booklet, is to increase a resting party's exposure to wandering monsters after pursuit, never to suppress it. This supports (without independently proving) the conclusion that ordinary `EXP-001` cadence should continue unmodified during underworld rest turns. |

---

## Simulator Ruling

No combination of 1974 and compatible later sources resolves every executable question this card must answer. Each ruling below is presented as a **proposed** Simulator Ruling for human decision — this card does not self-approve any of them. Per `SOURCE_HIERARCHY.md` §3 item 8, a Simulator Ruling is used only where no compatible historical source supplies a complete answer; where one does (cadence), it is adopted above as a completion instead.

**Ruling 1 (required) — What counts toward the cadence.**
*Proposed:* every qualifying non-rest dungeon turn, regardless of activity type (movement, search, listening, ESP, hiding, treasure-loading, combat, or any other turn-costed activity `EXP-002` recognizes), counts toward the recurring rest requirement. *Rationale:* `EXP-002`'s already-approved shared dungeon-time ledger treats all activity types uniformly for turn-elapsing purposes, and `EXP-001` already consumes that same uniform signal without regard to activity type. A movement-only counting rule for `EXP-004` would require inventing a second, parallel time-tracking mechanism inconsistent with the already-approved single-ledger architecture, which this card does not reopen. This is classified as a **necessary mechanical consequence** of not reopening `EXP-002`, not an independent Simulator Ruling requiring alternatives.

**Ruling 2 (required) — Does rest time generate its own rest debt.**
*Proposed:* `EXP-004` maintains a counter of "qualifying turns since rest was last satisfied," separate from `EXP-002`'s own elapsed-time ledger. Rest turns (ordinary or doubled) do **not** increment this counter — completing them instead resets it to zero. *Rationale:* without this distinction, a rest turn's own dungeon-time cost would itself count toward triggering the next rest, producing a nonsensical unbounded recursion inconsistent with the plain intent of a rest requirement (to be satisfiable). No historical source addresses this bookkeeping question, because it only arises when the rule is made executable. *Alternative considered and rejected:* a single unified counter where every elapsed turn, including rest turns, counts toward the next threshold — rejected because it either never allows the requirement to be satisfied (if rest turns also increment it) or requires an arbitrary exception rule at that point anyway, which is exactly the distinction this ruling proposes directly instead.

**Ruling 3 (required) — Enforcement when rest is due.**
*Proposed default:* a **hard gate** — once the qualifying-turn counter reaches the threshold (5, per the adopted B/X-corroborated cadence), no further qualifying non-rest turn may be consumed until a satisfying rest is completed. This is the most literal reading of 1974's obligatory language ("must be spent") without inventing new mechanical content (a numeric combat penalty) that 1974 never states, and it requires no reach into combat-domain mechanics. *Alternative (well-sourced, not the default proposal):* adopt B/X's **−1 to hit and damage rolls until rest is taken**, allowing activity to continue. This is a genuine, on-point, compatible later completion — arguably the historically "richer" answer — but its actual application is a combat-domain mechanic; if adopted, this card would only expose a `rest_overdue` state fact, and a separate combat-domain Rule Card (`COMBAT-002`/`COMBAT-006`) would need to consume it to apply the penalty. Both alternatives are presented for human decision; this card does not pick one on its own authority.

**Ruling 4 (required) — What "motionless" permits.**
*Proposed:* the smallest faithful reading — "motionless" restricts spatial movement, not all referee-adjudicated activity. A turn otherwise spent on quiet, non-movement activity (standing watch, listening, brief equipment handling) is not automatically disqualified from counting as the required rest turn, absent a more specific historical statement. *Alternative:* a maximal reading — a qualifying rest turn permits no other adjudicated activity of any kind. Neither reading is resolved by 1974 or the lineage; this ruling does not need to be finalized to complete this card's core accounting behavior (which needs only to know whether a given turn is *designated* as the rest turn, not to exhaustively police what else occurs during it), and is flagged as non-blocking in "Open Questions." **1974 does not connect this rest turn to hit-point recovery** (see "1974 Explicitly Establishes," item 6) — that is not itself a Simulator Ruling but a directly sourced negative finding, and this card does not propose changing it.

**Ruling 5 (required) — Voluntary/early rest.**
*Proposed:* a voluntarily-taken rest turn that meets the same definition as a mandatory one (one full turn, motionless) satisfies and resets the qualifying-turn counter identically to a mandatory rest turn — 1974 gives no textual basis for treating "the same activity, taken slightly early" as mechanically different from the mandatory case. *Alternative considered and rejected as less parsimonious:* a model in which voluntary rest consumes time without affecting the requirement at all, meaning the party could rest indefinitely without ever "banking" toward the eventual mandatory turn — rejected because it requires inventing a second, functionally distinct category of "resting" nowhere suggested by the source.

**Ruling 6 (required) — Doubled post-flight/pursuit rest and its interaction with ordinary rest debt.**
*Proposed:* the doubled (two-turn) post-flight/pursuit rest requirement is triggered immediately when the flight/pursuit episode ends (the most direct reading of "after a flight/pursuit takes place"), and **satisfies/resets** whatever ordinary rest debt is outstanding at that moment, rather than stacking as an additional, separately-tracked obligation. Concretely, applying this to the three scenarios raised in the assigning task:
- No ordinary rest debt outstanding when flight begins, flight ends → exactly **2 turns** required (the doubled rest alone).
- Ordinary rest threshold reached *during* the flight/pursuit episode itself, flight then ends → still exactly **2 turns**, not 3 — the doubled rest is proposed to be the ceiling 1974 establishes for this situation; nothing in the text supports adding the ordinary 1-turn requirement on top of the doubled one.
- Two separate flight/pursuit episodes occur before the special rest is taken → the outstanding requirement remains **2 turns**, not 4 — proposed as **not stacking**, because 1974 states a doubling relationship, not a compounding one, and no lineage source suggests otherwise.

*Alternative considered and rejected:* additive/stacking models for any of the three cases above — rejected for lack of any historical or lineage support; a compounding rule would be this card's own invention with no textual anchor at all, unlike the doubling itself which is explicitly 1974 text.

**Ruling 7 (required) — Rest interrupted by an encounter.**
*Proposed:* if the `EXP-001` check performed during a rest turn (ordinary or doubled) triggers a wandering-monster encounter that interrupts the party, the interrupted turn does **not** satisfy the rest requirement — the requirement remains outstanding, to be attempted again once it is safe to do so. Any subsequent combat consumes dungeon time normally through `EXP-002` and, per Ruling 1, counts as qualifying non-rest time toward the *next* rest requirement, not toward satisfying the interrupted one. *Rationale:* "motionless... rest" was not actually completed if interrupted, so treating the turn as satisfying would contradict the plain sense of the requirement; no partial-credit mechanism is proposed, consistent with `AGENTS.md` §5's guidance against inventing convenient complexity the source does not support. *Alternative considered and rejected:* a proportional/partial-credit model (an interrupted rest turn counts fractionally toward satisfying the requirement) — rejected as unsupported invention with no historical basis and unnecessary complexity for a rule 1974 states as a whole-turn requirement.

---

## Approved Mechanical Specification

*(Presented in pre-approval draft form, consistent with `EXP-002`'s original submission — not authoritative until a human sets this card's Status to `APPROVED`, per `AGENTS.md` §2.)*

**Scope.** This procedure determines: (a) when the recurring mandatory rest requirement becomes due, (b) what satisfies it, (c) how a flight/pursuit episode's doubled requirement interacts with it, and (d) what happens if a rest turn is interrupted. It does not decide *whether* the party chooses to rest at any given non-mandatory moment (a player/referee decision), does not define hit-point recovery, and does not implement any enforcement penalty itself if Ruling 3's combat-penalty alternative is later selected — that would be implemented by the combat domain consuming this card's exposed state.

**Dependencies:**

```text
EXP-002 (shared dungeon-time ledger, turn-elapsed signal)  ─┐
EXP-001 (wandering-monster check, consumes the same signal) ─┼─→  EXP-004 rest state
ENC-005 (flight/pursuit episode occurrence)                 ─┘
```

`EXP-004` consumes `EXP-002`'s "dungeon turn elapsed" signal as one of its boundary consumers, exactly as `EXP-001` does — it does not depend on `EXP-001`'s own content, only on the same shared signal. It consumes "a flight/pursuit episode has just ended" as an external event from `ENC-005`, exactly as `EXP-002` already consumes "the party is in a flight/pursuit state" without resolving it.

**Minimum authoritative state** (per Ruling 2 and the general principle of tracking no more than necessary):

| State | Meaning |
|---|---|
| `qualifying_turns_since_rest` | Count of completed non-rest qualifying turns (Ruling 1) since the rest requirement was last satisfied. Incremented by each "dungeon turn elapsed" signal attributable to non-rest activity; not incremented by rest turns themselves (Ruling 2); reset to 0 whenever the rest requirement is satisfied. |
| `rest_turns_required` | 0 if no rest is currently outstanding; 1 if an ordinary rest is due; 2 if a doubled post-flight/pursuit rest is due (Ruling 6). Set to 1 when `qualifying_turns_since_rest` reaches the threshold (5, per the adopted cadence). Set to 2 (not added to any existing value) when a flight/pursuit episode ends (Ruling 6). Decremented by one for each rest turn successfully completed without interruption; unchanged by an interrupted rest turn (Ruling 7). |

No further state is proposed. In particular, no separate state is proposed for "which specific activities occurred during a rest turn" (Ruling 4 does not require tracking this for `EXP-004`'s own accounting) or for stacking multiple flight/pursuit episodes (Ruling 6 proposes exactly one outstanding doubled requirement, not a count of episodes).

**Procedure — cadence and threshold (Rulings 1–2):**

```text
WHEN EXP-002 emits a "dungeon turn elapsed" signal for a turn attributable to
qualifying non-rest activity (i.e., the elapsed turn was not itself a rest turn):

    qualifying_turns_since_rest := qualifying_turns_since_rest + 1

    IF qualifying_turns_since_rest >= 5:
        rest_turns_required := MAX(rest_turns_required, 1)
```

**Procedure — enforcement (Ruling 3, primary proposal — hard gate):**

```text
BEFORE a further qualifying non-rest turn is consumed:

    IF rest_turns_required > 0:
        the requesting activity is not permitted to proceed
        (this is the same structural "boundary consumer signals interruption"
         mechanism EXP-002 already establishes as possible at each threshold —
         see EXP-002 "Approved Mechanical Specification," Accumulation algorithm)
```

*(If Ruling 3's alternative is instead approved, this block is replaced by: no blocking occurs; instead, `rest_turns_required > 0` is exposed as a `rest_overdue` fact for the combat domain to consume as a to-hit/damage penalty. This card does not specify that penalty's mechanics.)*

**Procedure — satisfying rest (Rulings 5, 7):**

```text
WHEN a rest turn (voluntary or mandatory) is consumed through EXP-002's
ordinary activity accounting (cost: 1 turn, or 2 turns if flagged as the
doubled post-flight/pursuit rest — both already fixed by EXP-002):

    IF the turn completes without an EXP-001-triggered interruption:
        rest_turns_required        := MAX(rest_turns_required - 1, 0)
        qualifying_turns_since_rest := 0
    ELSE  (interrupted — Ruling 7):
        rest_turns_required and qualifying_turns_since_rest are unchanged
        (the interrupted turn satisfies nothing; it must be attempted again)
```

**Procedure — flight/pursuit doubled rest (Ruling 6):**

```text
WHEN ENC-005 reports that a flight/pursuit episode has just ended:

    rest_turns_required := 2   (not added to any existing value — replaces/
                                 satisfies whatever ordinary debt was
                                 outstanding, per Ruling 6)
```

**Integration with `EXP-001` and `EXP-002` (unmodified).** A rest turn — mandatory, voluntary, or doubled — is consumed through `EXP-002`'s ordinary accounting exactly like any other activity, and each whole turn it completes emits `EXP-002`'s normal "dungeon turn elapsed" signal, which `EXP-001` consumes exactly as it always does (1d6, trigger on 6). Neither `EXP-001`'s cadence nor `EXP-002`'s accumulation algorithm is modified by this card. A two-turn doubled rest therefore produces two ordinary check opportunities, consistent with "Rest and Wandering-Monster Checks" and this card's Compatibility Analysis — no exception is created.

**Multi-turn activity crossing the threshold.** Because `EXP-002` already resolves turn boundaries progressively and synchronously during an in-progress multi-turn activity, `EXP-004`'s threshold check (above) is evaluated at each such boundary alongside `EXP-001`'s. If a multi-turn activity's *n*-th internal boundary is the one that pushes `qualifying_turns_since_rest` to 5, `rest_turns_required` becomes 1 at that same boundary, and (under Ruling 3's primary proposal) the activity is not permitted to continue past that point — exercising the same structural interruption possibility `EXP-002` already established without designing a new one.

**Survivability out of scope.** Consistent with `EXP-001`/`EXP-002`, this card specifies canonical historical rest accounting only. It must not accept a survivability policy, and no survivability policy may alter the cadence, enforcement, or doubled-rest rules, without a separately approved Rule Card or policy decision (`ARCHITECTURE.md` §10).

**No RNG owned by this card.** Like `EXP-002`, this procedure is purely state-tracking arithmetic; the only randomness in its vicinity belongs to `EXP-001`'s own check.

---

## Deterministic Test Cases

All cases are pure state-machine transitions; cases involving `EXP-001`'s own die roll use a controlled RNG for that portion only.

**Normal cadence:**

1. **Five qualifying turns trigger the requirement.** Five successive non-rest qualifying turns (of any mix of activity types, per Ruling 1) → `qualifying_turns_since_rest` reaches 5, `rest_turns_required` becomes 1.
2. **One rest turn satisfies it.** Following case 1, one uninterrupted rest turn → `rest_turns_required` returns to 0, `qualifying_turns_since_rest` resets to 0.

**Before threshold:**

3. **No premature requirement.** Four qualifying turns → `rest_turns_required` remains 0; no gating or penalty condition is active.

**Rest boundary / `EXP-002` integration:**

4. **Rest turn advances the shared ledger normally.** A rest turn's consumption produces exactly one `EXP-002` "dungeon turn elapsed" signal, identically to any other 1-turn activity.

**`EXP-001` integration:**

5. **Mandatory rest still produces a check opportunity.** A mandatory rest turn's elapsed-turn signal results in exactly one `EXP-001` check, using the same RNG contract as any other turn.

**No recursive debt (Ruling 2):**

6. **Rest does not generate new rest debt.** Starting from `rest_turns_required = 1`, `qualifying_turns_since_rest = 5`, completing the required rest turn resets both to `0`/`0` — not to `0`/`1` (which a naive "rest also counts as elapsed time" model would incorrectly produce).

**Multi-turn activity crossing the threshold:**

7. **Threshold reached mid-activity gates further progress (Ruling 3, primary proposal).** Starting from `qualifying_turns_since_rest = 4`, a multi-turn activity whose first internal boundary would be qualifying turn 5 → `rest_turns_required` becomes 1 at that boundary, and the activity's further progress is not permitted past that point, per `EXP-002`'s existing interruption structure.

**Voluntary early rest (Ruling 5):**

8. **Voluntary rest resets the counter.** Starting from `qualifying_turns_since_rest = 3`, a voluntarily-taken rest turn (not mandatory) → resets to `0`, identically to case 2's mandatory case.

**Flight/pursuit doubled rest (Ruling 6):**

9. **No prior debt.** `rest_turns_required = 0` when a flight/pursuit episode ends → becomes `2`.
10. **Prior ordinary debt already due.** `rest_turns_required = 1` when a flight/pursuit episode ends → becomes `2`, not `3`.
11. **Two episodes before rest is taken.** A second flight/pursuit episode ends while `rest_turns_required` is already `2` (from a first episode, unsatisfied) → remains `2`, not `4`.
12. **Doubled rest produces two check opportunities.** Satisfying a `rest_turns_required = 2` obligation consumes two turns through `EXP-002`, producing two ordinary `EXP-001` check opportunities — no exception.

**Interrupted rest (Ruling 7):**

13. **Interrupted mandatory rest does not satisfy the requirement.** Starting from `rest_turns_required = 1`, a rest turn whose `EXP-001` check triggers an encounter that interrupts it → `rest_turns_required` remains `1`, `qualifying_turns_since_rest` is unchanged (not reset).
14. **Combat following an interrupted rest counts toward the next requirement.** Continuing case 13, if the resulting combat consumes further dungeon turns, those turns increment `qualifying_turns_since_rest` normally (per Ruling 1), independent of the still-outstanding rest requirement from case 13.

## Provenance Classification

**1974 Explicit**
- A recurring mandatory rest requirement exists ("one turn every hour must be spent motionless").
- A flight/pursuit episode doubles the required rest period.
- Hit-point recovery is governed by a separate day-granularity system, not this p. 8 passage.

**Necessary Mathematical / Mechanical Consequence**
- The approximate 1-rest-turn-per-6-turn ratio (from turn ≈ 10 minutes, hour ≈ 6 turns).
- All qualifying-turn accounting uses `EXP-002`'s single shared ledger, uniformly across activity types (Ruling 1) — forced by not reopening `EXP-002`'s approved architecture, not an independent choice.
- The doubled rest period equals two turns (already fixed by `EXP-002`).

**Later Compatible D&D Completion**
- The exact discrete cadence, "5 qualifying turns → 1 mandatory rest turn," from the Holmes/B-X-corroborated "rest 1 turn in 6" convention.

**Simulator Ruling (proposed, unresolved pending human decision)**
- Ruling 2: rest turns do not generate their own rest debt.
- Ruling 3: enforcement mechanism when rest is due (hard gate, proposed default, vs. B/X's −1 to-hit/damage penalty, alternative).
- Ruling 4: the activity boundary of "motionless" (non-blocking).
- Ruling 5: voluntary/early rest resets the cadence.
- Ruling 6: doubled post-flight/pursuit rest satisfies/replaces rather than stacks with ordinary debt, and does not compound across repeated episodes.
- Ruling 7: an interrupted rest turn does not satisfy the requirement, and does not receive partial credit.

**Out of scope for this card**
- The B/X-attested −1 to-hit/damage penalty's actual mechanical application (`COMBAT-002`/`COMBAT-006`, only if Ruling 3's alternative is adopted).
- Flight/pursuit state entry/exit triggers (`ENC-005`).
- Hit-point recovery / healing (a future downtime/healing Rule Card).
- Wilderness-scale rest and pursuit-rest procedures (out of scope entirely; noted only for transparency).

---

## Open Questions

1. **Rulings 2–7 all require human decision before this card can be `APPROVED`.** See "Simulator Ruling" for the full proposals and alternatives.
2. **The B/X "−1 to hit/damage" citation (cadence and penalty figures) is well-corroborated by multiple independent secondary sources but not independently page-verified by this agent against the primary Holmes/Moldvay booklets.** Flagged for human attention before final approval, per the same standard applied to `EXP-002`'s B2 citation.
3. **Ruling 4 (what "motionless" permits) does not block this card's core accounting behavior** and may be left genuinely open even after approval, revisited only if a future card (e.g., a detailed activity-execution loop) needs a firmer answer.
4. **If Ruling 3's combat-penalty alternative is ever selected instead of the hard-gate default, this card would gain a soft forward dependency on the combat domain** (to expose `rest_overdue` in a form `COMBAT-002`/`COMBAT-006` can consume) not currently reflected in `docs/rules/INVENTORY.md`'s `EXP-004` row. This is not proposed as an inventory correction — the primary proposal (hard gate) requires no such dependency — but is noted here for the human reviewer's awareness in case the alternative is preferred.

## Approval

- Approved by: `<name>`
- Date: `<date>`
- Notes: `<optional>`

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
