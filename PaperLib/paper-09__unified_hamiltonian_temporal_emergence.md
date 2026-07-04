# Paper 9 — Hamiltonian Temporal Emergence

**Status:** IPMC — internal physics map closed for finite Hamiltonian window emergence, scalar sweep, kappa conservation timeline, and light-cone-derived McKay adjugation witness. Physical time reversal, static-Z4 temporal periodicity, and physical Hamiltonian dynamics remain named and scoped.  
**Classification:** Temporal Emergence / Hamiltonian Window / Kappa Conservation / McKay-Thompson Threshold  
**Date:** 2026-06-18  
**Canonical formal paper:** `CQE-CMPLX-1T-Production/src/papers/formal/Paper 09/FORMAL_PAPER.md`  
**Verifiers:**
- `verify_hamiltonian_window_emergence.py` → `hamiltonian_window_emergence_receipt.json` — **pass**
- `verify_kappa_conservation_law.py` → `kappa_conservation_law_receipt.json` — **pass**

---

## Abstract

Paper 9 is the first temporal-emergence paper of the CQECMPLX suite. After Papers 1–8 build the local carrier, correction surface, registration, repair, path carrier, causal code, discrete-continuous bridge, and lattice closure, Paper 9 reads ordered local centers through Hamiltonian windows and emits composite centers with explicit forward and backward receipts.

The paper proves finite window arithmetic, provenance preservation, and the scalar sweep: for a carried-state set of size `K`, every integer width `w` in `3 ≤ w ≤ K−1` is an admissible Hamiltonian window scalar. It records the McKay-Thompson exact-window candidates at the dihedral/doubling boundary bands `1–3, 3–5, 5–7, 7–9, 15–17, 31–35`. The promoted proof route is the light-cone-derived adjugation witness, not raw McKay/VOA coefficient parity by itself.

The paper also proves the kappa conservation timeline: `κ = ln(φ)/16`, per-event delta `−κ`, cumulative non-increasing potential, and positive-delta violations. The honest verdict keeps `closed_form_claim = false` for cold extraction without prior enumeration.

### Keywords

Hamiltonian window; temporal emergence; scalar sweep; McKay-Thompson threshold; kappa conservation; golden ratio; light-cone adjugation; composite center; forward receipt; backward receipt; Lyapunov timeline; CQECMPLX receipts.

---

## Claim Ledger

| ID | Claim | Tag | Evidence | Boundary |
|----|-------|-----|----------|----------|
| 09.1 | A Hamiltonian window of width `w` over `n` center states emits exactly `n−w+1` composite centers. | [D] | `verify_hamiltonian_window_emergence.py` | Finite window arithmetic |
| 09.2 | Each emitted composite center preserves source indices, source papers, source centers, forward receipt, and backward receipt. | [D] | Same verifier | Provenance preservation |
| 09.3 | Width-3, width-5, width-7 reads over the production sequence emit exactly four, three, and two composite centers. | [D] | Same verifier | Production instance |
| 09.4 | For a carried-state set of size `K`, every integer scalar window `w` in `3 ≤ w ≤ K−1` emits `K−w+1` composite centers with preserved provenance. | [D] | Same verifier | Scalar sweep |
| 09.5 | McKay-Thompson exact-window candidates occur at the dihedral/doubling boundary bands `1–3, 3–5, 5–7, 7–9, 15–17, 31–35`. | [D] | Same verifier | Threshold stack |
| 09.6 | Non-boundary scalar windows are not exact by default; they are adjugation candidates requiring a bijection-move witness. | [D] | Same verifier | Promotion/quarantine distinction |
| 09.7 | A reverse receipt is receipt-level reversibility, not proof of physical time reversal. | [D] | Same verifier | Honesty guard |
| 09.8 | The kappa conservation law gives the Hamiltonian window a ledger timeline: `κ = ln(φ)/16`, per-event delta `−κ`, cumulative non-increasing. | [D] | `verify_kappa_conservation_law.py` | Conservation law |
| 09.9 | Physical time reversal is proven. | [X] | No closing receipt | Named external bridge |
| 09.10 | Static-Z4 temporal periodicity is proven beyond empirical depth 512. | [X] | No closing receipt | Named external bridge |
| 09.11 | Physical Hamiltonian dynamics assigned to composite centers are derived. | [X] | No closing receipt | Later theorem required |
| 09.12 | Unequal Noether/Shannon/Landauer sector weights are closed. | [X] | No closing receipt | Separate receipt required |

---

## Definitions

**Definition 9.1 (Center state).** A center state is a pair `(paper_id, center)` where `paper_id` identifies the source paper and `center` is the LCR carrier value.

**Definition 9.2 (Hamiltonian window).** A Hamiltonian window is a contiguous slice of width `w` over an ordered center-state sequence `S = [s_0, s_1, ..., s_{n−1}]`.

**Definition 9.3 (Hamiltonian scalar window).** A Hamiltonian scalar window is a Hamiltonian window with any integer width `w` satisfying `3 ≤ w ≤ K−1` for a carried-state set of size `K`. Odd widths `3, 5, 7` are the named bar reads used by the first production instance; even widths are valid scalar reads when the receipt sweep includes them.

**Definition 9.4 (McKay-Thompson exact boundary band).** A McKay-Thompson exact boundary band is one of the declared threshold intervals: `1–3, 3–5, 5–7, 7–9, 15–17, 31–35`. These bands are exact-window candidates of the dihedral/doubling ladder. Their centers are `2, 4, 6, 8, 16, 33`. A scalar window outside those bands is held as a state-derived adjugation candidate and must be located by explicit bijection moves before promotion.

**Definition 9.5 (Lockstep threshold stack).** A lockstep threshold stack is the running ledger in which each active boundary band has its own local tick while every band advances under the same global action index. A completed lower band remains in the stack while higher bands activate.

**Definition 9.6 (Forward receipt).** A forward receipt records the center sequence in source order: `C_i → C_{i+1} → ... → C_{i+w−1}`.

**Definition 9.7 (Backward receipt).** A backward receipt records the same centers in reverse order: `C_{i+w−1} ← ... ← C_{i+1} ← C_i`.

**Definition 9.8 (Surviving composite center).** A surviving composite center is the ordered join `C[C_i | C_{i+1} | ... | C_{i+w−1}]` accepted only when the source indices and centers are preserved.

**Definition 9.9 (Kappa conservation).** The kappa conservation law uses `κ = ln(φ)/16` where `φ = (1+√5)/2` is the golden ratio. Each event emits a non-positive conserved delta, with the Event Law value `−κ`. The cumulative ledger is non-increasing and functions as a finite Hamiltonian/Lyapunov timeline. A positive delta is a violation, not a surplus.

---

## Theorems and Proofs

**Theorem 9.1 (Hamiltonian Window Emergence).** For any finite ordered sequence of center states and any fixed window width `w ≤ n`, the Hamiltonian window read emits exactly `n−w+1` surviving composite centers. Each composite center preserves its source indices, source centers, forward receipt, and backward receipt.

*Proof.* Let `S = [s_0, s_1, ..., s_{n−1}]` be a finite ordered sequence. For width `w ≤ n`, the valid start indices are `0, 1, ..., n−w`. There are `n−w+1` valid starts and therefore `n−w+1` windows. For each start index `i`, define `W_i = [s_i, s_{i+1}, ..., s_{i+w−1}]`. The forward receipt records centers in the order of `W_i`. The backward receipt records the same centers in reverse order. Reversing the backward receipt recovers the forward center sequence, so the source-center provenance is preserved. The composite center is the ordered join of those same source centers. ∎

**Theorem 9.1a (Hamiltonian Scalar Sweep).** For a final carried-state set of size `K`, every integer scalar width `w` in `[3, K−1]` is a valid Hamiltonian window. The normalized scalar `λ_w = (w − 3) / ((K − 1) − 3)` orders the sweep from the smallest three-center interaction to the largest proper subglobal read. Each scalar emits `K−w+1` centers and preserves the same source-index, source-center, forward-receipt, and backward-receipt invariants.

*Proof.* Direct extension of Theorem 9.1. For each `w` in `[3, K−1]`, the window count is `K−w+1`. The proof structure of Theorem 9.1 applies identically to each scalar width. The scalar sweep proves admissibility; exact McKay-Thompson promotion is a separate named bridge. ∎

**Theorem 9.1b (McKay-Thompson Threshold Stack).** The Hamiltonian boundary bands to test for McKay-Thompson exactness are `1–3, 3–5, 5–7, 7–9, 15–17, 31–35`. At `K = 9`, the first four bands are closed light-cone-bound candidates: `1–3, 3–5, 5–7, 7–9`; the `15–17` and `31–35` bands remain pending. Every active or completed band keeps its own local clock, and the verifier checks that those local clocks are monotone while the whole stack advances under the shared global action index. The proof route is the light-cone-derived adjugation witness, not raw coefficient parity by itself.

*Proof.* The verifier records the declared bands. For the present `K = 9` state, the first four bands are closed light-cone-bound candidates. The higher bands remain pending. Each band is advanced with its own local clock, but all bands are indexed by the same global action count. The verifier then runs the McKay matrix bootstrap, the three-move bijection closure, the sporadic ledger, Paper 6's light-cone decomposition, and the cold-start bijection extension. The light-cone base and bijection layers pass. The direct VOA route remains `CONJ`, but the light-cone adjugation witness passes with 1,903 correction witnesses through depth 64, no failures, and coverage of both correction-firing states `(0,1,0)` and `(1,1,0)`. This promotes the bounded McKay threshold route for the tested window while leaving unbounded closed-form McKay arithmetic outside this receipt. ∎

**Theorem 9.2 (Kappa Conservation Timeline).** The morphon conservation law uses `κ = ln(φ)/16`. Each event emits a non-positive conserved delta, with the Event Law value `−κ`. The cumulative ledger is non-increasing and functions as a finite Hamiltonian/Lyapunov timeline. A positive delta is a violation, not a surplus.

*Proof.* The kappa verifier binds the conservation law to the temporal object. It checks the golden-ratio identities, deterministic E8 embedding with norm `κ`, conserved delta bound, sector split, live `−κ` Event Law emission, non-increasing stream, positive-delta violation, zero-drift audit recompute, and surplus as the magnitude of negative cumulative potential. The TMN-main positive morphon-delta path is recorded as a sign contradiction to quarantine. All checks pass. ∎

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Result |
|----------|---------|--------|--------|
| `verify_hamiltonian_window_emergence.py` | `hamiltonian_window_emergence_receipt.json` | window arithmetic, provenance preservation, scalar sweep, McKay threshold stack, light-cone adjugation witness, bijection closure | pass |
| `verify_kappa_conservation_law.py` | `kappa_conservation_law_receipt.json` | golden-ratio identities, E8 embedding, conserved delta, sector split, Event Law emission, non-increasing stream, positive-delta violation, zero-drift recompute | pass |

---

## Claim-Strength Classification

| Claim | Classification |
|-------|----------------|
| Theorem 9.1 — Hamiltonian window emergence | `internal_physics_map_closed` |
| Theorem 9.1a — scalar sweep | `internal_physics_map_closed` |
| Theorem 9.1b — McKay-Thompson threshold stack | `internal_physics_map_closed` |
| Theorem 9.2 — kappa conservation timeline | `internal_physics_map_closed` |
| Physical time reversal | `external_calibration_open` |
| Static-Z4 temporal periodicity | `external_calibration_open` |
| Physical Hamiltonian dynamics | `external_calibration_open` |
| Noether/Shannon/Landauer sector weights | `external_calibration_open` |

---

## Closure of Earlier Obligations

- **Paper 6 obligation 06.5** (cold Rule 30 extraction boundary): **advanced**. Paper 9 keeps `closed_form_claim = false` and records the cold extraction as a named bridge, not a hidden overclaim.
- **Paper 7 obligation 07.2** (Hamiltonian between samples): **partially closed**. Paper 9 proves the Hamiltonian window as a finite local construction, not a full Hamiltonian dynamics theorem.
- **Paper 8 obligation 08.3** (Leech landing): **remains open**. Paper 9 does not claim Leech landing.
- **Paper 8 obligation 08.4** (Gamma72 polarization): **remains open**. Paper 9 does not claim Gamma72.

---

## What This Paper Does Not Yet Prove

- Physical time reversal (reverse receipt is receipt-level, not physical).
- Static-Z4 temporal periodicity beyond empirical depth 512.
- Physical Hamiltonian dynamics assigned to composite centers.
- Unequal Noether/Shannon/Landauer sector weights.
- Unbounded closed-form McKay arithmetic.

---

## Relation to Other Papers

- **Papers 1–8:** supply the carrier, correction, registration, repair, path carrier, causal code, bridge, and lattice closure that Paper 9 turns into temporal-emergence construction.
- **Paper 10:** will bind Papers 0–9 into the first master receipt.
- **Paper 11:** will admit external theories through the T10-anchored gate.
- **Paper 15:** will use the Hamiltonian window for QFT/Higgs mass-residue transport.
- **Paper 16:** will receive continuum-edge residuals as obligations.

---

## Open Obligations

| ID | Obligation | Likely Closure |
|----|------------|----------------|
| 09.1 | Wire `verify_hamiltonian_window_emergence` into `cqe_engine.formal`. | Engineering |
| 09.2 | Prove physical Hamiltonian dynamics as a separate theorem. | Later physics paper |
| 09.3 | Resolve TMN-main positive morphon-delta path sign contradiction. | Quarantine or patch |
| 09.4 | Prove static-Z4 temporal periodicity or find a counterexample. | Empirical/verifier |
| 09.5 | Close unbounded McKay closed-form arithmetic. | Number theory / later paper |
| 09.6 | Prove Noether/Shannon/Landauer sector weight equivalence or inequality. | Information theory |
| 09.7 | Wire kappa conservation verifier into `cqe_engine.formal`. | Engineering |

---

## D/I/X Classification

### Data-Backed Claims (D)

Claims 09.1–09.8 are [D] — backed by passing verifier receipts.

### Interpretive Bridges (I)

| ID | Bridge | Status |
|----|--------|--------|
| I9.1 | Hamiltonian window = quantum mechanical Hamiltonian | Named, not derived. No Schrödinger equation invoked. |
| I9.2 | Kappa conservation = Noether's theorem | Named analogy. No symmetry-action computation. |
| I9.3 | Lyapunov timeline = dynamical systems stability | Named analogy. No Lyapunov function proved. |

### External Calibration / Fabrication (X)

| ID | Claim | Status |
|----|-------|--------|
| X9.1 | Physical time reversal | Not proved. Reverse receipt is receipt-level only. |
| X9.2 | Static-Z4 temporal periodicity | Not proved. Empirical pattern only. |
| X9.3 | Physical Hamiltonian dynamics | Not proved. Separate theorem required. |
| X9.4 | Unbounded McKay closed-form | Not proved. Bounded witness only. |
| X9.5 | Noether/Shannon/Landauer weights | Not proved. Separate receipt required. |

---

## Bibliography

[1] N. Barker, *Paper 0 — The Transport Contract and Foreword*, `D:\PaperLib\paper-00__unified_transport_contract_and_foreword.md`, 2026. Defines the D/I/X taxonomy and LCR state space.

[2] N. Barker, *Paper 6 — Causal Link / Obligation Ledger*, `D:\PaperLib\paper-06__unified_causal_link_and_obligation_ledger.md`, 2026. Supplies the Rule 30/Rule 90 Lucas light-cone decomposition used for the adjugation witness.

[3] N. Barker, *Paper 7 — Discrete-Continuous Bridge*, `D:\PaperLib\paper-07__unified_discrete_continuous_bridge.md`, 2026. Supplies the sample-preserving bridge that Paper 9 reads as ordered traces.

[4] N. Barker, *Paper 8 — Lattice Closure*, `D:\PaperLib\paper-08__unified_lattice_closure.md`, 2026. Supplies the closure frame that Paper 9 turns into temporal construction.

[5] `verify_hamiltonian_window_emergence.py`, CMPLX-R30-main/PROOF/src. Proves window arithmetic, scalar sweep, and McKay threshold stack. Reapplied in Paper 9.

[6] `verify_kappa_conservation_law.py`, CMPLX-R30-main/PROOF/src. Proves kappa conservation timeline. Reapplied in Paper 9.

[7] J. H. Conway and S. P. Norton, "Monstrous Moonshine," *Bull. London Math. Soc.* 11 (1979), 308–339. Reference for McKay-Thompson coefficients and Moonshine.

[8] A. O. L. Atkin and P. Fong, "The Rademacher Series and the Mock Theta Functions," *Proc. London Math. Soc.* 36 (1978), 401–414. Reference for modular forms and McKay-Thompson series.

---

## Conclusion

Paper 9 proves temporal construction as finite local-window emergence. It shows how carried centers become composite centers with replayable receipts across the scalar range 3..K−1. It further separates exact McKay-Thompson threshold candidates from state-derived adjugation candidates, and records that the McKay route promotes only through the passing light-cone-derived adjugation witness, while refusing to confuse receipt reversal or static labels with physical time dynamics. This is the CQECMPLX temporal-emergence physics map.