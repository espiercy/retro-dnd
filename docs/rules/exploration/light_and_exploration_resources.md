# Rule Card: Light & Exploration Resources

## Rule ID

`EXP-006`

## Title

Light & Exploration Resources

> **Scope narrowed 2026-09-29 by human governance decision**, on the authority of the accepted
> Stage-A evidence. The card owns the **mundane exploration-resource mechanics that establish and
> evolve light/resource state**. It does **not** own the mechanics that consume that state. The
> inventory title is retained; the boundary is stated in §Scope Boundaries and is narrower than
> the title alone implies.

## Status

`APPROVED`

> **Approved by the human project owner, 2026-10-01**, as remediated at `b9af227`. Stage A:
> `ACCEPTED`. The approved card carried **no Simulator Ruling** at approval; **`SR-11` was
> added 2026-10-01** by human adjudication of an ignition ambiguity the accepted evidence had
> exposed. It still carries **no `Alternate-Source Compatible Completion` and no
> `Human-Approved Variant`**.
>
> **Ratified as approved, without further change to the submitted contract:** the §1–§8 mechanical
> specification and §A–§E boundaries, and all eight bounded-remediation findings —
> `normal dungeon conditions → DIM_LIGHT` **withdrawn**; `EXP-006` owns **mundane-light
> contribution, not global/world illumination**; absence of its own light **does not establish
> complete darkness**; it **does not produce** encounter `Visibility`; it **does not establish**
> blindness; **surprise is not an input** to mundane-light-state reporting; an exhausted source
> **ceases contributing its own illumination** as a Necessary Mechanical Consequence; and
> exhaustion of one source **does not imply** party/world darkness.
>
> **Approval of this card does not authorize implementation.** `CLUSTER-004` historical-rules
> implementation is **NOT AUTHORIZED** and requires separate explicit human authorization under
> `ARCHITECTURE.md` §15.2 step 4. The `EXP-006` Pre-Code Gate assessment is recorded at
> `docs/technical/EXP-006_PRE_CODE_GATE.md`.

> **Bounded synthesis correction, 2026-10-01 — refuelling does not ignite.** Under explicit human
> adjudication during Slice-B review, §4 and case `L12` are corrected: supplying a further flask
> to an expended lantern restores `remaining_turns` to `24` and **leaves it unlit**. The earlier
> `L12` wording — *"contributes illumination again"* — asserted an ignition this card never
> establishes, and is **withdrawn**. Fuel availability and ignition state are independent;
> ignition is §5's, and is reached only by a separately authorized operation.
>
> **This is a correction of Stage-B synthesis wording to match the adjudicated fuel/ignition
> separation. It is NOT a Simulator Ruling, NOT a Human-Approved Variant, NOT alternate-source
> completion, and NOT new source research.** No Stage-A evidence is touched, and **this
> correction added no ruling of any kind**. (The card's totals later changed for an unrelated
> question: `SR-11`, 2026-10-01 — see §Simulator Ruling.)

> **Bounded Rule Card remediation applied 2026-10-01 on human adjudication.** Human review did
> **not** approve the first submission; it found three related Stage-B synthesis defects at the
> boundary between *mundane light-resource state* and *world/encounter visibility and darkness
> consequences*. All three are corrected here, and **nothing else was reopened**:
>
> - **Finding A** — the card derived `DIM_LIGHT` from the phrase *"normal dungeon conditions"*.
>   The accepted evidence classified that inference `QUALIFIED, not forced`. **Withdrawn
>   entirely**; both source facts are preserved separately as routed evidence (§Undefined 2, §7).
> - **Finding B** — the card treated absence of its **own** mundane sources as complete darkness,
>   produced a `Visibility` category, asserted a blindness predicate, and required a surprise
>   state to be queried. **All four withdrawn.** The card now outputs mundane illumination facts
>   only (§6); `ENC-001` owns classification (§7); the blindness predicate is not asserted (§8);
>   surprise is not an input (L34).
> - **Finding C** — an `EXPENDED` source contributes no illumination. **Added as a Necessary
>   Mechanical Consequence**, scoped to the source and explicitly **not** to the party or world
>   (§4, L15a, L15b).
>
> **No Simulator Ruling, no Alternate-Source Compatible Completion, no Human-Approved Variant
> arose from Findings A-C.** Those were adjudications of synthesis and provenance boundaries.
> (`SR-11` was added later, 2026-10-01, for a different and genuinely ambiguous question --
> see §Simulator Ruling.)
>
> **Stage A accepted by the human project owner, 2026-09-29.** Evidence:
> `docs/rules/evidence/EXP-006-evidence-remediated.md`, which passed independent `DEC-0010`
> completeness review at the fifth attempt. **The four prior `FAIL` reviews stand unaltered and
> are not retroactively converted**; the `PASS` certifies the remediated packet only.
>
> **This card is synthesized from the accepted remediated packet, not from the superseded
> first-pass packet** (`EXP-006-evidence.md`), whose two headline conclusions were falsified by
> the source. See §Synthesis Falsification, item 9.
>
> **This card carries exactly one Simulator Ruling, `SR-11`** (§5's precedence at
> `skill + no tinderbox + ADVERSE`), and no `Alternate-Source Compatible Completion` and no
> `Human-Approved Variant`. Every other clause is `Rules Cyclopedia Explicit`, a necessary
> consequence of one, or an RC silence refused rather than filled.
>
> **Approval of this card would not authorize implementation.** No Pre-Code Gate has been begun
> for `CLUSTER-004`, and no implementation plan exists.

## Rules Domain

`exploration`

---

## Rules Cyclopedia Source

| Page | Object | Bearing | Visually verified |
|---|---|---|---|
| **Ch. 4 p. 70** | **Torch** description | `30'` radius; burns **one hour (six turns)** | **Yes** (leaf 69) |
| **Ch. 4 p. 69** | **Lantern** description | `30'` radius; burns **one flask of oil in four hours (24 turns)**; *"Most types are shuttered or enclosed against wind"* | **Yes** (leaf 68) |
| **Ch. 4 p. 69** | **Oil** description | *"Oil is burned in a lantern for light."* | **Yes** (leaf 68) |
| **Ch. 4 p. 70** | **Tinderbox** description | `1d6`, ignite on **1 or 2**, *"under normal (comparatively dry) circumstances"*, **once per round** | **Yes** (leaf 69) |
| Ch. 4 p. 69 | **Mirror** description | *"The area must be lit for the mirror to work this way"* — a light-conditioned item mechanic | **Yes** (leaf 68) |
| Ch. 4 p. 70 | **Waterskin/wineskin** | one quart capacity | **Yes** (leaf 69) |
| Ch. 4 p. 69 | **Rations**, standard and iron | Dungeon-conditioned spoilage. **Adjacent, not owned** — §Scope Boundaries D | **Yes** (leaf 68) |
| **Ch. 5 p. 83** | **`Fire-Building`** skill | Automatic ignition with tinderbox + skill; `1d6` on 1–2 without a tinderbox; **skill check with DM penalties in adverse conditions** | **Yes** (leaf 82) |
| Ch. 5 pp. 82, 86 | Skill-check procedure; `Sample Skills Table` | `1d20` ≤ ability; natural `1` always succeeds, `20` always fails; `Fire-Building` → **Intelligence**; DM penalty scale `+1/+2`, `+3/+4`, `+5/+10/+15` | **Yes** (leaves 81, 85) |
| Ch. 5 p. 81 | `General Skills` | *"Using general skills is **optional**"* — but **`DEC-0008` selects it as project-REQUIRED** | **Yes** (leaf 80) |
| **Ch. 13 p. 150** | **`Blindness`**, `Special Character Conditions` | A character without infravision in complete darkness **is blinded**: `−4` saves, `−6` attacks, `+4` AC, ⅓ speed unguided, ⅔ guided. **Consequences routed, not owned** | **Yes** (leaf 149) |
| Ch. 14 p. 154 | `Blindness`, `Special Attacks` | *"fighting in the dark without infravision can result in blindness"* — independent corroboration | **Yes** (leaf 153) |
| **Ch. 7 p. 93** | **Encounter Distances Table** | Keyed on a **`Visibility`** column: very good light `4d6×10'`, dim light `2d6×10'`, no light `1d4×10'`; `**` = full darkness with infravision used → **dim light** | **Yes** (leaf 92) |
| **Ch. 7 p. 92** | `Encounter Distance` section | **The table is consulted only when neither party is surprised.** Otherwise a flat `1d4×10'` | **Yes** (leaf 91) |
| Ch. 7 p. 91 | Game Turn Checklist step 1 | Wandering monsters appear `2d6×10'` away *"under normal dungeon conditions"* | **Yes** (leaf 90) |
| Ch. 13 p. 149 | `Timekeeping` / **Timetrack Table** | A tally sheet. *"mark off time as it passes"*. **Creates no second time authority** | **Yes** (leaf 148) |
| Ch. 5 p. 84 | `Lip Reading` | *"the available light should be taken into account"* — a fourth light-conditioned mechanic | **Yes** (second scan, leaf 83) |

**Bounding objects located and deliberately excluded:** the `Starvation Table` (Ch. 13 p. 150,
`CHAR-005` §7 + unowned causation); `Survival`/`Hunting`/`Nature Lore` (Ch. 5 pp. 84–85,
`CHAR-012`, wilderness-gated); the three `Oil of …` relics and `Dwarven lens` (Ch. 13 p. 146,
`MAGIC-*`/`TREAS-*`); the `Attack Roll Modifiers Table` (Ch. 8 p. 108, `COMBAT-*`); every
light-, darkness- and vision-related entry in the `Index to Spells` (p. 300), **all of which are
spells**. See §Scope Boundaries.

---

## Rules Cyclopedia Explicitly Establishes

1. **A torch casts light in a `30'` radius and burns for one hour — RC states this as `six turns`.**
2. **A lantern casts light in a `30'` radius and consumes one flask of oil in four hours — RC states this as `24 turns`.**
3. **Oil is the lantern's fuel.** *"Oil is burned in a lantern for light."*
4. **A tinderbox ignites a fire on `1` or `2` of `1d6`, under normal (comparatively dry) circumstances, and may be attempted once per round.**
5. **The `Fire-Building` skill changes that procedure** (Ch. 5 p. 83): with a tinderbox **and** the skill, ignition is **automatic, no roll**, in ordinary conditions; **without** a tinderbox it is `1d6` on `1–2` each round; **in adverse conditions** (high winds, wet wood) it is a **skill check with DM-assigned penalties**.
6. **A character without infravision in an area of complete darkness is blinded** (Ch. 13 p. 150), corroborated independently at Ch. 14 p. 154.
7. **RC conditions encounter distance on a `Visibility` category** — but only when **neither party is surprised** (Ch. 7 pp. 92–93).
8. **RC states light-source durations in turns itself**, in the same 10-minute turn `EXP-002` owns. No conversion is performed by this card.
9. **RC supplies a manual timekeeping instrument** — the timetrack — and *"mark off time as it passes"*, and **no executable expiry semantics**.
10. **Torch and lantern radii are identical (`30'`).** RC nowhere distinguishes their illumination quality.

## Rules Cyclopedia Leaves Undefined / Ambiguous

These are **fully mapped source silences**, not unfinished research. Each was carried through the
accepted Stage-A packet's closure gate.

1. **What happens at the moment a light source's duration reaches zero.** RC gives durations and a
   tally instrument and stops. No expiry step, no partial-turn rule, no "gutters out" state.
2. **How a party's carried light maps to a `Visibility` category.** RC supplies **no rule at all**
   connecting carried mundane light to the p. 93 `Visibility` column. One torch and six torches
   are not distinguished, and no quantity of torches is stated to reach any named category.

   Two separate source facts exist and **must not be merged** (human adjudication 2026-10-01,
   Finding A):

   ```text
   RC p. 91  Game Turn step 1: wandering monsters appear 2d6 x 10' away
             "under normal dungeon conditions".  Stated UNCONDITIONALLY, with no
             reference to a Visibility category and no surprise condition.

   RC p. 93  The Encounter Distances Table has a Dim light row whose Dungeon value
             is also 2d6 x 10'.
   ```

   **The identical dice expression does not establish semantic identity.** The accepted Stage-A
   evidence classified that inference as **`QUALIFIED, not forced`** (`E-13a`) and withdrew the
   earlier `NECESSARY CONSEQUENCE` treatment, because p. 91 may be a standing default that
   **bypasses** the table rather than an application of its `Dim light` row — p. 92 gates the
   table on neither party being surprised, and p. 91 imposes no surprise condition.

   **This card therefore derives nothing from the phrase *"normal dungeon conditions"*.** Both
   facts are preserved above, separately, as routed evidence for `ENC-001`.
3. **Ignition in adverse conditions for a character without `Fire-Building`.** The p. 70 tinderbox
   rule is expressly qualified to *"normal (comparatively dry) circumstances"*.
4. **Deliberate extinguishing.** RC states that lanterns are *"shuttered or enclosed against
   wind"* — a property, not a procedure. **No extinguish mechanic is created here.**
5. **Whether the timetrack method is intended for light durations** specifically, or only the
   magical-effect durations RC names.
6. **Water consumption rate.** RC gives the waterskin a capacity and no rate.

---

## Alternate-Source Completion Research

**Not applicable — no `DEC-0011` question was authorized for this card, and none is needed.**
Every item in §Undefined is a mapped RC silence or a governance decision, not a gap requiring
lineage disambiguation.

> **Note on sources.** RC p. 84 is defective in the project's primary scan and was obtained from a
> second scan of the **same edition and printing**. That is a different digitisation of the same
> primary source, **not** an alternate source under `SOURCE_HIERARCHY.md`.

## Compatibility Analysis

**Not applicable.** No alternate-source candidate was considered for import.

---

## Simulator Ruling

### `SR-11` — the adverse-condition `Fire-Building` branch governs regardless of a tinderbox

**Ruling, human project owner, 2026-10-01:**

```text
If a character has Fire-Building and conditions are ADVERSE, the
adverse-condition Fire-Building procedure governs, regardless of whether
the character possesses a tinderbox.

Therefore:
    skill = True, tinderbox = False, conditions = ADVERSE
        ->  ROUTED_SKILL_CHECK

The ordinary no-tinderbox 1d6 procedure does NOT override the
adverse-condition branch.
```

**The ambiguity this resolves.** The accepted Stage-A evidence (`E-36`, p. 83) establishes two
conditionals that RC states **in parallel, with no precedence**:

```text
RC Explicit:  "If the character is trying to build a fire WITHOUT a tinderbox,
               he will eventually succeed; he must make a 1d6 roll each round,
               and on a 1 or 2 he ignites the fire."

RC Explicit:  "If the character is trying to build a fire IN ADVERSE CONDITIONS
               (during high winds or using wet wood), he must make a skill check
               with penalties assigned by the DM."
```

**Both source statements are preserved above, separately and unchanged.** The input
`(skill, no tinderbox, ADVERSE)` satisfies both antecedents, and **RC supplies nothing that
chooses between them** — not an ordering rule, not a general-versus-specific principle, not a
restatement elsewhere. The ruling resolves **only that intersection**.

**ID allocation.** `SR-11` is the next available identifier. The registry was inspected rather
than assumed: `SR-1`–`SR-10` are allocated (`CLUSTER-002` and `CLUSTER-003`), and the only two
textual occurrences of `SR-11` in the repository are `CHAR-005`'s explicit statements that
**no `SR-11` exists** — denials, not allocations.

**Scope — deliberately narrow.** `SR-11` changes **no other row** of §5's matrix. The two
RC-explicit ordinary branches, the RC-explicit adverse-with-tinderbox branch, and all three
RC-silence refusals stand exactly as they were.

---

`SR-10` (starvation movement progression) is pre-existing, belongs to `CHAR-005` §7, and is
neither reopened, extended nor renumbered here.

## Human-Approved Variant

**Not applicable.**

---

## Approved Mechanical Specification

### 1. Inputs

```text
LightSource       kind (TORCH | LANTERN), lit: bool, remaining_turns: int
OilFlask          count held                      (identity/cost/enc: CHAR-004)
Tinderbox         held: bool                      (identity/cost/enc: CHAR-004)
FireBuildingSkill has_skill: bool                 (CHAR-012 -- CONSUMED, not derived)
Conditions        ORDINARY | ADVERSE              (DM-supplied; RC gives no test)
elapsed_turns     from EXP-002                    (AUTHORITATIVE -- CONSUMED, never recomputed)
```

### 2. Illumination

```text
TORCH    radius 30 feet
LANTERN  radius 30 feet
```

A source illuminates **only while lit**. The two radii are equal, and this card **must not**
introduce a quality distinction RC does not state.

### 3. Duration

```text
TORCH     6 turns per torch
LANTERN  24 turns per flask of oil
```

Both figures are **RC's own turn-denominated statements**, in `EXP-002`'s 10-minute turn. This
card performs **no hour-to-turn conversion**.

### 4. Depletion

For each lit source, when `EXP-002` reports `n` elapsed turns:

```text
remaining_turns := remaining_turns - n        (floor 0)
```

`EXP-002` is the **sole** authority for how many turns elapsed. This card **never** counts turns,
advances a clock, or maintains a parallel turn accounting.

**At `remaining_turns == 0` the source is `EXPENDED`, and that source contributes no
illumination.** It leaves `lit_sources` and stops contributing to `max_mundane_radius_feet`.

This much is a **Necessary Mechanical Consequence** of RC's own finite, stated durations: a torch
that *"burns for one hour (six turns)"* is not burning in the seventh turn, so it is not casting
its `30'` radius then. Nothing else would be a coherent reading of a stated duration.

**It is scoped to the source, and stops there** (human adjudication 2026-10-01, Finding C):

```text
source exhausted  ->  THAT SOURCE provides no light          <- Necessary Consequence

NOT:

source exhausted  ->  the party or the world is dark         <- NOT a consequence;
                      other illumination may exist, and this
                      card does not know about it (§6)
```

RC states **no expiry semantics** (§Undefined 1), so this card still synthesizes **no burn-out
event, no partial-turn proration, no extra action or cost, no automatic party darkness, no
`NO_LIGHT`, and no blindness**.

**Refuelling restores fuel; it does not ignite** (human adjudication 2026-10-01). A lantern
reaching zero consumes its flask, and a further flask may be supplied, which **restores
`remaining_turns` to `24` and leaves the lantern unlit**:

```text
expended lantern + new flask  ->  remaining_turns = 24
                              ->  lit = False
                              ->  contributes NO illumination
```

**Fuel availability and ignition state are independent.** RC's §4 sentence establishes that a
further flask restores the lantern's *fuel duration*; it establishes **no** automatic ignition or
relighting. A refuelled lantern becomes *capable* of contributing illumination only after a
separately authorized **ignition** operation (§5) changes its `lit` state. Supplying a flask is
not that operation.

The card states this only for a lantern that has **reached zero**. What supplying a flask to a
partly-full lantern does is **not established**, and no arithmetic is assigned to it — no topping
up to `24`, no adding `24`, no partial-flask arithmetic. The operation is **refused
deterministically**, an API precondition derived from this stated scope rather than a new
mechanic.

### 5. Ignition

**All eight combinations, each appearing exactly once. No wildcard, no `any`, no overlap.**

```text
skill  tinderbox  conditions   disposition                     provenance
-----  ---------  ----------   -----------------------------   -------------------------
 yes      yes      ORDINARY    AUTOMATIC, no roll              RC Explicit
 yes      yes      ADVERSE     skill check (CHAR-012)          RC Explicit
 yes      no       ORDINARY    1d6 per round, ignite on 1-2    RC Explicit
 yes      no       ADVERSE     skill check (CHAR-012)          SR-11  <- the ruling
 no       yes      ORDINARY    1d6 per round, ignite on 1-2    RC Explicit
 no       yes      ADVERSE     REFUSE -- undefined by RC       RC silence
 no       no       ORDINARY    REFUSE -- no procedure stated   RC silence
 no       no       ADVERSE     REFUSE -- no procedure stated   RC silence
```

**The fourth row is `SR-11` and nothing else is.** RC states two parallel conditionals —
*"If the character is trying to build a fire **without** a tinderbox… `1d6`…"* and *"If the
character is trying to build a fire **in adverse conditions**… skill check…"* — and supplies **no
precedence** between them. Their intersection is a genuine RC ambiguity, resolved by ruling, not
by reading. See §Simulator Ruling.

### 5.1 One attempt per round — enforced from caller-supplied state

RC: *"Someone with a tinderbox may try to use it **once per round**."* The rule is this card's;
**knowledge of the current round is not.**

```text
attempt_already_made_this_round: bool        supplied by the caller

    False  ->  one ignition attempt may be evaluated
    True   ->  ERROR -- another attempt is not permitted this round
```

**This is the same API boundary as `elapsed_turns`** (§1, §4): `EXP-006` **enforces** a rule from
authoritative state it is **given**, and does not become the authority that **tracks** that state.
It holds no round counter, no round number, no clock and no mutable state across calls, and it
never mutates the flag. The caller or orchestrator is responsible for supplying a truthful value;
which component does so is a frontier concern, and **no orchestrator and no action-economy
framework is created by this card** (approved case `L19`).

At most **one attempt per round**. The skill-check resolution itself (`1d20` ≤ Intelligence,
natural `1` succeeds, `20` fails, DM penalty added) is **`CHAR-012`'s** and is **consumed, not
reimplemented**; this card supplies only the branch condition.

The `UNDEFINED BY RC` branch **refuses with an explanatory error**. It does not default to the
`1d6`, because RC expressly qualifies that roll to ordinary circumstances.

### 6. Output — mundane illumination facts only

This card's **entire output**. Every field is scoped to the mundane sources this card owns, and
the field names say so, so that no consumer can mistake them for a statement about the world:

```text
mundane_light_contribution = {
    lit_sources:                 [LightSource]   # kind, radius_feet, remaining_turns
    any_mundane_source_lit:      bool            # THIS CARD'S OWN SOURCES ONLY
    max_mundane_radius_feet:     int | None      # 30 while any owned source is lit, else None
}
```

**What `any_mundane_source_lit == false` means, exactly** (human adjudication 2026-10-01,
Finding B):

```text
MEANS:         EXP-006 knows of no active mundane light source that it owns.

DOES NOT MEAN: complete darkness
               NO_LIGHT
               any Visibility category
               blindness
               that the party or the location is dark
```

The card owns **only mundane exploration-light resources**. It does not own environmental or
ambient illumination, and §B explicitly excludes `MAGIC-*`. **Absence of its own sources is
therefore an absence of knowledge, not a fact about the world**, and this card never converts the
one into the other.

### 7. Encounter visibility — **routed evidence, not an executable output**

**This card produces no `Visibility` category.** It does not classify, resolve or query the
Encounter Distances Table, and **surprise is not an input to it** — a consumer may ask this card
for its mundane-light facts without supplying any encounter circumstance at all.

The following RC facts are recorded **for `ENC-001`**, which owns the classification and the
resolution:

```text
p. 93  The Encounter Distances Table is keyed on a Visibility column with three
       named categories:  VERY GOOD LIGHT  /  DIM LIGHT  /  NO LIGHT.
       Dungeon values: 4d6 x 10'  /  2d6 x 10'  /  1d4 x 10'.

p. 93  Footnote **:  full darkness with infravision used is treated as DIM LIGHT.

p. 92  The table is consulted ONLY when NEITHER party is surprised.

p. 92  When EITHER party is surprised, the encounter-distance path is a flat
       1d4 x 10', and light does not enter the calculation.
```

**None of the above is executed here.** `ENC-001` is `[UNRESEARCHED]`; whatever aggregation it
needs — mundane light, environmental illumination, magical light, infravision, encounter
circumstances — is **its** rule to write, and **this card does not invent that aggregation**.

### 8. Darkness and blindness — **not established by this card**

The RC fact and its routing are preserved; what is withdrawn is this card's claim to be able to
trigger them.

```text
RC p. 150 (corroborated p. 154):
    complete darkness + no infravision  ->  blindness consequences
        -4 saves, -6 attacks, +4 AC
        1/3 normal speed unguided, 2/3 guided
```

**`EXP-006` cannot establish `complete darkness`**, because it owns only its own mundane sources
(§6). It therefore **does not evaluate, assert or report the blindness predicate**, and supplies
no input that a consumer could mistake for it.

```text
blindness consequences -- movement       ->  CHAR-005 §7   [LANDED]
blindness consequences -- save/attack/AC ->  COMBAT-*      [UNRESEARCHED]
infravision possession                   ->  CHAR-009      [UNRESEARCHED]

the COMPLETE-DARKNESS world-state predicate itself
    ->  OWNER NOT SETTLED.  No Rule ID in INVENTORY.md establishes global or
        environmental illumination state.  This is recorded as an open
        governance issue (Open Questions 7) and NO OWNER IS INVENTED HERE.
```

A downstream owner that has established complete darkness by authoritative means may then apply
the p. 150 consequences through the routes above. **This card is one input to that determination,
never the determination itself.**

---

## Scope Boundaries

### A. What this card owns

Mundane light and exploration-resource **state and its evolution**: whether a source it owns is
lit, that source's radius, its remaining duration, whether it can be ignited, depletion against
authoritative elapsed turns, and whether an exhausted source still contributes illumination.

**The card reports facts about its own sources. It makes no claim about the world's
illumination**, and every field in §6 is named to keep that distinction visible to consumers.

### B. What this card does **not** own

```text
Encounter distance resolution AND
  Visibility classification        ENC-001   -- §7 records routed evidence only;
                                              this card produces NO category
Complete-darkness / environmental
  illumination world state         OWNER NOT SETTLED -- §8, Open Question 7
Blindness/darkness movement        CHAR-005 §7 [LANDED]
Attack / save / AC consequences    COMBAT-*
Skill resolution procedure         CHAR-012
Infravision possession             CHAR-009
Magical light and darkness         MAGIC-*   -- Index to Spells p. 300 enumerated;
                                              every light/darkness entry there is a SPELL
Item identity, cost, price form,
  encumbrance                      CHAR-004  [LANDED]  -- NOT reopened
Dungeon time                       EXP-002   [LANDED]  -- NOT duplicated
Ordinary dungeon movement          EXP-003   [LANDED]
Torch used as a weapon             COMBAT-*/CHAR-004
Oil thrown as a missile, or
  "poured out and ignited to
  delay pursuit"                   ENC-005 / COMBAT-*  -- RC states NO mechanic for
                                                         the delay; none is invented
```

### C. The `CHAR-004` seam

`CHAR-004` is authoritative for **identity, cost, price form and encumbrance**. `EXP-006` owns
**use during exploration**. **No price, encumbrance, quantity-pricing, `Coin` or catalog fact is
restated, re-derived or varied by this card.**

### D. Rations — **adjacent, evidenced, deliberately unassigned**

Stage A established real RC mechanics: one ration feeds one adult for a week (~21 meals);
**standard rations *"spoil overnight"* in a dank dungeon**; **iron rations last two months in
normal travel and up to a week in dungeons**.

```text
This is structurally the same shape as torch burn time -- a purchased consumable with a
printed duration that is SHORTER INSIDE A DUNGEON.

OWNERSHIP IS NOT ASSIGNED HERE, by express governance direction.
No ration mechanic is specified, no Rule ID is created, and this card is NOT broadened
into a general provisioning or survival-resources card.
```

### E. Starvation — **outside this card**

Movement consequence: `CHAR-005` §7 **[LANDED]**, carrying `SR-10`. **Causation has no Rule ID
anywhere in `INVENTORY.md`**, and that remains an **open governance issue**. No owner is invented
here, and no starvation mechanic appears in this card.

---

## Deterministic Test Cases

Case IDs use the `L` series (Light), distinct from `CHAR-004`'s `E`, `CHAR-005`'s `M` and
`EXP-003`'s `D`.

### Illumination

| # | Input | Expected |
|---|---|---|
| L1 | Lit torch | radius **`30`** feet |
| L2 | Lit lantern | radius **`30`** feet |
| L3 | Unlit torch | illuminates nothing |
| L4 | **Torch radius differing from lantern radius** | **MUST NOT OCCUR** — guard test |
| L5 | **Any illumination-quality distinction between torch and lantern** | **MUST NOT EXIST** — guard test |

### Duration and depletion

| # | Input | Expected |
|---|---|---|
| L6 | Fresh torch | `6` turns |
| L7 | Lantern with one flask | `24` turns |
| L8 | Lit torch, `EXP-002` reports `1` elapsed turn | `5` remaining |
| L9 | Lit torch, `6` elapsed turns | `0` remaining; **`EXPENDED`**; **that source contributes no illumination** and leaves `lit_sources` |
| L10 | Lit torch, `9` elapsed turns | `0`, **floored — not negative** |
| L11 | **Unlit** torch, `3` elapsed turns | `6` remaining — unlit sources do not deplete |
| L12 | Lantern `EXPENDED`, new flask supplied | `24` remaining; **`lit = False`** — **no illumination contribution until separately ignited** (§5). Refuelling restores fuel, not ignition |
| L12a | **Refuelling a lantern that has not reached zero** | **REFUSED** — the card states a further flask only for a lantern *reaching zero*; no top-up or additive arithmetic is assigned |
| L13 | **This card advancing or counting turns itself** | **MUST NOT OCCUR** — guard test; `EXP-002` is sole authority |
| L14 | **Any second turn counter, clock or elapsed-time field owned here** | **MUST NOT EXIST** — guard test |
| L15 | **A burn-out event, partial-turn proration, or any extra action/cost at zero** | **MUST NOT EXIST** — guard test; RC states no expiry semantics |
| L15a | Two lit torches, one reaches `0` | the expended one contributes nothing; **the other still contributes**; `any_mundane_source_lit` **remains `true`** |
| L15b | **An exhausted source producing party/world darkness, `NO_LIGHT`, or blindness** | **MUST NOT OCCUR** — guard test; Finding C is scoped to the source |
| L16 | **Hour-to-turn conversion performed by this card** | **MUST NOT OCCUR** — RC states turns itself |

### Ignition

| # | Input | Expected |
|---|---|---|
| L17 | Tinderbox, no skill, ordinary | `1d6`; ignites on **`1` or `2`** |
| L18 | Tinderbox, no skill, ordinary, roll `3` | fails; may retry next round |
| L19 | Ignition requested with `attempt_already_made_this_round = True` | **ERROR** — another attempt is not permitted this round (§5.1) |
| L19a | Ignition requested with `attempt_already_made_this_round = False` | evaluated normally; the card **does not record** that an attempt occurred |
| L19b | **This card tracking rounds, or mutating the attempt flag across calls** | **MUST NOT OCCUR** — guard test; it enforces the rule from supplied state, it is not the authority that tracks it |
| L20 | Tinderbox **and** `Fire-Building`, ordinary | **AUTOMATIC**, no roll |
| L21 | `Fire-Building`, **no** tinderbox | `1d6` per round, ignites on `1` or `2` |
| L22 | `Fire-Building`, adverse conditions | routes to a **`CHAR-012` skill check**; this card supplies no roll |
| L23 | **No skill, tinderbox, adverse conditions** | **REFUSE** — `UNDEFINED BY RC`, explanatory error |
| L24 | **No skill, no tinderbox** | **REFUSE** — no procedure stated |
| L25 | **This card resolving a skill check itself** | **MUST NOT OCCUR** — guard test; `CHAR-012` owns `1d20` ≤ ability |
| L26 | **Adverse-condition ignition defaulting to the `1d6`** | **MUST NOT OCCUR** — guard test; RC qualifies that roll to ordinary circumstances |

### Mundane light state

| # | Input | Expected |
|---|---|---|
| L27 | Any owned source lit | `any_mundane_source_lit = true`, `max_mundane_radius_feet = 30` |
| L28 | No owned source lit | `any_mundane_source_lit = false`, `max_mundane_radius_feet = None` — **and nothing further is asserted** |
| L29 | **`any_mundane_source_lit = false` producing `NO_LIGHT`, complete darkness, or any world-state claim** | **MUST NOT OCCUR** — guard test; absence of this card's sources is absence of knowledge, not a fact about the world |
| L30 | **The phrase *"normal dungeon conditions"* producing `DIM_LIGHT` or any category** | **MUST NOT OCCUR** — guard test; the accepted evidence classified this `QUALIFIED, not forced` (`E-13a`). Identical `2d6×10'` does not establish semantic identity |
| L31 | **Any `Visibility` category (`VERY_GOOD_LIGHT` / `DIM_LIGHT` / `NO_LIGHT`) produced, classified or returned by this card** | **MUST NOT OCCUR** — guard test; `ENC-001` owns classification |
| L32 | **Infravision folded into a visibility classification here** | **MUST NOT OCCUR** — guard test; the p. 93 `**` footnote is `ENC-001`-facing evidence |
| L33 | **This card rolling `4d6×10'`, `2d6×10'` or `1d4×10'`** | **MUST NOT OCCUR** — guard test; `ENC-001` owns the roll |
| L34 | Mundane light state queried **with no surprise state supplied** | **SUCCEEDS** — surprise is not an input to this card |
| L35 | **Surprise, or any encounter circumstance, required to query mundane light state** | **MUST NOT OCCUR** — guard test |
| L36 | **Any `light state → encounter distance` path resolved inside this card** | **MUST NOT EXIST** — guard test; gated or ungated alike |

### Routed consequences

| # | Input | Expected |
|---|---|---|
| L37 | `any_mundane_source_lit = false`, character without infravision | **no blindness predicate asserted, evaluated or reported.** This card supplies illumination facts only |
| L37a | **Complete darkness established by this card from its own state** | **MUST NOT OCCUR** — guard test; owner of that predicate is **not settled** |
| L38 | **Any movement multiplier applied by this card** | **MUST NOT OCCUR** — `CHAR-005` §7 |
| L39 | **Any `−4` / `−6` / `+4` applied by this card** | **MUST NOT OCCUR** — `COMBAT-*` |
| L40 | **Infravision possession decided by this card** | **MUST NOT OCCUR** — `CHAR-009` |
| L41 | **Any magical light source handled here** | **MUST NOT OCCUR** — `MAGIC-*` |

### Seam guards

| # | Input | Expected |
|---|---|---|
| L42 | **Any price, `Coin` or encumbrance value emitted** | **MUST NOT EXIST** — guard test; `CHAR-004` |
| L43 | **Any ration mechanic** | **MUST NOT EXIST** — guard test; ownership unassigned |
| L44 | **Any starvation mechanic or causation** | **MUST NOT EXIST** — guard test |
| L45 | **Torch resolved as a weapon** | **ERROR** — `COMBAT-*`/`CHAR-004` |
| L46 | **Oil resolved as a thrown missile, or a pursuit-delay value** | **ERROR** — RC states **no** delay mechanic; none exists to call |
| L47 | Mirror or lip-reading use requiring a lit area | this card reports `any_mundane_source_lit` and the radii of its own sources; **whether the area counts as "lit" is not this card's call, and the item/skill mechanic is not owned here** |

---

## Provenance Classification

| Element | Classification |
|---|---|
| §2 radii; §3 durations; §5 tinderbox `1d6` on `1–2`; §5's once-per-round **rule**; §5's three RC-explicit `Fire-Building` branches and its three RC-silence refusals | **Rules Cyclopedia Explicit** (the refusals being RC silence, refused rather than filled) |
| **§5 precedence at `(skill, no tinderbox, ADVERSE)` → `ROUTED_SKILL_CHECK`** | **`SR-11` — Simulator Ruling.** **Not** `Rules Cyclopedia Explicit`: RC states two parallel conditionals and no precedence. **Not** a `Necessary Mechanical Consequence`: neither outcome is forced, and the competing branch is equally well attested. **Not** a `Human-Approved Variant` and **not** `Alternate-Source Compatible Completion`: no source is preferred over RC and no alternate edition was consulted. It resolves an intersection RC leaves genuinely ambiguous |
| §5.1 `attempt_already_made_this_round` as a **caller-supplied input** | **Not a rule** — an API boundary, identical in kind to `elapsed_turns`. The *rule* (one attempt per round) is RC Explicit; only the question of who tracks the round is answered here, and it is answered by **not** answering it inside this card |
| §7's recorded p. 92/p. 93 facts; §8's statement of RC's `complete darkness + no infravision → blindness` rule | **Rules Cyclopedia Explicit — recorded as ROUTED EVIDENCE, not executed here** |
| §4 depletion arithmetic against elapsed turns | **Necessary Mechanical Consequence** of RC's turn-denominated durations and `EXP-002`'s authoritative turn |
| **§4 an `EXPENDED` source contributes no illumination** | **Necessary Mechanical Consequence.** Premises, both RC Explicit: a torch *"burns for one hour (six turns)"* and a lantern *"[burns] one flask of oil in four hours (24 turns)"* (pp. 69–70), and each casts its `30'` radius **by burning**. A stated finite duration that has elapsed is a duration that is over; a source not burning is not casting its radius. No alternative reading of a finite printed duration exists, so **no Simulator Ruling is required**. **Scoped to the source** — it says nothing about the party or the world (guard L15b) |
| §3 "no conversion performed" | **Necessary Consequence** — RC states both hours **and** turns itself |
| §5's `REFUSE` branches (L23, L24) | **Necessary Consequence of a stated qualification** — RC expressly limits the `1d6` to ordinary circumstances; refusing is the only reading that does not extend it |
| **`normal dungeon conditions` → `DIM_LIGHT`** | **NOT CLASSIFIED — WITHDRAWN.** Not `Rules Cyclopedia Explicit`, not a `Necessary Consequence`, and not present anywhere in the specification. The accepted evidence classified the inference `QUALIFIED, not forced` (`E-13a`); human adjudication 2026-10-01 (Finding A) withdrew it from the card entirely. Guard test L30 |
| §6 `any_mundane_source_lit = false` asserting nothing further | **Scope limitation, not a rule** — the card owns only its own sources (Finding B). Guards L29, L37, L37a |
| §7 no `Visibility` category produced | **Ownership boundary** — `ENC-001` owns classification (Finding B / §4 direction). Guards L31–L33, L36 |
| §4's silence at zero *beyond* the source ceasing to burn | **Explicitly undefined by RC** — guard tests L15, L15b |
| §B, §C routing | **Not rules** — repository responsibility boundaries, set by accepted Stage-A evidence and governance |
| §D rations, §E starvation | **Evidenced, ownership deliberately unassigned by governance** |

**This card contains exactly one `Simulator Ruling` — `SR-11` — and no
`Alternate-Source Compatible Completion` and no `Human-Approved Variant`.**

---

## Synthesis Falsification

Performed before declaring this card ready, against the nine challenges set by the authorizing
direction.

| # | Challenge | Result |
|---|---|---|
| 1 | **Accidental ownership of downstream light consequences** | **Clean — and tightened 2026-10-01.** The pre-remediation card reported a **blindness predicate** derived from its own `any_lit == false`. Human review found that unsupported: this card cannot establish complete darkness (Finding B). §8 now asserts **no predicate at all**; it supplies illumination facts only. Guards L37, L37a, L38–L41 |
| 2 | **Duplicate dungeon-time authority** | **Clean.** §4 consumes `EXP-002`'s elapsed turns and owns no counter. Guards L13–L14. The Timetrack is recorded as a tally instrument, not adopted |
| 3 | **Duplicate equipment/catalog authority** | **Clean.** No price, price form, `Coin` or encumbrance value appears anywhere in the specification. Guard L42 |
| 4 | **Hidden assumptions about encounter distance** | **Clean — and corrected 2026-10-01.** The pre-remediation card produced a `Visibility` category and demanded a surprise state to query it. **Human review found that over-reached**: classification is `ENC-001`'s, and surprise is not an input to this card's own light state. §7 is now **routed evidence only**; no category is produced (L31), no die is rolled (L33), no path is resolved (L36), and querying light state without surprise **succeeds** (L34) |
| 5 | **Implicit magical-light behavior** | **Clean.** Only `TORCH` and `LANTERN` exist. Guard L41. The `Index to Spells` (p. 300) was enumerated in Stage A and every light/darkness entry on it is a spell |
| 6 | **Unsupported ration ownership** | **Clean.** §D records the evidence and assigns nothing. Guard L43. No ration appears in §1–§8 |
| 7 | **Starvation ownership leakage** | **Clean.** §E. Guard L44. `SR-10` is referenced as `CHAR-005`'s and not extended |
| 8 | **Resource timing not actually stated by RC** | **Clean.** `6` and `24` turns are RC's own turn-denominated figures. **No partial-turn proration, no burn-out event and no relight-cost was invented** — L15 guards precisely this, and it is the most tempting thing in the card to add |
| 9 | **Claims inherited from the superseded first-pass packet** | **Checked explicitly.** The first-pass packet asserted *"RC states no consequence for having no light"* and *"no light-bearing table exists"*. **Both were falsified, and this card asserts the opposite of each** — §Explicit 6 and 7, sourced to pp. 150/154 and 92/93. **No clause of this card traces to the failed packet** |

---

## Open Questions

**None block approval.** All six are mapped RC silences or governance items carried forward from
accepted Stage-A evidence.

1. **What happens when a light source's duration reaches zero.** RC states nothing; guard L15
   prevents invention.
2. **How carried mundane light maps to any `Visibility` category.** RC supplies no rule.
   `ENC-001` owns the classification; guards L30–L33.
3. **Adverse-condition ignition without `Fire-Building`.** Refused, not defaulted; guards L23, L26.
4. **Deliberate extinguishing.** RC gives the lantern's shuttering as a property, not a procedure.
5. **Rations — ownership open** (§D), by express direction.
6. **Starvation causation has no Rule ID** (§E) — a standing open governance issue, confirmed
   still true against the restored registry.
7. **The complete-darkness / environmental-illumination world-state predicate has no owner.**
   RC states the consequence (p. 150) and this card can supply one input to it, but **no Rule ID
   in `INVENTORY.md` owns global or ambient illumination state.** Raised by human review
   2026-10-01 (Finding B). **No owner is invented here**, and nothing in this card depends on one
   existing.

**Explicitly closed, recorded so they are not re-raised:** whether RC states a no-light
consequence (**yes** — p. 150, corroborated p. 154; the first-pass denial is withdrawn); whether a
light-conditioned table exists (**yes** — p. 93, gated by p. 92); whether RC supplies a
duration-tracking procedure (**a manual tally method, not an executable procedure** — p. 149);
whether `EXP-006` owns encounter distance (**no**); whether the Timetrack creates a second time
authority (**no**).

**Explicitly withdrawn by human review 2026-10-01, recorded so they are not reintroduced:** that
*"normal dungeon conditions"* yields `DIM_LIGHT` (**Finding A** — withdrawn; the shared `2d6×10'`
proves nothing); that this card may produce a `Visibility` category (**Finding B** —
withdrawn; `ENC-001` owns it); that `any_lit == false` establishes darkness or blindness
(**Finding B** — withdrawn); and that surprise is an input to querying this card's light state
(**withdrawn**).

## Approval

- Approved by: **Human project owner**
- Date: **2026-10-01**
- Approved at: **`b9af2270f80d67def24b913c264f5f133628452e`**
- Notes: Ratifies the §1–§8 mechanical contract and the §A–§E boundaries. At approval the card
  owned **no** Simulator Ruling; **`SR-11` was added 2026-10-01** by separate human adjudication
  (§Simulator Ruling). Every other clause is `Rules Cyclopedia Explicit` or a necessary
  consequence of one. The eight bounded-remediation findings are accepted as listed in §Status. Six RC silences,
  plus the unowned complete-darkness world-state predicate (Open Question 7), **remain named and
  guarded rather than filled, by express approval**. Rations and starvation causation **remain
  deliberately unassigned**. Implementation is **not** authorized by this approval.

**Submitted contract:** the §1–§8 mechanical specification and §A–§E boundaries, carrying
**exactly one Simulator Ruling (`SR-11`)**, **no `Alternate-Source Compatible Completion`** and
**no `Human-Approved Variant`** — every other clause `Rules Cyclopedia Explicit` or a necessary
consequence of one, with seven source silences named and guarded rather than filled.
