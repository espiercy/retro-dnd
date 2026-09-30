# `CLUSTER-004` — Independent Primary-Source Completeness Review, Pass 4

```text
PROTOCOL           RULE_CARD_RESEARCH_PROTOCOL.md §10.1.2 (who) / §10.3 (method)
                   DEC-0010 items 5, 7, 10, 11, 14, 15, 16, 17, 18
REVIEWER           Independent reviewer context.  Did NOT conduct the evidence
                   collection being certified, and did not participate in
                   reviews 1, 2 or 3.
PACKETS REVIEWED   docs/rules/evidence/EXP-006-evidence-remediated.md   (pass 4)
                   docs/rules/evidence/ENC-005-evidence-remediated.md   (pass 4)
PRIOR REVIEWS      pass 1  FAIL / FAIL   CLUSTER-004-stage-a-completeness-review.md
                   pass 2  FAIL / FAIL   CLUSTER-004-stage-a-completeness-review-2.md
                   pass 3  FAIL / FAIL   CLUSTER-004-stage-a-completeness-review-3.md
PRIMARY SOURCE     D&D Rules Cyclopedia (TSR 1071), IIIF page images
                   https://iiif.archive.org/iiif/TSR1071TheDDRulesCyclopedia$<leaf>/...
                   OCR used ONLY to test whether a page region is obtainable at all.
```

## Verdicts

```text
EXP-006   PRIMARY-SOURCE COMPLETENESS: FAIL

ENC-005   PRIMARY-SOURCE COMPLETENESS: FAIL
```

Both failures rest on **Findings 1 and 2**, which are the same defect seen from two
sides. Every other finding is MED or LOW and would not, on its own, have produced a
`FAIL`. Findings 1 and 2 are not stylistic and are not wording preferences: a page
region that neither available access method can render has been presented as
inspected, and the rows whose text lives in that region have been excluded by a
blanket sentence rather than by inspection.

---

## 1. Method

Per §10.3 I built my candidate list **before opening either packet**, from:

- RC Table of Contents, pp. 2–3 (leaf 1, leaf 2) — read in full, both pages;
- `Index to Tables and Checklists`, p. 301 (leaf 300) — read entry by entry;
- `General Index`, pp. 302–304 (leaf 301–303) — read entry by entry;
- `docs/rules/INVENTORY.md` — the rows for every Rule ID either packet names;
- `docs/decisions/` — `DEC-0008`, `DEC-0010`, and the `INDEX.md` roster;
- `docs/rules/clusters/CLUSTER-004-BOUNDARY-CORRECTION.md`;
- the landed cards `encumbrance_and_movement_rate.md` (`CHAR-005`) and
  `docs/rules/evidence/CHAR-005-evidence.md`.

Only after that list was fixed did I open the packets. Where a packet asserts a fact
about the **project** — a decision record, an `INVENTORY.md` row, a landed card's
contents — I opened that file rather than accepting the assertion, because review 3
found one such error and the direction asked whether there are others. **There are
two more** (Findings 5 and 13).

---

## 2. My independent candidate list, built before reading the packets

### 2.1 `EXP-006` — Light & Exploration Resources

| # | Candidate object | Route to it | Disposition after checking the packets |
|---|---|---|---|
| C1 | `Adventuring Gear Table` p. 69 + the Ch. 4 descriptions pp. 68–70 | TOC Ch. 4; p. 301 index | **Packet covers it.** Torch / Lantern / Oil / Tinderbox / Waterskin transcriptions verified exact against the p. 70 image by me (§5 below) |
| C2 | General Index `Torch . 62, 66, 69, 70` — the p. 62 and p. 66 limbs | General Index | **Covered**, routed to `CHAR-004` |
| C3 | `Oil . 62, 65, 69` — oil as thrown weapon | General Index | **Covered**, routed to `CHAR-004` |
| C4 | `Rations . 69` | General Index | **Covered** (§5.6, E-23–E-25) |
| C5 | `Food . 89, 121, 125` | General Index | **Covered** in §3.3, but see Finding 8 — `Clerics and the Create Food Spell Table . 125` is a **named p. 301 object** and is absent from §3.2 and §9.2 |
| C6 | `Game Turn Checklist` / `Game Day Checklist` p. 91 | p. 301 index | **Covered** |
| C7 | `Timetrack Table` p. 149, Timekeeping / Record Keeping pp. 148–149 | p. 301 index; General Index | **Covered** (§5.5) |
| C8 | p. 150 `Special Character Conditions` — Blindness, Starvation, Dehydration | General Index | **Covered** (§5.1, §5.4) and correctly not absorbed |
| C9 | `Infravision . 24, 25` | General Index | **Covered**, routed `CHAR-009` — and `CHAR-009` is the correct owner per `INVENTORY.md` |
| C10 | `Index to Spells`, **p. 300**, and the `light` / `continual light` spells | TOC: *"Appendix 4: Indices … 300 / Index to Spells … 300"* | **NOT covered.** Finding 8 (LOW–MED) |
| C11 | `Oil of darkness` / `moonlight` / `sunlight`, `Dwarven lens`, `Lightship` p. 146 | General Index | **Covered**, routed `MAGIC-*` with a stated reason |
| C12 | Ch. 5 `Sample Skills Table` p. 82 and the skill descriptions pp. 83–86 | p. 301 index | **Covered only in part.** Findings 1 and 2 (HIGH) |
| C13 | `Target Cover Table` / `Attack Roll Modifiers Table` p. 108 | p. 301 index | **Covered** (§5.9), correctly routed and not adjudicated |
| C14 | `Fire . 116` (Ch. 8 special attacks) | General Index | Not named. Burning-oil damage is `COMBAT-*`/`CHAR-004`; no light, radius, duration or resource fact. **No finding** |
| C15 | Ch. 17 `Pre-Game Checklist` p. 262, Running Adventures p. 261 | p. 301 index | **Covered**, excluded with reason |
| C16 | `Encumbrance . 63, 88` | General Index | **Covered**, routed `CHAR-004` / `CHAR-005` |
| C17 | The General Index has **no** `Light`, `Lantern`, `Tinderbox` or `Flask` entry | General Index, read entry by entry | **Independently confirmed correct.** The packet records this at §3.3 and the record is accurate |
| C18 | p. 70 `Shoes` — an exploration-gear item with a stated damage consequence for going without | p. 70 image | **NOT covered.** Review-3 item 7 asked for it by name; zero occurrences in the packet. Finding 9 (LOW) |

### 2.2 `ENC-005` — Retreat, Pursuit & Evasion (underworld)

| # | Candidate object | Route to it | Disposition after checking the packets |
|---|---|---|---|
| D1 | `Evasion Checklist` + `Evasion Table`, p. 99 | p. 301 index | **Covered**, transcriptions verified exact by me |
| D2 | General Index `Evasion . 91, 98-100` — the **p. 91** limb | General Index | **Covered** (§3.3, N-2) |
| D3 | `Pursuit . 98-100` | General Index | **Covered** |
| D4 | `Ship Evasion Table` p. 100 + `Evasion at Sea` | p. 301 index | Column excluded as naval — but see Finding 4: p. 100 col. 3 carries an **opposed-skill** evasion resolution that is a class-I parallel presentation and is never enumerated |
| D5 | `Combat Maneuvers Table` p. 104, `Retreat`, `Fighting withdrawal` | p. 301 index; General Index | **Covered** (§5.6), routed `COMBAT-*`, not absorbed |
| D6 | `Exhaustion . 88`, `Running speed . 88, 103`, `Encounter speed . 88, 95, 100, 103` | General Index | **Covered** (§5.5a), consumed from landed `CHAR-005` |
| D7 | p. 92 surprise / p. 93 `Encounter Distances Table` / `Encounter Checklist` | p. 301 index | **Covered** (N-4a/b/c), routed `ENC-001`/`ENC-002` |
| D8 | `Morale Scores Table` p. 103; `Combat Sequence Checklist` p. 102 | p. 301 index | **Covered**, routed `ENC-004` / `COMBAT-006` |
| D9 | `Monster movement rate . 88, 152` | General Index | **Covered**, routed `MON-003` |
| D10 | `Charge . 154` terrain list; `Terrain Effects on Movement` p. 88 | General Index | **Covered**, excluded by name, not imported |
| D11 | Ch. 13 p. 147 `Doors` / `Listening` — closing doors behind a fleeing party | General Index | Not named by `ENC-005`. RC p. 99 col. 1 *does* attach evasion value to *"closing doors behind them"* (N-35), and `EXP-006` routes p. 147 to `EXP-005`. Ownership is clean; **no finding**, recorded as checked |
| D12 | `Move silently . 22` / `Hide in shadows . 22` | General Index | Enumerated, but mis-routed — Finding 13 (LOW) |
| D13 | Ch. 5 skills: `Caving`, `Endurance`, `Tracking`, `Stealth`, and the rows on p. 84 | p. 301 index `Sample Skills Table . 82` | **Covered only in part.** Findings 1, 2 and 3 |
| D14 | `Lost . 89` (wilderness) vs p. 100's dungeon lost-condition | General Index | **Covered** (N-22), and the pass-4 restoration is verified exact |
| D15 | `Balancing Encounters Checklist` p. 101, `Castle Reactions Table` p. 99 | p. 301 index | **Covered**, excluded with reasons |

---

## 3. Findings

### Finding 1 — HIGH — both cards

**RC p. 84 cannot be rendered in full by either access method the packets use, and both
packets present it as inspected while recording no access limitation.**

I retried leaf 83 four times at three sizes (`1400,`, `2400,`, `full`), all HTTP 200
with full-size payloads (135,909 / 319,895 / 1,053,144 bytes). At every size, **only
column 1 renders. Columns 2 and 3 are blank.** This is a stable property of the IIIF
derivative, not a transient `504`. I then tested the OCR transcription as a fallback
locator: it is truncated at **exactly the same point** —

```text
OCR, p. 84 column 1, verbatim ending:
    "...In areas not normally rich in
     game he must make a "
        [then jumps straight to the p. 85 running head and Persuasion]
```

So the text of RC p. 84 columns 2–3 has never been read — not by pass 4, not by any
prior pass, and not by me. What lives there, by the alphabetical ordering of
`Skills Descriptions` (p. 84 col. 1 ends inside `Hunting`; p. 85 col. 1 opens inside
`Persuasion`), is the remainder of **`Hunting`** and the whole of **`Intimidation`,
`Knowledge`, `Labor`, `Language`, `Law and Justice`, `Leadership`, `Lip Reading`,
`Magical Engineering`, `Mapping/Cartography`, `Military Tactics`, `Mimicry`,
`Mountaineering`, `Muscle`, `Music`, `Mysticism`, `Nature Lore`, `Navigation`**.

What the packets say instead:

| Packet | Statement | Status |
|---|---|---|
| `EXP-006` §5.8a | *"pp. 84–86 were opened in pass 4"* | Overstates; p. 84 is two-thirds unrenderable |
| `EXP-006` E-43 | cites **pp. 84–85** as the object for `Hunting` / `Tracking` | The p. 84 half is cut off mid-sentence |
| `EXP-006` §11–18 (17) | *"**All pages cited were ultimately obtained as images.** No finding in this packet rests on OCR."* | **False as to p. 84** |
| `EXP-006` §2 / §9.1 | p. 84 appears on **neither** coverage list | §9.3 violation — a page carrying an evidence row is unlisted |
| `ENC-005` §9.1 | header *"Structural units inspected — **all as page images**"*, listing *"p. 84-85 … read ROW BY ROW … pass 4"* | Overstates |
| `ENC-005` §11–18 (17) | access limitations named: p. 104, p. 88 only | p. 84 omitted |

§9.2 names the required response in terms: *"If the current access method cannot
provide usable page images: `STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED`. Do not
declare evidence complete. This is a hard gate on the same footing as §4's."*
§11 item 17 independently requires access limitations to be reported *"even where a
workaround succeeded."* Neither packet does either.

This is the same species as the defect pass 4 itself corrects about pass 1 at
`EXP-006` §2.1 — *"Pass 1 §7.1 stated that pp. 302–303 could not be verified because
of remote 504s. **That statement was false when written**"* — with the sign reversed.
Pass 1 claimed access it had; pass 4 claims access it does not have.

**Required:** record the limitation, issue
`STOP — PRIMARY-SOURCE VISUAL ACCESS REQUIRED` for the p. 84 region or obtain it from
another rendition/edition, and reclassify every row that depends on it.

---

### Finding 2 — HIGH — both cards

**The `Sample Skills Table` "read ROW BY ROW" claim is not supported: four rows that
bear on the two responsibilities are named nowhere in either packet, and their
descriptions are the ones Finding 1 shows are unreadable.**

Both packets close the table with a blanket sentence:

```text
EXP-006 §9.2   "...all remaining rows inspected and EXCLUDED AS UNRELATED to
                light, time or exploration resources."
ENC-005 §3.2   "...all other rows inspected and EXCLUDED AS UNRELATED to retreat,
                pursuit or evasion."
```

I read the `Sample Skills Table` (p. 82, leaf 81) myself, row by row, and then grepped
both packets for every row name. Results:

| Sample Skills Table row | Named in `EXP-006` | Named in `ENC-005` | Description page | Why it is not "unrelated" |
|---|---|---|---|---|
| **`Mapping/Cartography`** (Int) | **0** | **0** | p. 84 — unreadable | `ENC-005` N-22's lost/not-lost branch turns on whether areas were *"already knew or **had mapped**"*; landed `EXP-003` asserts *"No separate mapping mechanic, time cost, roll, or failure state exists or is to be created"* — a named skill with a roll is a class-I parallel object against both |
| **`Navigation`** (Int) | **0** | **0** | p. 84 — unreadable | Checklist step 6 is *"determine where they now are."* RC p. 86's own `Time Use` paragraph uses *"a basic Navigation roll"* as its worked example, so RC treats it as a positional-determination skill |
| **`Nature Lore`** (Int) | **0** | **0** | p. 84 — unreadable | `EXP-006` Q11 (food/water supply) is dispositioned on the premise that `Survival` and `Hunting` are the only food/water skills and are wilderness-terrain-gated |
| **`Mountaineering`** (Dex) | **0** | **0** | p. 84 — unreadable | `ENC-005` Q3 *"difficult terrain"*; weaker than the three above, but it is a terrain-traversal skill in a card whose open question is terrain |
| `Escape` (Dex) | 0 | 0 | p. 83 — **readable** | *"Another roll is needed to open a locked door"* touches N-33's *"a magically locked door"* obstacle branch. Weak; recorded, not a basis for failure |
| `Danger Sense`, `Alertness` | 0 | 0 | pp. 82–83 — readable | Surprise-adjacent; `ENC-002` correctly owns surprise. **No finding** |
| `Stealth (choose terrain)` | 1 | 1 | p. 85 — readable | Named and routed. **Correct**, and I verified RC's `Indoors/Caves` option is real |

Under §9.5 Guardrail B this is a source-property claim (*"unrelated"*) standing where
only a research-operation claim is available — and for the four top rows the research
operation could not have been performed at all. Under §9.1's *"A failed search is not
evidence of absence"*, a blanket exclusion over an unrenderable region is the strongest
form of that error.

**This is also a direct recurrence of review-3 remediation item 3**, which asked for
every row bearing on the card to be dispositioned and for `EXP-006` §3.3's `Mapping`
row to be restated as a research operation or withdrawn. `EXP-006` §3.3 still reads:

```text
| Mapping | 5, 148, 256, 257 | yes | Player-facing advice + DM prep.
                                     NO EXECUTABLE MECHANIC; no light input |
```

— an unqualified source-property claim, made from a General Index entry that **does
not include the `Mapping/Cartography` general skill at all**. The `EXP-003` overlap
review 3 asked to be reported to the human owner is not reported.

---

### Finding 3 — MED — `ENC-005`

**§9.8 — `Caving` is treated as *the* step-6 determination while two sibling objects
remain undispositioned and unreadable.**

§5.7's heading is *"`Caving` (p. 83) — a governing object for checklist step 6"* and
§7.1 names `CHAR-012`'s `Caving` check as step 6's lost-determination provider. That
is a reasonable **principal** object. But §9.8 forbids treating a principal object as
the governing one *"until all related structured and detailed source objects have been
enumerated and dispositioned"* — and `Navigation` and `Mapping/Cartography` sit in the
same table, under the same optional system, addressing the same question (*where are
we / do we have a map*), with descriptions the packet cannot read.

The conclusion may well survive. It has not been earned yet.

---

### Finding 4 — MED — `ENC-005`

**RC p. 100 col. 3 carries a second, opposed-skill resolution of evasion, and it is
never enumerated. Review-3 item 11 asked for exactly this and it was not done.**

Verified on the p. 100 image (leaf 99), col. 3:

> *"If the DM is using the optional general skills rules, he or she can roll the two
> captains' Piloting skills in competition with one another. If the evading ship's
> captain rolls his skill better, he evades pursuit; if the pursuer rolls his better,
> he is able to close at the rates described above."*

`ENC-005` excludes the whole column as naval (§5.5, §9.3) and the string `Piloting`
does not occur anywhere in the packet. But this is a §9.1 **class I duplicate/parallel
presentation**: RC resolving *the same responsibility* — does the evader get away —
by an opposed skill contest rather than by the `Evasion Table`. The packet already
records one such parallel at N-17a (`Tracking` as *"a second, skill-based route to the
same question N-17 resolves with a percentage"*) and flags it `Recorded, not
reconciled`. A second instance, in the section's own pages, must be recorded the same
way before the column is excluded — class I says *"record each separately"* and *"do
not treat any one representation as automatically authoritative."*

Excluding it as *naval* is a plausible **disposition**; skipping the **enumeration** is
not.

---

### Finding 5 — MED — `EXP-006` — a project-registry fact asserted without opening the registry

`EXP-006` routes RC p. 150's generic conditions to a card that does not own them:

```text
§3.3   | Invisibility / Sleep / Stunning / Paralysis / Prone character | 150 | yes |
         Same p. 150 section as Blindness.  Routed -> COMBAT-* / CHAR-011.

§9.3   p. 150 Deafness/Invisibility/Paralysis/Prone/Sleep/Stunning
         Same section as Blindness; COMBAT-*/CHAR-011.  Read, not claimed.
```

`INVENTORY.md` line 90: **`CHAR-011` is Weapon Mastery.** It is not a condition card,
and nothing in its row touches blindness, sleep, paralysis, stunning or prone. The
movement half of p. 150 is `CHAR-005` §7 (which the packet cites correctly elsewhere);
the condition infrastructure has no owner, which is the kind of fact §9.3 exclusions
exist to surface.

This is the **fourth-class error the direction asked me to look for** — a claim about
the project rather than about the source, asserted without opening the file that
refutes it, in the same packet that records at §5.8 *"This is the third time in this
cluster that a claim was asserted without opening the artifact that refutes it."* It
is the fourth time. It does not leave a source object uninspected, so it is MED, not
HIGH — but the stated reason for a §9.3 exclusion names the wrong card, which is
precisely what makes an exclusion auditable or not.

---

### Finding 6 — MED — `ENC-005` — §17 hard-stop string still used as an inline label

```text
line 260   "N-14 remains unadjudicated.  `INTERNAL SOURCE CONFLICT REQUIRES REVIEW`."
line 570   Q5 ... RETAINED AS GENUINE SOURCE AMBIGUITY ...
                  `INTERNAL SOURCE CONFLICT REQUIRES REVIEW`
line 740   RECOMMENDATION:  EVIDENCE READY FOR HUMAN REVIEW
```

§17's message is `STOP — INTERNAL SOURCE CONFLICT REQUIRES REVIEW`, and its trigger is
an agent that *would choose between* conflicting passages. This packet correctly does
**not** choose; Q5 is properly `RETAINED AS GENUINE SOURCE AMBIGUITY` under §10.2.2
case 3, which §17's closing note expressly permits to pass completeness. Displaying
the stop string as a label therefore asserts a hard stop and a ready recommendation in
the same document.

What makes this a finding rather than a nitpick: **review 3 raised this exact item and
`EXP-006` fixed it** — `EXP-006` §19 remediation line 9 reads *"Hard-stop vocabulary no
longer used as an inline label"*, and `EXP-006`'s only use of the string is now a
properly framed hypothetical at §8.2 (*"A packet that chose a number here would trip
§17's STOP — …. This one does not choose."*). The identical defect in the sibling
packet was not fixed. That is the signature of patching the handed list rather than
re-running the check.

Vocabulary otherwise checks out: §6 confidence terms (`DIRECT PRIMARY TEXT`,
`PRIMARY TEXT + CROSS-REFERENCE CONFIRMED`, `NECESSARY CONSEQUENCE`) and §10.2
dispositions (`RESOLVED BY SOURCE INSPECTION`, `CONFIRMED OUT OF SCOPE`,
`RETAINED AS GENUINE SOURCE AMBIGUITY`) are used **verbatim** in both packets.
**No invented labels.** **No `BLOCKED` row in either packet** — confirmed by grep;
both claims of zero are true.

---

### Finding 7 — MED — `EXP-006` — the three coverage lists are still not mutually consistent

The direction asked whether §9.1, §2's image/locator split and §3.2/§3.3 are now
consistent. **They are not**, and the inconsistency is new in pass 4:

```text
§2  IMAGE-VERIFIED   68 69 70 81 82 83 88 91 92 93 98 99 100 104 108
                     149 150 154 301 302 303 304
§9.1 VISUALLY INSP.  ... same, PLUS 85 and 86 ...
NEITHER LIST         84          <- carries evidence row E-43
```

Also stale: §2's qualifier reads *"Every page that carries an evidence row
(`E-1` … `E-40`) … was read as a page image"* — pass 4 added **E-41, E-42, E-43**, so
the sentence does not cover its own newest rows, including the one on the unreadable
page. §9.3's *"General skills system (81-86)"* line still implies a range the lists do
not carry.

Review-3 item 5 required *"every page marked `OPENED`/`yes` in §3.2 and §3.3 [to]
appear on exactly one of [§2's lists]"*. Pass 4 reconciled the pass-3 pages and then
added three more without updating §2. `ENC-005` has no §2 split at all and asserts
*"all as page images"*, which Finding 1 shows is inaccurate.

---

### Finding 8 — LOW–MED — `EXP-006` — Appendix 4 enumerated from p. 301; RC's Appendix 4 begins at p. 300

§3.1 records `App. 4 Indices pp. 301-304`, and §9.1 records pp. 301–304 *"read in
full."* The RC Table of Contents (p. 3) prints:

```text
Appendix 4: Indices ............ 300
    Index to Spells ............ 300
    Index to Tables and Checklists  301
    General Index .............. 302
```

The **`Index to Spells` (p. 300) is a finding aid the packet never enumerates** — the
instrument that would list `light`, `continual light` and their kin by name. §9.1
class H treats index entries as completeness locators; §6.6 routes magical light to
`MAGIC-*` by assertion, having *"opened [them] only far enough to confirm they are
Chapter 12 magical items and Chapter 3 spells."*

The **routing** is defensible — `EXP-006` should not own spell mechanics, and RC p. 150
(which the packet does quote) is the point where a light spell's consequence enters
this card's space. The **enumeration** is not: the packet mis-states the source's own
structure and then claims that structure was read in full.

Also in this class: `Clerics and the Create Food Spell Table . 125` is a **named p. 301
object** (I confirmed it on the printed index) bearing on exploration resources. It is
dispositioned only inside §3.3's `Food` row, and is absent from §3.2's index table and
from §9.2's Guardrail C attestation — while §3.2 states *"every entry on p. 301 was
read and each one relevant to light, exploration resources, time or condition
consequences is dispositioned above or in §9.2."* Review-3 item 7 asked for it by
name. Not done.

---

### Finding 9 — LOW — `EXP-006` — p. 70 `Shoes` not recorded

Review-3 item 7 also asked for it. Zero occurrences. RC p. 70, verified on the image:

> *"Shoes: A character should have shoes if he is going to travel or explore dungeons;
> the DM might assign damage to barefoot characters walking through bad terrain or
> treacherous catacombs."*

A purchased item whose absence RC attaches a dungeon consequence to — structurally the
same shape as the card's other content. Small, but it was named in the remediation
list and is still missing.

---

### Finding 10 — LOW — both — stale self-description

```text
Both titles          "Stage-A Evidence (Remediated, Pass 2)"        (header says PASS 4)
Both §19             "subject to the mandatory §10.1.2 THIRD independent
                      completeness review"                          (this is the fourth)
Both §19             "Pass 3 remediation of the second review's findings:"
                      -- the list that follows contains NO pass-4 items
```

Neither packet records what pass 4 itself changed, in the section whose purpose is to
tell a reviewer what changed. Not a completeness defect; it made this review slower.

---

### Finding 11 — LOW — `EXP-006` — open-question count stale

§9.4 says *"All ten are in §8"*; §8 carries **Q1–Q13**. §11–18 item (12) says
*"§8, Q1–Q10"*, omitting Q11, Q12, Q13. §8.2 is printed before §8.1. **Every row is
in fact dispositioned** under §10.2 vocabulary, so the closure gate itself is
satisfied — this is a counting error, not a hidden item. §5.8's evidence table is also
split in half by an interposed prose subsection (lines 513–538), leaving rows E-36 to
E-38 orphaned from their header.

---

### Finding 12 — LOW — `ENC-005` — leftover conditional phrasing, and one dangling reference

The direction asked me to check for leftovers of the withdrawn "optional/undecided"
framing. The withdrawal is **substantially** consistent — E-33a and N-30a are both
correct (§4 below) and the `BOUNDARY-CORRECTION` §6 item 2 reasoning is sound. Two
residues:

```text
line 371  "That is a rule about the party at large whenever THE OPTIONAL SYSTEM
           IS SWITCHED ON."
              -- re-conditions N-28's automatic-loss rule on a switch DEC-0008
                 has already set.  Should read "in force for V1".

line 758  "...the open-ended DM adjustment..."
              -- in §19's remediation list, describing N-34 by the conclusion
                 §5.3a withdraws six hundred lines earlier.
```

And line 785 cites *"`§4.4`'s own dependency table"*. **There is no §4.4 in
`ENC-005`.** The dependency table is §7.1, and the `ENC-004 (DEC-0008 REQUIRED)` row it
refers to is real — I verified it. Review 3 flagged a dangling section reference in
`EXP-006` pass 2; the same class reappears here.

Otherwise: grep for `open-ended` returns only those two lines, and the pass-3
"explicitly open-ended" conclusion **is** withdrawn consistently, including in the
§10 falsification table, whose row reads `NOT ESTABLISHED EITHER WAY` and defers to
Q3. That is the correct handling.

---

### Finding 13 — LOW — `ENC-005` — second project-registry mis-routing

§3.3: `| Move silently | 22 | yes | Thief skill, CHAR-012. Excluded |`

`Move Silently` is a Thief class ability. `INVENTORY.md`'s `CHAR-009` row states in
terms: *"Thief's own abilities are owned by `CHAR-010` instead."* `CHAR-012` is General
Skills. Same class as Finding 5; the exclusion is right, the owner named is wrong.

---

### Finding 14 — LOW — `EXP-006` — E-32 item label

E-32 is headed **`Waterskin/wineskin`**. RC p. 70 prints a `Waterskin` entry and a
separate `Wine` entry (*"the cost of a quart of common wine, not including the
container"*). There is no `wineskin` item. **The quoted text is `Waterskin`'s and is
verbatim correct**; only the label invents a second item.

---

## 4. Review-3 remediation items — checked one by one

| # | Review-3 required item | Status | Evidence |
|---|---|---|---|
| 1 | `EXP-006`: open pp. 84, 85, 86; record `Hunting`, `Survival`, p. 86 modifier band, natural-1, `Time Use`; route to `CHAR-012`; do not absorb; do not resolve −6/−4/+15 | **partial** | pp. 85, 86 genuinely opened and all five items recorded and verified exact. **p. 84 is two-thirds unrenderable and is claimed as opened** — Finding 1. Non-absorption and non-resolution of the three values: **correct**, §5.9 and §8.2 |
| 2 | `EXP-006`: re-attest Q11 / Q4 against p. 85 or reclassify | **remediated** | Q11 restated in pass 4 with `Survival` as the wilderness answer and the dungeon case retained as ambiguity. Verified against the p. 85 image: the terrain list genuinely offers **no dungeon option**, so the disposition is source-grounded, **not an evasion of Q11** |
| 3 | `EXP-006`: read `Sample Skills Table` entry by entry; restate or withdraw §3.3's `Mapping` *"no executable mechanic"*; report the `EXP-003` overlap | **not remediated** | Finding 2. The `Mapping` row is unchanged and unqualified; `Mapping/Cartography` is named nowhere; the `EXP-003` overlap is not reported |
| 4 | `EXP-006`: withdraw the *"general skills NOT IN USE"* branch and Q5's conditional against `DEC-0008` | **remediated** | E-33a is **verified correct** (§5 below); Q5 rewritten; the branch is explicitly `WITHDRAWN` at §5.8 |
| 5 | `EXP-006`: complete §2's lists; reconcile §9.3's `81-86` with §9.1 | **not remediated** | Finding 7. Pass-3 pages reconciled; pass-4 pages 84/85/86 re-broke it |
| 6 | `EXP-006`: record p. 92's *"When the type of terrain … is known"* and reconcile with §7.2 and Q1 | **remediated** | E-11b **verified verbatim** against the p. 92 image. The narrowing at §5.2 is accurate and correctly does **not** treat p. 92's terrain phrasing as a fourth value in any conflict |
| 7 | `EXP-006`: disposition `Clerics and the Create Food Spell Table . 125` in §3.2/§9.2; add p. 70 `Shoes` and p. 86 natural-1 | **partial** | Natural-1 added to E-34 and verified. `Create Food` table absent from §3.2/§9.2 (Finding 8); `Shoes` absent entirely (Finding 9) |
| 8 | `ENC-005`: open pp. 85–86; record `Tracking`, `Using Skills Together`, `Using Skills Against Each Other`, `Stealth`; re-attest Q3 under case 3; follow the p. 83 class-G cross-reference | **partial** | `Tracking` (N-37) and the `Using Skills Together` tracking example **verified verbatim**; `Stealth` named. **`Using Skills Against Each Other` is named nowhere in `ENC-005`** (it *is* named in `EXP-006` §9.1). Q3 is still `RETAINED AS GENUINE SOURCE AMBIGUITY` with **no case-3 attestation** |
| 9 | `ENC-005`: restore *"as noted in the Evasion Table"* to N-34; withdraw the *"explicitly open-ended"* conclusion | **remediated** | **Verified verbatim** on the p. 99 col. 1 image. Withdrawal is consistent in §5.3a **and** in the §10 falsification table. Correctly left unresolved and folded into Q3 |
| 10 | `ENC-005`: restore p. 100's *"…they're fine"* to N-22; reconcile with §5.7's `Caving` | **remediated** | **Verified verbatim** on the p. 100 image. The reconciliation at §5.7's `CORRECT` block explicitly re-states the negative branch |
| 11 | `ENC-005`: enumerate p. 100 col. 3's `Piloting` hook as a class-I parallel before excluding the column | **not remediated** | Finding 4. `Piloting` occurs zero times in `ENC-005` |
| 12 | `ENC-005`: correct §19's third escalation against `DEC-0008` / `CHAR-012` | **remediated** | N-30a **verified correct**; `BOUNDARY-CORRECTION` §6 item 2 read directly and the packet's reasoning about it is sound (§5 below) |
| 13 | `ENC-005`: restore step 5b's sentence boundary and N-36's closing sentence; add an evidence row for step 5c's spell-escape branch | **partial** | N-36 still ends at *"…before the surprised group can recover enough to give chase"*; RC p. 99 col. 1 continues *"In fact, if the surprised party didn't detect the nonsurprised party, the surprised party will never know that it has just been through an encounter"* — still elided. No evidence row for step 5c's spell branch |
| 14 | Both: re-run the §10.1.1 adversarial self-review **into** the structured objects the indices name — read the table's rows and open every page those rows occupy | **partial — and this is the failure** | pp. 85 and 86 were opened and read well. p. 84 could not be opened and that was not said. Four rows whose text lives there were excluded by a blanket sentence. Findings 1 and 2 |
| 15 | Both: re-submit for §10.1.2 independent review | **remediated** | Both §19s submit rather than certify, and use the permitted language |

**Nine of fifteen items are remediated, and several are remediated well.** The two that
are not — items 3 and 14 — are the two that carry the pattern.

---

## 5. What I verified as correct, and where I looked

Recorded because §10.3 requires a reviewer who finds nothing to say what it looked for,
and because most of these packets is right.

**Primary source, read from page images by me:**

| Claim | Object | Result |
|---|---|---|
| E-41 *"not being able to see … +5, +10, or even +15"* | p. 86 (leaf 85) | **Exact.** Also correct that it is **not** a fourth value in the −6/−4 conflict: it modifies a roll-under **skill** roll, and RC's own band (`+1/+2`, `+3/+4`, `+5/+10/+15`) confirms it is the scale `Fire-Building`'s *"penalties assigned by the DM"* refers to |
| E-34's p. 86 half — natural 1 automatic success | p. 86 | **Exact**, *"A natural roll of 1 on 1d20 is an automatic success, just as a roll of 20 is an automatic failure"* |
| E-42 `Survival (choose terrain)` | p. 85 (leaf 84) | **Exact**, including the six-terrain list, automatic foraging in fertile areas, `+1` per additional person, *"He must roll each day."* The terrain list genuinely contains **no dungeon option**, so `CONFIRMED OUT OF SCOPE / CHAR-012 / wilderness-gated` is source-grounded and Q11's dungeon residue is correctly retained |
| E-43 / N-37 `Tracking` | p. 85 | **Exact** |
| N-37's p. 86 limb — the `Using Skills Together` tracking example | p. 86 | **Substantially exact**; the packet drops *"except to confirm the fact that there are no tracks"*, which does not change the finding |
| E-11b — p. 92's terrain-keyed pointer | p. 92 (leaf 91) | **Exact.** *"When the type of terrain (dungeon, wilderness, ocean/sea, or underwater) is known…"* The narrowing of `EXP-006`'s seam claim is correct and well argued |
| E-11a / N-4a — the surprise gate on encounter distance | p. 92 | **Exact**, all three branches |
| N-4b — automatic evasion on one-sided surprise | p. 92 | **Exact** |
| N-34 — *"…and other factors **as noted in the Evasion Table**"* | p. 99 col. 1 (leaf 98) | **Exact.** Withdrawal of *"explicitly open-ended"* is consistent throughout |
| N-10 `d100` roll-under, N-11 the 5% floor, N-12 party splitting, N-13 the symmetric ±25%, N-14 the prose `−10%` against the table `−15%` | p. 99 | **All exact.** The scouts conflict is genuinely printed; correctly left unadjudicated |
| N-35 area familiarity, *"closing doors behind them"* | p. 99 col. 1 | **Exact** |
| N-19 dropped goods **with** its *"if he or she feels…"* gate, N-20 `Regain Bearings`, N-21 full running speed for every chase round | p. 100 col. 1 (leaf 99) | **All exact** |
| **N-22 — *"If their movement carried them into areas they already knew or had mapped, they're fine"*** | p. 100 col. 2 | **Exact.** The restoration is correct and materially changes the reading |
| p. 100 column classification (col. 1 / 1–2 governing; col. 2 `Evasion at Sea`; col. 3 `Ship Evasion Table` + `Balancing Encounters`) | p. 100 | **Accurate**, except for Finding 4's unenumerated `Piloting` hook in col. 3 |
| N-28 `Caving`, N-31 `Endurance`, E-36 `Fire-Building`, E-37 `Blind Shooting`, E-38 `Food Tasting` | p. 83 (leaf 82) | **All exact** |
| E-27 Torch (30′, one hour / six turns), E-30 Tinderbox (`1d6`, 1–2, once per round), E-32 Waterskin (one quart, 30 cn / 5 cn) | p. 70 (leaf 69) | **All exact** |
| The General Index has no `Light` / `Lantern` / `Tinderbox` / `Flask` entry | pp. 302–304, read entry by entry | **Confirmed** |
| `Evasion . 91, 98-100`; `Pursuit . 98-100`; `Encounter speed . 88, 95, 100, 103`; `Skills . 82-85, 92`; `Exhaustion . 88` | pp. 302–304 | **Confirmed**; both packets' §3.3 page lists match the printed index |

**Project facts, read from the repository by me:**

| Claim | File checked | Result |
|---|---|---|
| E-33a / N-30a: `INVENTORY.md` `CHAR-012` reads *"RC Optional/Additional system → Project-Selected: **REQUIRED** (`DEC-0008`)"* | `INVENTORY.md` line 91 | **Correct, verbatim** |
| `DEC-0008` selected General Skills as project-required | `DEC-0008` line 29 | **Correct** — *"General Skills (RC Optional/Additional system, project-selected: REQUIRED)"* |
| `BOUNDARY-CORRECTION` §6 item 2 (*"newly discovered RC optional system — none found"*) is **not** reopened by General Skills | `CLUSTER-004-BOUNDARY-CORRECTION.md` §6 | **Correct.** General Skills is not newly discovered; it carries a registered project selection. Pass 4's withdrawal of pass 3's escalation is right, and withdrawing it does not conceal a live governance question |
| `SR-10`, cases `M57` (*"75–99% of 120′ = 30′, must not be 90′"*) and `M58` (monotonic) | `encumbrance_and_movement_rate.md` ll. 187–194, 543–544 | **Correct, verbatim, including the case IDs** |
| `CHAR-005` §7 records RC's printed `× 3/4` as RC-Explicit and `× 1/4` separately as `SR-10` | same, ll. 380, 597 | **Correct.** Q7's *"no defect in the landed card"* holds |
| Q13: p. 88 puts the exhausted `−2` on **damage** rolls, and `CHAR-005`'s evidence packet does not cite p. 108 | `encumbrance_and_movement_rate.md` l. 400; `CHAR-005-evidence.md` | **Correct** — `grep -c 108` on the evidence packet returns **0**. Properly reported, not adjudicated |
| Q8 / §5.4: starvation causation has no Rule ID; `BOUNDARY-CORRECTION` §6 item 8 | `BOUNDARY-CORRECTION` §6 item 8 | **Correct, still true** |
| `EXP-010` was deferred over **three** unresearched consumers; landed `EXP-003` case `D32` | `BOUNDARY-CORRECTION` §4 | **Correct, including the case ID** |
| p. 147 `Doors` / `Listening` routed to `EXP-005` *"which `INVENTORY.md` assigns this responsibility"* | `INVENTORY.md` line 105 | **Correct** — `EXP-005` is *"Searching, Listening, Doors & Secret Features … Chapter 13 (p. 147)"* |
| `ENC-004` carries `DEC-0008 REQUIRED`; `ENC-001`, `ENC-002`, `ENC-007`, `MON-003`, `COMBAT-006`, `CHAR-009`, `CHAR-012` all exist with the scopes claimed | `INVENTORY.md` lines 88, 116–122, 130, 142 | **All correct.** `ENC-005` §7.1's six-provider count is sound |

**Scope creep — checked hard, and I found none.** `EXP-006` does not absorb encounter
generation, surprise, reaction, initiative, blindness causation, starvation causation,
generic condition infrastructure, the general-skills system, `EXP-004`, `EXP-010` or the
stocking knot; it routes each by name and claims no mechanic. `ENC-005` does not absorb
generic terrain, marching order, combat-maneuver ownership, initiative, surprise,
reaction, morale or the general-skills system. **Pass 4's additional Chapter 5 material
stayed evidence and did not become absorption** — §5.8a and §5.7 both end in explicit
`CHAR-012` ownership with no skill mechanic claimed. The seams against `CHAR-004`
(prices/encumbrance/catalog/price forms), `EXP-002` (dungeon time), `CHAR-005`
(movement rates) and `EXP-003` (ordinary dungeon movement) are all held; no price,
encumbrance, `Coin` or price-form fact is restated, and no second time authority is
created. **Neither p. 99 printed defect is adjudicated**, and `ENC-005` §11–18 (14)
correctly frames the `DEC-0011` lineage request as a request requiring authorization.

---

## 6. What I checked and found nothing on

- **Chapter 6 pp. 87–90** against `EXP-006` — `Measurements of Game Time`,
  `Movement, Missile, and Spell Ranges`, `Water Movement Modification`, `Terrain
  Effects`, `Traveling Rates by Terrain`: all enumerated and routed or excluded with
  reasons. No light, torch, ration or duration mechanic that the packet missed.
- **Ch. 8 `Target Cover Table` p. 108** — I checked whether RC's cover categories are
  a disguised darkness rule. They are not: *"soft"* and *"hard"* cover only. The
  packet's exclusion reason is accurate.
- **`Forced Marches Table` p. 121, `Fatigue . 119`, War Machine** — no adventurer-scale
  light, resource or evasion mechanic. Exclusions correct.
- **Ch. 17 pp. 259–262** (`Pre-Game Checklist`, `Running Adventures`, `Room Contents` /
  `Unguarded Treasure`) — nothing that governs either card; the stocking knot is
  correctly left untouched.
- **`Ship Evasion Table` p. 100** — dispositioned by both packets. Beyond Finding 4's
  `Piloting` hook, I found nothing in the naval column that governs underworld evasion.
- **`Castle Reactions Table` p. 99, `Balancing Encounters` pp. 100–101** — correctly
  excluded; I confirmed on the p. 99 and p. 100 images that neither touches the evasion
  procedure.
- **`Chance of Encounter Table` p. 92** — I read it on the image. It genuinely has **no
  light or visibility column**, only `Type of Encounter` / `Roll Method` and a
  `Type of Terrain` / `Chance` sub-table. `EXP-006` §6.3's negative is accurate and
  correctly phrased as a research operation.
- **p. 83 `Escape`, `Danger Sense`; p. 85 `Stealth (indoors/caves)`** — readable, and
  their exclusions are defensible. `Stealth` bears on surprise, which `ENC-002` owns.
  Recorded as checked; **not** a basis for either verdict.
- **OCR as a fallback for p. 84** — tested and reported in Finding 1. It fails
  identically, which is why Finding 1 is a `STOP — PRIMARY-SOURCE VISUAL ACCESS
  REQUIRED` condition rather than a "read it in the OCR instead" correction.

---

## 7. Reviewer's note

The direction asked whether pass 4 broke the pattern or patched what review 3 handed
it. The answer is visible in one page number.

Review 3 wrote: *"this cluster has now found the first one twice and the second one
never."* Pass 4 opened p. 85 and p. 86 — the pages review 3 named — and read them
carefully; its work on `Survival`, on the `+5/+10/+15` band, on *"as noted in the
Evasion Table"* and on *"they're fine"* is accurate, verbatim, and in two cases
materially changes what the cards will say. Review 3's items 9, 10, 12, 6, 4 and 2 are
genuinely discharged.

And then pass 4 reached p. 84, could not render two-thirds of it, and **said nothing**.
It wrote *"pp. 84–86 were opened"*, listed *"p. 84-85 … read ROW BY ROW"*, affirmed
*"All pages cited were ultimately obtained as images"*, and closed the roughly sixteen
skills whose descriptions live in those two columns with *"all remaining rows inspected
and excluded as unrelated."* Two of them are `Mapping/Cartography` and `Navigation` —
in a cluster whose open question is what happens to a party that flees down a corridor
and does not know where it is.

The four prior diagnoses were: stopping at the page it found, at the index entry it was
given, at the paragraph it was quoted, and asserting a project fact without reading the
registry. The fourth class is the one above: **stopping at the edge of what the
rendering tool returned, and reporting that edge as the edge of the source.** It is a
harder failure to see than the first three, because the packet's own instruments all
say the page was opened — and the page *was* opened. Two-thirds of it just was not
there.

The remedy is small and the packets are close. Record the access limitation. Obtain
p. 84 from another rendition or issue the §9.2 stop. Name `Mapping/Cartography`,
`Navigation`, `Nature Lore` and `Mountaineering`, disposition them by inspection rather
than by blanket, and reconcile `Mapping/Cartography` against landed `EXP-003` by
reporting it, not adjudicating it. Fix the two owner IDs (`CHAR-011` → the p. 150
condition set has no owner; `CHAR-010` for Move Silently). Drop the inline hard-stop
label from `ENC-005`. Complete `EXP-006` §2's lists.

I set out to find omissions rather than to confirm the work, and I have said above
where I looked for each one, including the places I looked and found nothing (§5, §6).
Most of what these packets assert about the Rules Cyclopedia is exactly right, and I
verified it line by line against the printed pages rather than taking it on trust.

```text
EXP-006   PRIMARY-SOURCE COMPLETENESS: FAIL
ENC-005   PRIMARY-SOURCE COMPLETENESS: FAIL
```

**No file other than this review artifact was modified. No packet was edited, no Rule
Card drafted, no code written, nothing committed.**
