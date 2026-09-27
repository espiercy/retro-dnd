# ISSUE-016: CHAR-004 Catalogs, Starting Money and Derived Encumbrance (CLUSTER-003 Slice B)

## 1. Issue/Task Identifier and Objective

ISSUE-016 (completion-record ledger). Implement **Slice B** of
`docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §10: the V1 mundane
equipment catalogs, starting money, the free starting kit, and the
derived-encumbrance cases of `CHAR-004` §6.2.

No other Rule Card is implemented. **Per-class equipment legality and the
Druid `+50%` surcharge are `CHAR-004` §5/§7 and belong to Slice C**;
`CHAR-005` and `EXP-003` are untouched, and no placeholder for any of them
was created.

**Status: accepted by the human project owner, 2026-09-27**, after an
independent catalog-transcription review and three rounds of
human-adjudicated amendment.

## 2. Approved Inputs/Specifications

- `docs/rules/character_creation/starting_equipment_and_expedition_preparation.md`
  (`CHAR-004`, Status `APPROVED`, human-approved 2026-09-24; **amended
  2026-09-26 and 2026-09-27**) — the governing Rule Card.
- `docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` §6.2, §6.5, §9, §10
  (Slice B) — the approved implementation contract.
- `docs/rules/evidence/CLUSTER-003-catalog-transcription-review.md` — the
  independent second-pass transcription review of 2026-09-26 and its
  dispositions.
- `ARCHITECTURE.md` §15.2 step 4 — implementation-readiness re-approval,
  given by the human project owner; Slice A landed first (`eda2378`).
- RC Chapter 4 pp. 62–63, 65, 67, 69 — the printed tables `CHAR-004` §6.1
  **incorporates by reference** rather than enumerating. Transcribed from
  the page images and independently re-verified against them.

## 3. Files Created, Modified, or Deleted

**Created:**

- `src/rules/character_creation/equipment.py`
- `tests/rules/character_creation/test_equipment.py`
- `docs/rules/evidence/CLUSTER-003-catalog-transcription-review.md`
- This completion record.

**Modified:**

- `src/rules/character_creation/errors.py` — three new subclasses.
- `docs/rules/character_creation/starting_equipment_and_expedition_preparation.md`
  — the 2026-09-26 and 2026-09-27 amendments.
- `docs/rules/INVENTORY.md` — `CHAR-004` row.
- `docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md` — case ledger,
  conversion-note correction.
- `tests/rules/test_currency.py` — `IN_COPPER` immutability test.
- `docs/completion-records/INDEX.md` — index row.

**Deleted:** none.

Committed on `cluster-003-stage-a-evidence`. **Not merged** — under plan
§11 the branch stays unmerged until the cluster completes, and each slice
is *reviewed and accepted* rather than merged.

## 4. Behavior Actually Implemented

### Catalogs

`WEAPONS` (40 entries against 42 printed rows), `AMMUNITION` (7), `ARMOR`
(7) and `ADVENTURING_GEAR` (37 entries against 38 printed rows), as
`MappingProxyType` tables over frozen rows. The two printed weapon rows RC
prices by dimension are built by `net()` and `whip()`; the two printed gear
bundle rows are the 6- and 12-count offers of `TORCH` and `IRON_SPIKE`.
**No printed row of any of the four tables is missing.**

### Price specification (card §4.1)

Three closed forms — `FixedPrice`, `QuantityPrice`, `OpenEndedPrice` —
because a catalog price is not always one exact amount. The currency
primitive is untouched: `Coin` still holds only exact, non-negative,
integral copper pieces.

### Starting money

`starting_gold(rng)` — `3d6 x 10` gp through the RNG abstraction, one
expression, three d6, one sequence number.

### Derived encumbrance (card §6.2, §6.3)

Container-plus-contents with capacity as a hard limit; belt pouch `52 cn`
(`SR-6`); quiver `10 cn` total; worn-versus-packed clothing as an argument
rather than a mutation; ammunition as an inverse rate, exact or refused;
missile-weapon load variation; `net()` and `whip()`; waterskin.

### Purchase arithmetic

`selection_cost()` sums printed unit costs. Affordability and deduction are
the shared `Coin` primitive's ordering and its refusal to go below zero.

## 5. Rules Provenance

| Element | Classification |
|---|---|
| Catalog costs, encumbrances, capacities, conversions; §6.2 rows except those marked otherwise | **Rules Cyclopedia Explicit** |
| Belt pouch filled `52 cn` | **Simulator Ruling `SR-6`** (pre-existing) |
| Ammunition `Enc` as an inverse rate; net/whip derivation; filled-container arithmetic; empty sling `14 cn` | **Necessary Mathematical-Mechanical Consequence** |
| Torch quantity offers; "Clothes, extravagant" open-ended price; blowgun `5` darts; Sling `20 cn` includes 30 stones | **Rules Cyclopedia Explicit**, per the 2026-09-26 and 2026-09-27 amendments |
| Weapons Table `1/6 gp` read as the per-six rate | **Printed-notation reading**, the same category as the card's "Clothes, plain" marker; **not** a ruling |

**No new Simulator Ruling was made. No `Alternate-Source Compatible
Completion` is claimed. No Human-Approved Variant exists.**

## 6. Tests Added or Modified

`tests/rules/character_creation/test_equipment.py` — approved cases
`E1`–`E25`, `E53`–`E60` and `E61`–`E68`, with case IDs in docstrings and
`parametrize` ids. **`E26`–`E52` are Slice C and appear nowhere.**
`tests/rules/test_currency.py` gained the `IN_COPPER` immutability test.

Guard tests assert the *absence* of: class legality, Druid pricing,
`CharacterClass`, movement, encumbrance bands, total carried load,
mounts/vehicles/ships/siege, the Chapter 10 pathway, `float`/`Decimal`/
rounding, and fractional copper.

## 7. Exact Verification Commands Executed

```text
uv run python scripts/verify.py
```

## 8. Verification Results

```text
Tests:     PASS
Coverage:  PASS
Ruff:      PASS
mypy:      PASS
Overall:   PASS
```

## 9. Coverage Results

100% branch, per file:

```text
src/rules/character_creation/equipment.py   100%   0 missed
src/rules/character_creation/errors.py      100%
src/rules/currency.py                       100%
src/rules/  16 files at 100% branch per file; core aggregate 100.00%
```

## 10. Deviations

1. **`Ammunition` is its own type**, not an `Item` — the Ammunition Table's
   `Enc` is an inverse rate, and reusing `encumbrance_cn` would invite the
   misreading the card warns about.
2. **`missile_weapon_encumbrance(weapon, ammunition, shots)`** split from
   `ammunition_encumbrance` — two different printed rules.
3. **`selection_cost` added**, not in the plan's §6.2 sketch, because the
   plan assigns `E53`–`E55` to Slice B.
4. **`free_starting_kit(plain_clothes_sets)` takes a required argument**
   rather than being a constant: RC says "two or three" and a constant
   would have to pick one.
5. **Armor note codes `D`/`T`/`S` not transcribed** — class-facing, and
   card §7 states the permissions directly; carrying both would create a
   second authority for one rule.
6. **`UnresolvedPriceError` added** beyond the plan's §6.5 list, because
   the plan predates card §4.1.
7. **`E58`–`E60` landed in Slice B**, not Slice C as §10 assigns them:
   they are absence guards and belong with the data they guard.

## 11. Known Limitations/Unresolved Issues

- **Deferred, accepted by the human project owner 2026-09-27:** the net's
  printed size is the disjunction `M or L`, which RC resolves through the
  Nets Table; `net()` leaves `size` `None`, documented. Does not block
  Slice C.
- **Accepted, 2026-09-27:** `catalog_item("Torches")` and
  `catalog_item("Iron spikes")` raise for names RC prints as table
  headings. Canonical lookup uses the singular commodity name; both
  printed quantity offers are preserved.
- **Not V1-wired, unchanged:** the Chapter 10 high-level equipment
  pathway (card §C); mounts, vehicles, ships and siege equipment (card §B).
- **Card §8's unlisted-item procedure** is implemented as a rejection path
  only; no DM-availability policy object exists yet, as none is approved.

## 12. Architectural Consequences

`equipment.py` extends the landed style — pure functions and small frozen
value objects over explicit inputs, `MappingProxyType` tables, plain
`ValueError` for structural violations and `CharacterCreationError`
subclasses for domain rejections. No orchestration, inventory, ownership
or purchasing-workflow type was introduced. The dependency graph stays
acyclic: `equipment` imports `rng` and `currency` and nothing else from
`rules/`.

**Price specification is now distinct from a price amount.** That is the
one genuinely new concept this slice contributes, and it exists because RC
prints prices that are not single amounts — not because the implementation
wanted a richer model.

## 13. Independent Review

An independent second-pass transcription review (a separate reviewer that
did not author the transcription, per `DEC-0010` §10.1.2's principle)
compared every executable catalog row against the RC page images: 120 line
items, **115 MATCH, 4 DEFECT, 3 SOURCE-AMBIGUOUS**, all five governing
pages verified visually.

**No numeric transcription error was found in any of the four catalogs.**
The four defects were one dropped printed quantity (the twelve-spike
bundle) and three documentation defects; all are corrected. Of the three
ambiguities, one was adjudicated by the human project owner (the sling),
and two were accepted as documented-and-deferred.

## 14. Acceptance

- Accepted by: **Human project owner**
- Date: **2026-09-27**
- Notes: Accepted after the sling amendment landed. The independent review
  is recorded as having done its job — no numeric catalog transcription
  errors remain, the identified defects are corrected, and the one blocking
  ambiguity received a source-supported resolution that required no
  Simulator Ruling.
