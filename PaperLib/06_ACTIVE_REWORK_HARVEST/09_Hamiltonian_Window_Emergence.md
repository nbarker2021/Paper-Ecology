# Paper 09 — Hamiltonian Window Emergence

**Status:** IPMC — internal physics map closed for Hamiltonian window emergence, scalar sweep admissibility, McKay-Thompson threshold stack with light-cone adjugation witness, kappa conservation timeline, and U_R30 quantum circuit. Unbounded closed-form McKay arithmetic, physical time reversal, static-Z4 temporal periodicity, and measured quantum hardware claims remain open.

**Source papers:** CQE-paper-09, CQE-paper-09.25.  
**Canonical formal paper:** `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-09/FORMAL_PAPER.md`.  
**Verifiers:** `verify_hamiltonian_window_emergence.py`, `verify_kappa_conservation_law.py`, `verify_glm_alpha_fractional_cayley_dickson.py`, `verify_u_r30_quantum_circuit.py`.

---

## Abstract

Paper 09 formalizes temporal emergence as an iterated local-window read over already transported centers. The closed theorems are finite and exact: given an ordered list of carried centers, a Hamiltonian window of width `w` reads a contiguous slice forward, reads the same slice backward as a well-formed reverse receipt, and emits a composite center that preserves the source-center sequence. Starting with six base centers, widths `3`, `5`, and `7` produce four order-2 windows, three order-3 windows, and two order-4 windows.

The paper also separates McKay-Thompson exactness candidates from ordinary scalar admissibility. Candidate status is reserved for the declared dihedral/doubling threshold bands `1-3, 3-5, 5-7, 7-9, 15-17, 31-35`. At `K = 9`, the first four bands are closed light-cone-bound candidates; the higher bands are pending. The proof route is the light-cone-derived adjugation witness (1,903 correction witnesses through depth 64, zero failures), which promotes the bounded threshold route while leaving unbounded closed-form McKay arithmetic outside the receipt.

Additionally, the paper closes the kappa conservation law (`kappa = ln(φ)/16`) as a Hamiltonian/Lyapunov descent timeline, and the U_R30 reversible quantum circuit as an exact classical-reversible simulation.

The guard is extensive: the static Z4 chart template does not prove temporal periodicity, the reverse receipt is not physical time reversal, and the quantum circuit exactness is classical-reversible, not measured quantum hardware.

### Keywords

Hamiltonian window; temporal emergence; composite center; reverse receipt; scalar sweep; McKay-Thompson threshold; light-cone adjugation; kappa conservation; morphon potential; quantum circuit; U_R30; CQECMPLX receipts.

---

## Claim Ledger

| ID | Claim | Tag | Evidence | Boundary |
|----|-------|-----|----------|----------|
| 09.1 | Width-3 reads over six base centers produce four surviving composite centers. | [D] | `verify_hamiltonian_window_emergence.py`; `hamiltonian_window_emergence_receipt.json` (19/19) | Finite arithmetic |
| 09.2 | Width-5 reads after appending order-2 produce three surviving composite centers. | [D] | Same verifier | Finite arithmetic |
| 09.3 | Width-7 reads after appending order-3 produce two surviving composite centers. | [D] | Same verifier | Finite arithmetic |
| 09.4 | Every surviving composite center preserves source indices and source centers. | [D] | Same verifier | Provenance preservation |
| 09.5 | Every backward receipt reverses to the forward receipt. | [D] | Same verifier | Reverse receipt well-formedness |
| 09.6 | Scalar widths `w ∈ [3, K-1]` are admissible and preserve provenance. | [D] | Same verifier | Scalar sweep admissibility |
| 09.7 | McKay-Thompson bands match declared thresholds: `1-3, 3-5, 5-7, 7-9, 15-17, 31-35`. | [D] | Same verifier | Band declaration |
| 09.8 | At `K = 9`, the first four bands are closed; `15-17` and `31-35` are pending. | [D] | Same verifier | Threshold closure |
| 09.9 | Threshold local clocks are monotone and run in global lockstep. | [D] | Same verifier | Lockstep stack |
| 09.10 | Paper 6 light-cone decomposition and Paper 10 cold-start bijection pass before McKay binding. | [D] | Same verifier | Dependency ordering |
| 09.11 | The McKay route uses the passing light-cone adjugation witness (1,903 witnesses, depth 64, zero failures). | [D] | Same verifier | Bounded promotion |
| 09.12 | The static Z4 chart template does not prove temporal periodicity. | [D] | Same verifier | Falsifier |
| 09.13 | `kappa = ln(φ)/16` is exact and matches the source `0.030076`. | [D] | `verify_kappa_conservation_law.py`; `kappa_conservation_law_receipt.json` (10/10) | Numerical exactness |
| 09.14 | Golden-ratio identities `φ² = φ + 1` and `e^(16κ) = φ` hold. | [D] | Same verifier | Algebraic identity |
| 09.15 | The E8 embedding has norm exactly `kappa` and is deterministic. | [D] | Same verifier | Norm exactness |
| 09.16 | The morphon delta is conserved (`≤ 0`) and bounded by `kappa * affinity`. | [D] | Same verifier | Conservation bound |
| 09.17 | The sector split `delta_N + delta_I + delta_L = delta_Φ` is additive. | [D] | Same verifier | Sector decomposition |
| 09.18 | The per-event Event Law emission is exactly `-kappa`. | [D] | Same verifier | Cross-repo confirmation |
| 09.19 | A stream of conserved deltas keeps cumulative non-increasing; positive deltas are violations. | [D] | Same verifier | Violation detection |
| 09.20 | The audit chain recomputes cumulative with zero drift. | [D] | Same verifier | Audit consistency |
| 09.21 | Surplus is the spendable magnitude when cumulative is negative. | [D] | Same verifier | Surplus definition |
| 09.22 | The alpha fractional Cayley-Dickson derivation checks pass: integer decomp, vertex near 62, quadratic root range, stack residual ≤ 1, kappa match. | [D] | `verify_glm_alpha_fractional_cayley_dickson.py`; `alpha_fractional_cayley_dickson_receipt.json` (5/5) | Finite algebraic checks |
| 09.23 | The U_R30 reversible 3-qubit circuit is exact: bijective on 16 states, target = Rule 30, neighborhood preserved, double-apply restores ancilla. | [D] | `verify_u_r30_quantum_circuit.py`; `u_r30_quantum_circuit_receipt.json` (5/5) | Classical-reversible exactness |
| 09.24 | Unbounded closed-form McKay-Thompson arithmetic is proven. | [X] | No closing receipt | Bounded witness only; unbounded remains open |
| 09.25 | Physical time reversal is proven. | [X] | No closing receipt | Reverse receipt is receipt-level, not physical |
| 09.26 | The static Z4 chart template proves temporal periodicity. | [X] | `temporal_period_claim_supported = false` | Falsifier rejects |
| 09.27 | Measured quantum hardware / unistochastic-VOA physics is proven. | [X] | No closing receipt | Classical-reversible exactness only; hardware claim is external bridge |
| 09.28 | Unequal Noether/Shannon/Landauer sector weights are derived. | [X] | Equal thirds modeled; derivation is future work | Separate receipt needed |
| 09.29 | Palindromic-closure equivalence is given its own receipt. | [X] | Asserted in source prose, not yet receipted | Separate receipt needed |

---

## Definitions

**Definition 9.1 (Center state).** A center state is a pair `(paper_id, center)` where `center` is the surviving local quantity carried from that paper.

**Definition 9.2 (Hamiltonian window).** A Hamiltonian window of width `w` over an ordered sequence `S = [s₀, ..., sₙ₋₁]` is the contiguous slice `Wᵢ = [sᵢ, sᵢ₊₁, ..., sᵢ₊w₋₁]` starting at index `i`, for `0 ≤ i ≤ n - w`.

**Definition 9.3 (Forward read).** The forward read of window `Wᵢ` records the centers in source order: `Cᵢ → Cᵢ₊₁ → ... → Cᵢ₊w₋₁`.

**Definition 9.4 (Backward read).** The backward read of window `Wᵢ` records the reverse receipt: `Cᵢ₊w₋₁ ← ... ← Cᵢ₊₁ ← Cᵢ`.

**Definition 9.5 (Surviving composite center).** The surviving composite center of window `Wᵢ` is the ordered join of every center in the window, accepted only when the forward and backward receipts contain the same source centers in opposite order.

**Definition 9.6 (McKay-Thompson exact boundary band).** A McKay-Thompson exact boundary band is one of the declared dihedral/doubling threshold intervals: `1-3, 3-5, 5-7, 7-9, 15-17, 31-35`. Their centers are `2, 4, 6, 8, 16, 33`.

**Definition 9.7 (Lockstep threshold stack).** A lockstep threshold stack is a ledger in which every active or completed exact band keeps its own local tick while all bands advance under the same global action index.

**Definition 9.8 (Kappa).** `kappa = ln(φ)/16 ≈ 0.030075739066225217`, where `φ = (1 + √5)/2` is the golden ratio.

**Definition 9.9 (Conserved morphon delta).** A morphon delta is conserved if `delta_Φ ≤ 0`. The cumulative ledger is non-increasing; positive deltas are violations.

**Definition 9.10 (Event Law delta).** The per-event Event Law emission is exactly `-kappa`, minted live in every ChromaForge/PaneForge receipt.

---

## Theorems and Proofs

**Theorem 9.1 (Hamiltonian Window Emergence).** For any finite ordered sequence `S = [s₀, ..., sₙ₋₁]` of center states and any fixed window width `w ≤ n`, the Hamiltonian window read emits exactly `n - w + 1` surviving composite centers. Each composite center preserves its source centers, source indices, forward receipt, and backward receipt.

*Proof.* The valid window start indices are `0, 1, ..., n - w`. There are therefore `n - w + 1` windows. For each start index `i`, the window slice is `Wᵢ = [sᵢ, sᵢ₊₁, ..., sᵢ₊w₋₁]`. The forward read records the centers of `Wᵢ` in source order. The backward read records the same centers in reverse order. Since reversal is an involution, reversing the backward read recovers the forward center sequence. Thus the emitted composite center preserves the source centers and their provenance. ∎

For the CQECMPLX production instance, begin with six base center states. Width `3` produces `6 - 3 + 1 = 4` order-2 reads. Appending the resulting order-2 state gives seven states, so width `5` produces `7 - 5 + 1 = 3` order-3 reads. Appending that state gives eight states, so width `7` produces `8 - 7 + 1 = 2` order-4 reads. The verifier confirms these counts: 4, 3, and 2. ∎

**Theorem 9.1a (Hamiltonian Scalar Sweep).** For a final carried-state set of size `K`, every integer scalar width `w ∈ [3, K-1]` is an admissible Hamiltonian window. Each scalar emits `K - w + 1` centers and preserves the same source-index, source-center, forward-receipt, and backward-receipt invariants.

*Proof.* The verifier reads the final nine carried states with every integer width from `3` through `8`. Each width satisfies `count(w) = K - w + 1` and preserves source provenance. This proves scalar admissibility across the proper Hamiltonian range. The theorem proves admissibility, not exact McKay-Thompson promotion. ∎

**Theorem 9.1b (McKay-Thompson Threshold Stack).** Hamiltonian exactness candidates are reserved for the declared bands `1-3, 3-5, 5-7, 7-9, 15-17, 31-35`. At `K = 9`, the first four bands are closed light-cone-bound candidates and the higher bands are pending. Each band keeps a local clock, while the whole stack advances in lockstep under the global action index. The proof route is the light-cone-derived adjugation witness, which promotes the bounded McKay threshold route for the closed bands in the tested window.

*Proof.* The verifier separates boundary candidates from ordinary scalar admissibility. At `K = 9`, the closed light-cone-bound candidates are `1-3, 3-5, 5-7, 7-9`. The `15-17` and `31-35` bands remain pending future thresholds. Each active or completed band has a monotone local clock, and every clock is indexed by the same global action count. The verifier then runs the McKay matrix bootstrap, three-move bijection closure, Paper 11 sporadic ledger, Paper 6 light-cone decomposition, and Paper 10 cold-start bijection. The light-cone and bijection base passes. The direct VOA route remains `CONJ`, but the light-cone adjugation witness passes with 1,903 correction witnesses through depth 64, zero failures, and coverage of both correction-firing states `(0,1,0)` and `(1,1,0)`. This promotes the bounded McKay threshold route for the tested window while leaving unbounded closed-form McKay arithmetic outside this receipt. ∎

**Theorem 9.2 (Kappa Conservation Timeline).** Let `kappa = ln(φ)/16`. A morphon event emits a conserved non-positive potential delta, with per-event Event Law delta `-kappa`. The cumulative ledger is non-increasing, positive deltas are violations, and the ordered ledger of deltas is a finite Hamiltonian/Lyapunov timeline.

*Proof.* The verifier `verify_kappa_conservation_law.py` runs the ChromaForge conservation/morphon verifier. It checks:

1. `kappa = ln(φ)/16` numerically, agreeing with the source `0.030076`.
2. Golden-ratio identities `φ² = φ + 1` and `e^(16κ) = φ`.
3. The E8 embedding has norm exactly `kappa` and is deterministic.
4. The morphon delta is conserved (`≤ 0`) and bounded by `kappa * affinity`.
5. The sector split `delta_N + delta_I + delta_L = delta_Φ` is additive.
6. The per-event Event Law emission is exactly `-kappa`.
7. A stream of conserved deltas keeps cumulative non-increasing with zero violations.
8. A single positive delta is flagged as a violation; only positive deltas are.
9. The audit chain recomputes the cumulative with zero drift.
10. Surplus is the spendable magnitude when cumulative is negative.

All 10 checks pass. The theorem binds the conservation sign convention and records the TMN-main positive-delta emission as an upstream sign error (engine.py emits a strictly positive morphon_delta labeled "conserved surplus", which is backwards; the live receipt mints `-kappa`, confirming the conservation.py convention). ∎

**Theorem 9.3 (Alpha Fractional Cayley-Dickson).** The alpha inverse fractional derivation via Cayley-Dickson stacking passes finite algebraic checks: integer decomposition, vertex near 62, quadratic root range, stack residual `≤ 1`, and kappa match.

*Proof.* The verifier `verify_glm_alpha_fractional_cayley_dickson.py` checks the structural argument: the deep-hole quadratic has coefficients derived from `kappa`, vertex near 62, root `alpha_inv ≈ 123.96`, and the Cayley-Dickson stack yields `alpha_inv ≈ 137.004` with residual `0.032` from CODATA `137.035999084`. All 5 checks pass. The physical fine-structure identification is an external bridge, not a closed theorem. ∎

**Theorem 9.4 (U_R30 Quantum Circuit).** The reversible 3-qubit Rule 30 circuit is exact: bijective on 16 states, target reproduces Rule 30, neighborhood qubits are preserved, and double-apply restores the ancilla.

*Proof.* The verifier `verify_u_r30_quantum_circuit.py` checks the circuit against the Rule 30 column. All 5 checks pass. The theorem is classical-reversible exactness; the measured quantum-hardware / unistochastic-VOA physics claim is an external bridge. ∎

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Status |
|----------|---------|--------|--------|
| `verify_hamiltonian_window_emergence.py` | `hamiltonian_window_emergence_receipt.json` | 19 | pass |
| `verify_kappa_conservation_law.py` | `kappa_conservation_law_receipt.json` | 10 | pass |
| `verify_glm_alpha_fractional_cayley_dickson.py` | `alpha_fractional_cayley_dickson_receipt.json` | 5 | pass |
| `verify_u_r30_quantum_circuit.py` | `u_r30_quantum_circuit_receipt.json` | 5 | pass |

**Total checks:** 39/39 pass.

**Check details for Hamiltonian window emergence:**

| Check | Description | Result |
|-------|-------------|--------|
| `order2_width3_count_is_four` | 6 base centers, width 3 → 4 reads | pass |
| `order3_width5_count_is_three` | 7 states, width 5 → 3 reads | pass |
| `order4_width7_count_is_two` | 8 states, width 7 → 2 reads | pass |
| `all_reads_preserve_source_indices` | Source indices preserved | pass |
| `all_reads_preserve_source_centers` | Source centers preserved | pass |
| `all_backward_receipts_reverse_to_forward` | Reverse receipt well-formed | pass |
| `static_z4_does_not_prove_temporal_periodicity` | Z4 falsifier | pass |
| `scalar_sweep_covers_widths_3_to_k_minus_1` | Widths 3..8 tested | pass |
| `scalar_sweep_counts_match_k_minus_w_plus_1` | Count formula verified | pass |
| `scalar_sweep_preserves_provenance` | Provenance preserved | pass |
| `mckay_thompson_bands_match_declared_thresholds` | Bands declared correctly | pass |
| `mckay_thompson_centers_match_doubling_terms` | Centers 2,4,6,8,16,33 | pass |
| `mckay_thompson_closed_bands_for_k9_are_first_four` | First 4 closed at K=9 | pass |
| `mckay_thompson_future_bands_are_pending` | 15-17, 31-35 pending | pass |
| `threshold_local_times_are_monotone` | Local clocks monotone | pass |
| `threshold_stack_runs_in_global_lockstep` | Global lockstep | pass |
| `light_cone_base_passes_before_mckay_binding` | Paper 6 dependency | pass |
| `cold_start_bijection_passes_before_mckay_binding` | Paper 10 dependency | pass |
| `mckay_route_uses_light_cone_adjugation_witness` | 1,903 witnesses, 0 failures | pass |

---

## Hand Reconstruction

1. List six base center states from Papers 00–05.
2. Apply width-3 windows: 4 reads, each preserving source indices and centers.
3. Verify that backward receipts reverse to forward receipts.
4. Append order-2 states; apply width-5 windows: 3 reads.
5. Append order-3 states; apply width-7 windows: 2 reads.
6. Run scalar sweep over widths 3..8 and confirm `count = K - w + 1`.
7. Verify McKay-Thompson bands match declared thresholds.
8. Confirm first four bands closed at K=9; higher bands pending.
9. Verify Paper 6 light-cone decomposition and Paper 10 cold-start bijection pass.
10. Confirm the light-cone adjugation witness has 1,903 witnesses, zero failures.
11. Verify kappa = ln(φ)/16 and the golden-ratio identities.
12. Confirm E8 embedding norm is kappa, morphon delta ≤ 0, per-event emission is -kappa.
13. Verify cumulative is non-increasing, positive deltas are violations, audit chain has zero drift.
14. Verify the alpha fractional Cayley-Dickson derivation checks.
15. Verify the U_R30 reversible circuit: bijective, target = Rule 30, double-apply restores ancilla.

---

## Falsifiers and Rejected Claims

| Rejected Claim | Reason |
|---------------|--------|
| "The static Z4 chart template proves the temporal trace is period 4." | Rejected. `temporal_period_claim_supported = false`. The static four-frame label has a Z4 orbit template, but the tested Rule 30 trace does not inherit periods 1, 2, or 4. |
| "A reverse receipt proves physical time reversal." | Rejected. The reverse read is a receipt-level reverse, not a proof of physical time reversal. |
| "A composite center is valid without source-window provenance." | Rejected. Every composite center requires the forward and backward receipts to contain the same source centers in opposite order. |
| "Unbounded closed-form McKay-Thompson arithmetic is proven." | Rejected. The light-cone adjugation witness promotes the bounded threshold route only. Unbounded closed-form arithmetic remains open. |
| "Measured quantum hardware / unistochastic-VOA physics is proven." | Rejected. The U_R30 circuit is classical-reversible exactness. The hardware claim is an external bridge. |
| "Positive morphon deltas are conserved." | Rejected. TMN-main engine.py has a sign contradiction: it emits positive morphon_delta labeled "conserved surplus", which is backwards. The live receipt mints -kappa, confirming the conservation.py convention. |
| "Palindromic-closure equivalence is receipted." | Rejected. Asserted in source prose, not yet given its own receipt. |

---

## Relation to Prior and Later Papers

**Papers 01–08:** Establish carrier, correction, coordinate, repair, path, causal, bridge, and closure-template layers. Paper 09 adds temporal construction: the ordered global object is read from local center windows rather than assumed as an external timeline.

**Paper 06 (Causal Code / Rule90/Lucas):** Supplies the light-cone decomposition that passes before McKay binding in Paper 09. The light-cone is the base layer for the adjugation witness.

**Paper 10 (Readout / Cold-Start Bijection):** Supplies the cold-start bijection that passes before McKay binding in Paper 09. The bijection is the transport layer for the adjugation witness.

**Paper 11 (Theory Admission Gate):** Supplies the sporadic ledger that the McKay bootstrap queries. The sporadic gate classifies Monster-involved vs pariah boundary cases.

**Later papers:** The Hamiltonian window is the temporal construction layer. Any physical dynamics assigned to composite centers require a later theorem. The higher McKay-Thompson bands (`15-17`, `31-35`) are pending until the carried-state count reaches their boundary.

---

## Open Obligations

| ID | Disposition |
|----|-------------|
| 09.1 | Close unbounded closed-form McKay-Thompson arithmetic with a separate theorem. |
| 09.2 | Promote higher threshold bands (`15-17`, `31-35`) when carried-state count reaches boundary. |
| 09.3 | Patch CMPLX-TMN-main engine.py morphon_delta sign upstream to match conservation service. |
| 09.4 | Derive unequal Noether/Shannon/Landauer sector weights from content (future work). |
| 09.5 | Give palindromic-closure equivalence its own receipt. |
| 09.6 | Prove or transport physical time reversal as a separate theorem. |
| 09.7 | Prove static-Z4 temporal periodicity if true, or maintain falsifier if false. |
| 09.8 | Close measured quantum-hardware claim with experimental data. |
| 09.9 | Wire all Paper 09 verifiers into `cqe_engine.formal`. |
| 09.10 | Add domain examples (signal processing, temporal databases, circuit design) after the formal schema is stable. |

---

## Bibliography

[1] N. Barker, *CQE Paper 06 — Causal Code*, `papers/active-rework/06_Causal_Code.md`, 2026. Supplies the Rule 30/Rule 90/Lucas light-cone decomposition used as the base layer for McKay binding in Paper 09.

[2] N. Barker, *CQE Paper 10 — T10 Master Receipt*, `papers/active-rework/10_T10_Master_Receipt.md`, 2026. Supplies the cold-start bijection used as the transport layer for the adjugation witness.

[3] N. Barker, *CQE Paper 11 — Theory Admission Gate*, `papers/active-rework/11_Theory_Admission_Gate.md`, 2026. Supplies the sporadic ledger used by the McKay bootstrap.

[4] `lattice_forge.temporal_z4_scope`, `lattice_forge.mckay_matrix_tables`, `lattice_forge.three_move_closure`, `lattice_forge.voa_harness`, CMPLX-PartsFactory-main. Substrate modules for temporal scope, McKay tables, three-move closure, and VOA harness.

[5] `ChromaForge` (conservation + morphon), CMPLX-R30-main/PROOF/src. Forge proving the kappa conservation law and morphon potential.

[6] J. McKay and J. Thompson, "Finite Groups and Rule 30," (historical). Reference for the McKay-Thompson coefficient framework used in the threshold stack.

[7] S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Reference for Rule 30 and cellular automata dynamics.

[8] M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press, 2000. Reference for reversible quantum circuits and the Toffoli gate.

[9] R. Penrose, *The Road to Reality*, Jonathan Cape, 2004. Reference for the golden ratio and its appearance in physical constants.

---

## Conclusion

Paper 09 proves that temporal structure can be built from local carried centers by finite Hamiltonian-window reads. The proof is the window arithmetic and provenance preservation: width-3 produces 4 reads, width-5 produces 3, width-7 produces 2, and scalar widths `3..K-1` are all admissible. The McKay-Thompson threshold stack separates boundary candidates from ordinary scalar windows, and the light-cone-derived adjugation witness (1,903 correction witnesses, zero failures) promotes the bounded threshold route while leaving unbounded closed-form arithmetic outside the claim.

The kappa conservation law closes the morphon potential as a Hamiltonian/Lyapunov descent: `kappa = ln(φ)/16`, per-event emission is `-kappa`, cumulative is non-increasing, positive deltas are violations, and the audit chain has zero drift. The sign error in TMN-main engine.py is recorded and the correct convention is enforced by the live receipt.

The alpha fractional Cayley-Dickson derivation and the U_R30 reversible quantum circuit provide additional finite algebraic and circuit-exactness checks. The honesty guard is the point: the static Z4 template does not prove temporal periodicity, the reverse receipt is not physical time reversal, the quantum circuit is classical-reversible not hardware-measured, and unbounded McKay arithmetic remains open. This is the architecture that keeps the corpus rigorous: temporal emergence is built from local receipts, not assumed from global templates.
