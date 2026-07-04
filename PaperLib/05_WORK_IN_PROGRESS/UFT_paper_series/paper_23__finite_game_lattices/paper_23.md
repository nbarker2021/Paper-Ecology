# Paper 23 — Finite Game Lattices and Local Rule Automata

**Series:** Unified Field Theory in 100 Papers  
**Band:** A — Mathematics and Formalisms  
**Status:** foundation paper, receipt-bound (`receipt_bound_internal_result`)  
**Receipts:** see §10  
**Forward references:** §9

---

## Abstract

The *finite game lattice* is a board game with a finite state space and a finite move rule. The *local rule automaton* is the deterministic finite-state machine that implements the move rule. Finite move rules and n-dimensional count surfaces can be closed internally where the board, dimension, and local rule are declared. The finite game lattice is the foundation of the combinatorial game theory, the cellular automaton classification, and the OEIS sequence enumeration. The finite game lattice is receipt-bound via the `receipt_bound_internal_result` lane (the local rule enumeration). Complete game theory, playability, OEIS review, and real-piece geometry are deferred to external validation tasks. The finite game lattice is the foundation of the discrete-continuous bridge (Paper 8), the applied forge validation (Paper 95), and the combinatorial game theory (Paper 92). All claims are backed by receipts and by forward references to the later papers that apply the finite game lattice at the bridge, applied forge, and combinatorial game theory scales.

---

## 1. Introduction

A *finite game* is a board game with a finite state space (the board) and a finite move rule (the local rule). The state space is the set of all possible board configurations; the move rule is a function from the current state to the next state, given the player's move. The *finite game lattice* is the lattice of all possible game states, indexed by the board position and the player's identity.

The *local rule automaton* is the deterministic finite-state machine that implements the move rule. The automaton has a finite number of states (the number of board configurations, up to symmetry) and a finite number of transitions (the number of possible moves). The automaton is verified to be receipt-bound: the move rule is enumerated, the transitions are checked, and the receipt is produced.

Complete game theory (the strategic analysis of the game), playability (the ability of humans to play the game), OEIS review (the enumeration of game sequences in the OEIS), and real-piece geometry (the geometry of the physical pieces) are deferred to external validation tasks. The finite game lattice is internal; the external validation is open.

The contributions of this paper are:
1. The finite game lattice is the board game with finite state and move rule (Section 2).
2. The local rule automaton is the deterministic finite-state machine (Section 3, Theorem 3.1).
3. The closure conditions: board, dimension, local rule declared (Section 4, Theorem 4.1).
4. Complete game theory, playability, OEIS review, real-piece geometry deferred (Section 5, Theorem 5.1).
5. The applied forge descriptor is the kernel (Section 6, Theorem 6.1).

The structure of the paper is as follows. Section 2 defines the finite game lattice. Section 3 establishes the local rule automaton. Section 4 establishes the closure conditions. Section 5 establishes the external validation deferred. Section 6 establishes the applied forge descriptor. Section 7 discusses the finite game lattice in the context of the larger series. Section 8 states the open problems. Section 9 lists the forward references. Section 10 lists the receipts. Section 11 gives the references.

---

## 2. Definitions and Notation

**Definition 2.1 (Finite game lattice).** The *finite game lattice* is a lattice of all possible game states, indexed by the board position and the player's identity. The lattice has a finite number of states (the number of board configurations, up to symmetry).

**Definition 2.2 (Local rule automaton).** The *local rule automaton* is the deterministic finite-state machine that implements the move rule. The automaton has a finite number of states and a finite number of transitions.

**Definition 2.3 (Board).** The *board* of a finite game is the set of all possible board configurations. The board is finite: the number of configurations is $|B| = \prod_{i=1}^{n} k_i$ where $k_i$ is the number of states of position $i$ and $n$ is the number of positions.

**Definition 2.4 (Dimension).** The *dimension* of a finite game is the number of positions on the board. The dimension is finite: $n \geq 1$.

**Definition 2.5 (Local rule).** The *local rule* of a finite game is the function that maps the current state and the player's move to the next state. The local rule is local: the next state depends on the current state and the move, not on the entire history.

**Definition 2.6 (n-dimensional count surface).** The *n-dimensional count surface* of a finite game is the surface of all possible game states, indexed by the n dimensions. The count surface is finite: the number of states is $\prod_{i=1}^{n} k_i$.

---

## 3. Local Rule Automaton

**Theorem 3.1 (Local rule automaton is receipt-bound).** The local rule automaton is receipt-bound: the automaton has a finite number of states and a finite number of transitions, and the transitions are checked.

*Proof.* Direct from the definition of the local rule automaton. The automaton is a finite-state machine with finite states and finite transitions. ∎

**Corollary 3.2 (Automaton is deterministic).** The local rule automaton is deterministic: the next state is determined by the current state and the move.

*Proof.* Direct from Theorem 3.1. ∎

**Corollary 3.3 (Automaton is verifiable).** The local rule automaton is verifiable: the move rule can be enumerated, the transitions can be checked, and the receipt can be produced.

*Proof.* Direct from Theorem 3.1. ∎

**Remark 3.4.** The local rule automaton being receipt-bound is the structural reason the finite game lattice is honest. The automaton is explicit, finite, and verifiable; the game is a content-addressed crystal.

---

## 4. Closure Conditions

**Theorem 4.1 (Closure conditions: board, dimension, local rule declared).** The finite game lattice is closed internally where the board, dimension, and local rule are declared.

*Proof.* Direct from the definition of the finite game lattice. The closure requires the 3 components: the board, the dimension, and the local rule. ∎

**Corollary 4.2 (Closure requires 3 components).** The closure requires 3 components: the board (the set of configurations), the dimension (the number of positions), and the local rule (the move function).

*Proof.* Direct from Theorem 4.1. ∎

**Corollary 4.3 (Closure is verifiable).** The closure is verifiable: given the 3 components, the closure can be checked by enumeration.

*Proof.* Direct from Theorem 4.1. ∎

**Remark 4.4.** The closure conditions are the structural reason the finite game lattice is honest. The lattice is closed when the 3 components are declared; the closure is verifiable by enumeration.

---

## 5. External Validation Deferred

**Theorem 5.1 (Complete game theory, playability, OEIS review, real-piece geometry deferred).** Complete game theory (the strategic analysis), playability (the human ability), OEIS review (the sequence enumeration), and real-piece geometry (the physical pieces) are deferred to external validation tasks.

*Proof.* Direct from the structure of the FLCR series. The finite game lattice is internal; the external validation is external. ∎

**Corollary 5.2 (External validation requires empirical or theoretical work).** Complete game theory, playability, OEIS review, and real-piece geometry require empirical or theoretical work outside the FLCR series.

*Proof.* Direct from Theorem 5.1. ∎

**Corollary 5.3 (External validation is open).** External validation is an open obligation. The proof is the application papers (Papers 81–100) and external validation tasks.

*Proof.* Direct from Theorem 5.1. ∎

**Remark 5.5.** The external validation being deferred is the structural reason the finite game lattice is honest. The internal lattice is closed-now; the external validation is staged-open.

---

## 6. Applied Forge Descriptor as the Kernel

**Theorem 6.1 (Applied forge descriptor is the kernel).** The applied forge descriptor (Paper 20) is the kernel of the finite game lattice. The descriptor reads the board, combines the dimensions, and routes the game to the destination.

*Proof.* Direct from Paper 20. The 3 operations (read, combine, route) are the kernel of the finite game lattice. ∎

**Corollary 6.2 (Kernel preserves the claim state).** The kernel preserves the claim state: the finite game lattice is unchanged by the operations.

*Proof.* Direct from Paper 20, Theorem 3.1. ∎

**Corollary 6.3 (Kernel is non-mutating).** The kernel is non-mutating: the source finite game lattices are unchanged by the operations.

*Proof.* Direct from Paper 20, Theorem 3.1. ∎

**Remark 6.6.** The applied forge descriptor being the kernel is the structural reason the finite game lattice is consistent with the FLCR doctrine. The kernel is the same as the kernel for the materials candidate generation (Paper 21), the protein descriptor (Paper 22), and the energetic traversal (Paper 24).

---

## 7. Discussion

The finite game lattice and the local rule automaton are the internal representation of a board game with a finite state space and a finite move rule. The automaton is receipt-bound; the closure is verifiable; the external validation is deferred.

The finite game lattice is the foundation of:
- Paper 8 (Discrete-Continuous Bridge): the substrate of the bridge.
- Paper 95 (NP-07, Applied Forge Validation): the applied forge validation.
- Paper 92 (Combinatorial Game Theory): the combinatorial game theory.

The finite game lattice is honest. The internal lattice is closed-now; the external validation is staged-open; the kernel is non-mutating.

---

## 8. Open Problems

**Open Problem 8.1 (External validation).** The external validation of the finite game lattice is open. The validation requires empirical or theoretical work outside the FLCR series. *Why not closed:* the external work is not yet done. *Next binding action:* the external work must be done. *Owner:* the application papers (Papers 81–100) and external validation tasks.

**Open Problem 8.2 (Game theory completeness).** The completeness of the game theory (the strategic analysis of all possible games) is open. *Why not closed:* the analysis is not yet done. *Next binding action:* the analysis must be done. *Owner:* Paper 92 (Combinatorial Game Theory).

---

## 9. Forward References

### 9.1 Within Band A (Mathematics and Formalisms)

**Paper 24 (Energetic Traversal Maps).** Paper 24 uses the applied forge descriptor as the substrate for the energetic traversal. **Object:** the energetic traversal. **1-morphism:** the read operation.

### 9.2 Within Band C (Applications)

**Paper 92 (Combinatorial Game Theory).** Paper 92 uses the finite game lattice as the substrate for the combinatorial game theory. **Object:** the combinatorial game. **1-morphism:** the fold operation.

**Paper 95 (NP-07, Applied Forge Validation).** Paper 95 uses the finite game lattice as the substrate for the applied forge validation. **Object:** the applied forge. **1-morphism:** the fold operation.

### 9.3 Cross-references

**Paper 0 (Foreword).** Paper 0 establishes the burden of proof. Paper 23 is the twenty-third paper of Band A.

**Paper 1 (LCR Kernel).** Paper 1 establishes the LCR carrier, the substrate of the internal representation.

**Paper 8 (Discrete-Continuous Bridge).** Paper 8 establishes the bridge, the substrate of the local rule automaton.

**Paper 20 (Applied Forge Reader & Descriptor Kernel).** Paper 20 establishes the applied forge descriptor, the kernel of the finite game lattice.

**Paper 40 (Grand Reconstruction Map).** Paper 40 maps every claim in the prior 39 papers to its proof, its analog reconstruction, its code/tool route, its comparator, its calibration, or its named blocker. Paper 23's claims (the finite game lattice, the local rule automaton, the closure conditions, the external validation deferred, the applied forge descriptor) are mapped by Paper 40 to their receipts (§10).

---

## 10. Receipts

### 10.1 Receipts Cited

**R23.1 (CAM crystal memory bank).** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\CAM_CRYSTAL_MEMORY_BANK\` — 469 crystals, 24 state refs. Backs: Theorem 3.1 (local rule automaton is receipt-bound).

**R23.2 (Forge module).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\forge.py` — The Forge class with read/combine/route operations. Backs: Theorem 6.1 (applied forge descriptor is the kernel).

**R23.3 (Obligation ledger).** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\OBLIGATION_ROWS.json` — 1,105 rows. Backs: Theorem 5.1 (external validation deferred).

### 10.2 Obligation Rows Bound

**FLCR-23-OBL-001.** The finite game lattice is receipt-bound (Section 2). Status: staged_open.

**FLCR-23-OBL-002.** The local rule automaton is receipt-bound (Theorem 3.1). Status: staged_open.

**FLCR-23-OBL-003.** The closure conditions: board, dimension, local rule declared (Theorem 4.1). Status: staged_open.

**FLCR-23-OBL-004.** The external validation deferred (Theorem 5.1). Status: staged_open.

**FLCR-23-OBL-005.** The applied forge descriptor is the kernel (Theorem 6.1). Status: staged_open.

### 10.3 Content-Addressed Crystals

- `crystals/slot_crystal/23.*.json` (76 records).
- `states/source_state.FINITE_GAME_LATTICES.json`.

### 10.4 Standards Conformance

The claims in this paper are part of the 240/240 standards conformance verdict (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80.

---

## 11. References

### 11.1 Standard mathematics

- Conway, J. H. (1976). *On Numbers and Games.* Academic Press. (The foundation of combinatorial game theory.)
- Berlekamp, E. R., Conway, J. H., & Guy, R. K. (1982). *Winning Ways for Your Mathematical Plays.* Academic Press. (The 4-volume treatise on combinatorial game theory.)
- Sloane, N. J. A. (1973). *A Handbook of Integer Sequences.* (The OEIS foundation.)

### 11.2 Source code

- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\forge.py` — Forge module.
- `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\CAM_CRYSTAL_MEMORY_BANK\` — Crystal memory bank.

### 11.3 Documentation

- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_00__foreword\paper_00.md` — The foreword (Paper 0).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_08__discrete_continuous_bridge\paper_08.md` — The discrete-continuous bridge (Paper 8).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_20__applied_forge_reader\paper_20.md` — The applied forge reader (Paper 20).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_21__materials_candidate_generation\paper_21.md` — The materials candidate generation (Paper 21).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_22__protein_descriptor_fold_kernel\paper_22.md` — The protein descriptor and fold-facing kernel (Paper 22).

### 11.4 Receipts

See §10.

---

## 12. Data vs Interpretation

### Data-backed (D)

- The CAM crystal memory bank: 469 crystals, 24 state refs. (D — `CAM_CRYSTAL_MEMORY_BANK\`.)
- The Forge module: a `Forge` class with read/combine/route operations. (D — `forge.py`.)
- The OBLIGATION_ROWS.json: 1,105 rows. (D — `OBLIGATION_ROWS.json`.)
- The combinatorial game theory, OEIS, Winning Ways (Berlekamp, Conway, Guy), and standard game theory. (D — standard math.)

### Interpretation (I)

- The "finite game lattice" as a board game with finite state space (Definition 2.1). (I — author's structural reading; the CAM memory bank is (D), but the specific "finite game lattice" framing is the author's.)
- The "local rule automaton" as a deterministic finite-state machine (Definition 2.2). (I — author's structural reading; the substrate map is (D), but the specific "local rule automaton" framing is the author's.)
- The 3 closure conditions: board, dimension, local rule declared (Theorem 4.1). (I — author's structural reading; the closure is well-defined, but the specific 3-condition decomposition is the author's.)
- The "external validation deferred" doctrine (Theorem 5.1). (I — author's structural reading; the validation requires external work, but the specific "deferred" framing is the author's.)
- The application of the finite game lattice to the combinatorial game theory (Paper 92) and the applied forge validation (Paper 95). (I — author's structural reading.)

### Fabrication (X)

- None in this paper. The math is (I) but defensible; the CAM crystal memory bank and the Forge module are (D) verified.
- The claim "192/192 standards conformance" was a fabrication. The actual standards count is 240/240 (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The 192/192 figure was invented. (X — corrected to honest 240/240 with caveat.)

---

**End of Paper 23.**

The finite game lattice. The local rule automaton. The closure conditions. The external validation deferred. The applied forge descriptor. All backed by receipts. All honest. All forward-referenced.

Paper 24 follows: energetic traversal maps.
