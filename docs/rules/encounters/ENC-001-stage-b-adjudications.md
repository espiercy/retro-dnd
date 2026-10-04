# `ENC-001` — Encounter Distance — Stage-B Adjudications

> **Scope of this document.** It records Stage-B adjudications of questions left open and
> retained by the accepted `ENC-001` Stage-A evidence packet
> (`docs/rules/evidence/ENC-001-evidence.md`, Stage A `ACCEPTED` 2026-10-04 under
> `DEC-0013`). It is **not** the Rule Card, and it does not authorize implementation.
>
> **`Q-1`, `Q-3`, `Q-7`, `Q-9` and the feet/yards convention are adjudicated here.** `Q-7` is
> fully settled: its contract by human architecture decision, and its world/environment
> visibility owner **assigned to `SIM-003`**. Feet/yards is settled by finding that **no
> separate owner is required** — it is part of `ENC-001`'s typed output.
>
> **Known outstanding dependencies, enumerated rather than summarised as "one gap":**
> **`Q-4`** (whose infravision satisfies the p. 93 `**` footnote) is the one item **on
> `ENC-001`'s distance path that no component owns**; `SIM-003` additionally carries
> **daylight/time-of-day** and **weather** determination as unowned, scenario-supplied inputs.
> None of the three is adjudicated here. See the completion assessment at the end.
>
> **The accepted Stage-A packet is never modified by this document.** It records each question
> at its Stage-A disposition; Stage B adjudicates what `ENC-001` does about them without
> rewriting the evidence record.

```text
ADJUDICATION-STATUS
RULE-ID:   ENC-001
Q-1:       ADJUDICATED 2026-10-04; SR-12 APPROVED 2026-10-04
Q-3:       ADJUDICATED 2026-10-04; NO NEW SIMULATOR RULING
Q-7:       SETTLED 2026-10-04 by human architecture decision
           world/environment visibility OWNER ASSIGNED: SIM-003
Q-9:       ADJUDICATED 2026-10-04; NO NEW SIMULATOR RULING
           aerial is a Type of Terrain, not a Setting -- no row is missing
FEET/YARDS ADJUDICATED 2026-10-04; NO NEW SIMULATOR RULING, NO NEW OWNER
           part of ENC-001's typed output, not an ownership problem
Q-6:       resolved AS IT BEARS ON ENC-001 -- p. 115 is a different
           procedural domain (undersea missile ranges, not encounter distance)
STAGE B:   adjudication only; no Rule Card, no implementation
```

> **Historical note, 2026-10-04 — a label discrepancy that was stopped on.** An earlier
> task authorized adjudicating `Q-3` but described it as the *"normal dungeon conditions"
> vs `Dim light`* question, whose resolution would turn on caller-supplied world-visibility
> state. The accepted Stage-A packet's `Q-3` is a **different question** — the one
> adjudicated below. The question that task described is split across `Q-1` (already
> adjudicated, `SR-12`) and `Q-7` (not authorized). Adjudicating under the mismatched label
> would have decided `Q-7` while calling it `Q-3`, so the discrepancy was reported instead
> and nothing was decided. A subsequent task authorized `Q-3` **as the accepted packet
> actually words it**; that adjudication is below. `Q-7` was not adjudicated then and is
> not adjudicated now.
>
> **The Stage-A disposition is not rewritten.** The accepted packet still records `Q-3` as
> `RETAINED AS GENUINE SOURCE AMBIGUITY`, which is the correct *Stage-A* finding: Stage A
> established that RC does not equate the labels. Stage B adjudicates what `ENC-001` does
> about that; it does not revise the evidence record, and the accepted packet is unmodified.

---

## Q-1 — the two `2d6 × 10'` procedures

### 1. Question as the accepted packet states it

> Does "normal dungeon conditions" (p. 91) denote the table's Dim-light row? Both produce
> `2d6 × 10'`, and RC never equates them.

Restated for adjudication: **are the p. 91 wandering-monster distance and the
pp. 92–93 encounter-distance procedure one determination or two?**

### 2. Source basis — re-inspected this pass

| Page | Re-inspected | What it supplies |
|---|---|---|
| p. 91 | yes, page image | Game Turn Checklist step 1; `Wandering Monsters` prose; the `Encounters` definition |
| p. 92 | yes, page image | the `Encounter Distance` section; the sort-of-encounter sentence; the surprise sidebar |
| p. 93 | yes, page image | the Encounter Distances Table; the Encounter Checklist; `Wandering Monster Encounters` |

No new source area was opened, and no Stage-A governing object or ownership conclusion
changed. This is adjudication from the accepted evidence base.

**The sentence that decides it** is on p. 92, immediately above the `Encounter Distance`
heading and already within an inspected, governing page:

```text
p. 92
"When the DM chooses to have an encounter or when a die roll indicates an
encounter, the DM must first determine or randomly roll what sort of encounter
it is (an encounter with wandering monsters, an NPC or a group of NPCs, or a
trap). Once that's determined, he or she can run the encounter according to the
Encounter Checklist."
```

RC classifies **"an encounter with wandering monsters"** as one *sort of encounter*, and
sends every sort to the same Encounter Checklist. The `Encounter Distance` section follows
in the very next paragraph.

### 3. Competing interpretations

**Interpretation A — one determination, two presentations.** p. 91's `2d6 × 10'` is a
dungeon-case shorthand for the same "how far apart are they" determination that
pp. 92–93 set out in full.

**Interpretation B — two distinct procedures.** p. 91 establishes a separate default for
wandering-monster encounters under normal dungeon conditions; pp. 92–93 govern the
general case.

**Interpretation C — considered and rejected as unsupported.** That p. 91 is the
pre-computed value of the Dungeon/**Dim light** row specifically. This requires equating
"normal dungeon conditions" with "Dim light", which **RC nowhere states**; its only
support is the shared dice expression. Adopting it would reintroduce exactly the
simplification the accepted Stage-A research rejected when it refuted the inherited
`ENC-005` note calling the table "light-keyed". **Not adopted.**

### 4. Structural comparison

| | p. 91 `2d6 × 10'` | pp. 92–93 procedure |
|---|---|---|
| Position in RC's procedure | Game Turn Checklist step 1, at monster *arrival* | `Encounter Distance` section, entered once an encounter is determined |
| Trigger | a positive wandering-monster check | any encounter, of any sort |
| Visibility an input? | no | **yes** — a table axis |
| Setting an input? | only the qualifier "normal dungeon conditions" | **yes** — Dungeon / Wilderness / Ocean-sea / Undersea |
| Surprise already resolved? | **no** — surprise is Encounter Checklist step 2, reached *after* | **yes** — "has determined the relative conditions of surprise" |
| Describes initial awareness/contact distance? | yes — "the distance at which the monsters are detected", "both sides first have a chance to notice one another" | yes — "how far apart the two parties are when the encounter takes place" |
| Explicit redirect? | **yes, one-way:** "(see the 'Encounter Distance' section, below, for more information)" and "switch to the Encounter Checklist (on page 93)" | never refers back to p. 91 |
| Effect of applying both | **two distances for one encounter** — a double roll RC nowhere contemplates | — |

Four facts carry the weight:

1. **RC itself classifies wandering monsters as a *sort of encounter*** (p. 92) and routes
   every sort through the same Encounter Checklist. That is the opposite of a separate track.
2. **p. 91 defers to p. 92; p. 92 never defers back.** A one-way pointer from a short
   statement to a fuller one is the signature of a shorthand, not of a rival rule.
3. **The Encounter Checklist contains no distance step** — its six steps are Game Time,
   Surprise, Initiative, Reactions, Results, Encounter Ends (accepted Stage-A finding,
   re-confirmed on the p. 93 image). There is therefore no second point in the procedure at
   which a distance is produced; both routes converge on one determination.
4. **Applying both would double-roll.** RC gives no rule for choosing between two
   simultaneously applicable distances, which is strong evidence it does not intend two.

Interpretation B's best support is p. 91's distinctive wording — *detected*, and *"both
sides first have a chance to notice one another"*. That is real and is **not** dismissed:
it sits in genuine tension with p. 92's one-surprised branch, where notice is explicitly
asymmetric. But it is better read as describing *what an encounter distance is* than as
establishing a second mechanic, and the tension it creates is recorded below rather than
argued away.

### 5. Adjudication

**Interpretation A is better supported by the RC text.** The p. 91 `2d6 × 10'` statement
and the pp. 92–93 procedure are **one determination**, not two.

RC does not, however, *state* the precedence rule needed to make that deterministic when
both presentations are in view. Under `SOURCE_HIERARCHY.md` §7 and the adjudication order
in this task, that residue is closed by the smallest sufficient ruling:

```text
SIMULATOR RULING SR-12                                      APPROVED
Encounter distance is determined ONCE per encounter, by the pp. 92-93
procedure. Where RC's p. 91 wandering-monster statement and the pp. 92-93
procedure would both apply, the pp. 92-93 procedure GOVERNS and the p. 91
`2d6 x 10'` is NOT rolled as a second, separate distance.

A wandering-monster encounter is a SORT of encounter (RC p. 92), not a
separate distance track.

APPROVED BY:  human project owner
DATE:         2026-10-04
PROPOSED:     2026-10-04
```

> **This is a Simulator Ruling, not a Rules Cyclopedia reading**, and it is labelled as
> one. `SR-12` is the next free identifier (`SR-1`…`SR-11` are in use). It was proposed by
> an agent and **approved by the human project owner on 2026-10-04**; an agent may not
> approve a Simulator Ruling (`SOURCE_HIERARCHY.md` §9, `AGENTS.md` §12).
>
> **What `SR-12` does NOT decide**, stated so its scope cannot drift:
>
> - that "normal dungeon conditions" means `Dim light`, or any other visibility row;
> - which visibility category obtains at a given moment, or who owns that world state;
> - anything about surprise ownership, which remains `ENC-002`'s;
> - the p. 91 / p. 92 awareness-language tension (mutual notice vs asymmetric notice),
>   which §7 below records as residue.

**The smallest ruling that closes the gap.** It decides only *how many times distance is
determined and which presentation governs*. It does **not** decide which visibility row a
dungeon encounter selects, does not equate "normal dungeon conditions" with any visibility
category, and does not touch surprise.

### 6. Behaviour in the four required cases

| | Case | Result under `SR-12` |
|---|---|---|
| **A** | Wandering monster, ordinary dungeon conditions | One determination via pp. 92–93. Surprise first (`ENC-002`); if neither surprised, the Dungeon row selected by visibility. **`2d6 × 10'` is not rolled separately.** Which Dungeon row applies is **not decided here** — it needs the visibility category, which is `Q-3`/`Q-7` and the unowned world-visibility gap |
| **B** | Dungeon encounter in Dim light | Dungeon / Dim light → `2d6 × 10'`. Single roll |
| **C** | Dungeon encounter in darkness | Dungeon / No light → `1d4 × 10'`; or Dim light → `2d6 × 10'` if full darkness **with infravision used** (footnote `**`). Single roll |
| **D** | Non-dungeon setting | Wilderness / Ocean-sea / Undersea row, in **yards**. Single roll |

**No overlap and no double-rolling in any case.** Case A is the one that was previously at
risk, and the ruling removes the risk by removing the second roll — while leaving the
row-selection question openly unresolved rather than silently answering it.

### 7. Residual, recorded not resolved

- **Case A is not yet fully deterministic.** It cannot be, without the visibility-category
  dependency this task is forbidden to resolve. Per the adjudication order's third option,
  that residue is preserved as a dependency, not disguised: a deterministic Rule Card for
  case A awaits `Q-3`/`Q-7` and an owner for world visibility state.
- **The mutual-notice tension stands.** p. 91 calls its distance the one at which *both
  sides* first have a chance to notice one another; p. 92's one-surprised branch makes
  notice asymmetric. `SR-12` does not resolve this, and it is not the same question as
  `Q-1`. Recorded here for whoever drafts the Rule Card.

### 8. Ownership impact — **none**

| Boundary | Effect |
|---|---|
| `ENC-001` | Unchanged. Still owns encounter-distance determination, and the governing-object set is unchanged — the accepted packet's §5 table is byte-identical to the accepted blob, so no count is restated here (`DEC-0013`: counts are derived, not hand-maintained) |
| `ENC-002` | Unchanged. **Surprise remains `ENC-002`-owned.** `SR-12` makes `ENC-001` *consume* surprise state earlier in the sequence; it never derives it |
| `ENC-005` | Unchanged. `Contact` (p. 98) and `Evasion at Sea` (p. 100) stay `ENC-005`'s, and the initial-encounter-distance vs pursuit-starting-distance distinction is untouched |
| `EXP-006` | Unchanged. Still owns mundane light contribution and **not** world visibility |

No Stage-A governing object or ownership conclusion required changing, so this task's
`STOP` condition was not triggered.

### 9. Implementation consequence

For whoever is later authorized to draft the Rule Card — stated as consequence, not as a
specification:

- Encounter distance is produced **once**, by one procedure, with surprise state as an
  input supplied by the caller.
- No separate wandering-monster distance path exists; the wandering-monster check
  (`EXP-001`) decides *that* an encounter occurs, not *how far away*.
- The procedure cannot be made total until a visibility category is available, which is
  an **unowned** input today.

---

## Q-3 — `Very good light` vs `Clear daylight`

### 1. Question as the accepted packet states it

> Is the Dungeon row's "Very good light" the same condition as "Clear daylight"? RC prints
> two labels and never equates them.

Accepted Stage-A disposition: `RETAINED AS GENUINE SOURCE AMBIGUITY`, object `p. 93`.

This is a question about **two printed table labels**. It is *not* the question of which
visibility condition obtains in the world — that is `Q-7`, and it is out of scope here.

### 2. Source basis — re-inspected this pass

| Page | Re-inspected | Why |
|---|---|---|
| p. 93 | yes, authoritative page image, including a magnified crop of the table | carries both labels and the whole Encounter Distances Table |

**No other page was opened.** p. 93 points to p. 95, p. 102 and Chapter 14, but each is a
monster/combat reference rather than a definition of either visibility label, and pp. 94–97
are `ROUTED` to `EXP-008` in the accepted packet. The accepted Stage-A evidence identifies
no page defining either term. Stage-A research was not reopened.

### 3. Exact occurrences, labels preserved as printed

Transcribed from the page image, RC's capitalization and spacing kept:

```text
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

Every occurrence of the two labels:

| Label | Setting | Visibility label as printed | Encounter | Distance |
|---|---|---|---|---|
| `Very good light` | `Dungeon*` | `Very good light` | `DM's choice` | `4d6x 10'` |
| `Clear daylight` | `Wilderness` | `Clear daylight` | `DM's choice` | `4d6 x 10 yards` |
| `Clear daylight` | `Ocean/sea` | `Clear daylight` | `Ship` | `300 yards` |
| `Clear daylight` | `Ocean/sea` | `Clear daylight` | `Monster` | `4d6 x 10 yards` |

`Very good light` occurs **once**, on the only indoor setting. `Clear daylight` occurs
**three times**, all on outdoor settings. Neither label carries a footnote marker.

### 4. Structural comparison

| Property | `Very good light` | `Clear daylight` |
|---|---|---|
| Settings that use it | `Dungeon*` only | `Wilderness`, `Ocean/sea` |
| Do they ever co-occur in one setting? | **no — complementary distribution** | **no** |
| Row it selects | the setting's brightest tier | the setting's brightest tier |
| Distance expression | `4d6x 10'` | `4d6 x 10 yards`, **and** a flat `300 yards` on `Ocean/sea`/`Ship` |
| Footnote attached | none | none |
| Footnote mapping one to the other | **none exists** | **none exists** |
| Defined elsewhere in RC | not in the chapters the accepted packet searched | not in the chapters the accepted packet searched |

Four structural facts carry the weight, and all four are visible on the page image:

1. **Complementary distribution.** No setting offers both labels. They never compete for
   the same lookup, so the table never asks the reader to tell them apart.
2. **RC reuses labels verbatim when it means the same tier.** `Dim light**` and `No lightt`
   are printed *identically* across `Dungeon*`, `Wilderness` and `Ocean/sea`. RC was
   plainly willing to repeat a visibility label across settings — so the divergence at the
   top tier is a deliberate wording choice, not typographic drift. It is also adequately
   explained by the fact that *daylight is not available indoors*, which is a constraint on
   wording, not a claim about a different brightness.
3. **The Visibility column is not a uniform cross-setting enum.** `Undersea` collapses the
   entire axis to `Any light`. RC therefore does not maintain one global visibility
   vocabulary that the settings each draw from; the column is **setting-local**.
4. **The label does not carry the formula.** `Clear daylight` yields `4d6 x 10 yards` on
   `Wilderness` and `Ocean/sea`/`Monster`, but a flat `300 yards` on `Ocean/sea`/`Ship`.
   Distance is a function of `(Setting, Visibility, Encounter)`, never of the visibility
   label alone — so "same label, same distance" is not even true *within* `Clear daylight`,
   and identical dice across two labels proves correspondingly less.

### 5. The three questions, answered separately

```text
1. Are the WORDS identical?              NO -- they share no word at all
2. Does RC explicitly EQUATE the labels?  NO -- see the scope limit below
3. Must the simulator treat them as the
   same INPUT STATE for ENC-001?          NO -- and it must not, see section 7
```

**Scope limit on question 2, stated narrowly.** No equating passage appears on p. 93, and
none was found in the chapters the accepted Stage-A packet searched. That is the claim the
inspected material supports. It is **not** a claim that no such passage exists anywhere in
RC; the accepted packet's `Q-7` was already narrowed to the chapters searched for exactly
this reason, and the same limit is kept here rather than quietly widened.

### 6. Competing interpretations

**Interpretation A — equivalent visibility conditions.** The two labels name one effective
visibility state, worded per setting, and a simulator may normalize both to one internal
category. *Support:* identical structural position, identical `4d6 × 10` dice in the
`Dungeon`/`Wilderness` pair, no distinguishing footnote. *Against:* RC never says it, and
fact 3 above shows RC does not operate a single cross-setting visibility vocabulary at all
— so a shared underlying category cannot be inferred from parallel position. **Not adopted:
it asserts more than the source establishes.**

**Interpretation B — distinct RC conditions.** The differing labels are semantically
non-equivalent, and the simulator must keep separate categories unless some rule maps them.
*Support:* RC prints different words, reuses labels verbatim elsewhere, and never equates
these two. *Against:* that is evidence the wording choice was deliberate, not evidence the
*conditions* differ — the choice is fully explained by daylight's unavailability indoors.
**Not adopted as stated:** it reads "never equated" as "proven different", which the source
does not support either.

**Interpretation C — operationally equivalent in the table, textually and semantically
unequated by RC.** Each label occupies the brightest tier of its own setting; because of
complementary distribution they never compete, so the table is fully determinate without
RC ever having to equate them. RC leaves the semantic relationship **unmapped**, and the
table does not need it mapped. *Support:* all four structural facts in section 4, each read
off the page image. **Adopted.** It is the reading the table itself establishes, and it
claims nothing beyond it — it asserts neither identity (A) nor difference (B).

Interpretation C is retained because the source supports it, not to avoid choosing: it
makes a positive, checkable claim (the lookup is total per setting without an equivalence)
and it is falsifiable — a single setting offering both labels would refute it.

### 7. Adjudication

**RC does not equate `Very good light` and `Clear daylight`, and `ENC-001` does not equate
them either.** They are preserved as distinct RC-native visibility labels, each belonging
to its own setting.

This is adjudicated under step 4 of the adjudication order — *preserve separate states if
determinism does not require equivalence* — and step 3 is **not** reached:

```text
1. RC Explicit .................. the table's structure, read off the page image
2. Necessary Consequence ........ lookup is total per setting without an equivalence
3. Narrow Simulator Ruling ...... NOT REACHED
4. Preserve separate states ..... ADOPTED
```

**Why determinism does not require an answer.** The lookup key is
`(Setting, Visibility, Encounter)`. Once a setting is fixed, the visibility labels available
in that setting are fixed, and the brightest tier is named by exactly one label. At no point
does the procedure have to ask whether `Very good light` and `Clear daylight` denote the
same world condition — the question cannot arise inside a lookup, because no setting offers
both. Row selection is total and unambiguous without the equivalence.

```text
NO NEW SIMULATOR RULING

Q-3 is resolved by preserving what RC prints. Creating an equivalence (or a
non-equivalence) would decide something the table never asks and the source
never states. The next free identifier remains SR-13; it is not used here.
```

### 8. Behaviour in the four required cases

| | Case | Result |
|---|---|---|
| **A** | Dungeon with very strong illumination | Requires `Very good light` **specifically**. There is no `Dungeon*`/`Clear daylight` row, so `Clear daylight` is not a usable input in a dungeon |
| **B** | Wilderness in clear daytime | Requires `Clear daylight` **specifically**. There is no `Wilderness`/`Very good light` row |
| **C** | Caller supplies one generic "excellent visibility" state | **`ENC-001` cannot accept it.** Mapping one generic state onto both labels would assert that a single world condition satisfies the brightest tier in every setting — which is the equivalence `Q-3` asks about. Doing it inside `ENC-001` would **silently adjudicate** `Q-3` in the affirmative, so `ENC-001` requires the RC-native label instead |
| **D** | Future world-state provider preserves RC-native labels | **Negligible added complexity.** `Setting` is already a required input to the lookup, so a provider that must emit a visibility label already knows the setting; emitting that setting's own label adds no new dimension. Preservation is close to free, which is why it is preferred over an invented equivalence |

Case C is the load-bearing one. It is also the reason the adjudication has a contract
consequence at all: the cheapest-looking implementation choice — one tidy brightness enum —
is precisely the one that would decide `Q-3` without saying so.

### 9. Provenance classification

| Conclusion | Classification |
|---|---|
| The table's structure: complementary distribution, shared lower-tier labels, `Undersea`/`Any light`, footnote attachment, `Ocean/sea`/`Ship` flat `300 yards` | **Rules Cyclopedia Explicit** — read directly off the authoritative p. 93 image |
| Row selection is total per setting without equating the two labels | **Necessary Consequence** of that structure |
| No equating passage on p. 93 or in the chapters the accepted packet searched | **Rules Cyclopedia Explicit**, scope-limited — a narrowed negative finding, not an RC-wide claim |
| `ENC-001` consumes RC-native labels and does not normalize them | **Repository Boundary / Architecture** — a contract decision about where the ambiguity is owned, not a rules claim |
| Any equivalence or non-equivalence of the two labels | **none issued** — no Simulator Ruling |

**"Not equated" is not "proven distinct."** RC leaves the relationship between the two
labels **unmapped**, and this adjudication preserves that unmapped state. It does **not**
assert that a brightly lit dungeon and a clear day are different conditions in the fiction.
Whether one world condition satisfies both labels is left undecided, and is left decidable
later by whoever owns world visibility.

### 10. `Q-7` impact — **unchanged**

| | Question | Status |
|---|---|---|
| `Q-3` | Are two printed visibility labels equivalent? | **adjudicated here** — RC does not equate them; `ENC-001` preserves them |
| `Q-7` | Who determines which visibility condition obtains in the world? | **unchanged** — not adjudicated, not narrowed |

`Q-3` is answered entirely inside the table. `Q-7` asks who supplies the input *to* the
table. Neither the *who* nor the *which* is touched: no owner is assigned, no selector is
identified, and the accepted packet's `Q-7` row is not modified.

One honest qualification, recorded so it is not mistaken for progress on `Q-7`: this
adjudication fixes the **type** of the input that `Q-7`'s eventual answer must produce — an
RC-native label for the setting in play, not a normalized enum. That constrains the shape of
a future answer. It does not narrow the question, which remains open in full.

### 11. `EXP-006` boundary impact — **none**

`EXP-006` owns **mundane light contribution** — what a torch, lantern or similar light
source provides. `Q-3` is about the vocabulary of a table's Visibility column. Nothing in it
requires moving that boundary, and the boundary is unchanged.

**The tempting error, explicitly rejected:** *"`Very good light` is a dungeon condition,
dungeon light comes from torches, torches are `EXP-006`'s, therefore `EXP-006` owns
`Very good light`."* That does not follow. `EXP-006` owns what a light source contributes;
it does not own the aggregation of contributions into a visibility category, and it has
never owned world visibility. The word "light" appearing in a table label is not an
ownership argument.

### 12. Future `ENC-001` contract consequence

Stated narrowly, as consequence only — this is not a specification and authorizes nothing:

- `ENC-001` should accept the **RC-native visibility label as printed for the setting in
  play**, not a normalized cross-setting visibility enum.
- Valid labels are setting-indexed: `Dungeon*` admits `Very good light`, `Dim light**`,
  `No lightt`; `Wilderness` and `Ocean/sea` admit `Clear daylight`, `Dim light**`,
  `No lightt`; `Undersea` admits `Any light` only.
- A visibility label that does not belong to the supplied setting is a caller error, not
  something `ENC-001` resolves by mapping.

Who produces that label, and from what world state, is **not decided here** and is not
designed here.

### 13. Residue, recorded not resolved

- **The semantic relationship stays unmapped.** Whether one world condition can satisfy both
  `Very good light` and `Clear daylight` is undecided. This adjudication deliberately keeps
  it visible at the `ENC-001` boundary instead of burying it in a normalization step.
- **`Q-7` remains open**, and `ENC-001` still cannot be made total without it.
- **The feet/yards convention remains unowned.** It is visible again here — the same
  brightest tier reads `4d6x 10'` indoors and `4d6 x 10 yards` outdoors — but it is not
  resolved, and `Q-6` in the accepted packet still records the undersea feet/yards tension.
- **`Ocean/sea`/`Ship` flat distances** (`300`, `120`, `40` yards) are not dice expressions.
  Noted because it bears on the eventual contract's return type; not adjudicated.

---

## Q-7 — who determines which visibility category obtains

```text
Q-7 STATUS:  rules/contract question   SETTLED 2026-10-04
                                       by human architecture decision

             world/environment
             visibility OWNER          ASSIGNED 2026-10-04 -- SIM-003

ENC-001 consumes SIM-003-supplied RC-native visibility and validates that it
is legal for the supplied setting. SIM-003 is DEFINED, not designed and not
implemented, and the dependencies it records (Q-4; unowned daylight and
weather determination) remain open.
```

### 1. Question as the accepted packet states it

> Which visibility category obtains at a given moment — no selector in the chapters
> searched, and no Rule ID owns the world state.

Accepted Stage-A disposition: `RETAINED AS GENUINE SOURCE AMBIGUITY`, object `pp. 92, 93`.
The accepted packet also records the scope discipline applied to it:

> `Q-7` is scoped to match the negative claim it rests on. The pilot's wording asserted
> "no RC selector exists" at RC-wide scope while its own claim had been narrowed to the
> chapters searched. The narrower scope is kept and the broader wording deleted.

### 2. The two questions inside `Q-7`, kept apart

```text
A. RULES QUESTION
   Does RC define how to determine the current visibility category?

B. ARCHITECTURE QUESTION
   If RC does not, which simulator component owns the state ENC-001 consumes?
```

These are answered separately below. **A Simulator Ruling may close an RC ambiguity; it may
not be used to assign software ownership**, and none is proposed here.

### 3. Source basis — re-inspected this pass

| Page | Re-inspected | Bearing |
|---|---|---|
| p. 93 | yes (previous pass, this document's `Q-3`) | the table, its Visibility column and all three footnotes |
| p. 95 | **yes, page image this pass** | `Wilderness Encounters` — the sentence naming visibility a *factor* |
| p. 150 | **yes, page image this pass** | Ch. 13 `Blindness`, the darkness ↔ infravision link |

No other page was opened; broad completeness research was not reopened. pp. 24, 91, 92, 100
and 153 are taken from the accepted packet's transcriptions and evidence map rather than
re-inspected, because the accepted record already disposes of them for this question and
nothing here contradicts it.

**p. 95, confirmed verbatim on the page image:**

```text
p. 95  (Wilderness Encounters)
"Play out the encounter as described under "Encounters" on page 91, using the
visibility, distance, and surprise factors."
```

**p. 150, confirmed verbatim on the page image:**

```text
p. 150  (Special Character Conditions -> Blindness)
"Characters can be blinded by a variety of effects. For example, a light or
continual light spell may be cast directly on a character's eyes, or a
character without infravision may find himself in an area of complete
darkness."
```

### 4. Rules finding — what RC does and does not define

**RC defines no selector.** This is the accepted packet's single consequential negative
claim, and it is kept at exactly its established scope — Ch. 7 pp. 91–101, the three table
footnotes, Ch. 6 p. 87, Ch. 13 p. 150, Ch. 14 pp. 153 and 215; **not** Ch. 3 (Spells) or
Ch. 4 (Equipment). It is **not** an RC-wide claim and is not widened here. Nothing inspected
this pass disturbed it: p. 95 supplies no selector and p. 150 supplies no selector.

**But RC is not silent about the *shape* of the dependency, and that is the new finding.**
Three printed facts, read together, show RC treating visibility as a world fact the
adjudicator brings *to* the procedure rather than one the procedure derives:

| Fact | Page | What it shows |
|---|---|---|
| "the DM first needs to know where the characters are--dungeon or wilderness" | 93 | `Setting` is a fact the DM **already holds**. The table does not derive it |
| "using the visibility, distance, and surprise factors" | 95 | Visibility is listed as a **factor**, beside surprise (`ENC-002`-owned input) and distance (`ENC-001`'s output). RC groups it with the inputs |
| "a character without infravision may find himself in an area of complete darkness" | 150 | An *"area of complete darkness"* is presupposed as an existing world condition. RC states the **per-character consequence** of that condition and supplies no procedure for establishing it |

**Necessary Consequence:** in RC's own structure, the visibility category is an **input the
adjudicator supplies**, on exactly the same footing as `Setting`. RC's "selector" is the DM's
knowledge of the fiction. That is a real finding about the dependency's direction, and it is
*not* the same as RC defining a procedure — RC defines none, and none is invented here.

### 5. Inputs that may contribute to world visibility

Identified as categories only; **no aggregation is designed**. The distinction that matters
is the one the approved `EXP-006` card already enforces:

| Contributing world fact | Already owned by | Is it the aggregate category? |
|---|---|---|
| Mundane light sources (lit state, `30'` radius, duration) | `EXP-006` **[LANDED]** | **no** — a radius, not a category |
| Absence of a lit mundane source | `EXP-006`, which asserts **nothing further** from it | **no** — explicitly an absence of *that card's* knowledge |
| Magical light / darkness | `MAGIC-*` | no |
| Infravision possession | `CHAR-009` | no — and `60'` sight in the dark is a range, not a category |
| Daylight / time of day | **nothing** | — |
| Weather impairing vision | **nothing** — RC mentions it twice (footnote `t`; p. 100's DM discretion) but defines no category | — |
| Setting (`Dungeon*` / `Wilderness` / `Ocean/sea` / `Undersea`) | supplied with the encounter | no — the *other* axis |

**The owner of a contribution does not own the aggregate.** Every row above is either a
contribution or an unowned world fact; not one of them is the RC-native category the table
consumes. Two of the categories — daylight/time-of-day and weather — have **no owner at
all**, which is a wider gap than `Q-7` alone.

### 6. Model A — `ENC-001` owns visibility selection

`ENC-001` receives underlying world facts and derives its own RC-native label.

**This is not a hypothetical: it is close to the position the approved `EXP-006` Rule Card
already records.** `EXP-006` §7 states the RC facts are recorded *"for `ENC-001`, which owns
the classification and the resolution"*, and adds that *"whatever aggregation it needs —
mundane light, environmental illumination, magical light, infravision, encounter
circumstances — is **its** rule to write"*. Landed guard tests `L31`–`L33` and `L36` enforce
the `EXP-006` side of that boundary.

**Against it, three things:**

1. **It conflicts with `Q-3`, settled above.** `Q-3` concluded `ENC-001` accepts the RC-native
   label as printed for the setting and must *not* normalize. A card that aggregates light,
   daylight, weather and infravision into a category is deriving the label, not consuming it.
2. **It bloats the card.** `ENC-001`'s accepted scope is encounter-distance determination at
   contact. Aggregating environmental illumination is a different responsibility with
   different inputs, and `ENC-001` owns none of those inputs.
3. **Other subsystems need the same fact.** p. 150's blindness consequence (`CHAR-005` owns
   the movement effect per `EXP-006` §B), `COMBAT-*` attack/save/AC consequences, and
   `EXP-005` searching all turn on whether an area is dark. Per the decision standard, that
   a second subsystem needs the fact is **evidence against** making `ENC-001` the owner — a
   consumer of a fact should not be its producer.

**`EXP-006`'s own structured boundary table draws the line more narrowly than its §7 prose**,
and this is the tension that blocks closure — see section 10.

### 7. Model B — `EXP-006` owns visibility selection

**Excluded by approved governance, not merely disfavoured.** This is a repository fact,
verified in the active pass against the artifacts named:

- The **approved** `EXP-006` Rule Card, under **human adjudication 2026-10-01, Finding B**,
  withdrew exactly this: the card *"produced a `Visibility` category"* — **withdrawn**. The
  ratification line records `EXP-006` owns *"mundane-light contribution, not global/world
  illumination"* and *"does not produce encounter `Visibility`"*.
- Its §6 states what `any_mundane_source_lit == false` means, and lists under **DOES NOT
  MEAN**: `complete darkness`, `NO_LIGHT`, `any Visibility category`, `blindness`.
- The **landed implementation** carries the same boundary. `src/rules/exploration/light_and_exploration_resources.py`
  states it *"owns nothing about the world"* and must not *"state or derive
  global/environmental darkness, encounter Visibility, or blindness"*, citing Rule Card §6,
  §8 and Finding B. Guard tests `L29`–`L33`, `L36` enforce it.

Testing the §6 question directly: would expanding `EXP-006` **(A)** follow naturally from its
accepted responsibility, or **(B)** improperly turn a light-source/resource card into
world-state ownership? **(B).** `EXP-006` owns what *the party's own carried sources*
contribute. World visibility also depends on daylight, weather and magical light it does not
own, and on the absence of its sources — which it is expressly forbidden to read as darkness.
Expanding it would re-commit the precise error a human already withdrew. **Not adopted.** An
agent may not overturn a human adjudication recorded in an approved Rule Card.

### 8. Model C — a world/environment layer owns it

A separate world/environment responsibility determines the RC-native label and passes it to
`ENC-001`, which validates that the label is legal for the supplied setting.

**Strongest on the decision standard**, and it is the model RC's own structure points at
(section 4): the DM holds the world facts and brings visibility to the encounter as a factor.

| Criterion | Model C |
|---|---|
| Single responsibility | **yes** — `ENC-001` stays encounter-distance determination |
| Minimal cross-card knowledge | **yes** — `ENC-001` need not know about torches, weather, daylight or spells |
| No duplicated derivation | **yes** — one producer; `COMBAT-*`, `CHAR-005`, `EXP-005` can consume the same fact |
| Clear caller/callee contract | **yes** — label in, distance out, invalid label refused |
| Future reuse outside `ENC-001` | **yes** — this is the decisive one; several subsystems need it |
| Preserves accepted boundaries | **yes** — `EXP-006` untouched, `ENC-002` untouched, `Q-3` preserved |

It also leaves `Q-3`'s result intact: the world layer emits the label *for the setting in
play*, and `ENC-001` validates rather than normalizes.

### 9. Model D — does an existing Rule ID already own it?

Repository architecture inspection of `docs/rules/INVENTORY.md` and the accepted card
boundaries. This is not RC research.

| Rule ID | Current responsibility | Fits? | Would it broaden the card? |
|---|---|---|---|
| `EXP-006` Light & Exploration Resources | mundane light-source contribution | **no** | **yes** — and forbidden by Finding B |
| `EXP-003` Dungeon Movement | movement rates, mapping, special terrain | no | yes — unrelated axis |
| `EXP-005` Searching, Listening, Doors | search/listen procedures | no | yes — a *consumer* of darkness, not a producer |
| `EXP-008` Dungeon Stocking | what occupies an already-laid-out room | no | yes — content, not ambient conditions |
| `ENC-002` Surprise | surprise determination | no | yes |
| `CHAR-005` | blindness/darkness **movement** consequence | no | yes — consumes the condition |
| `CHAR-009` | infravision **possession** | no | yes — a capability, not a world state |
| `MAGIC-*` | magical light and darkness | no | partial contributor only |
| `SIM-001` Procedural Dungeon **Layout** Generation | layout/map generation only; scope deliberately narrowed | **no** | yes — but see below |

**No existing Rule ID fits.** Two independent artifacts already record this, and they agree:

```text
ENC-001 accepted Stage-A packet, section 10
  World visibility category        NO RULE ID EXISTS

EXP-006 approved Rule Card, section B ("What this card does not own")
  Complete-darkness / environmental
    illumination world state       OWNER NOT SETTLED -- section 8, Open Question 7
```

`EXP-006`'s own Open Question 7 states it outright: *"The complete-darkness /
environmental-illumination world-state predicate has no owner."*

**`SIM-001` is the nearest structural precedent, not a fit.** The `SIM-*` family exists for
responsibilities the simulator must specify *because RC supplies no rule* — `SIM-001` layout
generation, `SIM-002` survivability policy. Ambient illumination is the same kind of thing:
the accepted negative claim establishes RC supplies no rule, so there is nothing for a *Rule
Card* to specify. But `SIM-001`'s scope was deliberately narrowed to layout, and stretching
it would repeat the boundary-blurring that narrowing corrected. **No fit is invented.**

### 10. Ownership disposition — **human architecture decision, 2026-10-04**

The analysis above was returned to the human project owner with a recommendation and two
blockers. **The human project owner decided**, and the decision is recorded here verbatim as
a **human architecture decision — not an RC rule, and not an agent conclusion**:

```text
HUMAN ARCHITECTURE DECISION                    Q-7         2026-10-04
DECIDED BY:  human project owner

EXP-006 does NOT own aggregate/world visibility.

ENC-001 does NOT derive aggregate/world visibility.

ENC-001 consumes a caller-supplied RC-native visibility label
appropriate to the supplied setting and validates that input.

World/environment visibility is a separate ownership responsibility.
```

This selects **Model C** and rejects **Models A and B**. It also resolves blocker 2 by
choosing the `EXP-006` **§B** boundary over §7's broader prose — see section 14, where the
authorized reconciliation of that protected wording is recorded.

**What is settled, and what is not.** The distinction is load-bearing and is not a formality:

| | Status |
|---|---|
| The **rules/contract** question — *what does `ENC-001` do about the dependency?* | **SETTLED.** It consumes a supplied, setting-valid RC-native label, validates it, and refuses when a required one is absent |
| The **world/environment visibility owner** — *what component produces that label?* | **ASSIGNED** — see immediately below |

```text
WORLD/ENVIRONMENT VISIBILITY OWNER ASSIGNED        2026-10-04
SIM-003 -- World/Environment Visibility Classification
docs/technical/SIM-003_WORLD_VISIBILITY_CLASSIFICATION.md

Authority:  human architecture decision, 2026-10-04, approving the
            ownership analysis at the end of this document.
Scope:      CLASSIFICATION ONLY -- derives exactly one RC-native
            visibility label valid for the supplied setting.
Form:       a Simulator Specification (Non-Historical Design
            Requirement), NOT a Rule Card. RC supplies no mechanic
            here, so there is nothing for a Rule Card to specify.
```

**`Q-7` is now fully settled as an `ENC-001` Stage-B dependency:**

```text
ENC-001 consumes SIM-003-supplied RC-native visibility and validates
that it is legal for the supplied setting.
```

**What remains open, and is not hidden by this closure.** The *ownership* question is closed;
three dependencies `SIM-003` records are not, and none of them is `ENC-001`'s to resolve:
`Q-4` (whose infravision satisfies the p. 93 `**` footnote), and the fact that **daylight /
time-of-day and weather determination still have no owner** — they are scenario-supplied
inputs today. `SIM-003` is **defined, not designed and not implemented**.

### 11. Simulator Ruling — **not required**

```text
NO NEW SIMULATOR RULING

Q-7's rules half is an RC omission, and its remaining half is an ownership
question. A Simulator Ruling closes an RC ambiguity; it must not be used to
assign software ownership, and it must not paper over an architecture
ownership gap. SR-13 remains the next free identifier and is not used here.
```

**Confirmed after the decision.** The human decision of §10 is an architecture decision, and
it produced no residual game-rule ambiguity requiring a ruling: `ENC-001` consumes a label RC
already names and refuses when it is absent, neither of which extends an RC mechanic. `SR-13`
remains free. Should the later ownership decision surface a residual rules ambiguity, a
narrow `SR` could be proposed then — `PROPOSED — human approval required`, never
self-approved.

### 12. Relationship to `Q-3` — consistent, and `Q-3` is preserved

`Q-3` settled that `ENC-001` preserves RC-native labels, setting-indexed, and does not
normalize them. The decision selects Model C, which is the ownership model that **makes `Q-3`
implementable**: someone must emit the label `Q-3` says `ENC-001` consumes. Model A would
have strained `Q-3`, and it was rejected.

**`Q-3` is unchanged by the `Q-7` decision, and specifically is not collapsed:**

```text
Dungeon*                 Very good light   Dim light**   No lightt
Wilderness / Ocean-sea   Clear daylight    Dim light**   No lightt
Undersea                 Any light

Very good light and Clear daylight remain DISTINCT RC-native labels.
The caller supplies the one valid for the setting in play.
ENC-001 validates; it does not normalize them into one category.
```

### 13. Relationship to `SR-12` and "normal dungeon conditions"

`SR-12` is **not reopened**. It resolved the duplicate-distance-track question — distance is
determined once, by the pp. 92–93 procedure — and decided nothing about visibility.

**Stated plainly, because it is the tempting shortcut:** an ordinary dungeon encounter still
has **no supplied visibility category**. `"normal dungeon conditions"` is **not** concluded to
mean `Dim light`. That inference was classified `QUALIFIED, not forced` in `EXP-006`'s
accepted evidence, **withdrawn entirely by human adjudication 2026-10-01 (Finding A)**, and is
guarded against in landed code by `EXP-006` test `L30`. `ENC-001` must not now perform the
derivation `EXP-006` was forbidden to perform.

### 14. `EXP-006` boundary impact — **none; its §7 wording reconciled to its §B boundary**

`EXP-006` keeps exactly its accepted boundary: mundane light-source contribution, and nothing
about the world. It is **not expanded and not shrunk**, and the §6 test was applied in
section 7 with result **(B)** — expanding it would turn a resource card into world-state
ownership.

**The reconciliation was authorized by the human and performed.** The approved card contained
an internal contradiction, found by the analysis above:

| | Before |
|---|---|
| `EXP-006` **§7** | *"`ENC-001` is `[UNRESEARCHED]`; whatever aggregation it needs — mundane light, environmental illumination, magical light, infravision, encounter circumstances — is **its** rule to write"* — routing world/environment aggregation to `ENC-001` |
| `EXP-006` **§B** | `Visibility classification → ENC-001`; `Complete-darkness / environmental illumination world state → OWNER NOT SETTLED` |

**The human chose §B.** `EXP-006` §7 was therefore minimally corrected so that it no longer
assigns world/environment aggregation to `ENC-001`. Its corrected meaning:

```text
EXP-006 supplies only its owned light-source contribution and state.

ENC-001 CONSUMES a Visibility category for the encounter-distance lookup,
and owns the classification SCHEME -- which categories exist, which are
legal for which Setting, how the table is keyed.

Aggregating world/environment facts -- daylight and time of day, weather,
magical light, environmental darkness -- into a Visibility category is
owned by NEITHER card.

That responsibility is UNASSIGNED pending a separate architecture decision.
```

**What the correction did not touch**, because §7 of this task requires all of it to remain
true: `EXP-006` still owns mundane light-source contribution and resource behaviour, and
still owns **none** of daylight/time-of-day, weather visibility, magical-light aggregation,
environmental/global darkness, or the final encounter visibility category. `SR-11` is
unaltered, as is every other `EXP-006` adjudication, every guard test, the §B boundary table
itself, and the implementation. `EXP-006` research was not reopened. This is a
protected-document **consistency** correction under `AGENTS.md` §12, performed on explicit
human direction.

One incidental improvement in the same sentence: the corrected text no longer restates
`ENC-001`'s status as `[UNRESEARCHED]`. That was both stale (Stage A is `ACCEPTED`) and a
secondary restatement of a volatile fact `EXP-006` does not own
(`DEVELOPMENT_WORKFLOW.md` §4.1). It is dropped rather than updated, which is what the
single-owner status model requires.

### 15. Future `ENC-001` contract consequence

Narrow, now carried by the human decision, and still **not a specification** — no API, no
error type and no parameter beyond `visibility` is settled here, and no code is written:

```text
determine_encounter_distance(
    setting,            # Dungeon* / Wilderness / Ocean-sea / Undersea
    visibility,         # CALLER-SUPPLIED RC-native label, valid for the setting
    surprise_state,     # ENC-002's, consumed (SR-12)
    encounter_type,     # Ship / Monster / DM's choice, where the setting needs it
    ...
)
```

`visibility` is **caller-supplied** and must be valid for `setting` (`Q-3`). `ENC-001`
validates; it does not derive, aggregate or normalize. No other parameter is settled here,
and no code is written.

### 16. Missing-visibility behaviour — **explicit refusal, human-approved**

```text
HUMAN DECISION                                 Q-7         2026-10-04

If visibility is required by ENC-001 and is not supplied:
    explicit refusal / error

ENC-001 must NOT:
    silently default to Dim light
    infer aggregate visibility from EXP-006 alone
```

The three options, and why the approved one is the only tenable one:

| Option | Verdict |
|---|---|
| Derive internally | **No** — that is Model A, rejected by the decision in §10 |
| Default silently | **No** — RC supplies no default. Defaulting to `Dim light` re-commits Finding A, which a human withdrew and `EXP-006` guard `L30` forbids; defaulting to any other row invents a rule |
| Infer from `EXP-006` alone | **No** — explicitly excluded. `EXP-006` asserts nothing about the world from the absence of its own sources (§6 `DOES NOT MEAN`), so inferring from it would read an absence of knowledge as a fact |
| **Refuse / error** | **Yes** — the only option that neither invents a rule nor guesses |

**The accepted surprise short-circuit is preserved.** p. 92 sends both-surprised and
one-surprised encounters to a flat `1d4 × 10'` without consulting the table, so visibility is
required **only** on the neither-surprised path. Refusal is scoped to that path, and
`ENC-001` must **not** demand visibility merely for formality where surprise has already made
it unnecessary.

**Not designed here:** no API shape, no error type, no exception hierarchy. Nothing is
implemented.

### 17. Provenance classification

| Conclusion | Classification |
|---|---|
| RC defines no visibility selector (scope: the chapters the accepted packet searched) | **Rules Cyclopedia Explicit**, scope-limited negative finding — **not** RC-wide |
| p. 93 "the DM first needs to know where the characters are"; p. 95 "using the visibility, distance, and surprise factors"; p. 150's presupposed "area of complete darkness" | **Rules Cyclopedia Explicit** — page images re-inspected |
| Visibility is **supplied rather than derived** by `ENC-001` | **Necessary Consequence** (RC's own structure, §4) **+ human architecture decision** (§10) — both, and neither alone |
| `ENC-001` **validates** setting-compatible RC-native labels | **Repository Boundary / Architecture** |
| Missing required visibility ⇒ refusal | **Necessary Consequence**, **approved by the human** (§16) |
| `EXP-006` cannot own it (Finding B, §6 `DOES NOT MEAN`, guards `L29`–`L33`) | **Repository Boundary / Architecture** — verified against the approved card and landed module |
| No existing Rule ID fits; `SIM-001` is precedent, not a fit | **Repository Boundary / Architecture** |
| `EXP-006` §7 reconciled to its §B boundary | **Repository Boundary / Architecture** — human-directed protected-document consistency correction |
| **World/environment visibility owner** | **UNRESOLVED OWNERSHIP DECISION** — still unassigned |
| Any equivalence, default or derived category | **none issued** — no Simulator Ruling |

**No architecture choice above is labelled as an RC rule.** In particular the §10 decision is
a *human architecture decision*, not `Rules Cyclopedia Explicit`: RC supplies no selector, and
nothing here pretends it does.

### 18. Residue

- **The world/environment visibility owner is now assigned** — `SIM-003`, by human
  architecture decision 2026-10-04. `SIM-003` is **defined, not designed and not
  implemented**, so a deterministic end-to-end encounter still cannot be *run*; what has
  changed is that the responsibility is named and bounded rather than missing.
- **Daylight/time-of-day and weather still have no owner.** `SIM-003` *consumes* them as
  scenario-supplied facts and explicitly does not own their determination. This is a gap
  wider than `Q-7`, carried forward as `SIM-003` open dependencies 2 and 3.
- **`Q-4` remains unresolved** — whose infravision satisfies the p. 93 `**` footnote, and
  which rule applies it. `SIM-003` preserves it rather than closing it.
- **`EXP-006` §7 vs §B is resolved** — the human chose §B and §7 was corrected to match. No
  residue remains on that point.
- **A minor provenance inaccuracy in the accepted packet, reported not fixed.** Its §10 basis
  row quotes `EXP-006`'s module as *"Not a statement about the world"*. The module's actual
  words are *"It owns nothing about the world"* and *"never a fact about the world"*. The
  substance is identical and the routing conclusion is unaffected; the quotation marks are
  inexact. The accepted packet is **not** modified — it is accepted evidence.
- **`Q-9` and the feet/yards gap were untouched by this `Q-7` pass.** `Q-9` has since been
  adjudicated separately — see the `Q-9` section below. Feet/yards remains unowned.

---

## World/environment visibility — ownership analysis

```text
STATUS:  ANALYSIS, 2026-10-04 -- APPROVED AND ACTED ON

         Recommendation CREATE NEW SIM-* SPECIFICATION was approved by the
         human project owner on 2026-10-04. SIM-003 was created and
         registered; see the Q-7 disposition above. The analysis below is
         preserved as the reasoning that produced it, unaltered.
```

Authorized as a bounded architecture pass after the `Q-7` decision settled `ENC-001`'s
contract and left the producer unassigned. It defines **responsibility, not mechanics**.

### 1. The ownership problem, stated precisely

The unresolved responsibility is **not "visibility"**. It is:

```text
the AGGREGATION of world/environment facts into the single RC-native
visibility category that ENC-001 consumes for the Encounter Distances
Table lookup.
```

Current evidence has exposed these candidate inputs. **They are not assumed to share one
owner** — several already have owners, and determining the *smallest coherent* boundary is
the whole task:

| Input | Owner today |
|---|---|
| daylight / time-of-day | **none** |
| weather impairing vision | **none** |
| environmental / global darkness | **none** (`EXP-006` §8, `OWNER NOT SETTLED`) |
| mundane light-source contribution | `EXP-006` **[LANDED]** |
| magical-light contribution | `MAGIC-*` |
| setting | supplied with the encounter |
| infravision (character capability) | `CHAR-009` |

### 2. Layer decomposition — and what the owner should *not* take

| Layer | Contents | Should the proposed owner own it? |
|---|---|---|
| **World / environment facts** | daylight, weather, darkness, ambient illumination of an area, setting | **No — they already have a home.** See the finding below |
| **Contributions** | mundane light sources (`EXP-006`), magical light (`MAGIC-*`) | **No** — owned, and consumed as inputs |
| **Character-specific capabilities** | infravision, blindness, other perception effects | **No** — see §9 below; collapsing these into shared world state would make a *world* fact depend on who is standing in the room |
| **Derived encounter input** | the RC-native visibility category `ENC-001` consumes | **Yes — this, and only this** |

**The reframing finding.** `ARCHITECTURE.md` §6 already defines a **Dungeon State** domain
containing *"rooms/areas"* and *"persistent environmental changes"*, and a **Campaign State**
domain containing *"calendar/time"*. The raw world facts therefore **already have an
architectural home**: they are authored or generated per-area/per-campaign **data**, not
something a rule derives. RC supplies no determination procedure for them precisely because
there is nothing to derive — the DM simply knows the room is dark, exactly as the DM *"first
needs to know where the characters are"* (p. 93).

What has **no** home is the step that turns those facts into one RC-native label. That, and
not "the world", is the gap.

### 3. Existing-owner search

Re-confirmed against `INVENTORY.md` and the accepted/approved card boundaries; no RC research
reopened.

| Candidate | Responsibility | Fit |
|---|---|---|
| `EXP-003` Dungeon Movement | movement rates, mapping | no — unrelated axis |
| `EXP-005` Searching, Listening, Doors | search/listen procedures | no — a *consumer* of darkness |
| `EXP-006` Light & Exploration Resources | mundane light-source contribution | **no — forbidden**, Finding B, guards `L29`–`L33` |
| `EXP-008` Dungeon Stocking | what occupies an already-laid-out room | no — content, not ambient conditions |
| `ENC-001` Encounter Distance | distance at contact | **no — excluded by the `Q-7` decision** |
| `ENC-002` Surprise | surprise determination | no |
| `CHAR-005` | blindness/darkness **movement** consequence | no — consumer |
| `CHAR-009` | infravision **possession** | no — a capability |
| `MAGIC-*` | magical light and darkness | no — one contributor |
| `SIM-001` Procedural Dungeon **Layout** Generation | layout/map generation only | no — see Option B |

**No existing Rule ID fits**, consistent with the two independent records already on file
(`ENC-001` packet §10 `NO RULE ID EXISTS`; `EXP-006` §B `OWNER NOT SETTLED`).

### 4. Option A — extend an existing Rule ID

**Rejected, and on a structural ground stronger than "no card fits".** A **Rule Card
specifies an RC mechanic**. The accepted packet's consequential negative claim establishes
that RC supplies **no** procedure for determining which visibility category obtains. There is
therefore no RC mechanic for *any* Rule Card to specify. Option A is the wrong **artifact
class**, independently of which ID is chosen — and every candidate above would additionally
require substantial scope inflation.

### 5. Option B — extend `SIM-001`

**Rejected.** `SIM-001` owns *"layout/map generation only"*, and its scope was **deliberately
narrowed** in the current `INVENTORY.md` revision, which warns in terms that stocking,
monster and treasure determination *"must not be silently absorbed into `SIM-001`"*.
Absorbing world visibility would repeat precisely the boundary-blurring that narrowing
corrected. **`SIM-*` prefix similarity is not evidence of fit** and is not treated as any.

### 6. Option C — a new, narrowly scoped `SIM-*` specification

**Fits the existing taxonomy exactly.** `INVENTORY.md`'s `SIM-*` table is titled **"Simulator
Specifications (Non-Historical Design Requirements)"** and carries a **"Constraint Source"**
column — the family exists for responsibilities the simulator must specify *because RC does
not supply them*. The constraint source here is already on file and accepted: the `ENC-001`
negative claim.

**The scope-creep risk is real and is the thing to control.** A responsibility shaped as
*"owns shared world/environment predicates that RC assumes the DM knows"* is **too broad** —
it would grow into daylight, weather, time and propagation, and §11's reject condition would
fire. The boundary below is therefore narrowed to the **derivation only** (see §7), which is
what makes this option viable rather than what makes it dangerous.

### 7. Option D — unnumbered orchestration responsibility

**Rejected as the whole answer, but it is half right.** Its insight is correct: the *raw
facts* genuinely do belong to scenario/world data, and §2's finding is that they already have
a home in `ARCHITECTURE.md` §6 — **no new artifact is needed for them**.

It fails for the *derivation*, on two grounds:

1. **Governance.** An unnumbered responsibility has no approved boundary, no
   non-responsibility list and no guard tests. The `EXP-006` §7 contradiction this project
   just repaired was created exactly that way — by informal prose routing a responsibility
   nobody owned.
2. **Reuse.** Several consumers need the same derivation (§9). With no artifact, each would
   re-derive it, which is the duplicated-classification outcome the design standard forbids.

### 8. Aggregation boundary — **B: own the final classification, not the raw facts**

| Option | Verdict |
|---|---|
| A. raw world facts only | **No** — the gap would persist; someone must still aggregate, and `ENC-001` and `EXP-006` are both excluded |
| **B. the final RC-native visibility classification** | **Yes** — one cohesive derivation, with inputs it reads but does not own |
| C. both | **No** — this is the *"everything about the world"* subsystem the reject condition names |

Coupling check against the four things the design must avoid:

| Must avoid | Under B |
|---|---|
| `ENC-001` understanding light-source internals | avoided — it receives a label |
| `EXP-006` understanding encounter tables | avoided — unchanged; it keeps contributing |
| character cards owning global world state | avoided — see §9 |
| duplicated visibility classification | avoided — derived once, consumed by many |

### 9. Infravision boundary — **excluded from world visibility**

The p. 93 footnote `**` (*"Or full darkness with infravision used"*) folds a **character
capability** into a **table-row selection**. It must **not** be folded into world state:

- infravision is character-specific (`CHAR-009` owns possession); a party is typically mixed,
  so a *world* category that depended on it would vary by who is present — incoherent;
- RC gives it its own constraints, which the accepted packet preserves: `60'` in the dark,
  **suppressed by normal and magical light** (`E-18`), and recognition only within `10'`
  (`E-31`). These are perception limits, not ambient-illumination facts;
- **`Q-4` is unresolved** — *"Whose infravision satisfies footnote `**` — any one member's,
  all, or the noticing side's? RC does not say."* Folding infravision into the world category
  would silently adjudicate `Q-4`, which is out of scope.

**Therefore:** the proposed owner exposes the **world** visibility state, and the footnote
`**` adjustment is applied by the consuming rule, with the character capability supplied
separately. **No universal perception engine is proposed.**

> **Known unresolved dependency, recorded not closed.** *Which* rule applies footnote `**`,
> and on *whose* infravision, cannot be settled without `Q-4`. `ENC-001` is the likeliest
> applier since the footnote is printed on its own table, but that is an observation, not a
> decision, and it is **not** adjudicated here.

### 10. Known consumers — the reuse justification

| Consumer | Needs ambient visibility for | Evidence |
|---|---|---|
| `ENC-001` | the Encounter Distances Table lookup | **evidenced** — accepted Stage-A packet |
| `CHAR-005` | blindness/darkness **movement** (⅓ unguided, ⅔ guided) | **evidenced** — `EXP-006` §B routing, RC p. 150 |
| `COMBAT-*` | blindness attack/save/AC consequences (`−4`/`−6`/`+4`) | **evidenced** — `EXP-006` §B routing, RC p. 150, corroborated p. 154 |
| `EXP-005` searching/listening | plausible | **not evidenced here** — not asserted |
| `EXP-003` movement/navigation | plausible | **not evidenced here** — not asserted |
| `ENC-002` surprise | plausible | **not evidenced here** — not asserted |

**Three evidenced consumers besides `ENC-001`** is the reuse case, and it is drawn from
approved artifacts rather than speculation. The speculative rows are labelled as such and
none of these consumers is designed here.

### 11. Proposed artifact form — **not created**

```text
IDENTIFIER CLASS:  SIM-*  (Simulator Specification -- Non-Historical
                   Design Requirement). The next free number is SIM-003,
                   verified by enumerating SIM-N across the repository
                   (SIM-001, SIM-002 in use). NOT ASSIGNED, NOT REGISTERED.

TITLE (proposed):  World/Environment Visibility Classification

CONSTRAINT SOURCE: ENC-001 accepted Stage-A evidence -- RC states no
                   procedure for determining which visibility category
                   obtains (scope: the chapters searched).

RESPONSIBILITY:    Derive, once, the RC-native visibility category for a
                   given setting and location, from supplied world facts
                   and owned contributions. Nothing else.

INPUTS:            setting; ambient/environment state of the area
                   (scenario- or state-supplied); EXP-006's mundane light
                   contribution; MAGIC-* magical light contribution;
                   outdoor daylight and weather state (scenario-supplied).

OUTPUT:            exactly one RC-native visibility label, valid for the
                   supplied setting, per Q-3's setting-indexed vocabulary.

NON-RESPONSIBILITIES (explicit):
                   day/night cycle mechanics
                   weather generation rules
                   light propagation / illumination engine
                   terrain or weather simulation
                   calendar or time system          (EXP-002 owns turns)
                   character perception, infravision, blindness
                   the footnote ** adjustment        (depends on Q-4)
                   encounter distance                (ENC-001)
                   light-source resource behaviour   (EXP-006)
                   feet/yards unit convention        (still unowned)

CONSUMERS:         ENC-001, CHAR-005, COMBAT-*  (evidenced)

UNRESOLVED DEPENDENCIES:
                   Q-4   -- whose infravision satisfies footnote **
                   daylight/time-of-day has no owner
                   weather visibility has no owner
                   feet/yards has no owner
```

**Where RC supplies no procedure, the fact is recorded as caller/scenario-supplied or as a
future ownership gap — never invented here.** Daylight and weather are both: they are inputs
this responsibility would *read*, and their own determination remains unowned.

### 12. Comparison

| | Scope cohesion | Reuse | Coupling | Taxonomy fit | Creep risk | New machinery |
|---|---|---|---|---|---|---|
| **A** extend a Rule ID | poor | — | high | **wrong artifact class** — no RC mechanic to specify | high | moderate |
| **B** extend `SIM-001` | poor — two unrelated jobs | low | moderate | superficial only | **high** — repeats a corrected error | low |
| **C** new `SIM-*`, classification only | **strong** | **high** | **low** | **exact** | **low**, if §8-B scoped | **one small artifact** |
| **D** unnumbered orchestration | n/a | **low** — duplication | moderate | none — no governance | moderate | none |

### 13. Recommendation

```text
CREATE NEW SIM-* SPECIFICATION
```

It is the only option that satisfies every success criterion at once: `EXP-006` can remain
unchanged, `ENC-001` can remain narrow, the category is derived **once**, other evidenced
systems consume the same state, and character-specific perception stays separate. Options A
and B fail on artifact class and on a scope narrowing that must not be undone; D is right
about the raw facts — which is why §8-B leaves them where `ARCHITECTURE.md` §6 already puts
them — but gives the derivation no boundary and invites duplication.

The reject condition was tested and does **not** fire: the proposal is not a generic
"everything about the world" subsystem. It owns one derivation and explicitly disclaims
day/night, weather, propagation, terrain, calendar and perception.

### 14. Approval boundary

```text
NEW OWNERSHIP ARTIFACT RECOMMENDED -- HUMAN APPROVAL REQUIRED
```

**That approval was given on 2026-10-04**, and the recommendation was acted on in the same
form it was recommended: `SIM-003 — World/Environment Visibility Classification`,
**classification only**, registered under *Simulator Specifications* in `INVENTORY.md` and
specified at `docs/technical/SIM-003_WORLD_VISIBILITY_CLASSIFICATION.md`. The boundary shipped
is the boundary analysed — not a broader one — and `SIM-003` is defined, **not** designed and
**not** implemented.

*Recorded as at the time of the analysis:* no existing owner fitted without scope inflation,
so no existing artifact was nominated.

---

## Q-9 — `aerial` and the table's Setting axis

### 1. Question as the accepted packet states it

> The Chance of Encounter Table lists **aerial** terrain, but the table has no Aerial Setting
> row and RC gives no City-style bridge.

Accepted Stage-A disposition: `RETAINED AS GENUINE SOURCE AMBIGUITY`, object `pp. 92, 93`.
The supporting evidence row is `E-27` (p. 92, *Unresolved by RC*): *"The Chance of Encounter
Table lists aerial as a wilderness terrain, but the Encounter Distances Table has no Aerial
Setting row."*

### 2. Source basis — re-inspected this pass

| Page | Re-inspected | Supplies |
|---|---|---|
| p. 92 | **yes, page image this pass** | the Chance of Encounter Table, its terrain list and **both footnotes** — the material `E-27` rests on |
| p. 93 | yes (`Q-3` pass, incl. a magnified crop) | the Encounter Distances Table and its Setting axis |
| p. 95 | yes (`Q-7` pass) | the Wilderness Encounters Table, which carries a `Flyer` entry in every terrain column |

No whole-book aerial search was performed and no new source area was opened. `E-27`'s
paraphrase was verified against the page image rather than relied on.

### 3. The exact printed facts

```text
p. 92   Chance of Encounter Table

Type of Encounter    Roll Method
Dungeon and city     Roll 1d6 every two turns when traveling and roll 1d12 once
                     during the night; on a 1, an encounter occurs
Wilderness           Determine the type of terrain the party is in and roll 1d6 once
                     during the day and roll 1d12 once when camped at night;
                     consult the following for encounter occurrences

Type of Terrain                                                   Chance
Clear, grasslands, inhabited, or settled                            1
Forest, river, hills, barren lands, desert, ocean*, or aerial**    1-2
Swamp, jungle, or mountains                                        1-3

 *  Ocean: A roll of 1 indicates a normal ocean encounter. A roll of 2 indicates
    no encounter unless the ship lands at the end of the day; if so, a land
    encounter is used.
 ** Aerial encounters always use the Flyers subtable in the Wilderness Encounter
    Table, regardless of terrain.
```

Two further printed facts already in the accepted packet, both load-bearing here:

```text
p. 92  "When neither party is surprised, take a look at the Encounter Distances
        Table. When the type of terrain (dungeon, wilderness, ocean/sea, or
        underwater) is known, the DM can find out how far apart the groups are
        when the encounter takes place."

p. 93  "When a random encounter is to occur, the DM first needs to know where the
        characters are--dungeon or wilderness."
```

### 4. The four questions, answered separately

```text
A. Does RC recognize aerial encounters elsewhere?        YES -- explicitly
B. Does the Encounter Distances Table have an Aerial
   Setting row?                                          NO  -- absence recorded
                                                              as absence
C. Does RC explicitly route aerial encounters to one of
   the printed rows?                                     NOT for DISTANCE.
                                                         It routes them to the
                                                         Wilderness table for
                                                         MONSTER SELECTION.
D. Can ENC-001 stay deterministic without inventing a
   mapping?                                              YES -- see section 7
```

**C is where the care is needed.** Footnote `**` routes aerial encounters to the *Flyers
subtable in the Wilderness Encounter**s** Table* — the **monster-selection** table on p. 95,
**not** the Encounter **Distances** Table on p. 93. Those are different tables, and the
existence of aerial movement, aerial monsters or an aerial encounter-frequency band is **not**
evidence that a distance row exists. The two are not conflated below.

### 5. The structural finding — `aerial` is not a Setting peer

The Chance of Encounter Table has **two levels**, and `aerial` sits at the lower one:

```text
LEVEL 1   Type of Encounter     Dungeon and city  |  Wilderness
LEVEL 2   Type of Terrain       clear / grasslands / inhabited / settled
          (applies ONLY to      forest / river / hills / barren lands / desert /
          the Wilderness          ocean / AERIAL
          roll method)          swamp / jungle / mountains
```

`aerial` is a **Type of Terrain inside the Wilderness branch** — it is listed in the terrain
band the *Wilderness* roll method says to consult ("Determine the type of terrain the party is
in… consult the following"). It is never presented as a peer of `Dungeon`/`Wilderness`.

The Encounter Distances Table's `Setting` axis is the **upper** level. p. 92 names that axis
*"the type of terrain (dungeon, wilderness, ocean/sea, or underwater)"*, and p. 93 reduces the
basic question to *"where the characters are — dungeon or wilderness"*.

**So the two taxonomies are at different granularities, and `Q-9` compares across them.** The
Encounter Distances Table is not missing an `Aerial` row for the same reason it is not missing
a `Swamp` row, a `Desert` row or a `Jungle` row — **none of those is a Setting either**. Every
one of them is a Level-2 wilderness terrain.

That is the finding. `Q-9` reads as a gap only while `aerial` is taken for a Setting; once the
table's own two-level structure is read off the page, there is nothing missing.

### 6. Movement mode vs Setting

Tested on RC structure, not intuition:

| Question | RC's answer |
|---|---|
| Is `Setting` about where the **characters** are? | **Yes** — p. 93, *"where the characters are"*; p. 92, *"the type of terrain the party is in"* |
| Can a flying creature be encountered in a dungeon? | Nothing prevents it; the encounter is still a *dungeon* encounter, because that is where the party is |
| Does a creature's movement mode change the Setting? | **No** — Setting is a property of the location, not of a participant's locomotion |
| Does RC ever make `aerial` exclude a terrain? | **The opposite.** Footnote `**` says aerial encounters use the Flyers subtable *"regardless of terrain"* — terrain still exists and still applies; `aerial` overlays it |

**`aerial` therefore behaves as a movement-mode-derived encounter descriptor layered over
terrain, not as a mutually exclusive world Setting.** Footnote `**`'s own *"regardless of
terrain"* is the strongest printed evidence for this: a category that coexists with every
terrain is not a member of a mutually exclusive terrain partition.

### 7. Competing interpretations

**Interpretation A — aerial encounters use the `Wilderness` Setting.** *Adopted, for the
wilderness-branch case, on structure rather than on the intuition that "flying is outdoors".*
RC itself files `aerial` under the Wilderness roll method (p. 92, Level 2) and sends aerial
encounters to the Wilderness Encounters Table *always, regardless of terrain* (footnote `**`,
corroborated by the `Flyer` entries visible on p. 95). The intuitive version of A — *"flying
is outdoors, Wilderness is the outdoor row"* — is **not** what carries it; RC's own placement
of `aerial` inside the Wilderness branch is.

**Interpretation B — use the underlying surface Setting.** *Not adopted.* It is actively
disfavoured by printed text: footnote `**` says aerial encounters use the Flyers subtable
**"regardless of terrain"**, which is RC declining to let the surface govern the aerial case.
RC nowhere defines Setting by what lies beneath the participants.

**Interpretation C — aerial is outside the table's domain.** *Not adopted.* It presumes
`aerial` is a Setting whose row is missing. §5 shows it is a Level-2 terrain, so there is no
domain hole: an aerial encounter happens where the characters are, and that location has a
Setting. Adopting C would manufacture an unsupported-case branch for a case RC already covers.

**Interpretation D — none.** No further reading is supported by the primary text inspected,
and none is invented to pad the list.

### 8. The four required cases

| | Case | Setting | Basis |
|---|---|---|---|
| **A** | Flying creatures inside a large cavern/dungeon | **`Dungeon*`** | The party is in a dungeon; `Type of Encounter` is *Dungeon and city*, a different roll method whose terrain list does not apply. Movement mode does not relocate the party |
| **B** | Flying encounter over open wilderness | **`Wilderness`** | `aerial` is a Level-2 terrain in the Wilderness branch; Setting is the Level-1 value |
| **C** | Flying encounter over ocean | **`Wilderness`** on Interpretation A; `Ocean/sea` on B. **RC does not explicitly resolve this for *distance*** — see the residue note below |
| **D** | High-altitude encounter, no meaningful surface environment | **`Wilderness`** | Still a Wilderness-branch encounter; no row is missing, so no refusal arises |

> **Case C, stated honestly.** RC's footnote `**` settles the *monster* question for aerial
> over water (Flyers subtable, regardless of terrain) but says nothing explicit about which
> **Setting row** supplies the distance. The accepted packet's own `Q-6`-adjacent care applies:
> absence is recorded as absence.
>
> **It has no mechanical consequence, and that is an observation, not the argument.** The
> `Wilderness` rows and the `Ocean/sea` **`Monster`** rows carry identical distance
> expressions at every visibility tier — `4d6 x 10 yards`, `2d6 x 10 yards`, `1d4 x 10 yards`
> — and aerial encounters produce *Flyers*, i.e. monsters, not Ships, so the `Ocean/sea`
> `Ship` rows (the only ones that differ) are not reachable by an aerial encounter. Both
> admissible readings therefore coincide. **Identical numbers are not identical mechanics** —
> this project has twice declined to reason from a shared dice expression — so this is
> recorded as corroboration that the open point is harmless, **not** as proof that the two
> Settings are the same.

### 9. Adjudication

**`Q-9` does not describe a defect in the Encounter Distances Table.** The table has no
`Aerial` Setting row because **`aerial` is not a Setting** — it is a Type of Terrain inside
the Chance of Encounter Table's *Wilderness* branch, at a different level of RC's taxonomy
from the Setting axis. The absence is correct, not missing.

An aerial encounter takes its Setting from **where the characters are**, exactly as every
other encounter does. No mapping is invented, no printed Setting vocabulary is broadened, and
`Aerial` is **not** added to the Setting domain.

Adjudicated at steps 1–3 of the order; steps 4 and 5 are **not reached**:

```text
1. RC Explicit ............... aerial is a Type of Terrain under the Wilderness
                               roll method; footnote ** routes aerial encounters
                               to the Wilderness Encounters Table
2. Necessary Consequence ..... the Setting axis is the upper taxonomic level, so
                               a Level-2 terrain cannot be a missing Setting row
3. Caller-supplied Setting ... fully resolves it; ENC-001 validates
4. Narrow Simulator Ruling ... NOT REACHED
5. Unsupported / refusal ..... NOT REACHED
```

```text
NO NEW SIMULATOR RULING

The table was never missing a row, so no RC-unsupported choice has to be
made. Issuing an SR merely because a label does not appear in a column
would invent a category RC does not have. SR-13 remains the next free
identifier and is not used here.
```

### 10. Provenance classification

| Conclusion | Classification |
|---|---|
| `aerial` is a Type of Terrain listed under the `Wilderness` roll method | **Rules Cyclopedia Explicit** — p. 92 page image |
| Aerial encounters always use the Flyers subtable in the Wilderness Encounters Table, regardless of terrain | **Rules Cyclopedia Explicit** — p. 92 footnote `**`, corroborated by p. 95's `Flyer` entries |
| The Setting axis is the upper taxonomic level (*dungeon, wilderness, ocean/sea, underwater*) | **Rules Cyclopedia Explicit** — p. 92 prose, p. 93 prose |
| `aerial` is therefore not a missing Setting row | **Necessary Consequence** of the two levels above |
| Setting is a property of where the characters are, not of a participant's movement mode | **Necessary Consequence** |
| `ENC-001` consumes and validates a caller-supplied Setting | **Repository Boundary / Architecture** |
| Which Setting an over-ocean aerial encounter uses for *distance* | **Unresolved Dependency** — not explicitly stated by RC; shown non-consequential, not resolved |
| Any Setting mapping for `aerial` | **none issued** — no Simulator Ruling |

**No intuitive mapping is described as RC Explicit.** In particular the reading *"flying is
outdoors, so use Wilderness"* is **not** the basis of §9; RC's own placement of `aerial` inside
the Wilderness branch is.

### 11. `SIM-003` impact — **none**

`SIM-003` owns **visibility classification for a supplied Setting**. It does **not** choose the
Setting, and `Q-9` does not extend it: nothing here makes `SIM-003` a spatial or terrain
classifier, and its `INVENTORY.md` row and specification are unchanged.

**Is there a separate Setting-owner gap?** Examined, and the answer is **no** — stated with
the reason, so this is not merely an assertion:

- World **visibility** needed an owner because it is an **aggregation**: several contributing
  facts (light, daylight, weather, darkness) have to be combined into one category, and no
  component owned that combination. That is why `SIM-003` exists.
- **Setting has no aggregation step.** *Where the characters are* is a primitive world fact
  with an existing architectural home — `ARCHITECTURE.md` §6 **Dungeon State** (*rooms/areas*)
  and **Campaign State**. Nothing derives it; it is simply supplied, exactly as RC assumes
  (*"the DM first needs to know where the characters are"*).
- Per the `SIM-003` precedent, **a fact having no Rule Card is not a defect**, and no
  artificial ownership gap is recorded for one.

> **Recorded, not assigned.** If a later task wants a rule that disambiguates the over-ocean
> aerial case (§8 case C) rather than leaving it caller-supplied, that is a **Setting-selection**
> question. It would **not** belong to `SIM-003`, and it is not assigned to anything here.

### 12. Future `ENC-001` contract consequence

Narrow, consequence only — nothing designed, nothing implemented:

- `ENC-001` takes `setting` as a **caller-supplied RC-native Setting** and validates it,
  exactly as it does `visibility` (`Q-3`, `Q-7`). It does **not** derive Setting, and it does
  **not** become a spatial or environment classifier.
- The Setting domain is exactly the four printed values:

```text
Dungeon*  |  Wilderness  |  Ocean/sea  |  Undersea

"City" is treated just like any other wilderness terrain (RC p. 93).
AERIAL IS NOT A MEMBER of this domain and must not be added to it.
```

- If no supported Setting can be established, `ENC-001` **refuses** — the same shape as the
  missing-visibility case, and for the same reason: RC supplies no default, so a simulator that
  must not guess can only refuse. Note that `Q-9` itself produces **no** new refusal case;
  aerial encounters resolve to a printed Setting.

### 13. Residue

- **The over-ocean aerial Setting is not explicitly stated by RC for distance purposes**
  (§8 case C). Recorded as an unresolved dependency, shown to have no mechanical consequence,
  and deliberately **not** closed by a ruling.
- **`Q-4` remains open** (whose infravision satisfies the p. 93 `**` footnote), carried by
  `SIM-003`.
- **Daylight/time-of-day and weather determination remain unowned**, as `SIM-003` records.
- **The feet/yards convention remains unowned and is untouched here** — though `Q-9` touches
  the same rows, every aerial case above lands on a **yards** row, which changes nothing about
  who owns the convention.
- **No Setting-selection owner is created**, per §11.

---

## Feet/yards — the unit convention and who owns it

### 1. The gap as the accepted record states it

Two separate records, quoted as written:

> **Ownership gap** (accepted Stage-A packet §10): `Feet/yards unit convention` —
> *"RC Ch. 6 p. 87 — **no Rule ID claims it**"* — *"consumed here; recorded as a potential
> completion question, not assigned."*

> **Source tension** (accepted Stage-A packet `Q-6`): *"Undersea distance is in yards (p. 93)
> while p. 115 reads undersea ranges 'in feet at all times' — **possibly distinct concepts**"*
> — pp. 93, 115 — `RETAINED AS GENUINE SOURCE AMBIGUITY`.

Both match the expected subject. Note the packet's own hedge — *possibly distinct concepts* —
which §4 below tests rather than assumes.

### 2. Source basis — re-inspected this pass

| Page | Re-inspected | Supplies |
|---|---|---|
| p. 87 | **yes, page image this pass** | `Feet vs. Yards`; the `Movement, Missile, and Spell Ranges` sidebar |
| p. 93 | yes (`Q-3` pass, magnified crop) | the Encounter Distances Table's printed units |
| p. 115 | **yes, page image this pass** | `Underwater Combat` — the sentence `E-25` paraphrases |

No whole-book units search. `E-25` was a paraphrase, so it was verified on the image rather
than relied on — which turned out to matter (§4).

### 3. p. 87 — the rules fact, and a feature the packet's transcription did not carry

```text
p. 87  "Feet vs. Yards"
"In dungeons and other indoor settings, the basic unit of distance measurement
is the foot. ... In wildernesses, open fields, open city streets, and other
outdoor settings, the basic unit of distance measurement is the yard. (One yard
equals three feet.)"

"Missiles and spell ranges are also read as feet in dungeons and as yards in
the wilderness. However, the area affected by a spell ... is not read as yards;
it is always read as feet."

p. 87  sidebar "Movement, Missile, and Spell Ranges"
"Indoors: ... measured in feet (90' means ninety feet indoors)."
"Outdoors: ... measured in yards (120' actually means 120 yards outdoors)."
"Everywhere: Spell effects are always measured in feet."
```

**A notation convention, not only a unit-selection rule.** *"120' actually means 120 yards
outdoors"*: the glyph `'` is **scale-relative**, and the *same printed numeral* denotes feet
indoors and yards outdoors.

**Two scope limits on this observation, stated so it is not made to carry more than it does:**

- The notation statement sits in a sidebar headed *"Movement, Missile, and Spell **Ranges**"*.
  Encounter distance is none of those three. The broader *"basic unit of distance
  measurement"* sentence does cover distance generally, but what it establishes is **unit
  selection**, not the scale-relative glyph.
- **RC's encounter-distance material never leaves the unit ambiguous.** §5 shows p. 93 prints
  the unit on every row and p. 92 disambiguates the surprise path inline. So this notation
  feature is *not* the reason `ENC-001`'s result must carry a unit — see §9, which gives the
  actual reason.

### 4. p. 115 — the tension dissolves, and `E-25`'s paraphrase understated why

The sentence, read on the page image, with its headings:

```text
p. 115   Chapter 8: Combat  ->  Underwater Combat  ->  Missile Weapons

"Missile Weapons: Most missile weapons do not work underwater. Only crossbows
made by undersea dwellers (such as mermen) will function. Even with those
crossbows, read all undersea ranges in feet at all times."
```

**Classification: different procedural domain.** Not a contradiction, not an exception, not an
unresolved tension — and this is established by position and subject, not by preference:

- it sits under **`Missile Weapons`**, inside **`Underwater Combat`**, inside **Chapter 8:
  Combat**;
- its subject is the **range of a crossbow** — *"Even with those crossbows"* — i.e. a missile
  range;
- it is the undersea counterpart of p. 87's general rule that *"Missiles and spell **ranges**
  are also read as feet in dungeons and as yards in the wilderness."* p. 115 says: undersea,
  do not apply the outdoor/yards reading to missile ranges; read them in feet always.

**Encounter distance is not a missile range.** The Encounter Distances Table's `Undersea` row
(`1d6 x 10 yards`) is Chapter 7 material governing how far apart two groups are at contact.
p. 115 governs how far a crossbow bolt carries underwater. **The narrower claim actually
established:** the `ENC-001` procedure never consults a missile range, and p. 115 never
supplies an encounter distance — so neither is an input to the other. (A *comparison* between
the two can still arise in play — an undersea encounter at a distance in yards against a
merman crossbow's range in feet — which is `COMBAT-*`'s to handle and is recorded in §12.)

**The dissolution also survives the broadest reading of p. 115.** Even if *"all undersea
ranges in feet at all times"* were read as overriding the p. 87 outdoor convention generally,
the p. 93 `Undersea` row would still be unaffected: that row **does not use the notation at
all** — it spells out `1d6 x 10 **yards**`. p. 115 can only change how a `'` glyph is read,
and p. 93 prints no `'` on any undersea row. The conflict therefore dissolves under both the
narrow and the broad reading, which is why the conclusion does not rest on the scoping
argument alone.

> **What this does and does not settle.** For `ENC-001` the apparent conflict **does not
> arise**, and the accepted packet's own hedge — *possibly distinct concepts* — is confirmed
> as correct by inspection rather than assumed. Whether `COMBAT-*` has any residual question
> about undersea missile ranges is **`COMBAT-*`'s, not `ENC-001`'s**, and is not decided here.
> The accepted packet is not modified; `Q-6`'s Stage-A disposition stands as the Stage-A
> record.

### 5. p. 93 — the table has already applied the convention

The decisive observation about table application:

| Setting | How the table prints the unit |
|---|---|
| `Dungeon*` | `4d6x 10'` / `2d6x 10'` / `1d4x 10'` — the foot mark |
| `Wilderness` | `4d6 x 10 yards` / `2d6 x 10 yards` / `1d4 x 10 yards` — **the word spelled out** |
| `Ocean/sea` | `300 yards`, `4d6 x 10 yards`, `120 yards`, … — **spelled out** |
| `Undersea` | `1d6 x 10 yards` — **spelled out** |

**The Encounter Distances Table does not rely on the p. 87 notation convention.** It never
prints a bare `'` outdoors and expects the reader to convert; it spells `yards` out on every
outdoor row. p. 87 supplies the general convention, and **p. 93 has already applied it and
printed the result**. No row departs from it.

So for the table path there is no conversion left to perform, and no unit left to select —
only a unit to **carry**.

**The one place `ENC-001` meets the raw notation convention is the surprise short-circuit**,
and RC disambiguates it inline there too:

```text
p. 92  "the encounter distance is 1d4 x 10' (or yards if outdoors)"
p. 92  "the unsurprised party notices the surprised party at the 1d4 X 10'
        (or yards) distance rolled"
```

The indoor/outdoor split that governs it is already available to `ENC-001`: the table's
footnote `*` reads *"Or other indoor setting"* on `Dungeon`, and p. 87 names *"wildernesses,
open fields, open city streets, and other outdoor settings"* as the outdoor case. So
`Dungeon*` is the indoor Setting and `Wilderness`, `Ocean/sea` and `Undersea` are outdoor —
a function of the Setting `ENC-001` already consumes and validates (`Q-9`).

### 6. Repository ownership search

Architecture inspection of `INVENTORY.md`, `ARCHITECTURE.md`, the `SIM-*` specifications and
the landed modules in `src/`.

**No artifact owns *distance* units, the feet/yards convention or measurement
representation.** The three landed cards that express distances each state the unit of their
own output:

| Artifact | How it handles the convention | Scope |
|---|---|---|
| `EXP-003` Dungeon Movement | cites p. 87 `Feet vs. Yards` and states *"The distance unit. Indoors, **feet**"*; rates are feet per turn | **card-local**, indoor half only |
| `CHAR-005` Encumbrance & Movement | a landed `Setting` enum, `INDOORS = "feet"` / `OUTDOORS = "yards"`, with a `.unit` property, documented as *"only the unit they are read in does"* change | **card-local**, its own movement rates |
| `CHAR-004` equipment | carries the unit in the name — `dimension_feet`, `side_feet` | card-local |

**That is not, however, the only pattern this repository has, and it must not be presented as
one.** The repository **does** support small **shared primitives owned by no single Rule
Card**, and has landed three of them:

| Shared primitive | What it owns | Stated basis |
|---|---|---|
| `src/rules/currency.py` | exact monetary values in RC coin — *"owned by no single Rule Card… carrying representation and nothing else"*; includes RC's conversion ratios `1 pp = 5 gp = 10 ep = 50 sp = 500 cp` | *"Each owns **different data expressed in** money, so **none may own the representation itself**"* |
| `src/rules/character_creation/character_class.py` | the nine character-class identities | same pattern, cited by `currency.py` as its precedent |
| `src/rules/exploration/turn_credit.py` | the `EXP-002` → `EXP-001` turn-credit value types | same pattern, cited by `currency.py` as its precedent |

**This pattern is a small shared primitive, not a "units framework"**, and it must not be
dismissed as one. `currency.py` is precisely a *measurement* representation with conversion
ratios, so the existence of a measurement domain is not by itself a reason to avoid it.

**The repository's own documented decision test** (`docs/technical/CLUSTER-003_IMPLEMENTATION_PLAN.md`
§10, the `currency.Coin` row) is:

```text
Could CHAR-004 own it?  No. TREAS-*/ADV-003 will need the same type.
                        character_class.py precedent.
```

That test — *could one card own it, or will other named cards need the same type?* — is
applied honestly to this case in §7, Model B.

> **A collision worth flagging before an implementer meets it.** `CHAR-005` already has a type
> named `Setting` with **two** members, `INDOORS = "feet"` / `OUTDOORS = "yards"`, and a
> `.unit` property. `ENC-001`'s `Setting` axis has **four**
> (`Dungeon*`/`Wilderness`/`Ocean/sea`/`Undersea`). **Same word, different concepts.**
>
> **Why the reuse is tempting, stated so the trap is visible:** `ENC-001`'s four Settings
> collapse 4 → 2 onto `INDOORS`/`OUTDOORS` **for unit purposes exactly** — `Dungeon*` is
> indoor, the other three outdoor — which makes `CHAR-005.Setting` look like a ready-made unit
> selector for `ENC-001`. It is not. `CHAR-005`'s is a **reading-mode for movement rates**,
> whose own docstring says *"a rate of 90 is a rate of 90 either way"* and which is why
> `movement_rate` takes no setting; `ENC-001`'s is a **table-lookup axis that selects a row**,
> where `Wilderness` and `Ocean/sea` are different rows with different values. The 4 → 2
> collapse is true of the *unit* and false of the *lookup*, so reusing the type would silently
> lose the distinction `ENC-001` depends on. They must not be conflated or reused for one
> another. Recorded as an implementation hazard, not resolved here — no type is designed and
> nothing is renamed.

### 7. Competing ownership models

**Model A — `ENC-001` owns unit *selection*.** *Adopted in corrected form.* The label is
slightly wrong: there is nothing to **select**. Both of `ENC-001`'s output paths carry a unit
RC has already stated — the table row (§5) or p. 92's inline *"(or yards if outdoors)"*. What
`ENC-001` does is **carry** that unit out with the magnitude. That is not scope inflation; a
distance returned without its unit is an **incomplete result**, not a leaner one.

**Model B — a small shared primitive owns the representation.** *Not required here — but it is
a legitimate architectural option, not an absurd one, and it is rejected on responsibility
rather than on principle.*

The choice is between two patterns the repository actually has:

| | Card-local typed output (Model A) | Small shared primitive (Model B) |
|---|---|---|
| Shape | `ENC-001` carries the unit its governing table/prose already specifies | a module owned by no single card, carrying representation and nothing else |
| Precedent | `EXP-003`, `CHAR-005`, `CHAR-004` | `currency.py`, `character_class.py`, `turn_credit.py` |
| Trigger | one card's own result | *"Could one card own it? No — other named cards will need the same type"* |

**Applying the documented trigger honestly.** `currency.py` exists because `CHAR-004` *could
not* own `Coin`: `TREAS-*` and `ADV-003` were **named** as needing the same type, and the
cards each own *different data expressed in* money while needing the representation to behave
— exact arithmetic and scaling, with a real defect (the Druid surcharge) if precision were
lost. Neither limb of that is met for encounter distance:

1. **No other card needs the same type.** `ENC-001` is the only consumer. The three landed
   distance-bearing cards are already implemented and need no change: `EXP-003` is indoors-only
   feet, `CHAR-004`'s are named ints, and `CHAR-005` pairs a *movement rate* with a label —
   not an encounter distance. None is positioned as a second consumer the way `TREAS-*` was.
2. **There is no shared *behaviour* to own.** This is the substantive reason, and it is about
   responsibility, not convenience. `ENC-001` **does not convert** feet to yards or yards to
   feet, **does not normalize** measurements, **does not perform dimensional arithmetic**, and
   **needs no reusable unit-operation API**. Its governing table and prose already determine
   the unit of its own result (§5), and the result merely preserves the magnitude/unit pair RC
   supplied. A primitive carrying an inert label with no operations is not the `currency.py`
   case; `Coin` exists for arithmetic that had to be exact.

**A source-grounded reason to be positively cautious about a shared *unit-selection*
primitive.** This very adjudication establishes (§4) that **different distance-bearing
mechanics in RC follow different unit rules**: undersea *missile ranges* are read in feet at
all times (p. 115) while the undersea *encounter distance* is in yards (p. 93). A shared type
that assumed one unit rule across distance-bearing mechanics would therefore be **wrong on
current evidence**, not merely premature.

**Not foreclosed.** If a later card — `ENC-005`'s pursuit distances or `COMBAT-*`'s missile
ranges are the plausible candidates — genuinely needs the same `(magnitude, unit)`
representation, then `currency.py` is **the precedent to follow**, and this adjudication does
not stand in the way. What it declines to do is create that primitive speculatively for a
single consumer.

`CHAR-005`'s enum stays **card-local** and is not promoted into a shared owner by this task.

**Model C — caller/context owns units.** *Rejected.* It separates a printed RC rule from the
mechanic that uses it, and it discards a unit RC had already supplied: `30` handed to the
caller is indistinguishable between 30 feet and 30 yards, with a factor-of-three error as the
failure mode.

**Model D — the table output owns the unit intrinsically.** *Correct, and merged into A — but
incomplete on its own.* The table does define magnitude **and** unit per row. It does not
cover the **surprise short-circuit**, which is p. 92 prose rather than a table row, so "the
table owns it" leaves part of `ENC-001`'s output unaccounted for. A together with D covers
both paths.

### 8. Adjudication — not an ownership problem

**Feet/yards is not a rule-ownership problem. It is part of `ENC-001`'s typed output.**

The ownership gap recorded in the accepted packet is **closed by finding that no separate
owner is required**, not by assigning one:

```text
NO NEW OWNER REQUIRED, AND NONE CREATED

ENC-001 returns a distance together with its RC-prescribed unit. The unit is
not independently derived world state -- it is a property of the result,
stated by RC at the point the result is produced.
```

Adjudicated at steps 1–3 of the order; step 4 is **not reached**:

```text
1. RC Explicit ............... p. 87 states the convention; p. 93 has already
                               applied it and prints the unit on every row;
                               p. 92 states it inline for the surprise path
2. Necessary Consequence ..... ENC-001 never derives a unit. It carries the
                               one RC states, keyed to a Setting it already
                               consumes and validates
3. Architecture / output
   contract ................. ENC-001's result carries magnitude AND unit,
                               matching the established card-local pattern
4. Narrow Simulator Ruling ... NOT REACHED
```

```text
NO NEW SIMULATOR RULING

No contradiction affecting ENC-001 is present in the inspected governing
material -- pp. 87, 92, 93 and 115. p. 87 and p. 93 agree, and p. 115's
appearance of conflict dissolves into a different procedural domain.

SCOPE: no whole-book units search was performed, so this is NOT an RC-wide
claim that no contradiction exists anywhere in RC. It is a claim about the
material actually inspected, which is the material that governs ENC-001.

An SR must not be created to choose a software representation, and nothing
in the inspected material requires an RC-unsupported choice. SR-13 remains
the next free identifier and is not used here.
```

### 9. Future `ENC-001` output-representation consequence

Narrow, consequence only — **nothing designed, no units library, no implementation**:

- `ENC-001`'s result should carry **magnitude *and* unit** together.

  **The reason, stated with the right provenance.** The *source facts* are RC's: RC supplies a
  unit (p. 93 prints it on every row; p. 92 states it inline for the surprise path), and p. 87
  explains the contextual notation behind it. The *consequence* is the simulator's, not RC's:
  because RC supplies the unit, and because that unit differs between `Dungeon*` (feet) and
  the other three Settings (yards), **discarding it and returning only the magnitude would
  make the simulator's own representation incomplete** — a bare `30` would lose information RC
  had already supplied, with a factor-of-three error as the failure mode.

  This is a **Necessary Consequence / Repository Architecture** decision. It is **not** an
  RC-prescribed data structure, and RC is not claimed to dictate it — consistent with §10.
- The unit is `feet` for `Dungeon*` and `yards` for `Wilderness`, `Ocean/sea` and `Undersea`,
  on both the table path and the surprise path.
- This follows the same shape the three landed distance-bearing cards use for their own
  outputs (`CHAR-005`'s `.unit`, `EXP-003`'s stated unit, `CHAR-004`'s unit-bearing names) —
  **one option among the repository's patterns, not the only one it has** (§6, §7 Model B).
  **No units library is proposed**, no conversion is proposed, and `feet ↔ yards` arithmetic
  is not part of this.
- `ENC-001` must not reuse `CHAR-005`'s two-valued `Setting` for its four-valued axis (§6).

### 10. Provenance classification

| Conclusion | Classification |
|---|---|
| p. 87's `Feet vs. Yards` convention, including `"120' actually means 120 yards outdoors"` | **Rules Cyclopedia Explicit** — page image |
| p. 93 prints `'` on `Dungeon` rows and spells `yards` on every outdoor row; no row departs | **Rules Cyclopedia Explicit** — page image |
| p. 92 states the unit inline for the surprise path | **Rules Cyclopedia Explicit** |
| p. 115 governs undersea **missile ranges** in combat, not encounter distance | **Rules Cyclopedia Explicit** — different procedural domain, established by heading and subject |
| `ENC-001` never derives a unit; it carries the RC-stated one | **Necessary Consequence** |
| `ENC-001`'s result carries magnitude **and** unit, because discarding a unit RC supplied would leave the simulator's representation incomplete | **Necessary Consequence / Repository Architecture** — **not** an RC-prescribed data structure |
| No separate software owner is required for this mechanic, and the shared-primitive trigger is not met today | **Repository Boundary / Architecture** |
| Whether `COMBAT-*` has a residual undersea missile-range question | **Unresolved Source Tension** — `COMBAT-*`'s, not `ENC-001`'s |
| Any unit conversion, units framework or representation rule | **none issued** — no Simulator Ruling |

**Three things kept distinct, and they must not be conflated:**

```text
RC RULE PROVENANCE        RC owns the feet/yards convention as a rule, and
                          supplies the unit for each ENC-001 output path.

REPOSITORY OWNERSHIP      No separate software owner is necessary for THIS
                          mechanic. That is a statement about ENC-001, not a
                          repository-wide policy that measurement units are
                          always card-local.

SOFTWARE REPRESENTATION   ENC-001 owns the complete representation of its own
                          result. This is an architecture decision; RC does
                          not prescribe a data structure.
```

**No representation choice above is labelled an RC rule.**

### 11. `Q-9` and `SIM-003` — both untouched

- **`Q-9` is not reopened.** `Aerial` remains not a Setting. That aerial cases land on
  yards-based Settings is a **consequence** of the Setting mapping, and it played no part in
  deciding ownership here.
- **`SIM-003` is unchanged.** It owns visibility classification only; its specification
  already lists `feet/yards conversion` and measurement representation among its explicit
  non-responsibilities, and that boundary is preserved. Nothing here gives it distance units.

### 12. Residue

- **Undersea missile ranges** (p. 115) may still pose a question for `COMBAT-*`, including the
  cross-domain comparison noted in §4. Recorded, routed, **not** adjudicated — and it is not
  an input to `ENC-001`.
- **The `Setting` name collision** between `CHAR-005` (two-valued) and `ENC-001` (four-valued)
  is an implementation hazard, recorded for whoever implements `ENC-001` (§6).
- **No owner of *distance* units exists**, and this adjudication deliberately does not create
  one. **This does not establish a repository-wide policy that measurement units are always
  card-local** — the shared-primitive pattern (`currency.py` and its precedents) remains
  available, and §7 Model B states the conditions under which a later card should use it.

> **Reading this alongside `SIM-003`.** `SIM-003`'s specification lists *"feet/yards
> conversion or convention — still unowned"* among its non-responsibilities, and that remains
> accurate: **unit conversion genuinely has no owner**, because nothing in the project converts
> between feet and yards. That is **not** in tension with the closure here. This adjudication
> settles only that `ENC-001`'s *own result* carries the unit RC supplies for it; it does not
> claim an owner for conversion, and it does not give one to `SIM-003`. `SIM-003` is unchanged.

---

## `ENC-001` Stage-B completion assessment

**Assessment only — nothing below is adjudicated**, and no question is settled by appearing in
this table.

```text
BLOCKING FOR AN ENC-001 RULE CARD:    none for the contract itself
ON ENC-001's DISTANCE PATH:           one unowned item (Q-4)
EXTERNAL, ALSO UNOWNED:               SIM-003's daylight and weather inputs
```

| Item | Status | Blocking? |
|---|---|---|
| `Q-1` two `2d6 × 10'` procedures | **SETTLED** — `SR-12` approved | no |
| `Q-3` `Very good light` vs `Clear daylight` | **SETTLED** | no |
| `Q-7` who determines visibility | **SETTLED** — `SIM-003` owns classification | no |
| `Q-9` `aerial` and the Setting axis | **SETTLED** | no |
| **feet/yards** | **SETTLED** — part of `ENC-001`'s typed output | no |
| `Q-6` undersea feet/yards | **Resolved as it bears on `ENC-001`** — different procedural domain | no |
| `Q-2` (two parts: table-instance *and* mutual vs asymmetric notice) | first part **settled by `SR-12`** — distance is determined once by pp. 92–93; only the notice half survives, as residue under `Q-1` §7 | **no** — the surviving half concerns *awareness description*, not the distance produced |
| `Q-5` infravision `60'` vs a `20'–120'` roll | retained — **not assessed on fresh source this pass**; p. 24 was not re-inspected | **not blocking on the evidence in hand:** the accepted packet records no RC capping or re-roll rule, so producing the rolled value is the only option that invents nothing. **Whether awareness obtains at that distance is left open** and is not this card's output. Not adjudicated |
| `Q-8` p. 98 word order | retained | **no** — on the accepted packet's own §9 cross-reference ledger: *"p. 98 states **no procedure of its own**; it defers to pp. 91–93"* (`ENC-001-evidence.md` §9). p. 98 was **not** re-inspected this pass |
| **`Q-4` whose infravision satisfies footnote `**`** | retained; carried as `SIM-003` open dependency 1 | **the one unowned item on `ENC-001`'s distance path** — see below |
| `SIM-003` unowned daylight/weather inputs | external, **also unowned** | **no** for the `ENC-001` contract — they are inputs to `SIM-003`, not to `ENC-001` — but they are **not closed**, and are scenario-supplied today |

**The distinction that matters, stated plainly.** `ENC-001`'s **contract** is complete: a
Setting and a visibility label in, a distance with its unit out, refusal when a required input
is absent. Nothing above blocks writing that.

**End-to-end determinism is not complete**, for one case: full darkness **with infravision
used**, where the p. 93 footnote `**` promotes `No light` to `Dim light`. `SIM-003` explicitly
excludes infravision, and `ENC-001` consumes a supplied label — so **no component currently
owns applying that footnote**. That is `Q-4`, it is a classification-side question rather than
`ENC-001`'s to resolve, and it is **not adjudicated here**.

A Rule Card could be written for `ENC-001` today with that case routed out explicitly rather
than silently defaulted. Whether to do so is a human decision and is not taken here.
