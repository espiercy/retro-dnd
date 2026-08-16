# Rule Card: Dungeon Wandering-Monster Check

> **Migration note (2026-08-16).** Previously approved under the superseded 1974-primary source policy (`docs/decisions/DEC-0006-v1-playable-content-scope.md` and prior). Requires Rules Cyclopedia revalidation before implementation authority is restored (`DEC-0007-rules-cyclopedia-primary-rules-authority.md`, `DEVELOPMENT_WORKFLOW.md` §9.7). This does not indicate the research below was incorrect — only that it has not yet been reviewed against the current source hierarchy. All content below is preserved unchanged as the historical research and approval record; it is not rewritten by this migration. See `docs/rules/RULESET_BASELINE_MIGRATION.md`.
>
> Prior approval record: Approved by Human project owner, 2026-08-15, under the then-governing 1974-primary source policy — see this card's own "Approval" section below, preserved unchanged.

---

## Rule ID

EXP-001

## Title

Dungeon (Underworld) Wandering-Monster Check

## Status

REVALIDATION_REQUIRED

## Rules Domain

exploration

---

## 1974 Source

Gygax, Gary, and Dave Arneson. *Dungeons & Dragons, Volume 3: The Underworld & Wilderness Adventures.* Lake Geneva, WI: Tactical Studies Rules, 1974.

- Section **"UNDERWORLD MONSTERS"** (p. 9), paragraph **"Wandering Monsters"** (p. 10) — the operative procedure for this card.
- Section **"THE MOVE/TURN IN THE UNDERWORLD"** (p. 8) — defines the dungeon "turn" this procedure depends on (referenced, not specified, by this card — see "Dependencies" below).

**Verification method.** A digitized reproduction of the booklet was retrieved and its text extracted directly (not recalled from memory or taken from a secondary paraphrase). Page numbers were cross-checked two ways and agree: (a) the booklet's own printed page-footer sequence in the reproduction, and (b) the booklet's own table of contents, which lists "Underworld Monsters" beginning at page 9 and "Monster Determination and Level of Monster Matrix" (the table immediately following the Wandering Monsters paragraph) beginning at page 10. A secondary source (an independent OSR blog's page-by-page notes on this same booklet) was checked against the frequency finding below and agrees ("1 in 6 chance of wandering monster per turn, not every other turn") — noted here because "every other turn" is a common misattribution (it is Basic/Expert D&D's convention, not OD&D's), and this card explicitly does not import that later convention. No AD&D material was consulted.

**Exact source text (Wandering Monsters, p. 10):**

> "Wandering Monsters: At the end of every turn the referee will roll a six-sided die to see if a 'wandering monster' has been encountered. A roll of 6 indicates a wandering monster has appeared. The direction of appearance is determined by random number generation considering the number of possible entries. Distance and surprise are decided in the usual manner. The kind of monster is determined on the table below. (For wilderness encounters an entirely different table will be used)."

**Exact source text (turn definition, p. 8):**

> "Movement (distances given in Vol. 1) is in segments of approximately ten minutes. Thus it takes ten minutes to move about two moves — 120 feet for a fully-armored character. Two moves constitute a turn..."

## 1974 Explicitly Establishes

1. **Frequency.** The check is made "at the end of every turn" — every dungeon turn, without exception stated in the text (not "every other turn"; that is a later B/X-era convention, not this source's).
2. **Procedure.** One six-sided die (1d6) is rolled by the referee.
3. **Trigger.** "A roll of 6 indicates a wandering monster has appeared." A result of 1–5 does not.
4. **Scope boundary, stated by the source itself.** This is the *underworld* procedure. The same booklet contains a textually and mechanically separate "Wilderness Wandering Monsters" procedure (checked once per *day*, using a terrain-dependent matrix rather than a flat 1-in-6 roll) — the source explicitly flags this distinction ("For wilderness encounters an entirely different table will be used"). This card covers the underworld version only; the wilderness version is a distinct future Rule Card.
5. **No stated depth/level modifier to the check itself.** The Wandering Monsters paragraph states a flat, unmodified 1-in-6 roll with no dependency on dungeon level. This is treated as 1974-explicit rather than an oversight: the same booklet's treasure-type table (p. 7) *does* explicitly vary by "Level Beneath Surface" when the authors intended depth-based variation — its absence here is a meaningful contrast, not silence to be filled in.
6. **No stated referee discretion over whether to perform the check.** The clause is unqualified ("the referee will roll"). Elsewhere in the same booklet, discretionary procedures are explicitly marked as such (e.g., p. 10: "At the referee's option, Elves may be allowed the chance to sense any secret door they pass..."). The absence of equivalent qualifying language here is treated as 1974-explicit: the check is a standing procedure, not optional flavor.
7. **A dungeon turn is approximately ten minutes of game time** (p. 8), and non-movement activity is already expressed in turn units, not left outside the turn system: resting requires "one turn every hour must be spent motionless" (p. 8); searching a ten-foot section of wall "will require a full turn," with other, shorter activities (e.g., ESP'ing) "adjudged by the referee" as consuming a lesser portion of a turn (p. 8); and combat is explicitly subdivided into turns — "There are ten rounds of combat per turn" (p. 8). These references establish that "turn" is a recurring, bounded unit of dungeon time that rest, search, and combat all consume or are denominated in — not that its complete accounting semantics are defined (see "Dependencies").

## 1974 Leaves Undefined

Narrowly, within this card's scope: the 1974 text already ties rest, search, and combat to turn units (see item 7 above) — it does not leave *that* undefined. What it does not specify is the precise accounting/integration semantics a computer simulation needs: how partial-turn activities (e.g., a quarter-turn ESP check) accumulate toward a whole elapsed turn, and exactly when, relative to that accounting, the check in this card fires. This card does not resolve that narrower question — it is a dungeon-turn/exploration-turn system integration question, not a wandering-monster-check question (see "Dependencies" in the Mechanical Specification, and Open Questions).

Nothing else within this card's narrow scope (frequency, die, trigger value, procedure isolation) is left undefined by the 1974 text.

---

## Completion Research

Not applicable — 1974 is fully explicit for this card's narrow scope (frequency, die, and trigger value). The one genuine open item (precise turn-accounting/integration semantics — see "1974 Leaves Undefined") is a dependency on a not-yet-authored dungeon-turn Rule Card, not an unresolved rules *question* this card needs a later source to complete. No non-AD&D D&D-lineage research was performed beyond the single corroborating cross-check noted under "1974 Source" (confirming, not completing, the 1974 finding). No AD&D material was consulted or considered.

## Compatibility Analysis

Not applicable — no later-source completion was sought or imported into this card's mechanical specification.

---

## Simulator Ruling

Not applicable.

---

## Approved Mechanical Specification

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

## Deterministic Test Cases

All cases use a controlled RNG (`ScriptedRNG` or equivalent) supplying a specific queued die value — never probabilistic sampling as the acceptance mechanism (`RNG_CONTRACT.md` §9, `TESTING_STRATEGY.md` §3).

1. **Non-trigger, lowest value.** Scripted roll = 1 → no encounter triggered.
2. **Non-trigger, mid-range.** Scripted roll = 2 → no encounter triggered. Scripted roll = 3 → no encounter triggered. Scripted roll = 4 → no encounter triggered. (Included individually, not only as boundaries, so an off-by-one implementation — e.g., accidentally triggering on ≥5 — cannot pass by only testing the extremes.)
3. **Non-trigger, highest non-trigger value.** Scripted roll = 5 → no encounter triggered.
4. **Trigger, boundary value.** Scripted roll = 6 → encounter triggered.
5. **Exactly one RNG operation per check.** Using a scripted queue of length exactly 1, a single check invocation succeeds without exhausting or needing a second value — proving the procedure performs exactly one `roll_die(6)`/`roll("1d6")` call, never a hidden extra draw or a re-roll on any result.
6. **Procedure isolation.** On a triggered result, the produced outcome exposes only the trigger fact and the roll's own audit data — no monster, direction, distance, surprise, reaction, or treasure fields are present on it (there is no code path by which this procedure could populate them).
7. **Turn-dependency integration contract** (does not implement the turn system). Given a sequence of *N* "qualifying dungeon-turn elapsed" signals (simulated/stubbed, not the real turn system), the check procedure is invoked exactly *N* times, each consuming exactly one RNG operation — demonstrating the integration point is called once per elapsed turn, neither zero nor multiple times per signal. This is a contract test for whoever later implements the turn-system integration, not a test of turn semantics themselves.
8. **Determinism.** The same seed and call sequence via the seeded production RNG reproduce the same trigger/non-trigger outcome (`RNG_CONTRACT.md` §9's general reproducibility guarantee — this card introduces no exception to it).

## Provenance Classification

1974 Explicit.

---

## Open Questions

1. **Turn-accounting integration semantics.** Movement, rest, search, and combat are already turn-denominated per the 1974 text (see "1974 Explicitly Establishes," item 7); what a future dungeon-turn/exploration-turn Rule Card still needs to specify is the precise accounting algorithm — how partial-turn activities accumulate toward a whole elapsed turn, and exactly when, relative to that accounting, this card's "qualifying turn elapsed" signal fires. **This does not block approval of this card's own mechanical specification**, since the check procedure itself (roll, trigger, output) is fully specified independent of that answer.

---

## Approval

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
