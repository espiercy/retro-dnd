# Cluster 2: Character Foundation

## 1. Cluster ID

`CLUSTER-002`

## 2. Name

Character Foundation

## 3. Status

**Cluster direction: `APPROVED`** — human-approved 2026-08-23.
**Cluster boundary: `APPROVED`** — human-approved 2026-08-23.

**This document approves a cluster *boundary* only.** It does not approve any
Rule Card, does not resolve any mechanic, and does not authorize
implementation. Every constituent entry is still `Unresearched`; no `CHAR-*`
Rule Card file exists anywhere in the repository as of this approval.

Do not conflate these distinct gates (`ARCHITECTURE.md` §15.1/§15.2,
`DEC-0005` §3, `SOURCE_HIERARCHY.md` §9):

| Gate | State |
|---|---|
| Cluster selection | **Complete** — `CLUSTER-002` selected as the work following `CLUSTER-001` |
| Cluster boundary approval | **Complete** — this document, 2026-08-23 |
| Stage-A evidence research (Evidence-First, `DEC-0009`) | **Complete** — four packets in `docs/rules/evidence/CHAR-00{1,2,3,7}-evidence.md` |
| Stage-A primary-source completeness (`DEC-0010`) | **`INDEPENDENT REVIEW — PASS`** — human, 2026-08-29; all four cards `source coverage PASS` |
| **Human Evidence Review (`DEC-0009` §11)** | **`CLEARED`** — human, 2026-08-29 (see the clearance history below) |
| Stage B — mechanical synthesis / Rule Card drafting | **Complete — 2026-08-29.** Four Rule Cards in `docs/rules/character_creation/`; synthesis, legacy comparison, dependency findings and P1–P5 dispositions in `CLUSTER-002-stage-b-synthesis.md`. En route, a **Stage-B alternate-source research failure** was found by independent review — the BECMI lineage was declared "unanimous at +2" after inspecting two of five volumes, and the **Master Set** in fact states `+1`. Corrected record with full failure history: `docs/rules/evidence/CHAR-003-elf-hp-alternate-source-research.md`. **RC Stage-A completeness was unaffected and was not reopened** |
| **Human rulings (2026-08-29)** | **SR-1** Elf fixed HP at 10th = **+2**; **SR-2** a Mystic **may** raise Dexterity through the 2-for-1 trade; **SR-3** the Ch. 13 score switch is **included in V1**, runs **before** eligibility and may establish a class minimum, while the trade runs after and never can; **SR-4** discard offered when no score is above 9 **or** two are below 6, player may keep anyway; **SR-5** the post-selection 2-for-1 trade **may not reduce any ability below a creation minimum of the selected class** — eligibility is established before the trade and must remain true after it (closes the Mystic Wisdom 13 edge case). **All five are `Simulator Ruling` provenance — project adjudications, not RC findings** |
| **Human Rule Card Review** | **PASSED — 2026-09-04.** All four contracts reviewed in full, exact text, and corrected across four review rounds before approval |
| Rule Card approval (`CHAR-001`, `CHAR-002`, `CHAR-003`, `CHAR-007`) | **GRANTED — 2026-09-04. All four `APPROVED`** by the human project owner. `CHAR-003`'s approval ratified **SR-1**; `CHAR-001`'s ratified **SR-2, SR-3, SR-4 and SR-5**. `CHAR-002` and `CHAR-007` own **no** Simulator Ruling |
| Alternate-source governance | **`DEC-0011` `Approved` 2026-09-04**; `RULE_CARD_RESEARCH_PROTOCOL.md` §15.1 **IN FORCE** |
| **Pre-Code contract blocker — ability-score ceiling** | **RESOLVED — 2026-09-05.** The approved `CHAR-001` §4 trade admitted a target score of **19**, which approved `CHAR-007` `A15` rejects as outside its declared 2–18 domain. Closed by a human-approved synthesis correction adding **`R11` (prime-requisite ceiling)** and cases **`C1`–`C5`** to `CHAR-001`. **`Necessary Mechanical Consequence`, not a Simulator Ruling** — SR-2…SR-5 unchanged, no SR-6, R10 untouched. Root cause was **Stage-B synthesis/composition**, *not* source completeness; `DEC-0010` and `DEC-0011` were **not** reopened |
| **Approved deterministic contract cases** | **189** — `CHAR-001` **69** (was 64; +C1–C5), `CHAR-002` **30**, `CHAR-003` **42**, `CHAR-007` **48**. Placing a case in a future integration test module is **placement, not an additional contract case** |
| **Implementation-plan artifact (`ARCHITECTURE.md` §15.2 step 4)** | **OUTSTANDING.** `docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md` does not exist and must be drafted and **human-approved** before step 4 may pass, following `CLUSTER-001` precedent. **Step 4 is NOT marked passed** |
| Implementation-readiness approval | **Not granted** |
| **Implementation authorization** | **NOT GRANTED — `CLUSTER-002` implementation is NOT AUTHORIZED.** Rule Card approval is **not** implicit implementation permission; the next phase requires separate explicit human authorization (`ARCHITECTURE.md` §15.2, §16) |

### Requirements carried into `CLUSTER-002_IMPLEMENTATION_PLAN.md` (recorded 2026-09-05)

**These are planning requirements, not authorization.** They are recorded here because the ceiling blocker demonstrated that per-card review does not catch defects that live *between* cards.

**1. Rule-Card composition check — mandatory for every dependency between approved cards.** For each dependency the plan must explicitly:

```text
1. enumerate the upstream card's produced value/result domain;
2. compare it with the downstream card's accepted input domain;
3. identify shared invariants and boundary conditions;
4. reconcile contradictory or unreachable deterministic cases.
```

At minimum the plan must perform this check for:

| Dependency | What must be reconciled |
|---|---|
| **`CHAR-001` output domain vs `CHAR-007` accepted score domain** | The exact defect this requirement exists for. `CHAR-001` produces 3–18 (R11); `CHAR-007` accepts 2–18 and rejects 1/19 (`A15`) |
| **`CHAR-001` / `CHAR-002` class-minimum interaction** | R10 (SR-5) consumes `CHAR-002`'s raw-score minimums; eligibility is established before the trade and must hold after it |
| **`CHAR-003` Constitution-adjustment dependency on `CHAR-007`** | `CHAR-003` must obtain the Constitution adjustment from `CHAR-007`, never recompute it (`H36`) |

**2. Test-module placement — exactly one canonical owner per approved case.** All **189** approved cases must map 1:1. Cases whose *enforcement* crosses card boundaries — for example `E23`, `E29`, `E30`, `H36` (`CHAR-003`), `S1`, `W7`, `O1`–`O4`, `A15` — may be **placed** in an integration module; **placement never increases the contract-case count.** Any additional integration tests written purely for branch coverage are implementation tests and are counted separately.

**3. `CHAR-001` H1–H6 need their own module.** `CHAR-001` uses `H1`–`H6` for Chapter 10 above-1st-level generation while `CHAR-003` uses `H1`–`H42` for hit points — a live prefix collision. The plan should give the Chapter 10 cases a separate future module, e.g. `test_high_level_ability_score_generation.py`, so the two `H` runs are never confused.

### Human Evidence Review clearance history (2026-08-23 → 2026-08-29)

Recorded in order, and deliberately **not** rewritten as though the suspension never occurred — the sequence is the evidence that `DEC-0010`'s gates did their job:

| # | Event | Date |
|---|---|---|
| 1 | Stage-A evidence packets produced for all four cards; **initial human evidence clearance granted** | 2026-08-23 |
| 2 | **Primary-source completeness defect discovered** — RC p. 26 Elf Experience Table never inspected; a failed keyword search had been recorded as a finding of absence | 2026-08-23 |
| 3 | **Clearance suspended**; Stage B paused; `DEC-0010` opened | 2026-08-23 |
| 4 | Remediation — object/table audit, visual verification of 23 RC pages, complete Druid and Mystic entry inspection, all 18 open questions reconciled and dispositioned; a second defect (self-certification over an open question) found and corrected | 2026-08-23 |
| 5 | **Independent completeness review — `PASS`**, performed by the human project owner, not by the researcher that gathered the evidence (`DEC-0010` item 14 / protocol §10.1.2) | 2026-08-29 |
| 6 | **Human Evidence Review clearance restored** for `CHAR-001`, `CHAR-002`, `CHAR-003`, `CHAR-007` — all `ACCEPTED`; Stage B unpaused | 2026-08-29 |

**A cleared evidence gate is not a claim that RC is unambiguous.** Genuine, fully mapped primary-source conflicts remain open and are Stage-B problems, not evidence gaps (`RULE_CARD_RESEARCH_PROTOCOL.md` §10.2.2) — chiefly the **Elf 10th-level fixed hit-point gain, `+1` versus `+2`**, whose four contradictory RC statements are all visually verified as printed.

**Current authority:** Rules Cyclopedia
(`docs/decisions/DEC-0007-rules-cyclopedia-primary-rules-authority.md`), as
scoped for V1 by
`docs/decisions/DEC-0008-rules-cyclopedia-v1-rules-profile.md`.

## 4. Approved Boundary

Three existing inventory entries, plus one narrowed responsibility:

| Entry | Responsibility as scoped for this cluster |
|---|---|
| `CHAR-001` | Ability Score Generation |
| `CHAR-002` | Race & Class Eligibility (core roster) |
| `CHAR-003` | Hit Points & Hit Dice — **HP/HD responsibility only**; saving throws are `COMBAT-004`'s and remain outside this card (`INVENTORY_MIGRATION_MAP.md`, `CHAR-003` row) |
| `CHAR-007` | **General Ability Score Mechanical Effects — narrowed responsibility** (see §5) |

### Internal dependency graph

```text
CHAR-001  (no dependencies)
    ├──→ CHAR-002 ──→ CHAR-003
    └──→ CHAR-007 (narrowed — general ability-score mechanical effects)
```

Every declared dependency of every member is satisfied by another member of
the same cluster. `CHAR-001` declares no dependencies at all
(`docs/rules/INVENTORY.md`).

## 5. The `CHAR-007` Narrowing

`CHAR-007` as previously inventoried combined two responsibilities belonging
to different dependency regions:

1. **General ability-score mechanical effects** — self-contained, depends only
   on `CHAR-001`.
2. **The Chapter 19 ability-modifier-to-saving-throw mapping** — which
   abilities modify which saving-throw categories. This cannot be meaningfully
   specified without `COMBAT-004`'s own five saving-throw categories existing
   first, and so transitively reached into `COMBAT-001`–`COMBAT-003`.

**Approved disposition (2026-08-23):**

```text
CHAR-007     owns general ability-score mechanical effects
COMBAT-004   solely owns the Chapter 19
             ability-modifier-to-saving-throw mapping
```

**No new `CHAR-*` Rule ID was created.** This follows the ownership principle
already applied in this repository when saving-throw responsibility was
removed from `CHAR-003` and consolidated under `COMBAT-004`
(`docs/rules/INVENTORY_MIGRATION_MAP.md`, `CHAR-003` row: *"better owned by
`COMBAT-004`'s full class/level table… narrows `CHAR-003` accordingly rather
than duplicating saves in two places"*). `COMBAT-004` already declared this
mapping as its own obligation, so the receiving owner was already in place;
the change resolves a duplicate-ownership conflict rather than relocating
unowned content.

**The selected V1 rule is unchanged.** Chapter 19 Ability-Based Saving Throws
remains `REQUIRED / ENABLED` per `DEC-0008`. This is an ownership decision
about which Rule Card specifies the mapping — not a change to what the
simulator plays.

**Executed before research.** Because no `CHAR-007` Rule Card exists yet, this
narrowing disturbed no approved specification, no evidence, and no lifecycle
metadata. It is ordinary rules-inventory ownership work, not a project-wide
architecture or process decision, and therefore carries no decision record
(`DEVELOPMENT_WORKFLOW.md` §9.2) — consistent with the `CHAR-003` narrowing,
which likewise received none.

## 6. Explicit Exclusions

**Excluded responsibilities and entries:**

- **The Chapter 19 ability-modifier-to-saving-throw mapping → `COMBAT-004`** (§5).
- `CHAR-004` — Starting Equipment & Expedition Preparation.
- `CHAR-005` — Encumbrance & Movement Rate.
- `CHAR-006` — Retainers & Hirelings, as currently inventoried.
- `CHAR-008` — Alignment & Languages.
- `CHAR-009` and every higher `CHAR-*` entry — class/racial special abilities,
  Thief skills, Weapon Mastery, General Skills, high-level class branches,
  aging.
- All `EXP-*`, `ENC-*`, `MON-*`, `MAGIC-*`, `TREAS-*`, `ADV-*`, `SIM-*`.
- All `COMBAT-*` — with the single exception that `COMBAT-004`'s **ownership
  metadata** is clarified by §5. `COMBAT-004`'s own content is not researched,
  scoped, or approved by this cluster, and `COMBAT-004` is **not** a member of
  it.

**Also explicitly excluded:** production orchestration; player commands;
dungeon state; movement; equipment preparation; combat; and implementation of
any kind. No `Player`, `Party`, `Character`-manager, `GameState`, or
orchestration abstraction is proposed, authorized, or implied by this cluster.

## 7. Dependency Analysis

**Dependency-complete as bounded**, on repository evidence
(`docs/rules/INVENTORY.md` dependency columns):

- `CHAR-001` — no declared dependencies.
- `CHAR-002` — depends on `CHAR-001` (in cluster).
- `CHAR-003` — depends on `CHAR-002` (in cluster).
- `CHAR-007` (narrowed) — depends on `CHAR-001` (in cluster).

**No external dependency is declared by any member.** Outbound references
(`COMBAT-003`, `COMBAT-004`, `COMBAT-005`, `ENC-003`, `CHAR-006`, `CHAR-008`,
`CHAR-012`) are downstream *consumers* of this cluster, not prerequisites of
it.

**On the open `CHAR-003`/`CHAR-002` questions (§8).** Including the narrowed
`CHAR-007` in the boundary makes the cluster dependency-complete under either
resolution of those questions: if research establishes that hit-point
determination or race/class eligibility consumes ability-score-derived values,
the owning responsibility is already inside the cluster; if it establishes
they do not, `CHAR-007`'s inclusion is independently warranted as the fourth
character-foundation responsibility. The open questions therefore gate the
*content* of the cards, as is normal before research — they do not gate this
boundary.

**No speculative dependency has been declared.** `CHAR-003`'s inventory row
continues to declare `CHAR-002` only; `CHAR-007` has deliberately **not** been
added to it. That declaration is to be revisited only if evidence-stage
research establishes the dependency (§8, question 1).

## 8. Unresolved Evidence-Stage Questions

Carried forward for the Evidence-First research workflow
(`docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md`, `DEC-0009`). **None is answered
by this boundary approval**, and none may be answered from general D&D
knowledge or from an earlier edition in preference to Rules Cyclopedia primary
text (`AGENTS.md` §1, §2, §10).

1. **`CHAR-003` ↔ general ability-score effects.** Does the Rules Cyclopedia's
   hit-point determination procedure incorporate an ability-score-derived
   modifier, and if so, is that modifier's magnitude specified by the
   hit-point procedure itself or by the general ability-score-effects
   responsibility?
2. **`CHAR-002` ↔ general ability-score effects.** Does Rules Cyclopedia
   race/class eligibility depend on ability-score minimums, prime-requisite
   thresholds, or other mechanics whose authoritative values belong to the
   general ability-score-effects responsibility?
3. **`CHAR-007` internal extent.** Confirm whether the general
   ability-score-effects table and the Chapter 13 general ability-check
   procedure form one coherent `CHAR-007` responsibility, or whether another
   responsibility boundary is needed. `docs/rules/RC_V1_SCOPE_AUDIT.md` records
   that its own Chapter 13 content-boundary verification "remains partial" and
   that a dedicated primary-text pass should confirm the complete list.
4. **RNG contract consumption (minor).** No member's inventory row declares a
   dependency on the approved RNG abstraction, though ability-score generation
   plausibly consumes it (`docs/technical/RNG_CONTRACT.md`, `src/rng/`, already
   implemented and stable). To be confirmed during research rather than assumed
   here.

Questions 1 and 2 are the ones most likely to require an `INVENTORY.md`
dependency-row correction once answered.

## 9. Relationship to `CLUSTER-001`

**`CLUSTER-001` (Dungeon Exploration Time) and `CLUSTER-002` (Character
Foundation) have no direct dependency relationship in either direction.**

Neither `EXP-001` nor `EXP-002` is a dependency of any `CLUSTER-002` member,
and no `CLUSTER-002` member is a dependency of either. This was independently
established during first-cluster analysis
(`docs/rules/clusters/RC_V1_FIRST_CLUSTER_ANALYSIS.md` §5.5: *"`CHAR-001`–`003`
and `EXP-001`–`002` have no dependency relationship to each other at all"*).

**No cross-cluster integration gate is required, and none is to be invented.**
`CLUSTER-001`'s Step-4 cross-card integration gate
(`docs/completion-records/ISSUE-006-cluster-001-cross-card-integration.md`)
existed because `EXP-002` produced values `EXP-001` consumed. No comparable
producer/consumer relationship exists here, and manufacturing one would be
premature integration, not verification.

**Why this cluster is next:** dependency readiness and progression toward the
V1 expedition loop — not reuse of `CLUSTER-001`'s implementation. `CLUSTER-002`
is the only candidate boundary that is dependency-complete against the current
approved inventory without unresolved external reach, and it supplies the first
stage of `INVENTORY.md`'s own V1 gameplay loop ("Create / maintain party").

## 10. Roadmap Position

The approved direction, unchanged by this document:

```text
CLUSTER-001 — Dungeon Exploration Time          (VERIFIED)
        ↓
CLUSTER-002 — Character Foundation              (boundary APPROVED — this document)
        ↓
later: equipment / encumbrance / movement capability
        ↓
EXP-003 — Dungeon Movement, Mapping & Special Terrain
```

**Everything after `CLUSTER-002` is provisional.** No future cluster number,
name, or boundary is formalized by this document. `EXP-003` remains a
downstream consumer — it depends on `CHAR-005`, which depends on `CHAR-004`,
which depends on this cluster's output — and is correctly outside
`CLUSTER-002`.

## 11. Expected Simulation Capability After Eventual Implementation

Once — and only once — the four constituent Rule Cards are researched,
human-approved, implemented, and verified, the simulator would be able to
deterministically generate an RC-authoritative character: ability scores, a
legal race/class, starting hit points and hit dice, and the general mechanical
effects of ability scores.

**It would still not provide:** equipment, encumbrance, movement rate,
alignment/languages, class or racial special abilities, thief skills, saving
throws, combat, spellcasting, experience or advancement, any dungeon or
exploration behavior, or any player-facing interface. It produces a character;
it does not yet do anything with one.

## 12. Implementation Authorization Status

**`NOT AUTHORIZED`.**

`ARCHITECTURE.md` §15.2's Rules Baseline Migration Gate authorization dated
2026-08-18 is scoped explicitly and solely to `CLUSTER-001`'s `EXP-001` +
`EXP-002` boundary. As that section states, every other cluster "must
independently satisfy the same four steps." `CLUSTER-002` has satisfied step
(2) — cluster boundary approval — only. Steps (3) Rule Card approval and (4)
implementation-readiness approval are unaddressed, and `ARCHITECTURE.md` §16's
project-wide Pre-Code Development Gate applies unchanged.

**The next rules step** is Stage-A Evidence-First research under
`docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` and `DEC-0009` — which requires its
own explicit human authorization and has not begun.

## 13. Provenance

Selected following the next-cluster dependency audit and the `CHAR-007`
boundary analysis performed against `docs/rules/INVENTORY.md` (`APPROVED`
2026-08-16) and `docs/rules/clusters/RC_V1_FIRST_CLUSTER_ANALYSIS.md`, which
had identified Character-Foundation as the runner-up first-cluster candidate
and first flagged `CHAR-007`'s internal cohesion problem. Both analyses are
preserved unchanged as historical record. No decision record was created —
`DEC-0005` already governs dependency-complete cluster selection and
sequencing, and the `CHAR-007` narrowing is ordinary inventory ownership work
(§5). This document is the record of the human boundary approval itself.
