# `ENC-001` — Encounter Distance — Stage-B Adjudications

> **Scope of this document.** It records Stage-B adjudications of questions left open and
> retained by the accepted `ENC-001` Stage-A evidence packet
> (`docs/rules/evidence/ENC-001-evidence.md`, Stage A `ACCEPTED` 2026-10-04 under
> `DEC-0013`). It is **not** the Rule Card, and it does not authorize implementation.
>
> **`Q-1`, `Q-3` and `Q-7` are adjudicated here** — `Q-7` only in its rules/contract portion,
> by human architecture decision. **The world/environment visibility *owner* is still not
> assigned**, and saying so is not a formality: the gap is real and a separate architecture
> decision closes it. `Q-9` remains `RETAINED AS GENUINE SOURCE AMBIGUITY` exactly as the
> accepted packet records it, and the **feet/yards** convention remains unassigned. Nothing
> below assigns either.

```text
ADJUDICATION-STATUS
RULE-ID:   ENC-001
Q-1:       ADJUDICATED 2026-10-04; SR-12 APPROVED 2026-10-04
Q-3:       ADJUDICATED 2026-10-04; NO NEW SIMULATOR RULING
Q-7:       rules/contract portion SETTLED 2026-10-04 by human architecture decision
           world/environment visibility OWNER: NOT YET ASSIGNED
Q-9:       OPEN -- not adjudicated here
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
             visibility OWNER          NOT YET ASSIGNED
                                       separate architecture decision required

The ownership gap is NOT closed. What is settled is what ENC-001 does about
it: it consumes a supplied label and refuses when a required one is absent.
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
| The **world/environment visibility owner** — *what component produces that label?* | **NOT YET ASSIGNED** |

```text
WORLD/ENVIRONMENT VISIBILITY OWNER:
NEW OWNERSHIP DECISION REQUIRED
```

**The ownership gap itself is not closed, and this document does not claim it is.** No Rule
ID is created, no `SIM-*` specification is created, `INVENTORY.md` is not edited to invent an
owner, and ownership is assigned to no existing card — not `SIM-001`, not `EXP-006`, not
`ENC-001`. Whether the owner should be a small `SIM-*` specification or another architecture
form is a separate decision, deliberately left to a later task.

What the decision *does* achieve is that `ENC-001`'s own contract no longer waits on it:
`ENC-001` can be specified against a supplied input, and the unassigned producer is a
dependency rather than a blocker.

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

- **The world/environment visibility owner is still unassigned.** This is the live residue.
  `ENC-001`'s contract no longer waits on it, but nothing produces the label yet, so a
  deterministic end-to-end encounter still cannot be run. `NEW OWNERSHIP DECISION REQUIRED`.
- **Daylight/time-of-day and weather have no owner either** — a gap wider than `Q-7`, surfaced
  by section 5 and not resolved here. Whoever takes world visibility will meet these.
- **The form of the eventual owner is undecided** — a small `SIM-*` specification or another
  architecture form. Deliberately left to the next task; nothing here prejudges it beyond the
  observation in section 9 that `SIM-001` is precedent and not a fit.
- **`EXP-006` §7 vs §B is resolved** — the human chose §B and §7 was corrected to match. No
  residue remains on that point.
- **A minor provenance inaccuracy in the accepted packet, reported not fixed.** Its §10 basis
  row quotes `EXP-006`'s module as *"Not a statement about the world"*. The module's actual
  words are *"It owns nothing about the world"* and *"never a fact about the world"*. The
  substance is identical and the routing conclusion is unaffected; the quotation marks are
  inexact. The accepted packet is **not** modified — it is accepted evidence.
- **`Q-9` and the feet/yards gap are untouched.**
