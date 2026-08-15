# DEC-0002: RNG Contract

## Decision ID
DEC-0002

## Title
RNG Contract — Single-Stream, Rules-Facing Dice Abstraction

## Status
Approved

## Date
2026-08-15

## Context

The project's RNG requirements were established in `ARCHITECTURE.md` §5 (single simulation-owned stream) and further specified in a draft technical contract, `docs/technical/RNG_CONTRACT.md`. The project owner reviewed that draft and approved its overall architecture, subject to refinements addressing: how `sequence_number` relates to underlying random draws, precise scoping of the deterministic-reproduction guarantee, and a small addition to the approved dice-expression grammar. This record captures the now-approved contract at a decision-log level; the full technical specification remains in `docs/technical/RNG_CONTRACT.md`.

## Decision

The following RNG architecture is approved:

- **Single simulation-owned RNG stream.** One RNG instance per campaign, seeded once at campaign start (`ARCHITECTURE.md` §5). No per-domain, per-procedure, per-entity, per-level, or per-encounter streams without a future approved architecture change.
- **All simulation randomness flows through the RNG boundary.** Historical rules procedures never call an uncontrolled random facility directly; presentation/narrative code never consumes the simulation RNG.
- **Two public, rules-facing operations** — a single-die roll and a dice-expression roll — both built on one private, internal "raw draw" primitive, so there is exactly one place in the system where a random number is actually drawn.
- **Rich, immutable roll results**, carrying the original expression/spec, individual die values, the applied modifier, the total, and a rules-visible `sequence_number` — never reduced to an opaque integer.
- **One `sequence_number` per public roll operation, not per underlying die.** A `3d6` call consumes three raw draws from the stream but is one rules-visible operation with one sequence number; the underlying draw count remains recoverable as `len(dice)`.
- **A deliberately small dice grammar**: `dS`, `NdS`, `NdS+M`, `NdS-M` only — no mixed pools, exploding dice, keep/drop syntax, multiple modifiers, or general percentile notation beyond `1d100`.
- **Two conforming implementations**: a seeded production RNG, and a scripted/deterministic fake RNG that accepts a controlled sequence of raw values and still exercises real aggregation logic on top of them; an exhausted scripted sequence fails explicitly rather than falling back to real randomness.
- **A scoped reproducibility guarantee**: determinism is guaranteed for the same supported Python/toolchain version + same seed/state + same consumption sequence — not promised indefinitely across arbitrary future runtime versions.
- **Strict separation from rules semantics.** The RNG knows dice; it does not know reaction tables, treasure, monster generation, attack/saving throws, survivability, or XP.
- **Explicit errors, never silent coercion**, for malformed expressions, invalid dice counts/sizes, unsupported notation, and exhausted scripted test sequences.
- **RNG-state persistence is recognized as a future requirement and explicitly deferred** — not designed or implemented now. A future persistence format will likely need RNG state plus runtime/format-version and compatibility metadata, not the seed alone.

## Rationale

A single shared, strictly-bounded RNG stream is what makes the simulation deterministic, testable, and auditable end-to-end (`GAME_CONSTITUTION.md` §12, `ARCHITECTURE.md` §5) without the complexity of coordinating multiple independent streams. Distinguishing "rules-visible operation" from "underlying raw draw" resolves a real tension: rules code and audit logs should read in terms of the rolls a historical procedure actually made (one entry for "3d6"), while the implementation must still account precisely for every unit of randomness consumed, since reordering or adding a single draw changes every subsequent result for the rest of the campaign. Keeping the dice grammar small and keeping the RNG ignorant of rules semantics both follow directly from the project's broader anti-scope-creep and separation-of-concerns principles (`ARCHITECTURE.md` §4, §13).

Major alternatives considered and rejected or deferred:

- **One sequence number per raw draw** (i.e., a `3d6` call producing four sequence numbers — three dice plus the aggregate) was rejected: it exposes internal implementation mechanics as if they were independent historical rolls, degrading audit-log readability for no offsetting benefit.
- **Multiple RNG streams** (per rules domain, procedure, entity, level, or encounter) remain rejected, consistent with the already-approved architecture (`ARCHITECTURE.md` §5) — not reopened by this decision.
- **An unscoped, cross-version reproducibility guarantee** ("a seed alone reproduces a campaign forever, regardless of future Python/runtime changes") was rejected as an overpromise; the guarantee is scoped to the project's supported runtime version instead.
- **A general-purpose dice-notation language** (mixed pools, exploding dice, keep/drop syntax) was deferred rather than built pre-emptively; the grammar expands only when an approved Rule Card actually requires it.
- **A full roll-history/audit subsystem** was deferred in favor of the minimal roll-result-plus-event-embedding pattern, pending real debugging experience showing it is insufficient.

## Consequences

- Implementers of Issue 1 must build the two-tier internal design (private raw draw + two public sequence-numbered operations) rather than a simpler design where every die roll is independently sequenced.
- Any future need for multiple RNG streams, a broader dice grammar, or cross-version campaign reproducibility must be raised as a new decision, not assumed available under this one.
- RNG-state persistence remains an open implementation question for whenever `ARCHITECTURE.md` §7's persistence boundary is actually built; this decision does not resolve it, only flags it.
- The full mechanical/technical detail governing implementation remains `docs/technical/RNG_CONTRACT.md`; this record does not replace it.

## Supersedes

None.

## Superseded By

None.
