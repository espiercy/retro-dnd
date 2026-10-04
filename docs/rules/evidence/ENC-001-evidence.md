# `ENC-001` — Encounter Distance — Stage-A Evidence

> **`DEC-0012` pilot packet.** This is the first Stage-A evidence packet written after
> `DEC-0012` was approved (2026-10-01) and therefore the first that the evidence linter
> actually governs. It is not grandfathered: `scripts/lint_evidence.py`'s `GRANDFATHERED`
> frozenset is a closed list of twelve pre-`DEC-0012` packets and contains no `ENC-001`
> entry (verified §9, row R-6).

```text
PACKET-STATUS
RULE-ID:              ENC-001
PASS:                 1
SELF-FALSIFICATION:   COMPLETE
REPOSITORY-FACT-PASS: COMPLETE
INDEPENDENT-REVIEW:   PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
RECOMMENDATION:       EVIDENCE READY FOR HUMAN REVIEW
```

---

## 1. Research-Start Gate

| Item | Established |
|---|---|
| Exact card scope, as currently registered | `INVENTORY.md` row 116: `ENC-001` \| Encounter Distance \| Encounters chapter \| RC Core \| Dependencies `—` \| Downstream `—` \| V1 Reachable Yes \| Status `Unresearched` \| "Low-medium." |
| Known ownership seams | `ENC-002` surprise determination; `ENC-005` evasion/pursuit; `EXP-001` wandering-monster check; `EXP-006` mundane light sources; `EXP-002` turn accounting; `MON-*` monster terrain/speed; `COMBAT-*` attack-roll mechanics |
| Authoritative primary source | *D&D Rules Cyclopedia* (TSR, 1991; ISBN 1-56076-085-0), archive.org item `TSR1071TheDDRulesCyclopedia`, IIIF page images, `leaf = printed_page − 1` |
| Required structural + index instruments | Chapter headings; **Index to Tables and Checklists** (p. 301); **General Index** (pp. 302–304); end-of-book boundary confirmed at p. 305 |
| Current repository dependencies | Verified against `INVENTORY.md` this pass — see §9 |
| Primary-source visual access confirmed | **yes** — 19 pages rendered and read as page images; no page required a second digitisation; no access blocker |

**Scope boundary this packet will not cross:** the *determination of surprise* (`ENC-002`),
the *evasion/pursuit procedure* entered after contact (`ENC-005`), the *occurrence* check
that decides an encounter happens at all (`EXP-001` / Chance of Encounter Table), and the
*consumption* of a distance once produced (`COMBAT-*` missile ranges). This packet
establishes only what RC states about **how far apart two groups are when an encounter
takes place**.

The human-approved boundary fixed before research began is binding here: `ENC-001` may
**consume** authoritative caller-supplied surprise state, and must not roll surprise,
derive it, reproduce `ENC-002`'s mechanic, or assign surprise ownership to itself. Every
surprise cross-reference below is recorded as an external governing input, not absorbed.

## 2. Primary Source Accessed

| Source | Access method | Role |
|---|---|---|
| *D&D Rules Cyclopedia*, TSR 1991 | page images — `https://iiif.archive.org/iiif/TSR1071TheDDRulesCyclopedia$<leaf>/full/1400,/0/default.jpg`, `leaf = printed_page − 1` | authoritative |
| *D&D Rules Cyclopedia*, second digitisation (archive.org item `rules-cyclopedia`, same leaf offset) | available, **not needed this pass** — every page rendered legibly from the first item (§9.2.1 — would still be primary) | authoritative (unused) |
| OCR / full text | **not used at any point in this packet** | not used |

**Access limitations encountered, including where a workaround succeeded** (§11 item 17):

One request, for leaf 305, returned HTTP 500. Leaf 305 is **past the end of the book** —
p. 305 (leaf 304) is the printed back cover, visually confirmed. No page bearing content
was blocked, and no finding rests on an unrendered page. Every page listed under
`IMAGE-VERIFIED` in §7 was confirmed by reading its body text, not by its HTTP status
(§9.2.1).

## 3. Source Structure

| Structural unit | Pages | Could govern this card? |
|---|---|---|
| Ch. 2 — The Character Classes | 13–31 | **yes, partly** — infravision is a branch selector in the governing table's footnote ** |
| Ch. 4 — Equipment | 62–74 | no — light *sources* are `EXP-006`'s; no distance mechanic |
| Ch. 5 — General Skills | 81–86 | no — no skill selects or modifies encounter distance |
| Ch. 6 — Movement | 87–90 | **yes** — the feet/yards distance convention the table's units depend on (p. 87) |
| **Ch. 7 — Encounters and Evasion** | **91–101** | **yes — principal.** Carries the Encounter Distance section, the Encounter Distances Table, and a second distance statement in the Game Turn Checklist |
| Ch. 8 — Combat | 102–116 | no for distance determination — attack-roll and underwater-combat mechanics only; one terminology tension recorded (p. 115) |
| Ch. 13 — Dungeon Master Procedures | 143–151 | no — blindness/invisibility are condition effects, no distance mechanic |
| Ch. 14 — Monsters | 152–218 | **yes, by cross-reference** — p. 92 routes monster-specific surprise variation here; monster Terrain line bears on the table's Setting axis |
| Appendix 4 — Indices | 301–304 | **yes** — the two completeness instruments |

## 4. Coverage Manifest

| # | Object | Class (§9.1 A–I) | Page | Disposition |
|---|---|---|---|---|
| 1 | **Encounter Distances Table** | B (named table) | 93 | **VISUALLY INSPECTED** — principal governing object |
| 2 | **"Encounter Distance" prose section** | F (detailed prose) | 92 | **VISUALLY INSPECTED** — the three surprise branches and the routing into object 1 |
| 3 | **Game Turn Checklist, step 1** | C (checklist) | 91 | **VISUALLY INSPECTED** — states a wandering-monster appearance distance |
| 4 | **"Wandering Monsters" prose** | F | 91 | **VISUALLY INSPECTED** — restates that distance and names it a detection distance |
| 5 | **"Feet vs. Yards" / Distance section** | F | 87 | **VISUALLY INSPECTED** — the unit convention the table's two unit families depend on |
| 6 | **Movement, Missile, and Spell Ranges checklist** | C | 87 | **VISUALLY INSPECTED** — indoors/outdoors unit rule |
| 7 | **Infravision (Dwarf)** | F | 24 | **VISUALLY INSPECTED** — footnote ** selector; 60′ range |
| 8 | **Infravision (Elf)** | F | 25 | **VISUALLY INSPECTED** — "identical to that of dwarves" |
| 9 | **Halfling Special Abilities list** | F | 26 | **VISUALLY INSPECTED** — supports negative claim N-3 |
| 10 | **Halfling ability sections** | F | 27 | **VISUALLY INSPECTED** — no Infravision subsection; "dimly lit building interiors" recorded |
| 11 | **Encounter Checklist** | C | 93 | **VISUALLY INSPECTED** — contains **no** distance step; surprise is its step 2 |
| 12 | **Chance of Encounter Table** | B | 92 | **VISUALLY INSPECTED** — `ROUTED TO EXP-001` (occurrence, not distance) |
| 13 | **Monster Reactions Table** | B | 93 | **VISUALLY INSPECTED** — `ROUTED TO ENC-003` |
| 14 | **"Encounters" definition prose** | F | 91 | **VISUALLY INSPECTED** — "within visual range"; City → wilderness terrain |
| 15 | **Game Day Checklist** | C | 91 | **VISUALLY INSPECTED** — entry point; carries no distance value |
| 16 | **Dungeon Encounters / Wilderness Encounters prose + Wilderness Encounters Table** | B/F | 95 | **VISUALLY INSPECTED** — explicitly routes *back* to objects 1 and 11 for distance |
| 17 | **Underwater Combat / Naval Combat** | F | 115 | **VISUALLY INSPECTED** — unit-terminology tension recorded as Q-6; no distance mechanic |
| 18 | **Target Cover Table + Attack Roll Modifiers Table** | B | 108 | **VISUALLY INSPECTED** — `ROUTED TO COMBAT-*`; modify attack rolls, not distance |
| 19 | **Blindness / Invisibility (Special Character Conditions)** | F | 150 | **VISUALLY INSPECTED** — condition effects; confirms infravision↔complete-darkness link; no distance mechanic |
| 20 | **Monster description format — Nocturnal, Terrain** | F | 153 | **VISUALLY INSPECTED** — "dungeons are often dark as night"; Terrain line bears on Setting |
| 21 | **Environmental Variations** | F | 215 | **VISUALLY INSPECTED** — `EXCLUDED — monster-adaptation guidance, no distance mechanic` |
| 22 | **Index to Tables and Checklists** | A (index) | 301 | **VISUALLY INSPECTED** — enumerated in §5.1 |
| 23 | **General Index A–H** | A | 302 | **VISUALLY INSPECTED** — enumerated in §5.2 |
| 24 | **General Index H–Sl** | A | 303 | **VISUALLY INSPECTED** — enumerated in §5.2 |
| 25 | **General Index Sl–Z** | A | 304 | **VISUALLY INSPECTED** — enumerated in §5.2; index ends here |
| 26 | **Back cover** | I | 305 | **VISUALLY INSPECTED** — establishes the index's end boundary |
| 27 | Dungeon Encounters Levels 1–10 Tables | B | 94 | **DISPOSITIONED** — `ROUTED TO EXP-008`/`MON-001`: these select *which monster*, and p. 95's own prose sends distance back to object 1. Not visually inspected; recorded here so a reviewer can challenge the routing rather than discover the omission |
| 28 | Wilderness Encounter subtables 1–11 (incl. Castle, City) | B | 96–98 | **DISPOSITIONED** — same routing as row 27; the table at object 1 has no City row and p. 91 states City is treated as wilderness terrain. Not visually inspected |
| 29 | Evasion Checklist / Evasion Table / Ship Evasion Table | B/C | 99–100 | **ROUTED TO ENC-005** — Stage A accepted 2026-09-29; entered *after* contact, consumes distance rather than setting it |
| 30 | Combat Sequence Checklist | C | 102 | **ROUTED TO COMBAT-006** |
| 31 | Morale Scores Table | B | 103 | **ROUTED TO ENC-004** |
| 32 | Terrain Effects on Movement / Traveling Rates by Terrain / Water Movement Modification Tables | B | 88, 90 | **EXCLUDED — per-day travel rates; `EXP-003`/`CHAR-005` territory, no encounter-distance term** |
| 33 | Starvation Table | B | 150 | **EXCLUDED — unrelated; no Rule ID owns starvation causation (`INVENTORY.md` `EXP-006` row)** |

**Manifest closure:** every row above is dispositioned. Rows 27 and 28 are dispositioned
**without visual inspection**, by an explicit printed routing (p. 95) rather than by
assumption; they are named here, and in §15, precisely so that the disposition is
auditable and challengeable rather than silent.

## 5. Index Enumeration

### 5.1 Tables / Checklists Index

| Entry | Page | Disposition |
|---|---|---|
| **Encounter Distances Table** | 93 | **GOVERNING — principal object** |
| Chance of Encounter Table | 92 | `ROUTED TO EXP-001` — occurrence |
| **Encounter Checklist** | 93 | **GOVERNING context** — contains no distance step |
| **Game Turn Checklist** | 91 | **GOVERNING** — carries a distance value at step 1 |
| **Game Day Checklist** | 91 | OPENED — entry point, no distance value |
| Monster Reactions Table | 93 | `ROUTED TO ENC-003` |
| Evasion Checklist / Evasion Table | 99 | `ROUTED TO ENC-005` |
| Ship Evasion Table | 100 | `ROUTED TO ENC-005` |
| Castle Reactions Table | 99 | `ROUTED TO ENC-003` |
| Dungeon Encounters Levels 1-10 Tables | 94 | `ROUTED TO EXP-008` / `MON-001` |
| Wilderness Encounters Table (+ 11 subtables) | 95–98 | `ROUTED TO EXP-008` / `MON-001` |
| Encounter Challenge Table / Balancing Encounters Checklist | 101 | `ROUTED TO ENC-007` (`DEC-0008`: OFF by default for V1) |
| **Measurements of Game Time Table** | 87 | OPENED — time units, not distance |
| **Movement, Missile, and Spell Ranges** | 87 | **GOVERNING** — the indoors/outdoors unit rule |
| Character Movement Rates and Encumbrance Table | 88 | `ROUTED TO CHAR-005` |
| Terrain Effects on Movement Table | 88 | `EXCLUDED — per-day travel` |
| Traveling Rates by Terrain Table | 88 | `EXCLUDED — per-day travel` |
| Water Movement Modification Table | 90 | `EXCLUDED — travel rate` |
| Combat Sequence Checklist | 102 | `ROUTED TO COMBAT-006` |
| Morale Scores Table | 103 | `ROUTED TO ENC-004` |
| Target Cover Table | 108 | `ROUTED TO COMBAT-*` |
| Monster Intelligence Table | 214 | `EXCLUDED — unrelated` |
| Sample Skills Table | 82 | `EXCLUDED — no skill selects encounter distance` |
| NPC Reasons for Appearing Checklist | 155 | `EXCLUDED — motive, not distance` |
| Starvation Table | 150 | `EXCLUDED — unrelated` |

### 5.2 General Index

| Entry | Pages | Followed? | Disposition |
|---|---|---|---|
| Encounters | 91–96 | yes | **GOVERNING range** — objects 1–4, 11, 14–16 |
| Distance | 87 | yes | **GOVERNING** — the unit convention; note it does **not** point at 92/93 |
| Surprise | 92, 93 | yes | `ROUTED TO ENC-002` — consumed as external input |
| Infravision | 24, 25 | yes | **GOVERNING** — footnote ** selector |
| Yards | 87 | yes | **GOVERNING** — unit convention |
| Map scales | 87 | yes | OPENED — 10′ graph square; `ROUTED TO EXP-003` |
| Ranges | 87 | yes | **GOVERNING** — indoors/outdoors units |
| Encounter speed | 88, 95, 100, 103 | yes (88, 95) | `ROUTED TO CHAR-005` / `MON-003` — speed, not distance |
| Wandering monster | 93, 261 | yes (93) | `ROUTED TO EXP-001` |
| Wandering monsters check | 91 | yes | `ROUTED TO EXP-001`; its *appearance distance* is object 3 |
| Dungeon encounters | 95 | yes | `ROUTED TO EXP-008` |
| Wilderness encounters | 95, 96 | yes (95) | `ROUTED TO EXP-008`; routes distance back to object 1 |
| Castle encounters | 95, 96 | partly (95) | `ROUTED TO EXP-008` |
| Evasion | 91, 98–100 | yes (91) | `ROUTED TO ENC-005` |
| Pursuit | 98–100 | no | `ROUTED TO ENC-005` |
| Exploration | 91 | yes | OPENED — object 14 |
| Game turn / Game day / Game time | 91, 87 | yes | `ROUTED TO EXP-002` |
| Turns | 87, 91 | yes | `ROUTED TO EXP-002` |
| Feet | 87 | yes | **GOVERNING** — unit convention |
| Movement | 87, 88, 103, 263, 264 | partly (87, 88) | `ROUTED TO EXP-003` / `CHAR-005` |
| Monster — Movement rate | 88 | yes | `ROUTED TO MON-003` |
| Monster — Reactions | 93 | yes | `ROUTED TO ENC-003` |
| Monster — Environmental variations | 215 | yes | `EXCLUDED — no distance mechanic` |
| Nocturnal | 153 | yes | OPENED — "dungeons are often dark as night"; bears on Q-1 |
| Terrain | 119, 153 | yes (153) | OPENED — monster Terrain line bears on the Setting axis |
| Terrain effects on movement | 88 | yes | `EXCLUDED — per-day travel` |
| Blindness | 150, 154 | yes (150) | `ROUTED TO EXP-006` / `CHAR-005` — condition, no distance |
| Invisibility | 150 | yes | `ROUTED TO COMBAT-*` — attack-roll penalty only |
| Special defenses | 24, 25, 27, 154 | yes (24, 25, 27) | OPENED — infravision lives here |
| Underwater combat | 115 | yes | OPENED — unit tension Q-6 |
| Naval combat | 115 | yes | `ROUTED TO ENC-005` ("Evasion at Sea") |
| Swimming | 89 | no | `EXCLUDED — travel, not encounter distance` |
| Cover | 108 | yes | `ROUTED TO COMBAT-*` |
| Initiative | 102 | no | `ROUTED TO COMBAT-006` |
| Morale | 102, 103, 119 | no | `ROUTED TO ENC-004` |
| Lost | 89 | no | `ROUTED TO ENC-005` (`Regain Bearings`) |
| Balancing encounters | 100, 101 | no | `ROUTED TO ENC-007` |
| Skills | 82–85, 92 | yes (92) | **Index imprecision recorded** — p. 92 was read in full and carries no skill material; the "92" locator does not correspond to visible skill content on that page |

### 5.3 Specialist indexes

| Instrument | Entries relevant | Disposition |
|---|---|---|
| Index to Tables and Checklists (p. 301) | 25 entries, enumerated in §5.1 | **DISPOSITIONED** — this is the instrument that names the governing table |
| General Index (pp. 302–304) | 39 entries, enumerated in §5.2 | **DISPOSITIONED** |
| Any further index | none exists between p. 301 and the back cover at p. 305 | **DISPOSITIONED** — boundary visually confirmed |

### 5.4 Enumerated absences

The General Index contains **no entry** for any of the following terms, each of which a
researcher would plausibly use to locate this card's subject. Each absence was established
by reading the alphabetical neighbourhood where the entry would fall, not by a text search:

- **"Encounter distance"** — between `Encounter speed` and `Encounters` (p. 302). Absent.
- **"Visibility"** — between `Variant rules` and `Visitors` (p. 304). Absent.
- **"Light"** — between `Lifeboat` and `Lightship` (p. 303). Absent.
- **"Lantern"** — between `Land travel` and `Languages` (p. 303). Absent.
- **"Darkness"** — between `Dagger` and `Days` (p. 302). Absent.
- **"Ocean"** / **"Sea"** / **"Undersea"** — the O and S neighbourhoods (pp. 303, 304). Absent, although all three are printed *Setting* values in the governing table.

This is itself a material research fact and is carried as negative claim **N-1**: the
General Index cannot reach this card's governing table by the card's own subject name. The
**Index to Tables and Checklists** *can* — it lists `Encounter Distances Table … 93`
directly. The two instruments are therefore not interchangeable for this card, which is
exactly the completeness point `DEC-0012` §9.9 makes.

## 6. Governing Objects

| Object | Page | Type | Why it governs |
|---|---|---|---|
| **Encounter Distances Table** | 93 | table | Produces the distance whenever neither party is surprised, keyed on Setting × Visibility × Encounter |
| **"Encounter Distance" prose** | 92 | prose | States the two surprised-case distances, routes the unsurprised case to the table, and fixes the ordering relative to surprise |
| **Game Turn Checklist step 1** | 91 | checklist | States a wandering-monster appearance distance of `2d6 × 10'` under "normal dungeon conditions" |
| **"Wandering Monsters" prose** | 91 | prose | Restates that `2d6 × 10` value and characterises it as the distance at which monsters are *detected* |
| **"Feet vs. Yards" + Movement, Missile, and Spell Ranges** | 87 | prose + checklist | Supplies the indoor/outdoor unit rule the table's `10'` and `10 yards` families rest on |
| **Infravision** | 24, 25 | prose | Footnote ** makes infravision a selector for the Dim-light row; supplies its 60′ range and its suppression by light |
| **"Encounters" definition** | 91 | prose | "Within visual range"; and City is treated as wilderness terrain, which supplies the Setting the table omits |

> A **principal** governing object is named above (the Encounter Distances Table). *The*
> single governing object is deliberately **not** named: objects 3 and 4 state a distance
> that the table does not obviously produce, and until Q-1/Q-2 are adjudicated it cannot be
> established that the table alone governs (§9.8).

## 7. Visual Inspection Record

```text
COVERAGE-LEDGER
EVIDENCE-PAGES:  24, 25, 26, 27, 87, 91, 92, 93, 95, 108, 115, 150, 153, 215, 301, 302, 303, 304, 305
IMAGE-VERIFIED:  24, 25, 26, 27, 87, 91, 92, 93, 95, 108, 115, 150, 153, 215, 301, 302, 303, 304, 305
LOCATOR-ONLY:    none
ACCESS-BLOCKED:  none
```

| Page | Rendering confirmed | Note |
|---|---|---|
| 92 | full page, 1400px wide | Both columns legible; folio "92" visible; Encounter Distance section complete |
| 93 | full page, 1400px wide | **All 13 table rows, 4 column headers and 3 footnotes legible**; folio "93" visible |
| 87 | full page, 1400px wide | "Feet vs. Yards", Distance box and Measurements of Game Time Table all legible |
| 91 | full page, 1400px wide | Both checklists and the Wandering Monsters prose legible |
| 24, 25, 26, 27 | full page, 1400px wide | Infravision paragraphs and the halfling ability list legible |
| 95, 108, 115, 150, 153, 215 | full page, 1400px wide | Legible; each dispositioned in §4 |
| 301, 302, 303, 304 | full page, 1400px wide | Index columns legible entry by entry |
| 305 | full page, 1400px wide | Back cover — establishes that the index ends at p. 304 |

No page in this packet was read by OCR, and no finding rests on a partially rendered
image. Each page above was confirmed by reading its body text, not by its HTTP status.

## 8. Cross-Reference Ledger

| From | Explicit reference | Followed to | Result |
|---|---|---|---|
| p. 91 step 1 | "(see the 'Encounter Distance' section, below, for more information)" | p. 92 | **Followed.** Establishes that RC itself links the Game Turn Checklist's `2d6 × 10'` to the Encounter Distance section — the basis of Q-2 |
| p. 91 | "switch to the Encounter Checklist (on page 93)" | p. 93 | **Followed.** The Encounter Checklist has six steps and **none** of them is a distance step |
| p. 92 | "take a look at the Encounter Distances Table" | p. 93 | **Followed.** The table is the unsurprised-case procedure |
| p. 92 | "though this may differ with some monsters; see Chapter 14" | pp. 152–215 | **Followed to ownership only.** This qualifies *surprise*, not distance — `ROUTED TO ENC-002`; per-monster variation is `MON-*`'s |
| p. 93 footnote ** | "full darkness with infravision used" | pp. 24, 25 | **Followed.** Infravision is 60′, suppressed by normal and magical light; elf identical to dwarf |
| p. 95 | "Play out the encounter as described under 'Encounters' on page 91, using the visibility, distance, and surprise factors" | p. 91 | **Followed.** Confirms RC's own triple and that wilderness encounters use the same machinery |
| p. 95 | "Consult the Encounter Checklist and the Encounter Distances Table for other factors regarding encounters" | pp. 93 | **Followed.** Wilderness encounters route *back* to the same table — there is no separate wilderness distance procedure |
| p. 91 | "'City' is treated just like any other wilderness terrain" | p. 93 table | **Followed.** Supplies the Setting for City encounters, which the table does not list |
| p. 115 | "Read the rules for 'Evasion at Sea' in Chapter 7" | pp. 99–100 | Followed to ownership only — `ROUTED TO ENC-005` |
| p. 153 | monster `Terrain` line definitions incl. "Ocean … surface and underwater encounters" | p. 93 table | **Followed.** Monster Terrain supplies the table's Setting axis for wandering encounters |
| p. 150 | "a character *without infravision* may find himself in an area of complete darkness" | p. 24 | **Followed.** Independent confirmation of the infravision↔complete-darkness link the ** footnote assumes |

**Whole-source search terms used** (§9): the enumeration was index-driven and
structure-driven, not text-search-driven. The terms sought *as index entries*, each
recorded present or absent in §5.2/§5.4, were: `encounter distance`, `distance`,
`encounters`, `encounter speed`, `surprise`, `visibility`, `light`, `lantern`, `darkness`,
`infravision`, `yards`, `feet`, `ranges`, `map scales`, `terrain`, `nocturnal`,
`blindness`, `invisibility`, `cover`, `ocean`, `sea`, `undersea`, `underwater combat`,
`swimming`, `wandering monster`, `wilderness encounters`, `dungeon encounters`, `castle
encounters`, `evasion`, `pursuit`, `movement`, `initiative`, `morale`, `lost`, `balancing
encounters`, `skills`, `special defenses`. No finding in this packet rests on a text
search, and no absence is asserted from a failed search alone (§10.4).

## 9. Repository-Fact Verification

| Project claim | Artifact inspected | Identifier / section | Verdict |
|---|---|---|---|
| R-1: `ENC-001` is registered as "Encounter Distance", RC Core, dependencies `—`, status `Unresearched` | `docs/rules/INVENTORY.md` | row 116 | **VERIFIED** |
| R-2: `ENC-002` (Surprise) is `Unresearched` and itself depends on `CHAR-010` | `docs/rules/INVENTORY.md` | row 117 | **VERIFIED** |
| R-3: No `ENC-001` Rule Card, evidence packet or source module exists | working tree | recursive search for `*ENC-001*` / `*enc_001*`; `docs/rules/` has no `encounters/` directory | **VERIFIED** — none exists |
| R-4: `EXP-006` is landed and exposes mundane light state | `src/rules/exploration/light_and_exploration_resources.py` | `__all__` (13 names) | **VERIFIED** |
| R-5: `EXP-006` does **not** own world visibility | same file | `MundaneLightContribution` docstring, l. 367–377 | **VERIFIED** — the type is explicitly "**Not** a statement about the world" and deliberately not named `Visibility` or `WorldLight` |
| R-6: `ENC-001` is not grandfathered from the evidence linter | `scripts/lint_evidence.py` | `GRANDFATHERED` frozenset, l. 84–99 | **VERIFIED** — twelve entries, no `ENC-001`; comment states the list is closed |
| R-7: `ENC-001` is dependency-unblocked in the current cluster boundary | `docs/rules/clusters/CLUSTER-004-BOUNDARY-CORRECTION.md` | l. 229, "the 16 unblocked cards" | **VERIFIED** |
| R-8: `ENC-001` is one of `ENC-005`'s six Stage-B blocking providers | `docs/rules/evidence/ENC-005-evidence-remediated.md` | §7.1 l. 550; l. 564 | **VERIFIED** |
| R-9: `ENC-005` Stage A recorded encounter distance as "light-keyed" | same | N-4a, l. 147 | **CORRECTED — was "light-keyed"**. The table is keyed on **Setting × Visibility × Encounter**, not on light alone; p. 92 names the selector as "the type of terrain (dungeon, wilderness, ocean/sea, or underwater)". `ENC-005`'s note is a locator, and this packet does not rely on it |
| R-10: `EXP-001` owns the wandering-monster *check* | `docs/rules/INVENTORY.md` | row 101 — `VERIFIED`, implemented | **VERIFIED** |
| R-11: `DEC-0012` requires exactly one human-selected pilot with four fixed criteria | `docs/decisions/DEC-0012-stage-a-evidence-integrity-gates.md` | item 15, l. 302–315 | **VERIFIED** |
| R-12: No Rule ID currently owns a world *visibility category* | `docs/rules/INVENTORY.md` (all rows), plus R-5 | no row claims visibility/illumination state | **VERIFIED** — recorded as an ownership gap in §12, not invented |

## 10. Evidence Map

| # | Fact | Object | Provenance | Confidence |
|---|---|---|---|---|
| E-1 | The Encounter Distances Table has four columns — `Setting`, `Visibility`, `Encounter`, `Distance` — 13 data rows and 3 footnotes | p. 93, table | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-2 | Dungeon rows: Very good light `4d6x 10'`; Dim light `2d6x 10'`; No light `1d4x 10'` | p. 93 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-3 | Wilderness rows: Clear daylight `4d6 x 10 yards`; Dim light `2d6 x 10 yards`; No light `1d4 x 10 yards` | p. 93 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-4 | Ocean/sea rows split by `Encounter` = Ship vs Monster: Clear daylight `300 yards` / `4d6 x 10 yards`; Dim light `120 yards` / `2d6 X 10 yards`; No light `40 yards` / `1d4 x 10 yards` | p. 93 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-5 | Undersea row: `Any light`, DM's choice, `1d6 x 10 yards` — the only row whose Visibility value is "Any light" | p. 93 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-6 | Footnote `*` extends Dungeon to "Or other indoor setting" | p. 93 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-7 | Footnote `**` extends Dim light to "Or full darkness with infravision used" | p. 93 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-8 | Footnote `t` extends No light to "Or very poor visibility (heavy snow or fog, sandstorm, etc.)" | p. 93 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-9 | Both parties surprised → encounter distance is `1d4 x 10'` (or yards if outdoors) | p. 92 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-10 | One party surprised → the unsurprised party notices at the rolled `1d4 X 10'` distance; the surprised party does not notice until they reach **half** that distance | p. 92 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-11 | Neither surprised → consult the Encounter Distances Table, selected by "the type of terrain (dungeon, wilderness, ocean/sea, or underwater)" | p. 92 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-12 | Ordering is fixed: the DM determines that an encounter occurs **and** the relative conditions of surprise **before** deciding how far apart the parties are | p. 92 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-13 | Indoors the basic unit of distance is the **foot**; outdoors it is the **yard**; one yard equals three feet | p. 87 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-14 | RC's own stated reason for the outdoor difference is "more open terrain and better lighting" | p. 87 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-15 | Wandering monsters "appear `2d6 x 10'` away in a direction of the DM's choice" under **normal dungeon conditions** | p. 91, Game Turn Checklist step 1 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-16 | The same value is restated as a procedure: roll `2d6`, multiply by 10, "the result is the distance, in feet, at which the monsters are detected" | p. 91, Wandering Monsters prose | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-17 | Step 1 cross-references the Encounter Distance section "for more information" | p. 91 | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| E-18 | An encounter occurs when groups "come within **visual range** of one another and at least one group becomes aware of the other" | p. 91 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-19 | "City" is treated just like any other wilderness terrain | p. 91 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-20 | Infravision sees 60′ in the dark and "does not work in the presence of normal and magical light" | p. 24 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-21 | Elves have infravision "identical to that of dwarves" | p. 25 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-22 | The halfling's enumerated Special Abilities list contains no infravision; it does include hiding "in dimly lit building interiors" | pp. 26, 27 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-23 | A character without infravision "may find himself in an area of complete darkness" | p. 150 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-24 | The Encounter Checklist's six steps are Game Time, Surprise, Initiative, Reactions, Results, Encounter Ends — no step determines distance | p. 93 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-25 | Wilderness encounters are played out "using the visibility, distance, and surprise factors" and route to the Encounter Checklist and Encounter Distances Table | p. 95 | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| E-26 | "Dungeons are often dark as night," stated as part of the Nocturnal creature definition | p. 153 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-27 | Undersea missile ranges are read "in feet at all times" | p. 115 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-28 | Monster Terrain values include Ocean ("surface and underwater encounters"), Cavern, Settled, Open, River/Lake, Woods, Swamp, Desert, Mountain, Ruins, Cold/Arctic, Lost World | p. 153 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-29 | Monster Environmental Variations is DM adaptation guidance and states no distance mechanic | p. 215 | Unresolved by RC (no mechanic present) | DIRECT PRIMARY TEXT |
| E-30 | Cover and "Attacker can't see target" adjust **attack rolls**, not encounter distance | p. 108 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-31 | The Index to Tables and Checklists lists `Encounter Distances Table … 93` | p. 301 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-32 | The General Index lists `Distance … 87`, `Encounters … 91-96`, `Surprise … 92, 93`, `Infravision … 24, 25` | pp. 302–304 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-33 | The General Index ends on p. 304; p. 305 is the back cover | pp. 304, 305 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-34 | `ENC-001` owns no mechanic for determining *which* visibility category obtains | pp. 92, 93 | Unresolved by RC | NOT YET ESTABLISHED |

**Verbatim transcriptions** of governing text, each attributed to its page:

```text
p. 93 — Encounter Distances Table (complete)

Setting        Visibility          Encounter      Distance
Dungeon*       Very good light     DM's choice    4d6x 10'
Dungeon*       Dim light**         DM's choice    2d6x 10'
Dungeon*       No lightt           DM's choice    1d4x 10'
Wilderness     Clear daylight      DM's choice    4d6 x 10 yards
Wilderness     Dim light**         DM's choice    2d6 x 10 yards
Wilderness     No lightt           DM's choice    1d4 x 10 yards
Ocean/sea      Clear daylight      Ship           300 yards
Ocean/sea      Clear daylight      Monster        4d6 x 10 yards
Ocean/sea      Dim light**         Ship           120 yards
Ocean/sea      Dim light**         Monster        2d6 X 10 yards
Ocean/sea      No lightt           Ship           40 yards
Ocean/sea      No lightt           Monster        1d4 x 10 yards
Undersea       Any light           DM's choice    1d6 x 10 yards

  *  Or other indoor setting.
 **  Or full darkness with infravision used.
  t  Or very poor visibility (heavy snow or fog, sandstorm, etc.).
```

```text
p. 92 — "Encounter Distance" (complete section)

"Once the Dungeon Master has determined that an encounter will take place and
has determined the relative conditions of surprise for the two groups, he or
she can decide how far apart the two parties are when the encounter takes
place.
    When both parties are surprised, the encounter distance is 1d4 x 10' (or
yards if outdoors).
    When one party is surprised, the unsurprised party notices the surprised
party at the 1d4 X 10' (or yards) distance rolled; the surprised party won't
notice the unsurprised party until they reach half that distance.
    When neither party is surprised, take a look at the Encounter Distances
Table. When the type of terrain (dungeon, wilderness, ocean/sea, or
underwater) is known, the DM can find out how far apart the groups are when
the encounter takes place."
```

```text
p. 91 — Game Turn Checklist, step 1

"1. Wandering Monsters: If the wandering monsters check at the end of the
previous turn was positive, the monsters arrive now. Under normal dungeon
conditions, they appear 2d6 x 10' away in a direction of the DM's choice (see
the "Encounter Distance" section, below, for more information)."
```

```text
p. 91 — "Wandering Monsters"

"When a DM's roll indicates that wandering monsters will appear, they appear
the following turn. The DM rolls 2d6 and multiplies this number by 10; the
result is the distance, in feet, at which the monsters are detected.
    This is the distance at which the DM first begins keeping track of them
and the distance at which both sides first have a chance to notice one
another."
```

```text
p. 87 — "Feet vs. Yards"

"In dungeons and other indoor settings, the basic unit of distance measurement
is the foot. Missile and spell ranges are measured in feet; a character's
normal speed is expressed in feet. In wildernesses, open fields, open city
streets, and other outdoor settings, the basic unit of distance measurement is
the yard. (One yard equals three feet.) In outdoor settings, it is easier to
move quickly due to more open terrain and better lighting."
```

```text
p. 24 — "Infravision"

"Infravision is the ability to see heat (and the lack of heat). Dwarves have
infravision in addition to normal sight and can see 60' in the dark.
Infravision does not work in the presence of normal and magical light."
```

## 11. Negative Claim Ledger

```text
NEGATIVE-CLAIM-RECORD
CLAIM:                           The RC General Index has no entry for "Encounter
                                 distance", "Visibility", "Light", "Lantern",
                                 "Darkness", "Ocean", "Sea" or "Undersea".
SCOPE SEARCHED:                  General Index, pp. 302-304 (its full extent; p. 305
                                 is the back cover)
STRUCTURAL INSTRUMENTS CHECKED:  Appendix 4 heading; Index to Tables and Checklists
                                 (p. 301); General Index column structure
INDEXES CHECKED:                 General Index entry by entry across the alphabetical
                                 neighbourhood each absent term would occupy
SEARCH TERMS USED:               encounter distance, visibility, light, lantern,
                                 darkness, ocean, sea, undersea -- each sought as an
                                 index entry, by reading its neighbours, not by text
                                 search
CROSS-REFERENCES FOLLOWED:       Encounters 91-96; Distance 87; Surprise 92, 93;
                                 Infravision 24, 25
VISUAL PAGES INSPECTED:          301, 302, 303, 304, 305
FALSIFICATION ATTEMPT:           Sought the same terms in the Index to Tables and
                                 Checklists, where "Encounter Distances Table ... 93"
                                 IS present -- so the subject is indexed as a TABLE
                                 but not as a SUBJECT. The claim is therefore
                                 narrowed to the General Index and does not assert
                                 that the source fails to index the table at all.
CONFIDENCE:                      DIRECT PRIMARY TEXT
```

```text
NEGATIVE-CLAIM-RECORD
CLAIM:                           The Encounter Checklist (p. 93) contains no step that
                                 determines encounter distance.
SCOPE SEARCHED:                  p. 93 Encounter Checklist, all six numbered steps and
                                 their sub-steps, read complete
STRUCTURAL INSTRUMENTS CHECKED:  Index to Tables and Checklists entry "Encounter
                                 Checklist ... 93"; the checklist box itself
INDEXES CHECKED:                 Tables/Checklists Index; General Index "Encounters
                                 91-96"
SEARCH TERMS USED:               distance, encounter distance -- sought within the
                                 checklist text itself
CROSS-REFERENCES FOLLOWED:       p. 91 -> p. 93 ("switch to the Encounter Checklist");
                                 p. 95 -> p. 93
VISUAL PAGES INSPECTED:          91, 93, 95
FALSIFICATION ATTEMPT:           Looked specifically for a distance step hidden inside
                                 step 5 (Results) and step 1 (Game Time), where one
                                 could plausibly sit. Step 5's sub-steps cover traps,
                                 conversation, running away and combat; none sets a
                                 distance. Distance is set in the p. 92 prose BEFORE
                                 the checklist is entered, consistent with E-12.
CONFIDENCE:                      DIRECT PRIMARY TEXT
```

```text
NEGATIVE-CLAIM-RECORD
CLAIM:                           Halflings have no infravision; among PC races only
                                 dwarves and elves do.
SCOPE SEARCHED:                  Ch. 2 character-class entries for dwarf (pp. 23-25),
                                 elf (pp. 25-26) and halfling (pp. 26-27)
STRUCTURAL INSTRUMENTS CHECKED:  The per-class "Special Abilities" enumerated list and
                                 the per-class ability subsections
INDEXES CHECKED:                 General Index "Infravision ... 24, 25" -- two pages
                                 only, being the dwarf and elf entries
SEARCH TERMS USED:               infravision -- sought as an index entry and as a
                                 subsection heading in each class entry
CROSS-REFERENCES FOLLOWED:       p. 25 elf -> p. 24 dwarf ("identical to that of
                                 dwarves"); p. 150 -> p. 24
VISUAL PAGES INSPECTED:          24, 25, 26, 27, 150, 303
FALSIFICATION ATTEMPT:           Read the halfling's complete enumerated Special
                                 Abilities list on p. 26 looking for infravision, and
                                 read p. 27's ability subsections looking for an
                                 Infravision heading of the kind dwarf and elf each
                                 carry. Neither contains one. The halfling instead
                                 hides "in dimly lit building interiors", which is a
                                 different mechanic.
CONFIDENCE:                      DIRECT PRIMARY TEXT
```

```text
NEGATIVE-CLAIM-RECORD
CLAIM:                           RC states no procedure for determining WHICH
                                 visibility category (Very good light / Dim light /
                                 No light) obtains at a given moment.
SCOPE SEARCHED:                  Ch. 7 pp. 91-96 complete; the three table footnotes;
                                 Ch. 6 p. 87; Ch. 13 p. 150; Ch. 14 p. 153
STRUCTURAL INSTRUMENTS CHECKED:  Index to Tables and Checklists, read for any
                                 visibility, light or illumination table -- none is
                                 listed; General Index neighbourhoods for "Light",
                                 "Visibility", "Darkness" -- all absent (N-1)
INDEXES CHECKED:                 both instruments, pp. 301-304
SEARCH TERMS USED:               visibility, light, dim light, very good light, no
                                 light, darkness, illumination
CROSS-REFERENCES FOLLOWED:       p. 93 footnotes ** and t -> pp. 24, 25; p. 92 -> p. 93
VISUAL PAGES INSPECTED:          24, 25, 87, 91, 92, 93, 95, 150, 153, 301, 302, 303, 304
FALSIFICATION ATTEMPT:           Sought a definition in the three places it would most
                                 plausibly sit: the table's own footnotes (which
                                 EXTEND categories but never define them), the
                                 equipment light sources (EXP-006's accepted evidence
                                 establishes a 30' radius, which is a radius and not a
                                 category), and the Nocturnal definition on p. 153
                                 ("dungeons are often dark as night" -- a
                                 characterisation, with "often", not a rule). None
                                 supplies a selector.
CONFIDENCE:                      DIRECT PRIMARY TEXT
```

## 12. Ownership and Dependency Routing

| Mechanic | Owner | Status | Evidence for the routing |
|---|---|---|---|
| Encounter-distance determination | **`ENC-001`** (this card) | UNRESEARCHED → this packet | R-1 |
| Surprise determination (the `1d6`, the 1–2 result, per-monster variation) | `ENC-002` | UNRESEARCHED | R-2; p. 92 and p. 93 step 2 recorded as **input**, not claimed |
| **World visibility category** (which of Very good light / Dim light / No light obtains) | **NO RULE ID EXISTS** | — | R-12, R-5, negative claim N-4. `EXP-006` owns *mundane light contribution* and its own docstring states it is "**Not** a statement about the world"; no inventory row claims visibility state. **Recorded as a gap, not invented.** |
| Mundane light sources, radius, depletion | `EXP-006` | **LANDED** (approved 2026-10-01, implemented, merged) | R-4 |
| Whether an encounter occurs at all | `EXP-001` (dungeon wandering check) / Chance of Encounter Table | `VERIFIED`, implemented | R-10 |
| Evasion and pursuit after contact | `ENC-005` | Stage A accepted; Stage B deferred | R-8 |
| Monster movement rate / relative speed | `MON-003` | UNRESEARCHED | p. 93 table does not use speed; routed for `ENC-005` only |
| Monster reaction after contact | `ENC-003` | UNRESEARCHED | p. 93 Monster Reactions Table |
| Which monster is encountered | `EXP-008` / `MON-001` | UNRESEARCHED | pp. 94–98 |
| Feet/yards unit convention | **RC Ch. 6 p. 87 — no Rule ID claims it as its own responsibility** | — | `EXP-003` (APPROVED) states feet-indoors for *movement*; the general convention at p. 87 is consumed by this card. Recorded as a **potential completion question**, not assigned |
| Attack-roll effects of cover and not seeing a target | `COMBAT-*` | UNRESEARCHED | E-30 |
| Blindness as a character condition | `EXP-006` / `CHAR-005` routing already established | — | E-23; no distance mechanic |

## 13. Falsification Pass

```text
FALSIFICATION-RECORD
CONCLUSION:     The Encounter Distances Table is keyed on Setting AND Visibility
                (and, at sea, on Encounter type) -- not on light alone.
WOULD FALSIFY:  A table whose only discriminating column is Visibility, or prose
                naming light as the sole selector.
SOUGHT:         The table itself at p. 93, read column by column and row by row;
                and the p. 92 prose that routes into it.
RESULT:         Four columns confirmed. p. 92 names the selector as "the type of
                terrain (dungeon, wilderness, ocean/sea, or underwater)". Both
                axes are required: Dungeon/Dim light and Wilderness/Dim light give
                different units and different values.
DISPOSITION:    CONFIRMED -- and it CORRECTS the inherited ENC-005 note (R-9).
```

```text
FALSIFICATION-RECORD
CONCLUSION:     "Normal dungeon conditions" (p. 91) is NOT established by RC to mean
                the table's "Dim light" row, despite both yielding 2d6 x 10'.
WOULD FALSIFY:  Any RC text equating the two, or defining "normal dungeon
                conditions" in visibility terms.
SOUGHT:         p. 91 in full; p. 92-93 in full; the table's three footnotes;
                p. 153's Nocturnal definition; p. 87's lighting remark; the
                General Index neighbourhoods for Light/Visibility/Darkness.
RESULT:         No equating text found. p. 153 says "dungeons are OFTEN dark as
                night" -- a hedged characterisation inside a creature-activity
                definition, not a visibility rule. p. 87 attributes better
                lighting to the OUTDOORS, which if anything cuts against reading
                the dungeon default as "Very good light", but establishes nothing
                about which dungeon row applies.
DISPOSITION:    CONFIRMED as an open ambiguity -- recorded as Q-1, NOT adjudicated.
                This is the EXP-006 lesson in live form: the numeric coincidence is
                real and is exactly what would tempt a silent identification.
```

```text
FALSIFICATION-RECORD
CONCLUSION:     There is no separate wilderness encounter-distance procedure.
WOULD FALSIFY:  A distance rule inside the Wilderness Encounters material, or a
                second distances table keyed to outdoor terrain.
SOUGHT:         p. 95 Wilderness Encounters prose and box; the Tables/Checklists
                Index read for any second distances table; the General Index
                entries "Wilderness encounters 95, 96" and "Castle encounters".
RESULT:         p. 95 explicitly sends the reader back: "Consult the Encounter
                Checklist and the Encounter Distances Table". The Tables Index
                lists exactly one Encounter Distances Table. The single table
                carries the Wilderness rows itself.
DISPOSITION:    CONFIRMED.
```

```text
FALSIFICATION-RECORD
CONCLUSION:     ENC-001 does not depend on ENC-002's IMPLEMENTATION; it consumes
                authoritative surprise STATE supplied at its boundary.
WOULD FALSIFY:  RC text requiring the distance procedure to itself roll or derive
                surprise, or a repository row making ENC-002 a hard dependency.
SOUGHT:         p. 92's ordering sentence; p. 93 Encounter Checklist step 2;
                INVENTORY.md rows 116 and 117.
RESULT:         p. 92 fixes the order -- surprise is determined BEFORE distance
                (E-12) -- so surprise enters as a settled input. INVENTORY row 116
                records no dependency, which is consistent with consuming state
                rather than owning the mechanic. The two are reconcilable, and the
                inventory row needs no correction.
DISPOSITION:    CONFIRMED.
```

```text
FALSIFICATION-RECORD
CONCLUSION:     No Rule ID currently owns a world visibility category.
WOULD FALSIFY:  Any inventory row, approved card or landed module claiming
                illumination/visibility world state.
SOUGHT:         INVENTORY.md read for a visibility/illumination owner;
                EXP-006's module surface and the MundaneLightContribution
                docstring; the EXP-006 inventory row's routing list.
RESULT:         EXP-006's own docstring forecloses it in terms -- the type is
                deliberately NOT named Visibility or WorldLight and is "Not a
                statement about the world". No other row claims it.
DISPOSITION:    CONFIRMED -- recorded as a gap in §12 per AGENTS.md §3.
```

```text
FALSIFICATION-RECORD
CONCLUSION:     Rows 27-28 of the Coverage Manifest (pp. 94, 96-98) carry no
                encounter-distance mechanic.
WOULD FALSIFY:  A distance value printed inside the dungeon or wilderness
                encounter subtables.
SOUGHT:         p. 95's prose governing BOTH table families, which states what the
                reader does after rolling on them; the Tables/Checklists Index
                entries for every subtable.
RESULT:         p. 95 routes distance to the Encounter Distances Table for the
                wilderness family and to "Encounters" for the dungeon family.
                The subtables are monster-selection instruments.
DISPOSITION:    QUALIFIED -- the routing is RC-explicit, but pp. 94 and 96-98 were
                NOT visually inspected. This is declared in §4 and §15 rather than
                presented as inspected coverage, and is the single most likely
                place for independent review to find a gap.
```

## 14. Open-Question Closure

| # | Open question | Object implicated | Disposition |
|---|---|---|---|
| 1 | Does "normal dungeon conditions" (p. 91) denote the table's Dim-light row? Both produce `2d6 × 10'`, and RC never equates them | pp. 91, 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 2 | Is the p. 91 wandering-monster distance an *instance* of the p. 93 table, or an independent default that bypasses the surprise branches? Step 1 cross-references the Encounter Distance section, yet states a flat value | pp. 91, 92, 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 3 | Is the Dungeon row's "Very good light" the same condition as the Wilderness/Ocean rows' "Clear daylight"? RC prints two different labels and never equates them | p. 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 4 | Whose infravision satisfies footnote `**` — any one party member's, every member's, or the noticing side's? | p. 93 footnote | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 5 | Infravision reaches 60′, but the Dim-light dungeon row can roll `2d6 × 10'` = 20′–120′. RC does not say what happens when the rolled distance exceeds infravision's range | pp. 24, 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 6 | The Undersea row gives `1d6 × 10 yards`, while p. 115 says undersea *ranges* are read "in feet at all times". Same unit family, different instruction — possibly distinct concepts (encounter distance vs missile range) | pp. 93, 115 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 7 | Which visibility category obtains at a given moment — no RC selector exists and no Rule ID owns the world state | pp. 92, 93 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 8 | Does the table apply at all when a party is surprised? | pp. 92, 93 | RESOLVED BY SOURCE INSPECTION |
| 9 | Is encounter distance determined before or after surprise? | p. 92 | RESOLVED BY SOURCE INSPECTION |
| 10 | Which Setting row governs a City encounter, given the table has no City row? | pp. 91, 93 | RESOLVED BY SOURCE INSPECTION |
| 11 | Is there a separate wilderness distance procedure? | p. 95 | RESOLVED BY SOURCE INSPECTION |
| 12 | Does the Encounter Checklist determine distance? | p. 93 | RESOLVED BY SOURCE INSPECTION |
| 13 | Does any monster-specific rule vary encounter *distance* (as opposed to surprise)? | pp. 92, 153, 215 | CONFIRMED OUT OF SCOPE |
| 14 | Do cover, blindness or invisibility modify encounter distance? | pp. 108, 150 | CONFIRMED OUT OF SCOPE |

**On Q-1 and Q-2 together.** These are recorded as ambiguities, not as a printed
contradiction, because p. 91 hedges with "under normal dungeon conditions" and points the
reader onward to the Encounter Distance section rather than contradicting it. A reviewer
who judges them a printed internal conflict rather than an ambiguity should say so: that
classification carries the protocol's internal-conflict hard stop, and this packet's
recommendation would have to be revisited rather than reconciled by the researcher.

## 15. Primary-Source Coverage Checklist

- **Relevant structural units inspected:** Ch. 2 (character-class infravision entries),
  Ch. 6 (Distance / Feet vs. Yards), Ch. 7 pp. 91–93 and 95, Ch. 8 pp. 108 and 115,
  Ch. 13 p. 150, Ch. 14 pp. 153 and 215, Appendix 4 pp. 301–304, end boundary p. 305.
- **Tables / Checklists Index entries dispositioned:** 25 (ledger: §5.1).
- **General Index entries dispositioned:** 39 present entries, plus 8 enumerated absences
  (ledgers: §5.2, §5.4).
- **Specialist indexes dispositioned:** both instruments the source carries; no third
  index exists between p. 301 and the back cover.
- **Named tables inspected:** Encounter Distances Table (p. 93), Chance of Encounter Table
  (p. 92), Monster Reactions Table (p. 93), Wilderness Encounters Table (p. 95),
  Measurements of Game Time Table (p. 87), Target Cover Table and Attack Roll Modifiers
  Table (p. 108), Starvation Table (p. 150), Ram Attacks Table (p. 115).
- **Structured entity entries inspected as complete units (§9.7):** the Encounter
  Distances Table with all 13 rows and all 3 footnotes; the Encounter Checklist with all
  six steps and sub-steps; the Game Turn Checklist and Game Day Checklist complete; the
  dwarf, elf and halfling class entries' ability sections.
- **Cross-references followed:** 11 (ledger: §8).
- **Visual verification completed for:** 19 pages, each listed in §7's ledger.
- **Deliberately excluded objects, each with its reason:** Coverage Manifest rows 29–33
  (routed to `ENC-005`, `COMBAT-006`, `ENC-004`, `EXP-003`/`CHAR-005`, and an unowned
  starvation causation respectively).
- **Enumerated but NOT visually inspected:** pp. 94 and 96–98 (Coverage Manifest rows
  27–28), dispositioned by p. 95's explicit printed routing. This packet does not describe
  its coverage as complete over those pages, and §13's sixth record marks the disposition
  `QUALIFIED` for exactly that reason.

## 16. Independent Review Status

```text
ORIGINAL RESEARCHER OUTPUT:  PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
INDEPENDENT REVIEW:          NOT YET PERFORMED
HUMAN EVIDENCE REVIEW:       NOT GIVEN
```

**Research-Completion Gate (§11.1) — each line confirmed, not assumed:**

- [x] every Coverage Manifest row dispositioned — 33 rows, §4
- [x] no unresolved visual-access blocker — `ACCESS-BLOCKED: none`, §7
- [x] every material negative claim has a Negative Claim Record — 4 records, §11
- [x] every repository fact verified against the repository this pass — 12 rows, §9
- [x] pre-review self-falsification pass complete — 6 records, §13
- [x] open questions explicitly listed and classified — 14 rows, §14
- [x] required §6 and §10.2 vocabulary used verbatim
- [x] `scripts/lint_evidence.py` passes — invocation recorded in the completion record

The original researcher does not certify this packet (§10.1.2). Independent completeness
review is requested.
