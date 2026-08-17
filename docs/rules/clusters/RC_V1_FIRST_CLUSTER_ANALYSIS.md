# Rules Cyclopedia V1 — First Cluster Selection Analysis

## Status

`ANALYSIS — AWAITING HUMAN CLUSTER SELECTION`

This is not a Rule Card, not an approved cluster definition, and not a decision record. It is an analytical comparison of candidate first implementation clusters against the approved Rules Cyclopedia V1 Rules Inventory (`docs/rules/INVENTORY.md`, `APPROVED` 2026-08-16), produced to support — not make — the human cluster-selection decision required by `ARCHITECTURE.md` §15.1/§15.2 and `DEC-0005`. No cluster is created, activated, or approved by this document. The old `docs/rules/clusters/CLUSTER-001-dungeon-exploration-time.md` is treated strictly as historical/revalidation material; its three-item boundary is not assumed to survive and is independently re-derived below.

## 1. Method and Scope

This analysis is built entirely from already-approved repository documentation — `docs/rules/INVENTORY.md`'s dependency graph, `docs/rules/INVENTORY_MIGRATION_MAP.md`'s existing-card assessments, and the governing process documents. No new Rules Cyclopedia mechanical research, table transcription, ambiguity resolution, alternate-source selection, or Simulator Ruling was performed to produce it. Where a candidate's evaluation genuinely requires research not yet done, that is recorded as a weakness of the candidate, not resolved here.

Per `ARCHITECTURE.md` §15.1 / `DEC-0005` §3, a cluster is ready for implementation only when: (1) scope is clearly defined; (2) every directly required historical rule is identified; (3) every required Rule Card is approved; (4) external dependencies have a stable approved contract; (5) no unresolved rules ambiguity is left for the implementation agent. This analysis evaluates candidates *against* those criteria — it does not satisfy them. Selecting a cluster here does not make it ready; research, Rule Card (re)approval, and a later dedicated implementation-readiness pass remain required afterward.

**Prerequisite research vs. cluster membership.** These are kept explicitly distinct throughout: an item appearing early in `INVENTORY.md`'s proposed research order (e.g., `EXP-002`) does not by itself imply first-cluster membership, and a domain sharing a Rule ID prefix (e.g., every `CHAR-*` entry) does not by itself imply single-cluster membership. Each candidate below is evaluated on its own dependency-closure and cohesion merits, not on prefix or research-order position.

## 2. The Full Dependency Graph, As Currently Approved

Reconstructed directly from `INVENTORY.md`'s per-entry "Dependencies" columns (abbreviated; full detail in the inventory itself):

```text
CHAR-001 → CHAR-002 → CHAR-003 → CHAR-004 → CHAR-005 → EXP-003, EXP-010
                    ↘ CHAR-009 → CHAR-010 → EXP-005, EXP-007, ENC-002, COMBAT-002/003
                    ↘ MAGIC-001 → MAGIC-002 → MAGIC-003+/005/006
                    ↘ ADV-002
CHAR-001 → CHAR-007 → COMBAT-004 (ability-based save mapping), CHAR-012, CHAR-008-adjacent
CHAR-002 + CHAR-008 + CHAR-009 → CHAR-013 → MAGIC-006

EXP-002 (no dependencies) → EXP-001 (+ RNG), EXP-003, EXP-004, EXP-005, EXP-006, EXP-007, EXP-010
EXP-008 → MON-001, MON-002, TREAS-001   (see §4 — a circularity was found here)

ENC-001 (no dependencies)
ENC-002 → CHAR-010
ENC-003 → EXP-001/MON-001, CHAR-008
ENC-004 (Morale) → ENC-003, "combat domain"
ENC-005 → EXP-002, EXP-003
ENC-006 → ENC-003
ENC-007 → MON-001, EXP-001

MON-001 → EXP-001, EXP-008 (circular — see §4)
MON-002 → MON-001
MON-003 → MON-001, COMBAT-002
MON-004 → MON-003

COMBAT-001 (no dependencies) → COMBAT-002 → COMBAT-003 → COMBAT-008, COMBAT-009
COMBAT-004 → CHAR-003, CHAR-007          (combat's hard reach into CHAR)
COMBAT-005 (no dependencies) → COMBAT-009
COMBAT-006 → COMBAT-001
COMBAT-007 → CHAR-011, COMBAT-002, COMBAT-003   (Weapon Mastery combat effects)

TREAS-001 → EXP-008 → TREAS-002, TREAS-003 → TREAS-004
ADV-001 → TREAS-001, COMBAT-003, MON-001 → ADV-002 → ADV-003

SIM-001 (layout) — constraint-only, consumed by EXP-008, not a historical rule
SIM-002 (survivability) — cuts across everything, deliberately deferred
```

## 3. Preconditions Confirmed

1. Current branch is `main` at the start of this task, matching `origin/main` (`474887e`), working tree clean.
2. `docs/rules/INVENTORY.md` — `Status: APPROVED`, 2026-08-16.
3. `DEC-0007` and `DEC-0008` — both `Approved`.
4. Historical-rules implementation remains gated (`ARCHITECTURE.md` §15.2): step (1), inventory approval, is complete; steps (2)–(4) — cluster (re)approval, Rule Card approval/revalidation for that cluster, implementation readiness — are unaddressed and this analysis does not change that.
5. Analysis performed on a dedicated branch, `rc-v1-first-cluster-analysis`, off `main`.

## 4. A Discovered Dependency Problem (reported, not fixed)

**`MON-001` lists `EXP-008` as one of its own dependencies, while `EXP-008` also lists `MON-001` as one of its dependencies — a circular reference.** This is not new to this analysis; it was carried forward unexamined from the retired 1974-primary inventory's identical `MON-001` dependency listing (`EXP-001`, `EXP-008`), through both RC-driven inventory drafts, without being re-derived.

This task has not researched the correct dependency direction sufficiently to assert a specific fix. An earlier draft of this document did assert one (that `MON-001` should depend only on `EXP-001`, with `EXP-008` as a downstream consumer); that assertion is withdrawn here as unsupported by this task's actual scope. What can be said with confidence is only that the relationship among `EXP-001` (the wandering-encounter trigger), `EXP-008` (dungeon stocking), and `MON-001` (monster determination) is not currently coherent as approved, and must be re-derived — not assumed in either direction — before a future cluster containing `MON-001` or `EXP-008` is selected.

This is flagged here per instruction rather than corrected in `INVENTORY.md`. It does not affect the recommendation below, since the recommended cluster touches neither `MON-001` nor `EXP-008`.

## 5. Candidates Evaluated

Four candidates from `INVENTORY.md`'s own "Candidate Cluster Signals," each independently re-derived from the dependency graph in §2 rather than accepted at face value, plus consideration of whether a better cross-domain decomposition exists (§5.5).

### 5.1 Exploration/Time (re-derived, not the old `CLUSTER-001`)

**Candidate membership: `EXP-001` + `EXP-002` only.**

The old `CLUSTER-001` (`EXP-001`+`EXP-002`+`EXP-004`) is not the starting point — this membership is re-derived from the current graph. `EXP-002` has no dependencies at all. `EXP-001` depends only on `EXP-002` and the RNG abstraction (already implemented, approved, and edition-neutral — confirmed directly during this project's own prior `CLUSTER-001` implementation-readiness pass, `roll_die`/`roll` in `src/rng/rng.py`). Nothing else in the inventory is a hard dependency of either card. This two-item core is fully dependency-complete on its own.

`EXP-004` is deliberately excluded, for reasons distinct from (and stronger than) the old cluster's original rationale for including it. `EXP-004` is currently the single least stable entry touching this area: its old mandatory-rest mechanic does not survive as RC canon, its replacement (running exhaustion vs. a distinct wilderness-travel-rest procedure) is an open `SPLIT CANDIDATE`, and the wilderness-travel half may not even belong at the same *scale* as underworld turn accounting at all. The pre-migration `EXP-002` design was activity-type-agnostic, and the old `CLUSTER-001`'s own implementation-readiness analysis (§8 of that document) found a synthetic "an activity of cost *N* turns occurred" test fixture sufficient to exercise it without a real movement/search/rest procedure. That is useful historical/design evidence that a synthetic-input testing approach is *feasible* for this shape of problem — it is not current approved mechanical authority: `EXP-002` remains `REVALIDATION_REQUIRED`, and its revalidation must independently establish its own authoritative executable time-accounting/input contract, including whether a synthetic-fixture testing approach still applies, before implementation readiness. Excluding `EXP-004` removes the cluster's only source of real boundary instability; it does not depend on that revalidation outcome either way.

`EXP-003` (movement) was considered and excluded for the same reason the old `CLUSTER-001` excluded it: it requires `CHAR-005` (encumbrance/movement rate), which pulls in a `CHAR-001→002→004→005` chain unrelated to turn accounting itself. That reasoning is source-baseline-independent and applies unchanged under RC.

- **Cohesion:** Extremely tight — two cards, one shared purpose (authoritative dungeon time and the check it drives).
- **Dependency completeness:** Fully self-contained; only external dependency (RNG) is already stable.
- **Boundary stability:** Stable as a *boundary*, even though `EXP-001`'s internal mechanics need revalidation — excluding `EXP-004` removes the graph's main source of instability from this specific slice.
- **Research burden:** MEDIUM. Both cards need revalidation, not fresh research from zero. `EXP-001`'s exact change (every-other-turn cadence, delayed appearance) is already identified, not merely flagged as uncertain — this narrows, rather than opens, its revalidation scope. `EXP-002`'s turn-length convention is expected to survive; only its `EXP-001` integration contract needs direct reassessment.
- **Implementation burden:** LOW-MEDIUM. A small progressive-ledger state machine plus one die roll — and unusually for a first RC cluster, a large fraction of the *software*-architecture questions (exact-rational-arithmetic requirement, interruption/remaining-duration contract, RNG sufficiency) were already answered during this project's prior `CLUSTER-001` implementation-readiness pass. That prior analysis is not reusable verbatim (the rules changed), but the *shape* of the problem is already understood.
- **Independent testability:** Very high — a pure deterministic state machine exercisable with scripted RNG and synthetic activity inputs, no character, monster, or combat content required at all.
- **Downstream unlock value:** Very high — nearly every other domain (`EXP-003`/`005`/`006`/`007`/`010`, `ENC-003`, `ENC-005`) depends on `EXP-002`'s turn signal, and `ENC-003`/`ENC-007` depend on `EXP-001`'s trigger.
- **Incremental product value:** Moderate — produces no visible character or fight, but re-proves the full research→Rule-Card→implementation pipeline under the new authority on the smallest possible surface.
- **Premature-architecture risk:** Low — see implementation burden above; this is the candidate with the *least* unresolved software-architecture territory, not the most.

### 5.2 Character-Foundation

**Candidate membership: `CHAR-001`, `CHAR-002`, `CHAR-003`, and a *narrowed* `CHAR-007`.**

`CHAR-001` (no dependencies) → `CHAR-002` (needs `CHAR-001`) → `CHAR-003` (needs `CHAR-002`) is a clean, self-contained chain: the minimum needed to say "a character exists, with a class and hit points." This is deliberately narrower than the inventory's own illustrative list — `CHAR-004`–`CHAR-006` (equipment, encumbrance, retainers) and `CHAR-008` (alignment/languages) are excluded, and `CHAR-014` (Aging) is excluded outright.

**`CHAR-014` does not belong here.** It governs ability-score change across many game-years of play; it has no bearing on producing an initial valid character and unlocks nothing near-term. Including it would be exactly the "balloon because of a shared prefix" failure mode the assigning task warns against.

**Equipment/encumbrance/retainers are better deferred to a distinct later "expedition preparation" cluster**, not folded into character foundation — they serve the *next* loop stage ("prepare and equip"), not character existence itself, and `CHAR-005` specifically exists only to feed `EXP-003`/`EXP-010`, which are themselves excluded from Cluster 1 candidates for the reasons in §5.1.

**Alignment/languages (`CHAR-008`) is a closer call.** Its content is likely low-effort, but its *payoff* is entirely downstream (`ENC-003` reaction, `CHAR-013` Paladin/Druid prerequisites) — nothing in a narrow character-foundation cluster's own scope needs it. It can wait without harming this cluster's internal completeness; recommended exclusion for leanness, not because it's expensive.

**`CHAR-007` has a real internal cohesion problem, not just a research question.** As currently scoped, it bundles two things: general ability-score effects (self-contained, needs only `CHAR-001`) and the *specific* Chapter 19 ability-modifier-to-saving-throw mapping (which cannot be meaningfully specified without `COMBAT-004`'s five save categories existing first). A character-foundation cluster that includes all of `CHAR-007` as currently scoped either has to pull `COMBAT-004` (and transitively `COMBAT-001`–`003`) into Cluster 1, or accept that part of an "approved" card's content is actually unresolved pending a later card — neither is clean. This is flagged as a genuine `SPLIT CANDIDATE` risk for `CHAR-007`, parallel to the one already recorded for `CHAR-013`, not previously called out in the inventory. **This is reported as a candidate-evaluation finding; `INVENTORY.md` is not modified.**

- **Cohesion:** Good, if narrowed as above; `CHAR-007`'s split risk dents this somewhat.
- **Dependency completeness:** Good if `CHAR-007` is narrowed to exclude the save-mapping; poor (pulls in the entire early `COMBAT-*` chain) if not.
- **Boundary stability:** Moderate — the `CHAR-007` question above is a real, currently-undocumented instability.
- **Research burden:** LOW-MEDIUM — well-trodden character-creation content, mostly table transcription (ability generation method(s), class/race eligibility tables, HP/HD by class).
- **Implementation burden:** LOW — mostly data/value objects and table lookups; minimal procedural complexity.
- **Independent testability:** Moderate — can validate that character generation produces legal values, but there is no larger *procedure* to exercise (no time passing, no checks resolving) — this is closer to testing static data than testing behavior.
- **Downstream unlock value:** High in the long run (nearly everything eventually needs a character), but nothing else can *proceed* purely on this cluster alone — it unlocks other clusters' prerequisites, not their own execution.
- **Incremental product value:** Moderate — a real character sheet is genuine progress, but the simulator does not yet *do* anything with it.
- **Premature-architecture risk:** Low-moderate — character state schema decisions made here will ripple forward, somewhat more than the exploration candidate's narrower state footprint.

### 5.3 Combat-Foundation

**Candidate membership per the assigning task's own list: `COMBAT-001`, `002`, `003`, `004`, `005`, `006`, `008`, `009` (`COMBAT-007`/Weapon Mastery held separately for explicit tradeoff analysis).**

`COMBAT-001`→`002`→`003` is internally clean and now fully unblocked (RC's unified attack-roll system removed the old combat-system-selection fork entirely). `COMBAT-005` and `COMBAT-006` are each independently self-contained modulo `COMBAT-001`. `COMBAT-008` (Nonlethal Combat, required) needs only `002`/`003`.

**`COMBAT-004` (Saving Throws) is a hard, unavoidable reach outside the combat domain**: it depends on `CHAR-003` and `CHAR-007` directly. Because `COMBAT-009` (Mortally Wounded, required) in turn depends on `COMBAT-004`, **no combat-foundation cluster that includes the required Mortally Wounded variant can be dependency-complete without also pulling in a character-foundation slice** (at minimum `CHAR-001`, `002`, `003`, and the save-mapping portion of `CHAR-007` this analysis already flagged as its own split risk in §5.2). This is a materially different, and worse, dependency-completeness position than the exploration/time candidate's.

**The Weapon Mastery tradeoff, as the assigning task specifically requested, stated explicitly rather than silently resolved:** `CHAR-011`/`COMBAT-007` are not hard dependencies *of* `COMBAT-001`–`003`, `005`, `006`, `008`, `009` (the dependency arrow runs the other way — `COMBAT-007` depends on `COMBAT-002`/`003`, not the reverse), so a combat cluster *can* be built without them and remain internally dependency-complete. But Weapon Mastery is mandatory V1 content (`DEC-0008`), and its effects (attack/damage/AC bonuses, multiple attacks, special maneuvers) modify the exact mechanics `COMBAT-002`/`003` would establish. Implementing core attack resolution and damage now, without Weapon Mastery's extension points anticipated, creates a real risk that a later Weapon Mastery integration requires revisiting already-`APPROVED`/`IMPLEMENTED` combat mechanics — precisely the "painting into a corner" risk the assigning task names by identifier. The alternative — pulling `CHAR-011`/`COMBAT-007` into Cluster 1 now — avoids that risk but adds `CHAR-011`'s own independently-flagged **High** research burden (five mastery tiers, level-gated acquisition, multiple maneuvers) to an already large cluster. Neither option is free; both are recorded, and neither is picked here.

- **Cohesion:** Moderate — internally coherent around "combat," but the forced `CHAR-003`/`007` reach and the Weapon Mastery tension undermine standalone cohesion.
- **Dependency completeness:** Poor — the `COMBAT-004`/`CHAR` reach is real and unavoidable for any version of this cluster that includes the required `COMBAT-009`.
- **Boundary stability:** Moderate-low — the Weapon Mastery in/out question and `COMBAT-009`'s "recurring save interaction, if any" (already flagged as uncertain in the inventory) are both live boundary questions.
- **Research burden:** HIGH — nine cards if the full list is taken, two of which (`COMBAT-008`, `009`) are wholly new Chapter 19 content with no prior-draft precedent to lean on, plus `COMBAT-003`'s confirmed per-weapon damage-table transcription and `COMBAT-004`'s five-category save table.
- **Implementation burden:** HIGH — attack resolution, damage, saves, healing, sequencing, and two new variant systems form a large, interlocking state and procedure surface.
- **Independent testability:** High — combat is inherently deterministic-and-testable (dice in, resolved outcomes out); a genuine strength.
- **Downstream unlock value:** Very high — unlocks the entire "fight" half of the game, `MON-003`'s stat expression, and `ADV-001`'s combat-XP path.
- **Incremental product value:** High — arguably the single most legible system to see working end to end.
- **Premature-architecture risk:** High — the Weapon Mastery tension and the uncertain `COMBAT-009` save interaction are both genuine premature-lock-in risks, not merely research volume.

### 5.4 Encounter-Resolution

**Candidate membership: `ENC-001`–`ENC-006` (`ENC-004` Morale required, not a toggle, per `DEC-0008`).**

This candidate fails dependency-completeness more severely than any other. `ENC-002` needs `CHAR-010` (Thief skills). `ENC-003` needs both `EXP-001`/`MON-001` *and* `CHAR-008`. `ENC-004` (required) needs `ENC-003` plus an explicitly-vague "combat domain" dependency. `ENC-005` needs `EXP-002`/`EXP-003`. Only `ENC-001` and (partially) `ENC-006` are close to self-contained. Taken as a whole, this candidate simultaneously reaches into exploration, character, monster-determination, and combat domains — the assigning task's own warning ("a cluster that merely looks cohesive by domain but cannot execute without several unresolved external contracts is not dependency-complete") describes this candidate almost exactly.

- **Cohesion:** Superficially good (shared prefix, shared "an encounter is happening" theme) but not substantively — the theme's actual mechanics live everywhere else.
- **Dependency completeness:** Worst of the four candidates — simultaneous unresolved reach into `EXP`, `CHAR`, `MON`, and `COMBAT`.
- **Boundary stability:** Moderate-low — `ENC-004`'s "combat domain" dependency and `ENC-006`'s "possibly thin" classification are both unresolved.
- **Research burden:** MEDIUM in isolation per card, but the *true* burden includes resolving or stubbing every cross-domain dependency first.
- **Implementation burden:** MEDIUM for the procedures themselves, but they cannot be meaningfully exercised alone.
- **Independent testability:** Low — no meaningful end-to-end behavior is producible without exploration, character, monster, and combat all present in at least stub form.
- **Downstream unlock value:** High once buildable (real "an encounter happens and has consequences" behavior) — but that "once buildable" condition is exactly what dependency-completeness measures, and this candidate fails it.
- **Incremental product value:** Low as a first cluster — cannot demonstrate much in isolation.
- **Premature-architecture risk:** Moderate — forces early integration decisions across four domains before any of them are individually settled.

### 5.5 Considered and Rejected: A Combined Cross-Domain Candidate

A merged "character core + exploration/time" cluster (producing a character that can also experience elapsed dungeon time) was considered, since the assigning task explicitly invites cross-domain candidates. It is not recommended: `CHAR-001`–`003` and `EXP-001`–`002` have *no* dependency relationship to each other at all (a character's ability scores have no bearing on whether a dungeon turn has elapsed) — merging them would not close any dependency gap, only inflate scope and research/implementation burden for no dependency-completeness benefit. Cohesion and dependency closure, per the assigning task's own priority ordering, do not support combining domains that are already independently complete on their own.

## 6. Comparison Matrix

1–5 scales: higher is **better** for Cohesion, Dependency Completeness, Boundary Stability, Independent Testability, Downstream Unlock Value, Incremental Product Value, and Overall Suitability. Higher is **worse** for Premature-Architecture Risk. Research/Implementation Burden use LOW/MEDIUM/HIGH/VERY HIGH (higher = worse). No cell is a precise measurement — this supports the qualitative reasoning in §5, not a replacement for it.

| Dimension | Exploration/Time | Character-Foundation | Combat-Foundation | Encounter-Resolution |
|---|---|---|---|---|
| Cohesion | 5 | 4 | 3 | 3 |
| Dependency completeness | 5 | 4 | 2 | 1 |
| Boundary stability | 4 | 3 | 2 | 2 |
| Research burden | MEDIUM | LOW-MEDIUM | HIGH | MEDIUM* |
| Implementation burden | LOW-MEDIUM | LOW | HIGH | MEDIUM* |
| Independent testability | 5 | 3 | 4 | 2 |
| Downstream unlock value | 5 | 4 | 5 | 4 |
| Incremental product value | 3 | 3 | 4 | 2 |
| Premature-architecture risk | 1 (low) | 2 (low-mod) | 4 (high) | 3 (moderate) |
| **Overall suitability as first cluster** | **5** | **4** | **3** | **2** |

*Encounter-Resolution's per-card research/implementation burden looks moderate in isolation, but its true burden includes resolving cross-domain dependencies first — its low Overall Suitability score reflects this, not the burden figures alone.

## 7. Recommendation

### Recommended first cluster: **Exploration/Time**

**Proposed membership:** `EXP-001` (Dungeon Wandering-Monster Check), `EXP-002` (Dungeon Turn / Time Accounting). Two Rule Cards only.

**Purpose:** Establish authoritative dungeon-time accounting and the wandering-monster check it drives, under the Rules Cyclopedia's now-confirmed materially different mechanics — the smallest possible slice that both re-proves the RC research→Rule-Card→implementation workflow and produces a genuinely reusable foundation nearly every other domain depends on.

**Internal dependency graph:** `EXP-002` (no dependencies) → `EXP-001` (depends on `EXP-002`'s turn-elapsed signal and the RNG abstraction).

**Stable external dependency:** the RNG abstraction (`src/rng/`, `RNG_CONTRACT.md`) — already implemented, approved, edition-neutral, directly confirmed sufficient during this project's prior `CLUSTER-001` readiness pass. (A synthetic/scripted "an activity of cost *N* turns occurred" test fixture is expected to be usable for exercising this cluster without real character, map, or monster content — see §5.1 and §11 — but that is a controlled testing convention, not itself a stable external contract; `EXP-002`'s own revalidation must still establish its authoritative time-accounting/input contract.)

**Unresolved issues requiring research before implementation** (not performed here): `EXP-001`'s exact revalidated cadence/timing specification (every-other-turn, encounter appearing at the start of the next turn — the *finding* is known, the *executable specification* is not yet rewritten); `EXP-002`'s reassessed integration contract with `EXP-001` given that changed cadence; confirmation of whether `EXP-002`'s existing shared-ledger/progressive-boundary accounting model (a Simulator Ruling, not source-dependent) still applies unchanged.

**Why the boundary is coherent:** both cards share one purpose (authoritative dungeon time), have no dependency on any other domain, and — critically — excluding `EXP-004` removes the graph's only real source of instability in this area without weakening the cluster's own internal completeness: the pre-migration `EXP-002` design did not require a real rest/exhaustion procedure to be exercised meaningfully, and `EXP-004`'s exclusion does not depend on that design surviving revalidation unchanged.

**What it unlocks:** the rest of the exploration domain (`EXP-003`, `005`–`007`, `010`, all of which depend on `EXP-002`'s signal), `ENC-003`/`ENC-005`/`ENC-007` (which depend on `EXP-001`'s trigger or `EXP-002`'s time), and re-validates the entire cluster-workflow pipeline (research → Rule Card → human approval → implementation → verification) under the new source authority for the first time.

**Why it beats the alternatives:** highest score on every dependency-completeness and architecture-risk dimension (§6); the only candidate with zero unresolved external-domain reach; the lowest implementation burden of the four because much of its software-architecture territory was already explored under the old `CLUSTER-001`; and it avoids Character-Foundation's `CHAR-007` split ambiguity, Combat-Foundation's unavoidable `CHAR`-reach-plus-Weapon-Mastery tension, and Encounter-Resolution's four-domain dependency failure.

### Runner-up: **Character-Foundation** (`CHAR-001`, `CHAR-002`, `CHAR-003`, narrowed `CHAR-007`)

Loses to Exploration/Time primarily on **independent testability** and **incremental product value**: it produces valid character *data*, not exercised *behavior* — no time passes, no check resolves, nothing is rolled beyond initial generation. It also carries the newly-identified `CHAR-007` split risk (§5.2), which Exploration/Time has no equivalent of. It remains a strong second choice precisely because it has no dependency relationship to Exploration/Time at all (§5.5) — the two could proceed in either order or, per governance, sequentially as proposed in §8, without either blocking the other.

## 8. Tentative Next 3–5 Cluster Sequence (not an approval)

```text
Cluster 1 (recommended): Exploration/Time — EXP-001, EXP-002
        ↓
Cluster 2: Character-Foundation — CHAR-001, CHAR-002, CHAR-003,
           narrowed CHAR-007 (general ability effects only)
        ↓
Cluster 3: Expedition-Preparation — CHAR-004, CHAR-005, CHAR-006, CHAR-008,
           EXP-003, EXP-010 (natural pairing: EXP-003/010 need CHAR-005 anyway)
        ↓
Cluster 4: Combat-Foundation — COMBAT-001–006, 008, 009, plus CHAR-011/COMBAT-007
           (Weapon Mastery) pulled in deliberately at this stage rather than
           deferred further, and the CHAR-007 save-mapping content this
           analysis flagged as split-risk, now resolvable since COMBAT-004
           exists; also depends on Cluster 2's CHAR-003/007 being settled
        ↓
Cluster 5 (tentative — boundary NOT dependency-complete as sketched,
           requires later re-derivation): Monster & Encounter Integration —
           provisionally MON-001, MON-002, ENC-001–006, EXP-008 (dungeon
           stocking), TREAS-001. This placeholder grouping is known-incomplete:
           ENC-002 depends on CHAR-010 (Thief skills), which this sequence
           does not introduce until Cluster 6+, so ENC-002 cannot actually be
           built at Cluster 5 as listed. MON-003/MON-004 (monster combat
           stats/special abilities) are also omitted here without a stated
           reason. The real membership of this cluster — including whether
           CHAR-010 must move earlier, whether MON-003/MON-004 belong inside
           it or after it, and how the MON-001/EXP-008 circularity (§4)
           resolves — must be re-derived by dedicated future cluster
           analysis, not assumed from this placeholder list
        ↓
a first meaningful "create party → enter room → advance time →
trigger/resolve encounter" vertical slice is anticipated somewhere around
this boundary, but neither its exact cluster number nor its exact
membership is settled here
        ↓
Cluster 6+: catalog closures (MAGIC-001–006, MON-003/004 if not moved
            earlier, TREAS-002–004), CHAR-009/010/012/013 (class/racial
            abilities, Thief skills, General Skills, high-level branches),
            ADV-001–003 — large-volume content, correctly sequenced late per
            the inventory's own proposed research order, though CHAR-010's
            exact position is itself unsettled per the Cluster 5 note above
```

**Tentative estimate of when a meaningful dungeon-expedition vertical slice becomes possible: not before the Monster & Encounter Integration boundary sketched above (provisionally "Cluster 5")** — the point at which character, time, combat, monster determination, and encounter resolution would all need to coexist in at least minimal form. This is a soft planning signal only, not a settled milestone: the boundary itself is not yet dependency-complete (see the Cluster 5 note above), so its exact position and cluster number may shift once later monster/encounter cluster analysis re-derives it. Building that slice is not proposed as a near-term task.

## 9. Treatment of Existing `EXP` Rule Cards

- **`EXP-001`:** **First cluster.** Requires revalidation (materially changed cadence and timing, per `INVENTORY.md` Major Research-Risk Flags item 1). Lifecycle status not altered by this analysis — remains `REVALIDATION_REQUIRED`.
- **`EXP-002`:** **First cluster.** Requires revalidation, though narrower in scope than `EXP-001`'s (the turn-length convention itself is expected to survive; only the `EXP-001` integration contract needs direct reassessment). Status unaltered — remains `REVALIDATION_REQUIRED`.
- **`EXP-004`:** **No longer appropriate as originally grouped.** Excluded from the recommended first cluster. Its own scope must be resolved by dedicated future revalidation before it can be assigned to *any* cluster — it may split into a short-term dungeon/exertion responsibility (candidate for a later exploration-adjacent cluster) and a distinct wilderness-travel-rest responsibility (candidate for a future wilderness cluster, if one is ever built, since Wilderness Adventures reachability remains an open question in `INVENTORY.md`). Status unaltered — remains `REVALIDATION_REQUIRED`.

## 10. Whether Old `CLUSTER-001` Survives Conceptually

**Partially.** Two of its three original members (`EXP-001`, `EXP-002`) reappear as this analysis's own independently-derived recommendation, for substantially the same underlying reason (a minimal, dependency-complete turn-accounting core). The third (`EXP-004`) does not survive in that grouping — its exclusion here is better-justified than the old cluster's inclusion of it ever was, given `EXP-004`'s now-confirmed instability. The old cluster document itself is untouched by this analysis; its `REVALIDATION_REQUIRED` status is not changed.

## 11. Rule Cards Implied by the Recommendation

For the recommended cluster only, classified per the assigning task's categories — not drafted or researched here:

| Item | Classification |
|---|---|
| `EXP-001` | REVALIDATE EXISTING RULE CARD |
| `EXP-002` | REVALIDATE EXISTING RULE CARD |
| RNG abstraction | EXTERNAL STABLE CONTRACT (already implemented/approved) |
| Synthetic "activity occurred / costs *N* turns" test input | Not classified as an EXTERNAL STABLE CONTRACT and not a Rule Card — it is a controlled test fixture/testing convention for exercising time accounting without implementing movement/search/etc. Its continued suitability is not settled; `EXP-002`'s revalidation must establish the cluster's actual authoritative executable time-accounting/input contract. |

No new Rule Card and no split decision is implied by the recommended cluster itself. (Split decisions — `CHAR-007`, `CHAR-013`, `EXP-004` — belong to later clusters per §8 and are not triggered by selecting this one.)

## 12. `SIM-001` Relative to the Recommendation

**Not needed alongside the recommended cluster.** `EXP-001`/`EXP-002` do not touch dungeon stocking, layout, or any spatial content at all; a synthetic activity-cost test fixture is expected to be sufficient for their own meaningful testing, consistent with this project's prior `CLUSTER-001` implementation-readiness analysis — though, as with the rest of `EXP-002`'s testing approach (§5.1, §11), this remains subject to confirmation during `EXP-002`'s own revalidation rather than settled fact. `SIM-001` becomes relevant no earlier than the tentative Monster & Encounter Integration boundary (§8), once `EXP-008` (stocking) enters scope — and that boundary's exact composition is itself unsettled, per §8.

## 13. Human Decisions Required Before Cluster 1 Can Be Selected

Kept deliberately minimal, per instruction not to elevate ordinary future research questions into blocking decisions, and not to reopen any `DEC-0008` selection:

1. **Approve (or redirect) the cluster recommendation itself** — this is the entire purpose of this analysis; no other decision is required to *select* a first cluster.

Nothing else was identified as blocking. The `CHAR-007` split question (§5.2), `EXP-004`'s exact future scope (§9), and the sequencing in §8 are all research-time or later-cluster-selection-time questions, not prerequisites to choosing Cluster 1.

## 14. Confirmations

- No Rules Cyclopedia mechanical research, table transcription, ambiguity resolution, alternate-source selection, or Simulator Ruling was performed.
- No Rule Card was revalidated; `EXP-001`, `EXP-002`, `EXP-004` remain exactly as they were, `REVALIDATION_REQUIRED`.
- No cluster was approved or activated; `CLUSTER-001`'s status is unchanged; no new cluster document exists other than this analysis.
- No decision record was created.
- No file under `src/` or `tests/` was created, modified, or deleted.
- `docs/rules/INVENTORY.md` was not modified — the dependency issue in §4 is reported, not corrected.

## 15. Recommendation

**`READY FOR HUMAN CLUSTER SELECTION`.**

The dependency graph is well-enough understood from already-approved documentation to support a confident first-cluster recommendation without further analysis. The one open item worth human awareness before final sign-off is the circular `MON-001`/`EXP-008` dependency (§4) — it does not affect the recommended cluster and is not itself a blocker to selecting Exploration/Time as Cluster 1, but the actual relationship among `EXP-001`, `EXP-008`, and `MON-001` should be re-derived (this analysis does not know the correct direction) and `INVENTORY.md` corrected accordingly before any cluster reaching `MON-001` or `EXP-008` is later selected. Relatedly, §8's tentative Cluster 5 (Monster & Encounter Integration) sketch is known-incomplete — see §8's own note — and should not be read as a settled boundary either.
