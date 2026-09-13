"""CHAR-003 approved contract cases H1-H42.

Canonical owner of the complete CHAR-003 contract, per
docs/technical/CLUSTER-002_IMPLEMENTATION_PLAN.md §12's ownership ledger.
No CHAR-003 case belongs to any other slice.

    runtime / executable   40   H1-H35, H37, H39-H42
    static / API-shape      1   H36
    calling-contract        1   H38   -- no pytest function; see below
                           ---
                            42

H38 ("any attempt to reroll a hit-point die -> rejected") is a documented
calling-contract case. hit_point_gain is stateless, so a repeat invocation
for an already-resolved level is indistinguishable from a first one without
character or advancement state, which the approved plan forbids adding
(§4.1, §12.3.1). It therefore receives no ceremonial pytest function. Its
evidence is the module's roll-once contract statement, the executable tests
below proving one rolled level consumes exactly one die with no internal
retry, and the ISSUE-010 completion-record checklist.

Test names are qualified with ``char003`` because CHAR-001 also has
H-numbered cases, in a different module (plan §11).

A clearly separated implementation/coverage section follows at the end.
Those tests are NOT approved contract cases and must not be counted among
the 189.
"""

import ast
import inspect

import pytest

from rng import RollSequenceExhaustedError, ScriptedRNG
from rules.character_creation import hit_points_and_hit_dice
from rules.character_creation.character_class import CharacterClass
from rules.character_creation.errors import (
    AbilityScoreDomainError,
    CharacterCreationError,
    HitDieNotApplicableError,
    HitPointLevelError,
)
from rules.character_creation.hit_points_and_hit_dice import hit_point_gain

# Constitution scores chosen for the adjustment each produces (RC p. 9).
_CON_MINUS_3 = 3
_CON_MINUS_2 = 5
_CON_MINUS_1 = 8
_CON_ZERO = 10
_CON_PLUS_1 = 13
_CON_PLUS_3 = 18


def _span(
    cls: CharacterClass,
    levels: range,
    constitution: int,
    rolls: list[int] | None = None,
) -> int:
    """Total hit points gained over ``levels``, one invocation per level."""
    rng = ScriptedRNG(rolls if rolls is not None else [])
    return sum(
        hit_point_gain(rng, cls, level, constitution) for level in levels
    )


def _assert_queue_exhausted(rng: ScriptedRNG) -> None:
    """Prove an exact-length queue was consumed exactly, with none left."""
    with pytest.raises(RollSequenceExhaustedError):
        rng.roll_die(6)


def _imported_modules() -> set[str]:
    """Every module name this card's source imports, from its own AST."""
    tree = ast.parse(inspect.getsource(hit_points_and_hit_dice))
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            names.add(node.module)
    return names


# --- First level ---------------------------------------------------------


def test_char003_h1_fighter_con_0_d8_5() -> None:
    assert hit_point_gain(ScriptedRNG([5]), CharacterClass.FIGHTER, 1, _CON_ZERO) == 5


def test_char003_h2_fighter_con_plus_3_d8_8() -> None:
    assert (
        hit_point_gain(ScriptedRNG([8]), CharacterClass.FIGHTER, 1, _CON_PLUS_3) == 11
    )


def test_char003_h3_magic_user_con_minus_3_d4_1_floors_at_1() -> None:
    # 1 - 3 = -2; the floor gives 1, not -2.
    assert (
        hit_point_gain(ScriptedRNG([1]), CharacterClass.MAGIC_USER, 1, _CON_MINUS_3)
        == 1
    )


def test_char003_h4_magic_user_con_minus_3_d4_4_is_already_1() -> None:
    # 4 - 3 = 1; the arithmetic result is already 1 and the floor does not
    # change it.
    assert (
        hit_point_gain(ScriptedRNG([4]), CharacterClass.MAGIC_USER, 1, _CON_MINUS_3)
        == 1
    )


def test_char003_h5_magic_user_con_minus_2_d4_1_floors_at_1() -> None:
    assert (
        hit_point_gain(ScriptedRNG([1]), CharacterClass.MAGIC_USER, 1, _CON_MINUS_2)
        == 1
    )


def test_char003_h6_cleric_con_minus_1_d6_1_floors_at_1() -> None:
    assert (
        hit_point_gain(ScriptedRNG([1]), CharacterClass.CLERIC, 1, _CON_MINUS_1) == 1
    )


def test_char003_h7_cleric_con_plus_1_d6_1_floor_not_engaged() -> None:
    assert hit_point_gain(ScriptedRNG([1]), CharacterClass.CLERIC, 1, _CON_PLUS_1) == 2


def test_char003_h8_thief_con_0_d4_4() -> None:
    assert hit_point_gain(ScriptedRNG([4]), CharacterClass.THIEF, 1, _CON_ZERO) == 4


# --- Per-roll floor ------------------------------------------------------


def test_char003_h9_floor_applies_per_roll_not_to_the_total() -> None:
    # Not 3 - 9, and not floored once at 1: 1 per level, three levels.
    assert (
        _span(CharacterClass.MAGIC_USER, range(1, 4), _CON_MINUS_3, [1, 1, 1]) == 3
    )


def test_char003_h10_each_roll_floors_independently() -> None:
    assert (
        _span(CharacterClass.MAGIC_USER, range(1, 4), _CON_MINUS_3, [4, 4, 4]) == 3
    )


def test_char003_h11_mixed_rolls_still_floor_independently() -> None:
    assert (
        _span(CharacterClass.MAGIC_USER, range(1, 4), _CON_MINUS_3, [4, 1, 4]) == 3
    )


# --- Rolling ceiling -----------------------------------------------------


def test_char003_h12_fighter_1_to_12_consumes_exactly_9_dice() -> None:
    rng = ScriptedRNG([5] * 9)
    gains = [
        hit_point_gain(rng, CharacterClass.FIGHTER, level, _CON_ZERO)
        for level in range(1, 13)
    ]
    # Levels 1-9 rolled; levels 10, 11, 12 consumed no dice.
    assert gains[:9] == [5] * 9
    assert gains[9:] == [2, 2, 2]
    _assert_queue_exhausted(rng)


def test_char003_h13_halfling_1_to_8_consumes_exactly_8_dice() -> None:
    rng = ScriptedRNG([6] * 8)
    gains = [
        hit_point_gain(rng, CharacterClass.HALFLING, level, _CON_ZERO)
        for level in range(1, 9)
    ]
    assert gains == [6] * 8
    _assert_queue_exhausted(rng)


def test_char003_h14_halfling_gains_nothing_past_level_8() -> None:
    # Maximum level equals Name level: there is no fixed-gain band, and no
    # further hit points come from any source this card owns.
    with pytest.raises(HitPointLevelError):
        hit_point_gain(ScriptedRNG([]), CharacterClass.HALFLING, 9, _CON_ZERO)


def test_char003_h15_elf_1_to_10_is_nine_rolls_then_one_fixed_gain() -> None:
    rng = ScriptedRNG([6] * 9)
    gains = [
        hit_point_gain(rng, CharacterClass.ELF, level, _CON_ZERO)
        for level in range(1, 11)
    ]
    assert gains[:9] == [6] * 9
    assert gains[9] == 2
    _assert_queue_exhausted(rng)


# --- Fixed gains and the Constitution cut-off ----------------------------


def test_char003_h16_fighter_levels_10_to_12_ignore_a_plus_3_constitution() -> None:
    # +6 total (2 per level), not +15.
    assert _span(CharacterClass.FIGHTER, range(10, 13), _CON_PLUS_3) == 6


def test_char003_h17_dwarf_levels_10_to_12_ignore_a_minus_3_constitution() -> None:
    # +9 total (3 per level), not 0 -- the penalty does not apply either.
    assert _span(CharacterClass.DWARF, range(10, 13), _CON_MINUS_3) == 9


def test_char003_h18_cleric_levels_10_to_36() -> None:
    assert _span(CharacterClass.CLERIC, range(10, 37), _CON_ZERO) == 27


def test_char003_h19_mystic_levels_10_to_16() -> None:
    assert _span(CharacterClass.MYSTIC, range(10, 17), _CON_ZERO) == 14


def test_char003_h20_dwarf_gains_nothing_past_level_12() -> None:
    with pytest.raises(HitPointLevelError):
        hit_point_gain(ScriptedRNG([]), CharacterClass.DWARF, 13, _CON_ZERO)


def test_char003_h21_thief_levels_10_to_36_gain_2_per_level_not_1() -> None:
    assert _span(CharacterClass.THIEF, range(10, 37), _CON_ZERO) == 54


# --- The Elf fixed gain — Simulator Ruling SR-1 (+2) ---------------------


def test_char003_h22_elf_9_to_10_gains_2_unmodified_by_constitution() -> None:
    for constitution in (_CON_MINUS_3, _CON_ZERO, _CON_PLUS_3):
        assert (
            hit_point_gain(ScriptedRNG([]), CharacterClass.ELF, 10, constitution) == 2
        )


def test_char003_h23_elf_maximum_total_is_83() -> None:
    # 54 (nine d6 at 6) + 27 (Con +3 per roll) + 2 (SR-1) -- matches RC
    # p. 129's printed total.
    rolled = _span(CharacterClass.ELF, range(1, 10), _CON_PLUS_3, [6] * 9)
    total = rolled + hit_point_gain(ScriptedRNG([]), CharacterClass.ELF, 10, _CON_PLUS_3)
    assert rolled == 81
    assert total == 83


def test_char003_h24_elf_gains_nothing_past_level_10() -> None:
    with pytest.raises(HitPointLevelError):
        hit_point_gain(ScriptedRNG([]), CharacterClass.ELF, 11, _CON_ZERO)


def test_char003_h25_sr_1_reversal_guard() -> None:
    # The rejected reading's values are +1 and 82. If SR-1 is ever
    # revisited, this test and H22/H23 must invert together -- a reversal
    # must be a deliberate ruling change, never a silent drift.
    gain = hit_point_gain(ScriptedRNG([]), CharacterClass.ELF, 10, _CON_ZERO)
    assert gain == 2
    assert gain != 1
    total = _span(CharacterClass.ELF, range(1, 10), _CON_PLUS_3, [6] * 9) + gain
    assert total == 83
    assert total != 82


def test_char003_h26_elf_1_to_9_is_unaffected_by_sr_1() -> None:
    # Nine d6 rolls, Constitution applied per roll, floor per roll.
    rng = ScriptedRNG([1] * 9)
    gains = [
        hit_point_gain(rng, CharacterClass.ELF, level, _CON_PLUS_1)
        for level in range(1, 10)
    ]
    assert gains == [2] * 9
    _assert_queue_exhausted(rng)


def test_char003_h27_elf_floored_rolls_plus_the_fixed_gain() -> None:
    # 9 (floor, 1 per roll) + 2 = 11. The floor governs the rolls; SR-1's
    # fixed gain is added unmodified.
    rolled = _span(CharacterClass.ELF, range(1, 10), _CON_MINUS_3, [1] * 9)
    assert rolled == 9
    assert (
        rolled + hit_point_gain(ScriptedRNG([]), CharacterClass.ELF, 10, _CON_MINUS_3)
        == 11
    )


# --- Maximum-total regressions (RC p. 129) -------------------------------


def test_char003_h28_fighter_maximum_total_is_153() -> None:
    rolled = _span(CharacterClass.FIGHTER, range(1, 10), _CON_PLUS_3, [8] * 9)
    fixed = _span(CharacterClass.FIGHTER, range(10, 37), _CON_PLUS_3)
    assert (rolled, fixed, rolled + fixed) == (99, 54, 153)


def test_char003_h29_cleric_maximum_total_is_108() -> None:
    rolled = _span(CharacterClass.CLERIC, range(1, 10), _CON_PLUS_3, [6] * 9)
    fixed = _span(CharacterClass.CLERIC, range(10, 37), _CON_PLUS_3)
    assert (rolled, fixed, rolled + fixed) == (81, 27, 108)


def test_char003_h30_magic_user_maximum_total_is_90() -> None:
    rolled = _span(CharacterClass.MAGIC_USER, range(1, 10), _CON_PLUS_3, [4] * 9)
    fixed = _span(CharacterClass.MAGIC_USER, range(10, 37), _CON_PLUS_3)
    assert (rolled, fixed, rolled + fixed) == (63, 27, 90)


def test_char003_h31_thief_maximum_total_is_117() -> None:
    rolled = _span(CharacterClass.THIEF, range(1, 10), _CON_PLUS_3, [4] * 9)
    fixed = _span(CharacterClass.THIEF, range(10, 37), _CON_PLUS_3)
    assert (rolled, fixed, rolled + fixed) == (63, 54, 117)


def test_char003_h32_dwarf_maximum_total_is_108() -> None:
    rolled = _span(CharacterClass.DWARF, range(1, 10), _CON_PLUS_3, [8] * 9)
    fixed = _span(CharacterClass.DWARF, range(10, 13), _CON_PLUS_3)
    assert (rolled, fixed, rolled + fixed) == (99, 9, 108)


def test_char003_h33_halfling_maximum_total_is_72() -> None:
    # 48 (eight d6 at 6) + 24 (Con +3 over eight rolls); no fixed gains.
    assert _span(CharacterClass.HALFLING, range(1, 9), _CON_PLUS_3, [6] * 8) == 72


def test_char003_h34_cleric_at_level_15_is_87() -> None:
    rolled = _span(CharacterClass.CLERIC, range(1, 10), _CON_PLUS_3, [6] * 9)
    fixed = _span(CharacterClass.CLERIC, range(10, 16), _CON_PLUS_3)
    assert rolled + fixed == 87


def test_char003_h35_cleric_at_level_25_is_97() -> None:
    rolled = _span(CharacterClass.CLERIC, range(1, 10), _CON_PLUS_3, [6] * 9)
    fixed = _span(CharacterClass.CLERIC, range(10, 26), _CON_PLUS_3)
    assert rolled + fixed == 97


# --- Dependency and prohibitions -----------------------------------------


def test_char003_h36_no_constitution_adjustment_can_be_injected() -> None:
    # STATIC / API-SHAPE CONFORMANCE. The public operation's parameters are
    # exactly these four; there is no adjustment/modifier injection point,
    # so this card cannot produce an authoritative value without CHAR-007.
    parameters = inspect.signature(hit_point_gain).parameters
    assert list(parameters) == ["rng", "cls", "level", "constitution"]
    assert not [
        name
        for name in parameters
        if any(word in name.lower() for word in ("adjust", "modifier", "bonus"))
    ]
    # And the dependency is real: CHAR-007 is imported and consulted.
    assert any(
        "ability_score_effects" in module for module in _imported_modules()
    )


def test_char003_h37_constitution_9_to_12_adds_nothing() -> None:
    for constitution in (9, 12):
        assert (
            _span(CharacterClass.CLERIC, range(1, 10), constitution, [6] * 9) == 54
        )


# H38 -- DOCUMENTED CALLING-CONTRACT CONFORMANCE, no pytest function.
# See this module's docstring and ISSUE-010. The executable evidence that a
# rolled level consumes exactly one die with no internal retry is carried by
# H12, H13, H15 and H26 above, each of which uses an exact-length
# ScriptedRNG queue that fails loudly on an extra draw.


def test_char003_h39_druid_has_no_hit_die_at_first_level() -> None:
    with pytest.raises(HitDieNotApplicableError):
        hit_point_gain(ScriptedRNG([6]), CharacterClass.DRUID, 1, _CON_ZERO)


def test_char003_h40_druid_from_cleric_at_9th_then_plus_1_per_level() -> None:
    # Cleric progression to that point: the levels are requested as CLERIC,
    # because that is what the character is.
    rolled = _span(CharacterClass.CLERIC, range(1, 10), _CON_ZERO, [6] * 9)
    assert rolled == 54
    # Then +1 per level as a druid, with no die and no Constitution.
    assert hit_point_gain(ScriptedRNG([]), CharacterClass.DRUID, 10, _CON_ZERO) == 1
    assert _span(CharacterClass.DRUID, range(10, 37), _CON_ZERO) == 27


def test_char003_h41_chapter_19_variant_figures_are_not_used() -> None:
    # The Chapter 19 extended progression is NOT ENABLED for V1 and its
    # per-level figures differ: it gives the dwarf 2 per level, the core
    # rules 3.
    assert hit_point_gain(ScriptedRNG([]), CharacterClass.DWARF, 10, _CON_ZERO) == 3
    assert hit_point_gain(ScriptedRNG([]), CharacterClass.DWARF, 10, _CON_ZERO) != 2


def test_char003_h42_chapter_19_extended_table_is_not_used_for_the_elf() -> None:
    # The variant would extend demihumans past their core maxima. The Elf
    # stops at 10 with the SR-1 gain; there is no 11-36 progression here,
    # and the variant played no part in SR-1.
    assert hit_point_gain(ScriptedRNG([]), CharacterClass.ELF, 10, _CON_ZERO) == 2
    with pytest.raises(HitPointLevelError):
        hit_point_gain(ScriptedRNG([]), CharacterClass.ELF, 11, _CON_ZERO)


# =========================================================================
# Implementation / coverage tests — NOT approved contract cases.
# =========================================================================


def test_level_below_1_is_rejected() -> None:
    for level in (0, -1):
        with pytest.raises(HitPointLevelError):
            hit_point_gain(ScriptedRNG([]), CharacterClass.FIGHTER, level, _CON_ZERO)


def test_bool_is_rejected_as_a_level() -> None:
    # bool is a subtype of int, so static typing alone permits these and
    # True would otherwise be read as level 1. No type: ignore is needed
    # here, which is exactly why the runtime guard exists.
    for level in (True, False):
        with pytest.raises(HitPointLevelError, match="must not be a bool"):
            hit_point_gain(ScriptedRNG([6]), CharacterClass.FIGHTER, level, _CON_ZERO)


def test_non_integer_level_is_rejected_and_never_coerced() -> None:
    for level in (1.5, "1", None):
        with pytest.raises(HitPointLevelError, match="must be an int"):
            hit_point_gain(
                ScriptedRNG([6]),
                CharacterClass.FIGHTER,
                level,  # type: ignore[arg-type]
                _CON_ZERO,
            )


def test_druid_has_no_hit_die_at_any_rolled_level() -> None:
    # A necessary consequence of "does not apply", which the card states
    # without qualification. H39 names level 1; no Druid rolled level has a
    # defined die.
    for level in range(1, 10):
        with pytest.raises(HitDieNotApplicableError):
            hit_point_gain(ScriptedRNG([6]), CharacterClass.DRUID, level, _CON_ZERO)


def test_druid_past_its_maximum_is_a_level_rejection_not_a_hit_die_rejection() -> None:
    with pytest.raises(HitPointLevelError):
        hit_point_gain(ScriptedRNG([]), CharacterClass.DRUID, 37, _CON_ZERO)


def test_rolled_branch_propagates_char_007_domain_rejection_unchanged() -> None:
    # CHAR-007 owns the accepted adjustment domain (2-18). A score outside
    # it is rejected there, and that rejection is not caught or
    # reinterpreted here.
    with pytest.raises(AbilityScoreDomainError):
        hit_point_gain(ScriptedRNG([5]), CharacterClass.FIGHTER, 1, 19)


def test_fixed_branch_never_consults_constitution_at_all() -> None:
    # A Constitution CHAR-007 would reject does not matter on the fixed
    # branch, because the branch does not call CHAR-007.
    assert hit_point_gain(ScriptedRNG([]), CharacterClass.FIGHTER, 10, 19) == 2
    assert hit_point_gain(ScriptedRNG([]), CharacterClass.CLERIC, 10, 1) == 1


def test_every_fixed_gain_level_consumes_zero_dice() -> None:
    for cls, level in (
        (CharacterClass.CLERIC, 10),
        (CharacterClass.FIGHTER, 10),
        (CharacterClass.MAGIC_USER, 10),
        (CharacterClass.THIEF, 10),
        (CharacterClass.DWARF, 12),
        (CharacterClass.ELF, 10),
        (CharacterClass.MYSTIC, 16),
        (CharacterClass.DRUID, 36),
    ):
        # An empty queue raises on any draw, so reaching a value proves none.
        assert hit_point_gain(ScriptedRNG([]), cls, level, _CON_ZERO) >= 1


def test_public_surface_is_one_operation() -> None:
    assert list(hit_points_and_hit_dice.__all__) == ["hit_point_gain"]


def test_no_advancement_api_is_exported() -> None:
    exported = {
        name for name in dir(hit_points_and_hit_dice) if not name.startswith("_")
    }
    assert not [
        name
        for name in exported
        if any(
            word in name.lower()
            for word in ("maximum_level", "name_level", "progression", "advancement")
        )
    ]


def test_hit_point_errors_are_character_creation_errors() -> None:
    assert issubclass(HitPointLevelError, CharacterCreationError)
    assert issubclass(HitDieNotApplicableError, CharacterCreationError)


def test_only_the_rng_protocol_and_char_007_are_imported() -> None:
    modules = _imported_modules()
    assert "rng" in modules
    assert not [
        module
        for module in modules
        if module == "random"
        or "race_and_class_eligibility" in module
        or "ability_score_generation" in module
        or "rules.exploration" in module
    ]


def test_no_concrete_rng_implementation_is_imported() -> None:
    tree = ast.parse(inspect.getsource(hit_points_and_hit_dice))
    imported_names = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
        for alias in node.names
    }
    assert "RNG" in imported_names
    assert not {"SeededRNG", "ScriptedRNG"} & imported_names
