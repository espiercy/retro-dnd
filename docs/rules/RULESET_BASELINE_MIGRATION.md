# Rules Baseline Migration: 1974 OD&D-Primary → Rules Cyclopedia-Primary

This is a migration/audit record, not a Rule Card and not a decision record. It summarizes what changed under `docs/decisions/DEC-0007-rules-cyclopedia-primary-rules-authority.md` and where to find the durable governing text — it does not itself govern anything; where this document and a governing document (`SOURCE_HIERARCHY.md`, `GAME_CONSTITUTION.md`, `AGENTS.md`, `ARCHITECTURE.md`, `DEVELOPMENT_WORKFLOW.md`, `DEC-0007`) appear to differ, the governing document controls.

## 1. Previous Baseline

The 1974 three-book OD&D core (*Men & Magic*, *Monsters & Treasure*, *The Underworld & Wilderness Adventures*) was the project's primary and ultimate mechanical authority. Later non-AD&D D&D-lineage sources (Holmes, B/X, BECMI, Rules Cyclopedia) were used only to complete gaps the 1974 text left ambiguous or unresolved, consulted in that chronological order, with the Rules Cyclopedia positioned as the *last* and most consolidated fallback rather than as authority in its own right (`SOURCE_HIERARCHY.md`, as it stood before this migration; `docs/decisions/DEC-0001-project-foundation-baseline.md`'s "Historical Source Policy" summary).

## 2. New Baseline

The *Dungeons & Dragons Rules Cyclopedia* is now the primary and ultimate mechanical authority. An explicit Rules Cyclopedia rule governs regardless of what an earlier edition (including 1974 OD&D) says. BECMI, B/X, Holmes, and original OD&D/its supplements are now *alternate-source completion* material, consulted when the Rules Cyclopedia is silent, ambiguous, or incomplete — not in a rigid chronological order, but starting from whatever source is most directly relevant to the exact unresolved question (`SOURCE_HIERARCHY.md` §3, as rewritten by this migration).

A conflicting alternate-source rule that is nonetheless desired requires an explicit, documented Human-Approved Variant (`SOURCE_HIERARCHY.md` §7) — a new category this migration introduces. AD&D remains excluded by default, unchanged.

## 3. Why the Migration Occurred

Rule Card research and drafting for `EXP-001`, `EXP-002`, and `EXP-004` required close, page-verified engagement with the actual 1974 text. That engagement surfaced material differences between explicit 1974 mechanics and the rules the human project owner actually wants for this simulator — e.g., universal 1d6 weapon damage regardless of weapon type, and the absence of the Thief class from the original three-book roster. The project owner had not originally chosen the 1974 rules from prior familiarity with that specific text; having now reviewed what those rules actually require, the owner determined the 1974 core is not an adequate primary baseline for the intended game, while the project's underlying dungeon-crawler product vision remains exactly as originally intended. See `DEC-0007`'s Context for the full statement.

## 3.1 Historical Clarification — Original Product Intent (added 2026-08-16)

The repository's previous governing rules baseline treated the 1974 three-book OD&D core as primary authority — this was genuinely the active governing policy, in force and applied to real research and drafting work (`EXP-001`, `EXP-002`, `EXP-004`, `CLUSTER-001`, the original V1 inventory), for the period recorded in §1 and elsewhere in this document. That fact is not erased or rewritten by this clarification.

Subsequent review of the project's original intent established that this policy represented **governance drift**, not the project's original product vision: the intended rules target had been the Rules Cyclopedia interpretation of classic D&D from the outset. `DEC-0007` should therefore be understood as **restoring** the project's originally intended source of mechanical truth, not as the project owner abandoning an originally intended OD&D simulator in favor of a newly selected edition. The 1974-primary period is accordingly understood as an intervening governance/process drift that the project has now corrected, while the underlying dungeon-crawler product vision (`GAME_CONSTITUTION.md` §1, §7) never changed at all — see §3 above, which already noted the product vision remained "exactly as originally intended" through the migration; this section clarifies that the *rules baseline itself*, not only the product vision around it, is best understood as returning to its original target rather than departing to a new one.

## 4. Decisions Superseded

| Decision | Disposition |
|---|---|
| `DEC-0006-v1-playable-content-scope.md` (V1 Playable-Content Scope: Full 1974-Core Progression, Three-Book Boundary) | **Superseded by `DEC-0007`.** Its three-book playable-content boundary is directly and specifically contradicted by the new Rules Cyclopedia-primary policy. Status changed to `Superseded by DEC-0007`; its Context/Decision/Rationale/Consequences are preserved unchanged as a historical record — not rewritten. |

## 5. Decisions Inspected, Intentionally Left Active

| Decision | Why it remains valid |
|---|---|
| `DEC-0001-project-foundation-baseline.md` | Broad foundation summary covering game identity, encounter philosophy, survivability, simulation authority, persistence, RNG, and development governance — all unaffected. Only its "Historical Source Policy" bullet subsection describes the now-superseded 1974-primary policy; `DEC-0001` itself already provides that its governing documents control where they and its summary differ, so `DEC-0001`'s `Status` is **not** changed. `DEC-0007`'s own Consequences section is the cross-reference documenting this narrower staleness. |
| `DEC-0002-rng-contract.md` | RNG contract is edition-neutral (deterministic simulation-owned stream, `RollResult`, sequence semantics, `SeededRNG`/`ScriptedRNG`, die-range validation) — no baseline dependency. Confirmed by direct source inspection during this migration (§7 below). Unaffected. |
| `DEC-0003-python-toolchain-and-ci.md` | Toolchain/CI process decision, no rules-content dependency. Unaffected. |
| `DEC-0004-full-v1-rules-corpus-before-implementation.md` | Already `Superseded by DEC-0005`; a sequencing-policy record, not tied to which source is primary. Its own historical text is untouched by this migration. |
| `DEC-0005-v1-rules-inventory-and-clustered-implementation.md` | The dependency-complete cluster workflow (inventory first → select cluster → research → approve → implement → integrate → learn → next cluster) does not encode any 1974-specific assumption — its dungeon-crawl-loop diagram and five readiness criteria are source-neutral. Retained as the active *process*; only the *content* produced under it (the inventory, `CLUSTER-001`, the three Rule Cards) requires revalidation. |

## 6. Active Governance Files Changed

| File | Nature of change |
|---|---|
| `SOURCE_HIERARCHY.md` | Substantially rewritten. New §3 source order (Rules Cyclopedia primary; BECMI/B-X/Holmes/OD&D as alternate-source completion, non-rigid order); new §6 compatibility vocabulary (Preserved / Compatible Completion / Evolved-Different / Conflicting); new §7 Human-Approved Variant process; new §10 provenance categories. §4 (AD&D exclusion), §5 (clause-by-clause method), §8 (hybrid research approach), §11 (default research outcome) retained in substance, reworded for the new authority direction. |
| `GAME_CONSTITUTION.md` | §1 (Purpose), §2 (renamed "Rules-Cyclopedia Fidelity"), §3 (Ambiguity workflow), §4 (D&D Lineage), §5 (Rules Provenance) revised to state Rules Cyclopedia primacy and the new provenance categories. §13 (Human Authority) gains "Human-Approved Variants" to its list. §6–§12 (historical procedures, encounter philosophy, survivability, simulation authority, persistence, deterministic testability) unchanged — none depended on the source baseline. |
| `AGENTS.md` | §1 (Mission) restated around the Rules Cyclopedia; new paragraph on not silently preferring earlier editions and on `REVALIDATION_REQUIRED`. §4 (AD&D exclusion) and §10 (Rules Research Workflow) updated to the new hierarchy and compatibility vocabulary. §2, §3, §5–§9, §11–§13 unchanged. |
| `ARCHITECTURE.md` | New §15.2 "Rules Baseline Migration Gate" inserted after §15.1, recording the migration, the suspended roadmap, and the implementation freeze. §15.1's cluster-workflow mechanics and §16 (Pre-Code Development Gate, already cleared and unrelated to rules-content authority) unchanged. |
| `DEVELOPMENT_WORKFLOW.md` | New §9.7 "Revalidation After a Source-Authority Change," defining `REVALIDATION_REQUIRED` and the revalidation workflow. §1–§9.6, §10–§11 unchanged. |
| `docs/rules/_template.md` | Section names changed from `1974 Source`/`1974 Explicitly Establishes`/`1974 Leaves Undefined` to `Rules Cyclopedia Source`/`Rules Cyclopedia Explicitly Establishes`/`Rules Cyclopedia Leaves Undefined / Ambiguous`; `Completion Research` renamed `Alternate-Source Completion Research`; new `Human-Approved Variant` section added; `Provenance Classification` comment updated to the new categories; `Status Lifecycle` diagram gains `REVALIDATION_REQUIRED`. |
| `docs/decisions/DEC-0006-v1-playable-content-scope.md` | `Status` and `Superseded By` fields updated only; Context/Decision/Rationale/Consequences untouched. |
| `docs/decisions/DEC-0007-rules-cyclopedia-primary-rules-authority.md` | New record. |
| `docs/decisions/INDEX.md` | New row for `DEC-0007`; `DEC-0006`'s row `Status` updated. |
| `pyproject.toml` | `description` field updated to remove the "historically faithful... 1974" framing. |

## 7. Artifacts Marked `REVALIDATION_REQUIRED`

| Artifact | Prior status | Prior approval preserved |
|---|---|---|
| `docs/rules/exploration/dungeon_wandering_monster_check.md` (`EXP-001`) | `APPROVED`, 2026-08-15 | Yes — "Approval" section and full research/specification content unchanged; migration note added at top. |
| `docs/rules/exploration/dungeon_turn_time_accounting.md` (`EXP-002`) | `APPROVED`, 2026-08-16 | Yes — unchanged; migration note added at top. |
| `docs/rules/exploration/resting_procedure.md` (`EXP-004`) | `APPROVED`, 2026-08-16 | Yes — unchanged; migration note added at top. |
| `docs/rules/clusters/CLUSTER-001-dungeon-exploration-time.md` | `APPROVED`, 2026-08-15 | Yes — boundary analysis, rationale, and research ordering (§4–§14) unchanged; §3 status text and a top-level migration note added. |
| `docs/rules/INVENTORY.md` | `APPROVED`, 2026-08-15 | Yes — full content preserved as a historical record of the 1974-primary inventory; header notes added, and the `EXP-001`/`EXP-002`/`EXP-004` row statuses updated narrowly for internal consistency with the Rule Cards above. |

No mechanical content, research conclusion, or test case in any of the five artifacts above was rewritten by this migration. Only status fields and clearly delimited migration notes were added.

**Not marked `REVALIDATION_REQUIRED` by this migration, and left untouched:** the unmerged `cluster-001-implementation-readiness` branch and its `docs/rules/clusters/CLUSTER-001-implementation-readiness.md` (recommending `READY FOR IMPLEMENTATION` for the pre-migration cluster boundary). That branch was never merged to `main` and is therefore not part of the active documentation tree this migration audited; its recommendation is superseded in effect by this migration (the cluster it assessed is now `REVALIDATION_REQUIRED`) but its file was not edited, since doing so would require checking out a separate, non-`main`-based branch outside this migration's own branch lineage. Flagged here so it is not mistaken for still-current guidance if that branch is later revisited.

## 8. Artifacts Confirmed Edition-Neutral (No Change Required)

- **RNG/dice infrastructure** (`src/rng/`, `docs/technical/RNG_CONTRACT.md`, `DEC-0002`). Directly inspected: `roll_die(sides)` and `roll(expression)`, `RollResult`, `sequence_number` semantics, `SeededRNG`, `ScriptedRNG`, and die-range validation are all edition-neutral — they roll dice and validate results; they have no knowledge of which rules edition is authoritative. No change made or required.
- **`TESTING_STRATEGY.md`.** No 1974/OD&D-specific language found; its coverage thresholds, determinism requirements, and CI-gate model apply unchanged regardless of source authority.
- **No historical-rules production code exists yet** — `Cluster 1` was never implemented (`src/rules/`, `src/survivability/`, `src/state/`, `src/events/` are all still empty per `ARCHITECTURE.md` §13's module layout). There is therefore no rules-behavior code to migrate, and no risk of tests silently encoding superseded 1974 mechanics, because no such tests exist yet.
- **Toolchain/CI model** (`docs/technical/TOOLCHAIN_AND_CI.md`, `DEC-0003`). Purely infrastructure; not source-dependent.
- **`FIRST_CLAUDE_TASK.md`.** A historical record of the project's first assignment (an architecture review), describing the game as "1974" at the time that assignment was given. Left intentionally untouched as a historical record of a completed, one-time task instruction — not standing governance.

## 9. Known Areas Requiring Substantive Rebuild

- **`docs/rules/INVENTORY.md`** requires a full Rules Cyclopedia-based revalidation/rebuild, not a search-and-replace of source names. Content families that may change materially under Rules Cyclopedia review include (non-exhaustive, per the assigning task): classes, race/class structure, ability-score effects, combat, weapon damage, monster damage, armor and attack progression, saving throws, thief mechanics, spell availability and behavior, monster rules, treasure, magic items, reaction procedures, morale, movement, encumbrance, dungeon procedures, and advancement. This migration does not perform that rebuild — see §10.
- **`docs/rules/clusters/CLUSTER-001-dungeon-exploration-time.md`**'s three-item boundary (`EXP-001` + `EXP-002` + `EXP-004`) is not assumed to survive revalidation unchanged. It was derived from the prior inventory's dependency analysis, which itself requires revalidation first.
- **`EXP-001`, `EXP-002`, `EXP-004`** each require individual revalidation against the Rules Cyclopedia. Revalidation may conclude the Rules Cyclopedia is materially identical (card reframed with updated provenance, human reapproval) or materially different (specification and tests rewritten, human approval). No card is grandfathered back to `APPROVED` merely because it appears likely to match.

## 10. Next Required Task

**Rebuild/revalidate the V1 Rules Inventory against the Rules Cyclopedia**, per `ARCHITECTURE.md` §15.2:

```text
Rules Baseline Migration (this document)
        ↓
Rules Cyclopedia V1 Rules Inventory rebuild/revalidation
        ↓
human approval of the revised inventory
        ↓
new/revalidated dependency clusters
        ↓
Rule Card research/revalidation
        ↓
human approval
        ↓
implementation readiness
        ↓
implementation
```

Do **not** revalidate `EXP-001` individually as the immediate next step — the inventory should give global visibility again first, so revised research clusters are chosen deliberately rather than by re-litigating whichever card happens to be nearest at hand.

Historical-rules implementation authorization remains **FROZEN** (`ARCHITECTURE.md` §15.2) until that sequence reaches implementation readiness again.

## 11. Status Update (2026-08-16) — Inventory Rebuild Approved

The first step of §10's sequence is complete: `docs/rules/INVENTORY.md` has been rebuilt against the Rules Cyclopedia and is now `APPROVED` (2026-08-16), accompanied by `docs/rules/RC_V1_SCOPE_AUDIT.md` (coverage traceability) and `docs/rules/INVENTORY_MIGRATION_MAP.md` (row-by-row disposition of every entry the retired inventory contained). This approval satisfies §10's first step only — it does **not** clear the migration gate in `ARCHITECTURE.md` §15.2 as a whole and does **not** reauthorize any historical-rules implementation; §10's remaining steps (cluster revalidation/selection, Rule Card revalidation, human approval, implementation readiness) are unaddressed. `EXP-001`, `EXP-002`, `EXP-004`, and `CLUSTER-001` remain `REVALIDATION_REQUIRED`, untouched by this drafting/approval pass. The most significant finding surfaced is that `EXP-004` (Resting Procedure) may be materially changed or obsolete under RC — see the migration map's "Treatment of Existing Rule Cards."
