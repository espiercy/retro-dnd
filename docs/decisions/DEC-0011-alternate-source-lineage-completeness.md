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

`DEC-0010` governs the **primary** source. It says nothing about how a researcher chooses **which source units of an alternate-source lineage** to open. `CLUSTER-002` Stage B demonstrated that this is a distinct and independently sufficient failure mode — **twice, at two different levels of the corpus.**

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

The remediation **dispositioned all five top-level BECMI sets** — the lineage model in force at the time — and inspected the governing source material that produced the corrected finding. It established that the lineage is **evolved and conflicting**, not unanimous: `+2` (Expert Rulebook, Companion DM's Book) revised to `+1` (Master Players' Book). Master's Elf Experience Table revises the Elf's spell progression in the same object, so the change was deliberate.

**What the remediation did not do, stated precisely.** It corrected the **top-level** omission. It **did not** document a disposition of every constituent core rulebook inside every set, because the flat set-level model then in force did not call for one. **This record does not claim otherwise, and no retroactive audit was performed to make such a claim true.** The Elf mechanic was settled by human adjudication (SR-1) and does not depend on the alternate-source research being made exhaustive after the fact.

**Note where the governing statement actually lives.** It is in the **Master Players' Book**, one of the two core rulebooks in the Master Set — not in "the Master Set" as an undifferentiated unit. That detail is what makes item 1's hierarchy necessary rather than pedantic: see "The second-level form of the same defect" below.

### The defect, precisely

```text
Object-level rigor existed INSIDE the source units that were selected.
No completeness discipline governed the SELECTION of source units
comprising the alternate-source lineage.
```

Within each opened source unit the researcher did enumerate the governing entry, open the tables, verify visually, and search for duplicate presentations — `DEC-0010` §9.1 discipline, correctly applied. The failure was one layer up, in deciding that two sets constituted the lineage.

Three compounding factors, each of which this record addresses:

1. **Selection was driven by where the answer was expected, not by what the lineage contains.** The Elf caps at level 10; level 10 falls in the Expert Set's stated 4–14 range; Master was filed as "levels 26–36" and never tested. That reasoning is unsound because **a later source unit can restate and revise an earlier class entry** — and the Master Players' Book p. 12 reprints the entire Elf entry.
2. **A negative finding scoped to what was inspected was generalized to the lineage.** "No `+1` statement located" was accurate for the material actually opened and was stated as a property of BECMI. This is `DEC-0010` §9.5 Guardrail B's prohibited move, committed one level up from where Guardrail B is written.
3. **The word "unanimous" was applied to a five-set lineage on the strength of two agreeing sets.** Compounding this, the researcher recorded a *deliberate, reasoned* decision not to consult B/X, Holmes and OD&D — producing an appearance of considered completeness while an unexamined set of the **same, higher-priority** source sat undispositioned.

**This is not a "search harder" problem, and framing it that way would reproduce it.** No additional keyword search of the Expert and Companion material could have found a statement in Master. The instrument was not underused; the corpus was misdefined. As with `DEC-0010`, the remedy is enumeration and disposition, not diligence.

### The second-level form of the same defect

Human review of this record's own first draft caught a defect **in the proposed fix**. That draft enumerated the lineage as *"BECMI = Basic, Expert, Companion, Master, Immortals — five volumes"*, which is structurally unsafe: **a BECMI set is a boxed set, and most of them contain more than one core rulebook.**

```text
Basic Set        Players Manual  ·  Dungeon Masters Rulebook
Expert Set       Expert Rulebook
Companion Set    Players Companion (Book One) · Dungeon Masters Companion (Book Two)
Master Set       Master Players' Book · Master DM's Book
Immortals Set    Players' Guide to Immortals · DM's Guide to Immortals
```

Under a set-only enumeration, a researcher could write `Master Set — INSPECTED` while having opened only the Master DM's Book — **and the governing `+1` statement is in the Master Players' Book.** The identical omission would recur one level down, with the paperwork looking complete.

**The first remediation did not fix this, and did not claim to.** It operated under exactly that set-only model: it corrected which *sets* were on the list, which is what the model asked of it. **The nested weakness survived the remediation**, and was found only by human review of this record's own first draft. Saying otherwise would erase the reason the hierarchical refinement was needed.

The exact packaging vocabulary matters far less than the governance consequence:

> **Enumerating a set is not sufficient when that set contains multiple core source units that can independently restate, qualify, revise, or contradict the mechanic.**

Item 1 is therefore **hierarchical**, and item 3 makes a parent-level disposition explicitly insufficient. BECMI's boxed-set packaging is used as an **illustration, not as a universal model** — other lineages are organized differently, and the requirement is stated in terms that do not presume boxes.

### Both defects, and who caught each

```text
FIRST-LEVEL DEFECT — which sets were selected
    Expert + Companion inspected; Master omitted
    → lineage falsely called "unanimous at +2"
    Caught by:   human independent review
    Remediation: all five top-level BECMI sets dispositioned
    → Master Players' Book +1 discovered
    → lineage corrected to EVOLVED / CONFLICTING

SECOND-LEVEL DEFECT — which core rulebooks within a set
    This record's first draft treated each set as one "volume"
    → a parent-level disposition could still conceal an
      uninspected constituent core rulebook
    Caught by:   human review of DEC-0011's own text
    Remediation: hierarchical corpus enumeration (item 1),
                 parent-level disposition declared insufficient (item 3)
    NOT remediated by the first audit — it survived it
```

**Neither was caught by the process; both were caught by a human reader.** The Stage-B adversarial self-review restarted from the objects *within the source units already chosen*, so it could not surface a unit that was never on the list — the same structural lesson `DEC-0010` §10.1.2 drew for primary sources, now shown to apply to alternate sources too, and now shown to apply at **two** levels of the corpus. That is the basis for item 9 below.

## Decision

**When gap-directed alternate-source research relies on a named multi-unit rules lineage, the researcher must enumerate that lineage's structural units, then enumerate and disposition the constituent core source units within each materially relevant structural unit, before claiming that the lineage is exhaustive, unanimous, internally consistent, or silent.**

Specifically:

**1. Enumerate the lineage hierarchically, before opening anything.** Record the corpus as a structure, not a flat list, working down until the level at which a rule can actually be stated:

```text
LINEAGE
    ↓
STRUCTURAL UNITS          stages, sets, editions, printings —
    ↓                     whatever the lineage's own organization uses
CORE SOURCE UNITS         the individual rulebooks/volumes within each
    ↓                     structural unit
GOVERNING OBJECTS         entries, tables, stat blocks, procedures
                          inside each source unit (`DEC-0010` §9.1)
```

The vocabulary is deliberately generic. **A lineage organized as boxed sets, as single volumes, as numbered printings, or as a rulebook plus errata is covered equally**, and no packaging model is privileged. What must be identified is the level at which a rule can be independently stated — that is the level requiring disposition.

*Illustration only, not a mandated shape:* for BECMI, the structural units are the five boxed sets, and the core source units are the rulebooks within them — Basic (Players Manual; Dungeon Masters Rulebook), Expert (Expert Rulebook), Companion (Players Companion; Dungeon Masters Companion), Master (Master Players' Book; Master DM's Book), Immortals (Players' Guide to Immortals; DM's Guide to Immortals).

**2. Identify every materially relevant core source unit.** Relevance is assessed against the research question, not against convenience, and the assessment is recorded.

**The corpus is the lineage's core rules, not everything ever published for the game.** Adventures/modules, accessories, magazine articles, setting supplements, and unrelated products are **not** automatically in scope. Determining what constitutes the core rules corpus for the named lineage is itself part of the researcher's recorded assessment, and reaching beyond that corpus remains gap-directed under §15.

**3. Disposition every enumerated core source unit — a parent-level disposition is insufficient.** Each receives `INSPECTED` or `EXCLUDED WITH VERIFIED REASON`. **A core source unit may not silently sit outside the inventory**, and dispositioning a structural unit does **not** disposition the source units inside it:

```text
INSUFFICIENT     Master Set — INSPECTED

SUFFICIENT       Master Set
                   ├── Master Players' Book — INSPECTED → GOVERNING
                   └── Master DM's Book     — INSPECTED / EXCLUDED WITH VERIFIED REASON
```

This is the direct analogue of `DEC-0010` item 2 and Guardrail C, and it is what prevents the founding defect recurring one level below the set enumeration.

**4. A level-range or subject-matter assumption is not sufficient to exclude anything, at either level.** A structural unit or a core source unit whose nominal level range or apparent subject does not reach the question must still be dispositioned **by inspection** where it can **restate, revise, or supersede** earlier rules. Scope-based exclusion requires verification, not inference. *(Motivating instance: the Master Set was excluded as "levels 26–36", and its Players' Book carries the governing Elf statement.)*

**5. Later duplicate presentations are governing source objects.** A later source unit that reprints or revises an earlier one's class entry, table, or procedure is a **duplicate presentation** in the sense of `DEC-0010` §9.1 class I, and must be recorded separately. No presentation is automatically authoritative over another by virtue of position.

**6. Explicit conflict-precedence statements must be located, and their scope recorded.** Where any source unit states how contradictions with other units resolve, that statement is a **mandatory source object** for lineage research. Its **scope must be stated explicitly** — see item 10.

**7. "No statement located" remains scoped to what was actually inspected.** A negative finding must name the **core source units** inspected — not merely the structural units. It may not be restated as a property of the lineage unless completeness under items 1–3 has been established.

**8. Lineage-level claims require lineage-level completeness.** The words **unanimous**, **exhaustive**, **internally consistent**, and **absent from the lineage** are lineage-level claims. Each is prohibited until every materially relevant **core source unit** — not merely every structural unit — has been dispositioned.

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

`DEC-0010`'s object-level audit operates *within* a source that has already been chosen. It presumes the source is the Rules Cyclopedia, which is a single volume. A multi-unit lineage has enumerable structure **above** the object level — and, as human review of this record's own first draft established, **more than one level of it**. That structure is exactly where both forms of this failure occur. Applying `DEC-0010`'s principle to it is a scope extension, not a new principle — which is why this record **amends** rather than supersedes.

### Why the enumeration has to be hierarchical rather than flat

A flat enumeration fixes the level at which the last omission happened and leaves the level below it unguarded. That is not a hypothetical: the governing `+1` statement is in the **Master Players' Book**, so a set-only inventory reading `Master Set — INSPECTED` would have satisfied a flat rule while still missing the statement — with the paperwork now *looking* complete, which is worse than the original defect.

The rule therefore descends to **the level at which a rule can be independently stated**, and stops there. It does not descend into every product bearing the game's name; item 2 bounds the corpus to the lineage's **core rules**.

### Why the safeguard has to be structural rather than exhortative

The researcher who declared BECMI unanimous had, in the same document, written out Guardrail B's caveat about scoped negatives and then used the word "unanimous" three sentences later. Reminding researchers to be careful does not fix a defect that survives the researcher's own care. Enumeration makes the omission visible to a reviewer, which care does not — and a **hierarchical** enumeration makes the nested omission visible too.

### Source authority is unchanged — the point that most needs protecting

**RC remains primary** (`DEC-0007`). This record does **not** imply, and must not be read to imply, that a later alternate-source unit overrides RC. Alternate-source lineage research exists only to **clarify, complete, or help interpret** a documented RC gap or conflict (`SOURCE_HIERARCHY.md` §3, `RULE_CARD_RESEARCH_PROTOCOL.md` §15).

**A conflict-precedence statement inside a lineage governs that lineage's own internal relationships.** It does not automatically govern a later consolidating product that draws on the lineage.

The Elf case is the canonical illustration and is preserved as such:

- Master p. 2 instructs that Master's rules govern contradictions **with the previous boxed sets**.
- The Rules Cyclopedia is a later consolidation, not a fifth box. It does not incorporate that instruction.
- And RC demonstrably did **not** adopt Master's Elf wholesale: **RC p. 26's Elf Experience Table matches the Expert Set's spell progression** (level 10 = `3 3 3 3 2`), not Master's (`5 4 3 2 1`).

Reading "Master is later, and Master says its rules win" as decisive for RC would have been the mirror image of the original error — a confident conclusion from a partial reading of how the sources relate. **Item 6 requires locating such statements; item 10 forbids letting them travel.**

### Cost

Alternate-source research becomes slower, and some lineage questions will end `INCONCLUSIVE` that would previously have ended with a confident answer. The Elf question did exactly that. **That is the correct outcome**: it surfaced a real historical conflict for human adjudication instead of concealing it behind a false claim of lineage unanimity.

The hierarchical requirement adds roughly a doubling of the enumeration for a boxed-set lineage — ten core rulebooks rather than five sets, for BECMI. **It does not multiply the corpus indefinitely**, because item 2 confines it to the core rules and leaves everything beyond that gap-directed.

## Consequences

- `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` gains **§15.1 (Multi-Unit Lineage Corpus Completeness)** and a cross-reference from §10.1.2. **These amendments take effect only on human approval of this record**, and are marked in the protocol as proposed and not in force, following the convention used during `DEC-0010`'s drafting.
- `DEC-0010` is **not rewritten and not superseded.** It remains `Approved` and in force. The division of responsibility is:

  ```text
  DEC-0010  primary-source evidence completeness      (objects within one source)
  DEC-0011  alternate-source corpus completeness      (which source units, at
            during Stage B                             every level of the lineage)
  ```

- `DEC-0009`'s two-stage lifecycle, hard gates, and human evidence-review gate are unchanged. `DEC-0007`'s source hierarchy is unchanged. `DEC-0008`'s V1 rules profile is unchanged.
- The `CLUSTER-002` Stage-B alternate-source research record (`docs/rules/evidence/CHAR-003-elf-hp-alternate-source-research.md`) retains its full failure and correction history as governance provenance. **It is not to be tidied away.**
- No Rule Card, production module, or test is modified by this record.
- **The Elf hit-point mechanic is not established by this record.** It was set at `+2` by a separate human ruling of 2026-08-29, recorded in `docs/rules/character_creation/hit_points_and_hit_dice.md` as a **Simulator Ruling** — a project adjudication of a genuinely unresolved historical conflict, expressly **not** a claim that RC or BECMI resolves it.

## Supersedes

None. This record **extends** `DEC-0010`'s completeness discipline to the alternate-source research layer and **amends** `DEC-0009`'s §15 process by adding a required step. Neither is superseded; neither's historical text is rewritten.

## Superseded By

None.
