# `ENC-001` — Encounter Distance — Stage-B Adjudications

> **Scope of this document.** It records Stage-B adjudications of questions left open and
> retained by the accepted `ENC-001` Stage-A evidence packet
> (`docs/rules/evidence/ENC-001-evidence.md`, Stage A `ACCEPTED` 2026-10-04 under
> `DEC-0013`). It is **not** the Rule Card, and it does not authorize implementation.
>
> **Only `Q-1` is adjudicated here.** `Q-3`, `Q-7` and `Q-9` remain `RETAINED AS GENUINE
> SOURCE AMBIGUITY` exactly as the accepted packet records them, and the two ownership
> gaps — the world **visibility category** (`NO RULE ID EXISTS`) and the **feet/yards**
> convention — remain open and unassigned. Nothing below decides any of them.

```text
ADJUDICATION-STATUS
RULE-ID:   ENC-001
Q-1:       ADJUDICATED 2026-10-04; SR-12 APPROVED 2026-10-04
Q-3:       OPEN -- not adjudicated (see the scope note below)
Q-7:       OPEN -- not adjudicated here
Q-9:       OPEN -- not adjudicated here
STAGE B:   adjudication only; no Rule Card, no implementation
```

> **Scope note, 2026-10-04 — why `Q-3` is still open.** A task authorized adjudicating
> `Q-3` and described it as the *"normal dungeon conditions" vs `Dim light`* question,
> whose resolution would turn on caller-supplied world-visibility state. The accepted
> Stage-A packet's `Q-3` is a **different question** — whether the Dungeon row's
> `Very good light` is the same condition as the Wilderness/Ocean rows' `Clear daylight`.
> The question described is split across `Q-1` (already adjudicated, `SR-12`) and `Q-7`
> (not authorized). Adjudicating under the mismatched label would have decided `Q-7` while
> calling it `Q-3`, so the discrepancy was reported instead. `Q-3` is untouched.

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
