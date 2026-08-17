# Stage-A Evidence: EXP-001 — Dungeon Wandering-Monster Check

> **This is a Stage-A evidence artifact, not a Rule Card.** Produced under `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` (`DEC-0009-evidence-first-rule-research-protocol.md`). It is not mechanically authoritative, is not `APPROVED`, and is not permission to implement anything. `EXP-001` remains `REVALIDATION_REQUIRED`; `docs/rules/exploration/dungeon_wandering_monster_check.md` was not read or modified during this task.

## 1. Research Scope

**Investigating:** the Rules Cyclopedia procedure responsible for determining whether a wandering/random dungeon encounter is triggered as dungeon exploration proceeds — cadence, die/result, procedural timing relative to the Game Turn Checklist, trigger-vs-appearance distinction, interaction with encounter/round-mode (the interface question explicitly deferred by the now-`APPROVED` `EXP-002`), multi-turn-activity implications, and any RC-stated modifiers/exceptions.

**Explicitly excluded from this task:**
- Rewriting or revalidating `EXP-001`'s Rule Card (Stage B, not begun).
- Detailed comparison against, or use of, the superseded 1974-primary `EXP-001` card as a research checklist.
- Alternate-source (BECMI/B-X/Holmes/OD&D) research — Stage A is RC-only.
- Monster determination (which monster appears — `MON-001`), encounter distance, surprise, or reaction procedures in their own mechanical detail — noted only where they mark this responsibility's boundary.
- Resolving the previously-flagged `MON-001` ↔ `EXP-008` dependency-direction issue.
- Any Simulator Ruling proposal.
- Any production code or test change.

## 2. Primary-Source Access

**Source:** *Dungeons & Dragons Rules Cyclopedia* (Allston, Aaron, ed. TSR, 1991), full OCR transcription, `archive.org/stream/TSR1071TheDDRulesCyclopedia/TSR-1071-The-DD-Rules-Cyclopedia_djvu.txt` — the same primary-text representation successfully used for `EXP-002`'s research.

**Access method:** the full transcription (1,937,418 characters) was loaded directly in-browser and searched via the loaded page's own full text (in-page string search), not a truncated or summarized fetch. This is the method that succeeded for `EXP-002` after earlier `WebFetch`-based attempts failed on this same source.

**Inspectability confirmed:** surrounding paragraphs, full procedure/checklist text, table headings and rows, internal page cross-references (e.g., "on page 93," independently checked against the Table of Contents), and DM-guidance prose were all directly readable and were read in full for every location cited below — not sampled as isolated snippets.

**A methodological finding, recorded for future Stage-A tasks using this same source:** naive exact-substring search can miss OCR-line-wrapped phrases. The Game Turn Checklist's own text reads "The DM rolls ld6 every \nother turn" — a literal newline is inserted by the OCR between "every" and "other" — so a search for the unbroken string `"every other turn"` returns **zero** hits despite the phrase being present and readable in context. All quotations below were verified by reading full surrounding context, not by trusting a single substring match.

No access failure occurred. `STOP — PRIMARY SOURCE ACCESS REQUIRED` was not triggered.

## 3. Research Questions Investigated

A. Trigger cadence — how often, measured in what unit, from what reference point.
B. Check roll — which die, which result triggers, dungeon vs. other environments.
C. Timing within the Game Turn procedure — where the check sits relative to turn start/actions/results/turn end and arrival of a previously-triggered encounter.
D. Trigger vs. appearance — same instant, or distinct procedural moments.
E. Interaction with encounter/round-mode — the principal interface question deferred by `EXP-002`.
F. Multi-turn activities — how many check opportunities occur.
G. Modifiers/exceptions — dungeon level, environment, noise, special activity, party behavior, cleared areas, DM discretion.
Plus: responsibility boundary against `EXP-002`, `MON-001`, `ENC-*`, `EXP-008`.

## 4. Evidence Map

| Question | RC Location | Evidence Summary | Provenance | Confidence |
|---|---|---|---|---|
| A. Cadence unit/frequency | Ch. 7 p. 91, Game Turn Checklist step 4; Ch. 7 p. 93, "Wandering Monster Encounters" ("Wandering Monsters Check" subsection) | Two independent passages agree: the check is made **once every two turns**, not every turn. Checklist step 4: "The DM rolls 1d6 every other turn to check for this." Subsection: "Every two turns (not every turn), the DM rolls 1d6 to check for wandering monsters or random encounters." | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (two independent passages, verbatim-consistent) |
| A. Reference point for cadence | Ch. 7 p. 91, Game Turn Checklist (the check is step 4 of each iteration) | Under ordinary turn-mode exploration, the wandering-monster check is step 4 of the Game Turn Checklist and occurs every two game turns. RC does not independently establish whether encounter-credited turns, during which normal Game-Turn-Checklist execution is suspended, participate in that two-turn cadence — see row E below. | Rules Cyclopedia Explicit (ordinary turn-mode cadence only) | DIRECT PRIMARY TEXT |
| B. Check die and trigger result (dungeon) | Ch. 7 p. 91, Game Turn Checklist step 4 | "1d6... If this is a dungeon and a '1' comes up on the die, the PCs will encounter wandering monsters..." — 1-in-6, triggers on a **1** (not a 6). | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| B. Trigger result differs by environment | Ch. 7 p. 91–92, Chance of Encounter Table | "Dungeon and city": 1d6 every two turns + 1d12 once at night, "on a 1." "Wilderness": 1d6 by day + 1d12 at night, terrain-dependent range (1; 1–2; 1–3) rather than a flat "1." Dungeon and city share the same roll method/trigger; wilderness differs. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| C. Where the check sits in the procedure | Ch. 7 p. 91, Game Turn Checklist (all 4 steps) | The checklist is: (1) resolve arrival of any previously-triggered wandering monster [if positive, leave the checklist entirely for the Encounter Checklist], (2) Actions, (3) Results [may also exit to Encounter Checklist if an encounter arises from Actions/Results], (4) Wandering Monsters Check [the roll itself]. The check-roll is procedurally the **last** step of an iteration; a resulting arrival is resolved at step **1** of the **next** iteration. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| D. Trigger vs. appearance — same instant or distinct | Ch. 7 p. 91, Game Turn Checklist step 1 and step 4; "Wandering Monster Encounters" subsection | Explicitly distinct procedural instants, but not separated by an intervening full turn: a positive check at the end of turn N schedules arrival at the beginning of turn N+1, with no Game-Turn-Checklist iteration occurring between them. Step 4: a positive roll means monsters "will encounter... at the beginning of the next turn," not now. Step 1 of the following iteration: "If the wandering monsters check at the end of the previous turn was positive, the monsters arrive now." Subsection restates: "When a DM's roll indicates that wandering monsters will appear, they appear the following turn." | Rules Cyclopedia Explicit | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (three independent, mutually consistent statements) |
| D. What "arrival" means mechanically | "Wandering Monster Encounters" subsection | On arrival, distance is rolled (2d6×10 feet) and the DM "should switch to the Encounter Checklist (on page 93)" — arrival is itself the trigger into round-mode. | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| E. Does the wandering-monster check ever fire during round-mode (mid-encounter)? | Ch. 7 p. 93, Encounter Checklist step 1 | "Game time switches from 10-minute turns to 10-second rounds" when an encounter begins. The Game Turn Checklist (the only place the wandering-monster check is defined) is a turn-mode procedure; nothing describes it continuing to run, or being separately invoked, during round-mode. | Necessary Mechanical Consequence (of RC Explicit facts: the check is a Game-Turn-Checklist step; Game-Turn-Checklist mode is suspended during an encounter) | NECESSARY CONSEQUENCE |
| E. Does an encounter's credited turn(s) count toward the every-two-turns cadence? | *(no RC location found)* | **Not addressed anywhere located.** Neither the Encounter Checklist's "Encounter Ends: begin play with a new turn" (Ch. 7 p. 93) nor the structurally analogous Game Day Checklist's "Resume Travel" step (Ch. 7 p. 91) states whether resuming turn-mode continues, resets, or otherwise affects the wandering-check cadence counter. | Unresolved by RC | NOT YET VERIFIED — genuinely absent, not merely unsearched (see §7 whole-source pass and §8 falsification) |
| F. Multi-turn activities and check opportunities | Ch. 7 p. 91, Game Turn Checklist (structural) | The checklist is iteration-based: one iteration = one turn = one check opportunity (step 4) at most. `EXP-002`'s own approved contract (a discrete whole-turn credit per ordinary iteration, or `max(1, ceiling(encounter_rounds/60))` credits per resolved encounter) supplies the turn-counting; RC's text for the check itself says nothing beyond "every two [ordinary Game-Turn-Checklist iterations]" (see row A and §9 item 1 for the separate, unresolved question of whether encounter-credited turns count toward this same cadence). No RC statement was found addressing how many check opportunities a multi-turn *non-encounter* activity (e.g., a long rest or search) generates beyond the ordinary one-iteration-at-a-time reading. | Rules Cyclopedia Explicit (structure) / Unresolved by RC (multi-turn-activity opportunity count beyond the ordinary iteration model) | DIRECT PRIMARY TEXT (structure) / NOT YET VERIFIED (multi-turn specifics) |
| G. DM discretion to skip the roll | "Wandering Monster Encounters" subsection, "Important Note" | "If the Dungeon Master has already decided to have a prearranged encounter during this two-turn time period or if he has decided that the characters will have no encounter during this period, he can skip the wandering monster roll." | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| G. Frequency/chance modifiers (noise, battle, cursed items, special areas) | Same subsection, immediately following the Chance-of-Encounter-Table introduction | "Some actions or items may increase the chance of wandering monsters. Loud noises, battles, cursed items, or exploring special areas may allow the DM to check for wandering monsters every turn — and possibly with higher chances" | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT (see §8 falsification for the unresolved "when does this apply relative to a battle's own credited turn(s)" question) |
| G. Dungeon-level modifier to the check itself | Ch. 14 area (Number Appearing text, "level of the dungeon") | Dungeon level modifies **Number Appearing** once a monster is determined (`MON-002`'s territory), not the wandering-monster check's frequency or trigger threshold. No RC text ties dungeon depth to check cadence or trigger result. | Rules Cyclopedia Explicit (for what it does establish) / negative finding for EXP-001's own scope | DIRECT PRIMARY TEXT |
| Chapter/location correction | Table of Contents, p. 1–2 of the transcription | "Dungeon Adventures" is **not** an actual Rules Cyclopedia chapter title (confirms, for `EXP-001`, the same obsolete-label finding already corrected for `EXP-002`'s inventory row). The actual home is **Chapter 7: Encounters and Evasion** (TOC: p. 91), with subsections "Exploration and the Game Turn" (p. 91), "Encounters" (p. 91), "Surprise" (p. 92), "Monster Reactions" (p. 93), "Wandering Monster Encounters" (p. 93). | Rules Cyclopedia Explicit | DIRECT PRIMARY TEXT |
| Cross-reference naming discrepancy | Game Turn Checklist step 1 vs. Table of Contents | The checklist's own text says "See 'Handling Wandering Monsters,' below" — but no heading reading exactly "Handling Wandering Monsters" exists anywhere in the searchable transcription. The Table of Contents shows the actual printed heading is **"Wandering Monster Encounters"** (p. 93). This is very likely the same section under a slightly different name (in-text cross-reference vs. printed heading), not a missing section — its full content (the "Wandering Monsters" / "Wandering Monsters Check" prose, the DM discretion note, and the frequency-modifier note) was located and is fully captured above. Recorded as a minor source-fidelity note, not a gap. | Rules Cyclopedia Explicit (content located); naming discrepancy noted | PRIMARY TEXT + CROSS-REFERENCE CONFIRMED (content), NOT YET VERIFIED (exact reason for the naming mismatch — OCR artifact vs. RC's own internal inconsistency) |

## 5. Governing Procedure (as supported by evidence — not a Rule Card specification)

Dungeon wandering-monster checking is one step of a larger, explicitly sequenced **Game Turn Checklist** (Ch. 7 p. 91), not a freestanding rule stated in isolation:

```text
Each Game-Turn-Checklist iteration (= one dungeon turn, per EXP-002):
  1. Wandering Monsters (arrival):
       IF a check made at the end of the PREVIOUS iteration was positive
       THEN the previously-indicated monsters arrive now (2d6×10' distance)
            and play leaves this checklist for the Encounter Checklist
  2. Actions (party describes what it does this turn)
  3. Results (DM narrates outcomes; an encounter discovered here also
       exits to the Encounter Checklist)
  4. Wandering Monsters Check (the roll itself):
       Every OTHER iteration (i.e., once per two turns), roll 1d6.
       In a dungeon, a result of "1" is positive.
       DM may skip this roll if an encounter/no-encounter has already
       been decided for this two-turn period.
       Certain conditions (loud noise, an ongoing/recent battle, cursed
       items, special areas) may license checking every iteration
       instead, "and possibly with higher chances" (mechanism for the
       "higher chances" not further specified where found).
```

When step 1 or step 3 sends play to the **Encounter Checklist** (Ch. 7 p. 93), dungeon-turn-mode itself is suspended — "Game time switches from 10-minute turns to 10-second rounds" — and the Game Turn Checklist (including its own step 4 check) does not run again until the Encounter Checklist's final step ("Encounter Ends: begin play with a new turn") returns play to turn-mode.

This procedure answers, RC-natively, for **ordinary turn-mode exploration**: *what* triggers a check, *that it occurs every two game turns as step 4 of the Game Turn Checklist*, *what die/result*, *that trigger and arrival are distinct procedural instants* — the check at the end of turn N, arrival at the beginning of turn N+1, with no intervening Game-Turn-Checklist iteration — *and that the check does not run during round-mode*. It does **not** independently establish whether an encounter's own credited turn(s) — per `EXP-002`'s now-approved discrete whole-turn-credit model, produced while normal Game-Turn-Checklist execution is suspended — participate in that every-two-turns cadence when ordinary play resumes.

## 6. Whole-Source Search

**Search terms used** (exact strings tested against the full 1.9M-character transcription, in addition to the terms suggested by the assigning task): `wandering monster`, `Wandering Monster`, `Wandering Monsters`, `random encounter`, `Random Encounter`, `Chance of Encounter`, `every other turn` *(0 hits — OCR line-wrap artifact, see §2)*, `every two turns`, `every turn`, `beginning of the next turn`, `beginning of the turn`, `end of the turn`, `end of every turn`, `Handling Wandering`, `check for wandering`, `Encounter Table`, `Level of Dungeon`, `dungeon level`, `Handling Wandering Monsters`, `cleared`, `noise`, `Loud`, `suppress` *(0 hits)*, `lair`, `stocked`, `Monster Determination` *(0 hits)*, `Reaction`, `Surprise`, `Level Beneath` *(0 hits)*, `deeper`, `level of the dungeon`, `resume`, `after combat` *(0 hits)*, `after the encounter` *(0 hits)*, `Timekeeping`, `Timetrack`, `Record Keeping`, `interrupt`, `Dungeon Adventures` *(0 hits)*, `Chapter 7:`.

**Chapters/sections inspected:** Ch. 6 (Movement) — already characterized during `EXP-002`'s research, re-confirmed no wandering-monster content lives there; Ch. 7 (Encounters and Evasion) — Exploration and the Game Turn, Game Turn Checklist, Wandering Monster Encounters subsection, Chance of Encounter Table, Encounter Checklist, Surprise, Monster Reactions; Ch. 8 (Combat) — confirmed (during `EXP-002`'s research) to add nothing about wandering-monster cadence, only the Combat Sequence Checklist; Ch. 13 (Dungeon Master Procedures) — Record Keeping, Timekeeping, Timetrack Table, re-checked here and found to add nothing about cadence-during-encounters; monster stat-block area (Number Appearing / dungeon-level adjustment text) — confirmed dungeon level affects Number Appearing, not check cadence.

**Important cross-references discovered:**
- Game Turn Checklist step 1 → "Encounter Distance" section (governs arrival distance, not cadence).
- Game Turn Checklist step 1 → "Handling Wandering Monsters" (in-text name; actual heading appears to be "Wandering Monster Encounters" per TOC — see Evidence Map).
- Wandering Monster Encounters subsection → "the wandering monsters tables later in this chapter" — confirms monster-determination content (`MON-001`'s territory) is a separate, later part of the *same* chapter, not a different chapter, and is explicitly not this check's own concern.
- Encounter Checklist step 5(d) → Combat Sequence Checklist, Ch. 8 p. 102 (already characterized under `EXP-002`; adds nothing new here).
- Wilderness "Resume Travel" step (Game Day Checklist, Ch. 7 p. 91) — structurally analogous to the dungeon-scale "Encounter Ends: begin play with a new turn," and equally silent on any counter-continuity question. Its silence, matching the dungeon-scale procedure's silence, is treated as corroborating evidence that this is a genuine, structural RC gap rather than a search miss.

## 7. Falsification Passes

**Tentative conclusion (cadence):** under ordinary turn-mode exploration, the dungeon wandering-monster check is made once every two Game-Turn-Checklist iterations, never every single turn as a baseline rule. This is scoped to ordinary Game-Turn-Checklist iterations specifically — it does not assert whether encounter-credited turns participate in the same count (see row A, §9 item 1).
**Challenge:** is there another RC passage stating a different baseline frequency for dungeons specifically, or qualifying this one?
**Searches performed:** `every turn`, `every other turn`, `every two turns`, `Chance of Encounter`, `dungeon level`.
**Evidence:** two independent passages (checklist step 4; "Wandering Monster Encounters" subsection) state the identical two-turn cadence, with no located contradiction. The only located exception is the explicit "loud noises, battles, cursed items, special areas" modifier, which is a documented, named exception to the baseline, not a contradiction of it.
**Disposition:** **CONFIRMED** (baseline, ordinary turn-mode only), with the noise/battle/etc. modifier recorded as a separate, explicitly-flagged exception (see Evidence Map, row G), and encounter-credited-turn participation in this baseline left unresolved (see row A, §9 item 1).

**Tentative conclusion (check roll/result):** in a dungeon, 1d6 is rolled and a result of "1" is positive.
**Challenge:** does any other RC dungeon-context table use a different die or a different triggering result (e.g., the historically-familiar "6" from 1974 material, or a range rather than a single value)?
**Searches performed:** `Chance of Encounter`, `Encounter Table`, `1d6`/`ld6` occurrences in the immediate vicinity of both wandering-monster passages, the Chance of Encounter Table's own dungeon/city row.
**Evidence:** both the Game Turn Checklist and the Chance of Encounter Table agree: dungeon and city both use 1d6, triggering on "1." Wilderness uses a different (still 1d6-based, but range-based, e.g. 1–2 or 1–3) trigger depending on terrain — a documented, explained *difference*, not a contradiction of the dungeon rule.
**Disposition:** **CONFIRMED**.

**Tentative conclusion (timing — check at turn-end, arrival at next turn's start):** the roll happens at the procedural end of a Game-Turn-Checklist iteration (step 4 of 4); a resulting arrival happens at the start of the following iteration (step 1).
**Challenge:** does anything elsewhere describe the check occurring at the *beginning* of a turn instead, or arrival occurring *immediately* rather than delayed?
**Searches performed:** `beginning of the turn`, `beginning of the next turn`, `end of the turn`, `end of every turn`, direct re-reading of Game Turn Checklist steps 1–4 in full, direct re-reading of the "Wandering Monster Encounters" subsection in full.
**Evidence:** every located passage is mutually consistent — checklist step 1 ("check at the end of the previous turn... arrive now"), checklist step 4 ("at the beginning of the next turn"), and the subsection ("they appear the following turn") all describe the same pattern: a positive check at the end of turn N schedules arrival at the beginning of turn N+1, on opposite sides of the single intervening turn boundary, with no located exception and no additional full turn elapsing between the two instants.
**Disposition:** **CONFIRMED**.

**Tentative conclusion (`EXP-002` interface — encounter-credited turns and cadence):** RC does not state whether a turn credited to a resolved encounter (per `EXP-002`'s `max(1, ceiling(encounter_rounds/60))` model) counts toward the every-two-turns cadence.
**Challenge:** search specifically for any statement that would settle this either way — a rule tying cadence to elapsed game-time generally (which would imply encounter-credited turns *do* count, since they are dungeon turns by `EXP-002`'s own definition), or a rule explicitly resetting/pausing the counter across an encounter (which would imply they do *not*).
**Searches performed:** `resume`, `after combat`, `after the encounter`, `interrupt`, direct re-reading of Encounter Checklist step 6 ("Encounter Ends: begin play with a new turn") in full, direct re-reading of the structurally analogous Game Day Checklist step 5 ("Resume Travel: After the encounter, the party may resume travel") in full, direct re-reading of the Chapter 13 Timekeeping section in full.
**Evidence:** no passage was found stating either resolution. The two closest candidate passages (Encounter Checklist step 6; Game Day Checklist step 5) both describe *resuming* the higher-level procedure after an encounter without any statement about counters, cadence, or parity being preserved, reset, or otherwise affected. Their mutual silence, across two structurally parallel procedures at two different time-scales, is read as evidence this is a genuine gap in RC's own text rather than an unsearched corner.
**Disposition:** **REJECTED as a resolvable RC-Explicit question this pass.** Recorded as `RC UNRESOLVED` (§9), not manufactured into a Simulator Ruling or guessed at — no stop condition applies here, since a precise gap statement (not an ambiguous "couldn't find it") is the correct, expected Stage-A outcome for this question per the assigning task's own framing ("this is the principal interface question deliberately deferred from EXP-002... if RC does not resolve it, record the precise gap").

## 8. `EXP-002` Interface Evidence (consolidated)

- **`EXP-002` establishes** (read as active upstream project state, not reopened or revalidated here): a discrete, non-negative-integer turn-credit model. Ordinary Game-Turn-Checklist iterations each produce one credit; a resolved encounter produces `max(1, ceiling(encounter_rounds / 60))` credit(s), computed only once round-mode resolution finishes; no credit is produced during round-mode itself; multiple credits from one encounter remain individually distinguishable and correctly ordered; whether a given credit arose from an ordinary iteration or an encounter's resolution remains distinguishable information, deliberately preserved so that a cadence-sensitive consumer (`EXP-001`) *could* use it if needed.
- **RC establishes**, independently and consistently with the above, for ordinary turn-mode exploration: the wandering-monster check is a Game-Turn-Checklist step, occurring every two game turns; it does not run during round-mode (Encounter Checklist explicitly switches game time to rounds); a positive check at the end of turn N schedules arrival at the beginning of turn N+1 — distinct procedural instants on opposite sides of the next turn boundary, with no intervening Game-Turn-Checklist iteration, not a full additional turn elapsing between them.
- **RC does not establish**: whether the turn(s) credited to a resolved encounter's resolution count toward the every-two-turns parity once ordinary turn-mode resumes, or whether the counter is expected to simply continue counting through the interruption as though nothing had happened, restart, or otherwise be affected.
- **No incompatibility was found between `EXP-002`'s established contract and RC's `EXP-001`-relevant text.** `EXP-002`'s decision to preserve the ordinary-vs-encounter-credit distinction (rather than discarding it) appears, in light of this research, to have anticipated exactly the right piece of information a future `EXP-001` resolution might need — whichever way RC (or, if RC is silent, a future Simulator Ruling) ultimately resolves the cadence-continuity question. **No `UPSTREAM CONTRACT REVIEW MAY BE REQUIRED` flag is raised.**

## 9. Unresolved Questions

**`RC UNRESOLVED`**
1. Whether an encounter-credited turn counts toward `EXP-001`'s every-two-turns cadence the same as an ordinary turn (§7, §8).
2. The exact mechanism/table (if any) behind "and possibly with higher chances" for the noise/battle/cursed-item/special-area frequency modifier — RC states the increased-frequency part explicitly but the "higher chances" clause is not tied to a specific numeric table anywhere located.
3. Whether the noise/battle frequency modifier ("every turn" instead of every two) is intended to apply starting from the very next ordinary turn after a battle-triggering encounter, or only once some other condition is met — RC's wording ("battles" as a listed trigger) implies a battle can cause this, but does not state exactly when the heightened checking begins or how long it persists.
4. How many check opportunities a multi-turn *non-encounter* activity generates beyond the ordinary one-iteration-at-a-time reading (RC's checklist structure implies "one iteration, one possible check," but this was not separately, explicitly stated for a bulk multi-turn activity the way `EXP-002`'s own historical 1974 predecessor once addressed for its four-turn worked example — no RC equivalent worked example was located).
5. The precise reason for the "Handling Wandering Monsters" vs. "Wandering Monster Encounters" heading-name discrepancy (OCR artifact vs. genuine RC internal inconsistency) — low-stakes, does not affect the content already located.

**`BELONGS TO ANOTHER RULE CARD`**
6. Which specific monster appears once a check succeeds — `MON-001`.
7. Number Appearing, including the dungeon-level adjustment — `MON-002`.
8. Encounter distance calculation details beyond the 2d6×10' arrival-distance figure already captured — `ENC-001`.
9. Surprise, Monster Reactions, and the full Encounter Checklist's own mechanics beyond confirming they exist and that round-mode suspends turn-mode — `ENC-002`/`ENC-003`/combat domain, as already scoped by the inventory.
10. Dungeon stocking and the `MON-001` ↔ `EXP-008` circularity — not investigated or resolved here, per explicit instruction.

**`POTENTIAL STAGE-B COMPLETION RESEARCH`**
11. Item 1 above (encounter-credited-turn cadence participation) is the leading candidate for gap-directed alternate-source research in Stage B, **if** a human determines RC's silence needs completion rather than a Simulator Ruling or an as-designed "no distinction" reading. Not begun here.
12. Item 2 (numeric table behind "higher chances") is a secondary candidate, lower priority — the qualitative rule (check more often under those conditions) is already RC-Explicit; only the exact magnitude is unresolved.

**`UPSTREAM CONTRACT REVIEW MAY BE REQUIRED`**
13. None. See §8 — no incompatibility between RC evidence and `EXP-002`'s approved contract was found.

## 10. Confidence Assessment

High confidence for the core cadence/roll/timing/trigger-vs-appearance findings (items A–D): each rests on at least two independent, mutually consistent, directly-quoted primary-text passages, verified by direct re-reading of full surrounding context rather than isolated snippets, with a dedicated falsification pass for each. Medium-high confidence for the responsibility-boundary and modifier findings (item G, chapter/location corrections): single-location but directly-quoted RC text, cross-checked against the Table of Contents. The one genuinely open question (item E, encounter-cadence interaction) is reported as an honest gap after a real, documented search effort across the two structurally analogous procedures where an answer would most plausibly live — not a placeholder for research not yet attempted. No secondary source was consulted for any mechanical conclusion; the one methodological caveat is the OCR line-wrap issue noted in §2, which was identified and worked around, not silently absorbed into a false negative.

## 11. Recommendation

```text
EVIDENCE READY FOR HUMAN REVIEW
```

## 12. Human Evidence Review

```text
Human Evidence Review: ACCEPTED
Date: 2026-08-16
```

The Stage-A Rules Cyclopedia evidence basis above is accepted for progression to Stage B. Acceptance authorizes mechanical synthesis, legacy-card comparison, and gap-directed completion research under `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md`. **It does not approve `EXP-001` mechanics and does not change the Rule Card's lifecycle status** — `EXP-001` remains `REVALIDATION_REQUIRED` until a Stage-B draft is produced and separately, explicitly human-approved.

**Material Stage-B questions preserved, unresolved, from this evidence** (not resolved by this acceptance; Stage B must treat these as precise, gap-directed questions, not an invitation to browse earlier editions generally — `RULE_CARD_RESEARCH_PROTOCOL.md` §15):

1. Whether encounter-credited turn(s) — per `EXP-002`'s approved contract — participate in the every-two-turn wandering-monster cadence (§9 item 1).
2. What, if anything, supplies executable meaning to RC's "possibly with higher chances" language for noise, battles, cursed items, or special areas (§9 item 2).
3. Related timing/duration semantics for those heightened checks — when they begin and how long they persist relative to the triggering condition (§9 item 3).
4. Whether any completion is necessary for multi-turn non-encounter activities' check-opportunity count (§9 item 4).
