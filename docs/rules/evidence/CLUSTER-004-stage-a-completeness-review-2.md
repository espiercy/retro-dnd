# CLUSTER-004 — Independent Stage-A Evidence-Completeness Review (Pass 2)

```text
GATE:     INDEPENDENT COMPLETENESS REVIEW -- RULE_CARD_RESEARCH_PROTOCOL.md §10.1.2, §10.3
SCOPE:    docs/rules/evidence/EXP-006-evidence-remediated.md  (pass 2, full DEC-0010 re-run)
          docs/rules/evidence/ENC-005-evidence-remediated.md  (pass 2, bounded remediation)
SOURCE:   Dungeons & Dragons Rules Cyclopedia (TSR 1071, 1991) -- primary, RC only
DATE:     2026-09-29
REVIEWER: independent context; did not conduct the evidence collection being certified
```

> **This artifact is a completeness certification under §10.1.2. It is not a Rule Card, not a
> Stage-B synthesis, and not mechanically authoritative.** No mechanic is proposed, resolved or
> adjudicated here. Where this review quotes RC, it does so only to show that a governing object
> exists and what it says — establishing what it *means* is Stage B's job, after the gate clears.

---

## 1. Independence and method statement

I did not write, edit or advise on either remediated packet, did not conduct the evidence
collection, and have modified no repository file other than this one. I did not open any BECMI,
B/X, Holmes, OD&D or AD&D material; no alternate source was consulted.

Per §10.3 I began **from the source's own structure**, not from the packets:

1. `Index to Tables and Checklists`, RC p. 301 — read as a page image, **entry by entry**, both
   columns plus the Checklists list.
2. `General Index`, RC pp. 302, 303, 304 — read as page images, **all three complete**.
3. Chapter headings and the TOC region relevant to Ch. 4, 5, 6, 7, 8, 13, 14.
4. I then built my own candidate governing-object list, and only afterwards read the packets to
   see which candidates they had reached.

That order is what produced Findings 1 and 2 below: both are objects the **p. 301 Tables Index
and the General Index name**, that bear directly on the mechanic each card researches, and that
neither packet opened. Neither was reachable by starting from the packets' own checklists.

I did **not** re-grade pass 1. Where I refer to pass 1 it is only to check whether a numbered
finding of `CLUSTER-004-stage-a-completeness-review.md` was actually remediated (§8 below).

### 1.1 The packets were amended while this review was in progress

Both remediated packets were committed as `f474005` and then **further edited in the working
tree during this review**. I graded the **current working-tree state**, and I record the change
because one of my findings was materially affected by it.

```text
EXP-006-evidence-remediated.md   +28 / -? lines uncommitted
      adds E-11a (p. 92 Encounter Distance is surprise-gated); rewrites the
      Chance of Encounter Table negative; corrects the p. 68 Adventuring Gear
      boundary; adds Barding Table / Barding Encumbrance Table to §9.2
ENC-005-evidence-remediated.md   +10 / -? lines uncommitted
      adds N-4a / N-4b / N-4c (same p. 92 material); annotates §7.1 step 1
```

I re-verified the new material against the RC p. 92 page image myself: **E-11a, N-4a, N-4b and
N-4c are all exact as printed** (§4 and §6 below). The amendment **cures the load-bearing half
of what would otherwise have been my Finding 3/13** and is a genuine improvement — it also
supplies the governing procedure the p. 93 table sits inside, which §8 of the protocol requires.
It does **not** touch Findings 1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16 or 17, and it
**sharpens** Finding 5 against the packet rather than for it.

---

## 2. Verdicts

```text
EXP-006   PRIMARY-SOURCE COMPLETENESS: FAIL
```

```text
ENC-005   PRIMARY-SOURCE COMPLETENESS: FAIL
```

**Both failures are materially smaller than pass 1's, and I want that on the record.** Pass 2 is
a large improvement in both packets. Every transcription I re-verified against page images is
accurate to the letter with two exceptions noted below; the §5/§6 evidence map, the §6
confidence vocabulary, the §10.2 dispositions, the §10.2.1 reconciliation table and the §9.3
coverage checklist are all now present and used **verbatim**; the prior review's ten `EXP-006`
findings and six `ENC-005` findings are remediated with one exception each; there is **no scope
creep** in either packet; and **neither packet adjudicates a printed defect**.

A further amendment landed in the working tree during this review (§1.1) and improved both
packets again; I verified its new material and it is exact. **It does not affect either verdict**
— the four findings that drive them (1 and 2 for `EXP-006`, 11 and 12 for `ENC-005`) are
untouched by it.

What still fails is coverage, in the same structural way both times: **the indices were read as
lists of entries the researcher expected to matter, and objects whose titles do not contain the
card's vocabulary stayed outside the boundary.** `Attack Roll Modifiers Table` does not contain
the word "light." `Sample Skills Table` does not contain the word "tinderbox" or "lost." Both
are named in the p. 301 Tables Index. Both govern.

---

## 3. Findings — `EXP-006`

Severity key: **HIGH** = falsifies a stated conclusion, breaches a hard gate, or leaves a
governing object uninspected · **MED** = required content missing or a claim unsupported,
conclusions survive · **LOW** = record or accuracy defect.

### Finding 1 — **HIGH** — `Attack Roll Modifiers Table` (p. 108) is a named, light-conditioned, mechanically operative table that the packet never opens, names or dispositions

**Where I looked:** p. 301 `Index to Tables and Checklists`, entry `Attack Roll Modifiers Table
. 108`; General Index p. 302 `Attack rolls … 8, 9, 76, 105-107 / Modifiers … 108`; then RC
p. 108 as a page image, obtained this session.

**What RC prints, verified visually (p. 108, Ch. 8, *Attack Roll Modifiers*):**

```text
Attack Roll Modifiers Table
Circumstance                                    Attack Roll Modifier
Attacking from behind                           +2 bonus*
Attacker can't see target                       -4 penalty
Larger than man-sized monster attacks halfling  -1 penalty
Target exhausted                                +2 bonus
Attacker exhausted                              -2 penalty
 * Ignore defender's shield
```

**Why this is governing for `EXP-006`.** The packet's entire §5.1 is the consequence of a
character being unable to see — its E-2 records **−6 to all attack rolls** from p. 150. RC
prints, in its principal combat-modifier table, a **−4 penalty** for `Attacker can't see
target`. Whether these compose (a blind *character* at −6; a sighted attacker against an unseen
*target* at −4), whether one is a summary of the other, or whether they conflict, is a **Stage-B**
question. Stage A's obligation is to have the object on the record. It is not:

- **§3.2** (the p. 301 disposition list) does not contain it, and closes with *"No named table or
  checklist in the p. 301 index is left undispositioned."* That statement is **false**.
- **§9.2** (the Guardrail C `OPENED / VISUALLY INSPECTED / DISPOSITIONED` attestation) does not
  contain it. §9.5 Guardrail C: *"A named table may not silently exist outside the packet's
  coverage checklist."*
- **§9.1** does not list p. 108 among pages inspected.
- **§9.1 class I** (duplicate/parallel presentations) requires each presentation of the same
  mechanic to be recorded separately. This is the second presentation.

**Aggravating.** The pointer into this table is printed inside an object *both* packets read:
RC p. 104 `Retreat` — *"the same +2 that characters normally get for attacking from behind (see
the Attack Roll Modifiers Table on page 108)."* `ENC-005` §6.2 records following that
cross-reference *"to ownership only."* Following it one line further into the table's own rows
would have surfaced the `can't see target` row.

This is the `DEC-0010` §9.1.0 pattern exactly: a Tables Index entry present on an instrument the
packet says it read in full, bearing on the very mechanic being escalated, never opened.

### Finding 2 — **HIGH** — Chapter 5 (`Other Character Abilities`, pp. 81–86) is never inspected, and `Fire-Building` on p. 83 falsifies the packet's own tinderbox negative and its Q5 disposition

**Where I looked:** p. 301 Tables Index entries `Sample Skills Table . 82` and `Specialists and
General Skills Table . 133`; General Index p. 302 `General skills … 81-86, 133` and p. 303
`Skills … 82-85, 92` / `Skill check … 82` / `Skill roll … 82`; then RC p. 83 as a page image.

**What RC prints, verified visually (p. 83, col. 3, *Fire-Building*):**

```text
Fire-Building: This is the ability to start a fire without a tinderbox. A character
with a tinderbox and this skill is able to start fires automatically (no roll
necessary) in ordinary conditions. If the character is trying to build a fire without
a tinderbox, he will eventually succeed; he must make a 1d6 roll each round, and on a
1 or 2 he ignites the fire. If the character is trying to build a fire in adverse
conditions (during high winds or using wet wood), he must make a skill check with
penalties assigned by the DM.
```

Against the packet:

| Packet statement | Status |
|---|---|
| **E-30** presents the p. 70 tinderbox `1d6`, ignite on `1-2`, once per round as the tinderbox mechanic | **Incomplete.** RC qualifies it: with `Fire-Building`, a tinderbox-carrying character ignites **automatically, no roll**, in ordinary conditions |
| **§6.3:** *"No RC rule states an ignition chance for non-normal (wet) circumstances… Not located after inspecting pp. 69–70, p. 89 (weather/travel) and the General Index."* | **Survives only on the narrowest reading** ("chance" = a printed number). RC *does* supply a **procedure** for adverse conditions |
| **§8 Q5:** *"Tinderbox ignition outside normal circumstances… `RETAINED AS GENUINE SOURCE AMBIGUITY`. `PRIMARY PROCEDURE NOT YET ESTABLISHED` for non-normal conditions"* | **FALSIFIED.** RC establishes the primary procedure: a skill check with DM-assigned penalties. The §10.2.2 case-3 precondition ("all relevant governing objects inspected") is not met |
| **§6.3:** *"No RC rule states an ignition chance for non-normal (wet) circumstances"* — Guardrail B framing | The named research operations (pp. 69–70, p. 89, General Index) **did not cover** the object that answers it |

**Two further Ch. 5 objects on the same page bear on this card and are equally absent:**

- **`Blind Shooting`** (p. 83, col. 1): *"…typically used when the character is in darkness or
  when the target is outside the range of his sight or infravision… he needs an attack roll to
  hit the target, but the character doesn't suffer **the normal darkness penalties**."* This is
  RC **in its own voice** asserting that a category of "normal darkness penalties" exists, and
  printing an exception to it. It is directly on §5.1's subject, and it is one of the objects the
  prior review raised as Finding E-6 — which pass 2 does not address anywhere (§8 below).
- **`Food Tasting`** (p. 83, col. 3): *"the ability to taste food and water to see if they have
  spoiled."* This bears on **E-24**'s dungeon ration-spoilage mechanic, which §5.6 advances as
  the clearest candidate content for the card's *"& Exploration Resources"* half.

**`Sample Skills Table . 82` is a named p. 301 Tables Index object left undispositioned**
(Guardrail C), and `General skills . 81-86` / `Skills . 82-85, 92` are General Index entries
absent from §3.3, whose header claims the index was used *"as an **enumeration** instrument"*
and that *"Every entry below was read off the printed index pages and its target **opened**."*

I record that `CHAR-012 — General Skills` exists in `INVENTORY.md` (Unresearched) and that
routing Ch. 5 ownership there would be entirely defensible. **Routing is not the defect.** The
defect is that the chapter is neither enumerated nor dispositioned, and that a negative finding
and a `§10.2` disposition were written across it.

### Finding 3 — **MED** (was HIGH; **cured in substance mid-review**) — the p. 92 attestation preceded the inspection, and §2's blanket page-image claim still overstates the record

**Where I looked:** the shared scratchpad `…/scratchpad/rc/`, file timestamps; then RC p. 92 as
a page image.

As committed in `f474005`, §9.1 listed `p. 92 Ch. 7 Chance of Encounter Table` under
**"VISUALLY INSPECTED (page images)"**, §3.2 recorded it `OPENED`, §9.2 attested it `OPENED`
**and** `VISUALLY INSPECTED`, and §6.3's negative rested on it. `p. 92` is leaf 91. In the
shared scratchpad:

```text
leaf91.jpg   (p. 92)                  created 2026-09-29 05:41:23
EXP-006-evidence-remediated.md        written 2026-09-29 05:32:02
ENC-005-evidence-remediated.md        written 2026-09-29 05:35:05
pass-2 download window                        05:19:54 - 05:23:24
      (leaf103/p.104, leaf100/p.101, leaf86/p.87, leaf88/p.89 -- no p. 92)
```

**Every other page in either packet's §9.1 list is present and predates the packets.** p. 92 was
the single exception, and it arrived roughly nine minutes *after* the attestation was written.

**This has since been cured, and cured properly.** The working-tree amendment (§1.1) opens p. 92
and adds real content from it — `EXP-006` E-11a, `ENC-005` N-4a/N-4b/N-4c — which I verified
against the page image and found **exact** (§4, §6). The attestation is now true. I record the
sequence rather than deleting it, because the protocol's concern is not only whether a page was
eventually read but whether a `VISUALLY INSPECTED` attestation may be written before it is: this
is the same class of defect as the prior review's Finding E-8, which pass 2 itself corrected at
§2.1 as *"false when written."* **The correct response is the one that was taken** — open the
page and put its content on the record.

**What still stands.** §2 states: *"Every page cited in this packet was read as a page image.
There are no OCR-only findings in this packet."* §3.2 marks `OPENED`: `Passage Table` (p. 72),
`Forced Marches Table` (p. 121), `Natural/Unnatural Events Table` (p. 142), `Magical Item
Subtable: 5` (p. 229), `Room Contents Table` (p. 261), `Pre-Game Checklist` (p. 262). **No page
image for any of those six exists in the scratchpad, at any time.** §3.3 additionally marks
`yes` (inspected) for index targets on pp. 5, 10, 24, 25, 62, 65, 66, 89, 119, 121, 125, 146,
147, 148, 152, 256, 257. §2's blanket claim is not sustainable as written.

### Finding 4 — **MED** — the §9.3 Coverage Checklist and §3.3 disagree about what was inspected, so the checklist is not the auditable record §9.3 requires

§9.1 lists **17** pages as visually inspected (68, 69, 70, 91, 92, 93, 98, 99, 100, 104, 149,
150, 154, 301–304). §3.3 marks **"yes"** in its `Inspected` column for index targets on roughly
**20 further pages** that §9.1 never mentions, and its header says each target was *"opened."*

§9.3 exists so that *"a future reviewer must be able to ask 'what primary-source objects could
govern this mechanic, and did the researcher actually inspect each one?' and get a checkable
answer."* Here the two sections give different answers, and the reviewer cannot tell which is
the record. Reconciling them is a small edit; leaving them contradictory defeats the section.

### Finding 5 — **MED** — E-13 is classified `NECESSARY CONSEQUENCE`, but the nearest competing primary passage sits unrecorded on a page the packet transcribes, and the falsification pass never tested it

**Where I looked:** RC p. 91 as a page image, both columns.

E-12/E-13 derive that RC treats *"normal dungeon conditions"* as the `Dim light` row because
Game Turn Checklist step 1's `2d6 x 10'` matches exactly one Dungeon row of the p. 93 table.
Step 1's text and the three Dungeon rows are **both verified correct** (§4 below).

But RC states the same distance again, one column over, **with no visibility qualifier at all**
(p. 91, col. 2, *Wandering Monsters*):

```text
When a DM's roll indicates that wandering monsters will appear, they appear the
following turn. The DM rolls 2d6 and multiplies this number by 10; the result is the
distance, in feet, at which the monsters are detected.
```

That is a live competing reading: `2d6 x 10'` may be a **flat wandering-monster detection
rule**, not a light classification. §6 defines `NECESSARY CONSEQUENCE` as *"a logically forced
arithmetic/mechanical consequence of two or more `DIRECT PRIMARY TEXT` facts."* Equality of a
value between two passages does not force identity of category, so the row is at best
`QUALIFIED`. §10's falsification table tests only *"'Normal dungeon conditions' = `Very good
light`"*; it never tests *"the 2d6×10' is not a visibility statement at all."* The competing
sentence is on a page the packet quotes from and is nowhere in the packet.

Step 1's own cross-reference (*"see the 'Encounter Distance' section, below"*) does support the
link and should be weighed — but weighing it is the work, and it was not shown.

**The mid-review amendment makes this worse, not better.** New E-11a correctly establishes that
RC consults the `Encounter Distances Table` **only when neither party is surprised**; when
either is surprised the distance is a flat `1d4 x 10'`. But the Game Turn Checklist's
`2d6 x 10'` is stated at **step 1**, when wandering monsters *arrive* — before surprise is rolled
at Encounter Checklist step 2. So on the packet's own newly transcribed procedure, step 1's
value is produced at a point in the sequence where the light-keyed table has not yet been
reached. E-13 and E-11a are now in tension inside one packet, and neither §5.3 nor §10 addresses
it. E-13 must be re-derived against E-11a or downgraded.

### Finding 6 — **MED** — the `Waterskin` is absent, although the packet marks `Dehydration . 150` GOVERNING and the prior review named this object explicitly

**Where I looked:** RC p. 69 `Adventuring Gear Table` row and RC p. 70 description, both as page
images.

```text
p. 69 table:  Waterskin/wineskin   One-quart capacity; enc 30 when filled   1 gp   5
p. 70 prose:  "Waterskin: This flexible container is usually made of leather or a
               preserved animal bladder. It has a liquid capacity of one quart and an
               encumbrance of 30 cn when filled, 5 cn when empty."
```

§3.3 records `Dehydration . 150` as **GOVERNING** (jointly with Starvation). E-14 records `No
Water 1d8/day`. §5.6 develops rations at length as a dungeon-conditioned consumable. The single
RC object that holds water — the only water container in the gear catalog, and the paired input
to the dehydration side of the very table the packet transcribes — appears nowhere in the
packet, in a section (§5.7) that claims to have read the p. 69/70 description column *"as a
complete unit (§9.7)."* The prior review's remediation item 3 said in terms: *"Note the p. 70
Waterskin capacity as the paired input to the dehydration rule."*

### Finding 7 — **MED** — §3.3 routes p. 147 to an "unowned" responsibility that `INVENTORY.md` in fact assigns, and to a `§8` item that does not exist

§3.3:

> `Doors` / `Open doors` / `Secret door` | 10, 147 | … Routed → **unowned dungeon-interaction
> responsibility (§8 open item)**

`INVENTORY.md` line 102: `EXP-005 | Searching, Listening, Doors & Secret Features | Dungeon
Adventures chapter; **Chapter 13 (p. 147)** | … | Unresearched`. The responsibility is owned and
named, on the exact page cited. The packet routes the `Chance of Encounter Table` to `EXP-005`
four rows earlier in the same document, so the ID was in hand.

Separately, **`§8` contains no such open item** — Q1–Q10 are light mapping, burn tracking,
timetrack scope, rations, tinderbox, starvation table, `CHAR-005` check, starvation causation,
light-vs-surprise, and burn-out. The cross-reference is dangling.

### Finding 8 — **LOW** — §3.2's closure sentence is a source-property claim the list does not support

*"No named table or checklist in the p. 301 index is left undispositioned."* Reading p. 301
entry by entry, the following named objects are not in §3.2's list and not excluded by name
anywhere in the packet: `Attack Roll Modifiers Table . 108` (Finding 1), `Sample Skills Table
. 82` (Finding 2), `Clerics and the Create Food Spell Table . 125` — which the **prior review
flagged as unfollowed** and which pass 2 reaches only obliquely through the `Food . 89, 121,
125` index row — `Miscellaneous Siege Equipment Table . 74`, `Survival in the Elemental Planes
Table . 264`, `Magical Items Main Table . 228`, `Dungeon Encounters Levels 1-10 Tables . 94`,
`Target Cover Table . 108`.

I opened or checked the last five myself and **found nothing that governs this card**: the siege
table is belfries, galleries, mantlets and timber forts; `Target Cover Table` is physical cover
(`1/4` / `1/2` / `3/4` / full, soft and hard), not concealment by darkness; `Survival in the
Elemental Planes` is Ch. 18 planar. I record them so the boundary is checkable, not because they
change the card. The defect is the **unqualified closure sentence**, which is the same class of
statement §9.5 Guardrail B exists to prevent — and it is a *new* overclaim introduced in pass 2,
in the section that replaced the one pass 1 was failed for.

Also unenumerated: General Index `Special defenses … 24, 25, 27, 154`. I followed it: RC p. 27
*Woodland Abilities* — *"if a halfling finds some **deep shadows** or cover to hide in, his
chance drops to 33%; if he cannot find shadows or cover, he has **no chance at all**."* That is
a light-conditioned per-entity ability. It is plainly `CHAR-009`/`CHAR-002`'s to own, and I make
no claim that `EXP-006` should absorb it — only that the entry is not enumerated by a section
claiming enumeration.

### Finding 9 — **LOW** — §5.5's conclusion and its own E-22 are in tension

§5.5 concludes *"RC supplies a manual bookkeeping instrument (E-19, E-22) and **no executable
decrement procedure**."* E-22, on the same page, records RC's text: *"As game time passes,
**deduct from all magical effects durations**"*, and the alternate *"mark on the timetrack the
exact game time when the effect disappears. When that much time has been marked off, the DM
knows that the spell effect has ended."* Those are decrement procedures, stated for magical
effects. Q3 partly rescues this by asking whether they extend to light durations; the flat
sentence in §5.5 should be qualified to match E-22.

I separately confirm the **substantive** disposition: having read p. 149 in full, the
`Timetrack Table` **is** four rows of consecutive integers to mark off (28 / 24 / 6 / 60), the
surrounding prose is DM record-keeping advice, and *"the timekeeping note sheets can be
discarded after the adventure is over."* **The packet is right that it is a tally sheet and not
a procedure, and right that it creates no second time authority.** That question, asked directly
in the direction, is correctly answered.

### Finding 10 — **LOW** — hard-stop vocabulary used as an inline label

§8 Q5 carries `PRIMARY PROCEDURE NOT YET ESTABLISHED` — a §17 **hard-stop message** — inside a
row otherwise dispositioned `RETAINED AS GENUINE SOURCE AMBIGUITY`, while §19 recommends
`EVIDENCE READY FOR HUMAN REVIEW`. Whatever Finding 2 does to that row on the merits, the two
vocabularies should not be mixed: §10.2's four dispositions and §17's stop messages are
different instruments.

---

## 4. What I verified as CORRECT in `EXP-006`, and where I looked

All of the following I checked **against page images myself**, not against the packet.

| Packet claim | Where I looked | Result |
|---|---|---|
| **p. 150 `Blindness`** — cause *"without infravision … area of complete darkness"*; **−4** saves, **−6** attacks, **+4** AC; **one-third** unguided, *"measured in **feet**, not yards"*; **two-thirds** guided, yards outdoors; mounted-and-guided = no penalty | p. 150 image | **E-1 – E-5 exact.** The verbatim block in §5.1 matches the printed page word for word, including *"he has to guess where his target is by hearing"* and the ellipsis after *"one-third his normal speed"* |
| **p. 154 `Blindness`** — *"fighting in the dark without infravision can result in blindness"* + *"See 'Special Character Conditions' in Chapter 13"* | p. 154 image, magnified | **E-6 exact**, cross-reference confirmed. Correctly recorded as a §9.1 class-I duplicate presentation |
| **p. 93 `Encounter Distances Table`** — all 13 rows and all 3 footnotes | p. 93 image | **Exact.** Dungeon `Very good light 4d6x10'` / `Dim light** 2d6x10'` / `No light† 1d4x10'`; `* Or other indoor setting.`; `** Or full darkness with infravision used.`; `† Or very poor visibility (heavy snow or fog, sandstorm, etc.).` **E-7 – E-10 confirmed**, including the feet/yards split |
| **p. 91 Game Turn Checklist step 1** — *"Under normal dungeon conditions, they appear 2d6 x 10' away in a direction of the DM's choice"* | p. 91 image | **E-12 exact.** (The *derivation* built on it is Finding 5) |
| **p. 98 `Contact`** — *"only within visual range … the DM determines the encounter distance"* | p. 98 image | **E-11 exact** |
| **p. 92 `Encounter Distance` — E-11a (added mid-review)** — both surprised → `1d4 x 10'`; one surprised → unsurprised notices at that distance, surprised side not until **half**; neither surprised → consult the `Encounter Distances Table` | p. 92 image | **Exact as printed.** The surprise gate is real and is a materially useful qualification of §5.2 — *"When neither party is surprised, take a look at the Encounter Distances Table."* Correctly reinforces the `ENC-001`/`ENC-002` routing rather than claiming it |
| **p. 92 `Chance of Encounter Table` has no light or visibility column** | p. 92 image | **Confirmed.** Its columns are `Type of Encounter` / `Roll Method`, plus a `Type of Terrain` / `Chance` sub-table with an ocean and an aerial footnote. The amended §6.3 bullet is accurate |
| **p. 150 `Starvation Table`** — `1d2` / `1d8` / `1d10` per day; band rows `6h/No Penalty/No Penalty`, `8h/x3/4/-2`, `10h/x1/2/-4`, **`12h/x 3/4/-6`** | p. 150 image | **Exact, including the printed `x 3/4` at 75%-99%.** E-14 – E-18 confirmed; the worked example `10/32 = 0.3125` and the monsters clause are on the page |
| **`SR-10` claim — both halves** | `docs/rules/character_creation/encumbrance_and_movement_rate.md` | **Both verified.** §"`SR-10` — Starvation movement progression is `×3/4 → ×1/2 → ×1/4`"; provenance table row *"Starvation, 75–99% \| × 1/4 \| `SR-10` — RC prints `× 3/4`"*; approved cases **M57** (*"`30'` — `× 1/4` per `SR-10`. Must **not** be `90'`"*) and **M58** (*"multipliers are monotonic"*). The card records the printed value as RC Explicit and the ruling separately. **E-18 is correctly *not* claimed as a new defect** |
| **p. 149 `Timekeeping` / `Timetrack Table`** | p. 149 image | **E-19 – E-22 exact**; row lengths 28 / 24 / 6 / 60 confirmed |
| **pp. 69–70 items** — torch `30'` / *"one hour (six turns)"*; lantern `30'` / *"one flask of oil in four hours (24 turns)"* / *"shuttered or enclosed against wind"*; oil *"poured out and ignited to delay pursuit"*; tinderbox `1d6`, ignite on `1 or 2`, *"once per round"*; **mirror** *"The area must be lit for the mirror to work this way"*; rations `21 meals`, standard *"spoil overnight"*, iron *"two months (eight weeks) … up to a week in bad conditions (such as dungeons)"* | pp. 69, 70 images | **E-23 – E-31 all exact.** E-31 (mirror) is a genuine new find and is correctly on-card. (Finding 2 qualifies E-30; it does not impeach the transcription) |
| **"RC's General Index has no `Light`, `Lantern`, `Tinderbox` or `Flask` entry"** | pp. 302, 303, 304 images | **TRUE, verified.** p. 303 runs `Lifeboat 71 → Lightship 146 → Listening 147`; no `Light`. No `Lantern` between `Land travel` and `Languages`. p. 304 runs `Timekeeping 149 → Titles 135 → Torch`; no `Tinderbox`. p. 302 runs `Fire maneuver 103 → Food`; no `Flask` |
| Index citations `Torch . 62, 66, 69, 70`; `Oil . 62, 65, 69`; `Rations . 69`; `Adventuring gear . 68-70`; `Blindness . 150, 154`; `Starvation . 150`; `Timekeeping . 149`; `Record keeping . 148, 149`; `Mapping . 5, 148, 256, 257`; `Food . 89, 121, 125` | pp. 301–304 images | **All exact as printed**, including the `68`-not-`69` correction the packet makes |
| §6.3 negative: light is not an input to surprise, reaction, or wandering-monster frequency | pp. 91, 93 images | **Confirmed.** Encounter Checklist step 2 is a flat `1d6`, `1-2` surprised; step 4 routes to the `Monster Reactions Table` (`2d6`, Charisma-adjusted only); p. 91's raise-the-rate list is *"Loud noises, battles, cursed items, or exploring special areas"* — no light term. The Guardrail-B framing of these three is correct |
| `Land Transportation Gear Table` (p. 70) = Saddle & Tack, Saddle Bags, Cart, Wagon only | p. 70 image | **Confirmed**; exclusion correct |
| `CLUSTER-004-BOUNDARY-CORRECTION.md` §6 item 8 — starvation causation has no Rule ID | that file; `INVENTORY.md` | **Confirmed.** Item 8 reads *"Starvation has no Rule ID anywhere in the inventory, and is a causation owner"*; `CLUSTER-004-BOUNDARY-PROPOSAL.md` independently records *"starvation has **no Rule ID assigned at all**"* |

**Scope creep — I looked for it specifically, and found none.** I checked for absorption of
encounter generation, surprise, reaction, initiative, general blindness causation, starvation
causation, generic condition infrastructure, `EXP-004`, `EXP-010`, and the
`EXP-008`/`MON-001`/`TREAS-001` stocking knot. §7.1 declines each by name and the body holds to
it. The seams are respected: no price, encumbrance, `Coin`, quantity-pricing or legality fact is
restated (`CHAR-004`); no second dungeon-time authority is created (`EXP-002`); no movement rate
is re-derived (`CHAR-005`); ordinary dungeon movement is untouched (`EXP-003`). Magical light
(`Oil of darkness / moonlight / sunlight`, `light`, `continual light`) is routed to `MAGIC-*`
with nothing transcribed. **No mechanic is drafted. No printed defect is adjudicated.**

---

## 5. Findings — `ENC-005`

### Finding 11 — **HIGH** — the `Caving` skill (p. 83) is a governing object for checklist step 6, and the packet declares it `BLOCKED` over a single page it never opened

**Where I looked:** p. 301 `Sample Skills Table . 82`; General Index `Skills . 82-85, 92` — an
entry the packet *does* enumerate — then RC p. 83 as a page image.

**What RC prints, verified visually (p. 83, col. 2, *Caving*):**

```text
Caving: This is an ability to always know where one is while exploring underground
caves, cavern complexes, rivers, etc. A character with this skill will automatically
know the route he has taken to get where he is (if he was conscious all the time).
Many dwarves have this skill.
    The Caving skill can also be used in a maze. Skill checks are necessary when the
character has become disoriented. If he is forced to flee for a long stretch, he must
make a skill check to keep from being lost. (Characters without this skill
automatically become lost in such a situation.)
```

That is a printed procedure for **becoming lost as a consequence of fleeing** — which is this
card's step 6, `Regain Bearings`, entered from a chase. Against the packet:

| Packet statement | Status |
|---|---|
| **N-22 / §5.5:** RC states the lost **condition** in a dungeon *"at DM discretion"*; it supplies a **die-roll procedure only for wilderness travel** (`1d6`, Game Day step 2). *"So: no dungeon getting-lost **procedure**."* | **Falsified as stated.** p. 83 supplies a dungeon-side procedure — skill check, or automatic loss without the skill — keyed to exactly the flight case |
| **§6.3:** the section's negatives, framed as research operations over pp. 91, 93, 98–100, p. 88, p. 103 | Correctly framed, but **the named operations do not cover p. 83** |
| **§8 Q8:** *"Does `CHAR-012`'s Caving skill modify step 6?"* → **`BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED`** *for `CHAR-012`* … *"**Not** a gap in `ENC-005`'s own coverage."* | **It is a gap in coverage.** §10.2: a packet *"may **not** contain **unfinished source inspection disguised as an ambiguity**."* The material is one page, in the primary source, reachable from an index entry the packet enumerates. `p. 83` is absent from §9.1 |
| **§7.1** step 6 provider column: *"lost = **unowned in dungeons**"* | Inconsistent with the packet's own Q8, which treats `CHAR-012` as a candidate provider. `CHAR-012` exists in `INVENTORY.md` (Unresearched) and its notes name a *"catalog-closure obligation over the V1-reachable general-skill list"* |

Two Ch. 5 neighbours compound it, both on p. 83: **`Endurance`** (*"able to run … for an hour
without collapsing … must rest for three times the amount of time"*) and the p. 88 running rule
the packet does cite, which itself says *"(Characters with the optional `Endurance` skill can
maintain this pace for longer periods of time.)"* — i.e. **RC's own 30-round running limit
cross-references Ch. 5**, and that is precisely the subject of Q4.

### Finding 12 — **HIGH** — §17: a packet carrying a `BLOCKED` closure-gate item may not recommend `EVIDENCE READY FOR HUMAN REVIEW`

Independently of whether Q8 *should* have been `BLOCKED`, §17 states:

```text
An open-question closure-gate item (§10.2) is classified
  BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED
                                          →  STOP — MORE PRIMARY RESEARCH REQUIRED
```

§8 Q8 is classified `BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED`, verbatim. §19 recommends
`EVIDENCE READY FOR HUMAN REVIEW`. The packet's attempt to scope the blockage away ("for
`CHAR-012` … not a gap in `ENC-005`'s own coverage") is not one of §10.2's four dispositions:
if the item genuinely belongs to another card, the disposition is `CONFIRMED OUT OF SCOPE (with
explicit ownership and rationale)`, which the packet uses correctly five rows away for Q2, Q7
and Q9. As written the packet is internally inconsistent with the hard-stop table. This is
fixable by a correct classification **only after** Finding 11 is discharged.

### Finding 13 — **LOW** (**cured mid-review**) — p. 92 visual-inspection attestation

Same evidence as Finding 3: `ENC-005` §9.1 listed `p. 92` under *"Structural units inspected —
**all as page images**"* and §2.1 states *"No finding in this packet rests on OCR"*, while no
p. 92 image existed in the shared scratchpad until 05:41:23, after the packet's 05:35:05 mtime.

**Cured by the working-tree amendment**, which adds N-4a, N-4b and N-4c from the page. I verified
all three against the image and they are **exact**. N-4a in particular is a real improvement to
this card: it establishes that step 1's encounter distance is **gated on surprise**, which
tightens the `ENC-002` dependency in §7.1 and is the kind of governing-procedure context §8
requires. Recorded as LOW, and closed.

### Finding 14 — **MED** — `Exhaustion . 88` is not enumerated, and the p. 88 exhaustion rules governing step 5 have no evidence row

**Where I looked:** General Index p. 302 `Exhaustion … 88` and `Encumbrance / Effect on movement
… 88`; p. 304 `Speed … 88`; then RC p. 88.

§3.3 is headed *"General Index — **enumerated**, not cited (precedent `P-001`)"* and lists 20
entries. `Exhaustion . 88` is not among them, although it is the index entry for the subject of
the packet's own Q4. RC p. 88 states:

```text
A character can run at maximum speed for 30 rounds at most (5 minutes) before becoming
exhausted. (Characters with the optional Endurance skill can maintain this pace for
longer periods of time.)
...
An exhausted character must rest for at least three turns (30 minutes) before running
or fighting again. ... Monsters gain a +2 bonus to their attack rolls to hit the
character ... and the character must subtract 2 from all attack damage rolls.
A character who becomes exhausted but is forced to continue running cannot use his
maximum running speed. He drops to encounter speed and cannot move any faster until
he has rested.
```

Checklist **step 5 conducts the chase at running speed**, and step 5b's capture condition is
*"superior speed."* "Drops to encounter speed" is therefore a printed mechanical event inside
this card's own procedure. None of it appears in §5. The packet's Q4 is dispositioned
`RETAINED AS GENUINE SOURCE AMBIGUITY`; §10.2.2 case 3 requires *"all relevant governing objects
inspected"* and *"the completeness reviewer confirms no obvious governing material remains
uninspected."* I cannot so confirm while the exhaustion rule that step 5 collides with is
unrecorded, and while the `Endurance` skill RC itself names as the exception is uninspected.

The routing (`CHAR-005` §9 / `EXP-004` own it) is not in question and I am not asking the card
to claim them. Recording them is.

### Finding 15 — **MED** — the "verbatim, visually verified, re-verified here" Evasion Checklist drops a clause from step 5b

Magnified crop of p. 99, printed:

```text
b. The evading party is caught by the pursuers (because of superior speed or
   terrain obstacles). Combat occurs; go to the Combat Checklist in Chapter 8.
```

Packet §5.2:

```text
b. The evading party is caught by the pursuers (because of superior speed or
   terrain obstacles); go to the Combat Checklist in Chapter 8.
```

`Combat occurs;` is dropped and the sentence boundary altered. Small in itself — but the block
is introduced as *"Verbatim, visually verified… pass 1's transcription, confirmed by the
independent reviewer as exact, and **re-verified here**,"* and *"combat occurs"* is RC's own
statement of the **consequence** of capture, not merely a pointer to another checklist. A
re-verification pass that reproduces an inherited elision has not re-verified. **Every other
line of the checklist and every cell of the Evasion Table is exact** (§6 below).

### Finding 16 — **MED** — governing content on pp. 98–99, inside the section the packet says it read as one complete unit, has no evidence row

Verified on the p. 98 and p. 99 images; none of the following appears in §5:

1. **The catch-up determination** (p. 99, col. 3) — *"If the pursuers end one round having caught
   up to the evaders (**the DM should be keeping track of their relative positions to determine
   this**) and then **win initiative the next round**, they can attack, forcing the evaders to
   turn and fight."* This is the mechanical entry condition for step 5b and the reason step 5's
   `1d6` initiative matters. It is the most procedurally load-bearing sentence on the page after
   the `d100` direction.
2. **The obstacle branch** — *"Or the evaders could run into some obstacle that prevents them
   from continuing (a sheer cliff face, a dead-end hallway, a magically locked door, another
   party of enemies, and so on). In these situations, combat usually results, though the evaders
   might choose to surrender instead."*
3. **Open-ended DM adjustment** (p. 99, col. 1) — *"The DM **may adjust** evasion chances for
   terrain, differences in speed, **and other factors**…"* — the table's condition column is not
   closed, which matters to any executable reading of it.
4. **Area familiarity** (p. 99, col. 1) — *"If monsters are familiar with an area, they may be
   able to evade pursuers by rapidly turning corners, closing doors behind them, and so forth."*
   A printed evasion factor absent from both the table and the packet.
5. **Step 2's automatic evasion has movement content** (p. 98 → p. 99) — *"it may automatically
   evade the surprised group by **turning away and moving off at another direction at running
   speed for one round**. The nonsurprised group has enough time to get clear of the area…"*
   N-6 records only "skip to step 6."

§9.2 claims the section was read *"**as one complete source unit**, pp. 98→100, not as isolated
search windows."* I believe it was — these are not search-window misses. They are evidence-map
omissions, and §11 item 5 makes the evidence map the record.

### Finding 17 — **LOW** — N-19 elides the die's gating condition

Printed, p. 100 col. 1: *"…the DM rolls `1d6` ***if*** *he or she feels that the item dropped is
indeed appealing to the monster*."* N-19's ellipsis removes the italicised condition. The `1d6`
is not rolled unconditionally; the DM's appraisal gates it. §8's *"entry conditions and exit
conditions"* requirement makes that the operative half.

---

## 6. What I verified as CORRECT in `ENC-005`, and where I looked

| Packet claim | Where I looked | Result |
|---|---|---|
| **`Evasion Checklist`, p. 99** — steps 1, 2, 3, 4, 5, 5a, 5c, 6 | p. 99 image + two magnified crops | **Exact, word for word**, including *"go to Step 2"*, *"every *five rounds*"*, *"when terrain and circumstances warrant"*. One clause dropped at 5b (Finding 15) |
| **Printed defect — step-2 self-loop** | p. 99, magnified | **Confirmed printed.** *"If the other party is not surprised, **go to Step 2**."* Not an OCR artefact. Correctly **left unadjudicated** |
| **`Evasion Table`, p. 99** — 12 party/monster bands and 5 condition rows | p. 99 image | **Exact.** `1-4`: 50/70/90; `5-12`: 35/50/70; `13-24`: 25/35/50; `25+`: 10/25/35. `Wooded +25%`, `Featureless -15%`, `Pursuers twice as fast -25%`, `Evaders twice as fast +25%`, `Scouts in place -15%` |
| **`d100` direction (N-10)** | p. 99, col. 1 | **Exact:** *"The DM rolls a `d100`; on a `01-70`, the PCs have successfully evaded the monsters, and on a `71-00`, the monsters successfully pursue the characters."* Prior finding N-3 **remediated** |
| **5% floor (N-11)** | p. 99, col. 1 | **Exact:** *"Important Note: Regardless of the number of evasion penalties, the evading group always has at least a 5 % chance to evade."* |
| **Printed defect — scouts `-10%` prose vs `-15%` table** | p. 99, both magnified | **Confirmed printed, both on p. 99.** Correctly **left unadjudicated**; §10.2.2 case-3 handling is right on the objects inspected |
| **N-12 split parties; N-13 symmetric speed adjustment** | p. 99, col. 1 | **Exact**, including the parenthetical that states the symmetry explicitly |
| **N-16 / N-17 terrain** | p. 99, cols. 1 and 3 | **Exact.** Examples only, no criterion; the second Evasion Table roll on reaching difficult terrain while temporarily out of vision range is printed as described |
| **p. 100 col. 1 — dropped goods `1d6` / `1-3`; `Regain Bearings` subheading; full-running-speed-every-round + rest; lost in *"unexplored dungeon levels"*** | p. 100 image | **All four confirmed**, and `Regain Bearings` **is** a printed subheading. Prior finding N-1 **remediated**; the column reclassification is correct |
| **p. 104 — `Retreat` AND `Fighting Withdrawal` both carry the running-speed bridge** | p. 104 image | **Confirmed.** Both entries end *"If the character is not in hand-to-hand combat with his enemy when his movement phase comes up in the next round, he can go to running speed that next round."* N-24 (*"greater than half his encounter speed, up to his full encounter speed"*), N-25 (`5'`/round), N-26 (shield forfeit, `+2`, *"the same +2 … for attacking from behind"*) all exact. Prior finding N-6 **remediated** |
| **`Combat Maneuvers Table`, p. 104** | p. 104 image | **Confirmed.** 13 rows; `Fighting Withdrawal` and `Retreat` both `Hand-to-hand phase` / `All characters` |
| **p. 98 `Contact`** | p. 98 image | **Exact**, including *"only within visual range"* and *"the DM determines the encounter distance and the parties' relative states of surprise"* |
| **N-4a / N-4b / N-4c (added mid-review)** — encounter distance surprise-gated; *"One Group Is Surprised: The unsurprised group can take advantage of the situation by evading (automatic success, meaning that the other group doesn't notice them at all)"*; *"both sides roll `1d6`. Each side that rolls a `1` or `2` is surprised."* | p. 92 image | **All three exact.** N-4b is a genuine find: it is the **source** of checklist step 2's automatic success, one chapter-section earlier than the checklist, and it is correctly recorded as `ENC-002`'s and **not claimed** |
| **Entry conditions: p. 91 Game Day 4b; p. 93 Encounter Checklist 5c; p. 91 definition of evasion** | pp. 91, 93 images | **All three exact.** *"If the characters want to evade or pursue encountered monsters, the DM goes to the 'Evasion and Pursuit' section later in this chapter."* / *"If so, use the pursuit and evasion rules later this chapter to see if the PCs get away."* / *"'Evasion' is what happens when an encounter occurs and one side wants to escape the other; that side turns and runs."* Prior finding N-2 **remediated** |
| **p. 98 Definitions map 1:1 onto the six checklist steps** | p. 98 image | **Confirmed.** RC states it itself: *"The terms used in the Evasion Checklist are defined in the following subsections and are presented in the order that they are most likely to occur."* `Regain Bearings` is the sixth and is on p. 100 — the packet's argument for why pass 1's exclusion was wrong is sound |
| **§7.1 six-step dependency table — providers and statuses** | `docs/rules/INVENTORY.md`; pp. 93, 99, 102, 103 | **Correct.** `ENC-001` Encounter Distance — Unresearched; `ENC-002` Surprise — Unresearched; `ENC-004` Monster Morale — Unresearched, *RC Optional → Project-Selected: REQUIRED (`DEC-0008`)* exactly as the packet annotates; `MON-003` — Unresearched; `COMBAT-006` Combat Sequence, Initiative & Timing — Unresearched; `CHAR-005` landed. `ENC-005`'s own listed dependencies are `EXP-002`, `EXP-003` (both `VERIFIED`), so the inventory-vs-procedure gap the packet reports is real. **Four of six is right**; step 4 is the only wholly owned step. Step 6's provider column is the one defective cell (Finding 11) |
| **§7.2's `EXP-010` precedent — "THREE unresearched consumers"** | `CLUSTER-004-BOUNDARY-CORRECTION.md` §4 | **Exact.** The record names `ENC-002`, `ENC-003`, `COMBAT-006`, *"All three are unresearched"*, and defers. The packet presents the comparison as an observation, not a recommendation — correct |
| **§6.3 `EXP-010` negative — no marching-order input** | pp. 98–100 images | **Confirmed.** The procedure consumes party **size** only. `EXP-003` case `D32` is consistent |
| **`Charge . 154` terrain list** | p. 154 image | **Exact**, and correctly **not** imported as a generic terrain mechanic |

**Scope creep — I looked for it specifically, and found none.** I checked for absorption of
generic terrain, marching order, combat-maneuver ownership, initiative, surprise, reaction and
morale. §5.4's *"terrain adjusts a percentage, not a rate"* distinction is correct on the printed
text and is held. `Terrain Effects on Movement Table` (88), the `Charge` terrain list (154) and
the Mystic rough-terrain material are each excluded **by name**. The maneuvers are explicitly
`COMBAT-*`'s and are not claimed; `ENC-002`/`ENC-003`/`ENC-004`/`COMBAT-006` are routed as
providers only; `EXP-004` is followed only to ownership; `CHAR-004` is not reopened; the
wilderness/city subtables, `Castle Reactions Table`, `Ship Evasion Table` and `Balancing
Encounters` are excluded by name. **No mechanic is drafted. Neither printed defect is
adjudicated** — both are recorded as printed and escalated, which is the correct §10.2.2
behaviour.

---

## 7. §10.2.1 reconciliation table — every open statement in both pass-2 packets

| Open question / statement | Object implicated | Inspection completed? | Result | Owner | Still blocks completeness? |
|---|---|---|---|---|---|
| **EXP-006 Q1** — does a party with torches produce `Very good light` or `Dim light`? | pp. 91, 93, 69–70, index p. 301 | **Yes** for those objects; **no** for p. 108 | Genuine RC silence on the mapping. Survives Finding 1 (p. 108 adds a modifier, not a mapping) | `EXP-006` | **No** — `RETAINED AS GENUINE SOURCE AMBIGUITY` |
| **EXP-006 Q2** — burn-tracking in scope? | p. 149, pp. 69–70 | **Yes** | Correctly answered; qualify per Finding 9 | `EXP-006` | No |
| **EXP-006 Q3** — is the timetrack method meant for light durations? | p. 149 | **Yes** | Genuine silence | `EXP-006` | No |
| **EXP-006 Q4** — do rations belong to this card? | p. 69, index `Rations . 69` | **Yes**, but **p. 83 `Food Tasting` not inspected**; **Waterskin not recorded** | Evidence incomplete on the resource half | human owner | **YES** — see Findings 2, 6 |
| **EXP-006 Q5** — tinderbox outside *"normal … circumstances"* | pp. 69–70, 89, General Index | **No — p. 83 `Fire-Building` uninspected** | **FALSIFIED.** RC states the procedure | `EXP-006` / `CHAR-012` | **YES** — `BLOCKED — MORE PRIMARY-SOURCE RESEARCH REQUIRED` |
| **EXP-006 Q6** — Starvation `75%-99%` `× 3/4` | p. 150; `CHAR-005` card | **Yes, both** | Correctly `CONFIRMED OUT OF SCOPE`; `SR-10` verified; no new defect claimed | `CHAR-005` | No |
| **EXP-006 Q7** — does landed `CHAR-005` record the printed value? | `encumbrance_and_movement_rate.md` | **Yes** | **Confirmed.** RC Explicit and `SR-10` are separated exactly as §7 requires | — | No |
| **EXP-006 Q8** — who owns starvation causation? | `INVENTORY.md`; `BOUNDARY-CORRECTION` §6.8 | **Yes** | Confirmed still unassigned; correctly not absorbed | human owner | No |
| **EXP-006 Q9** — does light modify surprise / reaction / wandering frequency? | pp. 91–93, index | **Yes** | **Confirmed negative**, properly framed | `EXP-006` | No |
| **EXP-006 Q10** — light source burning out mid-turn | pp. 69–70, 91, 149 | **Yes** | Genuine silence | `EXP-006` | No |
| **EXP-006 §3.2** *"No named table or checklist … left undispositioned"* | p. 301, entry by entry | **No** | **False** — Findings 1, 2, 8 | `EXP-006` | **YES** |
| **EXP-006 §3.3** *"every entry … its target opened"* | ~20 pages | **Not evidenced** — §9.1 lists 17 pages, none of them those | Coverage record not auditable | `EXP-006` | **YES** — Finding 4 |
| **EXP-006 §9.2 p. 92 attestation** | p. 92 | **Now yes** — opened mid-review, E-11a added and verified exact | **Cured** | `EXP-006` | **No** — Finding 3, closed |
| **EXP-006 §2** *"no OCR-only findings"* | six `OPENED` pages with no image (72, 121, 142, 229, 261, 262) + ~17 §3.3 targets | **Not evidenced** | Blanket claim overstates the record | `EXP-006` | **YES** — Finding 3 residual |
| **EXP-006 §5.3 E-13** `NECESSARY CONSEQUENCE` | p. 91 col. 2; **now also p. 92 E-11a** | **Read but unrecorded / now in tension** | Classification overstated; competing reading untested; E-11a's surprise gate is unreconciled with step 1 | `EXP-006` | **YES** — Finding 5 (downgrade to `QUALIFIED`, or re-derive against E-11a) |
| **EXP-006 §3.3 `Doors`/`Listening` → "unowned (§8 open item)"** | `INVENTORY.md`; packet §8 | **Yes** | Owner is `EXP-005`; the `§8` item does not exist | `EXP-006` | No — record defect, Finding 7 |
| **ENC-005 Q1** — underworld-only or RC's general procedure? | pp. 91, 98–100 | **Yes** | Source is unambiguous (one procedure, naval split out); the card's narrowing is a project decision | human owner | **No** as to source — `RETAINED`; it is a Stage-B gate |
| **ENC-005 Q2** — specify before five unresearched providers? | §7; `INVENTORY.md`; `BOUNDARY-CORRECTION` §4 | **Yes** | Evidence verified and correct | human owner | No — `CONFIRMED OUT OF SCOPE` |
| **ENC-005 Q3** — *"difficult terrain"* criterion | pp. 99–100, 88, index | **Yes** | Confirmed: examples only | `ENC-005` | No |
| **ENC-005 Q4** — chase rounds vs the 30-round running limit | pp. 98–100, 88, 103 | **Partly — p. 88 exhaustion section and p. 83 `Endurance` unrecorded** | Case-3 attestation not yet supportable | `ENC-005` / `CHAR-005` / `EXP-004` | **YES** — Finding 14 |
| **ENC-005 Q5** — scouts `-10%` vs `-15%` | p. 99, both magnified | **Yes** | **Genuine printed conflict, fully mapped.** §10.2.2 case 3. Correctly unadjudicated | Stage B / human | **No** |
| **ENC-005 Q6** — step-2 self-loop | p. 99, magnified | **Yes** | **Genuine printed defect, fully mapped.** Correctly unadjudicated | Stage B / human | **No** |
| **ENC-005 Q7** — where the `Retreat` bridge belongs | p. 104 image | **Yes** | Evidence now complete on both sides; routing decision correctly reserved | human owner | No |
| **ENC-005 Q8** — `Caving` and step 6 | **p. 83** | **No** | **Falsifies §5.5/N-22's negative.** Unfinished source inspection classified `BLOCKED` | `ENC-005` | **YES** — Findings 11, 12 |
| **ENC-005 Q9** — who owns "lost in a dungeon"? | p. 100; `INVENTORY.md` | **Premise depends on Q8** | Must be re-asked after p. 83 | human owner | **YES** (via Q8) |
| **ENC-005 §3.3** *"enumerated, not cited"* | pp. 302–304, entry by entry | **Mostly yes** | `Exhaustion . 88` missing; `Hide in shadows . 22` / `Woodland abilities . 27` / `Doors . 147` not enumerated (I judge the last three immaterial) | `ENC-005` | **YES** for `Exhaustion` — Finding 14 |
| **ENC-005 §5.2** *"verbatim … re-verified here"* | p. 99, magnified | **Yes** | One clause dropped at 5b | `ENC-005` | No — Finding 15, correct and republish |
| **ENC-005 §9.1** p. 92 as a page image | p. 92; scratchpad artifacts | **Now yes** — N-4a/b/c added and verified exact | **Cured** | `ENC-005` | **No** — Finding 13, closed |

**There are no silent unresolved research tasks left after this table.** Every row above is
dispositioned.

---

## 8. Did pass 2 remediate each numbered finding of the prior review?

| Prior finding | Sev | Remediated? | Evidence |
|---|---|---|---|
| **E-1** Ch. 13 `Blindness` (p. 150) never inspected | HIGH | **YES** | §5.1 opens the complete entry, quotes it verbatim and correctly, and **withdraws** the Q2 absence claim in terms. I verified the block against the page |
| **E-2** `Encounter Distances Table` (p. 93) not dispositioned | HIGH | **YES** | §5.2 transcribes all 13 rows and 3 footnotes exactly, withdraws the *"LIGHT-BEARING TABLES … NONE"* claim, and records the `ENC-001` seam |
| **E-3** `Starvation Table . 150` never opened | HIGH | **YES, with one gap** | §5.4 opens it, transcribes it exactly, verifies the printed `× 3/4`, and correctly defers to `SR-10` rather than claiming a new defect. **The Waterskin the reviewer named was not added** — Finding 6 |
| **E-4** `Timetrack Table . 149` never opened | MED | **YES** | §5.5; disposition ("tally sheet, not a procedure, no second time authority") is supportable on the page. Minor internal tension at Finding 9 |
| **E-5** Guardrail-B violation in the headline | HIGH | **YES, but a new one is introduced** | The *"four item descriptions … and nothing else"* headline is gone. §3.2's *"No named table or checklist … left undispositioned"* is a new unqualified source-property claim, and it is false — Findings 1, 2, 8 |
| **E-6** *"darkness" 37 hits dismissed wholesale; `Blind Shooting` says RC has "normal darkness penalties"* | MED | **NO — not remediated** | `Blind Shooting` appears nowhere in pass 2. Ch. 5 is never inspected or dispositioned. This is the root of Finding 2 |
| **E-7** Ch. 14 p. 154 class-I duplicate not recorded | LOW | **YES** | §5.1 E-6, now visually verified, with the cross-reference followed and recorded as raising E-1 to `PRIMARY TEXT + CROSS-REFERENCE CONFIRMED` |
| **E-8** false access claim at §7.1 | LOW | **YES** | §2.1 states plainly *"That statement was false when written."* Commendable. Pass 2 initially repeated the pattern at p. 92 and then **cured it mid-review** by opening the page and adding E-11a — see Finding 3. The residual is §2's blanket page-image claim over six `OPENED` pages with no image |
| **E-9** no evidence map, no §6 vocabulary | MED | **YES** | §5 is an evidence map with a Confidence column; the §6 terms are used **verbatim** throughout (`DIRECT PRIMARY TEXT`, `PRIMARY TEXT + CROSS-REFERENCE CONFIRMED`, `NECESSARY CONSEQUENCE`). No invented substitute labels found. No row carries `SECONDARY SOURCE LOCATOR ONLY` or `NOT YET VERIFIED` |
| **E-10** no §10.2 classification | MED | **YES** | §8 uses all four §10.2 dispositions verbatim; §8.1 is a genuine §10.2.1 reconciliation table over pass 1's own open statements |
| **E-11** item transcriptions accurate | — | carried forward, **re-verified correct by me** | §5.7 |
| **N-1** p. 100 col. 1 excluded while quoted | HIGH | **YES** | §5.5 reclassifies the page column by column and adds N-19–N-22, all verified |
| **N-2** two entry conditions unfollowed | MED | **YES** | §5.1 N-1/N-2/N-3, all verbatim exact |
| **N-3** `d100` direction absent | MED | **YES** | N-10, exact, and correctly flagged as mechanically essential |
| **N-4** no `Primary-Source Coverage Checklist` | MED | **YES** | §9 exists with sub-sections for units inspected, complete-entry inspection, exclusions-with-reasons and unresolved items |
| **N-5** no evidence map / §6 vocabulary / §10.2 classification | MED | **YES** | §5, §8, §8.1 — all present, all verbatim |
| **N-6** p. 104 `Retreat` quote stops a paragraph short | MED | **YES** | §5.6, from the page image; **both** maneuvers carry the bridge, exactly as the prior reviewer predicted from OCR. I confirmed it visually |
| **C-1 / C-2** common vocabulary defects | MED | **YES, both packets** | |
| **C-3** `EVIDENCE READY` header standing over a self-contradicting addendum | MED | **YES** | Both packets replace the header `STATUS` line with `RECOMMENDATION see section 19`, and both pass-1 files now carry an honest `SUPERSEDED — PRIMARY-SOURCE COMPLETENESS: FAIL` forward pointer with the failure described rather than softened. This is well done |
| **C-4** no scope creep | — | **Still true.** I re-checked independently | |
| **Remediation item 15** — revert to `PREPARED FOR INDEPENDENT COMPLETENESS REVIEW` | — | **Partly** | Both §19s say `EVIDENCE READY FOR HUMAN REVIEW` *"subject to the mandatory §10.1.2 independent completeness review … recorded in `CLUSTER-004-stage-a-completeness-review-2.md`."* §11 item 19 permits only two strings, and neither packet uses any of §10.1.2's **prohibited** outputs (`SOURCE COMPLETENESS PASSED` / `CERTIFIED` / `HUMAN EVIDENCE GATE CLEARED`). **I do not treat this as a failure ground** — the subject-to clause resolves the tension honestly. `ENC-005`'s §17 problem (Finding 12) is separate and is a failure ground |

**Score: 15 of 16 prior findings remediated for `ENC-005` and `EXP-006` combined; E-6 is the one
that was not, and it is the seed of this pass's largest finding.**

---

## 9. Pages I read as images, and what I did not read

**(a) Read as page images by me, in full — every "verified" statement above rests on one of
these. None of it rests on OCR.**

```text
p.  69, 70        Adventuring Gear Table + all descriptions (lantern, mirror, oil,
                  rations, tinderbox, torch, waterskin); Land Transportation Gear Table
p.  83            Ch. 5 Other Character Abilities -- Blind Shooting, Caving, Endurance,
                  Fire-Building, Food Tasting                       <- Finding 2, 11
p.  84            Ch. 5 continuation (Healing, Hunting)
p.  91            Exploration and the Game Turn; Game Turn Checklist; Wandering Monsters;
                  Game Day Checklist; Encounters intro
p.  92            CHANCE OF ENCOUNTER TABLE; Encounter Distance section; the surprise
                  1d6 rule and its three outcomes        <- Findings 3, 5, 13
p.  93            Encounter Checklist; ENCOUNTER DISTANCES TABLE; Monster Reactions
p.  98            Evasion and Pursuit; Definitions; Contact; Decision to Evade
p.  99            EVASION CHECKLIST; EVASION TABLE; all prose; Castle Reactions Table
p. 100            Dropped goods; Regain Bearings; Evasion at Sea; Ship Evasion Table;
                  Balancing Encounters
p. 104            COMBAT MANEUVERS TABLE; Fighting Withdrawal; Retreat; Lance; Set Spear
p. 108            ATTACK ROLL MODIFIERS TABLE; Target Cover Table; Missile Adjustments
                                                                    <- Finding 1
p. 149            Timekeeping; TIMETRACK TABLE; Character Records; Adventure Record Sheets
p. 150            Special Character Conditions -> Blindness, Deafness, Invisibility,
                  Paralysis, Prone, Sleep/Unconsciousness, Starvation & Dehydration,
                  Stunning; STARVATION TABLE
p. 154            Ch. 14 Special Attacks -> Blindness, Charge
p. 301            INDEX TO TABLES AND CHECKLISTS -- all three columns, entry by entry,
                  plus the Checklists list
pp. 302, 303, 304 GENERAL INDEX -- all three pages, complete
```

Magnified crops taken: p. 99 checklist steps 1–4 and steps 5a–6 (to settle Findings 15 and the
self-loop); p. 154 `Blindness`.

**(b) Consulted as OCR only, deliberately, as a locator:** the p. 82 `Sample Skills Table` skill
list; RC p. 22 `Hide in Shadows`; RC p. 27 `Woodland Abilities`; RC p. 74 `Miscellaneous Siege
Equipment Table`; RC p. 88 running/exhaustion prose; RC p. 85 `Survival (choose terrain)`. Every
finding that depends on any of these is stated as a locator result and is **either** corroborated
by a page image (p. 83 for the skills; p. 108 for the exhaustion modifiers) **or** marked LOW and
non-load-bearing (pp. 22, 27, 74, 85).

**(c) Not opened by me, and no claim made about them:** pp. 24–25 (`Infravision` → `CHAR-009`),
pp. 94–97, pp. 101–103, pp. 121, 125, 142, 146–148, 152, 229, 256–262. Counting a page I did not
open as inspected would be the same error this review exists to catch.

**I opened no non-RC source.**

---

## 10. Required remediation

### `EXP-006` — bounded, but it is new primary research, not editing

1. **Open RC p. 108 and disposition the `Attack Roll Modifiers Table`** as a §9.1 class-C named
   object and class-I duplicate presentation. Record `Attacker can't see target −4 penalty` as
   its own evidence row beside E-2's `−6`, and classify the relationship under §10.2 — including,
   if the governing objects for the relationship are not all inspected, `BLOCKED` per §10.2.2
   case 1. **Do not resolve which number governs**; that is Stage B, and §17's
   `STOP — INTERNAL SOURCE CONFLICT REQUIRES REVIEW` applies if the packet would choose.
2. **Open Chapter 5 (pp. 81–86) and disposition it**, at minimum `Sample Skills Table` (p. 82),
   `Fire-Building`, `Blind Shooting`, `Food Tasting` and `Endurance`. Withdraw §8 Q5's
   `PRIMARY PROCEDURE NOT YET ESTABLISHED`, qualify E-30, and route ownership to `CHAR-012`
   explicitly rather than by silence.
3. **Qualify §2's** *"every page … read as a page image / no OCR-only findings"* to match the six
   §3.2 rows marked `OPENED` without an image (pp. 72, 121, 142, 229, 261, 262). *(The p. 92 half
   of this is already discharged — see Finding 3.)*
4. **Reconcile §9.1 with §3.3** so the coverage checklist is the record §9.3 requires.
5. **Downgrade E-13 to `QUALIFIED`, or re-derive it** — record p. 91 col. 2's unconditional
   `2d6 x 10'`, and reconcile it with the newly added E-11a, under which the light-keyed table is
   consulted only when neither party is surprised.
6. **Add the p. 69/70 `Waterskin`** as the dehydration-side consumable.
7. **Correct §3.2's closure sentence** to a research-operation claim naming what was inspected,
   and fix §3.3's p. 147 routing (`EXP-005`) and its dangling `§8` reference.

### `ENC-005` — genuinely short

8. **Open RC p. 83 `Caving`**, record it, and restate §5.5/N-22 and §6.3's dungeon-getting-lost
   negative on the corrected premise. Reclassify Q8 — either `RESOLVED BY SOURCE INSPECTION` with
   `CHAR-012` named as a step-6 provider in §7.1, or `CONFIRMED OUT OF SCOPE` with explicit
   ownership. **A `BLOCKED` row and `EVIDENCE READY FOR HUMAN REVIEW` cannot coexist** (§17).
9. **Enumerate `Exhaustion . 88`** and add evidence rows for RC p. 88's 30-round running maximum,
   the `Endurance` exception RC itself names, the rest requirement, and *"drops to encounter
   speed"* — then re-attest Q4 under §10.2.2 case 3 or reclassify it.
10. **Restore `Combat occurs;`** to step 5b's verbatim block.
11. **Add evidence rows** for the catch-up determination, the obstacle branch, the open-ended DM
    adjustment, the area-familiarity factor, and step 2's *"moving off at another direction at
    running speed for one round"*; restore N-19's *"if he or she feels that the item dropped is
    indeed appealing to the monster."*
12. *(Discharged mid-review — p. 92 opened, N-4a/b/c added and verified. No action.)*

### Both

13. Re-run the §10.1.1 adversarial self-review **from source structure**, and specifically from
    the **p. 301 Tables Index read entry by entry** — that single operation surfaces Findings 1
    and 2 and is what the structure-first ordering in §9.1.1 is for.
14. Re-submit for §10.1.2 independent review. Per §10.1.2 the original researcher may not restore
    a ready status on its own certification.

---

## 11. Reviewer's note

I set out to find omissions, and I have said where I looked for each one. The honest summary is
that pass 2 fixed almost everything it was asked to fix, fixed it properly rather than
cosmetically, and was candid about its own prior errors — §2.1's *"That statement was false when
written"* and §5.4's *"An earlier draft of this packet called E-18 a new third printed defect;
that was wrong, and the error is recorded rather than quietly removed"* are exactly the right
instincts, and both packets refuse, repeatedly and correctly, to decide things that are not
theirs to decide.

What it did not fix is the habit underneath the original failure. Pass 1 was failed because the
indices were used to cite rather than to enumerate. Pass 2 says, correctly, that it will
enumerate them — and then enumerates the entries whose titles sound like the card. `Blindness`,
`Starvation`, `Timekeeping` and `Encounter Distances` were caught this time because the prior
review named them. `Attack Roll Modifiers Table` and `Sample Skills Table` were not named by
anyone, so they stayed outside, even though the first prints a modifier for not being able to
see and the second is where RC put the rule for lighting a fire in the wet and the rule for
getting lost while fleeing.

Both are one page away. Neither requires new judgement, only opening. That is why I expect the
next pass to be short, and why I do not think either card is in trouble on the merits.

```text
INDEPENDENT COMPLETENESS REVIEW (PASS 2): COMPLETE

EXP-006   PRIMARY-SOURCE COMPLETENESS: FAIL
ENC-005   PRIMARY-SOURCE COMPLETENESS: FAIL

NEITHER PACKET IS READY FOR HUMAN EVIDENCE REVIEW.
No mechanic was proposed, resolved or adjudicated in this review.
No file other than this one was modified.
```
