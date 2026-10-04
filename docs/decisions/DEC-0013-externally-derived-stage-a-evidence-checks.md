# DEC-0013: Externally-Derived Stage-A Evidence Checks

## Decision ID
DEC-0013

## Title
Externally-Derived Stage-A Evidence Checks (supersedes `DEC-0012`)

## Status
Approved

## Date
2026-10-04

> **Lifecycle history.** Drafted 2026-10-04 under a human-assigned process-redesign task;
> **approved by the human project owner 2026-10-04.** The `Date` field carries the approval
> date, per this repository's convention (`DEC-0010`, `DEC-0011`, `DEC-0012`). How this
> record reached approval is preserved rather than erased:
>
> - It was drafted `Proposed — awaiting human approval`, because an agent has no authority
>   to approve a project-wide process decision (`DEVELOPMENT_WORKFLOW.md` §9,
>   `AGENTS.md` §12) — the same correction `DEC-0010` and `DEC-0012` each record having
>   had to make about themselves.
> - While proposed, an independent implementation review found that the first
>   implementation **did not deliver what this record's title claims**: the packet's
>   `SEEDS` block was researcher-written and the linter read nothing outside the packet,
>   so deleting p. 98 let the pilot's original `B-1` defect lint clean again. Corrected at
>   `916d77f` — seeds are now derived from `INVENTORY.md` and accepted neighbour packets.
> - A narrow closure review then found one further blocking defect: `RULE-ID` was itself a
>   packet-authored, unverified selector, so a one-character typo derived zero pages and
>   linted clean. Corrected at `1a340b5` with filename corroboration, `INVENTORY.md`
>   resolution, loud failure and targeted regressions.
> - Human approval is the closure step. **No further process review was performed**, by
>   deliberate application of this record's own anti-spiral principle: a bounded mechanical
>   defect is corrected, machine-verified and dispositioned by a human, not escalated into
>   another review cycle.
>
> **`DEC-0012` is superseded for future Stage-A work. `DEC-0012` remains historical and
> unchanged** — its text is byte-identical to the version approved 2026-10-01, and this
> record does not rewrite it.

## Supersedes

`DEC-0012 — Stage-A Evidence-Integrity Gates, Packet Template, and Structural Linter`.

**`DEC-0012` remains historical and is not rewritten.** Its rationale, its gates, its
pilot authorization and its fixed success criteria stay exactly as approved on
2026-10-01. This record supersedes its *mechanism*, not its diagnosis — which was
correct — and preserves the pilot result that justifies the replacement.

### `DEC-0012`'s pilot did not pass its own fixed success criteria

The pilot card was `ENC-001` (Encounter Distance), selected by the human project owner.
Against `DEC-0012` item 15's four criteria, quoted verbatim from that record:

```text
1. the evidence linter runs on the real packet;
2. the packet reaches independent review with all structural gates satisfied;
3. independent review #1 finds NO previously uninspected governing object;
4. no more than TWO independent completeness reviews are required to reach PASS.
```

| # | Result | Evidence |
|---|---|---|
| 1 | **PASS** | The linter governed `ENC-001-evidence.md`; the gate is no longer inert |
| 2 | **FAIL substantively** | Linter gates were satisfied while §9.3.1's enumerate-before-concluding was not |
| 3 | **FAIL** | Review #1 found RC p. 98 `Contact` |
| 4 | **FAIL** | Review #2 returned `FAIL`; the two-review budget was exhausted |

`DEC-0012` item 15 forbids softening these after the fact, and this record does not.
Two of four failed outright. The pilot artifacts are preserved on the
`enc-001-stage-a-evidence` branch at `b880ffd` — the Stage-A packet (`d24aa3a`), the
bounded remediation (`b880ffd`), and Independent Review #1 — and are the evidence for
everything below. They are referenced here rather than reproduced.

## Context

### The architectural conclusion: internal consistency is not external completeness

`DEC-0012` diagnosed the problem correctly. Its own rationale states, of the
`CLUSTER-004` failures that motivated it:

> "The failure was evidentiary closure, not rules interpretation … Not one `FAIL` was
> caused by misreading a rule."

That prediction held through the pilot. Across nine independent reviews of two cards —
seven on `EXP-006`, two on `ENC-001` — **21 blocking findings were raised and not one was
a rules-conformance defect.** Every transcription checked was exact, every index absence
claimed was true, every repository fact spot-checked held, and the researcher's own
packet correctly refuted an inherited error in accepted `ENC-005` evidence.

What failed was never the rules work. It was the artifact describing it.

`DEC-0012`'s remedy was to require more description: a Coverage Manifest, Negative Claim
Records, a Repository Fact Gate, a self-falsification pass, and a structural linter. Five
of those six mechanisms are **closed loops over the researcher's own account**. A Coverage
Manifest is the researcher's statement of what the researcher looked at; if a page is
never opened it simply does not appear, every instrument agrees with every other, and the
linter passes. That is precisely what happened: a packet containing the p. 98 omission
passed the `DEC-0012` linter cleanly.

**Only independent review was externally grounded, which is why it caught everything and
why cost concentrated there.**

### The observed failure modes this record responds to

```text
self-reported completeness        the manifest cannot see what was never enumerated
page / citation drift             E-19 cited p. 91 for text printed on p. 93
count drift                       three gate counts stale in a gate asserting
                                  "each line confirmed, not assumed"
overconfident coverage claims     "every row is now visually inspected", while six
                                  cited pages were uninspected
remediation-created defects       the pilot's remediation fixed both blocking findings
                                  and introduced two more -- one of them the same
                                  count defect, inside the remediation of that finding
excessive review cost             9 reviews, 21 blocking findings, 0 rules defects
```

## Decision

Stage-A evidence moves the mechanically checkable facts **outside** the researcher's
self-report surface, and reduces what the researcher maintains by hand.

**1. The researcher does not declare a page range.** Candidate pages are generated
externally. `DEC-0012`'s model let a researcher declare the interval that a check then
validated — a closed loop. There is no `ranges` field.

**2. Seeds come from four instruments.** The Tables/Checklists Index and General Index
for the card's subject terms; every page cited by accepted packets of the card's
neighbours; direct leads discovered during inspection; and any page the packet itself
cites. Neighbours are `INVENTORY.md` structured edges in both directions, union the seams
the researcher declares.

**3. A seed is an obligation, never inherited truth.** It means *someone cited this page
in a related context, so look and disposition it*. It carries a page and the name of the
packet it came from, and no conclusion — because a prior accepted packet may be wrong.
`ENC-005`'s accepted evidence described the Encounter Distances Table as "light-keyed",
which `ENC-001` correctly refuted against primary text, while that same packet would have
seeded p. 98 correctly. Seeds are reliable about **where to look** and must never be
treated as reliable about **what is there**.

**4. Two seed types only.** `PAGE` (a page needing disposition) and `LEAD` (a named term
or reference not yet tied to a page, which must resolve before Stage A completes). A
range is a set of pages, not a third type.

**5. One page ledger, five dispositions.** `INSPECTED`, `ROUTED_EXTERNAL`,
`IRRELEVANT_AFTER_INSPECTION`, `OUTSIDE_CARD_SCOPE`, `ACCESS_BLOCKED`. Routed and
out-of-scope pages name a Rule ID or a bounded reason, in one clause. `ACCESS_BLOCKED` is
a hard stop. Only an `INSPECTED` page may support an evidence row.

**6. Expansion is discovered, not declared.** When inspecting a page shows a governing
object beginning or continuing outside it, the pages spanned by that object's **own titled
structure** enter the candidate set — never a fixed page window, and never a whole chapter
by default.

**7. Citations are mechanically verified.** A quoted evidence row must match the
transcription recorded for the page it cites, after normalizing whitespace, quotation
glyphs and hyphenation. Case is preserved, because RC distinguishes `Dim light` from
`dim light` in table cells. A paraphrase row requires only that its page be `INSPECTED`;
its correctness is the reviewer's to judge. OCR is never authoritative.

**8. Counts are derived, never written.** Every tally the pilot got wrong — manifest rows,
open questions, falsification records, inspected totals, gate checkboxes — is computed by
the linter and printed. Writing one into a packet is itself a lint failure, because the
defect is the field's existence, not its value.

**9. Negative claims are narrowed to consequential ones.** A claim needs a record only if
a future Rule Card would rely on the asserted absence. Index-entry absences, artifact
existence, counts, and pages already dispositioned irrelevant do not. The pilot carried
four records; one was consequential, and it was the only one whose search proved
inadequate.

**10. Repository facts are machine-derived.** Artifact existence, Rule ID status, whether
an accepted packet cites a page, whether a symbol is exported — none of these are prose
rows. Human rows survive only for judgment: which Rule ID owns a mechanic, whether a
mechanic is semantically external, whether an ownership gap is genuine.

**11. Falsification is targeted.** Required for consequential negative claims, ownership
and exclusion judgments, and open semantic ambiguities. Not a general ceremony.

**12. The independent review charter is semantic.** The reviewer owns rules
interpretation, source-area exclusion, semantic cross-reference completeness, ownership
assignment, silent ambiguity adjudication, governing-object classification, and whether
the subject terms, neighbour list and exclusions were adequate. The reviewer is **not**
the primary detector for page numbers, counts, page gaps, artifact pairing, duplicate
status or tally mismatches. All five of the pilot's blocking slots were spent on work a
machine now does.

**13. Escalation is by consequence, not by label.**

```text
Mechanical defect, inspected source set unchanged, conclusions unchanged
    -> fix + machine verification.  NO independent re-review.

Defect revealing previously uninspected potentially governing source,
or changing a rules or completeness conclusion
    -> substantive completeness defect + independent re-review.
```

A provenance defect that reveals an uninspected source escalates. Classification follows
what the defect exposes, never what kind of artifact it sits in.

**14. Anti-spiral termination.**

| Defect class | Remediation | Independent re-review | Sufficient verification |
|---|---|---|---|
| Rules-conformance | Substantive | **Required** | Semantic review + human acceptance |
| Source-completeness | Inspect and disposition | **Required** | Semantic review |
| Mechanical provenance | Correct | No | Citation check green |
| Artifact self-description | Correct, **or delete the claim** | No | Derived checks green |
| Documentation / status | Proportional; **does not reopen accepted rules work** | No | Owner record updated |
| Governance / process | Human decision | No | Human |

**Budget: two substantive completeness reviews per Stage-A card.** Mechanical fixes do
not consume budget. If the budget is exhausted without `PASS`, **STOP and evaluate the
process** — there is no automatic third review.

**Anti-spiral clause: a remediation may not trigger a new full review cycle unless it
changes a rules or completeness conclusion.** `EXP-006` spiralled through six cycles
because every remediation reopened the whole surface; the pilot reproduced it in miniature.

**15. Grandfathering is carried forward unchanged.** The twelve pre-`DEC-0012` packets
remain a closed set and are **not migrated**. Historical packets stay historical.

## Consequences

- The canonical template drops from sixteen required sections to fourteen, and four of
  the survivors are materially smaller. No count field appears anywhere in it.
- `scripts/lint_evidence.py` is rewritten rather than extended: the checks tied purely to
  manual counts and duplicate self-description are **removed**, and seed-disposition,
  citation-verification and derived-count reporting take their place.
- The researcher-maintained surface is measurably smaller; the implementation report
  accompanying this record carries the before/after comparison against the pilot packet.
- `RULE_CARD_RESEARCH_PROTOCOL.md` and `AGENTS.md` §10 were aligned at `916d77f` under
  explicit human direction, both being protected or protocol-authoritative. The protocol
  carries a supersession notice at §1 naming exactly which instruments this record
  replaced and which still bind; its `DEC-0012` references below that notice are
  deliberately preserved as history. `DEVELOPMENT_WORKFLOW.md` §10.1 was added at
  `07eec15` and corrected at `1a340b5`.
- `ENC-001` resumes under this record, not as a third review under `DEC-0012`. Its
  remaining work is mechanical except for RC p. 100 `Evasion at Sea` and the scope
  residue in its open-question `Q-7`.

## Accepted limitations

These are known and accepted at approval. They are recorded here so that no later reader
has to rediscover them, and so that no artifact claims more than the mechanism delivers.

### A. Index seeding is not mechanically external

Candidate enumeration from the Rules Cyclopedia's **Tables/Checklists Index** and
**General Index** is **not** machine-derived, because the repository holds no structured
index dataset outside Stage-A packets themselves. Deriving index candidates from a ledger
written inside the packet under review would be circular, and that is the precise defect
this record exists to remove.

**Index enumeration therefore remains a manual, semantic research responsibility, reviewed
by the independent semantic reviewer.** It must not be described as machine-checked
anywhere — not in a packet, not in the template, not in the tooling's own output. The
linter prints this caveat on every real packet it reports on.

The gap is closable, but not by this record: it needs a repository-level index
transcription authored outside any Stage-A packet, under its own review. That is a separate
decision and is not created here.

What this costs in practice is bounded. The pilot's principal omission, RC p. 98 `Contact`,
is reachable **without** any index seeding: `ENC-005`'s accepted packet cites it, and
`INVENTORY.md`'s reverse edge reaches `ENC-005` with no researcher declaration at all.

### B. External-seed breadth is wide, deliberately

`ENC-001` currently derives **approximately 43** external page obligations, including
plainly external pages — pp. 3 and 300–304 among them, which are not encounter-distance
material by any reading.

This is the intended direction of error. A seed is an obligation to look, and the two
failure costs are asymmetric: an unnecessary seed costs one line to disposition
(`OUTSIDE_CARD_SCOPE`, `IRRELEVANT_AFTER_INSPECTION`), while a missing one costs an
independent review — which is exactly what the pilot spent.

**No threshold and no gate are added.** The linter prints seed provenance by origin packet
as a diagnostic only. **Actual seeding cost will be measured during controlled `ENC-001`
re-entry**, before any decision about whether breadth needs refinement. Refining it now
would be tuning against a single simulated card.

## Falsification condition

This record is wrong if, under it, independent review continues to spend its findings on
bookkeeping — or if the first cards run under it show rules-conformance defects that the
removed ceremony would have caught. The measurable criteria are:

```text
no previously uninspected governing object at first semantic review;
no mechanically detectable provenance or count defect reaches a human reviewer;
one semantic review normally sufficient;
a second review consumed only after a substantive completeness defect;
review and remediation effort does not exceed source-research effort per card.
```

Those are stated before any card runs under this record, for the same reason `DEC-0012`
stated its own: so they cannot be softened afterwards.
