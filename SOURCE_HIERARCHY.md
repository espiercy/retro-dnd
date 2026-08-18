# Retro D&D Simulator — Rules Source Hierarchy

> **Migration note (2026-08-16).** This document was rewritten under `DEC-0007-rules-cyclopedia-primary-rules-authority.md`. It previously established the 1974 three-book OD&D core as primary authority, with the Rules Cyclopedia treated only as a downstream completion/reference source. That policy is superseded. See `docs/rules/RULESET_BASELINE_MIGRATION.md` for the full migration record and `docs/decisions/INDEX.md` for the decision history.

## 1. Purpose

This document defines how the project resolves incomplete or ambiguous rules while preserving the *Dungeons & Dragons Rules Cyclopedia* as the simulator's canonical mechanical foundation.

The goal is to construct the most defensible, historically grounded executable interpretation of the D&D game the Rules Cyclopedia defines, using earlier and adjacent D&D-lineage material only when necessary to complete missing or ambiguous behavior — never to override an explicit Rules Cyclopedia mechanic merely because an earlier source is older or more historically primary.

## 2. Governing Principle

Use the Rules Cyclopedia's rule whenever one exists.

Where the Rules Cyclopedia does not completely specify behavior, search the alternate non-AD&D D&D lineage for the highest-priority, most directly relevant compatible treatment under §3.

Import only the portions that are compatible with what the Rules Cyclopedia already establishes.

An alternate source may clarify an omission or fill a gap. It may **not** silently override an explicit Rules Cyclopedia rule. A conflicting earlier-edition rule does not take precedence merely because it is chronologically older or was part of the project's superseded 1974-primary governance baseline.

## 3. Source Order

Research should normally proceed in this order:

1. **The Dungeons & Dragons Rules Cyclopedia** — the primary and ultimate mechanical authority for the simulator.

2. **Explicit external dependencies the Rules Cyclopedia itself invokes**, if research identifies one — evaluated individually, the same way *Chainmail* was treated as an explicit OD&D-era dependency under the prior policy.

3. **BECMI boxed-set material** (Basic/Expert/Companion/Masters/Immortals) — the direct lineage ancestor the Rules Cyclopedia consolidates; often the most directly relevant completion source for a Rules Cyclopedia gap.

4. **B/X D&D** (Moldvay Basic / Cook Expert) — consult when BECMI material does not resolve the question.

5. **Holmes Basic D&D, original 1974 OD&D, and OD&D-era supplements** — consult when earlier-listed sources do not resolve the question. This tier is now a *completion* source, not the primary authority it was under the superseded policy — see `docs/rules/RULESET_BASELINE_MIGRATION.md` for why that changed.

6. **Other historically relevant D&D-lineage material**, where a specific source is demonstrably more directly relevant to the exact unresolved question than the ordering above would suggest. This list is a practical default, not a rigid chronology requirement — document the reason a source is used out of its default position.

7. **Simulator Ruling** — used when no source in the alternate D&D lineage provides a complete, compatible answer.

## 4. AD&D Exclusion

AD&D is outside the normal research chain.

Do not consult or import AD&D rules merely because they provide a complete treatment.

If the non-AD&D D&D lineage fails to answer an indispensable question, prefer a documented Simulator Ruling.

An AD&D rule may be considered only when the human project owner explicitly authorizes that specific exception.

## 5. Clause-by-Clause Compatibility

Later or earlier alternate-source rules must not be imported wholesale simply because a Rules Cyclopedia rule is ambiguous or silent.

Break the unresolved behavior into individual questions.

For each question:

1. Record what the Rules Cyclopedia explicitly establishes.
2. Record the exact unresolved behavior.
3. Find the most relevant alternate-source treatment that addresses that behavior, per the order in §3.
4. Test that treatment for compatibility with the Rules Cyclopedia rule, using the vocabulary in §6.
5. Import, modify, reject, or escalate to a Simulator Ruling — or, if a conflicting rule is nonetheless desired, route it to the Human-Approved Variant process (§7).

An alternate source may be accepted for one part of a rule and rejected for another.

## 6. Compatibility Vocabulary

Every alternate-source comparison against the Rules Cyclopedia must be classified as exactly one of the following:

- **Preserved** — the alternate source materially matches the Rules Cyclopedia mechanic. Useful as corroboration; imports nothing new.
- **Compatible Completion** — the Rules Cyclopedia leaves a genuine gap, and the alternate source supplies executable detail without contradicting anything the Rules Cyclopedia explicitly establishes. May be imported.
- **Evolved / Different** — the alternate source belongs to the same D&D lineage but materially differs from the Rules Cyclopedia mechanic (a different edition's own design choice, not a gap-filling clarification). Historically useful — for lineage research, understanding where a Rules Cyclopedia mechanic came from, or as a candidate Human-Approved Variant — but **not** automatically importable as ordinary completion.
- **Conflicting** — the alternate rule directly contradicts an explicit Rules Cyclopedia mechanic. Cannot serve as ordinary completion under any circumstance. May only become active through the Human-Approved Variant process (§7), never silently.
- **Human-Approved Variant** — see §7. Not a research finding; a project-owner decision.

This vocabulary replaces the prior "clarification/completion vs. revision" framing with a finer-grained set of categories, since the *direction* of authority has changed (alternate sources completing the Rules Cyclopedia, not the Rules Cyclopedia completing 1974) and a single completion/revision binary was not precise enough for the added "Evolved/Different" and "Human-Approved Variant" cases this migration introduces.

## 7. Human-Approved Variant

A **Human-Approved Variant** is a deliberate, explicit project-owner decision to use a mechanic that conflicts with an explicit Rules Cyclopedia rule, or that is otherwise non-canonical relative to it (an earlier-edition procedure the owner prefers, an optional rule, a project-specific house rule, or a historically plausible alternative the owner wants regardless of Rules Cyclopedia precedent).

This category must remain explicit and uncommon — it exists so a deliberate deviation is visible and auditable, not so deviations become routine.

A Human-Approved Variant must document, at minimum:

1. the explicit Rules Cyclopedia rule being deviated from;
2. the chosen alternate behavior;
3. the source/provenance of the alternative, if any;
4. why the project intentionally deviates;
5. explicit human approval (name/date), distinct from ordinary Rule Card approval.

No implementation agent may create a Human-Approved Variant on its own authority. An agent may identify a candidate (e.g., an "Evolved/Different" comparison worth flagging) and recommend it for human consideration, exactly as it may propose a Simulator Ruling — it may not adopt one unilaterally.

No Human-Approved Variant exists yet as of this document's current revision. At present, the Rules Cyclopedia governs without exception across every researched rule.

## 8. Alternate-Source Research Approach (Hybrid Method)

The full clause-by-clause lineage walk in §5 is required for consequential ambiguities — cases where an alternate source could materially alter the power, scope, or operation of the game as the Rules Cyclopedia defines it. It is not required for every rule.

In practice:

- For consequential ambiguities, or anywhere an alternate source may materially alter Rules Cyclopedia behavior, trace the alternate lineage from the most directly relevant source forward, in the order given in §3, applying the §6 vocabulary at each step.
- Do not perform unnecessary genealogical research for a trivial gap whose alternate-source treatment is clearly and uncontroversially a Compatible Completion.
- Do not jump directly to a distant or loosely related source when doing so could conceal whether the material is actually a Compatible Completion or an Evolved/Different mechanic (§6) — that determination must be made explicitly, not assumed.
- Continue to exclude AD&D by default (§4) regardless of how this hybrid approach is applied.
- Where the superseded policy's own research already exists for a topic (e.g., prior 1974-primary Rule Card research), that research is not discarded — it becomes candidate alternate-source material to be re-evaluated against the Rules Cyclopedia using the §6 vocabulary, not re-derived from scratch. See `docs/rules/RULESET_BASELINE_MIGRATION.md` §"Preserve Existing Historical Research."

## 9. Required Rule Documentation

Each nontrivial or ambiguous rule should eventually have a Rule Card containing:

- Rule ID
- Status
- Rules Cyclopedia source
- What the Rules Cyclopedia establishes
- What the Rules Cyclopedia leaves undefined or ambiguous
- Alternate-source completion research examined, classified per §6
- Compatibility analysis
- Simulator Ruling, where required
- Human-Approved Variant, where applicable
- Approved mechanical specification
- Test cases
- Provenance classification

The `Status` field is a formal implementation gate, not a descriptive label: a Rule Card is not authoritative, and must not be implemented, until a human project owner sets Status to `APPROVED` (see `ARCHITECTURE.md` §12 and `AGENTS.md` §2). A Rule Card previously `APPROVED` under a since-superseded source authority does not retain implementation authority merely because its file still says `APPROVED` — see `DEVELOPMENT_WORKFLOW.md` §9.7 for the `REVALIDATION_REQUIRED` status this migration introduces for exactly that situation. The required field list and full Status lifecycle are maintained at `docs/rules/_template.md`, which is authoritative on the exact shape of a Rule Card.

## 10. Provenance Categories

Every implemented rule should be traceable to one of the following (`GAME_CONSTITUTION.md` §5 restates these as the product-facing provenance requirement):

- **Rules Cyclopedia Explicit** — directly and sufficiently specified by the Rules Cyclopedia.
- **Necessary Mathematical/Mechanical Consequence** — an unavoidable executable consequence of a Rules Cyclopedia Explicit rule (e.g., a stated ratio implying a per-unit value), not an independently sourced fact in its own right.
- **Alternate-Source Compatible Completion** — imported from BECMI, B/X, Holmes, OD&D, or another historically relevant non-AD&D D&D source (§3) to fill a genuine Rules Cyclopedia gap, classified as a Compatible Completion under §6.
- **Simulator Ruling** — behavior required by the simulation but not resolved by the Rules Cyclopedia or any compatible alternate source; documented per §11.
- **Human-Approved Variant** — a deliberate, documented deviation from an explicit Rules Cyclopedia rule, per §7.

## 11. Default Research Outcome

When uncertainty remains, do not guess.

The correct agent behavior is:

> identify the unresolved rule → document the ambiguity → stop implementation at that boundary → request a human ruling

Historical uncertainty is preferable to false certainty.
