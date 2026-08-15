# Retro D&D Simulator — Rules Source Hierarchy

## 1. Purpose

This document defines how the project resolves incomplete or ambiguous rules while preserving the 1974 Dungeons & Dragons game as the simulator's canonical foundation.

The goal is not to recreate a later edition. The goal is to construct the most defensible executable interpretation of the 1974 game using later D&D material only when necessary to complete missing behavior.

## 2. Governing Principle

Use the 1974 rule whenever one exists.

Where 1974 does not completely specify behavior, search forward through the non-AD&D Dungeons & Dragons lineage for the earliest complete treatment of the exact unresolved question.

Import only the portions that are compatible with what the earlier rule already establishes.

A later rule may clarify an omission. It may not silently overwrite an explicit 1974 rule.

## 3. Source Order

Research should normally proceed in this order:

1. **1974 Dungeons & Dragons core rules**
   - *Men & Magic*
   - *Monsters & Treasure*
   - *The Underworld & Wilderness Adventures*

2. **Explicit dependencies or procedures directly invoked by the 1974 rules**
   - Example: *Chainmail* where the 1974 rules explicitly depend upon it.
   - Other externally referenced material should be evaluated individually.

3. **Other original-D&D-era material**
   - Use only when it answers the unresolved question without contradicting the 1974 core.
   - Supplements are not assumed to override the core automatically.

4. **Holmes Basic D&D**
   - Consult for the earliest compatible complete treatment when applicable.

5. **B/X D&D**
   - Consult when earlier approved sources do not fully resolve the question.

6. **BECMI D&D**
   - Consult when earlier approved sources remain incomplete.

7. **Rules Cyclopedia**
   - Principal consolidated fallback for the non-AD&D D&D lineage.
   - Particularly useful as an implementation reference when its treatment remains compatible with the 1974 foundation.

8. **Simulator Ruling**
   - Used when no approved historical source provides a complete compatible answer.

## 4. AD&D Exclusion

AD&D is outside the normal research chain.

Do not consult or import AD&D rules merely because they provide a complete treatment.

If the D&D lineage fails to answer an indispensable question, prefer a documented Simulator Ruling.

An AD&D rule may be considered only when the human project owner explicitly authorizes that specific exception.

## 5. Clause-by-Clause Compatibility

Later rules must not be imported wholesale simply because a 1974 rule is ambiguous.

Break the unresolved behavior into individual questions.

For each question:

1. Record what 1974 explicitly establishes.
2. Record the exact unresolved behavior.
3. Find the earliest later D&D treatment that addresses that behavior.
4. Test that treatment for compatibility with the 1974 rule.
5. Import, modify, reject, or escalate to a Simulator Ruling.

A later source may be accepted for one part of a rule and rejected for another.

## 6. Clarification vs. Revision

A later source must be evaluated as either:

- **Clarification/completion** — adds behavior where the earlier rule was silent while preserving the established effect; or
- **Revision** — changes the power, scope, assumptions, or operation of the earlier rule.

Clarifications may be imported when compatible.

Revisions may not replace explicit 1974 behavior without a deliberate human design decision.

## 7. Rules Cyclopedia Policy

The Rules Cyclopedia is a favored reference because it consolidates the Basic D&D lineage into a mature and comparatively complete rules system.

However:

- it is not the simulator's canonical ruleset;
- it does not override explicit 1974 rules;
- it should normally be used only after earlier compatible D&D treatments have been considered;
- its mechanics may be adapted or partially imported when necessary to remain compatible with 1974.

## 8. Practical Research Approach (Hybrid Method)

The full clause-by-clause lineage walk in §5 is required for consequential ambiguities — cases where later material could materially alter the power, scope, or operation of the 1974 game. It is not required for every rule.

In practice:

- For consequential ambiguities, or anywhere later rules may materially alter the 1974 game, trace the historical lineage from the earliest relevant D&D source forward, in the order given in §3, before considering the Rules Cyclopedia.
- Once compatibility has been established for a given piece of behavior, the Rules Cyclopedia may be used freely as a consolidated implementation reference for that behavior — its wording and mechanical presentation are often the most implementation-ready.
- Do not perform unnecessary genealogical research for a trivial rule whose later treatment is clearly and uncontroversially compatible with the 1974 core.
- Do not jump directly to the Rules Cyclopedia when doing so could conceal a substantive rules evolution — i.e., when it has not yet been established whether the later treatment is a clarification or a revision (§6).
- Continue to exclude AD&D by default (§4) regardless of how this hybrid approach is applied.

A spell such as *Charm Person* is a representative example of a future high-scrutiny rule: its duration, means of ending, and interaction with other effects changed materially across editions, so a Rule Card for it should receive the full lineage treatment rather than a direct jump to a later consolidated source.

## 9. Required Rule Documentation

Each nontrivial or ambiguous rule should eventually have a Rule Card containing:

- Rule ID
- Status
- 1974 source
- What 1974 establishes
- What 1974 leaves undefined
- Completion sources examined
- Compatibility analysis
- Approved simulator interpretation
- Mechanical specification
- Test cases
- Provenance classification

The `Status` field is a formal implementation gate, not a descriptive label: a Rule Card is not authoritative, and must not be implemented, until a human project owner sets Status to `APPROVED` (see `ARCHITECTURE.md` §12 and `AGENTS.md` §2). The required field list and full Status lifecycle are maintained at `docs/rules/_template.md`, which is authoritative on the exact shape of a Rule Card.

## 10. Default Research Outcome

When uncertainty remains, do not guess.

The correct agent behavior is:

> identify the unresolved rule → document the ambiguity → stop implementation at that boundary → request a human ruling

Historical uncertainty is preferable to false certainty.
