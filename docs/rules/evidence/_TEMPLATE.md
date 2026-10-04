# `<RULE-ID>` — `<Title>` — Stage-A Evidence

> **Canonical Stage-A evidence template** (`DEC-0013`). Copy to
> `docs/rules/evidence/<RULE-ID>-evidence.md` and fill it in.
>
> **What changed from `DEC-0012`.** Page bookkeeping, counts and coverage claims are no
> longer written by hand — they are **derived or checked mechanically**. You disposition
> pages; you do not declare ranges, tally rows, or assert that everything was inspected.
> `DEC-0012`'s pilot failed because researcher-maintained instruments agreed with each
> other while being wrong about the source. **Internal consistency is not external
> completeness.**
>
> `scripts/lint_evidence.py` checks structure, seed dispositions and citations. It cannot
> check whether the research is right. A green linter is a floor, never a certification —
> you may never certify your own packet.
>
> Delete this banner and every `<...>` placeholder.

```text
PACKET-STATUS
RULE-ID:              <RULE-ID>
INDEPENDENT-REVIEW:   PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
RECOMMENDATION:       MORE PRIMARY RESEARCH REQUIRED
```

> `RECOMMENDATION` is exactly `EVIDENCE READY FOR HUMAN REVIEW` or
> `MORE PRIMARY RESEARCH REQUIRED`. An original researcher may never write
> `SOURCE COMPLETENESS PASSED`, `SOURCE COMPLETENESS CERTIFIED` or
> `HUMAN EVIDENCE GATE CLEARED`.

---

## 1. Scope and Seams

**This card owns:** `<the mechanic, in one sentence>`

**It does not own, and routes to:** `<Rule ID — mechanic>`, `<Rule ID — mechanic>`

**Neighbour Rule IDs** (seed sources — `INVENTORY.md` edges both directions, plus seams
you declare here): `<IDs>`

**Subject terms** (used against both indexes): `<terms>`

## 2. Primary Source

| Source | Access method | Role |
|---|---|---|
| `<edition, printing>` | `<page-image URL/path pattern>` | authoritative |
| `<OCR / full text>` | `<path>` | **locator only**, never evidence |

**Access limitations:** `<each, or "None encountered.">`

## 3. Seeds

> **Machine-generated obligations, not inherited truth.** A seed means *someone cited this
> page in a related context, so you must look and disposition it*. It does **not** mean the
> prior packet was right — an accepted packet may contain a wrong interpretation.

```text
SEEDS
TABLES-INDEX:   93
GENERAL-INDEX:  87, 91-96
NEIGHBOUR:      ENC-005: 98, 99, 100, 104
LEADS:          infravision -> 24, 25
```

> *The values above are an illustration, not this card's. Replace them.*

> You do **not** declare a page range. Candidate pages come from the instruments above
> plus anything you cite. A `LEAD` is a named term or printed reference not yet tied to a
> page; it must resolve before Stage A completes.

## 4. Page Dispositions

> The **only** page bookkeeping in this packet. Every seeded page, every page you cite, and
> every cross-reference target must appear here exactly once.

```text
PAGE-DISPOSITIONS
87: INSPECTED
91: INSPECTED
92: INSPECTED
93: INSPECTED
94: ROUTED_EXTERNAL EXP-008          # monster selection, not distance
95: INSPECTED
96: ROUTED_EXTERNAL EXP-008
98: INSPECTED
99: ROUTED_EXTERNAL ENC-005          # Evasion Checklist
100: ROUTED_EXTERNAL ENC-005         # Evasion at Sea
104: OUTSIDE_CARD_SCOPE COMBAT-*     # Retreat / Fighting Withdrawal
24: INSPECTED
25: IRRELEVANT_AFTER_INSPECTION      # elf entry duplicates p. 24
```

> *Illustrative values. Note p. 104: it was seeded from a neighbour packet, is
> genuinely not this card's, and costs exactly one line to dismiss.*

> Vocabulary: `INSPECTED`, `ROUTED_EXTERNAL`, `IRRELEVANT_AFTER_INSPECTION`,
> `OUTSIDE_CARD_SCOPE`, `ACCESS_BLOCKED`. `ROUTED_EXTERNAL` and `OUTSIDE_CARD_SCOPE`
> require a Rule ID or bounded reason. **`ACCESS_BLOCKED` is a hard stop** and forbids an
> `EVIDENCE READY FOR HUMAN REVIEW` recommendation. Only an `INSPECTED` page may support
> an evidence row.
>
> **Expansion is discovered, not declared.** When inspecting a page shows a governing
> object beginning or continuing outside it, the pages spanned by that object's own titled
> structure enter this list too — never a fixed page window, never a whole chapter by default.

## 5. Governing Objects

| Object | Page | Kind | Disposition | Owner |
|---|---|---|---|---|
| `<object>` | `<p.>` | `<table/checklist/prose/stat block>` | `<GOVERNING / ROUTED>` | `<Rule ID if routed>` |

## 6. Index Enumeration

> Index instruments are completeness instruments. Record **absent** entries too — an index
> with no entry for the mechanic's obvious name is itself a research fact.

| Instrument | Entry | Pages | Disposition |
|---|---|---|---|
| `<Tables / General>` | `<entry as printed>` | `<pp.>` | `<disposition>` |

**Enumerated absences:** `<terms that do not exist, or "None recorded.">`

## 7. Transcriptions

> One block per page carrying a quoted evidence row. Transcribed from the page image —
> OCR is never authoritative. The citation check matches quotes against these.

```text
TRANSCRIPTION p. <n>
<verbatim text, complete; an elision that removes a governing clause is a defect>
```

## 8. Evidence Map

| # | Page | Quote | Paraphrase | Object | Provenance | Confidence |
|---|---|---|---|---|---|---|
| E-1 | `<n>` | `<verbatim substring, or empty>` | `<summary, or empty>` | `<p., object>` | `<Rules Cyclopedia Explicit / Necessary Mechanical Consequence / Unresolved by RC>` | `<label>` |

> Confidence uses exactly one label: `DIRECT PRIMARY TEXT`,
> `PRIMARY TEXT + CROSS-REFERENCE CONFIRMED`, `NECESSARY CONSEQUENCE`,
> `SECONDARY SOURCE LOCATOR ONLY`, `NOT YET VERIFIED`, `NOT YET ESTABLISHED`,
> `REPOSITORY FACT — NOT A SOURCE CLAIM`.
>
> A row carries **either** a quote **or** a paraphrase. A quote must occur in its cited
> page's transcription; a paraphrase only requires the page to be `INSPECTED`, and its
> correctness is the reviewer's to judge.

## 9. Cross-References

| From | Printed reference | To | Result |
|---|---|---|---|
| `<p.>` | `<"see page X" as printed>` | `<p.>` | `<what it established, incl. "nothing relevant">` |

## 10. Ownership and Dependency Routing

| Mechanic | Owner | Status | Basis |
|---|---|---|---|
| `<mechanic>` | `<Rule ID, or "NO RULE ID EXISTS">` | `<LANDED / APPROVED / UNRESEARCHED>` | `<how established>` |

> Route consequences; do not absorb them. Where no owner exists, record the gap — do not
> invent one (`AGENTS.md` §3). Facts a machine can establish (artifact exists, Rule ID
> status, a packet cites page N, a symbol is exported) do **not** belong here.

## 11. Consequential Negative Claims

> Only claims a future Rule Card would **rely on**. Index-entry absences, artifact
> existence, counts, and pages already dispositioned irrelevant need no record.

```text
NEGATIVE-CLAIM
CLAIM:                  <the absence being asserted, at the scope actually searched>
SCOPE SEARCHED:         <chapters / page ranges>
INSTRUMENTS CHECKED:    <indexes, structural instruments>
FALSIFICATION ATTEMPT:  <where contrary evidence was sought, and what came back>
```

> If this packet asserts no consequential absence, state exactly: `NEGATIVE CLAIMS: NONE`.

## 12. Targeted Falsification

> Only for consequential negative claims, ownership/exclusion judgments, and open semantic
> ambiguities. Not a general ceremony. Keep each short and tied to one claim.

```text
FALSIFICATION
CONCLUSION:   <the claim under challenge>
SOUGHT:       <where contrary evidence was looked for>
RESULT:       <what came back>
DISPOSITION:  <CONFIRMED / QUALIFIED / REJECTED>
```

> A `REJECTED` conclusion stops the task. It is not replaced with a second guess.

## 13. Open Questions

| # | Question | Object | Disposition |
|---|---|---|---|
| 1 | `<question>` | `<p., object>` | `<label>` |

> Labels, verbatim: `RESOLVED BY SOURCE INSPECTION`, `CONFIRMED OUT OF SCOPE`,
> `RETAINED AS GENUINE SOURCE AMBIGUITY`,
> `BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED`. A `BLOCKED` row forbids an
> `EVIDENCE READY FOR HUMAN REVIEW` recommendation.

## 14. Independent Review

```text
INDEPENDENT REVIEW:    <NOT YET PERFORMED / INDEPENDENT COMPLETENESS REVIEW PASSED /
                        INDEPENDENT COMPLETENESS REVIEW FAILED>
HUMAN EVIDENCE REVIEW: <NOT GIVEN / ACCEPTED, with date>
```

> The reviewer evaluates **semantics**: rules interpretation, source-area exclusion,
> semantic cross-reference completeness, ownership assignment, silent ambiguity
> adjudication, governing-object classification, and whether the subject terms, neighbour
> list and exclusions were adequate. Page numbers, counts, gaps and tallies are the
> machine's job, not the reviewer's.
>
> **No count fields appear anywhere in this template.** Counts are derived by the linter
> and printed in its report; they are never maintained by hand.
