# DEC-0006: V1 Playable-Content Scope — Full 1974-Core Progression, Three-Book Boundary

## Decision ID
DEC-0006

## Title
V1 Playable-Content Scope: Full 1974-Core Progression, Three-Book Boundary

## Status
Approved

## Date
2026-08-15

## Context

The V1 Rules Inventory and Dependency Map (`docs/rules/INVENTORY.md`, drafted under `DEC-0004`, retained under `DEC-0005`'s cluster workflow) was reviewed. Its overall structure was accepted, but several entries implicitly assumed a low-character-level or low-dungeon-level v1 boundary without that boundary ever having been explicitly decided — e.g., magic-item and monster catalog scope was described as "tied to a chosen dungeon-level range," and spell scope as "spell levels reachable by v1 starting characters." Nothing in `DEC-0004` or `DEC-0005` actually established such a cap; it had crept into the inventory's own risk-flag language as an assumed simplification.

Separately, the inventory did not state an explicit boundary between the 1974 three-book core and later non-AD&D supplement material *for playable content specifically* (as distinct from using later sources to complete an incomplete or ambiguous 1974 mechanic, which `SOURCE_HIERARCHY.md` already governs). It also treated procedural dungeon-layout generation as an open historical question rather than recognizing it as a category the 1974 text simply doesn't address by design (referee hand-authorship), and gave no comparable tracking to the survivability-policy specification, ability-score mechanical effects, alignment/languages, the full race/class feature package beyond eligibility, combat sequencing/timing, or magic-item *use* as distinct from generation.

## Decision

**1. No artificial level or dungeon-depth cap.** The V1 Rules Inventory covers the full playable progression reachable through normal v1 play under the 1974 three-book core — not starting characters only, not character levels 1–3, not dungeon levels 1–3, or any similar provisional boundary. If normal play can advance a character to a higher supported level, the rules and content reachable at that level remain part of the v1 inventory: higher-level class progression, higher-level spells, deeper dungeon encounter content, treasure and magic items reachable through the canonical procedures, and the monsters/special abilities reachable through those procedures. Cluster-based *implementation* (`DEC-0005`) may still proceed incrementally, and an early cluster reasonably starting with low-level content is a legitimate sequencing choice — but that is an implementation-order decision, not a catalog boundary, and must not be read back into the inventory as a scope limit.

**2. Playable-content boundary: the 1974 three-book core.** For initial v1 playable content, the boundary is *Men & Magic*, *Monsters & Treasure*, and *The Underworld & Wilderness Adventures* (1974) — classes, spells, monsters, and magic items are drawn only from those three books. Later non-AD&D D&D sources remain available through `SOURCE_HIERARCHY.md` for *compatible completion* of an incomplete or ambiguous 1974 mechanic; they do not automatically enlarge the playable-content catalog. Concretely: the Thief class (Supplement I: *Greyhawk*) is not part of v1 core, and is tracked as future supplement-expansion scope, not silently included. This is not a permanent rejection of supplement content — a later, separately authorized and separately governed decision may expand the playable catalog:

```text
1974 three-book core
        ↓
faithful v1 dungeon-crawler baseline
        ↓
later explicitly authorized D&D supplement expansions
```

**3. Missing rule families added to the inventory** (`docs/rules/INVENTORY.md`):
- Ability score mechanical effects and their cross-system dependencies (`CHAR-007`) — not just ability *generation* (`CHAR-001`).
- Alignment and languages (`CHAR-008`), including communication dependencies relevant to encounters, retainers, monsters, and spells.
- The full race/class feature package — advancement, restrictions, special abilities, saving throws, attack progression, spell progression, turning undead, racial abilities/limitations (`CHAR-009`, cross-referencing existing `ADV-002`/`COMBAT-002`/`COMBAT-004`/`MAGIC-001–004` items) — not just eligibility (`CHAR-002`).
- Combat sequence, initiative, and timing — melee, missile, spellcasting, and movement ordering (`COMBAT-006`) — given explicit visibility rather than left implicit inside attack resolution (`COMBAT-002`), and flagged historically high-risk pending research into its relationship to *Chainmail*'s turn structure.
- Magic-item *use* — activation, class/race restrictions, identification of function, curses (`TREAS-004`) — distinct from magic-item *generation* (`TREAS-003`).

**4. Procedural dungeon generation and survivability policy tracked as Simulator Specifications, not historical rules.** Neither is a question the 1974 text answers or leaves ambiguous in the way a Rule Card resolves ambiguity — dungeon-layout generation is explicitly delegated by the source to referee hand-authorship, and survivability policy is an explicitly non-historical simulator concern (`ARCHITECTURE.md` §10). Both are now tracked as `SIM-001` and `SIM-002` respectively in a dedicated inventory section, distinct from the historically-defined procedures around them (dungeon stocking, monster/treasure generation, traps), so neither is silently forgotten nor mistaken for an unresolved historical ambiguity. Neither is researched or designed by this decision.

**5. Inventory groupings are not fixed 1:1 Rule Card boundaries.** An inventory entry is a proposed, reserved identifier for tracking purposes. It may split into multiple Rule Cards once research reveals distinct historical procedures, separate dependencies, racial modifiers, independent ambiguity, or independently testable behavior (e.g., `EXP-005`, "Searching, Listening, Doors & Secret Features," is flagged as a plausible future split). The inventory defines the complete rules surface; detailed research determines final Rule Card boundaries.

**6. Supplement expansion is tracked as a future-scope placeholder, not a detailed inventory.** `docs/rules/INVENTORY.md` records that later OD&D-era supplements may eventually introduce additional classes, spells, monsters, magic items, or rules options, subject to a future, separately authorized and separately governed decision and the same source-hierarchy/Rule Card process as everything else. A supplement-content inventory is future work, not part of this decision.

## Rationale

An inventory that silently narrows its own scope — even through well-intentioned simplifying language in a risk-flag column — defeats the purpose of having an inventory at all: it would let a level cap or a content-source boundary get decided implicitly, by omission, rather than explicitly, by a human. This is the same discipline the project already applies to individual Rule Cards (`GAME_CONSTITUTION.md` §3, `AGENTS.md` §3 — no silent rules decisions), extended here to the inventory that governs which rules get written in the first place. Distinguishing "playable-content boundary" (a catalog decision) from "historical-source-hierarchy for completion" (a research-methodology decision, already governed by `SOURCE_HIERARCHY.md`) keeps those two different kinds of decisions from being conflated — a later source can still complete an ambiguous 1974 mechanic without that same source's *unrelated* content (a whole extra class, an extra spell) sneaking into the v1 catalog as a side effect. Separating "historical rule the 1974 text is silent on" from "simulator-authored design requirement the 1974 text was never going to address" (dungeon generation, survivability policy) keeps the project's rules-provenance discipline (`GAME_CONSTITUTION.md` §5) honest — a Simulator Ruling is for resolving what a historical source leaves ambiguous, not a label of convenience for something with no historical answer to find in the first place.

## Consequences

- `docs/rules/INVENTORY.md` is revised in place (not rebuilt) to remove level-cap framing, state the three-book playable-content boundary, add the five new/expanded families above, reclassify dungeon generation and survivability policy as Simulator Specifications, and add the future-supplement-expansion note.
- `DEC-0005`'s cluster-based implementation workflow is unaffected — clusters may still be selected and implemented incrementally, including reasonably starting with lower-level content, without that being read as a catalog restriction.
- Of the inventory's original six major research-risk flags, the class-roster question (flag 5) is resolved by this decision. Combat-system selection (flag 1) and the dungeon-generation approach now tracked as `SIM-001` (flag 2) remain the two largest open decisions blocking downstream research.
- Supplement-content expansion (Thief and similar) remains explicitly out of v1 core, tracked for a distinct future decision.

## Supersedes

None. This decision is complementary to `DEC-0004` and `DEC-0005` — it clarifies the inventory's *content scope*, not the sequencing *process* those decisions established.

## Superseded By

None.
