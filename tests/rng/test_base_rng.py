"""Tests targeting _BaseRNG's internal abstract-method safety net.

_BaseRNG is a private implementation-sharing base class, not part of the
public contract (see tests/rng/test_contract_parity.py for the public
contract itself). This test exists specifically to exercise the
NotImplementedError path that protects against a future RNG
implementation forgetting to override `_raw_draw`.
"""

import pytest

from rng.rng import _BaseRNG


def test_raw_draw_is_abstract_and_must_be_overridden() -> None:
    base = _BaseRNG()
    with pytest.raises(NotImplementedError):
        base._raw_draw(6)
