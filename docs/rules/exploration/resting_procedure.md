# Rule Card: Resting Procedure

> **Migration note (2026-08-16).** Previously approved under the superseded 1974-primary source policy. Requires Rules Cyclopedia revalidation before implementation authority is restored (`DEC-0007-rules-cyclopedia-primary-rules-authority.md`, `DEVELOPMENT_WORKFLOW.md` §9.7). This does not indicate the research below was incorrect — only that it has not yet been reviewed against the current source hierarchy. All content below is preserved unchanged as the historical research and approval record; it is not rewritten by this migration. See `docs/rules/RULESET_BASELINE_MIGRATION.md`.
>
> Prior approval record: Approved by Human project owner, 2026-08-16, under the then-governing 1974-primary source policy — see this card's own "Approval" section below, preserved unchanged.

---

## Rule ID

EXP-004

## Title

Resting Procedure

## Status

REVALIDATION_REQUIRED

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
3. **Healing Wounds** (p. 35): "As noted previously, energy levels can only be regained by fresh experience, but common wounds can be healed with the passage of time (or the use of magics already explained). On the first day of complete rest no hit points will be regained, but every other day thereafter one hit point will be regained until the character is completely healed." This is an explicit, *separate*, day-granularity hit-point-recovery system, textually and mechanically distinct from the turn-granularity "motionless" requirement at p. 8. It directly informs "1974 Leaves Undefined" item 5 below: 1974 itself does not connect the underworld mandatory rest turn to hit-point recovery. This system belongs to a future healing/downtime Rule Card, not `EXP-004`.

## 1974 Explicitly Establishes

1. **A recurring mandatory rest requirement exists, and it is expressed in time, not distance.** "One turn every hour must be spent motionless" (p. 8) is stated as an obligation ("must be"), not as an optional or referee-discretionary activity — and critically, the unit it is measured against is an **hour** (elapsed dungeon time), not a distance moved or a count of moves taken. The requirement's own textual anchor is therefore time-based from the 1974 text itself, before any later source is consulted (see "Completion Research" for how Holmes makes this explicit and how it bears on what counts toward the cadence).
2. **The baseline rest period is one turn**, consuming dungeon time exactly as any other turn-costed activity (already fixed by `EXP-002`'s per-activity-type table — not reopened here).
3. **A flight/pursuit episode doubles the required rest period.** "Double the rest period must be taken after a flight/pursuit takes place" (p. 8) — i.e., two turns rather than one (already fixed by `EXP-002`'s per-activity-type table as "Rest, while in a flight/pursuit state = 2 turns" — not reopened here).
4. **The approximate ratio between the mandatory-rest cadence and elapsed time is fixed by arithmetic, though not by an explicit discrete counting rule.** A turn is "approximately ten minutes" (`EXP-002`, p. 8); an hour is therefore approximately six turns; "one turn every hour" therefore implies, as a matter of arithmetic, roughly one rest turn per six-turn cycle. The 1974 text does not itself say "after five turns" or "on the sixth turn" — see "1974 Leaves Undefined," item 1, and "Completion Research" for how the lineage supplies the exact discrete count.
5. **What triggers or ends a flight/pursuit state is not specified by this passage** — that remains `ENC-005`'s concern, exactly as `EXP-002` already established for the movement-doubling half of the same sentence. This card, like `EXP-002`, treats "a flight/pursuit episode has occurred" as an external event it consumes, not one it resolves.
6. **Hit-point recovery is governed by a separate, day-granularity system** (p. 35, "Healing Wounds") that the p. 8 passage does not reference and does not depend on. 1974 does not connect the underworld motionless-rest turn to wound healing.

## 1974 Leaves Undefined

Consistent with `EXP-002`'s own treatment of adjacent gaps, each item below is stated as narrowly as possible; several are since resolved by completion research, cross-referenced below.

1. **The exact discrete cadence.** 1974 gives a ratio ("one turn every hour"), not an executable counting rule. Resolved via later compatible completion — see "Completion Research" and "Compatibility Analysis."
2. **Whether the "hour" is measured only in movement time, or in all dungeon-turn time regardless of activity type.** Resolved via later compatible completion (Holmes) — see "Completion Research."
3. **Whether rest time itself counts toward triggering the next mandatory rest.** Not addressed by any historical source — a bookkeeping question 1974's authors had no occasion to consider. Resolved as a necessary mechanical consequence of the adopted six-turn cycle — see "Approved Mechanical Specification."
4. **What enforcement, if any, applies once mandatory rest is due and not taken.** The 1974 text states an obligation, not an enforcement mechanism. Resolved via later compatible completion (B/X) — see "Completion Research" and "Compatibility Analysis."
5. **What "motionless" permits or excludes** beyond the absence of spatial movement. Narrowly resolved for this card's purposes — see "Simulator Ruling."
6. **Whether resting before the mandatory threshold is arrived at satisfies or resets the requirement.** Resolved by Simulator Ruling — see below.
7. **How a flight/pursuit episode's doubled-rest requirement interacts with any ordinary rest debt already outstanding, and whether successive episodes compound it.** Resolved by Simulator Ruling — see below.
8. **What happens to the rest requirement's bookkeeping at the moment a rest turn's completed-turn boundary coincides with an `EXP-001`-triggered encounter**, and what happens if some future mechanic interrupts a rest turn before it has fully elapsed. Resolved — see "Approved Mechanical Specification" and Simulator Ruling on true pre-boundary interruption.

---

## Completion Research

Per `SOURCE_HIERARCHY.md` §8, this is treated as a consequential ambiguity (it gates enforcement behavior across the entire exploration loop) and researched with the full lineage walk rather than stopping at the first available later text, while staying bounded to underworld mandatory rest specifically — no broader fatigue, wilderness-travel, or healing-system research was performed, per the assigning instructions.

**Human review has independently verified the following citations**, resolving the verification caveat that previously accompanied them in this card's draft form. They are treated as settled for approval purposes.

**Holmes Basic D&D (1977).**
- Holmes explicitly clarifies the recurring rest cadence as **"one turn every hour / one turn out of every six."** This is the pivotal piece of completion evidence for this card: it confirms, in the D&D lineage's own words, that the 1974 hour-based formulation (item 1 under "1974 Explicitly Establishes") is correctly read as a **dungeon-time cadence** — a ratio of elapsed turns — rather than a distance- or movement-specific rule. Holmes restates the ratio without narrowing its scope to any one activity type.
- Holmes also preserves the concept of a doubled, two-turn rest after running (flight/pursuit), consistent with — not a revision of — the 1974 text.

**Moldvay B/X D&D (1981).**
- Moldvay explicitly states: **"after moving for five turns, the party must rest for one turn"**; and, consistent with Holmes, that **"one turn in six is spent resting."** Moldvay's own wording is specifically phrased in terms of *moving* — this card does not overstate it as a general "any five turns" statement in Moldvay's own words. However, Moldvay's narrower movement-specific phrasing does not displace the earlier, broader OD&D/Holmes hour-based (dungeon-time) formulation; Moldvay supplies the exact discrete count ("five"), which this card adopts, while the *scope* of what counts toward that count (all dungeon-turn activity, not movement alone) is grounded in the earlier and broader OD&D/Holmes framing, not in Moldvay's own narrower wording. This distinction is preserved transparently rather than silently harmonized (see "Compatibility Analysis").
- Moldvay explicitly states that characters who fail to rest **suffer a −1 penalty to hit and damage until they do rest.** This directly and completely addresses 1974's silence on enforcement.

**Hit-point recovery.** Holmes is independently corroborated as using its own day-granularity healing rule ("1–3 points... every 24 hours of full rest"), structurally the same *kind* of separate system as 1974's own p. 35 "Healing Wounds" passage — reinforcing, not contradicting, the conclusion that turn-scale motionless rest and day-scale wound healing are different systems throughout this lineage.

**BECMI / Rules Cyclopedia.** This specific mandatory-rest rule was **dropped** in BECMI and is not restated in the Rules Cyclopedia (the party is instead assumed to take breathers implicitly during ordinary dungeon movement). No completion material was found here, and none was needed, since Holmes and B/X together fully address both open questions (cadence and enforcement) `SOURCE_HIERARCHY.md` §3 sends research forward to resolve.

**Interrupted rest / rest-boundary ordering.** No non-AD&D lineage source addresses this bookkeeping question at the level of detail an executable specification needs. It is resolved instead as a necessary mechanical consequence of `EXP-002`'s own already-approved signal semantics (see "Approved Mechanical Specification") — not a Simulator Ruling in the sense of an invented answer, but a correction of an internal inconsistency in this card's own earlier draft.

**Voluntary/early rest and doubled-rest stacking.** No source — 1974 or lineage — addresses either question directly. Both are resolved by Simulator Ruling below, as the smallest sufficient proposals.

## Compatibility Analysis

| Source | Addresses | Judgment |
|---|---|---|
| Holmes — "one turn every hour / one turn out of every six" | Whether the cadence is time-based (all activity) or movement-specific | **Adopted as the governing clarification.** Confirms the 1974 hour-based formulation is a dungeon-time cadence, not a movement-specific one. This is the primary historical basis for treating all `EXP-002`-recognized activity types as qualifying — not software convenience, but Holmes's own explicit restatement of what 1974 already implies by measuring the requirement in hours. |
| Moldvay — "after moving for 5 turns, the party must rest for 1 turn" | Exact discrete count | **Adopted for the number only.** Supplies "five" as the precise count 1974's ratio implies but never states. Moldvay's own wording is movement-specific; this card does **not** adopt that narrowing — the broader time-based scope comes from the OD&D/Holmes formulation above, and Moldvay's phrasing is treated as compatible with, not a correction of, that broader scope, since nothing in Moldvay contradicts non-movement activity also consuming dungeon time that counts toward the same hour. |
| Moldvay — "−1 to hit and −1 to damage until rest is taken" | Consequence of not resting | **Adopted as a Later Compatible D&D Completion**, not a Simulator Ruling. Does not contradict any explicit 1974 statement (1974 states no consequence at all) and directly, completely answers the historical silence. Its actual application is a combat-domain mechanic (`COMBAT-002`/`COMBAT-006`); `EXP-004` exposes the historical fact (`rest_overdue`) the combat domain needs, without implementing attack mechanics itself. See "Approved Mechanical Specification." |
| BECMI / Rules Cyclopedia — rule dropped entirely | Cadence, consequence | **Not adopted.** Removing an explicit-enough historical procedure is a revision by omission, not a compatible completion, per `SOURCE_HIERARCHY.md` §6. Its absence there is noted, not imported. |
| Wilderness pursuit-rest (p. 20) — doubled monster-check exposure (two dice, not one) during pursuit-related rest | Whether resting parties get an exception from `EXP-001` checks | **Not adopted directly** — different scale (wilderness day-turns) and different mechanism (extra dice, not extra dungeon turns). **Used only as corroborating context**: it shows this source's own design instinct, elsewhere in the same booklet, is to increase a resting party's exposure to wandering monsters after pursuit, never to suppress it — supporting the conclusion that ordinary `EXP-001` cadence continues unmodified during underworld rest turns. |

---

## Simulator Ruling

Historical research (above) fully resolves the cadence, its scope, and the consequence of not resting — none of those are Simulator Rulings in this card's final form. What remains is a small set of genuinely unsourced executable bookkeeping questions, each resolved below as the smallest sufficient proposal, now approved.

**Ruling A — Meaning of "motionless" (narrow).**
**Approved:** a qualifying rest turn must contain no spatial movement by the resting party. This card does not decide whether other non-movement activity (listening, searching, spellcasting, equipment handling, standing watch, or any future action) may be performed concurrently with a qualifying rest turn — those procedures may establish their own compatibility with rest when they are researched. `EXP-004` supplies only: qualifying rest → full required rest duration elapsed → no spatial movement during that credited interval. This is deliberately narrow so as not to prejudge procedures this card does not own. 1974 does not connect this rest turn to hit-point recovery (see "1974 Explicitly Establishes," item 6) — a directly sourced fact, not itself a ruling, and unchanged here.

**Ruling B — Voluntary/early rest.**
**Approved:** a voluntarily-taken rest turn that meets the same definition as a mandatory one (one full turn, motionless) satisfies and resets the cadence identically to a mandatory rest turn — 1974 gives no textual basis for treating "the same activity, taken slightly early" as mechanically different from the mandatory case. No separate "voluntary rest" activity type is introduced beyond what is needed to track whether an obligation existed beforehand; the completed rest's effect on state is identical either way.

**Ruling C — Doubled post-flight/pursuit rest: non-stacking, replacement semantics.**
**Approved:** the doubled (two-turn) requirement is triggered immediately when the flight/pursuit episode ends, and **replaces/satisfies** whatever ordinary rest debt is outstanding at that moment rather than stacking as an additional obligation:
- No ordinary debt, flight ends → exactly **2 turns** required.
- Ordinary 1-turn rest already due, flight ends → **2 turns** total, not 3.
- A second flight/pursuit episode occurs before the outstanding doubled rest is completed → the requirement remains **2 turns**, not 4.

1974 states a doubling relationship, not a compounding one, and no lineage source suggests otherwise; an additive/stacking model would be this card's own invention with no textual anchor.

**Ruling D — True pre-boundary interruption receives no fractional rest credit.**
**Approved, smallest sufficient proposal:** if some future mechanic (not designed by this card, and not reachable by the currently approved `EXP-001`/`EXP-002` architecture — see "Approved Mechanical Specification" for why an `EXP-001` check itself cannot cause this) interrupts a rest turn before it has fully elapsed, that incomplete interval earns no whole-rest-turn credit. No fractional/partial-credit mechanism is proposed. Time already consumed before such an interruption remains consumed according to `EXP-002`'s own accounting — it is not refunded or discounted. No historical source addresses this bookkeeping question, because it only arises when the rule is made executable; this is the smallest rule that avoids inventing a partial-credit system `AGENTS.md` §5 would flag as unnecessary complexity. The exact sources of such an interruption, beyond current Cluster 1 behavior, are outside this card's scope.

**Ruling E — Considered but rejected: cumulative/escalating fatigue.**
A natural-seeming extrapolation of the adopted Moldvay completion was explicitly considered and is explicitly **not adopted**: that repeated missed rests might accumulate — e.g., a second missed rest interval producing −2 to hit/damage instead of −1, or the ordinary rest requirement growing to two, three, or more owed turns the longer the party remains overdue. **This is a considered-but-rejected inference, not a historical finding.** The sourced material (Holmes, Moldvay) establishes a recurring rest requirement, a flat −1 to hit/−1 to damage consequence while required rest is not taken, and that the penalty lasts until rest is taken. It does not establish an additional penalty per subsequent missed interval, cumulative fatigue levels, cumulative ordinary rest-turn debt, or progressively longer recovery the longer the party remains overdue. Accumulating fatigue penalties or additional ordinary rest debt is intuitively plausible, but no historical rule establishes either behavior; adding them would extrapolate beyond the sourced mechanics, so the simulator preserves the stated flat penalty and single-turn rest requirement instead, regardless of how many additional qualifying non-rest turns elapse while overdue. This does not require a project-wide `DEC-XXXX` decision record — it is a Rule-Card-scoped interpretive restraint, not a durable architecture/process decision (`DEVELOPMENT_WORKFLOW.md` §9.2). **Provenance note:** the non-stacking behavior is not itself an explicit historical statement (no source says "the penalty does not stack") — it is the absence of a historical statement to the contrary, combined with this project's policy against inventing mechanics beyond the source (`AGENTS.md` §2). This record exists so a future developer does not mistake the non-stacking behavior for an accidental omission.

---

## Approved Mechanical Specification

**Scope.** This procedure determines: (a) when the recurring mandatory rest requirement becomes due and how it is satisfied, (b) how a flight/pursuit episode's doubled requirement interacts with it, (c) the historical fact (`rest_overdue`) the combat domain needs to apply the B/X penalty, and (d) how a rest turn's completion relates to `EXP-001`'s boundary check. It does not decide *whether* the party chooses to rest at any given non-mandatory moment (a player/referee decision), does not define hit-point recovery, and does not implement the −1 to-hit/damage penalty itself — that is the combat domain's responsibility, consuming the fact this card exposes.

**Dependencies:**

```text
EXP-002 (shared dungeon-time ledger, turn-elapsed signal)  ─┐
EXP-001 (wandering-monster check, consumes the same signal) ─┼─→  EXP-004 rest state
ENC-005 (flight/pursuit episode occurrence)                 ─┘

EXP-004 rest state  ─→  rest_overdue fact  ─→  combat domain (COMBAT-002/COMBAT-006,
                                                 applies −1 to hit, −1 to damage —
                                                 not implemented by this card)
```

`EXP-004` consumes `EXP-002`'s "dungeon turn elapsed" signal as one of its boundary consumers, exactly as `EXP-001` does — it does not depend on `EXP-001`'s own content, only on the same shared signal. It consumes "a flight/pursuit episode has just ended" as an external event from `ENC-005`, exactly as `EXP-002` already consumes "the party is in a flight/pursuit state" without resolving it. It produces, but does not consume, a `rest_overdue` fact for the future combat domain — this is a documented downstream dependency, and does not require the combat domain to exist before `EXP-004` itself can be implemented and tested.

**Minimum authoritative state:**

| State | Meaning |
|---|---|
| `qualifying_turns_since_rest` | Count of completed non-rest qualifying turns — every dungeon turn `EXP-002` attributes to any activity type (movement, search, listening, ESP, hiding, treasure-loading, combat, or any other turn-costed activity), per "1974 Explicitly Establishes," item 1 and Holmes's clarification — since the rest requirement was last satisfied. Incremented by each qualifying non-rest "dungeon turn elapsed" signal, but only while `rest_turns_required = 0` (see procedure below — this is what prevents ordinary debt from escalating past one required turn, and what prevents a hidden second cadence from accumulating while rest is outstanding). Reset to 0 whenever the rest requirement is fully satisfied. |
| `rest_turns_required` | 0 if no rest is currently outstanding; 1 if an ordinary rest is due; 2 if a doubled post-flight/pursuit rest is due (Ruling C). Set to 1 when `qualifying_turns_since_rest` reaches 5. Set to 2 (not added to any existing value) when a flight/pursuit episode ends (Ruling C). Decremented by one for each rest turn whose completed-turn boundary is reached while `rest_turns_required > 0` (see ordering below — a voluntary rest turn completed while `rest_turns_required = 0` does **not** decrement it further); unaffected by a true pre-boundary interruption (Ruling D). |
| `rest_overdue` | A separately tracked boolean — **not** fully derivable from `rest_turns_required` alone, because it depends on activity history, not just on whether an obligation currently exists. `false` from the moment a requirement first arises (ordinary or doubled) until the party begins a qualifying non-rest activity while that requirement remains outstanding, at which point it becomes `true`; reset to `false` the moment the outstanding requirement is fully satisfied (`rest_turns_required` reaches 0). This is the state the combat domain's −1 to-hit/−1 to-damage penalty (Compatibility Analysis) actually gates on — not `rest_due` alone. |

**Derived fact** (not separately stored): `rest_due := (rest_turns_required > 0)` — an obligation exists. This is distinct from `rest_overdue`: a requirement can be due without yet being overdue (the party has not yet had the chance, or has not yet chosen, to act while it was outstanding).

**Invariants:**

```text
rest_turns_required ∈ {0, 1, 2}
rest_overdue = true  →  rest_turns_required > 0
rest_turns_required = 0  →  rest_overdue = false
qualifying_turns_since_rest never decreases except by being reset to 0
```

No further state is proposed, and none of the following is introduced: an accumulated missed-rest count, a fatigue-level counter, hidden ordinary-rest debt beyond the single `rest_turns_required` value, or a deferred/second cadence counter. In particular, no separate state is proposed for "which specific activities occurred during a rest turn" (Ruling A does not require tracking this for `EXP-004`'s own accounting) or for counting stacked flight/pursuit episodes (Ruling C proposes exactly one outstanding doubled requirement, not a count of episodes). `rest_due` and `rest_overdue` are this card's own precise executable representation of the adopted historical sequence ("rest required → failure to rest → penalty until rest") — Moldvay's text does not itself use these labels, and they are not presented as historical text.

**Procedure — cadence and threshold, ordinary debt does not escalate:**

```text
WHEN EXP-002 emits a "dungeon turn elapsed" signal for a turn attributable to
qualifying non-rest activity (i.e., the elapsed turn was not itself a rest turn):

    IF rest_turns_required = 0:
        qualifying_turns_since_rest := qualifying_turns_since_rest + 1
        IF qualifying_turns_since_rest >= 5:
            rest_turns_required := 1
    ELSE:
        (rest is already due or overdue — further qualifying turns do not
         increase rest_turns_required beyond its current value; the ordinary
         requirement never grows past 1, per the human decision that overdue
         rest is a fixed condition, not an accumulating count of owed turns)
```

**Rest becoming overdue (Later Compatible D&D Completion — Moldvay B/X, adopted; supersedes the earlier hard-gate proposal, which is rejected).** Reaching the threshold makes rest *due*, not immediately *overdue* — the penalty is not applied merely because a requirement first arises:

```text
WHEN rest_turns_required transitions from 0 to a positive value
(either the ordinary threshold is reached, or a flight/pursuit episode ends):

    rest_overdue := false     -- a fresh, not-yet-overdue obligation

WHEN a qualifying non-rest dungeon activity begins while rest_turns_required > 0
(this includes combat beginning while an outstanding requirement exists):

    rest_overdue := true      -- set before that activity resolves

WHILE rest_overdue:
    the party MAY continue undertaking dungeon activity — no activity is blocked
    the historical fact rest_overdue = true is exposed to the combat domain
    the combat domain (not this card) applies −1 to hit and −1 to damage while
        rest_overdue remains true

WHEN rest_turns_required reaches 0 (the outstanding requirement is fully satisfied):
    rest_overdue := false
    qualifying_turns_since_rest := 0
```

If the party begins satisfying the required rest immediately upon it becoming due, `rest_overdue` never becomes `true` at all for that occurrence — the penalty is conditioned on skipping the rest, not on the rest merely being owed.

**Rest-boundary ordering and its relationship to `EXP-001` (corrects the earlier draft's inconsistency).** `EXP-002` only emits a "dungeon turn elapsed" signal once a full turn has actually elapsed on the shared ledger — the signal is a *consequence* of the turn having completed, not a gate that could still prevent it from having completed. `EXP-004` and `EXP-001` are both consumers of that same signal. Therefore, when a rest turn reaches its completed-turn boundary:

```text
rest interval completes
        ↓
rest credit is applied (EXP-004 state updates — see below)
        ↓
the normal completed-turn signal is available to boundary consumers
        ↓
EXP-001 performs its check
        ↓
a triggered encounter, if any, follows
```

not the reverse — a check performed at that same boundary cannot retroactively un-complete a rest turn that has already elapsed, because the check's own opportunity to fire is itself downstream of that same turn having elapsed. Concretely, **required** and **voluntary** rest turns are handled by distinct branches, so that a voluntary rest (taken while `rest_turns_required` is already 0) can never drive it negative:

```text
WHEN a rest turn reaches a completed-turn boundary through EXP-002's ordinary
accounting:

    IF rest_turns_required > 0:                       -- required rest turn
        rest_turns_required := rest_turns_required - 1
        IF rest_turns_required = 0:
            rest_overdue                := false        (fully satisfied)
            qualifying_turns_since_rest := 0             (cadence resets)
        -- rest_turns_required is never allowed to go below 0 --

    ELSE:                                              -- voluntary rest turn
        qualifying_turns_since_rest := 0
        -- rest_turns_required remains 0; rest_overdue remains false --

    -- only then does EXP-001 perform its normal check on this same signal --
    -- a resulting encounter does not undo the update above --
```

- **One-turn ordinary rest, encounter at the boundary:** the single required turn completes, `rest_turns_required` reaches 0, `rest_overdue` becomes false, the cadence resets — *then* `EXP-001` checks; if it triggers, the encounter follows, but the rest requirement remains satisfied.
- **Two-turn doubled rest, encounter after the first turn:** the first turn completes, `rest_turns_required` goes from 2 to 1 (that turn's credit is not lost; `rest_overdue` is unaffected by completing a rest turn itself). *Then* `EXP-001` checks; if it triggers an encounter and combat begins, that combat is a qualifying non-rest activity beginning while `rest_turns_required > 0` — so `rest_overdue` becomes `true` at that point (per "Rest becoming overdue" above), while `rest_turns_required` remains `1` (the first turn's credit is not erased). The still-outstanding second turn is a **true pre-boundary interruption of a not-yet-started rest turn** — it is not consumed (Ruling D: no fractional credit for time not yet spent) and remains required once it is safe to attempt again.
- **Activity undertaken while a requirement is outstanding is not banked toward the next cadence.** While `rest_turns_required > 0`, `qualifying_turns_since_rest` does not increment at all (see the cadence procedure above) — such time is simply not counted anywhere, not deferred or held for later credit. There is no hidden second cadence running underneath the outstanding requirement. Once the requirement is eventually satisfied, `qualifying_turns_since_rest` resets to exactly 0 and a fresh five-turn cadence begins with no memory of activity that occurred while overdue — regardless of how much qualifying activity that was (see "Deterministic Test Cases" for the twelve-turn illustration).
- **True pre-boundary interruption** (Ruling D) — a full rest turn interrupted *before* it reaches a completed-turn boundary at all, by some mechanic outside the currently approved `EXP-001`/`EXP-002` architecture — earns no credit, and whatever partial dungeon time was consumed before the interruption remains consumed under `EXP-002`'s own accounting (no refund, no fractional credit).

**Procedure — flight/pursuit doubled rest:**

```text
WHEN ENC-005 reports that a flight/pursuit episode has just ended:

    rest_turns_required := 2   (not added to any existing value — replaces/
                                 satisfies whatever ordinary debt was
                                 outstanding, per Ruling C)
    rest_overdue := false      (a fresh, not-yet-overdue obligation, even if
                                 the ordinary requirement it replaces had
                                 already become overdue — see "Rest becoming
                                 overdue" above)
```

**Integration with `EXP-001` and `EXP-002` (unmodified).** A rest turn — mandatory, voluntary, or doubled — is consumed through `EXP-002`'s ordinary accounting exactly like any other activity, and each whole turn it completes emits `EXP-002`'s normal "dungeon turn elapsed" signal, which `EXP-001` consumes exactly as it always does (1d6, trigger on 6). Neither `EXP-001`'s cadence nor `EXP-002`'s accumulation algorithm is modified by this card, no second dungeon-time ledger is introduced, and rest-boundary processing is not batched — it is resolved at each individual completed-turn boundary, consistent with `EXP-002`'s progressive model. A one-turn ordinary rest produces one `EXP-001` check opportunity; a two-turn doubled rest produces up to two sequential opportunities, the second contingent on the first not being interrupted. No exception to `EXP-001`'s cadence is created; wandering checks are never suppressed while resting.

**Multi-turn qualifying activity crossing the threshold.** Because `EXP-002` already resolves turn boundaries progressively and synchronously during an in-progress multi-turn activity, `EXP-004`'s cadence procedure is evaluated at each such boundary alongside `EXP-001`'s. Reaching the fifth qualifying turn mid-activity sets `rest_turns_required` to 1 at that boundary; `rest_overdue` remains `false` at that exact instant (the requirement has only just become due). Consistent with the adopted overdue-rest completion, this does **not** interrupt the in-progress activity — the party may continue. If the activity has further qualifying turns remaining beyond the one that crossed the threshold, each of those is itself a qualifying non-rest turn occurring while `rest_turns_required > 0`, so `rest_overdue` becomes `true` at the next such turn (per "Rest becoming overdue" above) and the combat-domain penalty condition, if applicable, follows from there.

**Survivability out of scope.** Consistent with `EXP-001`/`EXP-002`, this card specifies canonical historical rest accounting only. It must not accept a survivability policy, and no survivability policy may alter the cadence, the overdue-rest fact, or the doubled-rest rules, without a separately approved Rule Card or policy decision (`ARCHITECTURE.md` §10).

**No RNG owned by this card.** Like `EXP-002`, this procedure is purely state-tracking arithmetic; the only randomness in its vicinity belongs to `EXP-001`'s own check.

---

## Deterministic Test Cases

All cases are pure state-machine transitions; cases involving `EXP-001`'s own die roll use a controlled RNG for that portion only.

**Normal cadence:**

1. **Four qualifying turns → no rest due.** Four successive non-rest qualifying turns (any mix of activity types) → `qualifying_turns_since_rest = 4`, `rest_turns_required = 0`, `rest_due = false`, `rest_overdue = false`.
2. **Fifth qualifying turn → ordinary rest becomes due, but not yet overdue.** A fifth qualifying turn → `qualifying_turns_since_rest = 5`, `rest_turns_required = 1`, `rest_due = true`, `rest_overdue = false` — reaching the threshold alone does not set `rest_overdue`.
3. **Qualifying normal rest clears it.** From case 2, one uninterrupted rest turn reaching its completed-turn boundary → `rest_turns_required = 0`, `qualifying_turns_since_rest = 0`, `rest_due = false`, `rest_overdue = false`.

**Immediate required rest keeps the party non-overdue:**

4. **Resting immediately upon rest becoming due never sets `rest_overdue`.** From case 2, if the party begins the required rest turn next (rather than further qualifying activity) → `rest_overdue` remains `false` throughout, and completion proceeds as in case 3.

**Overdue behavior (Moldvay B/X completion):**

5. **Skipping rest sets `rest_overdue`.** From case 2, the party instead undertakes further qualifying non-rest activity → `rest_overdue` becomes `true` (set before that activity resolves), and the activity itself is not blocked.
6. **The combat-domain contract is exposed only once overdue, not merely once due.** While in the state from case 5, `rest_overdue` reads `true`, and the historical fact is available for a combat-domain consumer to apply −1 to hit and −1 to damage (not implemented by this card). Contrast with case 2/4, where `rest_due = true` but `rest_overdue = false` and the penalty condition is *not* exposed as active.
7. **Ordinary debt does not escalate, and no hidden second cadence accumulates.** From case 5, additional qualifying non-rest turns elapse before rest is taken → `rest_turns_required` remains `1` throughout (never 2, 3, ...), `rest_overdue` remains `true`, and `qualifying_turns_since_rest` does not increment further while `rest_turns_required > 0` — none of that additional activity is banked or deferred toward a future cadence.

**Explicit non-stacking illustration (twelve qualifying turns without resting):**

8. **The penalty and requirement stay flat regardless of how long rest is skipped.** From case 5, the party continues through a total of twelve qualifying non-rest turns without resting → `rest_due = true`, `rest_overdue = true`, the exposed combat-domain condition remains exactly −1 to hit / −1 to damage (not −2, not any escalated value), and `rest_turns_required` remains exactly `1` (not 2, 3, ... — confirming no accumulated missed-rest count or cumulative ordinary-rest debt exists).
9. **Completing one qualifying rest turn afterward clears everything at once.** Continuing case 8, the party completes one qualifying rest turn → `rest_turns_required = 0`, `rest_due = false`, `rest_overdue = false`, the combat-domain penalty condition is removed, and `qualifying_turns_since_rest = 0` — a single ordinary rest turn, not twelve turns' worth of accumulated debt.

**Rest does not create debt:**

10. **A completed qualifying rest is not counted as turn one of the next cadence.** Immediately after case 3, `qualifying_turns_since_rest = 0` — the completed rest turn itself is not counted toward the next five-turn cadence.

**Mixed activities:**

11. **Different activity types contribute to the same cadence.** A sequence of, e.g., two movement turns, one search turn, one combat turn, and one treasure-loading turn (five qualifying turns of mixed type) → `rest_turns_required` becomes 1, identically to five turns of a single activity type.

**Voluntary rest:**

12. **Voluntary rest cannot produce negative debt.** From `qualifying_turns_since_rest = 3`, `rest_turns_required = 0`, `rest_overdue = false` (below threshold, no rest due), a voluntarily-taken rest turn completes → `qualifying_turns_since_rest = 0`, `rest_turns_required` remains exactly `0` (never negative), `rest_overdue` remains `false` — exercising the branch of the completed-rest procedure that does not decrement an already-zero requirement.
13. **A fresh five turns are required afterward.** Following case 12, five new qualifying turns are required before `rest_turns_required` becomes 1 again — not two (i.e., the three pre-voluntary-rest turns do not carry over).

**Doubled rest:**

14. **No prior debt.** `rest_turns_required = 0` when a flight/pursuit episode ends → becomes `2`, `rest_overdue = false` (a fresh obligation).
15. **Prior ordinary debt already due (or overdue).** `rest_turns_required = 1` when a flight/pursuit episode ends → becomes `2`, not `3`, and `rest_overdue` resets to `false` regardless of whether the replaced ordinary requirement had already become overdue.
16. **Repeated episode before satisfaction.** A second flight/pursuit episode ends while `rest_turns_required` is already `2` (unsatisfied) → remains `2`, not `4`.

**Boundary encounter during ordinary rest:**

17. **Credited rest survives a boundary encounter.** A one-turn ordinary rest reaches its completed-turn boundary (`rest_turns_required` goes from 1 to 0, `rest_overdue` and `qualifying_turns_since_rest` reset) — *then* `EXP-001`'s check, using a scripted roll of 6, triggers an encounter → the ordinary rest requirement remains satisfied (`rest_turns_required = 0`, `rest_overdue = false`) despite the encounter.

**Boundary encounter during doubled rest (interruption sets `rest_overdue`, credit preserved):**

18. **First turn credited, second remains required, resulting combat sets `rest_overdue`.** A two-turn doubled rest's first turn reaches its completed-turn boundary (`rest_turns_required` goes from 2 to 1; `rest_overdue` unaffected by completing a rest turn) — *then* `EXP-001`'s check, using a scripted roll of 6, triggers an encounter and combat begins → `rest_overdue` becomes `true` (combat is qualifying non-rest activity beginning while `rest_turns_required > 0`), `rest_turns_required` remains `1` (not reset to 2 — the first turn's credit is preserved), and the combat-domain penalty condition is applicable for the duration.

**True pre-boundary interruption:**

19. **No whole-turn credit, no fractional credit, consumed time remains consumed.** A rest turn interrupted by a mechanism outside the currently approved `EXP-001`/`EXP-002` architecture, before reaching a completed-turn boundary → `rest_turns_required` is unchanged (no decrement), and whatever partial dungeon time `EXP-002` had already accounted for that turn remains consumed under `EXP-002`'s own ledger (not refunded).

**`EXP-002` integration (no second ledger, no batching):**

20. **Rest turns advance the single shared ledger like any other activity.** A rest turn's consumption produces exactly one `EXP-002` "dungeon turn elapsed" signal per whole turn completed, using the same accumulator `EXP-002` already defines — no separate rest-specific ledger, and no batching of a doubled rest's two boundaries into a single deferred update.

## Provenance Classification

**1974 Explicit**
- A recurring mandatory rest requirement exists, expressed in time ("one turn every hour"), not distance.
- A flight/pursuit episode doubles the required rest period.
- Hit-point recovery is governed by a separate day-granularity system, not this p. 8 passage.

**Later Compatible D&D Completion / Clarification**
- Holmes's explicit restatement, "one turn every hour / one turn out of every six" — the primary historical basis for reading the requirement as a general dungeon-time cadence rather than a movement-specific one.
- The exact discrete executable cadence, "five qualifying turns → one mandatory rest turn," from Moldvay's "after moving for 5 turns" — adopted for its numeric count; Moldvay's own movement-specific wording is not adopted for the *scope* of what counts (see Compatibility Analysis).
- Moldvay's −1 to hit / −1 to damage consequence for failing to rest, exposed by `EXP-004` as `rest_overdue` for the combat domain to apply.

**Necessary Mathematical / Mechanical Consequence**
- The approximate 1-rest-turn-per-6-turn ratio (from turn ≈ 10 minutes, hour ≈ 6 turns) — the arithmetic underlying the adopted cadence.
- A completed rest turn does not itself count as a qualifying non-rest turn of the next cadence — the direct consequence of the adopted six-turn cycle (5 qualifying + 1 rest = 6), not an independently invented rule.
- The doubled rest period equals two turns (already fixed by `EXP-002`).
- Ordinary rest debt does not escalate past one required turn — the fixed-condition (not accumulating-count) reading of "overdue," a direct consequence of treating the requirement as satisfiable by exactly one rest turn.
- A rest turn's completed-turn boundary is reached, and its credit applied, before `EXP-001`'s check on that same signal resolves — a direct consequence of `EXP-002`'s already-approved signal semantics (the signal is emitted only once the turn has elapsed), not an independent judgment call.
- The `rest_due`/`rest_overdue` state labels and their transition points are this card's own precise executable representation of the adopted historical sequence ("rest required → failure to rest → penalty until rest") — not Moldvay's own wording, and not presented as historical text.
- Entering a doubled post-flight/pursuit requirement resets `rest_overdue` to `false` — a fresh obligation, per the same "due is not yet overdue" logic applied uniformly to both the ordinary and doubled cases, not a separately invented exception.

**Simulator Ruling (approved)**
- Ruling A: "motionless" requires no spatial movement; this card does not decide compatibility with other concurrent non-movement activity.
- Ruling B: voluntary/early rest resets the cadence identically to mandatory rest, without driving `rest_turns_required` negative.
- Ruling C: doubled post-flight/pursuit rest replaces/satisfies ordinary debt and does not stack across repeated episodes.
- Ruling D: a true pre-boundary interruption (outside current Cluster 1 architecture) earns no whole or fractional rest credit; consumed time remains consumed.

**Considered but rejected (not adopted — recorded to prevent misreading the omission as accidental)**
- Ruling E: cumulative/escalating fatigue — an additional −1 penalty per subsequent missed rest interval, cumulative fatigue levels, cumulative ordinary rest-turn debt, or progressively longer recovery the longer the party remains overdue. None of this is established by Holmes or Moldvay; the flat −1 to hit/−1 to damage penalty and the fixed single-turn ordinary requirement are preserved exactly as sourced, regardless of how many qualifying non-rest turns elapse while overdue. This is a deliberate historical-preservation interpretation (not extrapolating beyond the sourced mechanics), not an independently sourced anti-stacking rule — no source states "the penalty does not stack."

**Out of scope for this card**
- The −1 to-hit/−1 to-damage penalty's actual mechanical application (`COMBAT-002`/`COMBAT-006`) — `EXP-004` exposes `rest_overdue`; it does not implement the penalty.
- Flight/pursuit state entry/exit triggers (`ENC-005`).
- Hit-point recovery / healing (a future downtime/healing Rule Card).
- Wilderness-scale rest and pursuit-rest procedures.
- What future mechanic, if any, could cause a true pre-boundary interruption (Ruling D fixes only its *consequence*, not its cause).

---

## Open Questions

None that block approval or implementation within this card's defined scope.

The following are informational, non-blocking notes for awareness:

1. **A new cross-domain relationship now exists between `EXP-004` and the combat domain** (`rest_overdue` → −1 to hit / −1 to damage), not previously reflected anywhere in `docs/rules/INVENTORY.md`. This does not require the combat domain to exist before `EXP-004` can itself be implemented and tested (the combat-domain consumption is a separate, later integration step) — see "Inventory Maintenance" for the narrow inventory note this creates.
2. **What future mechanic could cause a true pre-boundary interruption** (Ruling D) is not designed here and is not currently reachable by the approved `EXP-001`/`EXP-002` architecture; only the consequence, if one ever occurs, is fixed.

## Approval

- Approved by: Human project owner
- Date: 2026-08-16
- Notes: Approval incorporates the following human decisions made during review: (1) the recurring cadence is five qualifying non-rest dungeon turns → one mandatory rest turn → repeat, grounded in 1974's own hour-based (time, not distance) formulation and Holmes's explicit "one turn out of every six" clarification, with Moldvay supplying only the discrete count; (2) all `EXP-002`-recognized activity types count toward the cadence, for the historical reason above, not merely as a software-architecture necessity; (3) a completed rest turn does not itself create rest debt, and ordinary overdue rest is a fixed one-turn condition that does not escalate; (4) the proposed hard-gate enforcement is rejected in favor of the Moldvay B/X completion — rest becomes *due* without penalty, and only becomes *overdue* (activating the combat domain's −1 to-hit/−1 to-damage condition via `rest_overdue`) once the party undertakes qualifying non-rest activity while a requirement is outstanding, correcting the earlier draft's conflation of "due" and "overdue"; (5) "motionless" is narrowly defined as no spatial movement, without deciding compatibility with other concurrent activity; (6) voluntary early rest resets the cadence and, per this revision, is handled by a distinct state-transition branch that never drives `rest_turns_required` negative; (7) doubled post-flight/pursuit rest replaces rather than stacks with ordinary debt, resets `rest_overdue` to a fresh not-yet-overdue state, and does not compound across repeated episodes; (8) a rest turn's completed-turn boundary is credited before `EXP-001`'s check on that same signal resolves, so a resulting encounter cannot retroactively invalidate an already-completed rest turn, though it may interrupt a not-yet-started subsequent turn of a doubled rest and set `rest_overdue` if the resulting combat begins while the second turn remains outstanding; (9) a true pre-boundary interruption (outside current Cluster 1 architecture) earns no fractional rest credit; (10) a cumulative/escalating fatigue interpretation (additional penalty or additional owed rest turns for each further missed interval) was explicitly considered and rejected as an unsupported extrapolation beyond the sourced flat penalty and single-turn requirement, recorded in "Simulator Ruling" (Ruling E) so the non-stacking behavior is not later mistaken for an accidental omission.

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
