# `CLUSTER-004` — Independent Primary-Source Completeness Review, Pass 5

```text
PROTOCOL           RULE_CARD_RESEARCH_PROTOCOL.md §10.1.2 (who) / §10.3 (method)
                   DEC-0010 items 5, 7, 10, 11, 14, 15, 16, 17, 18
REVIEWER           Independent reviewer context.  Did NOT conduct the evidence
                   collection being certified, and did not participate in
                   reviews 1, 2, 3 or 4.
PACKETS REVIEWED   docs/rules/evidence/EXP-006-evidence-remediated.md   (pass 5)
                   docs/rules/evidence/ENC-005-evidence-remediated.md   (pass 5)
PRIOR REVIEWS      pass 1  FAIL / FAIL   CLUSTER-004-stage-a-completeness-review.md
                   pass 2  FAIL / FAIL   CLUSTER-004-stage-a-completeness-review-2.md
                   pass 3  FAIL / FAIL   CLUSTER-004-stage-a-completeness-review-3.md
                   pass 4  FAIL / FAIL   CLUSTER-004-stage-a-completeness-review-4.md
PRIMARY SOURCE     D&D Rules Cyclopedia (TSR 1071)
                   PRIMARY scan  iiif.archive.org/iiif/TSR1071TheDDRulesCyclopedia$<leaf>
                   SECOND  scan  iiif.archive.org/iiif/rules-cyclopedia$<leaf>
```

## Verdicts

```text
EXP-006   PRIMARY-SOURCE COMPLETENESS: PASS

ENC-005   PRIMARY-SOURCE COMPLETENESS: PASS
```

**Both `HIGH` findings that produced the pass-4 `FAIL` are discharged, and I verified the
discharge against the printed pages myself rather than against the packets' account of
them.** RC p. 84 is genuinely blank in columns 2–3 in the primary scan and genuinely
complete in the second scan; I opened both. All six of the entries pass 5 transcribes
from that page are verbatim exact; the two remaining blanket-exclusion rows on the
`Sample Skills Table` are now backed by an inspection that could actually be performed.

**I have eleven findings. Every one is `MED` or `LOW`, and not one of them bears on
primary-source completeness.** I state that explicitly for each. No governing object is
left uninspected; no inspection claim in either packet is false; no source-property claim
I could test is unsupported; the §9.3 instrument is present and accurate in both packets;
the §10.2.1 reconciliation table is present in both; there is no `BLOCKED` row and no §17
conflict in either. Findings 1–11 are accuracy, hygiene and reporting defects that the
human reviewer should see, and that a Stage-B agent should not inherit silently — but
they are not completeness defects, and I do not fail either card for them.

I also **withdraw one of review 4's own findings** (its Finding 14) on source evidence:
see §5 below.

---

## 1. Method

Per §10.3 I built my candidate list **before opening either packet**, from:

- RC Table of Contents, pp. 2–3 (leaf 1, leaf 2), read in full;
- `Index to Tables and Checklists`, p. 301 (leaf 300), read entry by entry;
- `General Index`, pp. 302–304 (leaf 301–303), read entry by entry;
- `docs/rules/INVENTORY.md`, in full, including the Chapter 13 Coverage table and the
  Major Human Decisions list;
- `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` §6, §9.1–§9.8, §10–§10.3, §11, §17;
- `docs/decisions/DEC-0010-primary-source-completeness-audit.md`; `AGENTS.md` §10.

Only after that list was fixed did I open the packets.

Two targeting rules were given to me and I followed both:

1. **Spot-check cited pages for defective derivatives.** I opened **eleven** RC pages as
   images: pp. 2, 3, 69, 85, 86, 88, 97, 98, 99, 100, 104, 149, 301, 302, 303, 304, plus
   p. 84 in **both** renditions. Only p. 84 is defective. Anomalous JPEG payload size is
   a usable smell test — the defective leaf 83 is 135,909 bytes against a 500–700 KB norm
   — and I used it to select which pages to open; nothing else in either packet's cited
   range is anomalously small in a way the image does not explain.
2. **Verify every project-fact against the actual file.** I opened `INVENTORY.md`,
   `CLUSTER-003-equipped-dungeon-movement.md` and `CLUSTER-004-BOUNDARY-CORRECTION.md`
   rather than accepting any assertion about them. **Both of pass 5's owner-ID
   corrections are correct, and the `CLUSTER-003` open-question citation is correct to
   the item number.** Details in §5.

I also checked the packets for the encoding damage the direction warned about
(`grep` for UTF-8 mojibake sequences, U+FFFD replacement characters, code-fence parity,
heading counts, and a byte-level head of each file). **Both files are clean**: zero
mojibake, zero replacement characters, balanced fences (60 and 36), em-dashes and curly
quotes render correctly. The repair held.

---

## 2. My independent candidate list, built before reading the packets

### 2.1 `EXP-006` — Light & Exploration Resources

| # | Candidate object | Route to it | Disposition after checking the packets |
|---|---|---|---|
| C1 | `Adventuring Gear Table` p. 69 and the Ch. 4 descriptions pp. 68–70 | TOC Ch. 4; p. 301 index | **Covered.** I read the p. 69 image myself and verified E-23–E-26, E-28, E-29, E-31 verbatim (§5) |
| C2 | `Torch . 62, 66, 69, 70` — the p. 62 / p. 66 limbs | General Index | **Covered**, routed `CHAR-004` |
| C3 | `Oil . 62, 65, 69` | General Index | **Covered**, routed `CHAR-004`; E-29 verified exact |
| C4 | `Rations . 69`; `Food . 89, 121, 125` | General Index | **Covered** (§5.6); the three `Food` limbs routed away |
| C5 | **No `Light`, `Lantern`, `Tinderbox` or `Flask` entry exists in the General Index** | pp. 302–304, read entry by entry | **Independently confirmed.** The packet's §3.3 negative is an accurate statement about the instrument |
| C6 | `Infravision . 24, 25` | General Index | **Covered**, routed `CHAR-009`; correct owner per `INVENTORY.md` |
| C7 | `Blindness . 150, 154`; `Dehydration . 150`; `Starvation . 150`; `Invisibility`/`Sleep`/`Stunning`/`Paralysis`/`Prone character . 150` | General Index | **Covered** (§5.1, §5.4), correctly not absorbed, and the p. 150 owner ID is now correct (Finding-free; see §5) |
| C8 | `Timekeeping . 149`; `Record keeping . 148, 149`; `Timetrack Table . 149` | p. 301 index; General Index | **Covered** (§5.5). I read p. 149 and verified E-19–E-22 and the table's four row lengths |
| C9 | `Encounter Distances Table . 93` and the p. 92 surprise gate | p. 301 index | **Covered** (§5.2, E-11a, E-11b) |
| C10 | `Attack Roll Modifiers Table . 108`; `Target Cover Table . 108` | p. 301 index | **Covered** (§5.9), routed, **not adjudicated** — correct |
| C11 | Ch. 5 `Sample Skills Table . 82` and the skill descriptions pp. 83–86 | p. 301 index | **Now covered in full.** p. 84 obtained from the second scan; all six entries verified exact by me |
| C12 | `Oil of darkness` / `moonlight` / `sunlight . 146`; **`Dwarven lens . 146`**; `Lightship . 146` | General Index | Oils covered and routed. **`Dwarven lens` not named**, and the chapter attribution is wrong — Finding 4 (LOW–MED) |
| C13 | **`Index to Spells`, p. 300** — the finding aid that lists `light` / `continual light` / `darkness` by name | TOC p. 3: *"Appendix 4: Indices … 300 / Index to Spells … 300"* | **Not enumerated**, and §3.1/§9.1 mis-state Appendix 4 as pp. 301–304 — Finding 3 (LOW–MED). Second consecutive miss |
| C14 | `Clerics and the Create Food Spell Table . 125` | p. 301 index | Dispositioned inside §3.3's `Food` row; **absent from §3.2's index table and §9.2's Guardrail-C attestation** — Finding 11 (LOW) |
| C15 | p. 70 `Shoes` — a purchased item RC attaches a dungeon consequence to | p. 69 table row; p. 70 description | **Not recorded** (third flag) — Finding 11 (LOW) |
| C16 | p. 69 `Rope`, `Iron spikes`, `Pole`, `Grappling hook`, `Garlic`, `Holy water`, `Wolfsbane` | p. 69 image | Checked by me. None is a light source or a consumable with a printed duration; all are durable gear or anti-undead items belonging to `CHAR-004`/`TREAS-*`. **No finding** |
| C17 | `Fire . 116`; `Fatigue . 119`; `Forced Marches . 121` | General Index; p. 301 index | Siege / War Machine. Excluded with reasons. **No finding** |
| C18 | `Encumbrance . 63, 88`; Ch. 6 travel tables pp. 87–90 | General Index; p. 301 index | **Covered**, routed `CHAR-004`/`CHAR-005` or gated on the Wilderness decision |
| C19 | RC p. 149 `Placement During Encounters` / `Placement of figurines . 149` | General Index | **Not named by either packet** — Finding 10 (LOW). It carries no mechanic |
| C20 | `Nocturnal . 153` — monster activity cycles as a light-adjacent field | General Index | Checked. It is a `How to Read Monster Descriptions` field, `MON-003`'s, with no light mechanic. **No finding** |

### 2.2 `ENC-005` — Retreat, Pursuit & Evasion (underworld)

| # | Candidate object | Route to it | Disposition after checking the packets |
|---|---|---|---|
| D1 | `Evasion Checklist` + `Evasion Table`, p. 99 | p. 301 index | **Covered.** I read the p. 99 image and verified both transcriptions verbatim, **including both printed defects** |
| D2 | `Evasion . 91, 98-100`; `Pursuit . 98-100` | General Index | **Covered**; the p. 91 limb is the Game Day hook (N-2) |
| D3 | `Ship Evasion Table . 100` / `Evasion at Sea` — **and p. 100 col. 3's opposed-`Piloting` resolution** | p. 301 index; p. 100 image | Column excluded as naval. The `Piloting` hook is **still unenumerated** (third flag) — Finding 6 (LOW) |
| D4 | `Combat Maneuvers Table . 104`; `Retreat maneuver . 104`; `Fighting withdrawal maneuver . 104` | p. 301 index; General Index | **Covered** (§5.6). I read p. 104 and confirmed **both** maneuvers carry the identical running-speed bridge (N-23) |
| D5 | `Exhaustion . 88`; `Running speed . 88, 103`; `Encounter speed . 88, 95, 100, 103`; `Normal speed . 88, 103` | General Index | **Covered** (§5.5a). I read p. 88 and verified N-27a–N-27d verbatim |
| D6 | `Surprise . 92, 93`; `Encounter Distances Table . 93`; `Encounter Checklist . 93` | p. 301 index | **Covered** (N-4a/b/c), routed `ENC-001`/`ENC-002` |
| D7 | `Morale . 102, 103, 119`; `Initiative . 102`; `Combat Sequence Checklist . 102`; `Monster movement rate . 88, 152` | General Index; p. 301 index | **Covered**, routed `ENC-004` / `COMBAT-006` / `MON-003` |
| D8 | `Terrain . 119, 153`; `Charge . 154`; `Terrain Effects on Movement . 88` | General Index; p. 301 index | **Covered**, excluded **by name**, explicitly not imported |
| D9 | `Move silently . 22` / `Hide in shadows . 22` | General Index | Enumerated, and the owner ID is **now correct** — `CHAR-010` (§5) |
| D10 | Ch. 5 `Caving`, `Endurance`, `Tracking`, `Stealth`, and the p. 84 rows `Mapping/Cartography`, `Navigation`, `Nature Lore`, `Mountaineering` | p. 301 index `Sample Skills Table . 82` | **Now covered.** N-38 / N-39 are verbatim exact and the N-38 inference is sound (§5) |
| D11 | `Lost . 89` (wilderness) against p. 100's dungeon lost-condition | General Index | **Covered** (N-22), restoration verified exact |
| D12 | p. 99 col. 3's **spell** escape route (`teleport`, `pass wall`, `dispel magic`, `wall of iron`) | p. 99 image | Present only inside the verbatim checklist; **no evidence row, no `MAGIC-*` routing line** — Finding 7 (LOW) |
| D13 | p. 99 col. 1's closing sentence on one-sided surprise | p. 99 image | **Still elided from N-36** (third flag) — Finding 7 (LOW) |
| D14 | `Castle Reactions Table . 99`; `Balancing Encounters Checklist . 101`; wilderness/city subtables pp. 96–98 | p. 301 index | **Covered**, excluded with reasons. I read pp. 97 and 98 and confirmed the exclusions |
| D15 | p. 92 `Chance of Encounter Table`; `Wandering monsters check . 91` | p. 301 index | **Covered**, routed. Confirmed light-free |
| D16 | p. 149 `Placement During Encounters` — the position-tracking N-32 delegates to the DM | General Index `Placement of figurines . 149` | **Not named** — Finding 10 (LOW). RC supplies miniatures and chalk, not a mechanic |

---

## 3. Findings

### Finding 1 — MED — both cards — the coverage lists are still not mutually consistent

**`EXP-006` §2's `IMAGE-VERIFIED` list still omits pp. 84, 85 and 86**, and still scopes
itself to *"Every page that carries an evidence row (`E-1` … `E-40`)"* — the packet now
runs to **E-49**. §9.1 does list pp. 84, 85 and 86, correctly.

```text
§2   IMAGE-VERIFIED   68 69 70 81 82 83 88 91 92 93 98 99 100 104 108
                      149 150 154 301 302 303 304
§9.1 VISUALLY INSP.   the same, PLUS 84, 85, 86
```

`ENC-005` has the mirror defect in the other direction: §3.2 attests
`Combat Sequence Checklist` (**p. 102**) as `OPENED` **and** `VISUALLY INSPECTED`, and
§9.1's structural-units list does not contain p. 102.

Review 4's remedy *"Complete `EXP-006` §2's lists"* is **not discharged**, and pass 5
added nothing to §2 while adding six evidence rows to p. 84.

**Bears on primary-source completeness: NO.** Every discrepancy runs in the
**under-claiming** direction. No page is asserted inspected that was not; the error is
that inspected pages are missing from a supplementary list. §9.1 — which is the §9.3
instrument the protocol actually requires, and the one a future auditor will use — is
accurate in both packets, and I verified pp. 84, 85, 86 and 102's neighbours myself.
An under-claim cannot hide an uninspected object, which is what this gate exists to
catch.

---

### Finding 2 — MED — `EXP-006` / `ENC-005` — `Mapping (Cartography)` is quoted at one sentence of four, and the `EXP-003` parallel review 4 asked to be *reported* is still unreported

E-46 and N-38 both quote exactly one sentence of the p. 84 entry. The complete entry,
which I transcribed from the second scan, is:

> *"Mapping (Cartography): If a character has this skill, he can understand and make maps
> even if he cannot read and write. **The skill allows the character to comprehend simple
> maps without a skill roll; the character should make skill rolls to interpret or draft
> complicated layouts or to map an area by memory.** A character does not have to have
> this skill in order to map a dungeon as the characters explore it. A character who can
> map but not read obviously cannot understand the words on a map."*

The bolded sentence is the one neither packet carries, and it is the one that matters
outside this cluster: landed, `APPROVED` **`EXP-003`** states *"No separate mapping
mechanic, time cost, roll, or failure state exists or is to be created"*
(`INVENTORY.md`, `EXP-003` row). RC does attach skill rolls to *some* mapping work. That
is a §9.1 **class-I parallel presentation** against a landed card, and review 4's item 3
and its §7 remedy both asked for it to be **reported, not adjudicated**. It is not
reported. `EXP-006` §3.3's `Mapping` row is also unchanged from pass 4:

```text
| Mapping | 5, 148, 256, 257 | yes | Player-facing advice + DM prep.
                                     No executable mechanic; no light input |
```

**Bears on primary-source completeness: NO**, and I considered this one hardest.

- The **object is inspected.** p. 84 is now open and the entry is on the page image the
  packets cite; this is an incomplete transcription, not an uninspected object, and the
  full text is now on the record above.
- The **inference the packets draw is sound and unaffected.** E-46/N-38 conclude that
  N-22's *"had mapped"* branch creates no `CHAR-012` dependency. RC's fourth sentence
  says that in terms — *a character does not have to have this skill in order to map a
  dungeon as the characters explore it* — and the omitted sentence is about
  *interpreting complicated layouts* and *mapping from memory*, neither of which is the
  as-you-explore case N-22 turns on. The omitted text does not falsify any conclusion
  either packet reaches.
- §3.3's row is **scoped to the General Index entry's own four pages** (5, 148, 256,
  257). I read the TOC and the index entry; those four pages genuinely carry no
  mechanic, so the row is a page-scoped research-operation disposition, not a
  source-property claim about mapping in RC — and the same packet names and quotes the
  `Mapping/Cartography` skill three sections later, so the packet as a whole does not
  assert that no mapping skill exists.

**What I nonetheless ask the human reviewer to note:** the `EXP-003` parallel should go
on the record before Stage B, because a Stage-B agent reading only E-46 would carry
forward a stronger negative than RC supports. The full sentence is supplied above so
that no further source access is needed to do it.

---

### Finding 3 — LOW–MED — `EXP-006` — source-structure errors in §3.1, and the `Index to Spells` (p. 300) still not enumerated

Checked against the printed Table of Contents, pp. 2–3, which I read in full:

```text
PACKET §3.1                       RC's OWN TOC
Ch. 6  "The Adventure             Ch. 6  "Movement" ................. 87
        (land travel)" 87-90
Ch. 13 "pp. 144-155"              Ch. 13 "Dungeon Master Procedures"  143
                                  Ch. 14 "Monsters" ................. 152
                                     -> Ch. 13 is pp. 143-151
App. 4 "pp. 301-304"              Appendix 4: Indices ............... 300
                                      Index to Spells ............... 300
                                      Index to Tables and Checklists  301
                                      General Index ................. 302
```

§9.1 then records pp. 301–304 *"read in full"* under a structure that starts one page
later than the source's. The **`Index to Spells` (p. 300) is a §9.1 class-B/class-H
finding aid that is never enumerated** — the instrument that lists `light`,
`continual light` and `darkness` by name, in a packet named *Light & Exploration
Resources*. This is review 4's Finding 8, unremediated.

**Bears on primary-source completeness: NO.** The spells are out of `EXP-006`'s scope by
a stated, defensible boundary (§6.6, §7.1 route all magical light to `MAGIC-*`), the
point where a light spell's consequence actually enters this card's space is RC p. 150,
which **is** inspected and quoted (E-1), and the Ch. 13 range error over-covers rather
than under-covers — it wrongly annexes pp. 152–155 and drops p. 143, whose contents
(Ability Checks, Aging, Alignment Changes, Anti-Magic Effects) I checked against the TOC
and which carry nothing light- or resource-bearing. No governing object is missed. It is
a structure-mapping defect in the first step of the `DEC-0010` sequence, and it should be
fixed, but it hides nothing.

---

### Finding 4 — LOW–MED — `EXP-006` — RC p. 146 is Chapter 13, not Chapter 12, and the exclusion reason rests on that

§3.3 calls the three `Oil of …` relics *"**Magical** light items, Ch. 12"*, and §6.6
states they were *"opened only far enough to confirm they are **Chapter 12** magical
items and Chapter 3 spells, i.e. that they are not Chapter 4 equipment."*

Per the printed TOC: **Chapter 12 (Strongholds and Dominions) is pp. 134–142; Chapter 13
(Dungeon Master Procedures) is pp. 143–151, with `Demihuman Clan Relics` at p. 145.**
p. 146 is Chapter 13. `Dwarven lens . 146` — a General Index entry in the same cluster of
relics, and the only one whose name suggests optics — is not named at all.

**Bears on primary-source completeness: NO.** The routing survives the error intact:
they are magical relics either way, they belong to `MAGIC-*`/`TREAS-*` either way, and
`EXP-006` claims no mechanic from them. p. 146 is declared at §2 as an `OPENED VIA OCR
ONLY` locator-level read carrying no evidence row, which is the honest label for it. But
a §9.3 exclusion is only auditable if its stated reason is checkable, and this one
mis-states the source's own structure — the same class as Finding 3.

---

### Finding 5 — LOW — `EXP-006` — §6.5's blanket seam claim is falsified by the packet's own E-32

```text
§6.5   "No price, encumbrance, Coin, quantity-pricing or legality fact is restated
        or re-derived in this packet."

E-32   Waterskin: "...a liquid capacity of one quart and an ENCUMBRANCE OF 30 cn
        WHEN FILLED, 5 cn WHEN EMPTY."
```

**Bears on primary-source completeness: NO**, and it is not scope creep either. It is an
over-quotation, not an under-inspection: E-32 quotes the p. 70 description as a complete
unit (which §9.7 asks for), the encumbrance values are incidental to the sentence, the
packet uses them for nothing, and E-26 correctly routes the table's cost/`Enc` columns to
landed `CHAR-004` rather than restating them as this card's facts. The `CHAR-004` seam
holds in substance; only §6.5's absolute phrasing does not.

---

### Finding 6 — LOW — `ENC-005` — p. 100 col. 3's opposed-`Piloting` resolution is still unenumerated

I verified on the p. 100 image, col. 3:

> *"If the DM is using the optional general skills rules, he or she can roll the two
> captains' Piloting skills in competition with one another. If the evading ship's
> captain rolls his skill better, he evades pursuit; if the pursuer rolls his better, he
> is able to close at the rates described above."*

`grep Piloting ENC-005-evidence-remediated.md` returns **zero**. Review 3 item 11 and
review 4 Finding 4 both asked for it; this is the third pass in which it is absent.
(`EXP-006` does attest the `Piloting Skill: Types of Vessels Table` at §9.2.)

**Bears on primary-source completeness: NO**, and here I reach a different conclusion
from review 4, on the merits rather than by leniency. §9.1 class I governs *duplicate or
parallel presentations of the mechanic under research*. `ENC-005`'s researched
responsibility is **underworld** retreat, pursuit and evasion; a contest between two
**ship captains'** `Piloting` skills, printed under the heading `Evasion at Sea`, is not
a second presentation of that mechanic — it is the naval procedure, which the card
excludes on a source-grounded scope ground the packet states plainly and which Q1 flags
as the open card-scope decision. The column is inspected, the exclusion reason is true,
and nothing about the underworld procedure is hidden by it. The contrast with N-17a
(`Tracking` as a skill-based route to the question N-17 resolves by percentage) is real
but N-17a concerns the *same* dungeon-side question; this does not. It should still be
enumerated in one line for tidiness, and the text is supplied above.

---

### Finding 7 — LOW — `ENC-005` — step 5c's spell branch has no evidence row, and N-36's closing sentence is still elided

Two items from review 3 item 13 / review 4, both unremediated:

1. **Step 5c's spell route.** RC p. 99 col. 3 names four worked examples —
   *"a `teleport` spell to whisk the party to safety; a `pass wall` spell to get them
   somewhere inaccessible (followed by a `dispel magic` to cancel the `pass wall` so that
   the pursuers cannot follow); or a `wall of iron` spell to forestall pursuit."* The
   packet carries this only inside §5.2's verbatim checklist block and gives it no
   evidence row and no `MAGIC-*` routing line, although it routes the `oil poured to
   delay pursuit` non-mechanic from both sides (§6.2).
2. **N-36.** RC p. 99 col. 1 continues past where N-36 stops:
   *"In fact, if the surprised party didn't detect the nonsurprised party, the surprised
   party will never know that it has just been through an encounter."*

**Bears on primary-source completeness: NO.** Both texts sit on p. 99, which is inspected,
magnification-confirmed and transcribed at length; step 5c's branch is in the packet
verbatim inside the checklist; and neither omission changes a conclusion. The
elided N-36 sentence is a *strengthening* of the automatic-evasion outcome, not a
qualification of it.

---

### Finding 8 — LOW — both — four evidence-map cells do not use the §6 confidence vocabulary

§6 requires *"exactly one of"* five labels in every evidence-map row's Confidence column.
Four cells do not carry one:

```text
EXP-006 E-33a   "repository fact, not a source fact"
ENC-005 N-30a   "repository fact, not a source fact"
EXP-006 E-13a   "see below"
EXP-006 E-26    "CHAR-004 [LANDED] -- not restated as this card's fact"
```

**Bears on primary-source completeness: NO, and these are not invented confidence
labels.** None asserts a confidence level at all. E-33a and N-30a are `INVENTORY.md` /
`DEC-0008` rows explicitly flagged as **not** source facts — none of §6's five labels
fits a repository fact, and forcing one would be worse than the present wording; the
cleaner fix is to move both rows out of the evidence map into a project-facts note.
E-13a's *"see below"* resolves to §5.3, which withdraws the `NECESSARY CONSEQUENCE`
classification explicitly and correctly. **Everywhere else, both packets use §6's five
terms and §10.2's four dispositions verbatim, and I found no invented label**, including
in the qualified constructions (*"`CONFIRMED OUT OF SCOPE` for Stage A"*, Q11's split
disposition), which apply verbatim labels to stated sub-cases rather than coining new
ones.

---

### Finding 9 — LOW — both — stale self-description, throughout

Unremediated from review 4's Finding 10, plus what pass 5 added:

```text
BOTH titles     "Stage-A Evidence (Remediated, Pass 2)"     (header block says PASS 5)
BOTH §19        "subject to the mandatory §10.1.2 THIRD independent completeness
                 review"                                    (this is the FIFTH)
BOTH §19        "Pass 3 remediation of the second review's findings:"
                 -- the list that follows records NO pass-4 and NO pass-5 item, so
                    nothing in either packet states what pass 5 changed
EXP-006 §9.4    "All ten are in §8"                          (§8 carries Q1-Q13)
EXP-006 §11-18  "(12) Unresolved RC questions -- §8, Q1-Q10" (omits Q11, Q12, Q13)
EXP-006 §8      §8.2 is printed before §8.1; §5.8's evidence table is split in half by
                 an interposed prose subsection, orphaning E-36 to E-38
ENC-005 l.820   cites "§4.4's own dependency table"          (there is no §4.4; it is §7.1)
ENC-005 l.398   "whenever the OPTIONAL SYSTEM IS SWITCHED ON" (DEC-0008 already set it)
ENC-005 l.794   "the OPEN-ENDED DM adjustment"               (a conclusion §5.3a withdraws)
ENC-005         §7.2 / §8 Q2 / §18 say "FIVE" unresearched providers; §7.1 and §19
                 say SIX.  Six is correct -- I verified each against INVENTORY.md
```

**Bears on primary-source completeness: NO.** Every open question is dispositioned under
§10.2 vocabulary in the table itself, so the closure gate is satisfied and the counts are
counting errors, not hidden items. The provider count is the only one with mechanical
content and the correct figure (six) is the one §7.1's table and §19's decision question
carry. This made the review slower; it did not make it less conclusive.

---

### Finding 10 — LOW — both — RC p. 149 `Placement During Encounters` is not named, and it is what N-32 delegates to

`ENC-005` N-32 records that step 5b's *"caught"* is *"a DM-tracked positional
determination, not a roll"* — *"the DM should be keeping track of their relative
positions to determine this."* RC's only text on **how** the DM does that is on p. 149,
which I read:

> `Placement During Encounters` — *"If the DM keeps track of monster and PC locations by
> memory alone, he sometimes makes errors. Miniature figures or other items … are best
> used on a gridded playing surface to indicate distances…"* — with chalkboards as the
> alternative.

It carries the General Index entry `Placement of figurines . 149`. `EXP-006` inspects
p. 149 for Timekeeping and neither packet names this section.

**Bears on primary-source completeness: NO.** It is a tabletop aid with no die, no
input and no output — structurally identical to the `Timetrack Table`, which `EXP-006`
correctly classifies as *"PRESENTATION / TRACKING"* rather than a procedure. RC supplies
no positional measurement rule for a chase, which is exactly what N-32 says. The page is
inspected. Recording it in one line would close the loop on N-32's delegation and I
recommend it, but nothing governing is missing.

---

### Finding 11 — LOW — `EXP-006` — `Shoes` and the `Create Food` table are still outside the attestation lists

Both named by review 3 item 7 and review 4 Findings 8/9; neither actioned. `grep`
returns zero for `Shoes` and zero for `Create Food`.

- **p. 70 `Shoes`** — *"A character should have shoes if he is going to travel or explore
  dungeons; the DM might assign damage to barefoot characters walking through bad terrain
  or treacherous catacombs."* A purchased item (p. 69 table, `5 sp`) whose **absence**
  carries a dungeon consequence — the same shape as the card's other content.
- **`Clerics and the Create Food Spell Table . 125`** — a named p. 301 index object, while
  §3.2 states *"every entry on p. 301 was read and each one relevant to light,
  exploration resources, time or condition consequences is dispositioned above or in
  §9.2."*

**Bears on primary-source completeness: NO.** `Create Food` **is** dispositioned — inside
§3.3's `Food . 89, 121, 125` row, routed to `MAGIC-*` — so the object is enumerated and
only its Guardrail-C attestation line is missing; that is a placement defect, not a
coverage gap. `Shoes` is a genuine small omission on a page that is inspected and
transcribed at length, and its disposition is not in doubt (a `CHAR-004`-priced item with
a DM-discretionary damage note, adjacent to but not inside this card's
duration/consumable seam). Neither leaves a governing object unopened.

---

## 4. Review 4's remedy list, item by item

Review 4's remedies are in its §7 closing paragraph and its fourteen findings. I check
both.

### 4.1 The §7 remedy paragraph

| # | Review-4 remedy | Status | Evidence |
|---|---|---|---|
| 1 | *"Record the access limitation"* for p. 84 | **REMEDIATED** | `EXP-006` §2.2 and §11–18 (17); `ENC-005` §11–18 (17) and §9.1's p. 84 line. The account is accurate — I verified both scans independently (§5) |
| 2 | *"Obtain p. 84 from another rendition or issue the §9.2 stop"* | **REMEDIATED** | Second scan `rules-cyclopedia$83` obtained. I opened it: printed p. 84 renders complete in all three columns. Correctly framed as the same edition through a different digitisation, **not** a `DEC-0011` alternate source |
| 3 | *"Name `Mapping/Cartography`, `Navigation`, `Nature Lore` and `Mountaineering`, disposition them by inspection rather than by blanket"* | **REMEDIATED** | E-46, E-47, E-48, E-49 in `EXP-006`; N-38, N-39 in `ENC-005`. All verbatim exact against the second scan. `Hunting` (E-45) and `Lip Reading` (E-44) added beyond what was asked |
| 4 | *"Reconcile `Mapping/Cartography` against landed `EXP-003` by reporting it, not adjudicating it"* | **NOT REMEDIATED** | Finding 2. `EXP-003` appears in `EXP-006` only for movement and map scales; §3.3's `Mapping` row is unchanged; the entry is quoted at one sentence of four |
| 5 | *"Fix the two owner IDs (`CHAR-011` → the p. 150 condition set has no owner; `CHAR-010` for Move Silently)"* | **REMEDIATED — both, and both verified correct by me** | §5 below. The `CLUSTER-003` open-question citation is also correct **to the item number** |
| 6 | *"Drop the inline hard-stop label from `ENC-005`"* | **REMEDIATED** | `ENC-005`'s only occurrence of the string is now the pass-5 meta-note at §5.3a explaining the correction. Q5 and N-14 carry `RETAINED AS GENUINE SOURCE AMBIGUITY` under §10.2.2 case 3, with no stop string. `grep` confirms **no `BLOCKED` row in either packet** — every hit is meta-discussion of pass 2's removed row |
| 7 | *"Complete `EXP-006` §2's lists"* | **NOT REMEDIATED** | Finding 1 |

### 4.2 Review 4's fourteen findings

| # | Review-4 finding | Status in pass 5 |
|---|---|---|
| 1 | HIGH — p. 84 unrenderable and presented as inspected | **REMEDIATED.** Independently re-verified both ways |
| 2 | HIGH — `Sample Skills Table` blanket exclusion over an unreadable region | **REMEDIATED** as to inspection and naming. The `EXP-003` reporting tail is **not** — Finding 2 |
| 3 | MED — §9.8: `Caving` treated as *the* step-6 determination while siblings undispositioned | **REMEDIATED.** N-38 and N-39 disposition both siblings by inspection; N-39 confirms `Navigation` is the outdoor counterpart and `Caving` the underground one, which earns the principal-object claim rather than assuming it |
| 4 | MED — p. 100 col. 3's opposed-`Piloting` resolution unenumerated | **NOT REMEDIATED** — Finding 6. I disagree with its severity (see there), not with its existence |
| 5 | MED — `CHAR-011` named as owner of the p. 150 conditions | **REMEDIATED and verified** — §5 |
| 6 | MED — §17 hard-stop string used as an inline label in `ENC-005` | **REMEDIATED** |
| 7 | MED — the three coverage lists not mutually consistent | **NOT REMEDIATED** — Finding 1 |
| 8 | LOW–MED — Appendix 4 enumerated from p. 301; `Index to Spells` and `Create Food` table | **NOT REMEDIATED** — Findings 3 and 11 |
| 9 | LOW — p. 70 `Shoes` | **NOT REMEDIATED** — Finding 11 |
| 10 | LOW — stale self-description | **NOT REMEDIATED**, and extended — Finding 9 |
| 11 | LOW — open-question count stale; §5.8 table split | **NOT REMEDIATED** — Finding 9 |
| 12 | LOW — `ENC-005` leftover conditional phrasing and the `§4.4` dangling reference | **NOT REMEDIATED** — Finding 9 |
| 13 | LOW — `Move silently` routed to `CHAR-012` | **REMEDIATED and verified** — §5 |
| 14 | LOW — E-32 labelled `Waterskin/wineskin`, said to invent a second item | **CORRECTLY NOT ACTIONED — review 4's finding does not hold.** RC's own `Adventuring Gear Table` on **p. 69** prints the row *"Waterskin/wineskin — One-quart capacity; enc 30 when filled — 1 gp — 5"*, with a separate `Wine` row below it. I read the page. The packet's label is the source's own. **I withdraw this finding on behalf of the record** |

**Five of the seven §7 remedies and the two `HIGH` findings are discharged.** What is not
discharged is Finding 2's reporting tail and the accuracy/hygiene tail — Findings 1, 3,
6, 7, 9, 11 — none of which bears on completeness.

---

## 5. What I verified as CORRECT, and where I looked

§10.3 requires a reviewer who finds nothing to say what it looked for. Most of what these
packets assert is right, and I checked it against the printed pages and the actual
repository files rather than taking it on trust.

### 5.1 The p. 84 defect and its resolution — independently confirmed both ways

```text
PRIMARY scan, leaf 83 (135,909 bytes at /full/1400,/)
    Column 1 renders: Healing tail, HUNTING (truncated), and nothing else.
    The last words on the page are "In areas not normally rich in game he must make a"
    Columns 2 and 3 are BLANK.  Header and footer decoration are present.
    -> §2.2's description is EXACT, including the truncation point.

SECOND scan, rules-cyclopedia leaf 83 (713,574 bytes)
    Printed p. 84 renders COMPLETE in all three columns:
    Hunting, Intimidation, Knowledge, Labor | Language, Law and Justice, Leadership,
    Lip Reading, Magical Engineering, Mapping (Cartography), Military Tactics |
    Mimicry, Mountaineering, Muscle, Music, Mysticism, Nature Lore, Navigation,
    Persuasion (start).
    -> §2.2's resolution claim is EXACT.
```

Every pass-5 transcription from that page checks out **verbatim**:

| Row | Object | Result |
|---|---|---|
| **E-44** `Lip Reading` | p. 84 col. 2 | **Exact** — *"The distance to the target and the available light should be taken into account—the DM should apply skill roll penalties for difficult situations."* It genuinely is a fourth light-conditioned mechanic |
| **E-45** `Hunting`, in full | p. 84 col. 1 | **Exact**, all three limbs: *"In areas not normally rich in game he must make a skill roll and receive penalties to that roll (penalties determined by the DM)"*; *"he takes a **- 1** penalty for each additional person after the first he is trying to supply"*; *"He must roll each day."* The `- 1` is correctly transcribed and is **not** an error against `Survival`'s `+ 1` (p. 85) — RC really does print the two with opposite signs |
| **E-46 / N-38** `Mapping (Cartography)` | p. 84 col. 2 | **The quoted sentence is exact.** The entry is longer — Finding 2 |
| **E-47 / N-39** `Navigation` | p. 84 col. 3 | **Exact** — *"By taking directions from the position of the sun and the stars (or of whatever atmospheric phenomena are appropriate in your campaign), the character can always know roughly where he is."* |
| **E-48** `Nature Lore` | p. 84 col. 3 | **Exact**, including the seven-terrain list, *"edible and poisonous plants"*, the `- 2` in home territory and the *"up to a + 4"* ceiling |
| **E-49** `Mountaineering` | p. 84 col. 3 | **Exact** — *"This does not replace a thief's special climbing ability; it is the skill of mountain-climbing with the use of ropes, pitons, and other climbing gear."* |

**I also read the fourteen p. 84 entries neither packet names** — Intimidation,
Knowledge, Labor, Language, Law and Justice, Leadership, Magical Engineering, Mimicry,
Muscle, Music, Mysticism, Persuasion and the rest — specifically looking for a governing
object either card had swept up in a blanket exclusion. **There is none.** The two worth
recording as checked are `Mimicry` (signalling that does not tip off *"enemy listeners"*
— stealth-adjacent, but attached to no evasion mechanic and owned by `ENC-002`/
`CHAR-012`) and `Muscle` (*"a + 2 bonus on Strength rolls for tasks such as opening
doors"* — `EXP-005`'s, which both packets route p. 147 to). Neither belongs to `EXP-006`
or `ENC-005`.

### 5.2 Is N-38's dependency-closure inference sound? — **Yes**

N-38 concludes that because RC states *"a character does not have to have this skill in
order to map a dungeon as the characters explore it"*, N-22's *"already knew or had
mapped"* branch creates **no `CHAR-012` dependency**, leaving `Caving` (N-28) as the
card's only one.

The inference is **sound**. N-22's condition is about whether the party's flight crossed
into territory it had *previously mapped while exploring* — which is exactly the case
RC's sentence exempts from the skill. The sentences I found omitted (Finding 2) attach
rolls to *interpreting complicated layouts* and *mapping from memory*, neither of which
is the as-you-explore case, so they do not reopen the dependency. §7.1's step-6 row and
§19's six-counterparty figure are consistent with the conclusion.

### 5.3 Both owner-ID corrections — verified against the actual files

| Claim | File checked | Result |
|---|---|---|
| `EXP-006` §3.3 / §9.3: p. 150's `Invisibility` / `Sleep` / `Stunning` / `Paralysis` / `Prone` route to **`COMBAT-*`**, and *"the general status-condition responsibility has **no Rule ID** in `INVENTORY.md`"* | `INVENTORY.md`, Chapter 13 Coverage table, `Special character conditions` row | **Correct.** That row assigns these to **`COMBAT-003`** *"for now"* and flags the responsibility as *"a plausible future split into its own entry"* — i.e. no dedicated status-condition ID exists. `CHAR-011` (Weapon Mastery) is gone from both places |
| *"…exactly as **`CLUSTER-003`'s open question 8** records"* | `docs/rules/clusters/CLUSTER-003-equipped-dungeon-movement.md`, item 8 | **Correct to the item number, and near-verbatim.** Item 8 reads: *"Do the blindness / stunning / starvation movement multipliers (RC p. 150) belong to `CHAR-005` or to a status-condition responsibility `INVENTORY.md` does not yet contain? **No Rule ID was invented.**"* (Note this is `CLUSTER-003`'s **own** numbering — `INVENTORY.md`'s item 8 is the unrelated `CHAR-004` weapon-legality question. The packet cites the cluster document, and it cites it right) |
| `ENC-005` §3.3: `Move silently . 22` → **`CHAR-010`**, *"not `CHAR-012`"* | `INVENTORY.md`, `CHAR-010` and `CHAR-009` rows | **Correct.** `CHAR-010`'s title enumerates *"Move Silently"* by name, and `CHAR-009`'s row states *"Thief's own abilities are owned by `CHAR-010` instead"* |

**Both of the two errors the direction told me to expect in this class are genuinely
fixed, and pass 5 introduced no new project-fact claim that I could falsify.** I
re-checked the standing ones as well: `BOUNDARY-CORRECTION` §6 item 8 (*"Starvation has
no Rule ID anywhere in the inventory"*) — **correct, still true**; §6 item 2
(*"newly discovered RC optional system — none found"*) — **correct, and correctly not
reopened by General Skills**, which carries a registered `DEC-0008` selection;
`INVENTORY.md`'s `CHAR-012` row — **`"RC Optional/Additional system → Project-Selected:
REQUIRED (DEC-0008)"`, verbatim**, so E-33a and N-30a stand.

### 5.4 Primary source read from page images by me

| Claim | Object | Result |
|---|---|---|
| E-23–E-25 rations: *"about 21 meals"*; standard *"spoil overnight"* in a dungeon; iron *"two months (eight weeks) … up to a week in bad conditions"* | p. 69 (leaf 68) | **All exact** |
| E-28 Lantern (30′, one flask, *"four hours (24 turns)"*, shuttered), E-29 Oil (*"poured out and ignited to delay pursuit"*), E-31 Mirror (*"The area must be lit"*, `−2`, no shield) | p. 69 | **All exact** |
| E-26 table rows `Rations, iron 15 gp / 70 cn`, `Rations, standard 5 gp / 200 cn` | p. 69 | **Exact**, and correctly deferred to `CHAR-004` rather than claimed |
| E-42 `Survival` — six terrains with **no dungeon option**, automatic foraging in fertile areas, `+ 1` per additional person, *"He must roll each day"* | p. 85 (leaf 84) | **Exact.** Q11's wilderness/dungeon split is source-grounded |
| E-43 / N-37 `Tracking` (*"age of the tracks, type of terrain, number of tracks"*) | p. 85 | **Exact** |
| E-41 *"not being able to see … + 5, + 10, or even + 15"*, and E-34/N-29's *"A natural roll of 1 on 1d20 is an automatic success, just as a roll of 20 is an automatic failure"* | p. 86 (leaf 85) | **Exact.** Also correct that it is **not** a fourth value in the `−6`/`−4` conflict: it modifies a roll-under **skill** roll |
| N-37's p. 86 limb — *"there are no tracks to find … the other characters can't make their own Tracking skill rolls here, except to confirm the fact that there are no tracks"* | p. 86 | **Exact** |
| N-27a the 30-round maximum and the RC-named `Endurance` exception; N-27b the three-turn rest; **N-27c *"He drops to encounter speed"***; N-27d `+2` to hit and *"subtract 2 from all attack **damage** rolls"* | p. 88 (leaf 87) | **All exact.** Q13's p. 88-damage / p. 108-attack tension is real and correctly reported, not adjudicated |
| `Evasion Checklist` verbatim, **including step 2's own *"go to Step 2"* self-loop (N-5)** | p. 99 (leaf 98) | **Exact, character for character.** The defect is printed |
| `Evasion Table` verbatim, including `Pursuers have scouts in place −15%`, **against the prose's *"a - 10% penalty is applied to the evasion chance"* (N-14)** | p. 99 | **Both exact, both printed, adjacent on the same page.** Correctly `RETAINED AS GENUINE SOURCE AMBIGUITY`, correctly unadjudicated |
| N-10 the `d100` roll-under worked example (*"on a 01-70 … on a 71-00"*), N-11 the 5% floor, N-12 party splitting, N-13 the symmetric ±25%, N-32 catch-up, N-33 the obstacle branch and *"might choose to surrender instead"*, N-34 *"…as noted in the Evasion Table"*, N-35 *"closing doors behind them"*, N-17 the second roll and *"the pursuers fail to follow their tracks"* | p. 99 | **All exact** |
| N-19 dropped goods **with** its *"if he or she feels…"* gate; N-20 `Regain Bearings`; N-21 full running speed every chase round; **N-22 *"…they're fine"***; the p. 100 column classification | p. 100 (leaf 99) | **All exact.** The col. 1 / col. 1–2 governing classification is right |
| **N-23 — the running-speed bridge is printed in BOTH maneuvers**; N-24 `Retreat` at *"greater than half his encounter speed"*; N-25 the flat `5'`; N-26 shield forfeit and the `+2` cross-referenced to *"the Attack Roll Modifiers Table on page 108"*; N-27 the `Combat Maneuvers Table` rows | p. 104 (leaf 103) | **All exact.** Pass 1's single-maneuver attribution really was wrong |
| E-19–E-22 Timekeeping and the `Timetrack Table`'s four row lengths (28 / 24 / 6 / 60, with the two trailing em-dashes) | p. 149 (leaf 148) | **All exact.** The *"presentation / tracking, not a procedure"* disposition is right — the section is addressed to a DM with a pencil |
| p. 97 and p. 98 exclusions (wilderness/city subtables; the `Evasion and Pursuit` opening and `Definitions`) | pp. 97–98 (leaf 96–97) | **Accurate.** p. 98's `Contact` and `Decision to Evade` text matches N-4 and N-36 |
| The General Index has **no** `Light` / `Lantern` / `Tinderbox` / `Flask` entry; `Evasion . 91, 98-100`; `Pursuit . 98-100`; `Encounter speed . 88, 95, 100, 103`; `Exhaustion . 88`; `Retreat maneuver . 104`; `Fighting withdrawal maneuver . 104` | pp. 302–304, read entry by entry | **All confirmed**; both packets' §3.3 page lists match the printed index |

### 5.5 Scope creep — checked hard, and I found none

**`EXP-006`** does not absorb encounter generation or distance (`ENC-001`), surprise,
reaction or initiative (`ENC-002`/`ENC-003`/`COMBAT-006`), blindness causation generally,
starvation causation, generic condition infrastructure, the general-skills system,
`EXP-004`, `EXP-010` or the stocking knot. **The pass-5 additions are the test case, and
they pass it**: all six p. 84 entries end in explicit `CHAR-012` ownership with *"not
claimed"*, and E-48/E-49 are excluded outright. §7.1 routes every non-owned item by name.

**`ENC-005`** does not absorb generic terrain (excluded **by name** at §5.4 and §9.3,
including the `Charge` list and the previously rejected Mystic material), marching order
(`EXP-010` explicitly not absorbed; the procedure needs party *size*, not order),
combat-maneuver ownership, initiative, surprise, reaction, morale or the general-skills
system. **N-38/N-39 are used only to CLOSE a dependency, never to claim a mechanic** —
the most creep-prone move available in pass 5, and it was not made.

**Seams held.** `CHAR-004` — no price, `Coin`, quantity-pricing, catalog or price-form
fact is restated or used (the one incidental encumbrance quotation is Finding 5, and
E-26 defers the table rows correctly). `EXP-002` — §5.5 states in terms that the
Timetrack *"creates NO second time authority"* and that its ratios corroborate rather
than rival. `CHAR-005` — movement rates and the blindness multipliers are consumed, not
re-derived. `EXP-003` — ordinary dungeon movement is untouched (the outstanding item is
Finding 2's *reporting*, not an encroachment).

**Neither p. 99 printed defect is adjudicated.** N-5 and N-14 are both
`RETAINED AS GENUINE SOURCE AMBIGUITY` under §10.2.2 case 3, `ENC-005` §19 says so
explicitly, and the `DEC-0011` lineage request is correctly framed as a **request
requiring human authorization**, not as research performed.

### 5.6 Protocol instruments

| Requirement | `EXP-006` | `ENC-005` |
|---|---|---|
| §9.3 Primary-Source Coverage Checklist | **Present** (§9, with §9.1 structural units, §9.2 Guardrail-C attestation, §9.3 exclusions with reasons, §9.4 unresolved items) | **Present** (§9, same four parts, plus a §9.2 complete-entry statement for pp. 98–100) |
| §10.2.1 reconciliation table against the packet's own prior open statements | **Present** (§8.1, seven rows, all dispositioned) | **Present** (§8.1, ten rows, all dispositioned) |
| §10.2 closure gate — zero `BLOCKED` rows | **Confirmed by grep**; every hit is meta-discussion | **Confirmed by grep**; every hit is meta-discussion of pass 2's removed row |
| §17 — no hard-stop string used as a label alongside a ready recommendation | **Correct** — the only use is a framed hypothetical at §8.2 | **Correct** — the only use is the pass-5 meta-note recording the fix |
| §6 confidence and §10.2 disposition vocabularies verbatim | Verbatim throughout except the four cells at Finding 8; **no invented labels** | Verbatim throughout except N-30a; **no invented labels** |
| §11 required report contents (items 1–19) | All present | All present |
| Recommendation is a **submission**, not a certification (§10.1.2) | **Correct** — *"a submission, not a verdict"* | **Correct** — same |

---

## 6. What I checked and found nothing on

- **The whole `Index to Tables and Checklists` (p. 301), entry by entry**, against both
  cards' responsibilities. Beyond `Create Food . 125` (Finding 11) and the `Index to
  Spells` structural point (Finding 3), every entry bearing on light, exploration
  resources, time, condition consequences, retreat, pursuit or evasion is dispositioned
  in one of the two packets.
- **The whole `General Index` (pp. 302–304), entry by entry.** The only entries I found
  bearing on either card and absent from both packets are `Dwarven lens . 146`
  (Finding 4) and `Placement of figurines . 149` (Finding 10). I specifically checked
  `Fire . 116`, `Fatigue . 119`, `Food . 89, 121, 125`, `Lost . 89`, `Nocturnal . 153`,
  `Drowning`/`Swimming . 89`, `Speed . 88`, `Encumbrance . 63, 88`, `Immunity . 119`,
  `Invisibility . 150` and `Knockout . 112` — all either dispositioned or genuinely
  out of scope.
- **The fourteen unnamed p. 84 skill entries** (§5.1). No governing object among them.
- **p. 85's `Quick Draw` (`+2` to *individual* initiative) and `Snares`.** Individual
  initiative is declined for V1 by `DEC-0008` and step 5 uses group `1d6`; `Snares` is
  `EXP-007`'s. Neither is a gap.
- **p. 85's `Stealth (choose terrain)`, including its `Indoors/Caves` option.** Both
  packets name and route it. I checked whether it is a disguised evasion mechanic: it is
  not — it is a `Move Silently` analogue bearing on surprise, which `ENC-002` owns.
- **p. 99 col. 3's spell-escape examples** (Finding 7) and **p. 100 col. 3's `Piloting`
  hook** (Finding 6) — the only two texts on the `Evasion and Pursuit` pages that carry a
  mechanic and are not in an evidence row. Both are on inspected pages; neither changes a
  conclusion.
- **Anomalous-payload spot check across the cited range.** Beyond leaf 83, no cited page
  has a payload size unexplained by its own content. I opened the four smallest cited
  pages (pp. 97, 98, 149, and p. 85/86) to be sure; **all render in full**. The p. 84
  defect appears to be isolated within this cluster's citation range.
- **File integrity after the reported encoding round-trip.** Zero mojibake sequences,
  zero U+FFFD, balanced code fences, 48 and 36 headings, correct UTF-8 em-dashes from the
  first byte. Section markers and quotations render correctly throughout. **The repair
  held; no content was lost that I can detect**, and every quotation I sampled against
  the page images is character-exact, which is the strongest available evidence that the
  text survived intact.

---

## 7. Reviewer's note

The direction asked whether there is a further class of object or claim still outside.
I looked for one in the two places it was most likely to be — another defective
derivative, and another project fact asserted without opening the file — and **I did not
find one.**

Every page in the cluster's citation range that I could plausibly suspect renders in
full. Every project fact pass 5 asserts, including both of the owner-ID corrections and
the `CLUSTER-003` open-question citation that had to be right to the item number, checks
out against the actual file. Every one of the six entries recovered from the second scan
of p. 84 is character-exact, and I read the fourteen entries on that page that neither
packet names, specifically hunting for something swept up in a blanket exclusion. There
is nothing there.

What is left is a residue of accuracy and reporting defects — a page list that
under-claims, a chapter number off by one, an appendix that starts a page earlier than
the packet says, four entries never named, and a good deal of stale self-description.
Every one of them is real and every one should be fixed. **Not one of them leaves a
governing object uninspected, asserts an inspection that did not happen, or makes a
source-property claim the source refutes.** Four prior reviews failed these packets for
defects of exactly that kind, and this pass does not have one to report.

The one item I would most like the human reviewer to carry forward is Finding 2 — not
because it threatens completeness, but because the `Mapping (Cartography)` skill-roll
sentence bears on a **landed, approved** card (`EXP-003`) that says no mapping roll
exists, and the full text now needs to reach a human rather than sit one quotation short
in a Stage-A packet. I have supplied it verbatim above so that closing it requires no
further source access.

I set out to discover omissions rather than to confirm the work. I have said where I
looked for each one, including the places I looked and found nothing (§5, §6). I also
found and withdrew one of review 4's own findings on source evidence (its Finding 14),
because the Rules Cyclopedia's `Adventuring Gear Table` prints exactly the label that
review called invented.

```text
EXP-006   PRIMARY-SOURCE COMPLETENESS: PASS
ENC-005   PRIMARY-SOURCE COMPLETENESS: PASS
```

These are completeness certifications only. They certify that the primary source has been
mapped and inspected for both responsibilities — **not** that the Rules Cyclopedia is
unambiguous. `SOURCE COMPLETE ≠ SOURCE UNAMBIGUOUS` (§10.2.2). Both `ENC-005` printed
defects, the `−6`/`−4` sightlessness relationship, `EXP-006`'s Q1 light-to-`Visibility`
mapping, the ration and starvation-causation ownership questions, `ENC-005`'s underworld
scope question and its six unresearched counterparties all survive this `PASS` as
documented Stage-B and human-governance problems. The §11 human evidence-review gate is
unaffected and remains ahead of both packets.

**No file other than this review artifact was modified. No packet was edited, no Rule
Card drafted, no production code written, nothing committed.**
