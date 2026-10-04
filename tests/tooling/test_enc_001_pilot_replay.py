"""Replay of the ENC-001 DEC-0012 pilot against the corrected mechanism.

**These tests derive from the real repository**, not from hand-built fixtures:
the actual `docs/rules/evidence/ENC-005-evidence*.md` accepted packets and the
actual `docs/rules/INVENTORY.md`. That is the point. The first implementation's
replay inserted p. 98 into a fixture and then asserted it was required, which
proved nothing -- a page does not count as externally derived because the test
put it there.

Nothing here reads or modifies the frozen ENC-001 packet on its own branch.

What the pilot found, and what is replayed:

* Review #1 `B-1`  -- RC p. 98 `Contact` never enumerated. ENC-005's accepted
  packet cites p. 98; the researcher read line 147 of that file and not 146.
* Review #2 `BLOCKING-2` -- RC p. 100 `Evasion at Sea`, a visibility-conditioned
  distance, never enumerated.
* Review #2 `BLOCKING-1` -- a categorical coverage claim covering six
  uninspected pages.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))

from lint_evidence import (  # noqa: E402
    RepoContext,
    cited_pages,
    derive_external_seeds,
    inventory_neighbours,
)

# The pages the pilot's pass 1 actually inspected in Ch. 7 and its neighbours.
PILOT_PASS_1 = {24, 25, 26, 27, 87, 91, 92, 93, 95}

# The pages the two independent reviews found missing.
PILOT_MISSED = {88, 94, 96, 97, 98, 99, 100, 102, 103}


@pytest.fixture(scope="module")
def repo() -> RepoContext:
    return RepoContext.default()


def test_the_real_inventory_reaches_enc_005_without_any_declared_seam(
    repo: RepoContext,
) -> None:
    """ENC-001's own INVENTORY row carries an em dash in both dependency
    columns, so a forward walk finds nothing. The reverse edge saves it:
    ENC-005's row names ENC-001 as a provider in its notes.

    This is why edges are read in both directions, and it means the pilot's
    principal omission was reachable with no researcher declaration at all.
    """
    neighbours = inventory_neighbours("ENC-001", repo.inventory_text())
    assert "ENC-005" in neighbours


def test_the_real_enc_005_packet_cites_the_pages_the_pilot_missed(
    repo: RepoContext,
) -> None:
    """Read straight out of the accepted packet on disk."""
    packet = repo.evidence_dir / "ENC-005-evidence-remediated.md"
    assert packet.is_file()
    pages = cited_pages(packet.read_text(encoding="utf-8"))
    for page in (93, 98, 100):
        assert page in pages, f"p. {page} should be cited by the accepted ENC-005 packet"


def test_external_derivation_alone_produces_the_pilots_missed_pages(
    repo: RepoContext,
) -> None:
    """The principal claim: p. 98 and p. 100 arrive from outside the packet.

    No seam is declared here, so every page below comes from the INVENTORY
    reverse edge plus the accepted packet's own citations.
    """
    seeds = derive_external_seeds("ENC-001", [], repo)
    assert 98 in seeds, "B-1: p. 98 Contact"
    assert 100 in seeds, "BLOCKING-2: p. 100 Evasion at Sea"
    assert 93 in seeds, "the Encounter Distances Table itself"
    for page in sorted(seeds):
        assert all("ENC-005" in origin or "-evidence" in origin for origin in seeds[page])


def test_the_pilots_pass_1_page_set_leaves_derived_obligations_unmet(
    repo: RepoContext,
) -> None:
    """The pilot's actual coverage would not have reached a reviewer."""
    seeds = derive_external_seeds("ENC-001", [], repo)
    unmet = set(seeds) - PILOT_PASS_1
    assert unmet, "pass 1 should leave externally-derived obligations unmet"
    assert {98, 100} <= unmet
    assert len(PILOT_MISSED & unmet) >= 5


def test_p93_is_derived_externally_not_only_from_an_index(repo: RepoContext) -> None:
    """Index seeding is not external yet (no structured RC index exists outside
    packets). p. 93 is still covered, because the accepted neighbour packet
    cites it -- so the one externally-derived instrument reaches all three
    principal pages on its own.
    """
    seeds = derive_external_seeds("ENC-001", [], repo)
    assert 93 in seeds
    assert any("ENC-005" in origin for origin in seeds[93])


def test_derivation_carries_no_conclusion_from_the_neighbour_packet(
    repo: RepoContext,
) -> None:
    """ENC-005's accepted packet calls the table "light-keyed", which ENC-001
    refuted against primary text. The derived seeds must carry page numbers and
    a packet name, and nothing that could make that refutation harder.
    """
    packet = repo.evidence_dir / "ENC-005-evidence-remediated.md"
    assert "light-keyed" in packet.read_text(encoding="utf-8")
    seeds = derive_external_seeds("ENC-001", [], repo)
    blob = repr(seeds)
    assert "light-keyed" not in blob
    assert "Contact" not in blob
    assert all(isinstance(page, int) for page in seeds)
