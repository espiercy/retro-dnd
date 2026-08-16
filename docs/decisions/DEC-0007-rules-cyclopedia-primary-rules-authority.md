# DEC-0007: Rules Cyclopedia as Primary Rules Authority

## Decision ID
DEC-0007

## Title
Rules Cyclopedia as Primary Rules Authority

## Status
Approved

## Date
2026-08-16

## Context

The project originally selected the 1974 three-book OD&D core (*Men & Magic*, *Monsters & Treasure*, *The Underworld & Wilderness Adventures*) as the ultimate mechanical authority, with the non-AD&D D&D lineage — Holmes, B/X, BECMI, and the Rules Cyclopedia, in that order — used only to complete gaps the 1974 text left ambiguous or unresolved (`SOURCE_HIERARCHY.md`, `GAME_CONSTITUTION.md` §2, `DEC-0001`).

Subsequent rules-card research and drafting — completed for `EXP-001` (Dungeon Wandering-Monster Check), `EXP-002` (Dungeon Turn / Time Accounting), and `EXP-004` (Resting Procedure), and reflected throughout `docs/rules/INVENTORY.md` — required close, page-verified engagement with the actual 1974 text. That engagement revealed that explicit 1974 mechanics differ materially from the rules desired for this simulator. Examples include foundational character/combat differences such as universal 1d6 weapon damage regardless of weapon type, and the absence of later-standard content such as the Thief class from the original three-book class roster (already noted as excluded from v1 core in `DEC-0006`).

The human project owner had not originally selected the 1974 rules from prior personal familiarity with that specific text, and, after reviewing what those rules actually require in practice, determined that the 1974 core is not an adequate primary rules baseline for the intended game. The project's underlying dungeon-crawler product vision (`GAME_CONSTITUTION.md` §1, §7) is unaffected by this finding — only the *source of mechanical truth* has proven unsuitable.

## Decision

**The Dungeons & Dragons Rules Cyclopedia becomes the primary and ultimate mechanical authority for the simulator, effective immediately.**

1. When the Rules Cyclopedia explicitly defines a mechanic, that mechanic governs the simulator. A conflicting earlier-edition rule does not override an explicit Rules Cyclopedia rule merely because it is chronologically older.
2. Alternate historical D&D sources — BECMI boxed-set material, B/X, Holmes, OD&D and its supplements, and other historically relevant D&D-lineage material where justified — may provide compatible completion where the Rules Cyclopedia is silent, ambiguous, or leaves an executable gap. This is not a rigid chronological requirement; a more directly relevant source may be consulted out of that order when justified and documented.
3. An alternate-source rule that contradicts an explicit Rules Cyclopedia mechanic is not silently imported as completion. If such a rule is nevertheless desired, it becomes an explicit, human-approved variant — documented as such — not ordinary historical completion.
4. Where no Rules Cyclopedia rule exists and no compatible alternate-source completion is found after research, a documented Simulator Ruling remains the fallback, exactly as before.
5. AD&D remains excluded by default, unchanged from prior policy.

The full revised hierarchy, compatibility vocabulary, and provenance categories are specified in the rewritten `SOURCE_HIERARCHY.md`, which this decision authorizes and which is the authoritative detailed statement of this policy going forward — this record summarizes the decision; it does not duplicate the mechanics of applying it.

## Rationale

A rules baseline that the project owner does not actually want to ship is not a sound foundation regardless of how much research discipline has been applied to documenting it faithfully. Discovering this mismatch through direct engagement with the source text — rather than assuming suitability from reputation alone — is exactly the kind of evidence a foundational course correction should be based on. The project's other governing disciplines (provenance transparency, no silent rules invention, human approval of ambiguity resolutions, deterministic testability, dungeon-crawler product focus) do not depend on which specific source is primary, and are retained unchanged; only the identity of the primary source changes.

## Consequences

- `SOURCE_HIERARCHY.md` is substantially rewritten: the active research-priority chain now begins with the Rules Cyclopedia; the compatibility vocabulary (Preserved / Compatible Completion / Evolved-Different / Conflicting / Human-Approved Variant) and the provenance categories (Rules Cyclopedia Explicit / Necessary Mathematical-Mechanical Consequence / Alternate-Source Compatible Completion / Simulator Ruling / Human-Approved Variant) are introduced there.
- `GAME_CONSTITUTION.md` and `AGENTS.md` are revised to state the Rules Cyclopedia as the canonical foundation and to instruct agents accordingly, while retaining every other governing principle (simulation-over-narration, deterministic testability, provenance discipline, no silent rules invention, human approval requirements, dungeon-crawler product focus, historical transparency).
- The 1974-only playable-content boundary (`DEC-0006`) is removed as active policy; `DEC-0006` is marked `Superseded` by this record (see `docs/decisions/INDEX.md`). The new V1 content boundary is Rules Cyclopedia content reachable through the intended V1 dungeon-crawler loop, re-scoped rather than assumed identical to the old three-book boundary.
- `docs/rules/INVENTORY.md`, `docs/rules/clusters/CLUSTER-001-dungeon-exploration-time.md`, and the three approved Rule Cards researched under the superseded 1974-primary policy (`EXP-001`, `EXP-002`, `EXP-004`) no longer carry implementation authority as-is. Each is marked `REVALIDATION_REQUIRED` (a new status introduced by this migration, defined in `DEVELOPMENT_WORKFLOW.md` and `docs/rules/_template.md`) rather than left silently `APPROVED`. Their prior research and human-approval history is preserved, not deleted — see each artifact's own added note.
- Historical-rules implementation authorization is **FROZEN** until: (1) a Rules Cyclopedia V1 Rules Inventory is approved; (2) affected cluster boundaries are approved/revalidated under that inventory; (3) all Rule Cards required by the first revised cluster are approved under the new hierarchy; (4) implementation readiness is (re-)approved for that cluster. No `APPROVED` metadata dated under the superseded policy bypasses this freeze.
- The cluster-based development workflow (`DEC-0005`), the RNG technical contract (`DEC-0002`), the Python toolchain/CI model (`DEC-0003`), and the testing strategy remain valid and are not superseded by this decision — none of them encodes an assumption specific to the 1974 baseline. `DEC-0001`'s "Historical Source Policy" summary bullets, which described the now-superseded 1974-primary policy, are superseded in substance by this record; `DEC-0001` itself already provides that its governing documents control where they and its summary differ, so `DEC-0001`'s own `Status` is not changed — only this narrower point within it is now stale, and this record is the cross-reference that documents that.
- Prior 1974 research is not discarded. It remains valuable as historical-lineage evidence, for understanding where Rules Cyclopedia mechanics came from, and as a candidate alternate-source completion input under the new hierarchy where genuinely compatible.
- A companion migration audit document, `docs/rules/RULESET_BASELINE_MIGRATION.md`, records the full scope of files reviewed and changed under this decision.

## Supersedes

`DEC-0006-v1-playable-content-scope.md`. This record's primary purpose is establishing the Rules Cyclopedia as the new primary rules authority; `DEC-0006`'s three-book playable-content boundary is directly invalidated by that change, since it depended entirely on the 1974 three-book core being primary. See that record's own `Status`/`Superseded By` fields and `docs/decisions/INDEX.md`, both already updated accordingly.

`DEC-0001-project-foundation-baseline.md` remains active overall — this record does not supersede it. Only `DEC-0001`'s "Historical Source Policy" summary subsection is superseded in substance by this record (see Consequences above); `DEC-0001`'s own `Status` is unchanged, per its own provision that its governing documents control where they and its summary differ.

## Superseded By

None.

---

## Historical Clarification / Addendum — 2026-08-16

*The following is an addendum, not a revision. It does not alter this record's Context, Decision, Rationale, Consequences, Supersedes, or Superseded By fields above, all of which remain exactly as originally adopted.*

Later review of the original project conversation established that the Rules Cyclopedia interpretation of D&D was the project's original intended rules target. The 1974-primary policy described in this decision's original Context above accurately reflects the repository's actual governing policy immediately before this decision — that period genuinely happened and is not erased by this addendum — but it did not reflect the project's original product intent. The OD&D-primary period is therefore understood as intervening governance drift, not as an earlier, equally-valid product direction that this decision replaced with a new one. This decision restored the originally intended Rules Cyclopedia baseline while preserving the historical record of the temporary 1974-primary policy, exactly as that record already stands above and in `docs/rules/RULESET_BASELINE_MIGRATION.md` §3.1.
