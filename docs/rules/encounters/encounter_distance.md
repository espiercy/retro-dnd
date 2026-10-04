# Rule Card: Encounter Distance

## Rule ID

`ENC-001`

## Title

Encounter Distance

## Status

`APPROVED`

> **Approved by the human project owner, 2026-10-04**, as drafted at `9c9027b`. Only a human
> project owner may set this status (`SOURCE_HIERARCHY.md` §9, `AGENTS.md` §2); no agent may,
> and none did — this records the owner's decision.
>
> **Approval basis, as given:**
>
> - Stage A `ACCEPTED` under `DEC-0013`;
> - Stage B `COMPLETE`;
> - `SR-12` approved;
> - independent Rule Card semantic review **`PASS`**;
> - the post-review provenance correction mechanically verified;
> - **no blocking findings remain.**
>
> This card carries **one Simulator Ruling — `SR-12`** — and **no** `Alternate-Source
> Compatible Completion` and **no** `Human-Approved Variant`.
>
> **Approval authorizes implementation of this card's specification; it does not by itself
> clear the project-level Pre-Code Development Gate** (`ARCHITECTURE.md` §16), and no
> implementation, test or implementation plan exists for `ENC-001` yet.

## Rules Domain

`encounters`

---

## Rules Cyclopedia Source

*Dungeons & Dragons Rules Cyclopedia* (TSR, 1991). Pages carried by this card, all inspected as
authoritative page images during the accepted Stage-A research:

| Page | What it supplies |
|---|---|
| Ch. 7 p. 91 | Game Turn Checklist step 1; `Wandering Monsters`; the `Encounters` definition |
| Ch. 7 p. 92 | the `Encounter Distance` section and its three surprise branches |
| Ch. 7 p. 93 | the **Encounter Distances Table** and its three footnotes; `Wandering Monster Encounters` (City) |
| Ch. 6 p. 87 | `Feet vs. Yards` — the indoor/outdoor unit convention |
| Ch. 7 p. 95 | `Wilderness Encounters` routes back to the same Checklist and Table |
| Ch. 7 p. 98 | `Contact` — defers to the earlier encounter rules |

Full evidence, transcriptions and page dispositions:
`docs/rules/evidence/ENC-001-evidence.md` (Stage A `ACCEPTED`).
Stage-B adjudication history: `docs/rules/encounters/ENC-001-stage-b-adjudications.md`.

## Rules Cyclopedia Explicitly Establishes

1. **Distance is determined after surprise.** *"Once the Dungeon Master has determined that an
   encounter will take place and **has determined the relative conditions of surprise** for the
   two groups, he or she can decide how far apart the two parties are"* (p. 92).
2. **Both parties surprised → a flat `1d4 × 10'` (or yards outdoors)** (p. 92).
3. **One party surprised → the unsurprised party notices at the `1d4 × 10'` (or yards) distance
   rolled; the surprised party does not notice until half that distance** (p. 92).
4. **Neither party surprised → consult the Encounter Distances Table** (p. 92), keyed on
   `Setting`, `Visibility` and `Encounter` (p. 93).
5. **The table's thirteen rows, with their printed units** (p. 93) — reproduced in §4 below.
6. **The three table footnotes** (p. 93): `*` *"Or other indoor setting."*; `**` *"Or full
   darkness with infravision used."*; `†` *"Or very poor visibility (heavy snow or fog,
   sandstorm, etc.)."*
7. **City is treated as wilderness terrain** — *"'City' is treated just like any other
   wilderness terrain"* (p. 93).
8. **The unit convention**: the foot indoors, the yard outdoors (p. 87).
9. **The Encounter Checklist contains no distance step** — its six steps are Game Time,
   Surprise, Initiative, Reactions, Results, Encounter Ends (p. 93).
10. **Wilderness encounters route back to this same table** — *"Consult the Encounter Checklist
    and the Encounter Distances Table"* (p. 95).

## Rules Cyclopedia Leaves Undefined / Ambiguous

Stated as narrowly as the accepted evidence supports. Each is recorded in the accepted Stage-A
packet §13 and **none blocks this specification**:

- **Which visibility category obtains at a given moment** (`Q-7`). RC states no selector in the
  chapters searched. Resolved architecturally, not by RC: the category is **supplied** to this
  card — see §2 and §Scope Boundaries B.
- **Whose infravision satisfies footnote `**`** (`Q-4`). Affects *classification*, not this
  card's formula — see §6.
- **Whether a `2d6 × 10'` Dim-light roll exceeding infravision's `60'` changes anything**
  (`Q-5`). RC states no capping or re-roll rule, and this card invents none.
- **Whether p. 91's mutual-notice language and p. 92's asymmetric one-surprised branch can be
  reconciled** (`Q-2`, surviving half). Concerns awareness description, not the distance
  produced.
- **Whether p. 98's word order carries procedural force** (`Q-8`). p. 98 states no procedure of
  its own and defers to pp. 91–93.

---

## Alternate-Source Completion Research

**Not applicable.** No gap in this card's mechanical specification required alternate-source
completion. The one ambiguity that affected the specification (`Q-1`) was closed by a Simulator
Ruling after the RC text itself was found not to resolve it; see §Simulator Ruling.

## Compatibility Analysis

**Not applicable** — no alternate-source candidate was imported, so there is nothing to
classify under `SOURCE_HIERARCHY.md` §6.

---

## Simulator Ruling

This card depends on **exactly one** Simulator Ruling, `SR-12`, approved by the human project
owner on 2026-10-04. It carries no `Alternate-Source Compatible Completion` and no
`Human-Approved Variant`.

### `SR-12` — encounter distance is determined once, by pp. 92–93

```text
SIMULATOR RULING SR-12                                      APPROVED
Encounter distance is determined ONCE per encounter, by the pp. 92-93
procedure. Where RC's p. 91 wandering-monster statement and the pp. 92-93
procedure would both apply, the pp. 92-93 procedure GOVERNS and the p. 91
`2d6 x 10'` is NOT rolled as a second, separate distance.

A wandering-monster encounter is a SORT of encounter (RC p. 92), not a
separate distance track.

APPROVED BY:  human project owner
DATE:         2026-10-04
```

**Why a ruling was required.** RC classifies a wandering-monster encounter as one *sort of
encounter* (p. 92) and routes every sort through the same Encounter Checklist; p. 91 defers to
the `Encounter Distance` section while p. 92 never defers back; and the Checklist contains no
distance step. But RC never *states* the precedence rule, and applying both presentations would
produce two distances for one encounter — which RC gives no rule for choosing between.

**What `SR-12` does NOT decide** — its scope, preserved verbatim from the adjudication so it
cannot drift:

- that *"normal dungeon conditions"* means `Dim light`, or any other visibility row;
- which visibility category obtains at a given moment, or who owns that world state;
- anything about surprise ownership, which remains `ENC-002`'s;
- the p. 91 / p. 92 awareness-language tension (mutual notice vs asymmetric notice).

## Human-Approved Variant

**Not applicable.**

---

## Approved Mechanical Specification

> **Proposed, not approved** — this card is `DRAFT`. The heading is the template's.

### 1. Purpose

Given an encounter that has already been determined to occur and whose surprise state is
already known, produce **the distance at which the two parties are when the encounter takes
place** — once, with its unit.

### 2. Inputs

All four are **caller-supplied**. This card derives none of them.

| Input | Domain | Owner / source |
|---|---|---|
| `surprise state` | both surprised / one surprised (and which) / neither surprised | **`ENC-002`** — consumed, never rolled or derived here |
| `setting` | exactly `Dungeon*`, `Wilderness`, `Ocean/sea`, `Undersea` | world/location state; a primitive supplied fact |
| `visibility` | the RC-native label legal for that `setting` — see §3 | **`SIM-003`** classification; validated here, never derived |
| `encounter type` | `DM's choice`, `Ship`, `Monster` | supplied; only where the table distinguishes it (`Ocean/sea`) |

**`Aerial` is not a member of the `setting` domain** and is rejected (§7, `Q-9`).

**City** is not a separate `setting`: *"'City' is treated just like any other wilderness
terrain"* (p. 93), so a city encounter is supplied as `Wilderness`.

### 3. Visibility vocabulary — setting-indexed, never normalized

```text
Dungeon*                 Very good light   |  Dim light**   |  No light†
Wilderness               Clear daylight    |  Dim light**   |  No light†
Ocean/sea                Clear daylight    |  Dim light**   |  No light†
Undersea                 Any light
```

**`Very good light` and `Clear daylight` are distinct labels and are NOT equated.** RC prints
two labels and nowhere equates them; they are in complementary distribution, so no setting
offers both and the lookup never needs an equivalence (`Q-3`). A label not legal for the
supplied `setting` is rejected (§7).

### 4. Procedure

```text
STEP 1  Surprise is ALREADY DETERMINED (p. 92). This card does not determine it.

STEP 2  If BOTH parties are surprised:
            distance = 1d4 x 10 feet      (Dungeon*)
            distance = 1d4 x 10 yards     (Wilderness, Ocean/sea, Undersea)
            VISIBILITY IS NOT CONSULTED and is NOT REQUIRED.

STEP 3  If ONE party is surprised:
            distance = 1d4 x 10 feet/yards, as above -- the distance at which
            the UNSURPRISED party notices the surprised party.
            RC adds that the surprised party does not notice the unsurprised
            party until they reach HALF that distance.
            VISIBILITY IS NOT CONSULTED and is NOT REQUIRED.

STEP 4  If NEITHER party is surprised:
            a. validate `setting` against the four legal values
            b. validate `visibility` as legal FOR THAT SETTING (section 3)
            c. select the single Encounter Distances Table row matching
               (setting, visibility, encounter type)
            d. apply that row's printed formula or flat value
            e. return it with that row's PRINTED UNIT -- no conversion

STEP 5  The distance is produced ONCE (SR-12). The p. 91 `2d6 x 10'`
        wandering-monster statement is NOT rolled as a second distance.
```

### 5. Encounter Distances Table (RC p. 93)

Every row this card requires, as printed. **`Ocean/sea` `Ship` rows are kept distinct from
`Monster` rows**, and no rows are collapsed because their expressions happen to match.

| # | Setting | Visibility | Encounter | Distance | Unit |
|---|---|---|---|---|---|
| 1 | `Dungeon*` | `Very good light` | `DM's choice` | `4d6 × 10` | feet |
| 2 | `Dungeon*` | `Dim light**` | `DM's choice` | `2d6 × 10` | feet |
| 3 | `Dungeon*` | `No light†` | `DM's choice` | `1d4 × 10` | feet |
| 4 | `Wilderness` | `Clear daylight` | `DM's choice` | `4d6 × 10` | yards |
| 5 | `Wilderness` | `Dim light**` | `DM's choice` | `2d6 × 10` | yards |
| 6 | `Wilderness` | `No light†` | `DM's choice` | `1d4 × 10` | yards |
| 7 | `Ocean/sea` | `Clear daylight` | **`Ship`** | **`300`** (flat) | yards |
| 8 | `Ocean/sea` | `Clear daylight` | `Monster` | `4d6 × 10` | yards |
| 9 | `Ocean/sea` | `Dim light**` | **`Ship`** | **`120`** (flat) | yards |
| 10 | `Ocean/sea` | `Dim light**` | `Monster` | `2d6 × 10` | yards |
| 11 | `Ocean/sea` | `No light†` | **`Ship`** | **`40`** (flat) | yards |
| 12 | `Ocean/sea` | `No light†` | `Monster` | `1d4 × 10` | yards |
| 13 | `Undersea` | `Any light` | `DM's choice` | `1d6 × 10` | yards |

**Footnotes, as RC prints them:**

```text
 *  Or other indoor setting.
 ** Or full darkness with infravision used.
 †  Or very poor visibility (heavy snow or fog, sandstorm, etc.).
```

Footnotes `*`, `**` and `†` **extend which conditions reach a row**; they do not change the
row's formula. `**` is a *classification*-side extension — see §6.

### 6. The infravision footnote — classification-side, not applied here

```text
The p. 93 footnote ** affects VISIBILITY CLASSIFICATION, not the
encounter-distance formula once the resulting Visibility label has
been supplied.
```

This card therefore consumes the **final** label. Given `Dim light` it applies row 2 (Dungeon)
whether that label arose from actual dim light or from full darkness with infravision used —
the procedure is identical either way.

**This card does not specify**, and must not be read as specifying: whose infravision counts;
how a mixed party is handled; or which upstream component applies the footnote. Those remain
**external and unresolved** (`Q-4`) — see §Open Questions.

### 7. Rejected inputs

This card **refuses** rather than guessing. RC supplies no default, so a simulator that must
not guess can only refuse (`AGENTS.md` §3, §13).

| Condition | Behaviour |
|---|---|
| `visibility` required by step 4 but absent | **refuse — invalid call** |
| `visibility` label not legal for the supplied `setting` | **refuse — invalid call** |
| `setting` outside the four legal values, **including `Aerial`** | **refuse — invalid call** |
| `encounter type` missing where `Ocean/sea` distinguishes `Ship` from `Monster` | **refuse — invalid call** |
| `visibility` absent on a **surprise** branch (steps 2–3) | **not an error** — visibility is not consulted there and **must not be demanded for formality** |

**No silent default.** In particular `"normal dungeon conditions"` is **not** read as
`Dim light`. This card's own accepted Stage-A evidence retains that question as `Q-1`,
`RETAINED AS GENUINE SOURCE AMBIGUITY`, and `SR-12` expressly does not reinstate the inference
— see its non-scope above. **`EXP-006`** reached the same conclusion separately: *its* accepted
evidence classified the inference `QUALIFIED, not forced` (`E-13a`) and human adjudication
2026-10-01 (**Finding A**) withdrew it from that card entirely.

**No exception class, function signature or message is specified here** — that is implementation.

### 8. Output

```text
A single encounter distance, carrying BOTH:
    magnitude   -- the rolled or flat value from the selected row/branch
    unit        -- feet for Dungeon*, yards for Wilderness/Ocean-sea/Undersea
```

RC supplies the unit at the point it supplies the magnitude (the table prints it on every row;
p. 92 states it inline for the surprise branches), so **returning a magnitude without its unit
would discard information RC supplied**, with a factor-of-three error as the failure mode.

**No conversion is performed.** This card never converts feet to yards or yards to feet, and
specifies no data structure — carrying the unit is a representation requirement, not an
RC-prescribed type.

---

## Scope Boundaries

### A. What this card owns

```text
Determination of encounter distance at contact, from already-established
encounter inputs -- and nothing else.
```

### B. What this card does **not** own

```text
Whether an encounter occurs                     EXP-001
Surprise determination                          ENC-002
Visibility classification                       SIM-003
Mundane light-source mechanics                  EXP-006
Magical light mechanics                         MAGIC-*
World/environment state generation              world/scenario state
Setting determination (beyond validating it)    world/location state
Infravision / character perception              CHAR-009; Q-4 unresolved
Pursuit, evasion, and pursuit start distance    ENC-005
Reaction                                        ENC-003
Morale                                          ENC-004
General unit conversion                         unowned; nothing converts
Aerial movement and aerial combat               outside this card entirely
```

### C. Encounter distance is not permission to skip anything

A random encounter is **not** automatically combat (`AGENTS.md` §5). Producing a distance does
not bypass surprise, reaction, negotiation, morale, or evasion and pursuit where those systems
apply. This card produces one number and one unit; it decides nothing about what happens next.

### D. The `SIM-003` seam

This card consumes the **final RC-native visibility classification** and nothing behind it. It
does not know, and must not require, whether that classification came from daylight, weather,
mundane light, magical light, environmental darkness, or any other `SIM-003`-owned aggregation
input. **It does not consume `EXP-006` directly** — `EXP-006` is an upstream contributor *to
`SIM-003`*.

---

## Deterministic Test Cases

Conceptual input → expected-output cases, per `TESTING_STRATEGY.md` §2. **No implementation,
API or test code is specified here.**

| # | Input | Expected |
|---|---|---|
| D1 | Both surprised, `Dungeon*` | `1d4 × 10` **feet**; visibility not consulted |
| D2 | Both surprised, `Wilderness` | `1d4 × 10` **yards**; visibility not consulted |
| D3 | One surprised, `Dungeon*` | `1d4 × 10` **feet** for the unsurprised party; surprised party notices at **half** that |
| D4 | Both surprised, visibility **not supplied** | **succeeds** — visibility must not be demanded on this branch |
| D5 | Neither surprised, `Dungeon*` + `Very good light` | `4d6 × 10` feet |
| D6 | Neither surprised, `Dungeon*` + `Dim light` | `2d6 × 10` feet |
| D7 | Neither surprised, `Dungeon*` + `No light` | `1d4 × 10` feet |
| D8 | Neither surprised, `Wilderness` + `Clear daylight` | `4d6 × 10` yards |
| D9 | Neither surprised, `Undersea` + `Any light` | `1d6 × 10` yards |
| D10 | Neither surprised, `Ocean/sea` + `Clear daylight` + `Ship` | **flat `300` yards** |
| D11 | Neither surprised, `Ocean/sea` + `Clear daylight` + `Monster` | `4d6 × 10` yards |
| D12 | Neither surprised, `Ocean/sea` + `Dim light` + `Ship` | **flat `120` yards** |
| D13 | Neither surprised, `Ocean/sea` + `No light` + `Ship` | **flat `40` yards** |
| D14 | A city encounter supplied as `Wilderness` | the `Wilderness` rows apply |
| D15 | `Dungeon*` + `Clear daylight` | **refuse** — label not legal for that setting |
| D16 | `Wilderness` + `Very good light` | **refuse** — label not legal for that setting |
| D17 | `setting = Aerial` | **refuse** — not a Setting |
| D18 | Neither surprised, visibility absent | **refuse** |
| D19 | `Ocean/sea`, neither surprised, encounter type absent | **refuse** |
| D20 | **Any result returned as a bare magnitude without its unit** | **MUST NOT OCCUR** — guard |
| D21 | **Any feet↔yards conversion performed by this card** | **MUST NOT OCCUR** — guard |
| D22 | **`Very good light` and `Clear daylight` normalized to one category** | **MUST NOT OCCUR** — guard (`Q-3`) |
| D23 | **A second distance rolled from p. 91's `2d6 × 10'` for a wandering-monster encounter** | **MUST NOT OCCUR** — guard (`SR-12`) |
| D24 | **`"normal dungeon conditions"` producing `Dim light` or any category inside this card** | **MUST NOT OCCUR** — guard |
| D25 | **This card deriving, classifying or adjusting a visibility category** | **MUST NOT OCCUR** — guard (`SIM-003` owns it) |
| D26 | **This card rolling or deriving surprise** | **MUST NOT OCCUR** — guard (`ENC-002` owns it) |
| D27 | **This card applying the footnote `**` infravision adjustment** | **MUST NOT OCCUR** — guard (`Q-4`, upstream) |
| D28 | **An `Aerial` row existing in the table** | **MUST NOT EXIST** — guard (`Q-9`) |

## Provenance Classification

| Clause | Classification |
|---|---|
| §3 vocabulary; §5 table rows, values, units and footnotes; §4 steps 2–4 branch structure; City as wilderness terrain | **Rules Cyclopedia Explicit** |
| §4 step 1 — surprise precedes distance | **Rules Cyclopedia Explicit** (p. 92's own ordering) |
| §4 step 5 — distance produced once; p. 91 not rolled again | **`Simulator Ruling` — `SR-12`**, approved 2026-10-04 |
| §7 refusal on a missing or illegal required input | **Necessary Mechanical Consequence** of RC supplying no default plus the no-guessing requirement |
| §8 the result carries magnitude **and** unit | **Necessary Consequence / Repository Boundary** — **not** an RC-prescribed data structure |
| §2 inputs caller-supplied; §6 footnote `**` left upstream; §Scope Boundaries B and D | **Repository Boundary / Architecture** — human architecture decision 2026-10-04 (`Q-7`) |
| `Aerial` rejected as a Setting | **Necessary Consequence** of RC's two-level encounter taxonomy (`Q-9`) |
| Whose infravision satisfies footnote `**`; `SIM-003`'s daylight and weather inputs | **Open External Dependency** — see §Open Questions |

**No architecture decision above is presented as an RC rule**, and no software representation
is presented as RC-prescribed.

---

## Open Questions

**None blocks this specification.** Each is recorded as `NON-BLOCKING FOR ENC-001 RULE CARD`
in the Stage-B completion assessment, which is the authoritative record of their status —
not restated here.

| # | Question | Status |
|---|---|---|
| `Q-4` | Whose infravision satisfies footnote `**`, and which component applies it | **external, upstream** — `SIM-003` open dependency 1. **NON-BLOCKING** |
| — | `SIM-003`'s daylight / time-of-day input has no owner | **external** — `SIM-003`'s. **NON-BLOCKING** |
| — | `SIM-003`'s weather visibility input has no owner | **external** — `SIM-003`'s. **NON-BLOCKING** |
| `Q-2` | p. 91 mutual notice vs p. 92 asymmetric notice | awareness description, not the distance produced. **NON-BLOCKING** |
| `Q-5` | A Dim-light roll exceeding infravision's `60'` | RC states no cap; this card invents none. **NON-BLOCKING** |
| `Q-8` | Whether p. 98's word order carries procedural force | p. 98 defers to pp. 91–93. **NON-BLOCKING** |

**Current project status for these lives in the Stage-B artifact**
(`docs/rules/encounters/ENC-001-stage-b-adjudications.md`), which is their single authoritative
owner. This card states durable rules and boundaries, not changing project state.

## Approval

- Approved by: `human project owner`
- Date: `2026-10-04`
- Notes: Approved on the basis recorded in §Status — Stage A `ACCEPTED` under `DEC-0013`,
  Stage B `COMPLETE`, `SR-12` approved, independent Rule Card semantic review `PASS`, the
  post-review provenance correction mechanically verified, and no blocking findings remaining.
  The card was drafted at `d57246b` and corrected at `9c9027b`; it was **not** reviewed or
  certified by its author.
