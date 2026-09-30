# `TEST-900` — Linter Fixture — Stage-A Evidence

> **NOT EVIDENCE.** A test fixture for `scripts/lint_evidence.py`. `TEST-900` is a
> fictional Rule ID. No statement below was researched, and none may be cited as a
> source fact or a repository fact. See `tests/tooling/fixtures/README.md`.
>
> Its purpose is to prove that a **conforming post-`DEC-0012` packet passes** — a
> claim the repository itself cannot demonstrate while every real packet is
> grandfathered.

```text
PACKET-STATUS
RULE-ID:              TEST-900
PASS:                 1
SELF-FALSIFICATION:   COMPLETE
REPOSITORY-FACT-PASS: COMPLETE
INDEPENDENT-REVIEW:   PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
RECOMMENDATION:       EVIDENCE READY FOR HUMAN REVIEW
```

## 1. Research-Start Gate

| Item | Established |
|---|---|
| Exact card scope | fixture scope, established from the fixture register |
| Known ownership seams | `TEST-901` (downstream consumer) |
| Authoritative primary source | fixture source, first printing |
| Required structural + index instruments | TOC, Tables Index, General Index |
| Current repository dependencies | none; fixture is standalone |
| Primary-source visual-access confirmed | yes, both governing pages render |

**Scope boundary this packet will not cross:** consumption of the state this card
produces, which belongs to `TEST-901`.

## 2. Primary Source Accessed

| Source | Access method | Role |
|---|---|---|
| Fixture source, 1st printing | page images | authoritative |
| Fixture source OCR | full text | locator only |

**Access limitations encountered, including where a workaround succeeded:** None
encountered.

## 3. Source Structure

| Structural unit | Pages | Could govern this card? |
|---|---|---|
| Ch. 1 — Fixture Mechanics | 10–12 | yes — carries both governing objects |
| Ch. 2 — Unrelated Matter | 13–20 | no — no resource or duration mechanic |

## 4. Coverage Manifest

| # | Object | Class (§9.1 A–I) | Page | Disposition |
|---|---|---|---|---|
| 1 | Fixture Duration Table | B | 10 | VISUALLY INSPECTED |
| 2 | Fixture item descriptions | F | 11 | VISUALLY INSPECTED |
| 3 | Fixture Summary Box | E | 12 | DISPOSITIONED |
| 4 | Consumption Effects Table | C | 18 | ROUTED TO TEST-901 |
| 5 | Unrelated Appendix Table | C | 20 | EXCLUDED — no resource or duration content |

**Manifest closure:** every row above is dispositioned.

## 5. Index Enumeration

### 5.1 Tables / Checklists Index

| Entry | Page | Disposition |
|---|---|---|
| Fixture Duration Table | 10 | VISUALLY INSPECTED |
| Consumption Effects Table | 18 | ROUTED TO TEST-901 |

### 5.2 General Index

| Entry | Pages | Followed? | Disposition |
|---|---|---|---|
| Duration | 10, 12 | yes | DISPOSITIONED |
| Fixture item | 11 | yes | DISPOSITIONED |

### 5.3 Specialist indexes

| Instrument | Entries relevant | Disposition |
|---|---|---|
| Index to Fixture Effects, p. 21 | none relevant | DISPOSITIONED — every entry is a consumption effect, routed to `TEST-901` |

### 5.4 Enumerated absences

The fixture source's General Index has no `Resource` entry and no `Supply` entry;
the bridge to p. 10 runs through `Duration`.

## 6. Governing Objects

| Object | Page | Type | Why it governs |
|---|---|---|---|
| Fixture Duration Table | 10 | table | states the duration this card owns |
| Fixture item descriptions | 11 | prose | states the item's operating behaviour |

The p. 10 table is the **principal** governing object; the p. 11 descriptions
qualify it, so neither is *the* single governing object.

## 7. Visual Inspection Record

```text
COVERAGE-LEDGER
EVIDENCE-PAGES:  10, 11, 12
IMAGE-VERIFIED:  10, 11, 12, 18, 20
LOCATOR-ONLY:    13, 21
ACCESS-BLOCKED:  none
```

| Page | Rendering confirmed | Note |
|---|---|---|
| 10 | full, at 1400px | table renders complete; row count confirmed |
| 11 | full, at 1400px | all three columns legible |
| 12 | full, at 1400px | summary box legible |

## 8. Cross-Reference Ledger

| From | Explicit reference | Followed to | Result |
|---|---|---|---|
| 10 | see p. 18 | 18 | consumption effects; routed to `TEST-901`, nothing owned here |
| 11 | see Ch. 2 | 13 | nothing relevant located |

**Whole-source search terms used** (§9): duration, supply, resource, consume,
expire, replacement.

## 9. Repository-Fact Verification

| Project claim | Artifact inspected | Identifier / section | Verdict |
|---|---|---|---|
| `TEST-901` owns consumption effects | `tests/tooling/fixtures/README.md` | fixture register | VERIFIED — fixture-local claim, no real Rule ID asserted |

## 10. Evidence Map

| # | Fact | Object | Provenance | Confidence |
|---|---|---|---|---|
| E-1 | A fixture item lasts six units | p. 10 | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E-2 | The duration is restated on p. 12 | p. 12 | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED |
| E-3 | Two items therefore last twelve units | pp. 10–11 | Necessary Mechanical Consequence | NECESSARY CONSEQUENCE |
| E-4 | Consumption effects are not this card's | p. 18 | Unresolved by RC | REPOSITORY FACT — NOT A SOURCE CLAIM |

Verbatim, p. 10:

```text
A fixture item lasts six units once started, and no fixture rule shortens it.
```

## 11. Negative Claim Ledger

```text
NEGATIVE-CLAIM-RECORD
CLAIM:                           no second duration for the fixture item is printed anywhere
SCOPE SEARCHED:                  Ch. 1 pp. 10-12, Ch. 2 pp. 13-20, Appendix p. 21
STRUCTURAL INSTRUMENTS CHECKED:  TOC, Tables Index, chapter headings
INDEXES CHECKED:                 General Index (Duration, Fixture item), Index to Fixture Effects
SEARCH TERMS USED:               duration, lasts, expire, burn, units
CROSS-REFERENCES FOLLOWED:       p. 18, p. 13
VISUAL PAGES INSPECTED:          10, 11, 12, 18, 20
FALSIFICATION ATTEMPT:           re-swept the Tables Index for every table naming a duration, and
                                 re-read the p. 12 summary box against the p. 10 table
CONFIDENCE:                      DIRECT PRIMARY TEXT
```

## 12. Ownership and Dependency Routing

| Mechanic | Owner | Status | Evidence for the routing |
|---|---|---|---|
| duration state | `TEST-900` (this card) | in progress | §6 |
| consumption effects | `TEST-901` | UNRESEARCHED | §9 row 1 |

## 13. Falsification Pass

```text
FALSIFICATION-RECORD
CONCLUSION:     the fixture item's duration is six units
WOULD FALSIFY:  a second, different duration printed elsewhere in the source
SOUGHT:         Tables Index, General Index Duration entry, the p. 12 summary box, Ch. 2
RESULT:         none located; the p. 12 restatement agrees with p. 10
DISPOSITION:    CONFIRMED
```

```text
FALSIFICATION-RECORD
CONCLUSION:     consumption effects belong to TEST-901, not here
WOULD FALSIFY:  a p. 10-12 clause making this card resolve a consumption effect
SOUGHT:         both governing objects, and the p. 10 cross-reference to p. 18
RESULT:         p. 10 delegates explicitly; nothing here resolves an effect
DISPOSITION:    CONFIRMED
```

## 14. Open-Question Closure

| # | Open question | Object implicated | Disposition |
|---|---|---|---|
| 1 | does the duration pause when unused? | p. 10, p. 12 | RETAINED AS GENUINE SOURCE AMBIGUITY |
| 2 | who resolves a consumption effect? | p. 18 | CONFIRMED OUT OF SCOPE |
| 3 | is the duration restated a third time? | Appendix p. 21 | RESOLVED BY SOURCE INSPECTION |

## 15. Primary-Source Coverage Checklist

- Relevant structural units inspected: Ch. 1 pp. 10–12; Ch. 2 pp. 13–20 to exclusion
- Tables / Checklists Index entries dispositioned: 2, with §5.1 as the ledger
- General Index entries dispositioned: 2, with §5.2 as the ledger
- Specialist indexes dispositioned: Index to Fixture Effects, p. 21
- Named tables inspected: Fixture Duration Table, Consumption Effects Table
- Structured entity entries inspected as complete units (§9.7): the fixture item entry, p. 11
- Cross-references followed: 2, with §8 as the ledger
- Visual verification completed for: pp. 10, 11, 12, 18, 20
- Deliberately excluded objects, each with its reason: Unrelated Appendix Table, p. 20 — no resource or duration content

## 16. Independent Review Status

```text
ORIGINAL RESEARCHER OUTPUT:  PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
INDEPENDENT REVIEW:          NOT YET PERFORMED
HUMAN EVIDENCE REVIEW:       NOT GIVEN
```

**Research-Completion Gate (§11.1):**

- [x] every Coverage Manifest row dispositioned
- [x] no unresolved visual-access blocker
- [x] every material negative claim has a Negative Claim Record
- [x] every repository fact verified against the repository this pass
- [x] pre-review self-falsification pass complete
- [x] open questions explicitly listed and classified
- [x] required §6 and §10.2 vocabulary used verbatim
- [x] `uv run python scripts/lint_evidence.py` passes
