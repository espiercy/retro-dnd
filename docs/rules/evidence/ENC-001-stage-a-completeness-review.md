# `ENC-001` — Stage-A Independent Completeness Review #1

> **Immutable evidence.** This artifact records Independent Review #1 of
> `docs/rules/evidence/ENC-001-evidence.md` at commit
> `d24aa3ab4ac3bc7f2d9470c7a147e81bc4b4224b`. It is preserved unaltered. Later
> remediation is recorded in the packet and in the remediation commit, **never** by
> editing this review.

```text
REVIEW:        ENC-001 Stage-A Independent Completeness Review #1
PACKET:        docs/rules/evidence/ENC-001-evidence.md
PACKET COMMIT: d24aa3ab4ac3bc7f2d9470c7a147e81bc4b4224b
BRANCH:        enc-001-stage-a-evidence
REVIEWER:      independent agent; distinct role from the researcher (§10.1.2)
DATE:          2026-10-03
VERDICT:       FAIL
BLOCKING:      2
NON-BLOCKING:  7
DEC-0012 PILOT QUESTION:
    "Did review #1 discover any previously uninspected governing object?"
    ANSWER: YES -- RC p. 98 `Contact`
```

---

## 1. Verdict

**FAIL.** Two blocking findings, both enumeration/provenance defects of the class
`DEC-0012` was written to eliminate. One is the materialisation of a risk the packet
itself declared in advance.

## 2. Blocking findings

### B-1 — RC p. 98 `Contact` was never enumerated, never inspected, and is mis-dispositioned

RC p. 98, in `Evasion and Pursuit` → `Definitions` → `Contact`, prints:

> "Contact occurs when the two parties encounter one another, as per the earlier
> encounter rules. They do not have to be near one another, only within visual range.
> When the encounter occurs, the DM determines the encounter distance and the parties'
> relative states of surprise."

Coverage Manifest row 28 dispositioned pp. 96–98 as "Wilderness Encounter subtables 1–11
(incl. Castle, City)", **not visually inspected**. Row 29 routed evasion material to
`ENC-005` but scoped it to **pp. 99–100**. The `Contact` definition therefore fell in the
gap between the two rows, under a disposition that misdescribes p. 98's actual content.
The reviewer inspected leaf 97: p. 98 carries Subtable 10 (Castle) and Subtable 11 (City)
**and** the opening of `Evasion and Pursuit`, the `Definitions` lead-in, `Contact`, and
the start of `Decision to Evade`.

Why it blocks:

1. It is RC text naming encounter-distance determination in terms, and stating a contact
   condition ("within visual range") the packet treats as governing when it draws E-18
   from p. 91.
2. It bears on **E-12** (ordering) and on **Q-9**, which the packet marked
   `RESOLVED BY SOURCE INSPECTION`. p. 98 states both determinations at one moment and
   names distance first. Q-9 cannot be sound as resolved while this text is unexamined.
3. §13's fourth `FALSIFICATION-RECORD` recorded `SOUGHT: p. 92's ordering sentence;
   p. 93 Encounter Checklist step 2; INVENTORY.md rows 116 and 117`. The candidate
   falsifying text was at p. 98 and was not sought.

Aggravating circumstance found by the reviewer: the packet's R-9 cites
`docs/rules/evidence/ENC-005-evidence-remediated.md` **line 147**. Line **146** — the row
immediately above — is `ENC-005`'s accepted finding **N-4**, which quotes the p. 98
`Contact` text verbatim, labels it p. 98, bolds "encounter distance", and classifies it
`PRIMARY TEXT + CROSS-REFERENCE CONFIRMED`. An already-accepted project artifact records
p. 98 as encounter-distance-bearing primary text; the researcher was inside that file
during the repository-fact pass, one line away.

### B-2 — the City sentence is attributed to p. 91; it is printed on p. 93

The sentence *"'City' is treated just like any other wilderness terrain"* is printed on
**p. 93**, right column, in the `Wandering Monster Encounters` section. The packet cites
p. 91 in four places: E-19, §6 governing-objects row 7, the §8 cross-reference ledger, and
Coverage Manifest row 14.

The reviewer read leaf 90 (p. 91) in full at 1400px and re-cropped column 3 at 1600px. The
`Encounters` section on p. 91 contains "traveling through a heavily populated zone (such
as a town)" and nothing about City terrain.

Why it blocks: §4 has **no row** for the p. 93 `Wandering Monster Encounters` prose. That
object supplies both the City→wilderness rule and the dungeon-vs-wilderness
setting-selection sentence feeding the table's `Setting` axis. A governing fact is drawn
from an unenumerated object and attributed to a different object on a different page.
Q-10 is marked `RESOLVED BY SOURCE INSPECTION` on a citation that does not hold.

The reviewer notes fairly: the **fact** is true and the page is on `IMAGE-VERIFIED`. This
is a provenance and enumeration defect, not a rules error.

## 3. Non-blocking findings

1. **§3 Source Structure enumerates only 9 structural units.** Ch. 1, Ch. 3, Ch. 9–12,
   Ch. 15–19 and Appendices 1–3 appear nowhere, not even as `EXCLUDED — <reason>` rows.
2. **Aerial encounters are an unrecorded open question.** The Chance of Encounter Table
   (p. 92) prints `aerial**` as a wilderness terrain, but the Encounter Distances Table
   has no Aerial `Setting` row and RC supplies no City-style bridging statement.
   Reviewer inspected pp. 114–115: no encounter distance there either.
3. **§5.2's General Index ledger is materially incomplete** relative to §15's claim of
   39 entries. Missing: `Detection … 24, 25`, `Torch … 62, 66, 69, 70`,
   `Range, weapon … 108`, `Travel … 89, 91`, `Speed … 88`, `Setting … 256, 259`,
   `Environment … 119`, `Swoop … 115, 154`, `Combat — Aerial … 114, 115`. Reviewer
   followed each; none reaches an uninspected distance mechanic.
4. **§5.1 omits two entries it relies on elsewhere**: `Attack Roll Modifiers Table … 108`
   and `Challenge Percentage Table … 101`.
5. **The p. 92 surprise sidebar** is a distinct boxed object on an inspected page with no
   manifest row. Its substance is correctly routed in §12; only the enumeration is missing.
6. **Two verbatim transcriptions are silently truncated.** The p. 91 Game Turn Checklist
   step 1 quotation omits "Leave the Game Turn Checklist sequence and go to the Encounter
   Checklist, below…"; the p. 24 Infravision quotation omits the 10′ recognition clause,
   which is relevant to Q-4 and Q-5.
7. **Negative claim N-4's scope understates.** `SCOPE SEARCHED` excludes Ch. 4 Equipment
   and Ch. 3 Spells. The reviewer believes the claim is **true**; the record's
   auditability is what falls short.

## 4. Informational observations

- The packet's transcription faithfully reproduces scan artifacts: `lightt` is the dagger
  footnote marker set tight against "light", and `2d6 X 10 yards` genuinely uses a capital
  X in that one Ocean/sea row. Faithful for evidence; a Rule Card must not inherit them as data.
- **R-9 is genuinely good work.** `ENC-005`'s inherited "light-keyed" note is wrong, the
  packet caught it against primary text, and p. 92's "the type of terrain" is the right
  refutation. Reviewer confirmed both independently.
- `DEC-0012` pilot criterion 1 is **satisfied**: the linter runs and reports
  `ENC-001-evidence.md … PASS`, with 1 reference packet, 1 Stage-A packet, 12
  grandfathered. The gate is no longer inert.

## 5. Independent transcription of the Encounter Distances Table

Transcribed from leaf 92 full page, then re-verified from a `pct:34,8,64,26` crop at
2000px, before comparing against the packet.

```text
Encounter Distances Table
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

**Match: EXACT.** All 13 data rows, 4 column headers, 3 footnotes, every dice expression,
every unit, and the capital-X artifact. **No discrepancy.** E-1 through E-8 all accurate.

The reviewer also independently confirmed, word for word, the p. 92 `Encounter Distance`
section, the p. 91 `Wandering Monsters` prose, the p. 87 `Feet vs. Yards` paragraph, and
the p. 24 `Infravision` first three sentences. All exact.

## 6. Independent index-absence verification

Method: read the alphabetical neighbourhood on the page image, not a text search.

| Term | Neighbourhood read | Result |
|---|---|---|
| Encounter distance | p. 302: `Encounter speed` → `Encounters` | **ABSENT — packet correct** |
| Visibility | p. 304: `Variant rules` → `Visitors` → `Vortex` | **ABSENT — packet correct** |
| Light | p. 303: `Lifeboat` → `Lightship` → `Listening` | **ABSENT — packet correct** |
| Lantern | p. 303: `Land transportation` → `Land travel` → `Languages` | **ABSENT — packet correct** |
| Darkness | p. 302: `Dagger` → `Damage bonuses` → `Days` | **ABSENT — packet correct** |
| Ocean | p. 303: `Off-hand penalty` → `Officials` → `Oil` → `Omnivore` | **ABSENT — packet correct** |
| Sea | p. 303: `Scrolls` → `Secret door` → `Servitor` | **ABSENT — packet correct** |
| Undersea | p. 304: `Undead` → `Underwater combat` | **ABSENT — packet correct** |

**All eight absence claims are TRUE.** Present-entry locators also confirmed:
`Distance … 87`, `Encounters … 91-96`, `Surprise … 92, 93`, `Infravision … 24, 25`,
`Evasion … 91, 98-100`, `Pursuit … 98-100`, `Terrain … 119, 153`, `Yards … 87`,
`Feet … 87`, `Ranges … 87`, `Skills … 82-85, 92`, `Wandering monsters check … 91`,
`Nocturnal … 153`.

## 7. Finding on pp. 94, 96–98

- **p. 94** — Dungeon Encounters Tables. Monster-selection only. **No distance mechanic. Routing correct.**
- **p. 96** — Subtables 1–2, Special City Encounters, Wandering Monsters and High-Level PCs. **No distance mechanic. Routing correct.**
- **p. 97** — Subtables 3–9. **No distance mechanic. Routing correct.**
- **p. 98** — Subtables 10–11 **and** `Evasion and Pursuit`, `Definitions`, `Contact`,
  `Decision to Evade`. **Contains encounter-distance-bearing text.** See B-1.

p. 99 additionally inspected: Castle Reactions Table, Evasion Checklist, Evasion Table,
pursuit prose. Consumes distance rather than setting it. **Routing correct.**

## 8. The DEC-0012 pilot question

`DEC-0012` Decision item 15, four success criteria, verbatim:

```text
1. the evidence linter runs on the real packet;
2. the packet reaches independent review with all structural gates satisfied;
3. independent review #1 finds NO previously uninspected governing object;
4. no more than TWO independent completeness reviews are required to reach PASS.
```

### "Did review #1 discover any previously uninspected governing object?" — **YES**

**The object:** RC p. 98, `Evasion and Pursuit` → `Definitions` → `Contact`.

- *Not correctly routed.* Row 29 scopes the `ENC-005` routing to pp. 99–100; p. 98 is
  outside it. The only row covering p. 98 is row 28, factually wrong about the page.
- *Not free of encounter-distance content.* It names encounter-distance determination
  explicitly and states the visual-range contact condition. The project's own accepted
  `ENC-005` packet classifies this exact text as encounter-distance-bearing primary text.
- *Previously uninspected.* §4 states it plainly; §7's `IMAGE-VERIFIED` omits 98.
- *Should have been enumerated.* `DEC-0012` item 1 requires enumeration before conclusions.

**Counter-argument, stated so the human can weigh it:** p. 98 states no new procedure and
produces no distance value; it says "as per the earlier encounter rules", pointing back to
pp. 92–93, which *were* inspected and transcribed correctly. A reader requiring a governing
object to *generate* a distance would score criterion 3 as passed on a technicality. The
reviewer does not think that reading survives, because the packet's E-12 and Q-9 make a
positive claim about ordering that this text addresses.

**Criterion 2** is met as the linter measures it, but §9.3.1's substantive
enumerate-before-concluding gate is not, for the p. 98 object and the p. 93 object (B-2).
**Criteria 1 and 4** stand: the linter ran on the real packet and passed; this is review
#1, so a review #2 remains inside budget.

The reviewer records explicitly: the packet is far stronger than the `CLUSTER-004` pass-1
packets that motivated `DEC-0012` — exact table transcription, eight true index absences,
every repository fact checked holding, a correctly refuted inherited error, and its own
weakest point declared in advance rather than concealed. The remediation visibly raised the
floor. It did not reach the ceiling item 15 set.

## 9. Repository facts spot-checked (7 of 12)

| Row | Result |
|---|---|
| R-1 | **CONFIRMED** — `INVENTORY.md` line 116 as stated |
| R-2 | **CONFIRMED** — line 117, `ENC-002` deps `CHAR-010`, `Unresearched` |
| R-3 | **CONFIRMED** — one hit, the packet itself |
| R-5 | **CONFIRMED** — `MundaneLightContribution` docstring as quoted |
| R-6 | **CONFIRMED** — 12 grandfathered entries, no `ENC-001`, list closed |
| R-7 | **CONFIRMED** — 16 unblocked cards, `ENC-001` among them |
| R-12 | **CONFIRMED** — one unrelated prose hit in `COMBAT-008`; no row claims visibility state |

All seven accurate. No `UNVERIFIED PROJECT FACT` found.

## 10. Reviewer's own coverage limits

Stated plainly, because this review is subject to the standard it applies.

**Pages not opened:** 25, 26, 27 (so negative claim **N-3** on halfling infravision is
**unverified by this reviewer**); 100, 101; 88, 89, 90 (the `EXCLUDED — per-day travel`
dispositions accepted on index entries alone); 108 (E-30 unverified); 150 (E-23
unverified); 215 (E-29 unverified); 102–113, 116; 305 (the index end boundary rests on the
packet's word plus observed A–Z continuity).

**Chapters not enumerated at all:** Ch. 1, Ch. 3 (Spells), Ch. 4 (Equipment, including the
`Torch` entries), Ch. 5, Ch. 9–12, Ch. 15–19, Appendices 1–3. The reviewer does **not**
assert these are empty. Negative claim **N-4** is, in the reviewer's judgement, *probably*
true but **not independently established** by this review.

**Index coverage:** all three index pages read as full-page images; eight absences verified
by neighbourhood; ~60 present entries confirmed. Neither index transcribed entry by entry,
so finding 3 is a lower bound.

**Digitisation:** only the `TSR1071TheDDRulesCyclopedia` item used; no cross-check against
the second digitisation.

**Repository:** 7 of 12 fact rows checked. R-4, R-8, R-10, R-11 not verified.
`RULE_CARD_RESEARCH_PROTOCOL.md` §9–§11 not re-read in the original this pass.

**Not assessed:** whether the packet's rules *interpretation* is right. Q-1 through Q-7
appear to be genuine source ambiguities correctly retained rather than silently resolved —
notably Q-1, where the `2d6 × 10'` coincidence is exactly the identification an agent
would be tempted to make and the packet pointedly did not. That is a judgement, not a
verification.
