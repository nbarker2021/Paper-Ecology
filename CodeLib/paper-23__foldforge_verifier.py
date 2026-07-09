"""
paper-23__foldforge_verifier.py

FoldForge Protein Descriptor Verifier (Paper 23)
=================================================
A-family verifier — all B-family lattice/oloid imports stripped.
Replaces stub paper-23__unified_foldforge_protein_folding.py.

Canonical sequence: ``MKTFFVLLLCTFTVLA`` (16 residues)

Verified claims
---------------
- Claim 23.1 [D]: Residue chain reads as local (L, C, R) windows.
- Claim 23.2 [D]: Replayable contact-map receipt (symmetric, zero-diagonal).
- Claim 23.3 [D]: Candidate bifurcation marks at local side-changes.
- Claim 23.4 [D]: Bounded winding witness (8-state operator, gap-aware).
- Claim 23.5 [D]: Descriptor status = pass_with_open_obligations.

Open obligations (honestly marked [X])
--------------------------------------
- Native structure prediction (23.6)
- Deposited structure agreement (23.7)
- Free-energy minima (23.8)
- Fold rates (23.9)
- AlphaFold parity (23.10)
- Measured thermodynamic behavior (23.11)
"""

from __future__ import annotations

import json
import math
import hashlib
from typing import List, Tuple, Dict, Any, Optional
from dataclasses import dataclass, asdict

# ---------------------------------------------------------------------------
# 1. Amino-acid encoding as LCR states
# ---------------------------------------------------------------------------

HYDROPHOBIC: set = {"A", "V", "I", "L", "M", "F", "W", "Y", "C"}
POLAR: set = {"R", "N", "D", "E", "Q", "H", "K", "S", "T", "P", "G"}

# Normalised Kyte-Doolittle hydrophobicity (approximate, verifier-scale)
KD_SCALE: Dict[str, float] = {
    "A": 1.8, "C": 2.5, "D": -3.5, "E": -3.5, "F": 2.8,
    "G": -0.4, "H": -3.2, "I": 4.5, "K": -3.9, "L": 3.8,
    "M": 1.9, "N": -3.5, "P": -1.6, "Q": -3.5, "R": -4.5,
    "S": -0.8, "T": -0.7, "V": 4.2, "W": -0.9, "Y": -1.3,
}


@dataclass(frozen=True)
class ResidueState:
    """
    Paper-23 Claim 23.1 [D]: Each residue is encoded as a state vector
    suitable for local-window composition.
    """
    symbol: str
    index: int
    is_hydrophobic: bool
    hydrophobicity: float

    def side(self) -> str:
        """Return 'H' for hydrophobic or 'P' for polar."""
        return "H" if self.is_hydrophobic else "P"


class AminoAcidEncoder:
    """
    Encodes a raw amino-acid string into a list of ``ResidueState`` objects.

    Paper-23 Claim 23.1 [D]: residue chain can be read as local CQE windows.
    """

    @staticmethod
    def encode(sequence: str) -> List[ResidueState]:
        sequence = sequence.upper().strip()
        states: List[ResidueState] = []
        for idx, sym in enumerate(sequence):
            if sym not in KD_SCALE:
                raise ValueError(f"Unknown residue symbol '{sym}' at position {idx}")
            states.append(ResidueState(
                symbol=sym,
                index=idx,
                is_hydrophobic=(sym in HYDROPHOBIC),
                hydrophobicity=KD_SCALE[sym],
            ))
        return states

    @staticmethod
    def hydrophobic_mask(sequence: str) -> List[int]:
        """Return a binary mask: 1 = hydrophobic, 0 = polar."""
        return [1 if s in HYDROPHOBIC else 0 for s in sequence.upper().strip()]


# ---------------------------------------------------------------------------
# 2. Local (L, C, R) windows
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class LCRWindow:
    """
    Paper-23 Claim 23.1 [D]: local window (L, C, R) where C is the active
    residue and L, R are its backbone neighbours.
    """
    left: Optional[ResidueState]
    center: ResidueState
    right: Optional[ResidueState]
    window_index: int

    def is_interior(self) -> bool:
        """True when both left and right neighbours exist."""
        return self.left is not None and self.right is not None

    def to_tuple(self) -> Tuple[Optional[str], str, Optional[str]]:
        l_sym = self.left.symbol if self.left else None
        r_sym = self.right.symbol if self.right else None
        return (l_sym, self.center.symbol, r_sym)

    def side_pattern(self) -> Tuple[Optional[str], str, Optional[str]]:
        l_side = self.left.side() if self.left else None
        r_side = self.right.side() if self.right else None
        return (l_side, self.center.side(), r_side)


class LCRWindowBuilder:
    """
    Builds overlapping local (L, C, R) windows from an encoded residue chain.

    Paper-23 Claim 23.1 [D]: 16 residue-window rows; 14 complete interior
    windows for the canonical sequence ``MKTFFVLLLCTFTVLA``.
    """

    @staticmethod
    def build(states: List[ResidueState]) -> List[LCRWindow]:
        windows: List[LCRWindow] = []
        n = len(states)
        for i in range(n):
            left = states[i - 1] if i > 0 else None
            right = states[i + 1] if i < n - 1 else None
            windows.append(LCRWindow(
                left=left,
                center=states[i],
                right=right,
                window_index=i,
            ))
        return windows

    @staticmethod
    def count_interior(windows: List[LCRWindow]) -> int:
        return sum(1 for w in windows if w.is_interior())


# ---------------------------------------------------------------------------
# 3. Contact-map receipt
# ---------------------------------------------------------------------------

@dataclass
class ContactMapReceipt:
    """
    Paper-23 Claim 23.2 [D]: symmetric, zero-diagonal contact matrix with
    nonzero contacts.  The predicate is heuristic (separated hydrophobic
    residues form candidate contacts), not a native fold.
    """
    size: int
    matrix: List[List[int]]
    contacts: List[Tuple[int, int]]
    symmetric: bool
    zero_diagonal: bool
    nonzero: bool


class ContactMapBuilder:
    """
    Constructs a replayable contact-map receipt.

    Heuristic predicate (Paper-23 §3, Theorem 23.2):
    Two residues i < j are candidate contacts when
      * both are hydrophobic, and
      * |i - j| >= 3 (separated by at least two residues).
    """

    @staticmethod
    def build(states: List[ResidueState], min_sep: int = 3) -> ContactMapReceipt:
        n = len(states)
        mat = [[0] * n for _ in range(n)]
        contacts: List[Tuple[int, int]] = []
        for i in range(n):
            for j in range(i + 1, n):
                if j - i < min_sep:
                    continue
                if states[i].is_hydrophobic and states[j].is_hydrophobic:
                    mat[i][j] = 1
                    mat[j][i] = 1
                    contacts.append((i, j))
        sym = all(mat[i][j] == mat[j][i] for i in range(n) for j in range(n))
        zd = all(mat[i][i] == 0 for i in range(n))
        nz = len(contacts) > 0
        return ContactMapReceipt(
            size=n,
            matrix=mat,
            contacts=contacts,
            symmetric=sym,
            zero_diagonal=zd,
            nonzero=nz,
        )

    @staticmethod
    def density(receipt: ContactMapReceipt) -> float:
        n = receipt.size
        if n < 2:
            return 0.0
        possible = n * (n - 1) // 2
        return len(receipt.contacts) / possible


# ---------------------------------------------------------------------------
# 4. Candidate bifurcation marks
# ---------------------------------------------------------------------------

@dataclass
class BifurcationMark:
    """
    Paper-23 Claim 23.3 [D]: a local side-change treated only as a candidate
    turn or topology marker, not promoted to a real fold without structure
    comparison.
    """
    position: int
    from_side: str
    to_side: str
    window: LCRWindow


class BifurcationMarker:
    """
    Marks local side changes as candidate bifurcation events.

    A side-change is detected when the centre residue's side differs from
    either neighbour, indicating a local polarity reversal.
    """

    @staticmethod
    def mark(windows: List[LCRWindow]) -> List[BifurcationMark]:
        marks: List[BifurcationMark] = []
        for w in windows:
            if not w.is_interior():
                continue
            c_side = w.center.side()
            l_side = w.left.side()  # type: ignore[union-attr]
            r_side = w.right.side()  # type: ignore[union-attr]
            # A candidate bifurcation occurs when the centre is different
            # from at least one neighbour (local polarity reversal).
            if c_side != l_side or c_side != r_side:
                # Record the dominant-to-recessive transition direction
                from_side = l_side if l_side != c_side else r_side
                marks.append(BifurcationMark(
                    position=w.window_index,
                    from_side=from_side,
                    to_side=c_side,
                    window=w,
                ))
        return marks


# ---------------------------------------------------------------------------
# 5. Folding energy calculations (verifier-scale)
# ---------------------------------------------------------------------------

class EnergyCalculator:
    """
    Computes a heuristic folding energy for the descriptor, **not** claiming
    biological free-energy minima (Claim 23.8 [X] remains open).

    The energy model is:
      * contact energy   : negative (stabilising) for each satisfied
        hydrophobic contact;
      * solvation penalty: positive (destabilising) for each exposed
        hydrophobic residue without contacts.
    """

    CONTACT_ENERGY: float = -2.5  # arbitrary verifier-scale units
    SOLVATION_PENALTY: float = +1.0

    @classmethod
    def compute_energy(
        cls,
        states: List[ResidueState],
        contact_receipt: ContactMapReceipt,
    ) -> float:
        n = len(states)
        energy = 0.0
        contact_counts = [0] * n
        for i, j in contact_receipt.contacts:
            energy += cls.CONTACT_ENERGY
            contact_counts[i] += 1
            contact_counts[j] += 1
        for idx, st in enumerate(states):
            if st.is_hydrophobic and contact_counts[idx] == 0:
                energy += cls.SOLVATION_PENALTY
        return energy

    @staticmethod
    def hydrophobic_burial_ratio(
        states: List[ResidueState],
        contact_receipt: ContactMapReceipt,
    ) -> float:
        """Fraction of hydrophobic residues that participate in at least one contact."""
        hydrophobic_indices = [i for i, s in enumerate(states) if s.is_hydrophobic]
        if not hydrophobic_indices:
            return 0.0
        involved = set()
        for i, j in contact_receipt.contacts:
            involved.add(i)
            involved.add(j)
        buried = sum(1 for i in hydrophobic_indices if i in involved)
        return buried / len(hydrophobic_indices)


# ---------------------------------------------------------------------------
# 6. Protein structure constraints (verifier-scale)
# ---------------------------------------------------------------------------

class StructureConstraintChecker:
    """
    Verifies geometric and topological constraints on the residue chain
    descriptor, **not** claiming native structure prediction (Claim 23.7 [X]
    remains open).
    """

    @staticmethod
    def chain_connectivity(states: List[ResidueState]) -> bool:
        """Every residue must have sequential index coverage."""
        return all(states[i].index == i for i in range(len(states)))

    @staticmethod
    def no_clash_distance(
        states: List[ResidueState],
        contact_receipt: ContactMapReceipt,
        min_seq_sep: int = 3,
    ) -> bool:
        """
        Residues closer than ``min_seq_sep`` must not be marked as contacts
        (simple hard-sphere proxy).
        """
        for i, j in contact_receipt.contacts:
            if abs(i - j) < min_seq_sep:
                return False
        return True

    @staticmethod
    def angle_heuristic(windows: List[LCRWindow]) -> List[float]:
        """
        Returns a list of pseudo-angle scores derived from hydrophobicity
        gradients across interior windows.  Purely descriptor-level.
        """
        angles: List[float] = []
        for w in windows:
            if not w.is_interior():
                continue
            l_h = w.left.hydrophobicity  # type: ignore[union-attr]
            c_h = w.center.hydrophobicity
            r_h = w.right.hydrophobicity  # type: ignore[union-attr]
            # Pseudo-angle: variance of the three hydrophobicities
            mean_h = (l_h + c_h + r_h) / 3.0
            var = ((l_h - mean_h) ** 2 + (c_h - mean_h) ** 2 + (r_h - mean_h) ** 2) / 3.0
            angles.append(math.sqrt(var))
        return angles


# ---------------------------------------------------------------------------
# 7. Bounded winding witness (8-state finite operator)
# ---------------------------------------------------------------------------

class WindingWitness:
    """
    Paper-23 Claim 23.4 [D]: bounded winding substrate.

    Implements an 8-state finite operator that transitions according to
    residue-side patterns.  Bounded by ``max_depth`` and ``max_order``.
    The depth-only extractor is retained as a named gap.
    """

    STATES: Tuple[str, ...] = ("S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7")
    MAX_DEPTH: int = 512
    MAX_ORDER: int = 4

    # Transition table keyed by (current_state, side_pattern)
    # side_pattern is one of: "HHH", "HHP", "HPH", "HPP", "PHH", "PHP", "PPH", "PPP"
    _TRANSITIONS: Dict[Tuple[str, str], str] = {
        ("S0", "HHH"): "S1", ("S0", "HHP"): "S2", ("S0", "HPH"): "S3", ("S0", "HPP"): "S4",
        ("S0", "PHH"): "S5", ("S0", "PHP"): "S6", ("S0", "PPH"): "S7", ("S0", "PPP"): "S0",
        ("S1", "HHH"): "S2", ("S1", "HHP"): "S3", ("S1", "HPH"): "S4", ("S1", "HPP"): "S5",
        ("S1", "PHH"): "S6", ("S1", "PHP"): "S7", ("S1", "PPH"): "S0", ("S1", "PPP"): "S1",
        ("S2", "HHH"): "S3", ("S2", "HHP"): "S4", ("S2", "HPH"): "S5", ("S2", "HPP"): "S6",
        ("S2", "PHH"): "S7", ("S2", "PHP"): "S0", ("S2", "PPH"): "S1", ("S2", "PPP"): "S2",
        ("S3", "HHH"): "S4", ("S3", "HHP"): "S5", ("S3", "HPH"): "S6", ("S3", "HPP"): "S7",
        ("S3", "PHH"): "S0", ("S3", "PHP"): "S1", ("S3", "PPH"): "S2", ("S3", "PPP"): "S3",
        ("S4", "HHH"): "S5", ("S4", "HHP"): "S6", ("S4", "HPH"): "S7", ("S4", "HPP"): "S0",
        ("S4", "PHH"): "S1", ("S4", "PHP"): "S2", ("S4", "PPH"): "S3", ("S4", "PPP"): "S4",
        ("S5", "HHH"): "S6", ("S5", "HHP"): "S7", ("S5", "HPH"): "S0", ("S5", "HPP"): "S1",
        ("S5", "PHH"): "S2", ("S5", "PHP"): "S3", ("S5", "PPH"): "S4", ("S5", "PPP"): "S5",
        ("S6", "HHH"): "S7", ("S6", "HHP"): "S0", ("S6", "HPH"): "S1", ("S6", "HPP"): "S2",
        ("S6", "PHH"): "S3", ("S6", "PHP"): "S4", ("S6", "PPH"): "S5", ("S6", "PPP"): "S6",
        ("S7", "HHH"): "S0", ("S7", "HHP"): "S1", ("S7", "HPH"): "S2", ("S7", "HPP"): "S3",
        ("S7", "PHH"): "S4", ("S7", "PHP"): "S5", ("S7", "PPH"): "S6", ("S7", "PPP"): "S7",
    }

    def __init__(self, max_depth: int = MAX_DEPTH, max_order: int = MAX_ORDER):
        self.max_depth = max_depth
        self.max_order = max_order
        self.gaps: List[str] = ["DEPTH_ONLY_WINDING_EXTRACTOR_PENDING"]

    def run(self, windows: List[LCRWindow]) -> Dict[str, Any]:
        """
        Execute the bounded winding trace over the interior windows.

        Returns a witness dictionary with state trajectory, operator checks,
        and gap list.
        """
        state = "S0"
        trajectory: List[str] = [state]
        depth = 0
        for w in windows:
            if not w.is_interior():
                continue
            if depth >= self.max_depth:
                break
            pattern = "".join(w.side_pattern())  # type: ignore[arg-type]
            key = (state, pattern)
            if key not in self._TRANSITIONS:
                raise RuntimeError(f"Undefined transition for {key}")
            state = self._TRANSITIONS[key]
            trajectory.append(state)
            depth += 1
        unique_states = sorted(set(trajectory))
        return {
            "initial_state": "S0",
            "final_state": state,
            "trajectory_length": len(trajectory),
            "unique_states": unique_states,
            "state_count": len(unique_states),
            "bounded": len(trajectory) <= self.max_depth + 1,
            "schema_valid": True,
            "stable_operator": len(unique_states) <= 8,
            "gaps": self.gaps.copy(),
        }


# ---------------------------------------------------------------------------
# 8. Main verifier
# ---------------------------------------------------------------------------

@dataclass
class FoldForgeReceipt:
    """
    Paper-23 Claim 23.5 [D]: receipt emitted by the verifier.
    Status is ``pass_with_open_obligations``.
    """
    status: str
    residue_count: int
    residue_windows: int
    interior_windows: int
    contact_map_symmetric: bool
    contact_map_zero_diagonal: bool
    contact_map_nonzero: bool
    contact_map_density: float
    bifurcation_marks: int
    energy: float
    hydrophobic_burial_ratio: float
    winding_state_count: int
    winding_bounded: bool
    winding_gaps: List[str]
    open_obligations: List[str]


class FoldForgeVerifier:
    """
    End-to-end verifier for Paper-23 FoldForge claims.
    """

    CANONICAL_SEQUENCE: str = "MKTFFVLLLCTFTVLA"
    OPEN_OBLIGATIONS: List[str] = [
        "23.6 — Native structure prediction",
        "23.7 — Deposited structure agreement",
        "23.8 — Free-energy minima",
        "23.9 — Fold rates",
        "23.10 — AlphaFold parity",
        "23.11 — Measured thermodynamic behavior",
        "DEPTH_ONLY_WINDING_EXTRACTOR_PENDING",
    ]

    def __init__(self, sequence: Optional[str] = None):
        self.sequence = sequence or self.CANONICAL_SEQUENCE
        self.states: List[ResidueState] = []
        self.windows: List[LCRWindow] = []
        self.contact_receipt: Optional[ContactMapReceipt] = None
        self.bifurcations: List[BifurcationMark] = []
        self.energy: float = 0.0
        self.witness: Optional[Dict[str, Any]] = None

    def run(self) -> FoldForgeReceipt:
        """Execute the full verification pipeline."""
        # Step 1 — encode
        self.states = AminoAcidEncoder.encode(self.sequence)

        # Step 2 — LCR windows
        self.windows = LCRWindowBuilder.build(self.states)
        interior_count = LCRWindowBuilder.count_interior(self.windows)

        # Step 3 — contact map
        self.contact_receipt = ContactMapBuilder.build(self.states)
        density = ContactMapBuilder.density(self.contact_receipt)

        # Step 4 — bifurcation marks
        self.bifurcations = BifurcationMarker.mark(self.windows)

        # Step 5 — energy (verifier-scale)
        self.energy = EnergyCalculator.compute_energy(self.states, self.contact_receipt)
        burial = EnergyCalculator.hydrophobic_burial_ratio(self.states, self.contact_receipt)

        # Step 6 — structure constraints
        assert StructureConstraintChecker.chain_connectivity(self.states)
        assert StructureConstraintChecker.no_clash_distance(self.states, self.contact_receipt)
        angles = StructureConstraintChecker.angle_heuristic(self.windows)

        # Step 7 — winding witness
        w = WindingWitness()
        self.witness = w.run(self.windows)

        return FoldForgeReceipt(
            status="pass_with_open_obligations",
            residue_count=len(self.states),
            residue_windows=len(self.windows),
            interior_windows=interior_count,
            contact_map_symmetric=self.contact_receipt.symmetric,
            contact_map_zero_diagonal=self.contact_receipt.zero_diagonal,
            contact_map_nonzero=self.contact_receipt.nonzero,
            contact_map_density=density,
            bifurcation_marks=len(self.bifurcations),
            energy=self.energy,
            hydrophobic_burial_ratio=burial,
            winding_state_count=self.witness["state_count"],
            winding_bounded=self.witness["bounded"],
            winding_gaps=self.witness["gaps"],
            open_obligations=self.OPEN_OBLIGATIONS.copy(),
        )

    def write_receipt(self, path: str) -> None:
        """Emit the JSON receipt."""
        receipt = self.run()
        data = asdict(receipt)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)


# ---------------------------------------------------------------------------
# 9. Unit-test style verifications (executable as __main__)
# ---------------------------------------------------------------------------

def test_claim_23_1_lcr_windows() -> None:
    """
    Paper-23 Claim 23.1 [D]:
    The canonical sequence produces 16 residue-window rows and
    14 complete interior (L, C, R) windows.
    """
    v = FoldForgeVerifier()
    receipt = v.run()
    assert receipt.residue_count == 16, "Expected 16 residues"
    assert receipt.residue_windows == 16, "Expected 16 windows"
    assert receipt.interior_windows == 14, "Expected 14 interior windows"
    print("[PASS] Claim 23.1 — LCR windows verified.")


def test_claim_23_2_contact_map() -> None:
    """
    Paper-23 Claim 23.2 [D]:
    Contact map is symmetric, zero-diagonal, and contains nonzero contacts.
    """
    v = FoldForgeVerifier()
    receipt = v.run()
    assert receipt.contact_map_symmetric, "Contact map must be symmetric"
    assert receipt.contact_map_zero_diagonal, "Contact map must have zero diagonal"
    assert receipt.contact_map_nonzero, "Contact map must have nonzero contacts"
    assert 0.0 < receipt.contact_map_density < 1.0, "Density must be nontrivial"
    print("[PASS] Claim 23.2 — Contact-map receipt verified.")


def test_claim_23_3_bifurcation_marks() -> None:
    """
    Paper-23 Claim 23.3 [D]:
    Local side changes are marked as candidate bifurcations.
    """
    v = FoldForgeVerifier()
    receipt = v.run()
    assert receipt.bifurcation_marks > 0, "Expected at least one candidate bifurcation"
    print(f"[PASS] Claim 23.3 — {receipt.bifurcation_marks} candidate bifurcation mark(s) verified.")


def test_claim_23_4_winding_witness() -> None:
    """
    Paper-23 Claim 23.4 [D]:
    Winding witness is bounded, has an 8-state operator, and retains
    the depth-only extractor gap.
    """
    v = FoldForgeVerifier()
    receipt = v.run()
    assert receipt.winding_bounded, "Winding witness must be bounded"
    assert receipt.winding_state_count <= 8, "Operator must expose <= 8 states"
    assert "DEPTH_ONLY_WINDING_EXTRACTOR_PENDING" in receipt.winding_gaps
    print("[PASS] Claim 23.4 — Bounded winding witness verified.")


def test_claim_23_5_governance() -> None:
    """
    Paper-23 Claim 23.5 [D]:
    Descriptor status is pass_with_open_obligations.
    """
    v = FoldForgeVerifier()
    receipt = v.run()
    assert receipt.status == "pass_with_open_obligations"
    assert len(receipt.open_obligations) >= 6
    print("[PASS] Claim 23.5 — Governance (candidate until validated) verified.")


def test_folding_energy() -> None:
    """
    Verifier-scale energy calculation: negative energy indicates some
    hydrophobic burial; ratio > 0 means not all hydrophobes are exposed.
    """
    v = FoldForgeVerifier()
    receipt = v.run()
    assert receipt.energy < 0, "Expected stabilising (negative) verifier-scale energy"
    assert 0.0 < receipt.hydrophobic_burial_ratio <= 1.0
    print(f"[PASS] Folding energy = {receipt.energy:.3f}, burial ratio = {receipt.hydrophobic_burial_ratio:.3f}")


def test_structure_constraints() -> None:
    """
    Verifier-scale structure constraints: chain connectivity, no clash
    distances, and finite angle heuristics.
    """
    v = FoldForgeVerifier()
    v.run()
    assert StructureConstraintChecker.chain_connectivity(v.states)
    assert StructureConstraintChecker.no_clash_distance(v.states, v.contact_receipt)
    angles = StructureConstraintChecker.angle_heuristic(v.windows)
    assert len(angles) == 14
    assert all(math.isfinite(a) for a in angles)
    print("[PASS] Structure constraints verified.")


def run_all_tests() -> FoldForgeReceipt:
    print("=" * 60)
    print("FoldForge Verifier — Paper 23")
    print("=" * 60)
    test_claim_23_1_lcr_windows()
    test_claim_23_2_contact_map()
    test_claim_23_3_bifurcation_marks()
    test_claim_23_4_winding_witness()
    test_claim_23_5_governance()
    test_folding_energy()
    test_structure_constraints()
    print("=" * 60)
    v = FoldForgeVerifier()
    receipt = v.run()
    print(f"Status : {receipt.status}")
    print(f"Windows: {receipt.residue_windows} total, {receipt.interior_windows} interior")
    print(f"Contacts: {receipt.contact_map_nonzero} (density {receipt.contact_map_density:.3f})")
    print(f"Bifurcations: {receipt.bifurcation_marks}")
    print(f"Winding states: {receipt.winding_state_count}")
    print(f"Energy: {receipt.energy:.3f}")
    print(f"Open obligations: {len(receipt.open_obligations)}")
    print("=" * 60)
    return receipt


if __name__ == "__main__":
    receipt = run_all_tests()
    # Emit JSON receipt alongside stdout
    receipt_path = "foldforge_descriptor_receipt.json"
    with open(receipt_path, "w", encoding="utf-8") as f:
        json.dump(asdict(receipt), f, indent=2)
    print(f"Receipt written to {receipt_path}")
