# Retro D&D Simulator — Game Constitution

## 1. Purpose

Retro D&D Simulator is a computer game intended to simulate the procedures, uncertainty, danger, and emergent play of the original 1974 Dungeons & Dragons game as faithfully as practical.

The primary game experience is dungeon crawling. The game does not require an epic or overarching narrative. Campaign history should emerge from expeditions, exploration, encounters, treasure recovery, character advancement, death, survival, and the persistent consequences of player decisions.

## 2. Historical Fidelity

The 1974 Dungeons & Dragons rules are the canonical foundation of the simulator.

When a rule is explicitly and sufficiently defined in the 1974 rules, that rule must be preserved. It may not be replaced merely because a later rule is clearer, more balanced, more familiar, or easier to implement.

The simulator must not silently modernize Dungeons & Dragons.

## 3. Ambiguity Is a First-Class Design Concern

The 1974 rules are not complete in all areas. Ambiguity must be identified rather than hidden.

When implementation requires behavior that the 1974 rules do not fully define:

1. Determine precisely what the 1974 text establishes.
2. Determine precisely what remains undefined.
3. Consult the project's source hierarchy for the earliest compatible completion.
4. Import only behavior that is compatible with the 1974 rule already established.
5. If no compatible historical completion exists, create a documented Simulator Ruling.

No coding agent may silently resolve rules ambiguity.

## 4. D&D Lineage, Not AD&D

The project belongs to the Dungeons & Dragons lineage descending through Basic D&D and culminating in the Rules Cyclopedia.

AD&D rules are excluded by default. They may not be used as implementation authority unless a specific exception is explicitly approved by the human project owner.

If the non-AD&D D&D lineage does not provide a compatible answer, a documented Simulator Ruling is preferred to importing AD&D behavior.

## 5. Rules Provenance

Every implemented rule should be traceable to one of the following provenance categories:

- **1974 Explicit** — directly and sufficiently specified by the 1974 rules.
- **1974 Interpreted** — derived from the 1974 rules but requiring documented interpretation.
- **D&D Completion** — completed from an approved source in the non-AD&D D&D lineage.
- **Rules Cyclopedia Completion** — completed using the Rules Cyclopedia where earlier compatible coverage is unavailable or insufficient.
- **Simulator Ruling** — behavior required by the simulation but not satisfactorily resolved by approved historical sources.

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
- approving Rule Cards for implementation (see `SOURCE_HIERARCHY.md` and `AGENTS.md`);
- approving foundational process documents (`DEVELOPMENT_WORKFLOW.md`, `TESTING_STRATEGY.md`) and clearing the pre-code development gate (see `ARCHITECTURE.md`);
- approving and superseding durable architecture/process decision records (see `docs/decisions/`);
- authorizing modification of protected authority and process documents (see `AGENTS.md`);
- game design policy;
- difficulty policy;
- project scope.

Agents may identify ambiguity, propose interpretations, and recommend implementations. They may not silently establish new rules.
