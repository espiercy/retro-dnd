# Retro D&D Simulator — Game Constitution

> **Migration note (2026-08-16).** Sections 1, 2, 3, 4, and 5 below were revised under `DEC-0007-rules-cyclopedia-primary-rules-authority.md`, which replaced the 1974 three-book OD&D core with the *Dungeons & Dragons Rules Cyclopedia* as the simulator's primary rules authority. See `docs/rules/RULESET_BASELINE_MIGRATION.md` for the full migration record. Every other section of this document is unaffected and retained as originally adopted.

## 1. Purpose

Retro D&D Simulator is a computer game intended to simulate the procedures, uncertainty, danger, and emergent play of a retro Dungeons & Dragons dungeon crawler, grounded primarily in the *Dungeons & Dragons Rules Cyclopedia*, using historically compatible alternate D&D sources where necessary to complete or clarify the executable rules, as faithfully as practical.

The primary game experience is dungeon crawling. The game does not require an epic or overarching narrative. Campaign history should emerge from expeditions, exploration, encounters, treasure recovery, character advancement, death, survival, and the persistent consequences of player decisions.

## 2. Rules-Cyclopedia Fidelity

The *Dungeons & Dragons Rules Cyclopedia* is the canonical mechanical foundation of the simulator.

When a rule is explicitly and sufficiently defined in the Rules Cyclopedia, that rule must be preserved. It may not be replaced merely because an earlier or later source is more familiar, more historically primary, or easier to implement — including the project's own prior 1974-primary research, which remains valuable as historical and alternate-source material but no longer defines game behavior on its own authority (`SOURCE_HIERARCHY.md` §3, §10).

The simulator must not silently deviate from the Rules Cyclopedia's explicit mechanics without an explicit, documented Human-Approved Variant (`SOURCE_HIERARCHY.md` §7).

## 3. Ambiguity Is a First-Class Design Concern

The Rules Cyclopedia is not complete in all areas. Ambiguity must be identified rather than hidden.

When implementation requires behavior that the Rules Cyclopedia does not fully define:

1. Determine precisely what the Rules Cyclopedia establishes.
2. Determine precisely what remains undefined or ambiguous.
3. Consult the project's source hierarchy (`SOURCE_HIERARCHY.md` §3) for the most relevant compatible alternate-source completion.
4. Import only behavior that is compatible with the Rules Cyclopedia rule already established, classified per `SOURCE_HIERARCHY.md` §6.
5. If no compatible completion exists, create a documented Simulator Ruling.

No coding agent may silently resolve rules ambiguity, and no coding agent may silently substitute an earlier-edition preference for an explicit Rules Cyclopedia rule.

## 4. D&D Lineage, Not AD&D

The project belongs to the Dungeons & Dragons lineage that the Rules Cyclopedia consolidates — BECMI, B/X, Holmes, and original OD&D and its supplements are its alternate-source completion lineage (`SOURCE_HIERARCHY.md` §3).

AD&D rules are excluded by default. They may not be used as implementation authority unless a specific exception is explicitly approved by the human project owner.

If the non-AD&D D&D lineage does not provide a compatible answer, a documented Simulator Ruling is preferred to importing AD&D behavior.

## 5. Rules Provenance

Every implemented rule should be traceable to one of the following provenance categories (`SOURCE_HIERARCHY.md` §10):

- **Rules Cyclopedia Explicit** — directly and sufficiently specified by the Rules Cyclopedia.
- **Necessary Mathematical/Mechanical Consequence** — an unavoidable executable consequence of a Rules Cyclopedia Explicit rule.
- **Alternate-Source Compatible Completion** — completed from an approved source in the non-AD&D D&D lineage where the Rules Cyclopedia leaves a gap.
- **Simulator Ruling** — behavior required by the simulation but not satisfactorily resolved by the Rules Cyclopedia or any compatible alternate source.
- **Human-Approved Variant** — a deliberate, documented deviation from an explicit Rules Cyclopedia rule, approved by the human project owner (`SOURCE_HIERARCHY.md` §7).

Rules provenance is part of the product, not merely developer documentation.

## 6. Historical Procedures Must Be Preserved

When historical procedures exist, they must be implemented rather than replaced with modern abstractions.

This includes, when applicable:

- character generation;
- dungeon exploration turns;
- wandering-monster checks;
- monster generation tables;
- number appearing;
- surprise;
- encounter distance;
- reaction rolls;
- morale;
- pursuit and evasion;
- traps;
- combat;
- spell behavior;
- treasure generation;
- experience awards;
- resource consumption;
- encumbrance;
- retainers and hirelings.

A random encounter is not automatically a combat encounter. Reaction, surprise, morale, negotiation, retreat, and avoidance must remain meaningful systems wherever supported by the rules.

## 7. Dungeon Crawling Is the Core Game Loop

The primary loop is:

> Prepare → Enter Dungeon → Explore → Encounter → Decide → Risk → Recover Treasure → Escape → Advance → Prepare Again

The game should generate or provide dungeons with enough identity and internal coherence to feel like places rather than collections of disconnected rooms.

No overarching plot is required. Emergent campaign history is preferred to mandatory scripted narrative.

## 8. Difficulty and Survivability

The simulator must provide a historically faithful baseline mode.

Optional survivability settings may make the game less lethal, but they must remain explicitly separate from the canonical historical procedures.

Survivability options may modify areas such as:

- encounter quantity;
- trap lethality;
- trap telegraphing;
- retreat survivability;
- other explicitly approved danger-reduction mechanisms.

Survivability settings must not modify treasure generation or experience awards unless the project owner explicitly changes this policy.

This prohibition includes indirect mechanisms, not only direct ones. Survivability accommodations must not be implemented by, for example, rerolling, suppressing, or substituting canonical encounters specifically because doing so would change treasure or experience availability. Survivability policy may change danger and survival odds; it must not change what a surviving party could have recovered under the canonical, unmodified procedure.

The governing principle is:

> Difficulty options modify survivability, not rewards.

If easier survival changes the rate at which a surviving party advances, that is an emergent consequence and should not be automatically compensated for.

## 9. Canonical Result Before Difficulty Modification

Whenever a survivability rule modifies a historical result, the simulator should preserve the canonical result internally before applying the modification.

Conceptually:

> Historical Procedure → Canonical Result → Survivability Policy → Presented Result

This preserves auditability and allows the player or developer to determine exactly how the selected difficulty setting changed the historical outcome.

## 10. Simulation Determines Reality

Narrative presentation must not determine game state.

The rules engine determines what happens. Narrative systems describe the result.

An AI or narrative layer may provide atmosphere, dialogue, description, or flavor, but it may not alter authoritative simulation outcomes unless specifically given authority by an approved game rule.

## 11. Persistent Consequences

The game world should preserve meaningful consequences where practical.

Examples include:

- slain monsters remain slain;
- recovered treasure remains removed;
- broken or opened dungeon features remain changed;
- surviving factions may react to losses;
- abandoned equipment or bodies may remain or be moved by world simulation;
- explored areas remain known unless a rule or game condition says otherwise.

Persistence should support emergent campaign history without requiring a scripted overarching story.

## 12. Deterministic Testability

Randomness must be controllable for testing.

Core simulation procedures should accept an injectable or seedable random-number source so that rules behavior and procedural generation can be reproduced exactly during tests.

A change in implementation should not silently change unrelated random outcomes without being detectable.

## 13. Human Authority

The human project owner retains final authority over:

- historical interpretation;
- source compatibility judgments;
- Simulator Rulings;
- Human-Approved Variants (`SOURCE_HIERARCHY.md` §7);
- approving Rule Cards for implementation (see `SOURCE_HIERARCHY.md` and `AGENTS.md`);
- approving foundational process documents (`DEVELOPMENT_WORKFLOW.md`, `TESTING_STRATEGY.md`) and clearing the pre-code development gate (see `ARCHITECTURE.md`);
- approving and superseding durable architecture/process decision records (see `docs/decisions/`);
- authorizing modification of protected authority and process documents (see `AGENTS.md`);
- game design policy;
- difficulty policy;
- project scope.

Agents may identify ambiguity, propose interpretations, and recommend implementations. They may not silently establish new rules.
