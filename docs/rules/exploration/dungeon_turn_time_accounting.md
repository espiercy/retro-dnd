# Rule Card: Dungeon Turn / Time Accounting

> **Migration note (2026-08-16).** Previously approved under the superseded 1974-primary source policy. Requires Rules Cyclopedia revalidation before implementation authority is restored (`DEC-0007-rules-cyclopedia-primary-rules-authority.md`, `DEVELOPMENT_WORKFLOW.md` §9.7). This does not indicate the research below was incorrect — only that it has not yet been reviewed against the current source hierarchy. All content below is preserved unchanged as the historical research and approval record; it is not rewritten by this migration. See `docs/rules/RULESET_BASELINE_MIGRATION.md`.
>
> Prior approval record: Approved by Human project owner, 2026-08-16, under the then-governing 1974-primary source policy — see this card's own "Approval" section below, preserved unchanged.

---

## Rule ID

EXP-002

## Title

Dungeon Turn / Time Accounting

## Status

REVALIDATION_REQUIRED

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
7. **The worked treasure-loading example demonstrates, narrowly, that a single activity may span multiple turns, and that wandering-monster checks occur during those turns while the activity is still in progress** (pp. 13–14: "This will require; four turns... on the forth [fourth] try one is indicated"). This is stated narrowly and deliberately: the source demonstrates *this one adjudicated instance* costing four turns, and demonstrates checks occurring turn-by-turn while it runs. It does **not**, by itself, establish a general historical procedure that every multi-turn bulk activity must be assigned a whole-number cost or must always be declared fully in advance before it begins — that broader claim is not supported by a single worked example and is not asserted here (see "1974 Leaves Undefined," item 3, and the corrected treatment in "Approved Mechanical Specification").
8. **Combat/turn conversion.** "There are ten rounds of combat per turn" (p. 8) — an explicit, stated ratio. The absolute real-world duration of a single round is not stated anywhere in this source and is out of this card's scope (see "1974 Leaves Undefined," item 5, and "Dependencies").
9. **The wandering-monster check (`EXP-001`) fires once per elapsed turn regardless of which activity consumed that turn**, not only after movement. The worked example shows the check firing after a *listening* action (p. 13: "At this time a check for wandering monsters is also made"), and shows it firing once per turn, repeatedly, across a single sustained non-movement activity — the referee performs one check per turn of the four-turn treasure-loading activity, with the triggering result occurring "on the forth try" (p. 14). This directly corroborates `EXP-001`'s "at the end of every turn" reading (`dungeon_wandering_monster_check.md`, "1974 Explicitly Establishes" item 1) and extends it: the boundary is activity-agnostic, and — most significantly for this card's mechanical specification — the check is performed *while the loading activity is still under way*, not held back and batch-fired only once the whole four-turn activity concludes. This is the specific textual basis for the progressive (not batch) boundary-resolution model adopted below.

## 1974 Leaves Undefined

1. **Cross-activity-type accumulation.** The text assigns a turn-fraction cost to individual activities (a move, a search, an ESP attempt, a rest period) but never states a general rule for how fractional costs from *different* activity types combine into a single running count of elapsed turns. Resolved by Simulator Ruling — see "Simulator Ruling" below.
2. **Threshold/rounding semantics.** Every numeric example the source gives (half turn per move, quarter turn for ESP, full turn for a wall search, four turns for a bulk load) is a "clean" value. The text never addresses what happens when an accumulating running total would land at a non-clean value, or exactly *when*, relative to crossing a whole-turn boundary, the "turn has elapsed" event is considered to fire. Resolved by Simulator Ruling — see "Simulator Ruling" below.
3. **Whether bulk multi-turn activities must always be pre-declared as a whole-number cost.** The worked treasure-loading example shows one such instance; the source does not generalize it into a procedure (see "1974 Explicitly Establishes," item 7). Not resolved as a general rule by this card; the mechanical specification below deliberately avoids relying on a pre-declared-whole-turn assumption.
4. **Combat ending before all ten rounds are used, and combat exceeding ten rounds.** The text states the ratio "ten rounds of combat per turn" but never addresses what happens to turn-accounting if combat resolves before all ten rounds elapse, or continues past ten. Resolved via later compatible D&D completion — see "Completion Research," "Compatibility Analysis," and "Approved Mechanical Specification" below.
5. **Absolute real-world duration of a single combat round.** The 10-minute turn and the 10-rounds-per-turn ratio together invite an arithmetic inference of "one minute per round," but the source never states a round's duration directly, and later sources do not agree on this figure. This card does not need it — only the round-to-turn *ratio* matters for turn accounting — and treats it as out of scope, belonging to a future combat-timing card (`COMBAT-006`, per `docs/rules/INVENTORY.md`).
6. **Whether the worked example's listening-triggers-a-check moment is caused by listening itself, or by listening completing a turn that preceding movement had already partly filled.** The worked dialogue narrates several segments of corridor movement (10', 20', 30', etc.) before the listening action that immediately precedes a check. Read one way, this is fully explained by ordinary turn accounting: the preceding movement already used most of a turn, and the listening action's fractional cost was what crossed the boundary. Read another way, the example could be (loosely) illustrating that any discrete referee-adjudicated action is itself treated as boundary-crossing. The source does not disambiguate which reading is intended, and this card does not resolve it by fiat — it is noted as an interpretive uncertainty in the corroborating evidence itself, distinct from the accumulation-algorithm gap in item 1, and is addressed by adopting a single coherent accumulation model that is *consistent* with the worked example without depending on which reading is "true."

---

## Completion Research

Because 1974 leaves the items above undefined, the non-AD&D D&D lineage was researched in the order given in `SOURCE_HIERARCHY.md` §3, per the hybrid research approach (`SOURCE_HIERARCHY.md` §8), treating this as a consequential ambiguity warranting deeper-than-usual lineage research rather than stopping at the first available later algorithm.

**Holmes Basic D&D (1977).** Verified via `WebFetch` against a specialist secondary source (Zenopus Archives, "Turns in Holmes Basic," a blog dedicated to page-level verification of Holmes-era text). Findings:
- Holmes closely paraphrases OD&D's own turn structure: 10-minute exploration turns, two moves per turn, 120 feet baseline movement — consistent with, and adding nothing beyond, the 1974 text already in hand.
- Holmes introduces an explicit **separate duration for a "combat turn"**: ten rounds of ten seconds each (~100 seconds), distinct from the 10-minute exploration turn. This is not a simple restatement of OD&D's ratio; it resolves the round-duration question OD&D leaves open (see "1974 Leaves Undefined," item 5), but by giving combat time a *different* absolute duration than exploration time, which OD&D's text does not itself suggest.
- Directly verified: the source **does not address** cross-activity-type accumulation of partial turns ("the post does not explicitly address how searching, listening, or other activities combine toward a full turn"), and **does not address** exactly when a turn is considered complete for the purpose of firing boundary procedures. Holmes does not close this card's central accumulation gap (item 1).

**B/X D&D — Moldvay Basic (1981) / Cook Expert.** Findings (via `WebSearch`, cross-checked against the structure of the Holmes findings above):
- Confirms the same 10-minute exploration turn and 120 feet/turn baseline movement, adding no new information for this card's needs.
- States a rest requirement of "1 turn for every 5 explored" — i.e., a 6-turn cycle (5 active + 1 rest). This is numerically identical to the ratio implied by OD&D's own "one turn every hour" (a turn ≈ 10 minutes, so an hour ≈ 6 turns, of which the stated 1 is rest, leaving 5). See "Compatibility Analysis."
- States that wandering-monster checks are made **"every two turns,"** not every turn. This directly contradicts the explicit 1974 text ("at the end of every turn," `EXP-001` p. 10) and is the same later convention `EXP-001` already identified and rejected. It is rejected again here, explicitly, for the same reason.
- No accumulation algorithm across mixed activity types was found in this source either.

**B2, *The Keep on the Borderlands* (Gygax, TSR, c. 1979–1980).** A Basic-D&D-compatible module, authored by one of the 1974 game's co-authors, within the Holmes/B-X lineage `SOURCE_HIERARCHY.md` permits for compatible completion:

> "For the sake of convenience, a DM can consider one entire melee turn to equal one normal turn (that is, 10 minutes), no matter how many melee rounds the combat took." (B2, p. 4, as quoted by Zenopus Archives, "Turns in Holmes Basic")

This directly addresses the combat-ending-early gap ("1974 Leaves Undefined," item 4). **Human review of this citation is now complete** — the human decision recorded below (see "Compatibility Analysis" and "Approved Mechanical Specification") confirms independent verification of the B2 rule and adopts it as a later compatible D&D completion, superseding the earlier draft's flag that the citation rested on an unverified secondary quote pending independent confirmation.

## Compatibility Analysis

| Source | Addresses | Judgment |
|---|---|---|
| Holmes — combat-turn as separate ~100-second unit | Round-duration gap (item 5) | **Not adopted.** Not needed for this card's scope (only the round-to-turn *ratio* matters here; absolute round duration belongs to `COMBAT-006`), and adopting a second, shorter real-time duration for "turn" during combat is an avoidable complication `EXP-002` does not need to take on. Not judged incompatible with 1974 — judged unnecessary. |
| B/X — "1 turn rest per 5 explored" | Rest-cadence gap | **Adopted as corroboration**, not as new information. It independently reproduces the same 6-turn cycle implied by OD&D's own "one turn every hour" statement once a turn is taken as ≈10 minutes. Because it is arithmetically identical to what 1974's own numbers already imply, this is treated as a compatible restatement, not a revision — it does not change the ratio, it confirms this card's mathematical reading of it is the one the D&D lineage actually continued to use. |
| B/X — wandering check "every two turns" | Turn-boundary/check-firing cadence | **Rejected**, explicitly and for the second time in this project. Contradicts the 1974 text's "at the end of every turn," which `EXP-001` already established and this card does not reopen. Per `SOURCE_HIERARCHY.md` §6, a later source that contradicts explicit 1974 procedure is a revision, not a compatible completion, and is excluded. |
| B2 — combat consumes exactly one normal turn regardless of rounds used | Combat-ending-early gap (item 4) | **Adopted — Later Compatible D&D Completion, human-approved.** Does not contradict any explicit 1974 statement; it is a natural, convenience-motivated rounding of the explicit 10-rounds-per-turn ratio for the case where fewer than ten rounds are used, rather than a revision of it. It introduces one new assumption 1974 itself does not state — that partial combat rounds up to a full turn, with the unused portion of the block representing recovery and related post-combat activity, rather than contributing a proportional fraction — which is exactly why this is classified as a *later completion* and not treated as though 1974 said it directly. This classification is deliberately kept separate from "1974 Explicit": see "Provenance Classification." |

---

## Simulator Ruling

**Approved.** No combination of 1974 and compatible later sources supplies an executable cross-activity accumulation algorithm; 1974 explicitly assigns turns and fractions of turns to multiple dungeon activities (movement, rest, search, ESP, combat) but never states how those different activity types' fractional costs combine into one running elapsed-turn count, nor the exact threshold/rounding behavior needed to make that arithmetic executable. Human decision has now approved the following as a Simulator Ruling:

**The shared dungeon-time ledger.** The simulation maintains one shared dungeon-time ledger per exploring party — not a separate counter per activity type. Every turn-costed activity, regardless of type (movement, rest, search, listening, ESP, hiding, treasure-loading, combat), adds its cost to this same ledger:

```text
movement fraction
+ search/listen/etc. fraction
+ other time-consuming activity
        ↓
shared accumulated dungeon time
        ↓
cross whole-turn boundary
        ↓
emit one completed-turn event
```

Any fractional remainder beyond a crossed threshold carries forward into the next turn's accumulation.

**This is not described as an explicit 1974 rule.** Its provenance is **Simulator Ruling**: 1974 supplies the individual activity costs; the shared ledger and its threshold/carry-forward mechanics are this project's own executable synthesis of those costs, adopted because it is the simplest model consistent with the worked-example evidence (item 9 under "1974 Explicitly Establishes") without requiring a decision about which reading of the listening/movement interaction ("1974 Leaves Undefined," item 6) is correct — under this model, both readings produce the same observable behavior. This is **not** an action-point system: it tracks a single scalar quantity (elapsed dungeon-time), not discrete spendable actions, and it does not introduce any new gameplay affordance — no activity's stated 1974 cost is changed by this ruling.

The precise accumulator semantics (threshold-crossing behavior, remainder carry-forward, progressive per-activity emission) are specified in full in "Approved Mechanical Specification," per the human decision that this ruling must be precise enough for deterministic implementation.

---

## Approved Mechanical Specification

**Scope.** This procedure defines what a dungeon turn is, how turn-costed activities accumulate into a count of fully elapsed turns, and when a "qualifying dungeon-turn interval has elapsed" signal (`EXP-001`'s stated dependency) fires. It does not decide *whether, when, or why* any particular activity occurs — movement destination selection, the decision to rest, the decision to search, combat resolution, and treasure-loading decisions are all owned by other procedures (`EXP-003`, `EXP-004`, `EXP-005`, combat domain, etc.). This card is consumed by those procedures; it does not consume them.

**Dependencies:**

```text
CHAR-005 (movement rate)  ─┐
EXP-004 (resting procedure)─┤
EXP-005 (search/listen)    ─┼─→  activity + its turn-cost  ─→  shared dungeon-time ledger  ─→  "turn elapsed" signal(s)  ─→  EXP-001
combat domain (round count)─┤
ENC-005 (flight/pursuit)   ─┘
```

`EXP-002` does not depend on any of these procedures' own mechanical content (what a search roll's odds are, when resting is triggered, etc.) — it only needs to be told, by whichever procedure decided an activity occurred, what turn-cost that activity carries. The integration direction with `EXP-001` is one-way, as already established by `CLUSTER-001-dungeon-exploration-time.md` §5: `EXP-002` produces a signal `EXP-001` consumes; `EXP-002`'s own content does not depend on `EXP-001`.

### Per-activity-type turn-cost table

Open-ended; the referee/simulator may assign a cost to an activity type not listed, per item 6 under "1974 Explicitly Establishes."

| Activity | Turn-cost | Provenance |
|---|---|---|
| One move (per the movement-rate procedure, `CHAR-005`) | 1/2 turn | Necessary mathematical consequence of "two moves constitute a turn" (1974 Explicit ratio) |
| One move, while in a flight/pursuit state | 1/4 turn (ratio doubled) | 1974 Explicit |
| ESP attempt | 1/4 turn | 1974 Explicit (named example) |
| Searching a ten-foot wall section for secret passages | 1 turn | 1974 Explicit (named example) |
| Listening, hiding, and any other activity 1974 leaves to referee adjudication | **Externally supplied** — this card accepts a historically/adjudicatively determined cost as an input and integrates it into the shared ledger; it does not assign a universal fixed value, and does not need to know *why* the supplied cost is what it is | 1974 Explicit (open-ended category itself); the specific numeric value supplied for any given instance comes from whatever procedure adjudicates it, not from this card |
| Treasure-loading or other bulk activity, adjudicated to a specific multi-turn cost | Whichever cost the adjudicating procedure declares for that instance — treated the same as any other externally supplied cost, **not** as a general historical rule that every bulk activity must be pre-declared as a whole number of turns | 1974 Explicit, via a single worked example (see "1974 Explicitly Establishes," item 7) — narrowly an instance, not a generalized procedure |
| Rest | 1 turn (2 turns if following a flight/pursuit state) | 1974 Explicit |
| Combat, per full ten-round block | 1 turn per block | 1974 Explicit ratio ("ten rounds of combat per turn") for a complete block; see "Combat time accounting" below for partial/successive blocks |

### Combat time accounting

Three distinct claims, kept separate per the human decision, each with its own provenance:

1. **Ten combat rounds equal one dungeon turn.** 1974 Explicit (p. 8, "There are ten rounds of combat per turn").
2. **A partially used ten-round block still consumes the full dungeon turn**, with the unused portion of that block representing recovery and related post-combat activity rather than being available to carry forward or be spent on something else. **Later Compatible D&D Completion** (B2, p. 4, human-approved — see "Compatibility Analysis"). Not 1974-explicit.
3. **Successive ten-round blocks consume successive dungeon turns**, following the pattern:

```text
1–10 combat rounds   → 1 dungeon turn
11–20 combat rounds  → 2 dungeon turns
21–30 combat rounds  → 3 dungeon turns
...

dungeon turns consumed by combat = ceiling(combat rounds / 10)
```

   This formula is **not** presented as explicit 1974 text. It is a **necessary logical/mechanical consequence** of applying claim 1 (the explicit per-block ratio) together with claim 2 (the human-approved completion that a partial block still consumes a whole turn) to combat lasting more than one block — i.e., each successive block of up to ten rounds, including a final partial block, is accounted for the same way claim 2 already establishes for a single block.

   As with any other multi-turn activity, completed-turn boundaries arising during combat are to be resolved progressively — one signal per block completed, as combat proceeds — rather than withheld and batch-emitted only once combat ends entirely, **to the extent the eventual combat integration permits**. This card does not design combat sequencing, initiative, or round-by-round mechanics; that remains `COMBAT-006`'s responsibility. This card establishes only the turn-accounting shape combat must eventually feed into.

### Accumulation algorithm (approved Simulator Ruling)

The accumulator advances **progressively as an activity's time cost is consumed**, not only after the activity finishes, and resolves each threshold crossing immediately before any remaining time is consumed:

```text
STATE: ledger  (a non-negative exact/rational value — turns and fractions of a turn — initialized
                to 0 at the start of a dungeon expedition; shared across all activity types;
                scoped to the exploring party)

WHEN an activity begins, carrying a total time cost C (turns), supplied by whatever
procedure adjudicated or calculated that cost:

    remaining := C

    WHILE remaining > 0:
        distance_to_boundary := 1 - fractional_part(ledger)
        step := MIN(remaining, distance_to_boundary)

        ledger    := ledger + step
        remaining := remaining - step

        IF ledger has just reached a whole integer:
            EMIT "dungeon turn elapsed" signal                       (immediately — see below)
            RESOLVE boundary consumers (e.g. EXP-001) synchronously,
                    before any further remaining time is consumed
            ledger := ledger - 1                                     (`step` never advances
                                                                        the ledger past a
                                                                        threshold in a single
                                                                        iteration, so at this
                                                                        exact point `ledger`
                                                                        holds a whole integer;
                                                                        subtracting 1 resets
                                                                        its current fraction
                                                                        to zero. Any further
                                                                        unconsumed activity
                                                                        time still lives in
                                                                        `remaining` and is
                                                                        processed by the next
                                                                        loop iteration, which
                                                                        may leave a fractional
                                                                        `ledger` value once
                                                                        `remaining` reaches 0)
            IF a boundary consumer signals that the activity is interrupted:
                STOP  (remaining cost, if any, is not consumed;
                       the interruption/resumption protocol itself
                       is not designed by this card)
```

Consequences of this shape, each following directly from the human decision:

- **Progressive, not batch, emission.** A four-turn activity produces four sequential "dungeon turn elapsed" signals *while the activity is under way* — one at each whole-turn threshold the activity's consumption crosses — matching the worked example's turn-by-turn wandering checks during the treasure-loading activity, rather than one batch of four signals only after the activity concludes.
- **Immediate resolution.** Each signal is resolved by its consumers (starting with `EXP-001`) before the ledger advances further, so a boundary consumer's result (e.g., a triggered wandering-monster encounter) is known before the remainder of an in-progress activity's time is spent.
- **Interruption is structurally possible, not architected here.** Because a boundary consumer resolves before the activity continues, a boundary-triggered event may interrupt the activity before its full declared or adjudicated duration completes. This card establishes only that this structural possibility exists at every threshold; the interruption/resumption protocol (how an interrupted activity communicates its partial completion back to whatever procedure initiated it, whether it can later resume, etc.) is explicitly **not** designed here.
- **No threshold is skipped, and no signal is emitted without a genuine crossing.** The `WHILE` loop guarantees one emission per whole-integer threshold actually crossed, however many that is for a given activity, and guarantees an activity that does not cross a threshold (e.g., a single ESP attempt from `ledger = 0`) emits no signal at all merely because the activity ended.
- **Exact/rational values.** The specification above is written in exact conceptual arithmetic (fractions of a turn), not a specific numeric representation. This card does not prescribe a Python numeric type or implementation data structure for `ledger` — that is an implementation-time decision, not a rules decision.

**Worked numeric example** (per the human decision's own illustration): ledger currently holds 1/2 turn of unconsumed remainder; a new activity costs 3/4 turn. Total progression is 1¼ turns: the loop crosses exactly one whole-turn threshold (emitting exactly one "dungeon turn elapsed" signal), and 1/4 turn remains on the ledger afterward.

### Rest and the shared ledger

A rest activity's cost (1 turn, or 2 turns following a flight/pursuit state, per "1974 Explicitly Establishes," item 4 and item 3) is consumed through the same accumulation algorithm as any other activity — it is not tracked on a separate counter, and rest time crosses ordinary dungeon-turn boundaries exactly as movement, search, or combat time does, participating in the same shared ledger. This card establishes only that time-accounting fact. It does **not** determine when mandatory rest is due, how the rest requirement itself is tracked over the course of an expedition, what constitutes satisfying it, or any other part of the resting procedure — those remain `EXP-004`'s responsibility, and are not absorbed into this card.

### Movement and the shared ledger

Consistent with `CLUSTER-001`'s boundary, this card owns only the historical time relationship "two moves = one dungeon turn," from which "one ordinary move = one-half dungeon turn" follows as a necessary mathematical consequence, not as an independently quoted historical rule. Spatial distance and encumbrance-derived movement capability remain outside `EXP-002` and belong to `CHAR-005` / `EXP-003`; this card only needs to know that a move occurred and that it costs 1/2 turn (1/4 turn during flight/pursuit) to feed the shared ledger.

### Output and integration with `EXP-001`

`EXP-002` supplies exactly one "dungeon turn elapsed" signal per whole dungeon turn actually elapsed on the shared ledger — never more, never fewer, and never merely because an activity ended without crossing a threshold. Each signal carries no data beyond the fact of a turn having elapsed, consistent with `EXP-001`'s own output contract ("carries no data beyond the fact of triggering"). `EXP-001` consumes each such signal, unmodified from its existing approved specification:

```text
1d6
6   → wandering encounter triggered
1–5 → no wandering encounter triggered
```

This card does not modify `EXP-001`'s cadence and does not import the B/X "every two turns" convention (rejected above, for the second time in this project). Because signals are now resolved immediately/progressively rather than in a batch, `EXP-001`'s check is performed synchronously at each threshold as it is crossed — consistent with the worked example, where the referee checks turn-by-turn during the four-turn loading activity rather than waiting until it finishes.

**No RNG owned by this card.** This procedure is purely arithmetic. It performs no die rolls and must not be given its own RNG stream (`ARCHITECTURE.md` §5, `AGENTS.md` §7) — the only randomness in this card's vicinity belongs to the procedures that decide activity *outcomes* (e.g., `EXP-001`'s own check), not to this card's accounting.

**Survivability out of scope.** Consistent with `EXP-001`, this card specifies canonical historical time accounting only. It must not accept a survivability policy, and no survivability policy may alter turn-costs or the accumulation algorithm, without a separately approved Rule Card or policy decision (`ARCHITECTURE.md` §10).

---

## Deterministic Test Cases

All cases are pure-arithmetic and require no RNG double for `EXP-002` itself; cases involving `EXP-001`'s own die roll use a controlled RNG for that portion only, per `EXP-001`'s existing test convention.

**Fractional accumulation:**

1. **Single half-turn move, no boundary yet.** One move (cost 1/2 turn) from `ledger = 0` → ledger = 0.5, zero signals.
2. **Second move crosses the first boundary.** A second move (1/2 turn) immediately after case 1 → ledger returns to 0, exactly one signal.
3. **Mixed-activity-type accumulation crosses a shared boundary.** One move (1/2) + one ESP attempt (1/4) + a second ESP attempt (1/4) → totals exactly 1.0 → exactly one signal, ledger returns to 0. This is the case that most directly exercises the approved shared-ledger ruling.
4. **Remainder carries forward after crossing.** Ledger at 1/2 turn of unconsumed remainder; a new activity costs 3/4 turn (the worked numeric example from "Approved Mechanical Specification") → exactly one signal, 1/4 turn remains on the ledger afterward.

**Multi-turn activity, progressive emission:**

5. **Four sequential boundaries during one in-progress activity.** A single activity with a declared/adjudicated cost of 4 turns, starting from `ledger = 0` → four "dungeon turn elapsed" signals, emitted in order (turn 1, turn 2, turn 3, turn 4) *while the activity is being consumed*, each resolved before the next portion of the activity's time is consumed — not four signals batched after the activity concludes. Directly reproduces the worked example's "four turns... on the forth try" behavior.
6. **Interruption at a boundary.** Same setup as case 5, except a boundary consumer signals interruption after the second threshold is crossed → exactly two signals are emitted, the activity does not consume its remaining declared time, and no third or fourth signal fires. This card does not test or define the detailed interruption/resumption architecture beyond confirming the activity stops consuming further time at that point.

**Combat:**

7. **4 rounds → 1 dungeon turn.** A combat activity resolved in 4 of a possible 10 rounds → 1 turn consumed, one signal (`ceiling(4/10) = 1`).
8. **10 rounds → 1 dungeon turn.** A full ten-round block → 1 turn consumed, one signal (`ceiling(10/10) = 1`).
9. **11 rounds → 2 dungeon turns.** One full block plus one round into a second block → 2 turns consumed, two signals emitted progressively as each block completes (`ceiling(11/10) = 2`).
10. **20 rounds → 2 dungeon turns.** Two full blocks → 2 turns consumed, two signals (`ceiling(20/10) = 2`).
11. **21 rounds → 3 dungeon turns.** Two full blocks plus one round into a third → 3 turns consumed, three signals (`ceiling(21/10) = 3`).

**Referee-supplied fractional activity:**

12. **Externally supplied cost integrates without `EXP-002` needing to know its source.** An activity supplied with an adjudicated cost of 1/4 turn (e.g., standing in for a listening check, or any other referee-adjudicated activity) is accepted and accumulated on the shared ledger identically to a named 1974 example (such as an ESP attempt) — verifying `EXP-002` treats the *value* uniformly regardless of *why* that value was chosen.

**Threshold and remainder correctness:**

13. **Threshold exactness — lands exactly on a boundary.** An activity sequence whose total lands at exactly 1.0 (not past it) fires exactly one signal, not zero and not two.
14. **No signal without a genuine crossing.** An activity that does not cross a threshold (e.g., a single ESP attempt from `ledger = 0`, ending at 0.25) fires zero signals — an activity ending is not itself a signal-firing event.

**No RNG dependency:**

15. **`EXP-002`'s own procedure requires no RNG.** The accumulation procedure can be exercised through an arbitrary sequence of activity-completion calls with no RNG double supplied at all (or one that raises on any call) and still produces correct signal counts.

**Paired integration contract with `EXP-001`:**

16. **One check opportunity per completed-turn signal.** Given a scripted sequence of activities whose combined cost is known to complete exactly *N* whole turns, invoking `EXP-001`'s check procedure once per emitted signal results in exactly *N* checks, each consuming exactly one RNG operation — the mirror image of `EXP-001`'s own existing "Turn-dependency integration contract" test, confirming both ends of the `EXP-002` → `EXP-001` integration point agree on signal count, including when those signals are emitted progressively mid-activity rather than in a batch.

## Provenance Classification

This card is provenance-mixed; no single category from `GAME_CONSTITUTION.md` §5 applies to it as a whole. The categories are kept deliberately distinct, per the human decision, and are not blurred together:

**1974 Explicit**
- Dungeon turn ≈ ten minutes.
- Two moves constitute one turn.
- ESP = 1/4 turn; searching a ten-foot wall section = 1 turn (named examples).
- Rest = one turn every hour; doubled following flight/pursuit.
- Ten combat rounds = one dungeon turn.
- The wandering check (`EXP-001`) fires once per elapsed turn, demonstrated occurring during non-movement activities, including mid-activity for a multi-turn bulk activity.

**Necessary Mathematical / Mechanical Consequence**
- One ordinary move = one-half turn (half of the explicit two-moves-per-turn ratio).
- Approximately six ten-minute turns correspond to approximately one hour (the arithmetic basis for the rest cadence; corroborated, not established, by B/X's independently stated "1 turn per 5 explored").
- Successive ten-round combat blocks correspond to successive dungeon turns, i.e. `ceiling(rounds / 10)` — the mechanical consequence of combining the explicit per-block ratio with the later-completion rule for a partial block (see next category).

**Later Compatible D&D Completion**
- A partially used ten-round combat block still consumes the whole dungeon turn (B2, p. 4, human-approved).

**Simulator Ruling**
- The single shared cross-activity dungeon-time ledger (rather than per-activity-type counters).
- The exact threshold/carry-forward/progressive-emission semantics that make the historical fractional costs executable.

**Out of scope for this card**
- The absolute real-world duration of a single combat round (`COMBAT-006`).
- Flight/pursuit state entry/exit triggers (`ENC-005`).

---

## Open Questions

1. **Interruption/resumption protocol.** This card establishes that a boundary-triggered event may structurally interrupt an in-progress multi-turn activity, but does not design how an interrupted activity communicates its partial completion, whether or how it later resumes, or what state it leaves behind. This is deferred to whichever future card(s) integrate this accounting into actual activity execution (likely touching `EXP-004`, `EXP-005`, and `COMBAT-006`), and does not block this card's own approval.
2. **Whether fixed numeric costs should eventually be assigned to listening, hiding, or other currently-adjudicated activities**, for implementation convenience. This card deliberately leaves them externally supplied rather than inventing fixed values; a future decision to fix specific values would itself be a further Simulator Ruling, not addressed here.
3. **Combat round's absolute real-world duration** remains out of scope, flagged for `COMBAT-006` (`docs/rules/INVENTORY.md`), which already carries a historically-high-risk flag pending research into *Chainmail*'s relationship to D&D's turn structure. This card does not depend on that answer.
4. **Flight/pursuit state boundaries** (what triggers entry into or exit from a flight/pursuit state) remain `ENC-005`'s concern. This card only consumes that state as an external boolean input to the movement/rest cost table.

## Approval

- Approved by: Human project owner
- Date: 2026-08-15
- Notes: Approval incorporates the following decisions made during human review: (1) the shared, cross-activity dungeon-time ledger is adopted as a Simulator Ruling, with exact threshold-crossing and remainder-carry-forward semantics specified for deterministic implementation; (2) turn-boundary signals are resolved progressively and immediately as an in-progress activity's time is consumed, not batch-emitted only after the activity finishes — reflected in the four-turn worked-example test case and the interruption-possibility note; (3) the B2 "partial combat block still consumes a full turn" rule is adopted as a Later Compatible D&D Completion (not a Simulator Ruling), with successive-block combat accounting (`ceiling(rounds / 10)`) following as its mechanical consequence; (4) referee-adjudicated activities without a stated 1974 numeric cost (listening, hiding, and similar) remain externally supplied rather than assigned invented fixed values.

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
