# DEC-0001: Project Foundation Baseline

## Decision ID
DEC-0001

## Title
Project Foundation Baseline

## Status
Approved

## Date
2026-08-15

## Context

Before any production code was written, the project's human owner and an implementation agent conducted a multi-round architecture and governance review covering `ARCHITECTURE.md`, `GAME_CONSTITUTION.md`, `SOURCE_HIERARCHY.md`, `AGENTS.md`, `DEVELOPMENT_WORKFLOW.md`, and `TESTING_STRATEGY.md`. That review produced a large set of interlocking decisions about game identity, historical-source policy, architecture, testing, and development governance.

This record does not attempt to reconstruct every individual exchange of that review. It exists to give the project a single, durable, at-a-glance summary of the foundational decisions in force as of this record's date, each of which is fully specified in its authoritative governing document. Where this summary and a governing document ever appear to differ, the governing document controls.

## Decision

The following principles are adopted as the project's foundation:

**Game Identity**
- The game is a faithful simulation of original 1974 Dungeons & Dragons (`GAME_CONSTITUTION.md` §1–2).
- It is primarily a dungeon crawler with emergent campaign history, not a required epic overarching story (`GAME_CONSTITUTION.md` §7).
- Historical random-generation procedures (monsters, treasure, encounters, etc.) are preserved where available rather than replaced with modern abstractions (`GAME_CONSTITUTION.md` §6).

**Historical Source Policy**
- 1974 OD&D is authoritative where explicit (`GAME_CONSTITUTION.md` §2, `SOURCE_HIERARCHY.md` §2).
- Missing behavior is completed through the non-AD&D D&D lineage when compatible (`SOURCE_HIERARCHY.md` §3, §5).
- The Rules Cyclopedia is a favored consolidated implementation reference once compatibility with 1974 has been established (`SOURCE_HIERARCHY.md` §7, §8).
- Consequential ambiguity requires tracing the historical lineage rather than jumping directly to a consolidated later source (`SOURCE_HIERARCHY.md` §8).
- AD&D is excluded by default unless a human explicitly authorizes a specific exception (`GAME_CONSTITUTION.md` §4, `SOURCE_HIERARCHY.md` §4).

**Rules Ambiguity**
- Ambiguity is identified and reported, never silently resolved (`GAME_CONSTITUTION.md` §3, `AGENTS.md` §3).
- Approved Rule Cards govern executable rules behavior (`GAME_CONSTITUTION.md` §5, `AGENTS.md` §2).
- Human approval (Status: `APPROVED`) is required before a Rule Card may be implemented (`SOURCE_HIERARCHY.md` §9, `docs/rules/_template.md`).

**Encounter Philosophy**
- An encounter does not imply combat (`GAME_CONSTITUTION.md` §6, `ARCHITECTURE.md` §9).
- Surprise, reaction, morale, pursuit/evasion, negotiation, retreat, and combat remain independently meaningful, independently testable procedures where historically appropriate (`ARCHITECTURE.md` §4, §9).

**Survivability**
- Optional survivability accommodations are permitted and may soften authorized encounter/trap characteristics (`GAME_CONSTITUTION.md` §8).
- Survivability settings do not increase treasure or XP income (`GAME_CONSTITUTION.md` §8).
- Treasure-generation and XP-award procedures are structurally isolated from survivability settings — they accept no survivability parameter and expose no ordinary code path for modification (`ARCHITECTURE.md` §10).
- Survivability must not indirectly manipulate reward opportunity through rerolling or suppression of canonical results (`GAME_CONSTITUTION.md` §8, `ARCHITECTURE.md` §10).

**Simulation Authority**
- Simulation state and rules outcomes are authoritative (`GAME_CONSTITUTION.md` §10, `ARCHITECTURE.md` §2).
- Presentation/narrative is downstream and may not rewrite mechanical reality (`ARCHITECTURE.md` §11).
- Events describe committed outcomes; the project is not currently committing to full event sourcing (`ARCHITECTURE.md` §8).

**Persistence**
- Campaign/dungeon consequences persist (`GAME_CONSTITUTION.md` §11).
- Persistence is an architectural boundary from the beginning of the project (`ARCHITECTURE.md` §7).
- No database or storage technology is yet selected.
- Domain state must not be shaped around a particular storage implementation (`ARCHITECTURE.md` §7).

**RNG**
- One simulation-owned RNG stream is used initially; no per-procedure or per-entity streams without an approved architecture change (`ARCHITECTURE.md` §5).
- All randomness flows through the controlled, injectable abstraction (`ARCHITECTURE.md` §5, `AGENTS.md` §7).
- The RNG must be seedable, injectable, deterministic, and testable (`ARCHITECTURE.md` §5).
- The future RNG design should preserve meaningful information about individual random results (e.g., constituent dice, not only a final total), not merely the campaign seed. The exact representation is deferred to a future RNG technical design task.

**Development Governance**
- No production code before the Pre-Code Development Gate clears (`ARCHITECTURE.md` §16).
- Implementation occurs through small, dependency-ordered, bounded issues (`ARCHITECTURE.md` §15).
- Completed implementation work requires a permanent completion record (`DEVELOPMENT_WORKFLOW.md`).
- Comprehensive automated testing is part of implementation, not a later cleanup activity (`TESTING_STRATEGY.md` §1).
- Coverage and verification requirements become hard automated CI/build gates once the toolchain is selected; a failed mandatory gate fails the build (`TESTING_STRATEGY.md` §9).
- Protected authority and process documents cannot be autonomously modified by an implementation agent; changes require explicit human direction (`AGENTS.md` §12).

## Rationale

These decisions were adopted to keep the simulator historically defensible, auditable, and resistant to silent rules drift or scope creep, while avoiding premature architectural or technological commitments before any code exists. Each principle above traces to a specific governing document, which remains the authoritative source; this record exists so the *set* of foundational decisions can be reviewed and referenced as a whole, without requiring anyone to reconstruct it from conversation history.

## Consequences

- All future implementation work is bound by the Pre-Code Development Gate and the governing documents cited above.
- Future decisions that materially change any of the principles above should be recorded as new decision records that supersede the relevant part of this baseline, rather than by editing this record after the fact (see `DEVELOPMENT_WORKFLOW.md` §9.4).
- This record does not itself authorize any implementation; the gate items listed in `ARCHITECTURE.md` §16 still govern when production code may begin.

## Supersedes

None.

## Superseded By

None.
