# `SIM-003` — World/Environment Visibility Classification

> **This is a Simulator Specification (Non-Historical Design Requirement), not a Rule Card.**
> It specifies a responsibility boundary the simulator must own *because the Rules Cyclopedia
> supplies no determination procedure*. Nothing in it is an RC rule, and it must not be read
> as one. It is registered in `docs/rules/INVENTORY.md` under **Simulator Specifications**.

```text
STATUS:       OWNERSHIP BOUNDARY DEFINED -- NOT IMPLEMENTED, NOT DESIGNED
CREATED:      2026-10-04
AUTHORITY:    human architecture decision, 2026-10-04
SUPERSEDES:   the "world/environment visibility OWNER: NOT YET ASSIGNED" gap
              recorded in ENC-001 Stage-B Q-7
```

## 1. Purpose

`ENC-001` consumes an RC-native visibility label to select a row of the Encounter Distances
Table (RC p. 93). The `ENC-001` accepted Stage-A evidence establishes, at the scope it
searched, that **RC states no procedure for determining which visibility category obtains**.
Human adjudication then settled that `EXP-006` does not own aggregate/world visibility and
that `ENC-001` does not derive it.

`SIM-003` exists to own that one missing step, so the category is **derived once**, by a named
owner with a bounded contract, rather than re-derived inside every consumer or inferred
silently from a provider that disclaims it.

## 2. Responsibility — **classification only**

```text
Given:
    the setting
    supplied world/environment facts
    the applicable separately-owned light contributions

Derive:
    exactly one RC-native visibility label, valid for that setting
```

That is the whole responsibility. `SIM-003` is a **derivation**, not a state store and not a
simulation of the conditions it reads.

## 3. Inputs

`SIM-003` **consumes** these facts. Consuming a fact does **not** make `SIM-003` the owner of
the mechanics that produce it, nor its storage owner.

| Input | Supplied by |
|---|---|
| Setting (`Dungeon*` / `Wilderness` / `Ocean/sea` / `Undersea`) | the caller, with the situation |
| Ambient / environment state of the area | world state — `ARCHITECTURE.md` §6 **Dungeon State** (*rooms/areas*, *persistent environmental changes*) |
| Daylight / time-of-day state | scenario / world state; `ARCHITECTURE.md` §6 **Campaign State** holds *calendar/time* |
| Weather visibility state | scenario / world state |
| Environmental darkness | scenario / world state |
| Mundane light-source contribution | **`EXP-006`** |
| Magical-light contribution, where applicable | **`MAGIC-*`** |

**Where RC provides no determination procedure, the fact is scenario/world-state supplied**
unless and until a future card or specification establishes a mechanic. That is a normal
supplied input, **not** an ownership gap — a fact having no Rule Card is not a defect, and no
artificial gap is recorded for one.

## 4. Output

Exactly one RC-native visibility label, valid for the supplied setting. The vocabulary is
`ENC-001`'s, settled under `Q-3`, and is reproduced here as the contract's value domain:

```text
Dungeon*       Very good light   |  Dim light   |  No light
Wilderness     Clear daylight    |  Dim light   |  No light
Ocean/sea      Clear daylight    |  Dim light   |  No light
Undersea       Any light
```

**`Very good light` and `Clear daylight` are NOT normalized into one category.** They are
distinct RC-native labels in complementary distribution; `Q-3` settled that RC never equates
them and that the distinction is preserved. `SIM-003` emits the label belonging to the
supplied setting and must not collapse the two.

## 5. Non-responsibilities — **explicit, to prevent absorption**

`SIM-003` does **not** own:

```text
day/night-cycle mechanics
calendar / time advancement                 EXP-002 owns the turn
weather generation
terrain / weather simulation
environment-state storage                   ARCHITECTURE.md section 6
light propagation
mundane light-source resource mechanics     EXP-006
magical-light spell mechanics               MAGIC-*
character-specific perception
infravision                                 CHAR-009 owns possession
blindness                                   CHAR-005 / COMBAT-* consequences
encounter distance                          ENC-001
surprise                                    ENC-002
feet/yards conversion or convention         still unowned
```

**`SIM-003` is not a general world-state subsystem.** If a later change would make it one,
that change is out of scope for this specification and requires its own architecture decision.

## 6. Provider boundaries

**`EXP-006` — mundane light-source contribution.** `SIM-003` consumes what `EXP-006` reports
and **must not reproduce its mechanics**: no light-source value model, no radius, no duration
or depletion, no ignition. `EXP-006`'s accepted boundary is unchanged by this specification,
including that the absence of a lit mundane source it owns is an absence of *that card's*
knowledge and **never** a fact about the world — `SIM-003` must not read it as darkness.

**`MAGIC-*` — magical-light contribution.** Consumed where applicable; spell mechanics are not
reproduced.

## 7. Character perception boundary

Character-specific perception stays **outside** this classification, for a structural reason:

```text
shared environment state must not vary solely because a different
character is observing it
```

Infravision, blindness and other per-character perception effects are therefore not inputs to
`SIM-003` and not part of its output. `SIM-003` reports the **world's** visibility; a rule
that needs to apply a character capability does so separately, with that capability supplied
by its own owner.

**Known unresolved dependency, preserved not closed.** RC p. 93's footnote `**` — *"Or full
darkness with infravision used"* — folds a character capability into a table-row selection.
Which rule applies that footnote, and on whose infravision, depends on `ENC-001` Stage-A
**`Q-4`**, which is `RETAINED AS GENUINE SOURCE AMBIGUITY`: *"Whose infravision satisfies
footnote `**` — any one member's, all, or the noticing side's? RC does not say which the
footnote means."* **`Q-4` is not adjudicated here**, and no perception engine is invented.

## 8. Known providers and consumers

| Role | Party | Basis |
|---|---|---|
| Provider | `EXP-006` — mundane light contribution | approved Rule Card, landed |
| Provider | `MAGIC-*` — magical light, where applicable | inventory |
| Provider | world/scenario state — setting, ambient, daylight, weather | `ARCHITECTURE.md` §6 |
| **Consumer** | **`ENC-001`** — Encounter Distances Table row selection | `ENC-001` accepted Stage-A evidence; `Q-7` human decision |

**Stated precisely, because the distinction matters.** `CHAR-005` (blindness/darkness
movement) and `COMBAT-*` (blindness attack/save/AC) are evidenced — via `EXP-006` §B routing
and RC p. 150, corroborated p. 154 — to need an **ambient-darkness fact**. Whether that fact
is *this* specification's label is **not established**: RC p. 150's *"area of complete
darkness"* and the table's `No light` row are related but not shown to be the same predicate,
and the `No light` row also covers *"very poor visibility (heavy snow or fog, sandstorm)"*.
They are therefore recorded as **likely future consumers, not confirmed ones** (§10).

## 9. Provenance

| Element | Classification |
|---|---|
| The RC-native visibility vocabulary and the table it keys | **Rules Cyclopedia Explicit** — RC p. 93 |
| RC supplies no procedure for determining which category obtains | **Rules Cyclopedia finding, scope-limited** — the chapters the `ENC-001` packet searched; **not** an RC-wide claim |
| The need for a single deterministic classification owner | **Necessary Consequence + Repository Architecture** |
| Assigning that ownership to `SIM-003` | **Human Architecture Decision**, 2026-10-04 |
| Raw daylight / weather values | **scenario / world-state supplied** unless separately governed |

**`SIM-003` is not an RC rule and must not be described as one.** It specifies who derives a
value RC assumes an adjudicator already knows.

## 10. Open dependencies

| # | Dependency | Status |
|---|---|---|
| 1 | **`Q-4`** — whose infravision satisfies footnote `**`, and which rule applies it | `RETAINED AS GENUINE SOURCE AMBIGUITY`; not adjudicated |
| 2 | **Daylight / time-of-day determination** has no owner | scenario-supplied today; no mechanic is created here |
| 3 | **Weather visibility determination** has no owner | scenario-supplied today; no mechanic is created here |
| 4 | Whether `CHAR-005` / `COMBAT-*` consume this label or a distinct ambient-darkness predicate | **not established**; see §8 |
| 5 | **Feet/yards** convention | unowned; explicitly not `SIM-003`'s |

None of these blocks the ownership boundary above. Items 2 and 3 are **supplied inputs**, not
gaps in this specification — `SIM-003` requires no decision about when sunrise occurs, how
weather is rolled, how fog forms, how long weather persists, or how light physically
propagates.

## 11. What this specification does not do

It defines **responsibility, not mechanics**. There is no algorithm, no API, no data model, no
error type and no implementation. A later, separately authorized task may design and implement
`SIM-003`; this artifact only fixes what it owns and what it must never absorb.
