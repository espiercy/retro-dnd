# Rule Card Template

> This is the required shape of an authoritative Rule Card (`SOURCE_HIERARCHY.md` §9). Copy this file to draft a new Rule Card; do not edit this template in place.
>
> This template is governance/specification documentation, not production code. It — and Rule Cards drafted from it — may exist, be researched, and be drafted before the Pre-Code Development Gate (`ARCHITECTURE.md` §16) clears. **Implementing** a Rule Card's approved mechanical specification is production code and remains blocked until that gate clears, regardless of the Rule Card's own approval status.

---

## Rule ID

<!-- Short, stable, unique identifier, e.g. ENC-001. Never reused, even if a card is abandoned. -->

## Title

<!-- Short human-readable name, e.g. "Wandering Monster Check (Dungeon Level 1)". -->

## Status

<!-- One of: DRAFT, RESEARCHED, AWAITING_APPROVAL, APPROVED, IMPLEMENTED, VERIFIED.
     See "Status Lifecycle" at the bottom of this file. Only APPROVED (or a later status)
     authorizes implementation, and only a human project owner may set it. -->

## Rules Domain

<!-- e.g. exploration, encounters, combat, magic, monsters, treasure, character_creation -->

---

## 1974 Source

<!-- Citation(s) to the specific 1974 text — Men & Magic / Monsters & Treasure /
     The Underworld & Wilderness Adventures — with page/section reference where possible. -->

## 1974 Explicitly Establishes

<!-- What the 1974 text actually and sufficiently specifies, stated precisely. -->

## 1974 Leaves Undefined

<!-- The exact unresolved behavior. Be as narrow as possible — do not describe an entire
     rule as "undefined" when only one clause of it is. -->

---

## Completion Research

<!-- Only if 1974 leaves the behavior undefined: the non-AD&D D&D lineage sources examined,
     in the order given in SOURCE_HIERARCHY.md §3, and what each source says about the exact
     unresolved question. Follow the hybrid research approach in SOURCE_HIERARCHY.md §8.
     Omit or mark "Not applicable — 1974 fully explicit" when 1974 is fully explicit. -->

## Compatibility Analysis

<!-- For each later-source candidate considered: clarification/completion vs. revision
     (SOURCE_HIERARCHY.md §6), and whether it is compatible with what 1974 already establishes. -->

---

## Simulator Ruling

<!-- Only if required — i.e., no compatible historical completion exists
     (SOURCE_HIERARCHY.md §3 item 8, GAME_CONSTITUTION.md §3). State the ruling and why no
     historical source resolved it. Write "Not applicable." if no ruling was required. -->

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

<!-- One of the categories in GAME_CONSTITUTION.md §5:
     1974 Explicit / 1974 Interpreted / D&D Completion / Rules Cyclopedia Completion /
     Simulator Ruling. -->

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
APPROVED          — set only by a human project owner; authorizes implementation
      ↓
IMPLEMENTED       — mechanical specification implemented per DEVELOPMENT_WORKFLOW.md
      ↓
VERIFIED          — implementation's tests and required verification have passed
                     (TESTING_STRATEGY.md §9–§10)
```

Only a Rule Card explicitly set to `APPROVED` (or a later status) by a human project owner may authorize rules implementation (`SOURCE_HIERARCHY.md` §9, `ARCHITECTURE.md` §12, `AGENTS.md` §2). An approved Rule Card does not, by itself, override the project-level Pre-Code Development Gate (`ARCHITECTURE.md` §16).
