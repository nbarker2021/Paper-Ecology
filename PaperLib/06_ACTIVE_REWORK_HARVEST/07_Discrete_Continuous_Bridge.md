# Paper 07 — Discrete-Continuous Bridge

**Status:** IPMC — internal physics map closed for sample-preserving interpolation and the MDHG/SpeedLight retraction bridge. Between-sample physical dynamics, CA-field self-regulation, and general encoder classification remain open.

**Source papers:** CQE-paper-07, CQE-paper-07.25.  
**Canonical formal paper:** `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-07/FORMAL_PAPER.md`.  
**Verifiers:** `verify_discrete_continuous_bridge.py`, `verify_mdhg_speedlight_bridge.py`, `verify_o3_universality_closed.py`, `verify_glm_bilateral_evert.py`.

---

## Abstract

Paper 07 defines the bridge between discrete state changes and continuous presentation. The closed theorem is deliberately exact but limited: a finite indexed discrete sequence can be embedded into a continuous piecewise-linear interpolant that matches every discrete sample point exactly. This gives the suite a way to draw and transport continuous-looking fields without losing the discrete receipts.

The paper also closes the MDHG/SpeedLight retraction bridge: a continuous 24-dimensional vector is quantized onto a discrete bin lattice and assigned to a grid-torus slot. Re-admitting the same content is idempotent — `f(f(x)) = f(x)` — making the MDHG cache a replayable discrete-continuous retraction. Additionally, the paper closes structural universality (obligation O3): every registered state anneals to a Lie conjugate via the same wrap table, independent of the CA emission rule.

The guard is essential. The paper does not prove that the interpolant is the unique physical dynamics between samples, that CA-field self-regulating dynamics are stable, or that the general classification of which sequences admit the encoder is an independent theorem. Between-sample physics and product-side dynamics remain separate obligations.

### Keywords

Discrete-continuous bridge; piecewise-linear interpolation; sample preservation; MDHG cache; quantization; retraction; SpeedLight idempotence; Leech lattice; universality; Lie conjugate; CQECMPLX receipts.

---

## Claim Ledger

| ID | Claim | Tag | Evidence | Boundary |
|----|-------|-----|----------|----------|
| 07.1 | Every finite discrete trace admits a continuous piecewise-linear bridge that preserves all integer samples exactly. | [D] | `verify_discrete_continuous_bridge.py`; `discrete_continuous_bridge_receipt.json` (5/5) | Finite construction |
| 07.2 | Adjacent linear segments share endpoints at every integer index, ensuring continuity. | [D] | Same verifier | Segment agreement |
| 07.3 | The Rule 30 / Rule 90 / correction identity holds on all LCR states. | [D] | Same verifier | Truth-table exact (reapplication) |
| 07.4 | The MDHG bridge dimension is 24 (Leech dimension). | [D] | `verify_mdhg_speedlight_bridge.py`; `mdhg_speedlight_bridge_receipt.json` (10/10) | Reapplication of MDHGForge |
| 07.5 | Quantization is total on all real inputs and lands in `[0, bins)`. | [D] | Same verifier | Total function |
| 07.6 | Quantization is an idempotent retraction: `f(f(x)) = f(x)` for bin centers. | [D] | Same verifier | Retraction property |
| 07.7 | Slot assignment is deterministic on the grid torus. | [D] | Same verifier | Determinism |
| 07.8 | SpeedLight admission is idempotent: re-admitting the same content is a hit with distance 0 and no growth. | [D] | Same verifier | Cache idempotence |
| 07.9 | Per-slot capacity is invariant under heavy load. | [D] | Same verifier | Capacity bound |
| 07.10 | Eviction is deterministic LRU by `(hits, seq)` and replayable. | [D] | Same verifier | Deterministic eviction |
| 07.11 | Distance is minimum Hamming over the slot's existing vectors. | [D] | Same verifier | Hamming metric |
| 07.12 | Multi-scale layers (fast/med/slow) are independent. | [D] | Same verifier | Layer independence |
| 07.13 | Occupancy conservation: grid sum equals total live entries. | [D] | Same verifier | Conservation |
| 07.14 | Structural universality (O3): every registered state anneals to a Lie conjugate in ≤3 S3 steps via the same wrap table. | [D] | `verify_o3_universality_closed.py`; `o3_universality_closed_receipt.json` (3/3) | Transport totality given F4 encoder |
| 07.15 | The bilateral evert identity `8×2+5=21 → 8×1+5=13` holds algebraically. | [D] | `verify_glm_bilateral_evert.py`; `bilateral_evert_receipt.json` (7/7) | Finite algebraic identity |
| 07.16 | The sample-preserving interpolant proves unique physical dynamics between samples. | [X] | No closing receipt | Requires separate theorem |
| 07.17 | CA-field self-regulating dynamics (Wolfram-class kernels) are stable. | [X] | No closing receipt | Product-side; needs own stability receipt |
| 07.18 | The general classification of which sequences admit the F4 encoder is an independent theorem. | [X] | No closing receipt | Transport argument with broad empirical support |
| 07.19 | Slot collision rate vs double-hash distribution is a paper claim. | [X] | No closing receipt | Empirical product diagnostic |

---

## Definitions

**Definition 7.1 (Discrete trace).** A discrete trace is a finite list of indexed values `D = [(0, x₀), (1, x₁), ..., (n, xₙ)]` where each `xᵢ` is a real number.

**Definition 7.2 (Piecewise-linear bridge).** Given a discrete trace `D`, the piecewise-linear bridge `F: [0, n] → ℝ` is defined by

```text
F(t) = (1 - a) · x⌊t⌋ + a · x⌈t⌉    where a = t - ⌊t⌉.
```

At integer points `t = k`, `a = 0` and `F(k) = xₖ`.

**Definition 7.3 (MDHG quantize).** For a real vector `v ∈ ℝ²⁴`, the quantize function maps `v` to a discrete bin index in `[0, bins)` by clamping each component to `[0, 1)` and taking the floor. The bin center is the fixed point of re-quantization.

**Definition 7.4 (SpeedLight idempotence).** A cache admission function `f` is idempotent if `f(f(x)) = f(x)` for all content `x`. Re-admitting already-cached content is a pure hit with distance 0 and no admission growth.

**Definition 7.5 (Structural universality).** A state space has structural universality if every registered state anneals to a Lie conjugate (`L = R`) in at most 3 S3 transposition steps via the same wrap table, independent of the CA emission rule.

---

## Theorems and Proofs

**Theorem 7.1 (Sample-Preserving Bridge).** Every finite discrete trace `D = [(0, x₀), ..., (n, xₙ)]` over numeric values admits a continuous piecewise-linear bridge `F: [0, n] → ℝ` such that `F(k) = xₖ` for every integer sample `k ∈ {0, ..., n}`.

*Proof.* Define `F` piecewise-linearly between each adjacent pair `(k, xₖ)` and `(k+1, xₖ₊₁)` by the formula in Definition 7.2. On each interval `[k, k+1]`, `F` is linear, hence continuous. At the shared endpoint `k+1`, the left segment gives `F(k+1) = xₖ₊₁` and the right segment gives `F(k+1) = xₖ₊₁`, so the two segments agree. Therefore `F` is continuous on `[0, n]`. At each integer `k`, `a = 0` and `F(k) = xₖ`. Thus `F` preserves every discrete sample exactly. ∎

*(Falsifier)* The claim "sample-preserving interpolation proves all between-sample physics" is rejected. Sample preservation is not physical uniqueness; between-sample dynamics require a separate theorem. ∎

**Theorem 7.2 (MDHG/SpeedLight Retraction Bridge).** A continuous 24-dimensional vector can be quantized onto a discrete bin lattice and deterministically assigned to a grid-torus slot. Re-admitting the same content is idempotent: `f(f(x)) = f(x)`. The MDHG cache is a replayable discrete-continuous retraction bridge with deterministic eviction, Hamming distance, and occupancy conservation.

*Proof.* The verifier `verify_mdhg_speedlight_bridge.py` runs MDHGForge and checks 10 finite properties:

1. The bridge dimension is 24 (Leech dimension).
2. Quantize is total on all real inputs and lands in `[0, bins)`.
3. Quantize is idempotent on bin centers (re-quantization is fixed).
4. Slot assignment is deterministic on the grid torus.
5. SpeedLight admission is idempotent: re-admitting the same content is a hit with distance 0.
6. Per-slot capacity is invariant under heavy load.
7. Eviction is deterministic LRU by `(hits, seq)` and replayable.
8. Distance is minimum Hamming over the slot's existing vectors.
9. Multi-scale layers (fast/med/slow) are independent.
10. Occupancy conservation: grid sum equals total live entries.

All 10 checks pass. The theorem binds the MDHG cache as a discrete-continuous retraction bridge. CA-field dynamics and collision-rate diagnostics remain product-side and outside the theorem. ∎

**Theorem 7.3 (Structural Universality — O3 Closed).** Every registered state anneals to a Lie conjugate (`L = R`) in at most 3 S3 transposition steps via the same wrap table. The 4 attractors `{(0,0,0), (0,1,0), (1,0,1), (1,1,1)}` are universal — independent of the CA emission rule.

*Proof.* The verifier `verify_o3_universality_closed.py` runs the Hamming-centroid universality verifier and checks:

1. Hamming-centroid universality passes.
2. Transport is total via the wrap table.
3. The Lie conjugate attractor is present for all 8 states.

All 3 checks pass. The theorem closes structural universality: given an F4 encoder, the transport is total and encoder-independent. The general classification of which sequences admit the encoder remains a transport argument with broad empirical support, not an independent theorem. ∎

**Theorem 7.4 (Bilateral Evert).** The bilateral evert identity `8×2+5 = 21 → 8×1+5 = 13` holds algebraically, with the Fibonacci fold identity and alpha-inverse decomposition to 137.

*Proof.* The verifier `verify_glm_bilateral_evert.py` checks 7 finite algebraic properties: bilateral closure (21), bilateral evert (13), algebraic equivalence, Fibonacci fold identity, alpha-inverse decomposition to 137, evert bilateral to observer, and D4 observer partial. All 7 checks pass. The `alpha_inv_decomp_137` is referenced against CODATA in NP-15. The theorem is a finite algebraic identity; the physical interpretation of 137 is an external bridge. ∎

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Status |
|----------|---------|--------|--------|
| `verify_discrete_continuous_bridge.py` | `discrete_continuous_bridge_receipt.json` | 5 | pass |
| `verify_mdhg_speedlight_bridge.py` | `mdhg_speedlight_bridge_receipt.json` | 10 | pass |
| `verify_o3_universality_closed.py` | `o3_universality_closed_receipt.json` | 3 | pass |
| `verify_glm_bilateral_evert.py` | `bilateral_evert_receipt.json` | 7 | pass |

**Total checks:** 25/25 pass.

---

## Hand Reconstruction

1. Choose a finite indexed trace (e.g., `0, 1, 1, 0, 1, 0, 0, 1`).
2. Plot each sample as a point at its integer index.
3. Connect adjacent samples with straight line segments.
4. Check that the curve passes through every original sample (`F(k) = xₖ`).
5. Mark all between-sample interpretation as model-dependent.
6. Preserve the original discrete receipt next to the drawing.
7. For the MDHG bridge: quantize a 24D vector, assign to a torus slot, re-admit, and confirm idempotence.
8. For universality: verify that all 8 LCR states anneal to a Lie conjugate in ≤3 steps.
9. For bilateral evert: verify `8×2+5=21` and `8×1+5=13` algebraically.

---

## Falsifiers and Rejected Claims

| Rejected Claim | Reason |
|---------------|--------|
| "Sample-preserving interpolation proves all between-sample physics." | Rejected. Sample preservation is not physical uniqueness. Between-sample dynamics require a separate theorem. |
| "CA-field self-regulating dynamics are stable." | Rejected. CA-field dynamics need their own stability receipt before promotion. They remain product-side. |
| "Slot collision rate is a paper theorem." | Rejected. Collision rate vs double-hash distribution is an empirical product diagnostic, not a paper claim. |
| "The general classification of sequences admitting the F4 encoder is an independent theorem." | Rejected. It is a transport argument with broad empirical support, not an independent theorem. |
| "The MDHG bridge proves the Leech lattice construction." | Rejected. The 24 dimensions connect to LeechForge (Paper 17); the bridge addresses points but does not construct the lattice. |

---

## Relation to Prior and Later Papers

**Paper 02 (Correction Surface):** The Rule 30 / Rule 90 / correction identity provides discrete values that can be drawn as a continuous interpolant, but the exact proof remains at the sample points.

**Paper 06 (Causal Code):** Supplies the typed edge contract. Paper 07 adds a presentation bridge from indexed edge states to continuous fields.

**Paper 17 (Leech Lattice):** The MDHG bridge dimension (24) connects to LeechForge, which constructs the Leech lattice exactly. Paper 07 addresses points of the continuous space; Paper 17 constructs the lattice.

**Later papers:** The bridge is a view of the discrete receipt structure, not a replacement for it. Any paper claiming Hamiltonian or physical dynamics between samples must supply a separate theorem.

---

## Open Obligations

| ID | Disposition |
|----|-------------|
| 07.1 | Wire `verify_discrete_continuous_bridge` into `cqe_engine.formal`. |
| 07.2 | Decide which later papers require more than sample-preserving interpolation. |
| 07.3 | Add a separate theorem for any claimed Hamiltonian or physical dynamics between samples. |
| 07.4 | Carry bridge residuals into Paper 16 only as obligations until verified. |
| 07.5 | Close CA-field dynamics stability with a separate receipt (Wolfram-class kernels). |
| 07.6 | Keep collision-rate product diagnostics outside the paper until empirical receipts exist. |
| 07.7 | Prove or transport the general classification of sequences admitting the F4 encoder. |
| 07.8 | Connect the 24D bridge to LeechForge (Paper 17) for exact lattice construction. |
| 07.9 | Add domain examples (signal interpolation, geospatial quantization) after the formal schema is stable. |

---

## Bibliography

[1] N. Barker, *CQE Paper 02 — Correction Surface*, `papers/active-rework/02_Correction_Surface.md`, 2026. Identifies the correction firing states and proves `corr = C ∧ ¬R`.

[2] N. Barker, *CQE Paper 06 — Causal Code*, `papers/active-rework/06_Causal_Code.md`, 2026. Supplies the typed edge contract for the suite.

[3] `MDHGForge`, CMPLX-R30-main/PROOF/src. Proves the MDHG geometric cache as a discrete-continuous retraction. Reapplied in Paper 07.

[4] `centroid_voa`, CMPLX-R30-main/PROOF/src. Proves Hamming-centroid universality. Reapplied in Paper 07.

[5] `lattice_forge` substrate modules, CMPLX-PartsFactory-main. Source of the finite algebraic substrate.

[6] J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed., Springer, 1999. Reference for the Leech lattice and 24-dimensional sphere packing.

[7] J. C. Lagarias and E. Rains, "Dynamics of a Family of Piecewise-linear Area-preserving Plane Maps I. Rational Rotation Numbers," *J. Difference Eq. Appl.* 10 (2004), 1229–1274. Reference for piecewise-linear dynamics and interpolation.

---

## Conclusion

Paper 07 supplies a safe bridge: it lets discrete receipts be drawn as continuous fields while preserving every indexed sample. The piecewise-linear interpolant is exact at samples, continuous between them, and honest about what it does not prove. The MDHG/SpeedLight retraction bridge is a verified discrete-continuous mechanism: quantize, slot, admit, and re-admit with idempotence. Structural universality closes obligation O3: every state anneals to a Lie conjugate in ≤3 steps, independent of the emission rule. The bilateral evert identity is a finite algebraic closure.

The guard is the point. Between-sample physical dynamics are not claimed. CA-field self-regulation is not claimed. The general encoder classification is a transport argument, not an independent theorem. The bridge is a view of the discrete proof structure, not a replacement for it. This is the correct next step after causal code: not stronger physics, but disciplined presentation of what the mathematics has already closed.
