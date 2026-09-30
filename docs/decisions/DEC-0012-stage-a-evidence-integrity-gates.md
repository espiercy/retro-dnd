# DEC-0012: Stage-A Evidence-Integrity Gates, Packet Template, and Structural Linter

## Decision ID
DEC-0012

## Title
Stage-A Evidence-Integrity Gates, Packet Template, and Structural Linter

## Status
Proposed — awaiting human approval

## Date
2026-09-30

> **Lifecycle note.** Drafted 2026-09-30 under a human-assigned research-process
> remediation task. It is recorded as `Proposed — awaiting human approval` because an
> agent has no authority to approve a project-wide process decision
> (`DEVELOPMENT_WORKFLOW.md` §9, `AGENTS.md` §12) — the same correction `DEC-0010`
> records having had to make about itself. The status term matches the one `DEC-0010`
> adopted for that state.
>
> The assigning task authorized the governance edits, the template, the linter and its
> tests; it did not authorize approving this record, lifting the Stage-A research freeze,
> or any rules research.

## Context

### What happened

`CLUSTER-004` Stage A (`EXP-006`, `ENC-005`) required **five independent completeness
reviews**. Reviews 1–4 returned `FAIL / FAIL`; review 5 returned `PASS / PASS`. The full
history is preserved at `docs/rules/evidence/CLUSTER-004-stage-a-completeness-review*.md`
and summarized in `docs/rules/clusters/CLUSTER-004-equipment-resources-and-evasion.md` §3,
and is **not rewritten by this record** — it is the evidence that motivates it.

The independent-review gate worked. The researcher workflow did not. Four `FAIL` cycles is
far too expensive a way to reach a correct packet.

### The failure was evidentiary closure, not rules interpretation

Not one `FAIL` was caused by misreading a rule. Every one was caused by a packet treating
its own coverage as closed when it was not, and then writing conclusions on top of that.

Two measurements make the cost concrete:

```text
Reviews 1-3   found uninspected GOVERNING OBJECTS
              (p. 93 Encounter Distances Table; p. 150 Blindness; p. 108 Attack Roll
               Modifiers; Ch. 5 pp. 81-86 general skills; p. 85 Survival)

Reviews 4-5   found almost no such objects.  Review 5's reviewer states, for its
              Findings 1, 8 and 9 in terms:  "Bears on primary-source completeness: NO."
              Those two cycles were spent almost entirely on BOOKKEEPING defects --
              page lists that disagreed with each other, four off-vocabulary table
              cells, stale self-description, a hard-stop string used as a label.
```

Reviews 4 and 5 were therefore the expensive cycles that a machine could largely have
replaced. That observation, not a general wish for more rigour, is what shapes this record.

### Root-cause analysis

**What already worked, and is preserved unchanged:**

| Instrument | Evidence that it worked |
|---|---|
| **Structure-first ordering** (§9.1.1) | Every governing object eventually found was reached through TOC / Tables Index / General Index enumeration, never through keyword search |
| **Independent completeness review** (§10.1.2) | Caught all six HIGH findings. Without it, pass 1 would have been certified with two false source-property claims |
| **Reviewer builds its own candidate list first** (§10.3) | Reviews 3, 4 and 5 each built an independent candidate-object list *before* opening the packets. That is the method that found what the packets missed |
| **Preservation of failed reviews** (§12) | Pass 1's packets and all four `FAIL` reviews are committed unaltered. The analysis above is only possible because nothing was collapsed |
| **Visual-inspection requirement** (§9.2) | Directly produced the p. 84 discovery: the defect was *invisible* to OCR, which truncates at the same point |
| **Source hierarchy and alternate-source controls** | Held throughout. No alternate-source research occurred, no Simulator Ruling was self-approved, AD&D never entered |

**What failed operationally**, classified as the assigning task requires:

| # | Failure | Concrete instance | Classification |
|---|---|---|---|
| 1 | A search that failed to reveal something became an unsupported absence claim | Pass 1: *"RC states no consequence for having no light"* (RC does, p. 150) and *"no light-conditioned table"* (RC has one, p. 93). Both false; both were the packet's headline conclusions | **Researcher noncompliance.** §9.5 Guardrail B already prohibited exactly this, in these words. **Also: not mechanically checkable** |
| 2 | Partial inspection became a claim that the source was exhausted | *"read ROW BY ROW"* over `Sample Skills Table` rows whose descriptions sit on an unrenderable page (review 4 F2); *"All pages cited were ultimately obtained as images"* — false as to p. 84 (review 4 F1) | **Insufficiently explicit rule.** §9.3 required a checklist but nothing prohibited completeness *wording* unsupported by it. **Plus not mechanically checkable** |
| 3 | Repository ownership/dependency facts stated from memory | p. 150's conditions routed to `CHAR-011`, which `INVENTORY.md` line 90 defines as **Weapon Mastery** (review 4 F5); a second mis-routing at review 4 F13; p. 147 called *"unowned"* when `INVENTORY.md` assigns it (review 2 F7) | **Missing rule.** The protocol governs *source* research end to end and says nothing about verifying claims about *this project* |
| 4 | Indexes used as citation sources rather than enumerated as completeness instruments | Pass 1 *cited* the General Index and missed `Blindness . 150, 154` sitting in it. Pass 2 then enumerated it and reached p. 150, p. 149, `Rations`, `Dehydration`, `Starvation` | **Precedent not elevated.** `P-001` recorded this after `CLUSTER-003` and was explicitly left `NOT YET ELEVATED`, so it bound nobody |
| 5 | Inaccessible / partially rendered material not treated as a hard stop | RC p. 84 renders columns 2–3 blank at every size in the project's scan, with HTTP 200 and full payloads. Both packets presented it as inspected and recorded no access limitation (review 4 F1) | **Researcher noncompliance.** §9.2's `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED` already covered it. **Plus a genuine gap:** nothing said HTTP success is not proof of visibility, or that a second digitisation is still primary access |
| 6 | Required vocabulary and checklists regressed although they already existed | Four confidence cells off §6 vocabulary (review 5 F8); `INTERNAL SOURCE CONFLICT REQUIRES REVIEW` used as a bare inline label beside a ready recommendation (review 4 F6); three mutually inconsistent coverage lists across three passes (review 4 F7, review 5 F1); a `BLOCKED` closure item in a packet recommending `EVIDENCE READY FOR HUMAN REVIEW` (review 2 F12) | **Protocol requirements that cannot currently be mechanically checked.** Every one is a deterministic, machine-decidable property that was instead checked by hand, repeatedly, by expensive reviewers |

### What this implies

Failures 1, 2 and 5 are noncompliance with rules that were already explicit and already
correct. **Making `DEC-0010` longer would not have prevented them.** A researcher who
skipped an explicit prohibition will skip a more emphatic restatement of it.

Failures 2, 5 and 6 share a property that *is* actionable: each is a **structurally
verifiable** claim. Whether every page carrying an evidence row appears on a
visual-inspection list is arithmetic. Whether a confidence cell holds one of five strings
is a set membership test. Whether a packet recommends `EVIDENCE READY` while containing a
`BLOCKED` closure item is one grep. Those were checked by reviewers because there was
nothing else to check them.

Failure 3 is the one true missing rule, and failure 4 is a precedent the project had
already learned and then declined to make binding.

## Decision

**Stage-A evidence integrity becomes structurally required and machine-verified rather
than narratively requested.** Specifically:

**1. A mandatory pre-conclusion Coverage Manifest.** Before substantive mechanical
conclusions may be written, a packet must carry a Coverage Manifest enumerating every
potentially governing object — structural units, TOC entries, Tables/Checklists Index
entries, General Index entries, specialist indexes, governing tables, governing prose,
cross-references, visually inspected pages, pages not yet visually inspected, and
repository dependencies requiring verification — each with an explicit disposition in the
established vocabulary. The required order is fixed and the reverse is prohibited:

```text
enumerate  →  inspect  →  disposition  →  falsify  →  conclude

PROHIBITED:  write conclusions, then reconstruct coverage afterward
```

**2. A Negative Claim Gate.** A material absence claim — *"RC has no…"*, *"no table
exists"*, *"no procedure exists"*, *"the source is silent"*, *"no dependency exists"* —
may not stand as an established finding without a **Negative Claim Record** stating the
claim, scope searched, structural instruments checked, indexes checked, search terms used,
cross-references followed, visual pages inspected, falsification attempt, and confidence
classification. A failed keyword or OCR search is never sufficient evidence of absence.
Where the enumeration is incomplete, the issue is classified **`NOT YET ESTABLISHED`**,
which is added to the §6 confidence vocabulary — not reported as source silence.

**3. A Repository Fact Gate.** Every claim about *this project* — ownership, landed
status, *"there is no Rule ID"*, *"this dependency is unresearched"*, *"this test already
covers X"*, *"the inventory says"*, *"the implementation contains"* — must be verified
against the current repository **during the active pass**, naming the artifact inspected
and, where practical, the identifier or section. **Model memory is not evidence.** An
unchecked claim is marked **`UNVERIFIED PROJECT FACT`** and blocks the completion gate. A
distinct repository-fact verification pass runs before independent review; it is
project-state verification, not source-completeness review.

**4. Index instruments are completeness instruments.** `P-001` is **elevated from
precedent to binding protocol** (§9.9). Where the source provides index instruments —
General Index, Tables/Checklists Index, spell index, other specialist indexes — each
applicable instrument must be enumerated and dispositioned in an auditable ledger, and
absent entries recorded. A packet may not state that an index was read in full unless its
ledger makes the enumeration auditable. The requirement is demonstrated systematic
consideration, not transcription of the whole index.

**5. An operational Primary-Source Visual Access Gate** (§9.2.1). §9.2's hard stop is
unchanged; what is added is how to discharge it. Permitted attempts: alternate rendering,
magnification or crops, local copies, and **another digitisation of the same edition** —
which remains primary-source access and does **not** trigger `DEC-0011`. Prohibited:
inferring absence from a failed render, substituting OCR as proof, and **treating HTTP
success as proof that page contents were visible**. Access failures and their resolution
are recorded whether or not a workaround succeeded.

**6. Unsupported completeness language is prohibited** (§9.10). *read in full*, *fully
inspected*, *complete*, *exhaustive*, *all relevant entries* may be used only where a
coverage instrument makes them auditable. Otherwise the packet describes exactly what was
inspected.

**7. A mandatory pre-review self-falsification pass** (§10.6), distinct from ordinary
source search and from §10's per-conclusion falsification. It covers, at minimum, negative
claims, ownership assignments, source-silence findings, dependency conclusions and scope
exclusions, recording for each: the conclusion, what evidence would falsify it, where that
evidence was sought, the result, and the disposition. A packet may not enter independent
review before this pass is complete.

**8. A Research-Start Gate** (§5.1). Before substantive research: exact card scope, known
ownership seams, authoritative primary source, required structural/index instruments,
current repository dependencies, and primary-source visual-access availability.

**9. A Research-Completion Gate** (§11.1). Before independent review may be requested,
deterministic confirmation that every manifest row is dispositioned, no visual-access
blocker remains, every material negative claim has a record, repository facts are checked,
self-falsification is complete, open questions are listed, required vocabulary is present,
and **the evidence linter passes**.

**10. Independent completeness review is unchanged in force and redefined in role.** It
remains mandatory, the original researcher still may not self-certify, and the reviewer
remains free to `FAIL` a packet. What changes is the expectation:

```text
Current failure mode:  the reviewer discovers basic uninspected governing objects
Desired role:          the reviewer adversarially challenges an already exhaustive packet
```

Nothing in this record weakens §10.1.2, and `§10.3`'s requirement that the reviewer build
its candidate list from the source rather than from the packet is retained explicitly,
because it is the instrument that actually worked.

**11. A canonical Stage-A evidence-packet template** (`docs/rules/evidence/_TEMPLATE.md`)
structurally requires the instruments above, in order, so that conformance is the default
rather than something a researcher must remember.

**12. A machine-checkable structural linter** (`scripts/lint_evidence.py`), integrated as
a gate in the canonical verification operation. It verifies **presence and structural
consistency only** — never factual correctness of research. Eighteen checks, each
traceable to a recorded `CLUSTER-004` failure (see the check-to-failure map below). No
NLP, no truth checking, no document framework.

**13. The canonical Stage-A sequence is amended** to include the new gates. `DEC-0010`
item 13's sequence is superseded *as amended* by the sequence below; `DEC-0010`'s own text
is not rewritten (`DEVELOPMENT_WORKFLOW.md` §9.4), and a forward-pointer note is added to
it. `RULE_CARD_RESEARCH_PROTOCOL.md` §3 and §9.1.1 carry this same sequence, in this same
relative order — §3 additionally showing the `EVIDENCE COLLECTION` step and the Stage-B tail,
and §9.1.1 additionally splitting the structure phase into its TOC/Tables-Index and
governing-object-inventory steps, exactly as both did before this amendment:

```text
RESEARCH-START GATE                          ◄── §5.1        NEW
        ↓
PRIMARY-SOURCE ACQUISITION                   ◄── §4
        ↓
SOURCE-STRUCTURE / FINDING-AID REVIEW        ◄── §9.1.1
        ↓
INDEX-INSTRUMENT ENUMERATION                 ◄── §9.9        NEW (elevates P-001)
        ↓
COVERAGE MANIFEST                            ◄── §9.3.1      NEW
        ↓
OBJECT / TABLE COMPLETENESS AUDIT            ◄── §9.1
        ↓
VISUAL INSPECTION OF SIGNIFICANT OBJECTS     ◄── §9.2, §9.2.1
        ↓
COMPLETE-ENTRY / DETAILED MATERIAL           ◄── §9.7
        ↓
EXPLICIT CROSS-REFERENCES                    ◄── §9.1 class G
        ↓
WHOLE-SOURCE CROSS-REFERENCE SEARCH          ◄── §9
        ↓
FALSIFICATION / CHALLENGE PASS               ◄── §10
        ↓
NEGATIVE CLAIM LEDGER                        ◄── §10.4       NEW
        ↓
REPOSITORY-FACT VERIFICATION PASS            ◄── §10.5       NEW
        ↓
OPEN-QUESTION CLOSURE GATE                   ◄── §10.2
        ↓
PRE-REVIEW SELF-FALSIFICATION PASS           ◄── §10.6       NEW
        ↓
ADVERSARIAL SELF-REVIEW                      ◄── §10.1.1
        ↓
RESEARCH-COMPLETION GATE (linter passes)     ◄── §11.1       NEW
        ↓
INDEPENDENT COMPLETENESS REVIEW              ◄── §10.1.2 hard gate; not the researcher
        ↓
HUMAN EVIDENCE REVIEW                        ◄── §11 hard gate
```

**14. Stage-A research freeze.** No new Stage-A research is authorized until this
remediation is accepted by the human project owner. Already-certified evidence continues
through later governance stages; in particular the authorized `EXP-006` Stage B is **not**
invalidated by this record.

### Check-to-failure map

Every linter check answers *"would this have prevented or cheaply detected an actual
`CLUSTER-004` failure?"* A check that could not answer yes was not added.

| Check | What it verifies | The recorded failure it catches |
|---|---|---|
| `E001` | Required instrument sections exist | Failures 1–6 structurally; pass 1 had no manifest, no negative-claim ledger, no repository-fact section |
| `E002` | `PACKET-STATUS` ledger present, keys complete | New instrument; makes `E003`–`E018` decidable |
| `E003` | Recommendation is exactly one of §11's two strings | Review 2 F12 vicinity |
| `E004` | Review status uses §10.1.2 vocabulary; no self-certification | §10.1.2's prohibited outputs |
| `E005` | `COVERAGE-LEDGER` present and parseable | Review 4 F7: three mutually inconsistent coverage lists |
| **`E006`** | **Every page carrying an evidence row is `IMAGE-VERIFIED` or `ACCESS-BLOCKED`** | **Review 4 F1 and F7; review 5 F1 — p. 84 carried evidence row E-43 and appeared on no list. Survived three passes and two reviews** |
| `E007` | No page is both `IMAGE-VERIFIED` and `LOCATOR-ONLY` | Review 3 F6: the image/locator split was inaccurate |
| **`E008`** | **An `ACCESS-BLOCKED` page forces the visual-access stop and forbids `EVIDENCE READY`** | **Review 4 F1 (HIGH) — p. 84 unrenderable, presented as inspected, no limitation recorded, packet recommended ready** |
| **`E009`** | **A `BLOCKED` closure item forbids `EVIDENCE READY`** | **Review 2 F12 (HIGH) — `ENC-005` pass 2 did exactly this** |
| `E010` | Negative Claim Ledger carries records with all nine fields, or explicit `NONE` | Failure 1 |
| **`E011`** | **Absence stated in prose with no Negative Claim Record behind it** | **Pass 1's two false headline claims — the defect that caused the first `FAIL`** |
| `E012` | Completeness wording requires the enumeration instruments | Failure 2; review 4 F2 |
| `E013` | Every evidence-map Confidence cell is §6 vocabulary | Review 5 F8 |
| `E014` | Every closure disposition is §10.2 vocabulary | §10.2 compliance, checked by hand in reviews 4 and 5 |
| `E015` | A §17 hard-stop body never appears as a bare inline label | Review 4 F6, which review 3 had already raised and only one of two packets fixed |
| **`E016`** | **Repository-fact rows exist or explicit `NONE`; `UNVERIFIED PROJECT FACT` blocks ready** | **Review 4 F5 and F13 — `CHAR-011` named as owner of p. 150's conditions without opening `INVENTORY.md`** |
| `E017` | `FALSIFICATION-RECORD` blocks exist with all five fields | §10 compliance; failure 1's missing falsification |
| `E018` | Self-falsification and repository-fact passes are `COMPLETE` before ready | Gate 9's enforcement |

**Failures this record does not claim to catch mechanically**, stated plainly rather than
overclaimed: stale self-description (review 5 F9), an elision inside a verbatim quotation
(review 2 F15, review 3 F14), a governing object nobody enumerated, and any judgement
about whether research is *correct*. Those remain the independent reviewer's and the human
owner's work — which is the point of redefining the reviewer's role rather than replacing
it.

## Rationale

`DEC-0009` fixed synthesizing before evidence closed. `DEC-0010` fixed believing evidence
had closed when a class of object had never been opened. The failure this record addresses
is narrower and more embarrassing: **the protocol's own requirements were already correct,
and were not followed** — and the only thing standing between a non-conforming packet and
human review was an expensive human-or-model reviewer reading tens of thousands of words
to notice that a page number was missing from a list.

Three design choices follow from that:

1. **Prefer structure over exhortation.** A template that has a Negative Claim Ledger
   section makes the omission visible; a paragraph asking researchers to be careful about
   absence claims demonstrably did not.
2. **Automate only what is decidable.** The linter makes no attempt to judge research. It
   checks arithmetic, set membership and string presence — exactly the class of defect that
   consumed reviews 4 and 5.
3. **Do not weaken the gate that worked.** Independent review stays mandatory and stays
   able to `FAIL`. The intent is to raise the floor of what reaches it, so that a reviewer
   spends its effort adversarially challenging an exhaustive packet instead of discovering
   that p. 93 was never opened.

The cost is one new gate in the verification path and one template to fill in. The
expected saving is three of the five review cycles `CLUSTER-004` needed. If the next
cluster still needs two independent reviews, this record has paid for itself; if it needs
four, the diagnosis was wrong and should be revisited rather than reinforced.

## Consequences

1. `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` gains §5.1 (Research-Start Gate), §9.2.1
   (visual-access operations), §9.3.1 (Coverage Manifest and required order), §9.9 (index
   instruments, elevating `P-001`), §9.10 (prohibited completeness language), §10.4
   (Negative Claim Gate), §10.5 (Repository Fact Gate), §10.6 (pre-review
   self-falsification), §10.1.3 (independent reviewer's redefined role), §11.1
   (Research-Completion Gate), §11.2 (required template), one added §6 confidence label
   (`NOT YET ESTABLISHED`) and one repository-fact label, two added §17 hard stops, and the
   amended Stage-A sequence in §3 and §9.1.1.
2. `AGENTS.md` §10 gains the binding summary of the new gates. It is a protected document
   (§12); this edit was performed under explicit human direction in the assigning task,
   which §12 requires.
3. `docs/rules/evidence/_TEMPLATE.md` is created as the canonical Stage-A packet template.
4. `scripts/lint_evidence.py` is created and added to `scripts/verify.py` as an
   independently reported gate; `docs/technical/TOOLCHAIN_AND_CI.md` §8–§9 is updated so
   the documented gate list matches the implemented one.
5. `tests/tooling/test_lint_evidence.py` tests the linter itself. `pyproject.toml` adds
   `scripts` to pytest's `pythonpath` so the tool is importable under test.
6. `docs/rules/RESEARCH_PROCESS_PRECEDENTS.md` records `P-001` as **ELEVATED** by this
   record. `P-002` remains recorded and un-elevated; its general lesson — that a negative
   finding must rest on structural inspection rather than a keyword sweep — is now binding
   through §10.4 for primary-source claims, but its alternate-source front-matter
   requirement is not elevated here, because alternate-source research was outside this
   task's authorization.
7. **Grandfathering is explicit and narrow.** The twelve Stage-A packets that exist today
   are exempt from the linter by name, listed in `scripts/lint_evidence.py`'s
   `GRANDFATHERED` frozenset and pinned by a test. They were researched, reviewed and — for
   `CLUSTER-004` — independently certified under the protocol as it then stood; retro-fitting
   the new ledgers to them would rewrite accepted evidence rather than improve it. The list
   is closed: a packet written after this record is never added to it. Reviewer artifacts
   (completeness reviews, audits, gap-research records) are not Stage-A packets and are not
   linted.
8. Stage A gains one template and one gate. Reviews are expected to get *cheaper*, not
   more numerous; the target shape is `research → self-falsification → one independent
   review → human evidence review`, with a second independent review exceptional.
9. `CLUSTER-004`'s five-review history is preserved unaltered and is cited as motivating
   evidence. No prior `FAIL` is retroactively relabelled.
10. No production simulator code, Rule Card, or rules test is created or modified by this
    record. It changes the research process and its tooling only.
11. The Stage-A research freeze in Decision item 14 remains in force until a human project
    owner accepts this remediation.

## Supersedes

None. This record **amends** `DEC-0009`'s and `DEC-0010`'s Stage-A process by adding
required steps, and supersedes `DEC-0010` item 13's Stage-A sequence *as amended* by
Decision item 13 above. `DEC-0009`, `DEC-0010` and `DEC-0011` all remain `Approved` and in
force; their historical text is not rewritten to imply they ever contained these
requirements.

## Superseded By

None.
