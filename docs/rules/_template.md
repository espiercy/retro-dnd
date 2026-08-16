# Rule Card Template

> This is the required shape of an authoritative Rule Card (`SOURCE_HIERARCHY.md` §9). Copy this file to draft a new Rule Card; do not edit this template in place.
>
> This template is governance/specification documentation, not production code. It — and Rule Cards drafted from it — may exist, be researched, and be drafted before the Pre-Code Development Gate (`ARCHITECTURE.md` §16) clears. **Implementing** a Rule Card's approved mechanical specification is production code and remains blocked until that gate clears, regardless of the Rule Card's own approval status.
>
> **Migration note (2026-08-16).** This template was revised under `DEC-0007-rules-cyclopedia-primary-rules-authority.md` to reflect the Rules Cyclopedia as primary rules authority, replacing the prior 1974-primary section names and provenance categories. See `docs/rules/RULESET_BASELINE_MIGRATION.md`. Rule Cards drafted under the prior template (`EXP-001`, `EXP-002`, `EXP-004`) are not retroactively reformatted to this shape as part of the migration itself — see each card's own `REVALIDATION_REQUIRED` note.

---

## Rule ID

<!-- Short, stable, unique identifier, e.g. ENC-001. Never reused, even if a card is abandoned. -->

## Title

<!-- Short human-readable name, e.g. "Wandering Monster Check (Dungeon Level 1)". -->

## Status

<!-- One of: DRAFT, RESEARCHED, AWAITING_APPROVAL, APPROVED, REVALIDATION_REQUIRED, IMPLEMENTED, VERIFIED.
     See "Status Lifecycle" at the bottom of this file. Only APPROVED (or a later status other than
     REVALIDATION_REQUIRED) authorizes implementation, and only a human project owner may set it. -->

## Rules Domain

<!-- e.g. exploration, encounters, combat, magic, monsters, treasure, character_creation -->

---

## Rules Cyclopedia Source

<!-- Citation(s) to the specific Rules Cyclopedia text — edition/printing, section, and page
     reference where possible. -->

## Rules Cyclopedia Explicitly Establishes

<!-- What the Rules Cyclopedia text actually and sufficiently specifies, stated precisely. -->

## Rules Cyclopedia Leaves Undefined / Ambiguous

<!-- The exact unresolved behavior. Be as narrow as possible — do not describe an entire
     rule as "undefined" when only one clause of it is. -->

---

## Alternate-Source Completion Research

<!-- Only if the Rules Cyclopedia leaves the behavior undefined or ambiguous: the alternate
     non-AD&D D&D-lineage sources examined, in the order given in SOURCE_HIERARCHY.md §3, and
     what each source says about the exact unresolved question. Follow the hybrid research
     approach in SOURCE_HIERARCHY.md §8. Omit or mark "Not applicable — Rules Cyclopedia fully
     explicit" when the Rules Cyclopedia is fully explicit. -->

## Compatibility Analysis

<!-- For each alternate-source candidate considered, classify it using SOURCE_HIERARCHY.md §6's
     compatibility vocabulary: Preserved / Compatible Completion / Evolved-Different / Conflicting.
     A Conflicting finding cannot be imported as ordinary completion — see "Human-Approved Variant"
     below if the conflicting behavior is nonetheless desired. -->

---

## Simulator Ruling

<!-- Only if required — i.e., no compatible alternate-source completion exists
     (SOURCE_HIERARCHY.md §3 item 7, GAME_CONSTITUTION.md §3). State the ruling and why no
     alternate source resolved it. Write "Not applicable." if no ruling was required. -->

## Human-Approved Variant

<!-- Only if the project owner deliberately chooses a mechanic that conflicts with, or is
     otherwise non-canonical relative to, an explicit Rules Cyclopedia rule (SOURCE_HIERARCHY.md
     §7). Must document: (1) the explicit Rules Cyclopedia rule being deviated from; (2) the
     chosen alternate behavior; (3) its source/provenance, if any; (4) why the project
     intentionally deviates; (5) explicit human approval (name/date), distinct from ordinary
     Rule Card approval below. This section must remain uncommon — write "Not applicable." when
     no variant is in effect, which is expected for the overwhelming majority of Rule Cards. No
     implementation agent may create an entry here on its own authority. -->

---

## Approved Mechanical Specification

<!-- The precise, implementable mechanical procedure: inputs, steps, tables, formulas,
     outputs. Precise enough that an implementation agent can code from it without
     inventing mechanics (ARCHITECTURE.md §12). -->

---

## Deterministic Test Cases

<!-- Concrete input → expected-output cases. Cover, where applicable: every outcome/branch,
     boundary values, minimum and maximum die results, modifiers and exceptions,
     success/failure paths, explicitly prohibited behavior, interactions with other
     procedures, historical edge cases, and survivability-policy interactions where this
     procedure is one of the limited set permitted to accept a survivability policy.

     These test cases are part of the implementation's acceptance criteria
     (TESTING_STRATEGY.md §2) — a mechanical clause should not be approved without enough
     test specification here to establish its intended behavior. -->

## Provenance Classification

<!-- One of the categories in GAME_CONSTITUTION.md §5 / SOURCE_HIERARCHY.md §10:
     Rules Cyclopedia Explicit / Necessary Mathematical-Mechanical Consequence /
     Alternate-Source Compatible Completion / Simulator Ruling / Human-Approved Variant. -->

---

## Open Questions

<!-- Anything still unresolved that does not block approval of the specification above,
     or that should be revisited later. Write "None." if there are none. -->

## Approval

<!-- Set by the human project owner only. -->

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

`REVALIDATION_REQUIRED` is not a failure state and does not imply the card's research was wrong — see `DEVELOPMENT_WORKFLOW.md` §9.7 for its exact meaning and the revalidation workflow. A card in this status must not be implemented, and any code previously implemented against it must be treated as suspect pending revalidation (`ARCHITECTURE.md` §15.2) — no historical-rules production code has actually required this treatment as of the 2026-08-16 migration, since none had been implemented yet.
