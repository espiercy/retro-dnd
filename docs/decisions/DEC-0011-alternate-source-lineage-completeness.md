# DEC-0011: Alternate-Source Lineage Completeness Required for Gap Research

## Decision ID
DEC-0011

## Title
Alternate-Source Lineage Completeness Required for Gap Research

## Status
PROPOSED — AWAITING HUMAN APPROVAL

## Date
2026-08-29

> **Lifecycle note.** This record is **not approved and is not active authority.** Until a human project owner approves it, `DEC-0009` and `DEC-0010` (both `Approved`) remain the operative research process, and the `RULE_CARD_RESEARCH_PROTOCOL.md` §15.1 amendment this record proposes is drafted-but-not-in-force. The status term follows the convention established during `DEC-0010`'s drafting.
>
> **An implementation agent may not approve a project-wide process decision** (`DEVELOPMENT_WORKFLOW.md` §9, `AGENTS.md` §12). This record was drafted on explicit human direction; the direction to draft it is not an approval of it.

## Context

`DEC-0010` (`Approved` 2026-08-29) established primary-source completeness discipline: enumerate and disposition every governing **object** in the primary source before claiming coverage. It closed the defect in which the Elf Experience Table (RC p. 26) was never opened.

`DEC-0010` governs the **primary** source. It says nothing about how a researcher chooses **which volumes of an alternate-source lineage** to open. `CLUSTER-002` Stage B demonstrated that this is a distinct and independently sufficient failure mode.

### The motivating failure, stated factually

`CHAR-003` reached Stage B with a genuine, fully mapped Rules Cyclopedia self-contradiction: RC states the Elf's fixed hit-point gain at 10th level as `+1` twice (p. 25 stat block; p. 130 Step 6) and as `+2` twice (p. 25 Class Details prose; p. 129 Maximum Hit Points calculation), with one pair contradicting on a single printed page. Gap-directed alternate-source research was properly authorized to help interpret that conflict.

The research then:

```text
inspected the BECMI Expert Set        → found +2
inspected the BECMI Companion Set     → found +2
declared the BECMI lineage "unanimous at +2"
recorded "no +1 statement located; no internal BECMI conflict"
proposed +2 as the resolution, and wrote it into the Rule Card draft
```

**It did not inspect the Master Set.** Independent human review found that the **BECMI Master Players' Book p. 12** states:

> *"Hit points: 1d6 per level through 9th level, modified by Constitution if applicable. **Add 1 hp at 10th level, with no Constitution effect.**"*

— and that **Master Players' Book p. 2** carries an explicit conflict-precedence statement:

> *"If you discover a contradiction between this set and previous sets, the rules given here should be used."*

The corrected audit dispositioned all five BECMI core volumes and established that the lineage is **evolved and conflicting**, not unanimous: `+2` (Expert, Companion) revised to `+1` (Master). Master's Elf Experience Table revises the Elf's spell progression in the same object, so the change was deliberate.

### The defect, precisely

```text
Object-level rigor existed INSIDE the volumes that were selected.
No completeness discipline governed the SELECTION of volumes
comprising the alternate-source lineage.
```

Within each opened volume the researcher did enumerate the governing entry, open the tables, verify visually, and search for duplicate presentations — `DEC-0010` §9.1 discipline, correctly applied. The failure was one layer up, in deciding that two volumes constituted the lineage.

Three compounding factors, each of which this record addresses:

1. **Volume selection was driven by where the answer was expected, not by what the lineage contains.** The Elf caps at level 10; level 10 falls in the Expert Set's stated 4–14 range; Master was filed as "levels 26–36" and never tested. That reasoning is unsound because **a later volume can restate and revise an earlier class entry** — and Master p. 12 reprints the entire Elf entry.
2. **A volume-scoped negative finding was generalized to the lineage.** "No `+1` statement located" was accurate for the two volumes inspected and was stated as a property of BECMI. This is `DEC-0010` §9.5 Guardrail B's prohibited move, committed one level up from where Guardrail B is written.
3. **The word "unanimous" was applied to a five-volume lineage on the strength of two agreeing volumes.** Compounding this, the researcher recorded a *deliberate, reasoned* decision not to consult B/X, Holmes and OD&D — producing an appearance of considered completeness while an unexamined volume of the **same, higher-priority** source sat undispositioned.

**This is not a "search harder" problem, and framing it that way would reproduce it.** No additional keyword search of the Expert and Companion volumes could have found a statement in Master. The instrument was not underused; the corpus was misdefined. As with `DEC-0010`, the remedy is enumeration and disposition, not diligence.

**What caught it was a human reviewer, not the process.** The Stage-B adversarial self-review restarted from the objects *within the volumes already chosen*, so it could not surface a volume that was never on the list — the same structural lesson `DEC-0010` §10.1.2 drew for primary sources, now shown to apply to alternate sources too. That is the basis for item 9 below.

## Decision

**When gap-directed alternate-source research relies on a named multi-volume rules lineage, every materially relevant core volume must be enumerated and dispositioned before the researcher may claim that the lineage is exhaustive, unanimous, internally consistent, or silent.**

Specifically:

**1. Enumerate the lineage first.** Before opening any volume, record the lineage's constituent volumes as a list, from the lineage's own structure. For BECMI that list is **Basic, Expert, Companion, Master, Immortals** — five volumes, not "the one that covers the relevant level range."

**2. Identify every materially relevant core volume.** Relevance is assessed against the research question, not against convenience, and the assessment is recorded.

**3. Inspect or explicitly exclude each volume, with a verified reason.** Every volume in the enumeration receives a disposition — `INSPECTED` or `EXCLUDED WITH VERIFIED REASON`. **A volume may not silently sit outside the lineage inventory.** This is the direct analogue of `DEC-0010` item 2 and Guardrail C.

**4. A level-range assumption is not sufficient to exclude a later volume.** A volume whose nominal level range or subject matter appears not to reach the question must still be dispositioned by inspection where it **can restate, revise, or supersede** earlier rules. Scope-based exclusion requires verification, not inference. *(Motivating instance: the Master Set was excluded as "levels 26–36" and contains the governing Elf statement.)*

**5. Later duplicate presentations are governing source objects.** A later volume that reprints or revises an earlier volume's class entry, table, or procedure is a **duplicate presentation** in the sense of `DEC-0010` §9.1 class I, and must be recorded separately. No presentation is automatically authoritative over another by virtue of position.

**6. Explicit conflict-precedence statements must be located, and their scope recorded.** Where a lineage volume states how contradictions with other volumes resolve, that statement is a **mandatory source object** for lineage research. Its **scope must be stated explicitly** — see item 10.

**7. "No statement located" remains volume-scoped.** A negative finding must name the volumes inspected. It may not be restated as a property of the lineage unless lineage completeness under items 1–3 has been established.

**8. Lineage-level claims require lineage-level completeness.** The words **unanimous**, **exhaustive**, **internally consistent**, and **absent from the lineage** are lineage-level claims. Each is prohibited until every materially relevant core volume has been dispositioned.

**9. Independent Alternate-Source Completeness Review.** Where an alternate-source finding will **materially resolve** a documented RC ambiguity or gap:

```text
INDEPENDENT ALTERNATE-SOURCE COMPLETENESS REVIEW
REQUIRED BEFORE THE COMPLETION MAY BE ADOPTED
```

The original researcher **may** prepare the alternate-source evidence package and **may** report it as `PREPARED FOR INDEPENDENT COMPLETENESS REVIEW`. It **may not** self-certify a consequential lineage conclusion as `unanimous`, `exhaustive`, or `complete` for the purpose of resolving the RC gap.

This is the **same reviewer role** `DEC-0010` item 14 / `RULE_CARD_RESEARCH_PROTOCOL.md` §10.1.2 already defines — a reviewer context that did not conduct the evidence collection being certified. **No new or parallel reviewer role is created**, and the distinction between adversarial self-review (§10.1.1) and independent completeness review (§10.1.2) is unchanged. This record extends that existing gate to cover the alternate-source layer.

Where the finding is **not** materially consequential — it corroborates without deciding anything, or the RC gap is closed on other grounds — items 1–8 still apply, but independent review is not separately required.

**10. Alternate-source authority is unchanged, and a precedence statement does not travel.** This record grants alternate sources **no** additional authority. See Rationale.

## Rationale

### Why this is not covered by `DEC-0010`

`DEC-0010`'s object-level audit operates *within* a source that has already been chosen. It presumes the source is the Rules Cyclopedia, which is a single volume. A multi-volume lineage has an enumerable structure **above** the object level, and that structure is exactly where this failure occurred. Applying `DEC-0010`'s principle to it is a scope extension, not a new principle — which is why this record **amends** rather than supersedes.

### Why the safeguard has to be structural rather than exhortative

The researcher who declared BECMI unanimous had, in the same document, written out Guardrail B's caveat about volume-scoped negatives and then used the word "unanimous" three sentences later. Reminding researchers to be careful does not fix a defect that survives the researcher's own care. Enumeration makes the omission visible to a reviewer, which care does not.

### Source authority is unchanged — the point that most needs protecting

**RC remains primary** (`DEC-0007`). This record does **not** imply, and must not be read to imply, that a later alternate-source volume overrides RC. Alternate-source lineage research exists only to **clarify, complete, or help interpret** a documented RC gap or conflict (`SOURCE_HIERARCHY.md` §3, `RULE_CARD_RESEARCH_PROTOCOL.md` §15).

**A conflict-precedence statement inside a lineage governs that lineage's own internal relationships.** It does not automatically govern a later consolidating product that draws on the lineage.

The Elf case is the canonical illustration and is preserved as such:

- Master p. 2 instructs that Master's rules govern contradictions **with the previous boxed sets**.
- The Rules Cyclopedia is a later consolidation, not a fifth box. It does not incorporate that instruction.
- And RC demonstrably did **not** adopt Master's Elf wholesale: **RC p. 26's Elf Experience Table matches the Expert Set's spell progression** (level 10 = `3 3 3 3 2`), not Master's (`5 4 3 2 1`).

Reading "Master is later, and Master says its rules win" as decisive for RC would have been the mirror image of the original error — a confident conclusion from a partial reading of how the sources relate. **Item 6 requires locating such statements; item 10 forbids letting them travel.**

### Cost

Alternate-source research becomes slower, and some lineage questions will end `INCONCLUSIVE` that would previously have ended with a confident answer. The Elf question did exactly that. **That is the correct outcome**: it surfaced a real historical conflict for human adjudication instead of concealing it behind a false claim of lineage unanimity.

## Consequences

- `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` gains **§15.1 (Multi-Volume Lineage Completeness)** and a cross-reference from §10.1.2. **These amendments take effect only on human approval of this record**, and are marked in the protocol as proposed and not in force, following the convention used during `DEC-0010`'s drafting.
- `DEC-0010` is **not rewritten and not superseded.** It remains `Approved` and in force. The division of responsibility is:

  ```text
  DEC-0010  primary-source evidence completeness
  DEC-0011  alternate-source lineage completeness during Stage B
  ```

- `DEC-0009`'s two-stage lifecycle, hard gates, and human evidence-review gate are unchanged. `DEC-0007`'s source hierarchy is unchanged. `DEC-0008`'s V1 rules profile is unchanged.
- The `CLUSTER-002` Stage-B alternate-source research record (`docs/rules/evidence/CHAR-003-elf-hp-alternate-source-research.md`) retains its full failure and correction history as governance provenance. **It is not to be tidied away.**
- No Rule Card, production module, or test is modified by this record.
- **The Elf hit-point mechanic is not established by this record.** It was set at `+2` by a separate human ruling of 2026-08-29, recorded in `docs/rules/character_creation/hit_points_and_hit_dice.md` as a **Simulator Ruling** — a project adjudication of a genuinely unresolved historical conflict, expressly **not** a claim that RC or BECMI resolves it.

## Supersedes

None. This record **extends** `DEC-0010`'s completeness discipline to the alternate-source research layer and **amends** `DEC-0009`'s §15 process by adding a required step. Neither is superseded; neither's historical text is rewritten.

## Superseded By

None.
