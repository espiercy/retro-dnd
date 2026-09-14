# Primary-Source Completeness Audit: CLUSTER-003 Stage A (CHAR-004, CHAR-005, EXP-003)

> **⚠ SUPERSEDED IN PART BY THE INDEPENDENT REVIEW AND BY REMEDIATION PASS 1 (2026-09-13).**
>
> The independent completeness review this artifact was prepared for **has now been performed, and it did not pass**:
>
> ```text
> CLUSTER-003 STAGE-A INDEPENDENT COMPLETENESS REVIEW
> RESULT:                      REMEDIATION REQUIRED
> PRIMARY-SOURCE COMPLETENESS: FAIL -- unfinished structural inspection
> BOUNDARY INTEGRITY:          REOPEN REQUIRED
> ALTERNATE-SOURCE RESEARCH:   NOT AUTHORIZED
> RULE CARDS / PRE-CODE / IMPLEMENTATION: NOT AUTHORIZED
> ```
>
> **The reviewer was right on both counts, and §10's own framing was wrong on one.** This artifact's §10 item 1 characterised the Mystic `MV` dependency as *"not a `CLUSTER-003` boundary-reopen condition — `CHAR-009` is not one of the three deferred cards."* The approved boundary rule is not limited to the deferred trio: it fires on a mechanically indispensable dependency on **any** unlanded Rule Card outside the cluster. **The boundary is reopened and provisional.**
>
> The remediation record — including the per-class inspection table, the two governing objects this audit's §7 failed to surface, and the boundary-reopen evidence package — is **`docs/rules/evidence/CLUSTER-003-remediation-pass-1.md`**. §13 below records what the reconciliation table in §8 looks like after remediation. **The body of this artifact is preserved unaltered as audit history**, including the incorrect §10 framing, because what the process actually concluded is evidence.
>
> **Status: ~~`RESEARCHER SELF-REVIEW COMPLETE / AWAITING INDEPENDENT COMPLETENESS REVIEW`~~ → `REMEDIATION COMPLETE / RESEARCHER SELF-REVIEW COMPLETE / AWAITING SECOND INDEPENDENT COMPLETENESS / BOUNDARY REVIEW`.**
>
> This artifact records the **adversarial self-review** permitted to the original researcher by `docs/rules/RULE_CARD_RESEARCH_PROTOCOL.md` §10.1.1. It is **not** the independent completeness review required by §10.1.2 / `DEC-0010` item 14, which "may NOT be performed by the original researcher." Nothing in this document certifies `CLUSTER-003` Stage-A completeness, and the researcher does not claim it.
>
> Applying the §10.3 method as the original researcher produces exactly one permitted output token, and this is it:
>
> ```text
> PREPARED FOR INDEPENDENT COMPLETENESS REVIEW
> ```
>
> **Stage B was not begun. No Rule Card was drafted. No production code was written. No cluster boundary was expanded.**

## 1. Audit Scope and Method

**Cards audited:** `CHAR-004` (Starting Equipment & Expedition Preparation), `CHAR-005` (Encumbrance & Movement Rate), `EXP-003` (**Dungeon Movement** — audited under its then-current title *"Dungeon Movement, Mapping & Special Terrain"*, **renamed 2026-09-14** by human governance decision; §14.3).

**Method — `DEC-0010` structure-first order, per protocol §9.1.1.** The pass began from the source's own structure, not from any prior packet (there are none for these three cards) and not from keyword search:

```text
1  RC Table of Contents                        -> audit class A
2  RC Index to Tables and Checklists (p. 301)  -> audit class B
3  governing-object inventory per card         -> audit classes C-I
4  visual inspection of mechanically
   significant tables (IIIF page images)       -> protocol SS9.2
5  complete governing sections read in full    -> protocol SS9.7 where in scope
6  explicit cross-references followed          -> audit class G
7  whole-source cross-reference search         -> protocol SS9
8  falsification / challenge pass              -> protocol SS10
9  open-question closure inventory             -> protocol SS10.2
10 adversarial self-review                     -> protocol SS10.1.1  <- this file
11 independent completeness review             -> protocol SS10.1.2  <- NOT DONE
12 human evidence review                       -> protocol SS11      <- NOT REACHED
```

**Research-risk classification: HIGH for all three cards** (protocol §9.4). *Equipment* and *encumbrance/movement* are both named high-risk responsibilities, mechanically significant tables drive every procedure, and **Guardrail D trigger 1 fires on `CHAR-005`** — a per-class table exists for the researched subject (the Mystic `MV` column). §9.2 visual verification was therefore mandatory, not discretionary, and was performed.

**Primary source.** *Dungeons & Dragons Rules Cyclopedia* (TSR, 1991). OCR transcription at `archive.org/stream/TSR1071TheDDRulesCyclopedia/TSR-1071-The-DD-Rules-Cyclopedia_djvu.txt` for navigation, search and prose; IIIF page images at `iiif.archive.org/iiif/TSR1071TheDDRulesCyclopedia$<leaf>/…` for visual verification (`leaf = printed_page − 1`). Neither access stop condition was triggered.

**Alternate sources: none consulted.** No RC gap has been established at a precision that authorises gap-directed research (protocol §15), and §9.1 forbids manufacturing that precondition on keyword exhaustion. AD&D was not consulted (`AGENTS.md` §4).

## 2. Objects Visually Verified (protocol §9.2)

Eleven mechanically significant structured objects were read from page images rather than OCR:

| # | Object | Printed page | Leaf | Card(s) | Outcome |
|---|---|---|---|---|---|
| 1 | Character Movement Rates and Encumbrance Table | 88 | n87 | `CHAR-005`, `EXP-003` | Four columns, six rows, no footnote, no hidden column |
| 2 | **Mystic Special Abilities Table (`MV` column)** | 31 | n30 | `CHAR-005` | 120′ → 320′ by level; **disproves the p. 88 universal** |
| 3 | Terrain Effects on Movement Table + footnote | 88 | n87 | `EXP-003` | All outdoor terrain; OCR `1 F2 normal` is really `1 ½ normal` |
| 4 | Traveling Rates by Terrain Table (header) | 88 | n87 | `EXP-003` | **Every numeric column is "Miles Covered Per Day"** |
| 5 | Starvation Table (`Movement Rates` column) | 150 | n149 | `CHAR-005` | `× 3/4` at 75–99% is **genuinely printed**, not OCR noise |
| 6 | Armor Table | 67 | n66 | `CHAR-004`, `CHAR-005` | Suit Armor `Enc 750 cn` confirmed |
| 7 | Adventuring Gear Table (both halves + 3 footnotes) | 69 | n68 | `CHAR-004` | **Two printed defects found** |
| 8 | Weapons Table (columns and values) | 62 | n61 | `CHAR-004` | Five columns; no dropped rows at the page break |
| 9 | Weapons Table (Notes) | 63 | n62 | `CHAR-004` | Twelve note codes confirmed |
| 10 | Ammunition Table | 63 | n62 | `CHAR-004` | **`Enc` column is "# of shots per cn"**, an inverse rate |
| 11 | Barding Encumbrance Table | 68 | n67 | `CHAR-004`, `CHAR-005` | Two-band animal system, structurally unlike the character table |

**Three of these eleven changed a conclusion that OCR alone would have produced** (#3, #5, #10), and one (#2) was reached only through the Tables Index, not through any chapter a topic-driven search would have opened. This is `DEC-0010`'s stated purpose operating as intended, and it is the strongest single argument for not treating this cluster's evidence as closable by search.

## 3. Primary-Source Object Inventory — `CHAR-004`

| Class | Object | Inspected | Disposition |
|---|---|---|---|
| A | Ch. 1 steps 5–6 "Roll for Money" / "Buy Equipment", p. 8 | Yes, in full | Governing procedure |
| A | Ch. 4 Equipment pp. 62–74 | Money, Weapons, Armor, Adventuring Gear, Land Transportation read in full | Governing catalogs |
| A | Ch. 13 "Equipment Not Listed", p. 147 | Yes, in full | Governing (unlisted-item procedure) |
| B | Tables Index — 23 equipment-bearing entries | Swept in full | See §2 for the six verified |
| C | Weapons, Weapons (Notes), Ammunition, Armor, Barding, Barding Encumbrance, Adventuring Gear, Riding Animal Costs, Land Transportation Gear, Nets | All inspected; six **visually verified** | Nets Table OCR-only; its mechanically significant rule lives in verified note `n` |
| D | Ch. 2 class entries (weapon/armour permissions) | **No — stopped at cluster boundary** | **OPEN** — `CHAR-004-evidence.md` §11 item 3 |
| E/I | Starting money and free kit stated 3× (Ch. 1 p. 8, Ch. 4 p. 62, Ch. 4 p. 69) | All three recorded separately | Divergence recorded as Defect 4 |
| F | Weapon descriptions A–W; Armor incl. complete Suit Armor; Adventuring Gear descriptions A–W; Land Transportation descriptions and Vehicle Movement Speeds | Yes | Governing |
| G | Ch. 1 → Ch. 2; Ch. 4 → Ch. 6; Ch. 4 → Ch. 14; note `r` → Ch. 5; thieves' tools → `CHAR-010`; Ch. 13 → Ch. 4 | All six followed | Four routed out of scope |
| H | Index to Tables and Checklists p. 301 | Yes | Class-B instrument |
| H | General Index p. 302 | **No** | **OPEN** — `CHAR-004-evidence.md` §11 item 6 |
| — | Water transport, siege, Weapon Mastery, Treasure, Ch. 14 Loads, Ch. 11 retainers, `ADV-003` | **Deliberately excluded, each with a stated reason** | Recorded as located, not as absent |

## 4. Primary-Source Object Inventory — `CHAR-005`

| Class | Object | Inspected | Disposition |
|---|---|---|---|
| A | Ch. 6 Movement pp. 87–89 | Read in full through Water Travel | Governing |
| A | Ch. 13 Special Character Conditions p. 150; Climbing p. 145 | Yes, in full | **Three movement modifiers outside Ch. 6** |
| A | Ch. 4 Armor p. 67; Suit Armor p. 68; Barding p. 68; Vehicle Movement Speeds p. 70 | Yes | Overrides and parallel systems |
| B | Tables Index — 21 movement/encumbrance-bearing entries | Swept in full | **Surfaced the Mystic and Ethereal Plane tables** |
| C | Character Movement Rates and Encumbrance; Mystic Special Abilities; Starvation; Barding Encumbrance; both terrain tables; Measurements of Game Time | All inspected; six **visually verified** | Governing or boundary |
| D | Mystic class table inspected as a structured object, then its prose legend | Yes | **Decisive finding** |
| D | The other eight class entries, for a movement statement | **No** | **OPEN** — `CHAR-005-evidence.md` §11 item 1 |
| E/I | Coin-weight stated in Ch. 4 p. 63 and Ch. 6 p. 88, with different wording (*awkwardness*) | Both recorded | Class-I divergence preserved |
| E/I | Character encumbrance (six bands) vs. animal/vehicle encumbrance (two bands) | Both recorded | **Recorded as separate systems, not merged** |
| F | Ch. 6 Time, Distance, Feet vs. Yards, Map Scales, Movement, Normal/Encounter/Running, Exhaustion, Character Movement Rates, Monster Movement Rates, Land Travel, Swimming | Yes | Governing |
| G | Ch. 4 → Ch. 6; Ch. 6 → Ch. 14; Ch. 6 → Endurance skill; Ch. 6 → Measurements table; Ch. 2 → Ch. 5 Acrobatics | All followed | Three routed out |
| H | Index to Tables and Checklists p. 301 | Yes | Class-B instrument |
| H | General Index p. 302 | **No** | **OPEN** — `CHAR-005-evidence.md` §11 item 4 |
| — | Ch. 19 Variant Rules body | **No — only its three TOC sub-headings** | **OPEN** — `CHAR-005-evidence.md` §11 item 3 |
| — | Water Movement Modification Table, Aerial Travel, Ethereal Plane movement, spell-borne movement effects, Ch. 14 monster Loads | **Deliberately excluded, each with a stated reason** | Recorded as located |

## 5. Primary-Source Object Inventory — `EXP-003`

| Class | Object | Inspected | Disposition |
|---|---|---|---|
| A | Ch. 7 "Exploration and the Game Turn" p. 91 | Yes, in full | **Governing procedure** |
| A | Ch. 6 Time / Distance / Map Scales / Movement pp. 87–88 | Yes, in full | Governing |
| A | Ch. 13 Mapping p. 148; Climbing p. 145 | Yes, in full | Mapping: **no mechanic** |
| A | Ch. 1 "Mapping and Calling" | Yes, in full | Player roles, explicitly not game rules |
| B | Tables Index — terrain, exploration, time, evasion entries | Swept in full | **Exactly two terrain tables exist; both verified** |
| C | Game Turn Checklist; both terrain tables; Measurements of Game Time; Character Movement Rates | Inspected; three **visually verified** | Governing or bounding |
| D | Mystic class table + Acrobatics prose | Yes | **Sole text presupposing dungeon-scale terrain effects** |
| E/I | Mapper's role stated in Ch. 1 and Ch. 13 p. 148 | Both recorded separately | Class-I divergence preserved |
| F | Ch. 7 exploration sections; Ch. 6 movement sections; Ch. 13 Mapping and Climbing; Ch. 1 Mapping and Calling | Yes | Governing |
| G | Ch. 7 → Ch. 6; Ch. 6 → terrain tables; Ch. 7 → Encounter Checklist; Ch. 7 step 3b → the mapper; Ch. 7 p. 98 → Evasion Table; Ch. 2 → unstated terrain modifier | All followed | Four routed out |
| H | Index to Tables and Checklists p. 301 | Yes | Class-B instrument |
| H | General Index p. 302 | **No** | **OPEN** — `EXP-003-evidence.md` §11 item 4 |
| — | Ch. 17 "Designing Adventures and Dungeons" pp. 259–262 | **No** | **OPEN** — `EXP-003-evidence.md` §11 item 3 |
| — | Encounter Checklist, Evasion Table, Doors, Listening, light sources, traps, `P3` Ability Checks, overland travel | **Deliberately excluded with ownership and rationale** | `CONFIRMED OUT OF SCOPE` |

## 6. Findings

### Finding 1 — `CHAR-005` has an unlanded incoming dependency that `INVENTORY.md` does not record

RC p. 88 states "**Any character** will have a movement rate of `120' (40')` unless he is weighed down by a lot of gear." RC p. 31's **visually verified** Mystic `MV` column contradicts that universal for one of the nine V1 classes, rising to 320′ at 16th level, with the class text confirming that above 16th level "the mystic's armor class, **movement rate**, number of attacks, and hand-to-hand damage no longer improve."

`INVENTORY.md` records `CHAR-005`'s dependency as `CHAR-004` alone. On this evidence that is **incomplete**: the Mystic progression is class-entry material scoped in `CHAR-009`'s row.

**This is raised, not resolved.** It is **not** a boundary-reopen condition as the task defined it — `CHAR-009` is not among the three deliberately deferred items (`CHAR-006`, `CHAR-008`, `EXP-010`) — but it is a genuine unlanded incoming dependency that a human must settle before Stage B.

**How this finding was reached matters.** It came from the **Tables Index**, not from Chapter 6 and not from a topic search. A researcher who had read the movement chapter thoroughly and searched `movement rate` would still have had to read the out-of-domain hits to find it. Protocol §9.4 Guardrail D trigger 2 — *question the search strategy before drawing any conclusion about the source* — is what produced it.

### Finding 2 — `CHAR-004`'s ownership of purchase legality is genuinely contested by the source itself

RC states class weapon and armour permissions in **Chapter 4 itself** (Weapons Table notes `c`, `w`, `2H`, `HH`; the armour prose naming nine classes) **and** routes the buying step to Chapter 2: "Before you go shopping, be sure you have read the full description of your character class" (Ch. 1 p. 8). Landed `CHAR-002`'s approved boundary assigns "weapon/armor permissions" to `CHAR-009`/`TREAS-004`.

This is an **audit class I duplicate presentation**, not a missing dependency. The assigned falsification target — that `CHAR-004` needs no unlanded class card — survives for the money roll, the catalog, costs, encumbrances and the unlisted-item procedure, and **does not survive** for purchase legality. Raised for human governance.

### Finding 3 — the `EXP-003` "Special Terrain" responsibility has no located RC dungeon-scale mechanic

Three independent lines converge:

1. RC's own bounding sentence: terrain "**makes no difference to the combat round or the 10-minute turn**" (Ch. 6 p. 88).
2. The Tables Index lists **exactly two** terrain tables, both on p. 88; both were **visually verified**; both operate on **miles per day**.
3. The only RC application of "difficult terrain" to a dungeon is an **evasion** condition (Ch. 7 p. 98), owned by `ENC-005`.

Against that stands a single presupposition: Mystic Acrobatics (Ch. 2 p. 31) lets a mystic cross "rough, broken terrain at no modification to his movement rate… it only affects his **encounter speed and running speed**" — a rule RC never states.

**Disposition: `RC DOES NOT SPECIFY`.** Recorded, not completed, not invented. This is the second-strongest argument in the cluster for visual verification: the bounding sentence and the table headers are both page-layout facts that OCR degrades.

### Finding 4 — the `EXP-003` "Mapping" responsibility is a DM technique with no mechanic

Both RC mapping passages were read in full. Ch. 13 p. 148 is four description guidelines (clear descriptions, consistent terms — *side passage*, *four-way intersection*, *T-intersection* — a standard `10' wide and 10' high` corridor convention, simple shapes first). Ch. 1 "Mapping and Calling" defines mapper and caller as **player roles**, with the caller explicitly "**not a game rule that players have to use**". And Ch. 6 p. 88 states that normal speed "includes many assumed actions—**mapping**, peeking around corners, resting."

**Consequence for Stage B, recorded now so it cannot be silently violated later:** charging exploration time for mapping would **double-count** a cost RC has already priced into the rate.

### Finding 5 — `EXP-010` is not an incoming dependency of `EXP-003`

`marching order` occurs **once** in the whole OCR text, in **NPC party generation**. `single file`, `front rank`, `order of march` and `abreast` return nothing. RC's two party roles are conveniences, one of them explicitly not a rule. The Tables Index contains no formation table.

**The task's boundary-reopen condition is therefore NOT triggered by `EXP-010`.** Stated as coverage over the objects inspected, not as proof RC contains nothing.

### Finding 6 — four internal source defects, all visually verified, none resolved

| # | Defect | Objects verified | Disposition |
|---|---|---|---|
| 1 | **Belt pouch arithmetic.** Printed row `Pouch, belt | Capacity 50 cn | 5 sp | 2*`; printed footnote "a fully filled belt pouch has an encumbrance of **55 cn**". `2 + 50 = 52 ≠ 55`. | Both on leaf n68 | `RETAINED AS GENUINE SOURCE AMBIGUITY` |
| 2 | **Suit Armor movement.** `Enc 750 cn` (leaf n66) sits in the `401–800` band → `90' (30')` (leaf n87); the item description states "**The wearer's movement rate is 30' (10')**" — the `1,201–1,600` band. RC supplies no override language in either direction. | Three objects, all verified | `RETAINED AS GENUINE SOURCE AMBIGUITY` |
| 3 | **Starvation Table non-monotonicity.** Movement column runs `No Penalty / × 3/4 / × 1/2 / × 3/4` while rest hours (6→8→10→12) and attack penalty (none→−2→−4→−6) both worsen monotonically. The page image was read specifically to exclude an OCR artifact: **the print really says `× 3/4`.** | Leaf n149 | `RETAINED AS GENUINE SOURCE AMBIGUITY` |
| 4 | **"Clothes, plain" footnote marker.** Prints `20***` (the *quiver* footnote) where every other clothing row prints `**` (the packed/worn footnote). | Leaf n68 | Recorded as a **typographic defect**, not as a rule |

Per protocol §10.2.2 case 3, a fully mapped genuine conflict does not itself block source completeness. All four qualify: the governing objects are inspected, the contradictory passages are recorded verbatim, and none is an unfinished inspection wearing an ambiguity's clothes.

### Finding 7 — `CHAR-004` encumbrance is not a constant per item

At least four item classes carry **derived** encumbrance: nets and whips are priced per square foot / per foot (`1 cn` per sq ft; `10 cn` per ft); containers change encumbrance when filled (footnote `*`); packed clothing's encumbrance is **disregarded entirely when worn** (footnote `**`); and a weapon's listed `Enc` already includes a normal ammunition load, which varies (footnote `a`). A Stage-B specification modelling `Enc` as a scalar per catalog row would be incomplete against the verified source.

### Finding 8 — character, animal and vehicle encumbrance are three presentations of two different systems

Characters use a **six-band** table (RC p. 88). Animals use a **two-band** table — `Full Movement (cn)` / `Half Movement (cn)` (RC p. 68, verified) — and monsters use the same shape by RC's own description ("somewhat simpler… full movement rate up to a certain amount… half its movement rate up to twice that amount", Ch. 6 p. 88), with per-creature values in Ch. 14. Vehicles inherit the animal rule. Recorded as **separate systems**, per audit class I; not merged, and not generalised into one model.

## 7. Adversarial Self-Review (protocol §10.1.1)

The §10.3 challenge list, applied by the original researcher to his own work. This is self-review; it is not certification.

| Challenge | Answer |
|---|---|
| Were all relevant tables located? | The Tables Index was swept in full for all three cards and is the reason two objects entered the packets that no chapter-driven pass would have reached (Mystic `MV`, Movement in the Ethereal Plane). **Eleven objects were visually verified.** Three tables remain OCR-only and are declared: Nets (p. 65), Riding Animal Costs and Land Transportation Gear (p. 70). |
| Were all relevant stat blocks checked? | **No — and this is the largest declared hole.** Only the Mystic class table was opened as a structured object. The other eight class entries were not checked for a movement statement (`CHAR-005-evidence.md` §11 item 1), and none was read as a complete entry for weapon/armour permissions (`CHAR-004-evidence.md` §11 item 3). Given that the *one* class table opened overturned a stated universal, the prior that the others are silent is weaker than it would otherwise be. |
| Did the Tables Index reveal anything absent from the packets? | It revealed the two findings above **into** the packets. Nothing surfaced by the Index was dropped: the Ethereal Plane movement table and the water/siege tables are recorded as located-and-excluded with reasons rather than omitted. |
| Did a later chapter restate the mechanic? | Yes, repeatedly, and each restatement is recorded separately: coin-weight (Ch. 4 and Ch. 6), starting money and free kit (Ch. 1, Ch. 4 table, Ch. 4 description), the mapper's role (Ch. 1 and Ch. 13), and encumbrance-to-movement (Ch. 4 cross-reference and Ch. 6 table). |
| Did OCR flatten, mangle, or drop a meaningful table? | **Yes, three times, each caught by visual verification**: the Terrain Effects table's `1 ½ normal` read as `1 F2 normal`; the Ammunition table's `Enc` column semantics (*# of shots per cn*) were destroyed by linearisation; the Starvation table's movement column was ambiguous in OCR and had to be resolved on the page. |
| Did the researcher treat prose as complete when an operational table exists? | Checked specifically for this. The p. 88 table was taken as the operational object for encumbrance→rate, and the prose was read for what the table cannot carry (group rate, exhaustion, running limits, unit semantics). The reverse error — treating a table as complete when governing prose exists — is what Finding 1 and Finding 6.2 correct. |
| Did the packets follow all explicit cross-references? | All located cross-references were followed at least to the point of establishing ownership. Four were deliberately stopped at the cluster boundary and each stop is declared: Ch. 2 class descriptions, Ch. 14 monster Loads, `P3` Ability Checks, and the Encounter Checklist. |
| Was any negative finding asserted as absence rather than "not located"? | Reviewed line by line. Every negative in the three packets is phrased as coverage over named inspected objects. **One negative is stronger than "not located" and is deliberately so** — that dungeon terrain does not modify turn-scale movement — because RC states it positively ("makes no difference to the combat round or the 10-minute turn") and both candidate tables were visually verified. That is the difference protocol §9.1 draws, and it is claimed only where the difference is real. |

**What this self-review did not do, and could not:** begin from a context that had not already formed these conclusions. That is precisely why §10.1.2 exists, and why this artifact stops where it does.

## 8. Open-Question Closure Gate — reconciliation table (protocol §10.2.1)

Every declared open item across the three packets, in one place.

| # | Original open question | Source region/object implicated | Inspection completed? | Result | Responsibility owner | Still blocks completeness? |
|---|---|---|---|---|---|---|
| 1 | Ch. 2 class entries as complete entries — weapon/armour permissions | RC pp. 13–31 | **No** | Deliberately stopped at cluster boundary; ownership contested (Finding 2) | `CHAR-009` (proposed) / human | **Yes**, if `CHAR-004` is ruled to own purchase legality |
| 2 | The other eight class tables — any `MV`-style column | RC pp. 13–29 | **No** | Only the Mystic table was opened | `CHAR-009` / `CHAR-005` | **Yes** |
| 3 | Ch. 19 Variant Rules body | RC pp. 266–267 | **No** | Only three TOC sub-headings used | `CHAR-005` | **Yes** |
| 4 | Ch. 17 "Designing Adventures and Dungeons" | RC pp. 259–262 | **No** | Not opened | `EXP-003` | **Yes** |
| 5 | General Index (p. 302) as a completeness locator | RC Appendix 4 | **No** | Tables Index swept in full; General Index not | all three | **Yes** — audit class H partly discharged |
| 6 | Ch. 10 high-level character creation — any wealth/equipment provision | RC pp. 129–131 | **No** | Located in `CLUSTER-002`; not re-opened | `CHAR-001` §5 / `CHAR-004` | **Yes** — small and cheap to close |
| 7 | Nets Table not visually verified | RC p. 65 | **No** | The mechanically significant rule (1 sp / 1 cn per sq ft) lives in **verified** note `n` | `CHAR-004` | No |
| 8 | Riding Animal Costs / Land Transportation Gear Tables not visually verified | RC p. 70 | **No** | Deliberate; scope unsettled (row 9) | pending row 9 | **Yes**, if mounts are ruled in scope |
| 9 | Whether `CHAR-004` extends to mounts, vehicles, ships and siege | RC Ch. 4 pp. 70–74 | Partial | Scope question, not a source question | **Human governance** | **Yes** |
| 10 | Whether the blindness / stunning / starvation movement multipliers belong to `CHAR-005` or to an unassigned condition responsibility | RC p. 150 | **Yes — text inspected** | Ownership question | **Human governance** | **Yes** — a Rule ID may need assigning, which this researcher may not do |
| 11 | Whether "Mapping" survives in `EXP-003`'s title as a mechanic | RC Ch. 1 + Ch. 13 p. 148 | **Yes — both read in full** | No mechanic exists to own (Finding 4) | **Human governance** | **Yes** — card-scope decision |
| 12 | Mystic `MV` × encumbrance composition | RC p. 31 + RC p. 88 | **Yes — both objects inspected** | RC does not address it | human / Stage B | No — `RETAINED AS GENUINE SOURCE AMBIGUITY` |
| 13 | Racial-armour movement reduction magnitude | RC p. 67 | **Yes — text inspected** | `RC DOES NOT SPECIFY` | human / Stage B | No |
| 14 | Rough/broken-terrain modifier presupposed by Mystic Acrobatics | RC p. 31 ↔ p. 88 ↔ Tables Index | **Yes for indexed objects** | `RC DOES NOT SPECIFY` (Finding 3) | human / Stage B | No |
| 15 | Suit Armor movement conflict | RC pp. 67, 68, 88 | **Yes — all three verified** | Genuine printed contradiction | human / Stage B | No — §10.2.2 case 3 |
| 16 | Starvation Table non-monotonicity | RC p. 150 | **Yes — verified** | Genuine printed defect | human / Stage B | No — §10.2.2 case 3 |
| 17 | Belt pouch arithmetic | RC p. 69 | **Yes — both sides verified** | Genuine printed defect | human / Stage B | No — §10.2.2 case 3 |
| 18 | `EXP-005` / `EXP-007` resolution procedures | RC Ch. 13 pp. 147–148 | **No — deliberately** | Already assigned; Doors recorded in the landed `CLUSTER-002` audit §5.4 | `EXP-005`, `EXP-007` | No — `CONFIRMED OUT OF SCOPE` |
| 19 | `EXP-010` as a prerequisite | whole-source sweep + Ch. 1 roles | **Yes for objects inspected** | No RC prerequisite located (Finding 5) | `EXP-010` (deferred) | No — **boundary-reopen NOT triggered** |
| 20 | `P3` generic Ability Check | RC Ch. 13 p. 143 | **No — deliberately not opened** | Reached only as a cross-reference from Climbing | deferred item `P3` | No — **not absorbed** |
| 21 | Water/aerial travel, Ethereal Plane movement, siege, Treasure, Ch. 14 Loads, Ch. 11 retainers | various | **No — deliberately** | Excluded with reasons; recorded as located | respective owners | No |

**Six rows (1–6) are unfinished source inspection, and three (9, 10, 11) require human decisions.** Per protocol §10.2, **there are zero silent unresolved research tasks** — every one is on this table. And per §10.2, completeness may not be declared while they stand. **It is not declared.**

## 9. Negative-Finding Re-Audit

Each negative claim in the three packets, restated with the objects that support it, so a reviewer can attack it directly.

| Negative claim | Objects inspected that support it | Strength |
|---|---|---|
| No third character-carried equipment catalog beyond the seven located | TOC Ch. 4; Tables Index (23 entries); Ch. 4 read in full | **Not located** — bounded by open rows 1, 5 |
| No per-class starting-equipment package or kit table | Tables Index; Ch. 1 steps 5–6; Ch. 4 Money | **Not located** — bounded by open rows 1, 6 |
| No optional or simplified encumbrance variant | `optional rule` sweep; Ch. 19 TOC sub-headings; Tables Index | **Not located** — bounded by open row 3; deliberately *not* claimed as absence |
| No second character encumbrance table | Tables Index swept in full; Ch. 6 read in full | **Not located**, strong |
| No RC statement reconciling Mystic `MV` with encumbrance bands | **Both governing objects inspected and verified** | **Genuine gap**, not a search miss |
| No mapping mechanic | Both mapping passages read in full; Ch. 6 p. 88 states mapping is already in the rate | **Strong** — supported by a positive statement |
| No PC marching-order procedure | phrase sweep (`marching order` = 1 hit, NPC generation); Ch. 1 roles read in full; Tables Index | **Not located**, moderate-strong |
| No dungeon-scale terrain movement modifier | **RC's own bounding sentence** + both terrain tables **visually verified** + Tables Index exhaustive for terrain | **Strongest** — an explicit positive statement of non-application |

**No negative in these packets is asserted as absence on the strength of a failed search alone.** Where a claim is stronger than "not located", the positive text that makes it stronger is cited.

## 10. Boundary and Governance Questions Raised — for Human Decision Only

None of the following is decided, adopted, or acted on. Each is raised because a researcher may not settle it.

1. **`CHAR-005` → class-abilities dependency** (Finding 1). Does `CHAR-005` acquire a `CHAR-009` dependency, or does the Mystic `MV` progression stay wholly in `CHAR-009` with `CHAR-005` specifying only the encumbrance-driven component? `INVENTORY.md`'s `CHAR-005` dependency cell is incomplete either way.
2. **`CHAR-004` → purchase legality** (Finding 2). Does `CHAR-004` own class weapon/armour purchase restrictions — which RC states in `CHAR-004`'s own chapter — or do they stay with `CHAR-009`/`TREAS-004` as `CHAR-002`'s approved boundary has it?
3. **`CHAR-004` scope.** Does "Starting Equipment & Expedition Preparation" extend to mounts, vehicles, ships and siege equipment, all of which live in Chapter 4?
4. **Condition-driven movement multipliers.** Do blindness, stunning and starvation movement effects belong to `CHAR-005`, or to a status-condition responsibility that `INVENTORY.md` does not currently contain? **No Rule ID was invented.**
5. **`EXP-003` title.** "Mapping" names no RC mechanic and "Special Terrain" names no located RC dungeon-scale mechanic. Whether the card's title should change is a governance decision.
6. **Where the `RC DOES NOT SPECIFY` items go.** The racial-armour reduction and the rough-terrain modifier are candidates for gap-directed alternate-source research **after** the §9.1 audit closes — not before, and not on this researcher's initiative.

**Deferred items untouched, as instructed:** `CHAR-006` (Retainers), `CHAR-008` (Alignment), `EXP-010` (Party Formation & Marching Order) — none researched, none absorbed, and `EXP-010` was tested only to establish it is **not** a prerequisite. `P1`, `P3`, `CHAR-003 W2` (MOOT) and `CHAR-003 W3` (NOT V1-WIRED) — untouched. `DEC-0010` and `DEC-0011` — not reopened.

## 11. Status After This Audit

```text
CHAR-004   Stage-A packet written; SS11.19 recommendation MORE PRIMARY RESEARCH REQUIRED
CHAR-005   Stage-A packet written; SS11.19 recommendation MORE PRIMARY RESEARCH REQUIRED
EXP-003    Stage-A packet written; SS11.19 recommendation MORE PRIMARY RESEARCH REQUIRED

CLUSTER-003 Stage A
    adversarial self-review (SS10.1.1)          COMPLETE  <- this artifact
    independent completeness review (SS10.1.2)  NOT PERFORMED
    human evidence review (SS11)                NOT REACHED
    Stage B                                    NOT BEGUN, NOT ELIGIBLE
```

**What the `MORE PRIMARY RESEARCH REQUIRED` recommendation means here.** It is not a report of failure and not a claim that the cards are poorly understood — all three core procedures are established and eleven governing objects are visually verified. It means that six rows of §8's reconciliation table are **unfinished source inspection**, which `DEC-0010` forbids carrying past a completeness claim, and three more require human decisions no researcher may make. The honest status is that the evidence is substantial, the perimeter is not closed, and the researcher who collected it is not the one who gets to say it is.

```text
CLUSTER-003 STAGE-A RESEARCH:
RESEARCHER SELF-REVIEW COMPLETE
AWAITING INDEPENDENT COMPLETENESS REVIEW
```

---

## 13. Post-Remediation Reconciliation (added 2026-09-13)

> Recorded after the independent review returned `REMEDIATION REQUIRED` and remediation pass 1 was performed. Full detail: `docs/rules/evidence/CLUSTER-003-remediation-pass-1.md`.

### 13.1 What the independent reviewer found incomplete

1. **Unfinished structural inspection** — rows 1–6 of §8's reconciliation table were declared open and were genuinely load-bearing, not cosmetic.
2. **Boundary integrity** — the Mystic `MV` dependency did trigger the reopen condition, and §10 item 1 said it did not.

### 13.2 §8 reconciliation table after remediation

| §8 row | Then | Now |
|---|---|---|
| 1 — Ch. 2 class entries, weapon/armour permissions | Open | **CLOSED.** All nine entries read as complete entries; all nine boxed blocks visually verified. Five classes carry class-entry-only restrictions; the Druid carries a **+50% pricing rule**. Remediation §2, §4 |
| 2 — the other eight class tables, any `MV`-style column | Open | **CLOSED.** All nine experience tables opened as page images. Only the Mystic has a movement column. Corroborated by RC's own "Understanding the Tables" column enumeration. Remediation §2 |
| 3 — Ch. 19 body | Open | **CLOSED on complete inspection.** Two printed pages, both visually verified; five sections; **no encumbrance or movement variant.** The TOC's three sub-headings were indeed incomplete. Remediation §5.1 |
| 4 — Ch. 17 pp. 259–262 | Open | **CLOSED**, and pp. 256–257 added after the index flagged them. **Material finding:** the dungeon map scale is DM-variable. Remediation §5.2 |
| 5 — General Index | Open | **CLOSED, and it was not empty.** It surfaced **RC Ch. 8 p. 103 "Movement"** — a governing object this audit's §7 missed entirely — and the decisive `Weapon restrictions 14, 17, 19, 21, 23, 25, 26, 28, 29` entry. Remediation §5.3, §5.5 |
| 6 — Ch. 10 high-level creation | Open | **CLOSED, and it was not empty.** A different money rule (1% of XP), equipment by grant, an alternate cash method, two magic-item methods, a price table, and the only RC owned-vs-carried distinction. Remediation §5.4 |
| 7 — Nets Table not visually verified | Non-blocking | **Unchanged, still non-blocking** |
| 8, 9 — mount/vehicle tables; `CHAR-004` scope | Human decision | **Unchanged** |
| 10 — p. 150 condition multipliers ownership | Human decision | **Unchanged** |
| 11 — `EXP-003` "Mapping" in the title | Human decision | **Widened** — "Special Terrain" joins it. `CARD TITLE / RESPONSIBILITY BOUNDARY REVIEW REQUIRED` |
| 12 — Mystic `MV` × encumbrance | Retained ambiguity | **Retained, and now defensible** under §10.2.2 case 3. Sub-item closed: "above 16th level" is moot (`Maximum Level: 16`, visually verified) |
| 13 — racial-armour reduction | `RC DOES NOT SPECIFY` | **WITHDRAWN AS A GAP.** The complete sentence is *"The DM **can** impose penalties"* — RC delegates by design. This audit quoted the parenthetical without its governing sentence |
| 14 — rough/broken-terrain modifier | Possible gap | **Retained, now narrower.** RC Ch. 14 p. 153's Charge prohibition is a real indoor terrain constraint, but on an **action**, not a rate |
| 15–17 — Suit Armor, Starvation, belt pouch | Retained | **All three survive re-testing unchanged** |
| 18–21 — deliberate exclusions | Out of scope | **Unchanged** |

### 13.3 What §7's adversarial self-review got right, and what it missed

§7 answered *"Were all relevant tables located?"* by pointing at the Tables Index sweep, and *"Were all relevant stat blocks checked?"* with an honest **"No — and this is the largest declared hole."** That self-assessment was accurate: the class-entry hole was the single largest, and closing it produced Finding 2's sharpening and the per-class evidence in remediation §4.

What §7 **missed** is that its table-centred framing could not catch a governing object that is **prose under a plain heading inside another chapter's procedure**. RC Ch. 8 p. 103 is titled simply "Movement", carries no table, and is not reachable from the Tables Index. Only the **General Index** — audit class H, which §7 recorded as "only partially discharged" and then did not treat as blocking — leads to it.

**Lesson recorded for future clusters:** audit class H is not a formality to be discharged last. For a mechanic that appears in several chapters under a common word, the General Index is the instrument that finds the presentations a topic-driven search will not.

> **Elevated to a cross-cluster process precedent, 2026-09-14.** This lesson is now recorded as **`P-001`** in `docs/rules/RESEARCH_PROCESS_PRECEDENTS.md`:
>
> ```text
> When a primary source provides a General Index, General Index inspection
> is a REQUIRED source-structure completeness instrument for DEC-0010
> research, alongside the TOC and the Tables Index.
> ```
>
> That register is a **precedent record, not governance** — it does not amend `DEC-0010` or `RULE_CARD_RESEARCH_PROTOCOL.md`, neither of which was modified. Elevating `P-001` into either is a human decision and is flagged there as outstanding.

### 13.4 New findings that did not exist before remediation

| Kind | Finding |
|---|---|
| **New governing object** | RC Ch. 8 p. 103 "Movement" — normal speed is *never* used in combat; movement-budget rules; and a **factor-of-3 inconsistency** with Ch. 6 on running speed |
| **New governing object** | RC Ch. 14 p. 153 "Charge" — *"A monster cannot charge in certain types of terrain: broken, heavy forest, jungle, mountain, swamp"*, with *"20 yards (**20 feet indoors**)"* |
| **New contradiction** | Magic-user dagger: Ch. 4 note `w` vs. Ch. 2 *"Dagger only"* |
| **New contradiction** | Running speed: Ch. 6 vs. Ch. 8 p. 103 |
| **New tension** | Mystic *"or own personal possessions"* — flavour framing the entry's own rules do not implement |
| **New tension** | Standing up: "one round of movement" vs. "an action" |
| **Reclassified** | Dungeon map scale — a DM-variable default, not a constant |
| **Reclassified** | Racial-armour movement reduction — DM discretion by design, **not** a gap |
| **Citation corrected** | "Mapping and Calling" is on **p. 5**, not in Chapter 1 |
| **Citation corrected** | The Dwarf Experience Table prints on **p. 24**; the Tables Index says p. 23 |

### 13.5 Status (as at 2026-09-13; superseded by §14)

```text
CLUSTER-003 STAGE-A REMEDIATION:

REMEDIATION COMPLETE
RESEARCHER SELF-REVIEW COMPLETE
AWAITING SECOND INDEPENDENT COMPLETENESS / BOUNDARY REVIEW

STAGE B:                    NOT STARTED / NOT AUTHORIZED
ALTERNATE-SOURCE RESEARCH:  NOT STARTED / NOT AUTHORIZED
```

---

## 14. Stage-A Closure (added 2026-09-14)

### 14.1 Second independent completeness / boundary review — result

```text
CLUSTER-003 STAGE-A REMEDIATION:   PASS
PRIMARY-SOURCE COMPLETENESS:       CONDITIONAL PASS
REMAINING COMPLETENESS ITEM:       visual verification of the Nets Table
BOUNDARY GOVERNANCE:               RESOLVED BY HUMAN DECISION
STAGE B / ALTERNATE-SOURCE:        NOT AUTHORIZED
```

The remediation recorded in §13 was **accepted substantively**. §10's incorrect boundary framing, which §13's banner withdrew, is confirmed withdrawn.

### 14.2 The one conditional item — closed

**Nets Table, RC p. 65, leaf n64 — visually verified 2026-09-14.**

```text
Nets Table
Victim's Size   Equivalent*    Net Size**
Very small      Up to 1'       2'X2'
Small           1+'-3'         4'X4'
Medium          3+'-6'         6'X6'
Large           6+'-10'        9'X9'
Very large      10+'-15'       12'x12'
Huge            15+'-20'       16'x16'
Mammoth         20+'-30'       25'X25'

 * A small net is right for a target the size of a halfling; a medium net
   is right for human, dwarf, and elf targets.
** Or equivalent in square feet.
```

Three columns, seven rows, two footnotes — **identical to the OCR record in `CHAR-004-evidence.md` §4.** Footnote `**` is the linkage to the **visually verified** Weapons Table note `n` (1 sp and 1 cn **per square foot**); RC's own worked example — a medium 6′×6′ net = 36 sq ft → 36 sp, 36 cn — is consistent with the Medium row, and every other row derives cleanly under the same rule. Footnote `*` calibrates the size categories to PC races.

```text
new mechanic?      NO
new contradiction? NO
new dependency?    NO
new ownership issue? NO
```

The verification did surface one detail worth recording rather than discarding: the net weapon description on the same page states that *"halflings and small nonhumans (such as goblins) **cannot use nets larger than 6′ × 6′**"* — a class/race mundane equipment restriction printed in **Chapter 4** rather than Chapter 2. It is an additional instance of an already-recorded category, it contradicts nothing, and under the 2026-09-14 governance Decision 1 it is already owned by `CHAR-004`. **It is not new substantive evidence and does not reopen any structural inspection.**

**Every identified primary-source inspection item for `CLUSTER-003` is now complete.**

### 14.3 Human boundary and ownership governance — applied

Five decisions were issued and applied; the canonical record is `docs/rules/clusters/CLUSTER-003-equipped-dungeon-movement.md` §3.1. In summary: `CHAR-004` owns mundane equipment legality; `CHAR-005` owns the authoritative movement-rate mechanic including Mystic `MV`; `EXP-003` is renamed and narrowed to **Dungeon Movement**; the Chapter 10 high-level pathway is **`researched / preserved / NOT V1-WIRED`**; and condition effects are split so that causation stays with its owner while the movement-rate effect belongs to `CHAR-005`.

**No additional whole Rule Card was required.** `CHAR-009`, `CHAR-006`, `CHAR-008` and `EXP-010` remain outside the cluster.

### 14.4 What did NOT change

**No source contradiction or ambiguity was resolved during closure.** The governance decisions settled *which card owns which mechanic*; they did not settle *what the rule is* anywhere the source is unclear. Every preserved question in §13.4 and §8 stands, and `DEC-0011` remains un-activated.

### 14.5 Status

```text
CLUSTER-003 STAGE-A PRIMARY-SOURCE RESEARCH:

RESEARCHER CLOSURE COMPLETE
ALL IDENTIFIED PRIMARY-SOURCE INSPECTION ITEMS COMPLETE
HUMAN BOUNDARY / OWNERSHIP GOVERNANCE APPLIED

AWAITING FINAL INDEPENDENT DEC-0010 COMPLETENESS CERTIFICATION

STAGE B:                    NOT STARTED / NOT AUTHORIZED
ALTERNATE-SOURCE RESEARCH:  NOT STARTED / NOT AUTHORIZED
```

**`STAGE-A COMPLETENESS PASS` is not written and must not be inferred.** `DEC-0010` reserves that certification to an independent reviewer who did not conduct the research.
