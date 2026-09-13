"""CHAR-001 — Ability Score Generation (§1, §4, §6).

See docs/rules/character_creation/ability_score_generation.md (Status:
APPROVED, human-approved 2026-09-04, amended 2026-09-05 with trade rule R11
and cases C1-C5) for the governing Rule Card, and
docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §7.7 for the approved
implementation contract this module implements (Slice D).

Four independent pure operations. Each takes values and returns values.

THE CANONICAL CALLING SEQUENCE — STATED, NOT OWNED
--------------------------------------------------
The Rule Card's §0 ordering is **rules ordering only. It specifies no
orchestration object, and none may be inferred from it.** The sequence is::

    generate_ability_scores
        -> optional discard decision          (§6.1, SR-4)
        -> optional AUTHORIZED switch         (§6.2, SR-3)
        -> eligibility evaluation and class choice   (CHAR-002)
        -> optional atomic 2-for-1 trades     (§4, R1-R11)

**This module does not orchestrate that sequence.** It exposes four
functions a caller invokes in that order; it holds no state between them,
and it cannot observe where in the sequence it is being called.

Four approved cases are therefore **calling contracts**, not runtime
branches (implementation plan §12.2.1), and no state is added to make them
observable:

    T11  The trade is optional. Not invoking apply_trade leaves the
         immutable AbilityScores unchanged — R8 is a caller contract.
    W2   Authorization is external. An unauthorized switch means
         apply_highest_score_switch is simply not called.
    W6   The operation performs one two-score swap; that a caller
         authorizes AT MOST ONE switch is the caller's obligation, which a
         stateless function cannot observe.
    D7   discard_may_be_offered returns permission to OFFER. It never
         forces a discard, and the player may retain the character.

It does not, and must not, own:

- class selection, or the eligibility procedure (CHAR-002 — this module
  consumes its prime-requisite and creation-minimum tables and duplicates
  neither);
- player or DM policy: whether a discard is offered or accepted, and
  whether a switch is authorized, are decisions above this module;
- creation state, phase, session or completion. R9's time-boxing and the
  sequencing cases S2, W7, O1-O4 are correspondingly not observable here;
- Chapter 10 above-1st-level generation (§5) — a separate module, Slice E,
  which this module must never import (approved case H6);
- hit points (CHAR-003), ability-score effects (CHAR-007), starting money
  (CHAR-004), alignment, languages, height and weight (CHAR-008), or
  experience and advancement (ADV-001, ADV-002).
"""

from __future__ import annotations

from rng import RNG
from rules.character_creation.ability import Ability, AbilityScores
from rules.character_creation.character_class import CharacterClass
from rules.character_creation.errors import (
    ClassMinimumViolationError,
    IllegalSwitchError,
    IllegalTradeError,
    PrimeRequisiteCeilingError,
)
from rules.character_creation.race_and_class_eligibility import (
    creation_minimums,
    prime_requisites,
)

__all__ = [
    "apply_highest_score_switch",
    "apply_trade",
    "discard_may_be_offered",
    "generate_ability_scores",
]


_GENERATION_EXPRESSION = "3d6"
"""RC p. 6: "Roll 3d6 for each ability" (card §1)."""

_DISCARD_MAXIMUM = 9
"""SR-4's first predicate: a discard may be offered when no score is ABOVE
9. The boundary matters — 9 is not above 9 (approved case D6)."""

_DISCARD_LOW_SCORE = 6
"""SR-4's second predicate threshold: scores BELOW 6. The boundary matters
— 6 is not below 6 (approved case D5)."""

_DISCARD_LOW_SCORE_COUNT = 2
"""SR-4's second predicate: at least two scores below 6."""

_TRADE_DONOR_COST = 2
"""The donor gives up two points per trade (card §4)."""

_TRADE_TARGET_GAIN = 1
"""The target gains one point per trade — the 2:1 rate, identical for every
class; no class-specific rate exists (approved case M5)."""

_TRADE_DONOR_FLOOR = 9
"""R6: after the trade the donor must be at least 9. R7 is the same rule
restated at the boundary — a donor already at 10 or less cannot be
lowered, because 10 - 2 = 8 (card §4)."""

_TRADE_TARGET_CEILING = 18
"""R11: the target may not exceed 18. A Necessary Mechanical Consequence of
RC's standing range limitation for ability scores (RC p. 6; p. 130), NOT
RC-explicit at p. 7 and NOT a Simulator Ruling (card §4)."""

_UNEXCHANGEABLE_DONORS = frozenset({Ability.CONSTITUTION, Ability.CHARISMA})
"""R3: Constitution and Charisma points cannot be exchanged with others."""


def generate_ability_scores(rng: RNG) -> AbilityScores:
    """Roll the six ability scores in place (card §1).

    One ``3d6`` expression per ability, in the Rules Cyclopedia's own
    declaration order, each recorded against the ability it was rolled
    for. Exactly **18 d6 draws** and six roll sequence numbers are
    consumed (approved case G5).

    **No reroll, discard, sorting, reassignment, drop-lowest, switch or
    trade occurs here.** Assignment follows roll order, never sorted order
    (approved case G4); every other provision is a separate operation a
    caller invokes afterwards.
    """
    rolled = [rng.roll(_GENERATION_EXPRESSION).total for _ in Ability]
    return AbilityScores(
        rolled[0], rolled[1], rolled[2], rolled[3], rolled[4], rolled[5]
    )


def discard_may_be_offered(scores: AbilityScores) -> bool:
    """Whether a discard **may be offered** for ``scores`` (§6.1, SR-4).

    RC states the condition twice, non-equivalently; SR-4 adopts the
    detailed formulation::

        no ability score is above 9
                OR
        at least two ability scores are below 6

    Both boundaries are exclusive as written: **9 is not above 9** and
    **6 is not below 6** (approved cases D5, D6).

    Returns permission only. It discards nothing, rerolls nothing, and
    does not decide whether the player accepts — *"a player might want to
    play this character; if he does, let him."* The retention decision is
    the caller's (approved case D7, a calling contract).
    """
    low_scores = sum(
        1 for ability in Ability if scores[ability] < _DISCARD_LOW_SCORE
    )
    return (
        scores.maximum() <= _DISCARD_MAXIMUM
        or low_scores >= _DISCARD_LOW_SCORE_COUNT
    )


def apply_highest_score_switch(
    scores: AbilityScores,
    target_class: CharacterClass,
    source_ability: Ability,
    target_prime_requisite: Ability,
) -> AbilityScores:
    """Perform an **already-authorized** Chapter 13 switch (§6.2, §6.2.1).

    RC: *"Just switch the highest score rolled for the character to the
    Prime Requisite ability appropriate to the class the player wants."*
    This is a **swap of two scores**, not a free rearrangement: exactly
    the two named abilities exchange values and nothing else changes.

    Both ends are supplied explicitly. The destination must be, because
    three classes carry two prime requisites (Elf, Halfling, Mystic) and
    "the prime requisite appropriate to the class" does not name a unique
    one. The source must be, because **where several abilities tie for the
    maximum, any tied maximum may be the authorized source** — the DM or
    simulation policy chooses, and **no ability-order, alphabetical or
    random tie-break exists here** (§6.2.1).

    Validates, at operation level:

    - ``source_ability`` currently holds the maximum score;
    - ``target_prime_requisite`` is a prime requisite of ``target_class``,
      read from CHAR-002, which owns that table;
    - the two are different abilities — naming one twice is not a swap of
      two scores.

    **Authorization itself is not decided here** (approved case W2), and
    **that at most one switch is authorized is a caller obligation this
    stateless function cannot observe** (approved case W6).
    """
    if scores[source_ability] != scores.maximum():
        raise IllegalSwitchError(
            f"the switch moves the highest rolled score; "
            f"{source_ability.name} holds {scores[source_ability]}, not the "
            f"maximum {scores.maximum()}"
        )
    if target_prime_requisite not in prime_requisites(target_class):
        raise IllegalSwitchError(
            f"the switch destination must be a prime requisite of "
            f"{target_class.name}; {target_prime_requisite.name} is not"
        )
    if source_ability is target_prime_requisite:
        raise IllegalSwitchError(
            f"the switch is a swap of two scores; {source_ability.name} was "
            f"named as both source and destination"
        )
    return scores.replace(
        {
            source_ability: scores[target_prime_requisite],
            target_prime_requisite: scores[source_ability],
        }
    )


def apply_trade(
    scores: AbilityScores,
    chosen_class: CharacterClass,
    donor: Ability,
    target: Ability,
) -> AbilityScores:
    """Perform **one** 2-for-1 prime-requisite trade (§4, rules R1-R11).

    Exactly one atomic exchange::

        score(donor)  -= 2
        score(target) += 1

    RC permits *"this trade as many times as you want"*; **the caller
    controls how many occur** by invoking this function repeatedly. There
    is deliberately no amount, count, repeat or maximize parameter, and no
    production helper loops it — RC's own worked example at p. 7 (approved
    cases T13, C5) is three calls, not one call of size three.

    Rules enforced, in this order, so each approved case observes the rule
    it names:

    ``R1``/``R2``
        ``target`` must be a prime requisite of ``chosen_class``. Classes
        with two prime requisites may target either; that needs no special
        branch, because CHAR-002's table is the authority.
    ``R5``
        ``donor`` and ``target`` must differ — only the target is raised,
        and §4's ``score(D) -= 2; score(T) += 1`` treats them as distinct
        operands.
    ``R3``
        ``donor`` may be neither Constitution nor Charisma.
    ``R4``
        ``donor`` may not be Dexterity. This bars **lowering** Dexterity
        only; raising it where it is a prime requisite is legal, which is
        what SR-2 turns on (approved cases T8, M1, M3).
    ``R6``/``R7``
        after the trade the donor must be at least 9. Checked **before**
        R11, because approved case T14 rejects on the donor floor even
        though its target would also breach the ceiling.
    ``R11``
        after the trade the target must be at most 18. Evaluated on the
        prospective value **before any result is constructed**, so C2 and
        C4 observe :class:`PrimeRequisiteCeilingError` and never the
        value object's own guard.
    ``R10``
        every creation minimum of ``chosen_class`` must still be
        satisfied, read from CHAR-002. This **preserves** eligibility
        already established; it never lets a trade establish it.

    ``R8`` (the trade is optional) and ``R9`` (it happens at this step
    only) are caller contracts — approved cases T11 and S2 — and no flag
    or phase parameter is added for either.
    """
    if target not in prime_requisites(chosen_class):
        raise IllegalTradeError(
            f"R1: only a prime requisite may be raised; {target.name} is not "
            f"a prime requisite of {chosen_class.name}"
        )
    if donor is target:
        raise IllegalTradeError(
            f"R5: only the target is raised; {donor.name} was named as both "
            f"donor and target"
        )
    if donor in _UNEXCHANGEABLE_DONORS:
        raise IllegalTradeError(
            f"R3: Constitution and Charisma points cannot be exchanged; "
            f"{donor.name} was named as donor"
        )
    if donor is Ability.DEXTERITY:
        raise IllegalTradeError(
            "R4: Dexterity cannot be lowered (it may still be raised where "
            "it is a prime requisite)"
        )

    lowered = scores[donor] - _TRADE_DONOR_COST
    if lowered < _TRADE_DONOR_FLOOR:
        raise IllegalTradeError(
            f"R6/R7: no score may be lowered below {_TRADE_DONOR_FLOOR}; "
            f"{donor.name} at {scores[donor]} would become {lowered}"
        )

    raised = scores[target] + _TRADE_TARGET_GAIN
    if raised > _TRADE_TARGET_CEILING:
        raise PrimeRequisiteCeilingError(
            f"R11: a trade may not raise its target above "
            f"{_TRADE_TARGET_CEILING}; {target.name} at {scores[target]} "
            f"would become {raised}"
        )

    adjusted = scores.replace({donor: lowered, target: raised})
    for ability, minimum in creation_minimums(chosen_class).items():
        if adjusted[ability] < minimum:
            raise ClassMinimumViolationError(
                f"R10: {chosen_class.name} requires {ability.name} "
                f"{minimum} or better at creation; the trade would leave "
                f"{adjusted[ability]}"
            )
    return adjusted
