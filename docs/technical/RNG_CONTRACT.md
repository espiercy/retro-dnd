# RNG Technical Contract

## 1. Purpose and Status

This document is the technical design for the project's Random Number Generation (RNG) abstraction — Pre-Code Development Gate item 7 (`ARCHITECTURE.md` §16). It is a specification, not an implementation: no Python modules are created by this document.

This contract's architecture has been approved by the project owner, subject to the refinements incorporated into this revision. The approval is recorded as `docs/decisions/DEC-0002-rng-contract.md`, which summarizes this contract and references it rather than duplicating it. No RNG implementation exists yet; implementation remains subject to the Pre-Code Development Gate as a whole (`ARCHITECTURE.md` §16) and to separate, explicit authorization to begin Issue 1.

## 2. Ownership Model

One simulation-owned RNG stream, per `ARCHITECTURE.md` §5:

```text
Campaign / Simulation
        └── RNG(seed)
```

A campaign/simulation session owns exactly one RNG instance, seeded once at campaign start. All historical random procedures within that campaign draw from that single instance. No rules domain, procedure, entity, dungeon level, or encounter receives its own RNG stream. This contract introduces no exception to that rule; a future architecture decision would be required to change it (`ARCHITECTURE.md` §5).

## 3. The RNG Boundary

All simulation randomness flows through this abstraction:

```text
Rules Procedure
      ↓
Simulation RNG abstraction
      ↓
Random result
```

Historical rules procedures must never call an uncontrolled random facility directly. This is required for deterministic testing, replayability, debugging, rules auditing, and reproducibility (`ARCHITECTURE.md` §5, `AGENTS.md` §7).

Presentation and narrative code must never consume the simulation RNG (§8).

## 4. Public Contract

The RNG abstraction exposes exactly two **public, rules-facing operations**, both returning the same rich result type (§5), and each assigned exactly one `sequence_number` (§6) per call:

- **A single-die operation** — roll one die of a given size.
- **A dice-expression operation** — parse a small, fixed dice notation (§7) and return the aggregate result of rolling all the dice it specifies.

Internally, both public operations are built on a single, private, non-public primitive — a **raw draw**: pull one uniformly random face value from the underlying stream. A raw draw is not itself part of the public contract, is not wrapped in a roll result, and does not receive its own `sequence_number`. The single-die operation performs exactly one raw draw; the dice-expression operation performs as many raw draws as the expression's dice count (`N`) requires, entirely internally, aggregating them into one result.

This keeps exactly one place in the system where "a random number is actually drawn" — the raw draw — while ensuring the rules-visible history (§6) records one entry per public call a rules procedure actually made, not one entry per underlying draw. Every random draw the simulation ever makes still passes through this one raw-draw primitive; the two-tier design (raw draw vs. public operation) exists to give sequence numbers rules-relevant meaning, not to create a second path to randomness.

Both public operations are defined identically by two conforming implementations (§9): a seeded production implementation and a scripted/deterministic test implementation. Rules procedures depend only on this abstract contract, not on which implementation is in use.

## 5. Roll Result Representation

A roll — from either public operation — returns an immutable value carrying (conceptually; field names are illustrative, not a Python API commitment):

| Field | Meaning |
|---|---|
| `expression` | The dice notation that produced this result (e.g., `"3d6+1"`), or its canonical single-die equivalent (e.g., `"1d6"`) when produced via the single-die operation directly. |
| `dice` | The individual die results, in roll order (e.g., `(4, 2, 5)`). |
| `die_size` | The number of faces used (e.g., `6`). All dice within one roll share this size (§7). |
| `modifier` | The applied flat arithmetic modifier (`0` if none). |
| `total` | `sum(dice) + modifier`. |
| `sequence_number` | A monotonically increasing index identifying this **public roll operation's** position in its RNG instance's rules-visible history (§6) — not a count of underlying raw draws. |

This satisfies the requirement that a dice operation preserve more than an opaque final integer: individual dice are inspectable, the modifier is separated from the total, and the roll is traceable by `sequence_number` without needing to replay the campaign seed.

The number of raw draws (§4) a given result required is recoverable from `len(dice)` — a single-die result always has exactly one entry in `dice`; a `roll("3d6")` result has three. No separate "draws consumed" field is needed in the public contract for this reason (§6 explains why the draw count and the sequence number are deliberately different numbers).

Deliberately excluded from this value: wall-clock timestamps, the identity of the calling rules procedure, campaign/character identifiers, and narrative text. Those are rules-procedure or event-layer concerns (§10, §11) — attaching them to the RNG's own result would blur the boundary between "the RNG rolled dice" and "the rules interpreted what the dice meant," which this contract is specifically designed to keep separate.

## 6. Sequence-Number Semantics

`sequence_number` identifies a **rules-visible public roll operation** (§4) — one single-die call or one dice-expression call — not every underlying raw draw that operation required.

```text
roll("3d6")

sequence_number: 17
dice: [4, 2, 5]
modifier: 0
total: 11
```

This must **not** ordinarily become four separate sequence numbers (one per die plus one for the aggregate) — the individual die draws are constituent values of operation 17, not separate historical rolls in their own right. The design goal is a clean audit history:

```text
Roll 17: 3d6   → [4, 2, 5]     = 11
Roll 18: 1d6   → [3]           = 3
Roll 19: 2d6+1 → [2, 6] + 1    = 9
```

rather than one that exposes internal implementation mechanics as separate historical rolls.

**This does not change how much of the underlying RNG stream is consumed.** A `3d6` roll still requires three raw draws (§4) from the authoritative stream — rules-visible operation count and underlying-draw count are deliberately different numbers:

```text
Rules-visible operation count: 1
Underlying random draws:       3
```

Adding, removing, or reordering an underlying raw draw still changes every later result in the campaign, exactly as it would without this distinction (§8) — this section changes what receives a *sequence number*, not how much of the stream a given call consumes. Implementers must not conflate the two: `sequence_number` is for rules-facing audit/diagnostics (§10); raw-draw count (recoverable as `len(dice)`, §5) is what actually governs stream state.

## 7. Dice Expression Scope

Supported notation, deliberately small:

```text
dS
NdS
NdS+M
NdS-M
```

`dS` is shorthand for `1dS` (e.g., `d6` ≡ `1d6`) — both are accepted notation. The resulting `expression` field records whichever form was actually requested; this contract does not mandate normalizing one form to the other, only that both parse to the same aggregate behavior.

Where:
- `N` — number of dice, a positive integer (`N ≥ 1`). No artificial upper bound is imposed; historical procedures have not been found to need one, and none is invented pre-emptively.
- `S` — die size (faces), a positive integer (`S ≥ 1`). No fixed allow-list of "historical" die sizes (e.g., restricting to {4,6,8,10,12,20,100}) is imposed — restricting the *notation grammar* is enough to keep the parser small; restricting the *die-size range* would add a rule with no corresponding implementation-complexity benefit and risks blocking a legitimate future need.
- `M` — an optional flat integer modifier, applied once to the summed total. No per-die modifiers.

Explicitly **not** supported in this initial scope (any of these must raise an error, §12, not silently degrade):
- Mixed-size dice pools (e.g., `2d6+1d4`).
- Exploding dice, reroll-on-N mechanics as notation, drop-lowest/keep-highest.
- Multiple modifiers, or a modifier applied to anything other than the final total.
- Percentile shorthand (`d%`) as special notation — a percentile roll is expressed as `1d100` (or, if an eventual rules implementation needs 2d10-as-percentile per some historical procedure, that composition happens in rules code calling the dice-expression operation twice, not as RNG-abstraction notation).

This is not a general-purpose tabletop dice language, and should not become one unless a specific approved Rule Card's mechanical specification requires notation this scope doesn't cover — at which point the gap should be reported the same way any other specification gap is (`AGENTS.md` §3), not silently patched into the parser.

## 8. Consumption Semantics

Because there is one shared stream (§2), **when** randomness is consumed matters as much as what is consumed — advancing the stream at all, even for a value nobody uses, changes every subsequent result for the rest of the campaign. This is expected and correct behavior for a single-stream design, but it has consequences this contract makes explicit:

- **No "peek" operation exists.** There is no way to inspect what the next roll would be without consuming it. A peek that doesn't consume the stream isn't meaningfully implementable without saving/restoring RNG state around it (reintroducing per-call state complexity); a peek that does consume the stream is just an oddly named roll. Neither is provided.
- **Retry/reroll loops must be explicit and historically motivated, never an implementation convenience.** Some historical procedures do specify an actual reroll; when a Rule Card specifies that, it is implemented as an explicit, visible call to roll again. Rules code must never silently reroll because a generated value was inconvenient for the implementation.
- **Diagnostic/logging/debugging code must never consume the RNG.** A debug path that "rolls again to show what would have happened" is exactly the hidden-consumption failure mode this contract exists to prevent. Diagnostics must only ever display data already captured from an actual roll (§10) — never re-derive it by rolling again.
- **Presentation code must never consume the simulation RNG** — consistent with `ARCHITECTURE.md` §2/§11 (simulation determines reality; presentation describes it). If presentation ever needs "random" flavor (e.g., varying which of several idle-room descriptions to show), that must use a separate, non-simulation-owned source of randomness explicitly outside this contract, never the campaign's simulation RNG.

Any change to the order or number of raw draws a rules procedure triggers is a consequence-bearing change: it changes every later roll's outcome for that campaign/seed, regardless of how those draws are grouped into sequence-numbered operations (§6). Implementers and reviewers should treat "this refactor added/removed/reordered a random draw" as a change requiring the same scrutiny as a rules-behavior change, even when its author considers it purely internal.

## 9. Deterministic Testing

Two implementations conform to the public contract (§4):

**Seeded production implementation.** Deterministic reproduction is guaranteed under the project's supported runtime contract:

> Same supported Python/toolchain version (`docs/technical/TOOLCHAIN_AND_CI.md` §2) + same initial RNG seed/state + same sequence of simulation RNG consumption ⇒ the same expected sequence of raw draws, and therefore the same sequence of roll results.

This is **not** a promise that a seed alone reproduces a campaign indefinitely across arbitrary future Python or runtime versions. The project pins one Python minor version specifically to make determinism well-defined within a known environment (`docs/technical/TOOLCHAIN_AND_CI.md` §2), not to make it environment-independent forever. Resuming a campaign reliably after a runtime upgrade is a persistence-and-compatibility concern, not a property this RNG contract can guarantee on its own — see §13.

**Scripted/deterministic test implementation ("fake RNG").** Constructed with a predetermined, ordered queue of raw die values to return (e.g., "next results: 6, 2, 4, 1") rather than a seed. Each raw draw the fake performs consumes the next queued value; the dice-expression operation still performs its own real aggregation logic (summing N draws + modifier) on top of those queued values — a scripted sequence `4, 2, 5` used for `3d6` must still exercise real dice aggregation and result construction, not simply return a prebuilt total of `11`. If the queue is exhausted, the fake raises an explicit error (§12) rather than falling back to real randomness or silently repeating/wrapping the queue.

**A scripted value must be a possible result of the die it is drawn for.** The fake may force *which* valid result a die produces; it must not be able to manufacture a result the corresponding production die could never produce — a queued value of `9` for a d6 is invalid, not merely an unusual choice, since `SeededRNG` can never produce it either. Each value is validated against the specific die size at draw time (not at construction time, since the same fake instance may be asked for different die sizes across its lifetime) and must be an `int` (excluding `bool`, per §12's explicit-failure-over-silent-coercion principle) within `[1, sides]`; anything else raises explicitly (§12) rather than silently accepting an impossible result. This closes a gap in this contract's original text, which specified queue *exhaustion* behavior but did not explicitly require this invariant — identified in post-merge review and corrected without otherwise changing the approved architecture.

Both implementations satisfy the identical rules-facing contract (§4) so that a rules procedure's tests can supply the fake with an exact scripted sequence to hit a specific historical branch (e.g., "force a natural 1"), without hunting for a seed that happens to produce it — this is the primary reason the fake exists alongside seeded reproduction rather than seeding being considered sufficient on its own.

## 10. Roll Diagnostics

Design goal: a historically significant random result should be explainable after it occurs, without needing to replay the campaign from its original seed.

Minimum design proposed for Issue 1 and the immediately following rules issues:

- Every roll result carries a `sequence_number` (§6), assigned by the RNG boundary, giving every rules-visible roll a stable, queryable position in its campaign's history.
- Rules procedures that produce a historically significant outcome embed the relevant roll result(s) directly in the structured event they emit (`ARCHITECTURE.md` §8) — e.g., a `ReactionResolved` event carries the reaction roll's full result alongside the interpreted historical outcome. This is the rules procedure's responsibility, not the RNG's (§11) — the RNG only ever hands back dice data; a rules procedure decides what that data meant and records both together.

Do not add timestamps, narrative information, character IDs, or other domain metadata to the core RNG result unless a later requirement justifies doing so (§5). Rules/event layers may add contextual meaning around a roll; the RNG result itself stays minimal.

Explicitly deferred, not designed now: a standalone roll-history/audit service (a queryable log of every roll ever made, independent of the events already produced). The roll-result-plus-event-embedding pattern above is proposed as sufficient for the first vertical slice; whether a fuller audit subsystem is needed is a question for a future architecture decision once real debugging experience exists to justify it (`ARCHITECTURE.md` §13's premature-infrastructure caution applies here too).

## 11. Separation From Rules Semantics

The RNG rolls dice. It does not interpret what the dice mean.

```text
RNG:
2d6 → [2, 5] → 7

Reaction procedure:
7 → particular historical reaction result
```

The RNG abstraction has, and must continue to have, zero knowledge of: reaction tables, treasure tables, monster generation, attack rolls, saving throws, survivability policy, or XP. It returns only the fields in §5 — dice, modifier, total, expression, sequence number. Mapping a `total` to a historical table result happens entirely inside the relevant rules procedure, which calls the RNG boundary and then performs the interpretation itself.

This boundary is a hard constraint on implementation, not just a design preference: a convenience helper such as a `roll_reaction()` function must never live inside the RNG module — it belongs in the reaction rules module, which internally calls the RNG's dice-expression operation and performs the table lookup itself.

## 12. Error Behavior

Invalid requests fail explicitly; none of the following are silently coerced, clamped, or defaulted:

- Malformed dice-expression string (doesn't match §7's grammar).
- Zero or negative number of dice.
- Non-positive die size.
- Unsupported notation (mixed dice pools, modifiers beyond a single flat integer, anything outside §7's scope).
- An exhausted controlled test sequence on the fake RNG (§9) — distinguished from other errors so a test author immediately recognizes "my scripted sequence was too short" rather than a generic failure.
- A scripted value on the fake RNG that is not a possible result for the requested die — out of `[1, sides]`, or not an `int` (including `bool`) at all (§9) — distinguished from exhaustion (the queue isn't empty; its next value is simply invalid for this specific request).

Error handling never invents a domain-specific game ruling (e.g., there is no "invalid roll, treat as a natural 1" fallback anywhere in this contract) — an error always propagates to the caller as an error, for rules code (or ultimately a human) to handle, never resolved into a plausible-seeming in-game result on the RNG's own authority.

## 13. Persistence — Deferred Requirement

Not designed or implemented by this document. Recorded here so the eventual implementation doesn't foreclose it by accident.

Because campaign state persists (`ARCHITECTURE.md` §7) and the simulation is meant to be deterministically reproducible, resuming a saved campaign and continuing its RNG stream deterministically will eventually require persisting enough RNG state to continue from exactly where the campaign left off — not merely the original seed (replaying an entire campaign's history of RNG calls to "fast-forward" back to the current point is a theoretical option but not a robust long-term persistence strategy).

Beyond the RNG algorithm's own state, a future persistence format will likely also need to record runtime/format version and simulation-compatibility metadata alongside it — since this contract's reproducibility guarantee (§9) is explicitly scoped to a supported runtime version, resuming a campaign reliably after a runtime change is a compatibility concern the persistence layer must address, not something raw RNG state alone can solve. Conceptually, a future persistence record may need information similar to:

```text
RNG algorithm/state
runtime/format version
simulation compatibility metadata
```

This document does not design that format. It records the requirement so Issue 1's implementation choices remain compatible with it — in particular, preferring an underlying pseudo-random algorithm whose internal state is introspectable/serializable (e.g., a generator exposing something equivalent to `getstate()`/`setstate()`) over one that is opaque.

## 14. Path to Approval

This contract has been approved by the project owner, incorporating the refinements recorded in this revision. The decision record is `docs/decisions/DEC-0002-rng-contract.md`, which summarizes this contract and its rationale and references this document for full technical detail rather than duplicating it.

No RNG implementation exists yet, and none is created by this document. Implementation remains subject to the Pre-Code Development Gate as a whole (`ARCHITECTURE.md` §16) and requires separate, explicit authorization to begin.
