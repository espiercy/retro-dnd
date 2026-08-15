# Rule Card: Dungeon Turn / Time Accounting

---

## Rule ID

EXP-002

## Title

Dungeon Turn / Time Accounting

## Status

AWAITING_APPROVAL

## Rules Domain

exploration

---

## 1974 Source

Gygax, Gary, and Dave Arneson. *Dungeons & Dragons, Volume 3: The Underworld & Wilderness Adventures.* Lake Geneva, WI: Tactical Studies Rules, 1974.

- Section **"THE MOVE/TURN IN THE UNDERWORLD"** (p. 8) — the operative turn-definition passage this card specifies (referenced but not specified by `EXP-001`).
- **"EXAMPLE OF THE REFEREE MODERATING A DUNGEON EXPEDITION"**, worked play dialogue (pp. 13–14) — corroborating evidence for how the turn boundary behaves across mixed activity types (not itself a rules statement, but the source's own demonstration of the rule in use).
- Sample dungeon level, item 8 of the worked annotations (p. 5) — a further worked example of referee-adjudicated activity time-cost (pit-climbing).

**Verification method.** Consistent with `EXP-001`: a digitized reproduction of the booklet was retrieved and its text extracted directly (pypdf text extraction; poppler/pdftoppm unavailable in this environment), not recalled from memory or taken from a secondary paraphrase. Page numbers were cross-checked against the reproduction's own printed page-footer sequence and the established PDF-page-to-booklet-page offset used throughout this project's Vol. 3 research (`docs/rules/exploration/dungeon_wandering_monster_check.md` §"1974 Source"). No AD&D material was consulted.

**Exact source text (turn/move definition, p. 8):**

> "THE MOVE/TURN IN THE UNDERWORLD: In the underworld all distances are in feet, so wherever distances are given in inches convert them to tens of feet. Movement (distances given in Vol. 1) is in segments of approximately ten minutes. Thus it takes ten minutes to move about two moves — 120 feet for a fully-armored character. Two moves constitute a turn, except in flight/pursuit situations where the moves/turn will be doubled (and no mapping allowed). Time must be taken to rest, so one turn every hour must be spent motionless, and double the rest period must be taken after a flight/pursuit takes place. Time spent searching for anything (secret passages, hidden treasure, etc.), loading treasure, listening, ESP'ing, hiding, will be adjudged by the referee as to what portion of a turn will be used by the activity. Typically, ESP'ing will take but a quarter turn, while searching a ten foot section of wall for secret passages will require a full turn. Melee is fast and furious. There are ten rounds of combat per turn."

**Exact source text (worked example, pp. 13–14):**

> "Listen at the door — three of us. (After rolling three dice) You hear nothing. (At this time a check for wandering monsters is also made.)"
>
> "...This will require; four turns. (Ho checks for monsters wandering in, and on the forth try one is indicated. However, as there was a listener at the door it is approaching, he also checks to see if it is detected, allowing a good probability that it will be heard.) As you complete your loading..."

**Exact source text (worked example, p. 5):**

> "Falling into the pit would typically cause damage if a 1 or a 2 were rolled. Otherwise, it would only mean about one turn of time to clamber out, providing the character had spikes or associates to pull him out..."

## 1974 Explicitly Establishes

1. **Turn length.** A dungeon turn is "approximately ten minutes" of game time (p. 8).
2. **Movement/turn conversion.** "Two moves constitute a turn" (p. 8) — an explicit, stated ratio, not a derived one. Ten minutes of movement time corresponds to about two moves, i.e. 120 feet for a fully-armored character (p. 8) — the specific feet-per-move *rate* underlying this figure, and how it varies by encumbrance, is `CHAR-005`'s concern and is not re-derived here; this card takes only the *turn-cost ratio* ("two moves per turn") from the passage.
3. **Flight/pursuit modifier.** During flight/pursuit, the moves/turn ratio is explicitly doubled, and mapping is explicitly disallowed during that state (p. 8). The following rest period is explicitly doubled as well ("double the rest period must be taken after a flight/pursuit takes place," p. 8). **What triggers or ends a flight/pursuit state is not specified here** — that is `ENC-005`'s (Retreat, Pursuit & Evasion) concern. This card treats "the party is in a flight/pursuit state" as an external boolean input it does not itself resolve.
4. **Rest requirement.** "One turn every hour must be spent motionless" (p. 8) — an explicit, mandatory, recurring rest cost. **Whether/when rest is actually taken, and any consequence of skipping it, is not specified here** — that is `EXP-004`'s concern (see "Dependencies" below).
5. **Search, listening, ESP, hiding, and treasure-loading are turn-costed, referee-adjudicated activities**, explicitly described as an open-ended category ("will be adjudged by the referee as to what portion of a turn will be used by the activity," p. 8) — not a closed enumeration. Two specific numeric examples are given directly in the text: ESP'ing "will take but a quarter turn"; searching a ten-foot section of wall for secret passages "will require a full turn" (p. 8).
6. **The open-ended adjudication category extends to activities beyond the five named in the p. 8 passage.** The pit-climbing worked example (p. 5) assigns "about one turn" to clambering out of a pit — an activity not among the five named on p. 8 — using the same "referee adjudges a portion of a turn" principle. This is explicit corroboration that the p. 8 list (search, load treasure, listen, ESP, hide) is illustrative, not exhaustive.
7. **Multi-turn bulk activities receive a referee-declared whole-turn cost, not a fractional one.** The worked example's treasure-loading activity is assigned a flat cost of "four turns" by the referee before it proceeds (pp. 13–14), rather than being timed incrementally piece by piece.
8. **Combat/turn conversion.** "There are ten rounds of combat per turn" (p. 8) — an explicit, stated ratio. The absolute real-world duration of a single round is not stated anywhere in this source and is out of this card's scope (see "1974 Leaves Undefined," item 4, and "Dependencies").
9. **The wandering-monster check (`EXP-001`) fires once per elapsed turn regardless of which activity consumed that turn**, not only after movement. The worked example shows the check firing after a *listening* action (p. 13: "At this time a check for wandering monsters is also made"), and shows it firing once per turn, repeatedly, across a single sustained non-movement activity — the referee performs one check per turn of the four-turn treasure-loading activity, with the triggering result occurring "on the forth try" (p. 14). This directly corroborates `EXP-001`'s "at the end of every turn" reading (`dungeon_wandering_monster_check.md`, "1974 Explicitly Establishes" item 1) and extends it: the boundary is activity-agnostic, and a single continuous activity spanning multiple turns produces one check per turn crossed, not one check for the whole activity.

## 1974 Leaves Undefined

1. **Cross-activity-type accumulation.** The text assigns a turn-fraction cost to individual activities (a move, a search, an ESP attempt, a rest period) but never states a general rule for how fractional costs from *different* activity types combine into a single running count of elapsed turns. For example: does a half-turn move followed by a quarter-turn ESP attempt followed by another quarter-turn ESP attempt total to exactly one elapsed turn (triggering one `EXP-001` check), or is each activity type tracked and rounded independently? No passage states this. This is the central gap this card must resolve or explicitly flag (see "Simulator Ruling").
2. **Threshold/rounding semantics.** Every numeric example the source gives (half turn per move, quarter turn for ESP, full turn for a wall search, four turns for a bulk load) is a "clean" value. The text never addresses what happens when an accumulating running total would land at a non-clean value, or exactly *when*, relative to crossing a whole-turn boundary, the "turn has elapsed" event is considered to fire.
3. **Combat ending before all ten rounds are used.** The text states the ratio "ten rounds of combat per turn" but never addresses what happens to turn-accounting if combat resolves (all opponents fled, defeated, or the party withdraws) before all ten rounds elapse: does the encounter still consume a full turn, does it consume a proportional fraction (e.g., four of ten rounds = 0.4 turn) carried forward with other activity, or something else? No passage states this.
4. **Absolute real-world duration of a single combat round.** The 10-minute turn and the 10-rounds-per-turn ratio together invite an arithmetic inference of "one minute per round," but the source never states a round's duration directly, and (per Completion Research below) later sources do not agree on this figure. This card does not need it — only the round-to-turn *ratio* matters for turn accounting — and treats it as out of scope, belonging to a future combat-timing card (`COMBAT-006`, per `docs/rules/INVENTORY.md`).
5. **Whether the worked example's listening-triggers-a-check moment is caused by listening itself, or by listening completing a turn that preceding movement had already partly filled.** The worked dialogue narrates several segments of corridor movement (10', 20', 30', etc.) before the listening action that immediately precedes a check. Read one way, this is fully explained by ordinary turn accounting: the preceding movement already used most of a turn, and the listening action's fractional cost was what crossed the boundary. Read another way, the example could be (loosely) illustrating that any discrete referee-adjudicated action is itself treated as boundary-crossing. The source does not disambiguate which reading is intended, and this card does not resolve it by fiat — it is noted as an interpretive uncertainty in the corroborating evidence itself, distinct from the accumulation-algorithm gap in item 1, and is addressed by adopting a single coherent accumulation model that is *consistent* with the worked example without depending on which reading is "true" (see "Approved Mechanical Specification").

---

## Completion Research

Because 1974 leaves the items above undefined, the non-AD&D D&D lineage was researched in the order given in `SOURCE_HIERARCHY.md` §3, per the hybrid research approach (`SOURCE_HIERARCHY.md` §8), treating this as a consequential ambiguity warranting deeper-than-usual lineage research rather than stopping at the first available later algorithm.

**Holmes Basic D&D (1977).** Verified via `WebFetch` against a specialist secondary source (Zenopus Archives, "Turns in Holmes Basic," a blog dedicated to page-level verification of Holmes-era text). Findings:
- Holmes closely paraphrases OD&D's own turn structure: 10-minute exploration turns, two moves per turn, 120 feet baseline movement — consistent with, and adding nothing beyond, the 1974 text already in hand.
- Holmes introduces an explicit **separate duration for a "combat turn"**: ten rounds of ten seconds each (~100 seconds), distinct from the 10-minute exploration turn. This is not a simple restatement of OD&D's ratio — it resolves the round-duration question OD&D leaves open (see "1974 Leaves Undefined," item 4), but does so by giving combat time a *different* absolute duration than exploration time, which OD&D's text does not itself suggest.
- Directly verified: the source **does not address** cross-activity-type accumulation of partial turns ("the post does not explicitly address how searching, listening, or other activities combine toward a full turn"), and **does not address** exactly when a turn is considered complete for the purpose of firing boundary procedures. Holmes does not close this card's central gap (item 1).

**B/X D&D — Moldvay Basic (1981) / Cook Expert.** Findings (via `WebSearch`, cross-checked against the structure of the Holmes findings above; not independently opened page-by-page, flagged below):
- Confirms the same 10-minute exploration turn and 120 feet/turn baseline movement, adding no new information for this card's needs.
- States a rest requirement of "1 turn for every 5 explored" — i.e., a 6-turn cycle (5 active + 1 rest). This is numerically identical to the ratio implied by OD&D's own "one turn every hour" (a turn ≈ 10 minutes, so an hour ≈ 6 turns, of which the stated 1 is rest, leaving 5). See "Compatibility Analysis."
- States that wandering-monster checks are made **"every two turns,"** not every turn. This directly contradicts the explicit 1974 text ("at the end of every turn," `EXP-001` p. 10) and is the same later convention `EXP-001` already identified and rejected. It is rejected again here, explicitly, for the same reason.
- No accumulation algorithm across mixed activity types was found in this source either.

**B2, *The Keep on the Borderlands* (Gygax, TSR, c. 1979–1980).** A Basic-D&D-compatible module, authored by one of the 1974 game's co-authors, within the Holmes/B-X lineage `SOURCE_HIERARCHY.md` permits for compatible completion. Found via `WebFetch` of the Zenopus Archives "Turns in Holmes Basic" post, which quotes it directly with a page citation:

> "For the sake of convenience, a DM can consider one entire melee turn to equal one normal turn (that is, 10 minutes), no matter how many melee rounds the combat took." (B2, p. 4, as quoted by Zenopus Archives)

This directly addresses the combat-ending-early gap (item 3 above). **Verification caveat:** this quote was not independently confirmed against the primary B2 text — a direct fetch of the B2 PDF (via two independent hosts) failed at the network layer in this environment, and the alternative Zenopus Archives page dedicated specifically to B2 does not repeat this quote. The citation rests on a single specialist secondary source with a specific page attribution, not on this agent's own reading of the primary text. This is flagged explicitly for human attention below and in the Simulator Ruling section — it is presented as the leading completion candidate, not as settled fact.

## Compatibility Analysis

| Source | Addresses | Judgment |
|---|---|---|
| Holmes — combat-turn as separate ~100-second unit | Round-duration gap (item 4) | **Not adopted.** Not needed for this card's scope (only the round-to-turn *ratio* matters here; absolute round duration belongs to `COMBAT-006`), and adopting a second, shorter real-time duration for "turn" during combat is an avoidable complication `EXP-002` does not need to take on. Not judged incompatible with 1974 — judged unnecessary. |
| B/X — "1 turn rest per 5 explored" | Rest-cadence gap | **Adopted as corroboration**, not as new information. It independently reproduces the same 6-turn cycle implied by OD&D's own "one turn every hour" statement once a turn is taken as ≈10 minutes. Because it is arithmetically identical to what 1974's own numbers already imply, this is treated as a compatible restatement, not a revision — it does not change the ratio, it confirms this card's mathematical reading of it is the one the D&D lineage actually continued to use. |
| B/X — wandering check "every two turns" | Turn-boundary/check-firing cadence | **Rejected**, explicitly and for the second time in this project. Contradicts the 1974 text's "at the end of every turn," which `EXP-001` already established and this card does not reopen. Per `SOURCE_HIERARCHY.md` §6, a later source that contradicts explicit 1974 procedure is a revision, not a compatible completion, and is excluded. |
| B2 — combat consumes exactly one normal turn regardless of rounds used | Combat-ending-early gap (item 3) | **Proposed completion, not yet adopted.** Does not contradict any explicit 1974 statement (it is a natural, convenience-motivated rounding of the explicit 10-rounds-per-turn ratio for the case where fewer than ten rounds are used, rather than a revision of it). It does introduce a new assumption 1974 itself does not state: that partial combat rounds up to a full turn rather than contributing a proportional fraction. Because this is a specific, consequential mechanical choice — not a case where the later text merely restates 1974's own arithmetic — it is routed to "Simulator Ruling" for explicit human decision rather than silently folded into the specification, and its citation chain (see verification caveat above) should be independently checked before that decision is finalized. |

---

## Simulator Ruling

Two decisions are required because no combination of 1974 and compatible later sources fully resolves them. Both are presented as **proposed** rulings for human decision — this card does not self-approve them.

**Ruling 1 (required) — Cross-activity-type accumulation model.**
No source, 1974 or later, states a general rule for combining turn-fractions from different activity types into a single elapsed-turn count. *Proposed:* a single running accumulator, scoped per exploring party, that adds each activity's turn-cost (as defined by the per-activity-type table in the Mechanical Specification below) regardless of activity type, and fires one "turn elapsed" event each time the running total reaches or passes a whole integer, carrying any remainder forward. This is not stated by any source; it is proposed because it is the simplest model consistent with the worked-example evidence (item 9 under "1974 Explicitly Establishes") without requiring a decision about which of the two readings in "1974 Leaves Undefined" item 5 is correct — under this model, both readings produce the same observable behavior. This is **not** an action-point system: it tracks a single scalar quantity (elapsed-turn fractions), not discrete spendable actions, and it does not introduce any new gameplay affordance (no activity's stated cost is changed by this ruling).

**Ruling 2 (required, pending citation verification) — Combat ending before ten rounds.**
*Proposed:* adopt the B2 completion — a combat encounter, once triggered, consumes exactly one full turn for time-accounting purposes regardless of how many of the ten rounds were actually used. *Rejected alternative:* proportional accounting (e.g., 4 of 10 rounds = 0.4 turn contributed to the accumulator), which was considered but not adopted as the default proposal because no source — 1974 or later — describes it; it would be this card's own invention of a finer-grained model than any historical source uses. The B2 rule is preferred because it has an actual (if imperfectly verified) historical precedent and is simpler to implement and reason about. **This ruling should not be finalized until the B2 citation is independently verified against the primary text** (see "Completion Research" verification caveat).

Both rulings are reflected in the Mechanical Specification below, each clause tagged with its provenance so that a human reviewer can accept, reject, or amend either independently of the other.

---

## Approved Mechanical Specification

*(Presented in pre-approval draft form — see "Simulator Ruling." Not authoritative until a human sets this card's Status to `APPROVED`, per `AGENTS.md` §2.)*

**Scope.** This procedure defines what a dungeon turn is, how turn-costed activities accumulate into a count of fully elapsed turns, and when a "qualifying dungeon-turn interval has elapsed" signal (`EXP-001`'s stated dependency) fires. It does not decide *whether, when, or why* any particular activity occurs — movement destination selection, the decision to rest, the decision to search, combat resolution, and treasure-loading decisions are all owned by other procedures (`EXP-003`, `EXP-004`, `EXP-005`, combat domain, etc.). This card is consumed by those procedures; it does not consume them.

**Dependencies:**

```text
CHAR-005 (movement rate)  ─┐
EXP-004 (resting procedure)─┤
EXP-005 (search/listen)    ─┼─→  activity + its turn-cost  ─→  EXP-002 accumulator  ─→  "turn elapsed" signal(s)  ─→  EXP-001
combat domain (round count)─┤
ENC-005 (flight/pursuit)   ─┘
```

`EXP-002` does not depend on any of these procedures' own mechanical content (what a search roll's odds are, when resting is triggered, etc.) — it only needs to be told, by whichever procedure decided an activity occurred, what turn-cost that activity carries. The integration direction with `EXP-001` is one-way, as already established by `CLUSTER-001-dungeon-exploration-time.md` §5: `EXP-002` produces a signal `EXP-001` consumes; `EXP-002`'s own content does not depend on `EXP-001`.

**Per-activity-type turn-cost table** (open-ended; the referee/simulator may assign a cost to an activity type not listed, per item 6 under "1974 Explicitly Establishes"):

| Activity | Turn-cost | Provenance |
|---|---|---|
| One move (per the movement-rate procedure, `CHAR-005`) | 1/2 turn | Necessary mathematical consequence of "two moves constitute a turn" (1974 Explicit ratio) |
| One move, while in a flight/pursuit state | 1/4 turn (ratio doubled) | 1974 Explicit |
| ESP attempt | 1/4 turn | 1974 Explicit (named example) |
| Searching a ten-foot wall section for secret passages | 1 turn | 1974 Explicit (named example) |
| Listening at a door | Referee/simulator-adjudicated fraction (no numeric example given) | 1974 Explicit (open-ended category); specific value is a Simulator Ruling if a fixed value is wanted, or left to case-by-case adjudication if not — **not resolved by this card** |
| Hiding | Referee/simulator-adjudicated fraction | 1974 Explicit (open-ended category); no numeric example given — same treatment as listening |
| Loading treasure (small scale) | Referee/simulator-adjudicated fraction | 1974 Explicit (open-ended category) |
| Loading treasure (bulk, as in the worked example) | Whole-number of turns, assigned as a block before the activity proceeds | 1974 Explicit, via worked example (item 7) |
| Rest | 1 turn (2 turns if following a flight/pursuit state) | 1974 Explicit |
| Ad hoc referee/simulator-adjudicated activity (e.g., climbing out of a pit) | Referee/simulator-adjudicated fraction or whole number | 1974 Explicit (open-ended category, corroborated by the pit-climbing worked example) |
| Combat, resolved using all ten rounds | 1 turn | Necessary mathematical consequence of "ten rounds of combat per turn" (1974 Explicit ratio) |
| Combat, resolved before all ten rounds are used | 1 turn (full turn regardless of rounds actually used) | **Proposed D&D Completion (Simulator Ruling 2, pending citation verification)** — not 1974-explicit |

**Accumulation algorithm** (Simulator Ruling 1 — proposed, not yet human-approved):

```text
STATE: accumulated_turns  (a non-negative rational/decimal value, initialized to 0 at the
                            start of a dungeon expedition; scoped to the exploring party)

WHEN an activity with turn-cost C completes:
    accumulated_turns := accumulated_turns + C
    WHILE accumulated_turns >= 1:
        accumulated_turns := accumulated_turns - 1
        EMIT "qualifying dungeon-turn interval has elapsed"   (consumed by EXP-001)
```

The `WHILE` (not `IF`) is deliberate: it reproduces the worked example's four-turns-four-checks behavior (a single bulk activity with a multi-turn cost fires one signal per whole turn it completes, in sequence — "1974 Explicitly Establishes," item 9) without requiring the bulk activity to be artificially decomposed into four separate 1-turn activities by whatever procedure invokes this card.

**Non-discretionary application.** Every turn-costed activity contributes to the same accumulator, regardless of type — movement, rest, search, listening, ESP, hiding, treasure-loading, and combat are not tracked on separate counters. This is what "1974 Leaves Undefined" item 1 identifies as unstated by the source; it is adopted here as Simulator Ruling 1, and a human reviewer may substitute a different model (e.g., per-activity-type counters) if they judge the evidence differently.

**Output.** Each invocation of the activity-completion step emits zero or more "turn elapsed" signals (zero if the activity's cost did not complete a turn; one or more per the `WHILE` loop otherwise). Each signal carries no data beyond the fact of a turn having elapsed — consistent with `EXP-001`'s own output contract, which "carries no data beyond the fact of triggering." This card does not decide what else, if anything, happens when a turn elapses beyond firing this signal (light-source consumption, `EXP-006`, is a separate consumer of the same signal and is out of scope here).

**No RNG.** This procedure is purely arithmetic. It performs no die rolls and must not be given its own RNG stream (`ARCHITECTURE.md` §5, `AGENTS.md` §7) — the only randomness in this card's vicinity belongs to the procedures that decide activity *outcomes* (e.g., `EXP-001`'s own check), not to this card's accounting.

**Survivability out of scope.** Consistent with `EXP-001`, this card specifies canonical historical time accounting only. It must not accept a survivability policy, and no survivability policy may alter turn-costs or the accumulation algorithm, without a separately approved Rule Card or policy decision (`ARCHITECTURE.md` §10).

---

## Deterministic Test Cases

All cases are pure-arithmetic and require no RNG double, unlike `EXP-001`'s tests.

1. **Single half-turn move, no signal.** One move (cost 1/2 turn) → accumulator = 0.5, zero "turn elapsed" signals.
2. **Two half-turn moves complete a turn.** Two successive moves (1/2 + 1/2) → accumulator returns to 0, exactly one "turn elapsed" signal.
3. **Mixed-activity-type accumulation (tests Simulator Ruling 1 directly).** One move (1/2) + one ESP attempt (1/4) + a second ESP attempt (1/4) → totals exactly 1.0 → exactly one signal, accumulator resets to 0. This is the case that distinguishes the proposed cross-activity-type model from a per-activity-type-counter alternative; it should be revisited if a human reviewer selects a different model for Ruling 1.
4. **Full-turn activity from zero.** A ten-foot wall search (cost 1 turn) starting from accumulator = 0 → exactly one signal.
5. **Multi-turn bulk activity fires multiple signals in sequence.** A single treasure-loading activity with a declared cost of 4 turns → exactly four "turn elapsed" signals from one activity-completion call, accumulator returns to 0 — directly reproducing the worked example's "four turns... on the forth try" behavior.
6. **Rest, standard.** One rest activity (cost 1 turn) → exactly one signal.
7. **Rest, doubled after flight/pursuit.** One rest activity flagged as following a flight/pursuit state (cost 2 turns) → exactly two signals from one activity-completion call.
8. **Movement during flight/pursuit.** One move flagged as occurring during a flight/pursuit state (cost 1/4 turn, per the doubled ratio) → accumulator = 0.25, zero signals; four such moves → exactly one signal.
9. **Combat, full ten rounds.** A combat activity resolved using all ten rounds (cost 1 turn) → exactly one signal.
10. **Combat, ending early — depends on Ruling 2.** A combat activity ending after fewer than ten rounds. *If Ruling 2 is approved as proposed:* cost = 1 turn regardless of rounds used, identical outcome to case 9. *If a human reviewer instead selects proportional accounting:* cost = (rounds used / 10) turn, contributing a fraction to the shared accumulator like any other partial-turn activity. This test case's expected result is explicitly conditional on which ruling is approved and must not be finalized until that decision is made.
11. **Threshold exactness — lands exactly on a boundary.** An activity sequence whose total lands at exactly 1.0 (not past it) fires exactly one signal, not zero and not two — verifies the `>=` threshold in the accumulation algorithm is correctly inclusive.
12. **Carry-forward correctness past a single boundary.** An activity costing more than 1 turn in a single step (e.g., a hypothetical 1.5-turn cost) fires exactly one signal and leaves exactly 0.5 accumulated afterward — verifies the remainder is preserved rather than discarded or causing a second premature signal.
13. **No RNG dependency.** The accumulation procedure can be exercised through an arbitrary sequence of activity-completion calls with no RNG double (or an RNG double that raises on any call) supplied at all, and still produces correct signal counts — proving this card introduces no hidden randomness.
14. **Paired integration contract with `EXP-001`.** Given a scripted sequence of activities whose combined cost is known to complete exactly *N* whole turns, invoking `EXP-001`'s check procedure once per emitted signal results in exactly *N* checks, each consuming exactly one RNG operation — the mirror image of `EXP-001`'s own existing "Turn-dependency integration contract" test, confirming both ends of the `EXP-002` → `EXP-001` integration point agree on signal count.

## Provenance Classification

This card is provenance-mixed; no single category from `GAME_CONSTITUTION.md` §5 applies to it as a whole. Per-clause breakdown:

| Clause | Classification |
|---|---|
| Turn ≈ 10 minutes | 1974 Explicit |
| Two moves = one turn | 1974 Explicit |
| One move = 1/2 turn (uniform per-move cost) | Necessary mathematical consequence of an explicit ratio |
| Flight/pursuit doubles moves/turn and doubles following rest | 1974 Explicit |
| Rest = 1 turn/hour | 1974 Explicit |
| Rest operationalized as a ~1-in-6-turn cadence | Necessary mathematical consequence; corroborated (not established) by B/X's independent "1 per 5 explored" — D&D Completion, corroborating only |
| Search/listen/ESP/hide/load-treasure are turn-costed, open-ended, referee-adjudicated | 1974 Explicit |
| ESP = 1/4 turn; 10-ft wall search = 1 turn | 1974 Explicit (named examples) |
| Ad hoc activities (e.g., pit-climbing) also referee-adjudicated | 1974 Explicit (via worked example) |
| Bulk activities receive a whole-turn cost declared up front | 1974 Explicit (via worked example) |
| Ten rounds of combat = one turn | 1974 Explicit |
| Wandering check fires once per elapsed turn, any activity type, including mid-bulk-activity | 1974 Explicit (via worked example); reaffirms `EXP-001` |
| Cross-activity-type accumulation into one running total | **Simulator Ruling (proposed, unresolved)** |
| Whole-turn threshold/rounding semantics (`>=` firing, remainder carry-forward) | **Simulator Ruling (proposed, unresolved)** |
| Combat ending early consumes exactly one full turn regardless of rounds used | **D&D Completion (proposed, via B2 — pending citation verification), not yet a ruling** |
| Absolute real-world duration of a single combat round | Out of scope for this card (`COMBAT-006`) — not classified here |

---

## Open Questions

1. **Simulator Ruling 1 (cross-activity-type accumulation) requires a human decision before this card can be `APPROVED`.** See "Simulator Ruling." No compatible historical source resolves it; a specific proposal is given, but this card does not self-approve it.
2. **Simulator Ruling 2 (combat ending before ten rounds) requires both a human decision and independent verification of the B2 citation before this card can be `APPROVED`.** The current citation rests on a single secondary source (Zenopus Archives quoting B2 p. 4); a direct fetch of the primary B2 text failed in this environment and should be retried, or the module consulted directly, before finalizing.
3. **Fixed numeric turn-costs for listening and hiding are not given by 1974** (only the open-ended "referee adjudges" clause). This card leaves them adjudicated rather than assigning arbitrary fixed fractions, consistent with not inventing mechanics the source does not state. A human reviewer may wish to assign fixed values for implementation convenience; that would itself be a further Simulator Ruling, not addressed here.
4. **Combat round's absolute real-world duration** is explicitly out of scope for this card and is flagged for `COMBAT-006` (`docs/rules/INVENTORY.md`), which already carries a historically-high-risk flag pending research into *Chainmail*'s relationship to D&D's turn structure. This card does not depend on that answer.
5. **Flight/pursuit state boundaries** (what triggers entry into or exit from a flight/pursuit state) are not resolved here and belong to `ENC-005` (Retreat, Pursuit & Evasion). This card only consumes that state as an external boolean input to the movement/rest cost table.

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
