"""EXP-003 approved contract cases D1-D32 (CLUSTER-003 Slice E).

Canonical owner of the complete EXP-003 contract. No EXP-003 case belongs to
any other slice.

    runtime / executable       D1-D3, D6-D12, D16-D17, D22, D28, D30
    static / API-shape         D4, D5, D13-D15, D18-D21, D23-D27, D29,
                               D31, D32
                              ---
                               32

The static cases assert the **absence** of behaviour — a mapping roll, a
terrain modifier, an orchestration loop, a quantisation step — and must not
be dropped as "negative tests that pass trivially". Each is the executable
form of a boundary the approved card draws.

D28's integration drives the **real** landed DungeonTimeAccounting, never a
stub, following the CLUSTER-001 precedent.

A clearly separated implementation/coverage section follows at the end.
Those tests are NOT approved contract cases and must not be counted among
EXP-003's 32.
"""

import ast
import inspect
from fractions import Fraction

import pytest

from rules.character_creation.character_class import CharacterClass
from rules.character_creation.encumbrance_and_movement import (
    MovementMode,
    MovementRate,
    combat_movement,
    movement_rate,
    party_movement_rate,
)
from rules.character_creation.errors import MovementNotPermittedError
from rules.exploration import dungeon_movement
from rules.exploration.dungeon_movement import (
    DEFAULT_MAP_SCALE_FEET,
    GAME_TURN_CHECKLIST,
    DungeonMovementAllowance,
    turn_movement_allowance,
)
from rules.exploration.dungeon_turn_time_accounting import DungeonTimeAccounting
from rules.exploration.turn_credit import TurnCreditOrigin

CC = CharacterClass


def rate(encumbrance_cn: int, cls: CharacterClass = CC.FIGHTER, level: int = 1) -> MovementRate:
    return movement_rate(cls, level, encumbrance_cn)


# --- The rate used: D1-D6 --------------------------------------------------


@pytest.mark.parametrize(
    ("case", "encumbrance_cn", "feet"),
    [("D1", 0, 120), ("D2", 401, 90), ("D3", 2401, 0)],
    ids=lambda v: str(v),
)
def test_the_turn_allowance_is_the_partys_normal_speed(
    case: str, encumbrance_cn: int, feet: int
) -> None:
    """D1, D2, D3 — the allowance is the party's normal speed, in feet."""
    allowance = turn_movement_allowance(rate(encumbrance_cn))
    assert allowance.feet == feet


def test_d3_an_immobile_party_cannot_advance() -> None:
    """D3 — party normal speed 0': 0 feet; the party cannot advance."""
    allowance = turn_movement_allowance(rate(2401))
    assert allowance.feet == 0
    assert allowance.is_immobile
    assert allowance.squares() == 0


def test_d4_and_d5_encounter_and_running_speed_cannot_be_offered_as_the_rate() -> None:
    """D4, D5 — encounter or running speed offered as the exploration rate: ERROR.

    Structural: the argument is a whole MovementRate and only its normal
    speed is read, so there is no parameter through which either could be
    supplied. Asserted over the parsed function, so a later edit that starts
    reading .encounter or .running fails here.
    """
    assert list(inspect.signature(turn_movement_allowance).parameters) == ["party_rate"]
    source = ast.parse(inspect.getsource(turn_movement_allowance))
    attributes = {
        node.attr for node in ast.walk(source) if isinstance(node, ast.Attribute)
    }
    assert "normal" in attributes
    assert "encounter" not in attributes
    assert "running" not in attributes
    # A bare number is not a rate, whatever a caller meant it to be.
    with pytest.raises(ValueError, match="must be a MovementRate"):
        turn_movement_allowance(Fraction(40))  # type: ignore[arg-type]


def test_d6_normal_speed_is_refused_inside_the_combat_sequence() -> None:
    """D6 — normal speed requested inside the combat sequence: ERROR (Ch. 8 p. 103).

    The boundary runs both ways, and it is CHAR-005's to enforce. Driven
    here against the real implementation rather than restated.
    """
    with pytest.raises(MovementNotPermittedError, match="never used during the combat sequence"):
        combat_movement(rate(0), MovementMode.NORMAL)
    # And this card's allowance is the per-turn rate, not a combat rate.
    assert turn_movement_allowance(rate(0)).feet == rate(0).normal


# --- Map scale: D7-D11 -----------------------------------------------------


@pytest.mark.parametrize(
    ("case", "encumbrance_cn", "squares"),
    [("D7", 0, Fraction(12)), ("D8", 401, Fraction(9)), ("D9", 1601, Fraction(3, 2))],
    ids=lambda v: str(v),
)
def test_squares_at_the_default_scale(
    case: str, encumbrance_cn: int, squares: Fraction
) -> None:
    """D7, D8, D9 — 120' is 12 squares, 90' is 9, and 15' is 1.5 — unrounded."""
    assert DEFAULT_MAP_SCALE_FEET == 10
    assert turn_movement_allowance(rate(encumbrance_cn)).squares() == squares


def test_d9_a_fractional_square_count_is_not_rounded() -> None:
    """D9 — 15' at the default scale: 1.5 squares, NOT rounded by this card."""
    squares = turn_movement_allowance(rate(1601)).squares()
    assert squares == Fraction(3, 2)
    assert squares not in (1, 2)
    assert isinstance(squares, Fraction)


def test_d10_a_dm_configured_scale_changes_the_square_count() -> None:
    """D10 — 120' at a DM scale of 5' per square: 24 squares; the rate is still 120 feet."""
    allowance = turn_movement_allowance(rate(0))
    assert allowance.squares(5) == 24
    assert allowance.feet == 120


@pytest.mark.parametrize("scale_feet", [1, 5, 10, 20, 100])
def test_d11_a_configured_scale_never_changes_the_underlying_rate(scale_feet: int) -> None:
    """D11 — a configured map scale changing the rate in feet: MUST NOT OCCUR.

    The allowance is frozen and squares() is a pure read, so the scale
    reaches the square count and nothing else.
    """
    allowance = turn_movement_allowance(rate(0))
    before = allowance.feet
    allowance.squares(scale_feet)
    assert allowance.feet == before == 120
    assert allowance.squares(scale_feet) == Fraction(120, scale_feet)


# --- Mapping: D12-D17 ------------------------------------------------------


def test_d12_mapping_costs_no_additional_time() -> None:
    """D12 — party maps as it explores: no additional time cost.

    The allowance for a mapping party is the allowance for any party,
    because RC's rate already includes mapping.
    """
    assert turn_movement_allowance(rate(0)).feet == 120
    assert list(inspect.signature(turn_movement_allowance).parameters) == ["party_rate"]


def test_d13_d14_d15_no_mapping_mechanic_exists() -> None:
    """D13, D14, D15 — mapping roll, failure state, movement penalty: MUST NOT EXIST.

    RC's four mapping presentations were read in full during Stage A and
    none contains a die, a time cost or a failure state.
    """
    public = {name for name in vars(dungeon_movement) if not name.startswith("_")}
    forbidden = {
        "mapping_roll",
        "map_check",
        "MappingResult",
        "mapping_failed",
        "MAPPING_TIME_COST",
        "mapping_penalty",
        "mapper",
        "caller",
    }
    assert public & forbidden == set()
    # No RNG reaches this card at all — a mapping roll could not be made.
    module = ast.parse(inspect.getsource(dungeon_movement))
    imported = {
        node.module
        for node in ast.walk(module)
        if isinstance(node, ast.ImportFrom) and node.module is not None
    }
    assert not any("rng" in name for name in imported)


def test_d16_a_party_may_decline_to_appoint_a_mapper_or_caller() -> None:
    """D16 — party declines to appoint a mapper or caller: permitted.

    Neither is a game rule; RC says of the caller that "it's not a game rule
    that players have to use". Nothing here asks for either.
    """
    assert turn_movement_allowance(rate(0)).feet == 120
    parameters = set(inspect.signature(turn_movement_allowance).parameters)
    assert not parameters & {"mapper", "caller", "roles", "party"}


def test_d17_resting_and_peeking_are_already_included_in_the_rate() -> None:
    """D17 — resting or peeking around corners: already included; not charged again.

    Charging for them would double-count a cost RC's rate already contains,
    so there is no parameter and no deduction for either.
    """
    parameters = set(inspect.signature(turn_movement_allowance).parameters)
    assert not parameters & {"resting", "peeking", "actions", "deductions"}
    public = {name for name in vars(dungeon_movement) if not name.startswith("_")}
    assert not public & {"rest_cost", "peek_cost", "action_cost", "deduct"}


# --- Terrain: D18-D20 ------------------------------------------------------


def test_d18_and_d19_no_dungeon_terrain_modifier_exists() -> None:
    """D18, D19 — a dungeon terrain modifier on the turn or the round: MUST NOT EXIST.

    RC states the non-application positively: terrain "makes no difference
    to the combat round or the 10-minute turn".
    """
    public = {name for name in vars(dungeon_movement) if not name.startswith("_")}
    forbidden = {
        "terrain",
        "Terrain",
        "TERRAIN_MODIFIERS",
        "terrain_modifier",
        "rough_terrain",
        "broken_terrain",
        "difficult_terrain",
    }
    assert public & forbidden == set()
    assert "terrain" not in inspect.signature(turn_movement_allowance).parameters


def test_d20_the_overland_terrain_tables_do_not_reach_a_dungeon_turn() -> None:
    """D20 — overland terrain table applied to a dungeon turn: ERROR.

    Those tables are per-day and outdoor, both visually verified as such.
    Neither exists here, so neither can be applied.
    """
    public = {name for name in vars(dungeon_movement) if not name.startswith("_")}
    forbidden = {
        "TERRAIN_EFFECTS_ON_MOVEMENT",
        "TRAVELING_RATES_BY_TERRAIN",
        "travel_rate_per_day",
        "daily_travel_distance",
    }
    assert public & forbidden == set()


# --- The exploration loop: D21-D27 -----------------------------------------


def test_d21_the_checklist_has_four_steps_in_order() -> None:
    """D21 — four checklist steps, executed in order.

    Recorded as inert data. This card owns the movement spend at step 2 and
    no function here runs a step.
    """
    assert GAME_TURN_CHECKLIST == (
        "Wandering monsters",
        "Actions",
        "Results",
        "Wandering-monster check",
    )
    assert len(GAME_TURN_CHECKLIST) == 4


def test_d21_this_card_owns_no_loop() -> None:
    """D21 — the checklist is recorded, not run. No orchestration exists here."""
    public = {name for name in vars(dungeon_movement) if not name.startswith("_")}
    forbidden = {
        "explore",
        "run_turn",
        "game_turn",
        "next_turn",
        "ExplorationEngine",
        "TurnManager",
        "GameState",
        "Party",
        "Session",
    }
    assert public & forbidden == set()


def test_d22_and_d24_wandering_monsters_are_delegated() -> None:
    """D22, D24 — arrivals at step 1 and the step-4 check are EXP-001's and EXP-002's.

    2d6 x 10 feet, 1d6 every other turn, a dungeon encounter on a 1: none of
    it is restated here, and no RNG reaches this module.
    """
    assert GAME_TURN_CHECKLIST[0] == "Wandering monsters"
    assert GAME_TURN_CHECKLIST[3] == "Wandering-monster check"
    public = {name for name in vars(dungeon_movement) if not name.startswith("_")}
    forbidden = {
        "wandering_monster_check",
        "encounter_distance",
        "WANDERING_CHECK_INTERVAL_TURNS",
        "monsters_arrive",
    }
    assert public & forbidden == set()


def test_d23_a_wandering_monster_result_does_not_initiate_combat() -> None:
    """D23 — a wandering-monster result routes to the Encounter Checklist.

    It must not initiate combat directly. Nothing here decides that an
    encounter becomes a fight; surprise and reaction are ENC-002/ENC-003's.
    """
    public = {name for name in vars(dungeon_movement) if not name.startswith("_")}
    forbidden = {
        "begin_combat",
        "start_combat",
        "initiative",
        "surprise",
        "reaction",
        "attack",
        "Combat",
    }
    assert public & forbidden == set()


def test_d25_describing_a_new_area_is_a_dm_obligation_not_a_mechanic() -> None:
    """D25 — party enters a new area: the DM describes it so the mapper can map it."""
    assert GAME_TURN_CHECKLIST[2] == "Results"
    public = {name for name in vars(dungeon_movement) if not name.startswith("_")}
    assert not public & {"describe_area", "AreaDescription", "room_description"}


def test_d26_step_two_actions_are_declared_here_and_resolved_elsewhere() -> None:
    """D26 — listening, searching or opening a door: declared at step 2, resolved in EXP-005/007."""
    assert GAME_TURN_CHECKLIST[1] == "Actions"
    public = {name for name in vars(dungeon_movement) if not name.startswith("_")}
    forbidden = {"listen", "search", "open_door", "find_trap", "detect_trap"}
    assert public & forbidden == set()


def test_d27_the_exit_condition_is_the_dms_and_owns_no_state_here() -> None:
    """D27 — exit condition met: the exploration loop is left.

    The loop is not this card's, so neither is leaving it. Nothing here
    holds a "still exploring" flag to clear.
    """
    public = {name for name in vars(dungeon_movement) if not name.startswith("_")}
    forbidden = {"exit_condition", "is_exploring", "leave_loop", "in_dungeon"}
    assert public & forbidden == set()


# --- Integration: D28-D32 --------------------------------------------------


def test_d28_turn_credit_is_delegated_to_the_landed_exp_002() -> None:
    """D28 — turn credit consumed: delegated to landed EXP-002, not re-implemented.

    Drives the REAL DungeonTimeAccounting, never a stub. This module imports
    nothing from it; the two compose at the caller.
    """
    accounting = DungeonTimeAccounting()
    allowance = turn_movement_allowance(rate(0))

    credit = accounting.complete_ordinary_turn()
    assert credit.turn_number == 1
    assert credit.origin is TurnCreditOrigin.ORDINARY
    assert allowance.feet == 120
    assert allowance.squares() == 12

    second = accounting.complete_ordinary_turn()
    assert second.turn_number == 2
    # The allowance is per turn and is unchanged by time passing: it carries
    # no turn number and no elapsed time.
    assert turn_movement_allowance(rate(0)).feet == 120
    assert not hasattr(allowance, "turn_number")

    module = ast.parse(inspect.getsource(dungeon_movement))
    imported = {
        node.module
        for node in ast.walk(module)
        if isinstance(node, ast.ImportFrom) and node.module is not None
    }
    assert "rules.exploration.dungeon_turn_time_accounting" not in imported
    assert not any("turn_credit" in name for name in imported)


def test_d29_the_party_rate_is_delegated_to_char_005() -> None:
    """D29 — party rate derivation: CHAR-005 §8's slowest member, not re-derived here.

    turn_movement_allowance receives no encumbrance, class or level, so it
    cannot re-derive a rate even by accident. Driven against the real
    party_movement_rate.
    """
    party = [rate(0), rate(401), rate(801)]
    party_rate = party_movement_rate(party)
    assert party_rate.normal == 60

    allowance = turn_movement_allowance(party_rate)
    assert allowance.feet == 60
    assert allowance.squares() == 6

    parameters = set(inspect.signature(turn_movement_allowance).parameters)
    assert not parameters & {"encumbrance", "total_encumbrance_cn", "cls", "level"}


def test_d30_a_mystics_rate_flows_through_unaltered() -> None:
    """D30 — Mystic at MV 130', 0 cn, default scale: 130 feet; 13 squares."""
    mystic_rate = rate(0, CC.MYSTIC, 2)
    assert mystic_rate.normal == 130
    allowance = turn_movement_allowance(mystic_rate)
    assert allowance.feet == 130
    assert allowance.squares() == 13


def test_d30_a_genuinely_fractional_rate_also_flows_through_unaltered() -> None:
    """D30 — the fractional-rate case: nothing here touches the value.

    A Mystic's encounter rate is 43 1/3', and although this card uses normal
    speed, the same exactness must survive: a 15' rate is 1.5 squares.
    """
    assert turn_movement_allowance(rate(1601)).squares() == Fraction(3, 2)
    assert turn_movement_allowance(rate(1601)).squares(4) == Fraction(15, 4)


@pytest.mark.parametrize("scale_feet", [3, 4, 7, 9])
def test_d31_this_card_never_rounds_or_snaps_a_fractional_rate(scale_feet: int) -> None:
    """D31 — this card rounding or snapping a fractional rate: MUST NOT OCCUR."""
    allowance = turn_movement_allowance(rate(0))
    squares = allowance.squares(scale_feet)
    assert squares == Fraction(120, scale_feet)
    assert isinstance(squares, Fraction)
    module = ast.parse(inspect.getsource(dungeon_movement))
    for node in ast.walk(module):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in ("round", "int", "float")
        if isinstance(node, ast.Constant):
            assert not isinstance(node.value, float)


def test_d32_no_party_formation_input_exists() -> None:
    """D32 — EXP-010 party formation requested: not required; no formation input."""
    parameters = set(inspect.signature(turn_movement_allowance).parameters)
    assert not parameters & {"formation", "marching_order", "order", "front_rank"}
    public = {name for name in vars(dungeon_movement) if not name.startswith("_")}
    forbidden = {"MarchingOrder", "Formation", "party_formation", "marching_order"}
    assert public & forbidden == set()


# ===========================================================================
# Implementation and coverage tests below. NOT approved contract cases.
# ===========================================================================


def test_the_module_imports_only_what_it_consumes() -> None:
    module = ast.parse(inspect.getsource(dungeon_movement))
    imported = {
        node.module
        for node in ast.walk(module)
        if isinstance(node, ast.ImportFrom) and node.module is not None
    }
    assert imported == {
        "__future__",
        "dataclasses",
        "fractions",
        "typing",
        "rules.character_creation.encumbrance_and_movement",
    }


def test_an_allowance_is_immutable() -> None:
    import dataclasses

    allowance = turn_movement_allowance(rate(0))
    with pytest.raises(dataclasses.FrozenInstanceError):
        allowance.feet = Fraction(999)  # type: ignore[misc]


@pytest.mark.parametrize("bad", [120, "120", None, 1.5])
def test_an_allowance_cannot_be_built_from_a_non_fraction(bad: object) -> None:
    with pytest.raises(ValueError, match="must be a Fraction"):
        DungeonMovementAllowance(bad)  # type: ignore[arg-type]


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_allowance_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="must not be a bool"):
        DungeonMovementAllowance(bad)  # type: ignore[arg-type]


def test_a_negative_allowance_is_refused() -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        DungeonMovementAllowance(Fraction(-1))


@pytest.mark.parametrize("bad", [0, -1, -10])
def test_a_map_scale_that_is_not_positive_is_refused(bad: int) -> None:
    with pytest.raises(ValueError, match="scale_feet must be positive"):
        turn_movement_allowance(rate(0)).squares(bad)


@pytest.mark.parametrize("bad", [True, False])
def test_a_bool_map_scale_is_refused(bad: bool) -> None:
    with pytest.raises(ValueError, match="scale_feet must be an int"):
        turn_movement_allowance(rate(0)).squares(bad)


@pytest.mark.parametrize("bad", ["10", None, 10.0, Fraction(10)])
def test_a_non_int_map_scale_is_refused(bad: object) -> None:
    with pytest.raises(ValueError, match="scale_feet must be an int"):
        turn_movement_allowance(rate(0)).squares(bad)  # type: ignore[arg-type]


def test_the_checklist_is_a_tuple_and_cannot_be_mutated() -> None:
    assert isinstance(GAME_TURN_CHECKLIST, tuple)
    with pytest.raises(TypeError):
        GAME_TURN_CHECKLIST[0] = "x"  # type: ignore[index]
