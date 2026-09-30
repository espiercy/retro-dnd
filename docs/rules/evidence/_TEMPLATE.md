# `<RULE-ID>` — `<Title>` — Stage-A Evidence

> **This is the canonical Stage-A evidence-packet template** (`DEC-0012`;
> `RULE_CARD_RESEARCH_PROTOCOL.md` §11.2). Copy it to
> `docs/rules/evidence/<RULE-ID>-evidence.md` and fill it in **in section order**.
>
> **The order is the point.** §9.3.1 fixes it:
>
> ```text
> enumerate  →  inspect  →  disposition  →  falsify  →  conclude
> ```
>
> Writing conclusions first and reconstructing coverage afterwards is prohibited
> (§9.3.1), and it is the specific behaviour that cost `CLUSTER-004` four `FAIL`
> review cycles.
>
> `scripts/lint_evidence.py` checks this packet's **structure** — that the required
> instruments exist and that its own ledgers agree with each other. It cannot check
> whether the research is right. Run it before requesting independent review
> (§11.1); a green linter is a floor, never a certification.
>
> Delete this banner and every `<...>` placeholder. Leave no section out: where a
> category is genuinely empty, say so explicitly with the stated "NONE" form —
> an omitted section is ambiguous, an explicit "none" is not.

```text
PACKET-STATUS
RULE-ID:              <RULE-ID>
PASS:                 1
SELF-FALSIFICATION:   NOT STARTED
REPOSITORY-FACT-PASS: NOT STARTED
INDEPENDENT-REVIEW:   PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
RECOMMENDATION:       MORE PRIMARY RESEARCH REQUIRED
```

> `SELF-FALSIFICATION` and `REPOSITORY-FACT-PASS` become `COMPLETE` only when §12
> and §9 below are actually finished. `RECOMMENDATION` is exactly one of
> `EVIDENCE READY FOR HUMAN REVIEW` or `MORE PRIMARY RESEARCH REQUIRED` (§11), and
> an original researcher may never write `SOURCE COMPLETENESS PASSED`,
> `SOURCE COMPLETENESS CERTIFIED` or `HUMAN EVIDENCE GATE CLEARED` (§10.1.2).

---

## 1. Research-Start Gate

> Completed **before** substantive research (§5.1). Each line is established, not
> assumed — a stale project boundary or an unavailable source is cheap to discover
> now and expensive to discover after a full pass.

| Item | Established |
|---|---|
| Exact card scope, as currently registered | `<INVENTORY.md` row, quoted scope`>` |
| Known ownership seams | `<neighbouring card IDs and what each owns>` |
| Authoritative primary source | `<edition / printing / access method>` |
| Required structural + index instruments | `<TOC, Tables Index, General Index, specialist indexes>` |
| Current repository dependencies | `<verified against INVENTORY.md this pass>` |
| Primary-source visual access confirmed | `<yes / partial — name the gap>` |

**Scope boundary this packet will not cross:** `<what is deliberately out of scope, and its owner>`

## 2. Primary Source Accessed

| Source | Access method | Role |
|---|---|---|
| `<edition, printing>` | `<page images — exact URL/local path pattern>` | authoritative |
| `<same edition, second digitisation>` | `<URL/path>` | authoritative (§9.2.1 — still primary) |
| `<OCR / full-text>` | `<URL/path>` | **locator only**, never sole evidence (§9.5) |

**Access limitations encountered, including where a workaround succeeded** (§11 item 17):

`<list each, or "None encountered.">`

## 3. Source Structure

> The source's own structure, read before its content (§9.1.1).

| Structural unit | Pages | Could govern this card? |
|---|---|---|
| `<Ch. N — title>` | `<pp.>` | `<yes / no, with reason>` |

## 4. Coverage Manifest

> **The pre-conclusion instrument** (§9.3.1). Every potentially governing object is
> enumerated here **before** mechanical conclusions are written, and every row
> carries an explicit disposition drawn from the repository's established
> vocabulary: `OPENED` / `VISUALLY INSPECTED` / `DISPOSITIONED` / `ROUTED TO <ID>` /
> `EXCLUDED — <reason>` / `ACCESS BLOCKED` / `NOT YET ESTABLISHED`.
>
> A row may not be left blank, and a row may not be added after the conclusions it
> would have governed.

| # | Object | Class (§9.1 A–I) | Page | Disposition |
|---|---|---|---|---|
| 1 | `<object>` | `<A–I>` | `<p.>` | `<disposition>` |

**Manifest closure:** `<every row above is dispositioned / rows N, M remain open — the packet therefore recommends MORE PRIMARY RESEARCH REQUIRED>`

## 5. Index Enumeration

> Index instruments are **completeness instruments, not citation aids** (§9.9,
> elevating precedent `P-001`). Enumerate the relevant entries and disposition
> each; a claim that an index was surveyed must be backed by the ledger below.
> Record **absent** entries too — an index that has no entry for the mechanic's
> obvious name is itself a research fact.

### 5.1 Tables / Checklists Index

| Entry | Page | Disposition |
|---|---|---|
| `<entry as printed>` | `<p.>` | `<disposition>` |

### 5.2 General Index

| Entry | Pages | Followed? | Disposition |
|---|---|---|---|
| `<entry as printed>` | `<pp.>` | `<yes/no>` | `<disposition>` |

### 5.3 Specialist indexes

| Instrument | Entries relevant | Disposition |
|---|---|---|
| `<e.g. Index to Spells, p. 300>` | `<list>` | `<disposition>` |

### 5.4 Enumerated absences

`<index entries that do not exist, named explicitly — or "None recorded.">`

## 6. Governing Objects

| Object | Page | Type | Why it governs |
|---|---|---|---|
| `<object>` | `<p.>` | `<table / checklist / prose / stat block>` | `<reason>` |

> A **principal** governing object may be named. *The* single governing object may
> not, until every related structured and detailed object is dispositioned (§9.8).

## 7. Visual Inspection Record

```text
COVERAGE-LEDGER
EVIDENCE-PAGES:  69, 70, 150
IMAGE-VERIFIED:  69, 70, 150
LOCATOR-ONLY:    72, 121
ACCESS-BLOCKED:  none
```

> The page numbers above are illustrative, and the block is machine-read: replace
> them with this card's own. `EVIDENCE-PAGES` is every page carrying an evidence row
> in §10; `IMAGE-VERIFIED` is every page read as a page image; `LOCATOR-ONLY` is
> every page reached only through OCR, for routing or exclusion, carrying no
> evidence row; `ACCESS-BLOCKED` is `none` or the pages that could not be rendered.

> The linter enforces what five reviews kept catching by hand: every
> `EVIDENCE-PAGES` entry must appear under `IMAGE-VERIFIED` or `ACCESS-BLOCKED`, no
> page may be both `IMAGE-VERIFIED` and `LOCATOR-ONLY`, and any `ACCESS-BLOCKED`
> page forces `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED` and forbids an
> `EVIDENCE READY FOR HUMAN REVIEW` recommendation (§9.2, §9.2.1).
>
> **HTTP 200 is not proof that a page rendered.** Confirm the body text is visible
> (§9.2.1).

| Page | Rendering confirmed | Note |
|---|---|---|
| `<p.>` | `<size/crop used>` | `<e.g. columns 2-3 blank in scan A; obtained from scan B>` |

## 8. Cross-Reference Ledger

| From | Explicit reference | Followed to | Result |
|---|---|---|---|
| `<p.>` | `<"see page X" as printed>` | `<p.>` | `<what it established, including "nothing relevant">` |

**Whole-source search terms used** (§9): `<exact terms>`

## 9. Repository-Fact Verification

> Every claim about **this project** — ownership, landed status, "no Rule ID
> exists", "this dependency is unresearched", "the inventory says", "a test already
> covers this" — is verified against the repository **during this pass** (§10.5).
> Model memory is not evidence. An unverified claim is marked
> `UNVERIFIED PROJECT FACT` and blocks the completion gate.

| Project claim | Artifact inspected | Identifier / section | Verdict |
|---|---|---|---|
| `<claim as it appears in this packet>` | `<repo-relative path>` | `<line / row / §>` | `<VERIFIED / CORRECTED — was X / UNVERIFIED PROJECT FACT>` |

> If this packet makes no claim about the project, state exactly:
> `REPOSITORY FACTS: NONE`.

## 10. Evidence Map

| # | Fact | Object | Provenance | Confidence |
|---|---|---|---|---|
| E-1 | `<what the source establishes>` | `<p., object>` | `<Rules Cyclopedia Explicit / Necessary Mechanical Consequence / Unresolved by RC>` | DIRECT PRIMARY TEXT |

> The Confidence column uses **exactly one** §6 label per row:
> `DIRECT PRIMARY TEXT`, `PRIMARY TEXT + CROSS-REFERENCE CONFIRMED`,
> `NECESSARY CONSEQUENCE`, `SECONDARY SOURCE LOCATOR ONLY`, `NOT YET VERIFIED`,
> `NOT YET ESTABLISHED`, or `REPOSITORY FACT — NOT A SOURCE CLAIM`. No invented
> labels, no prose in that cell.

**Verbatim transcriptions** of governing text, each attributed to its page:

```text
<verbatim quotation, complete — an elision that removes a governing clause is a
defect, not a convenience>
```

## 11. Negative Claim Ledger

> **Absence requires stronger evidence than presence** (§10.4). Every material
> negative claim gets a record. A failed keyword or OCR search is never sufficient:
> without the enumeration, the correct classification is `NOT YET ESTABLISHED`, not
> source silence.

```text
NEGATIVE-CLAIM-RECORD
CLAIM:                           <the absence being asserted>
SCOPE SEARCHED:                  <chapters / page ranges>
STRUCTURAL INSTRUMENTS CHECKED:  <TOC, Tables Index, chapter headings>
INDEXES CHECKED:                 <General Index entries, specialist indexes>
SEARCH TERMS USED:               <exact terms>
CROSS-REFERENCES FOLLOWED:       <pages>
VISUAL PAGES INSPECTED:          <pages>
FALSIFICATION ATTEMPT:           <where evidence against this claim was sought, and what came back>
CONFIDENCE:                      <DIRECT PRIMARY TEXT | NOT YET ESTABLISHED | ...>
```

> If this packet asserts no material absence, state exactly:
> `NEGATIVE CLAIMS: NONE`.

## 12. Ownership and Dependency Routing

| Mechanic | Owner | Status | Evidence for the routing |
|---|---|---|---|
| `<mechanic>` | `<Rule ID, or "NO RULE ID EXISTS">` | `<LANDED / APPROVED / UNRESEARCHED>` | `<§9 row that verified it>` |

> Route consequences; do not absorb them. Where no owner exists, record the gap —
> do not invent an owner (`AGENTS.md` §3).

## 13. Falsification Pass

> §10 for each consequential conclusion, and §10.6's **pre-review
> self-falsification pass** for the five classes that failed historically:
> negative claims, ownership assignments, source-silence findings, dependency
> conclusions, and scope exclusions. Actively seek the evidence that would make
> each conclusion false.

```text
FALSIFICATION-RECORD
CONCLUSION:     <the claim under challenge>
WOULD FALSIFY:  <what evidence would make it false>
SOUGHT:         <where that evidence was looked for — objects, pages, instruments>
RESULT:         <what came back>
DISPOSITION:    <CONFIRMED / QUALIFIED / REJECTED>
```

> A `REJECTED` conclusion stops the task (`STOP — MORE PRIMARY RESEARCH REQUIRED`).
> It is not replaced with a second guess (§10).

## 14. Open-Question Closure

> Every unresolved statement this packet contains, classified with exactly one
> §10.2 label. **Zero silent unresolved research tasks** (§10.2).

| # | Open question | Object implicated | Disposition |
|---|---|---|---|
| 1 | `<question>` | `<p., object>` | RESOLVED BY SOURCE INSPECTION |

> Permitted labels, verbatim: `RESOLVED BY SOURCE INSPECTION`,
> `CONFIRMED OUT OF SCOPE`, `RETAINED AS GENUINE SOURCE AMBIGUITY`,
> `BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED`. A `BLOCKED` row forbids an
> `EVIDENCE READY FOR HUMAN REVIEW` recommendation.

## 15. Primary-Source Coverage Checklist

> §9.3's required section. This is the instrument a future auditor will use, so it
> must agree with §4, §5 and §7 rather than restate them loosely.

- Relevant structural units inspected: `<list>`
- Tables / Checklists Index entries dispositioned: `<count, with §5.1 as the ledger>`
- General Index entries dispositioned: `<count, with §5.2 as the ledger>`
- Specialist indexes dispositioned: `<list>`
- Named tables inspected: `<list>`
- Structured entity entries inspected as complete units (§9.7): `<list>`
- Cross-references followed: `<count, with §8 as the ledger>`
- Visual verification completed for: `<pages, per §7's ledger>`
- Deliberately excluded objects, each with its reason: `<list>`

> Completeness wording — `read in full`, `fully inspected`, `exhaustive`,
> `all relevant entries` — is permitted only where the ledgers above make it
> auditable (§9.10). Where they do not, describe exactly what was inspected
> instead.

## 16. Independent Review Status

```text
ORIGINAL RESEARCHER OUTPUT:  PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
INDEPENDENT REVIEW:          <NOT YET PERFORMED / PASS / FAIL, with the review artifact>
HUMAN EVIDENCE REVIEW:       <NOT GIVEN / ACCEPTED, with date>
```

**Research-Completion Gate (§11.1) — each line confirmed, not assumed:**

- [ ] every Coverage Manifest row dispositioned
- [ ] no unresolved visual-access blocker
- [ ] every material negative claim has a Negative Claim Record
- [ ] every repository fact verified against the repository this pass
- [ ] pre-review self-falsification pass complete
- [ ] open questions explicitly listed and classified
- [ ] required §6 and §10.2 vocabulary used verbatim
- [ ] `uv run python scripts/lint_evidence.py` passes

> Only then is independent completeness review requested. The original researcher
> does not certify its own packet (§10.1.2).
