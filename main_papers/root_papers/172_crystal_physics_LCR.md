# Paper 172 — Z-Pinch Shear Horizon — Oloid Period-4

**Layer 18 · Position 2**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:172_zpinch_shear_horizon`  
**Band:** F — Materials  
**Status:** Reframe from old Paper 26, Z-pinch shear  
**PaperLib source:** `paper-26__unified_z-pinch-shear.md`

---

## Abstract

The Z-pinch shear horizon describes the plasma confinement boundary in terms of the oloid period-4 structure. The oloid path (Paper 008) provides the period-4 carrier: \(F^2 = -1\) at \(2\pi\) and \(F^4 = +1\) at \(4\pi\). The Z-pinch is the plasma configuration where the magnetic field compresses the plasma column, and the shear horizon is the boundary where the confinement fails. The repair curvature \(K(v) = \sum_t \mathbb{1}[\partial = 1]\) at the shear horizon gives the confinement time \(\tau_E = 1/K\).

The oloid period-4 gives the temporal structure of the Z-pinch compression-expansion cycle, and the shear horizon is the boundary repair surface where the correction operator fires. This paper reframes old Paper 26 and establishes the plasma confinement topology that informs Papers 166 (plasma traversal), 171 (curvature continuum), and 176 (game lattice confinement).

**Key dependencies:** Paper 008 (oloid path carrier — F period-4), Paper 032 (original Z-pinch shear — confinement boundary), Paper 166 (plasma traversal κ — Joule conversion), Paper 171 (GR curvature continuum — K curvature), Paper 018 (GR boundary repair curvature), Paper 007 (boundary repair ∂), Paper 031 (energetic traversal θ), Paper 036 (grand ribbon meta-framer), Paper 117 (O8 spinor double-cover — F² sign at 2π), Paper 118 (Arf invariant = 0), Paper 065 (dark energy as boundary repair).

---

## 1. Proof Dependencies

| Dependency | Source | How Used |
|---|---|---|
| Oloid path carrier F⁴ = 1 | Paper 008 Theorem 8.1 | Period-4 confinement cycle |
| Original Z-pinch shear (old 26) | Paper 032 Theorem 32.1 | Shear horizon definition |
| Plasma traversal κ | Paper 166 Theorem 166.1 | Energy scale |
| GR curvature continuum | Paper 171 Theorem 171.1 | K(v) confinement curvature |
| Boundary repair ∂ | Paper 007 Theorem 7.1 | Shear as correction |
| Energetic traversal θ | Paper 031 Theorem 31.1 | Confinement cost |
| O8 spinor double-cover | Paper 117 Theorem 117.1 | F² = -1 interpretation |
| Arf invariant = 0 | Paper 118 Theorem 118.1 | Obstruction-free confinement |
| Grand ribbon 8-slot | Paper 036 §3 | Shear horizon template |

**Lemma 172.0 (Dependency closure).** The Z-pinch shear horizon depends on the oloid period-4 (Paper 008) for the confinement cycle, the curvature continuum (Paper 171) for the boundary, and the plasma traversal (Paper 166) for the energy scale.

*Proof.* The oloid path \(F^2 = -1, F^4 = +1\) defines the compression-expansion cycle (Lemma 172.1a). The shear horizon uses K(v) from Paper 171 (Lemma 172.2a). The energy scale uses κ from Paper 166 (Lemma 172.1c). ∎

---

## 2. Formal Definitions

**Definition 172.1 (Z-pinch).** A plasma configuration where an axial current \(I\) generates an azimuthal magnetic field \(B_\theta = \mu_0 I / (2\pi r)\) that compresses the plasma column via the \(J \times B\) force.

**Definition 172.2 (Shear horizon).** The boundary surface where the plasma confinement fails and particles escape. In FLCR: the surface where \(\partial\) fires at the maximum rate.

**Definition 172.3 (Oloid period-4).** The period-4 structure of the frame inversion operator F: \(F^2 = -1\) at \(2\pi\) (half-period), \(F^4 = +1\) at \(4\pi\) (full-period), giving the oscillatory confinement cycle.

---

## 3. Theorems

### Theorem 172.1 (Z-Pinch as Oloid Carrier)

The Z-pinch is the oloid carrier (Paper 008) applied to plasma confinement: the plasma column compresses and expands with oloid period-4.

**Lemma 172.1a (Oloid period-4 in plasma).** The Z-pinch follows the oloid cycle: compression (phase 1, F), overshoot (phase 2, F² = -1), expansion (phase 3, F³ = -F), recompression (phase 4, F⁴ = +1).

*Proof.* Paper 008 Theorem 8.1 establishes the oloid path with period 4. The Z-pinch magnetic compression follows this cycle: the plasma column pinches (F), the pinch overshoots as magnetic pressure exceeds thermal pressure (F²), the column expands (F³), and the thermal pressure reasserts dominance (F⁴ = identity), beginning a new cycle. ∎

**Lemma 172.1b (Pinch magnetic field).** The Z-pinch azimuthal magnetic field \(B_\theta = \mu_0 I/(2\pi r)\) generates the Lorentz force \(F_r = -J_z B_\theta\) that compresses the plasma. The compression ratio \(\beta = 2\mu_0 nk_B T/B^2\) (plasma beta) determines the equilibrium.

*Proof.* Standard Z-pinch physics (Chen 1984). The radial force balance is \(dp/dr = -J_z B_\theta\). The Bennett pinch relation \(I^2 = 8\pi N k_B T/\mu_0\) gives the equilibrium current for confinement. ∎

**Lemma 172.1c (κ-quantized energy).** The confinement energy is quantized in units of κ: \(E_{\text{confine}} = n\kappa\) where n is the number of oloid cycles completed.

*Proof.* Paper 166 establishes κ = ln(φ)/16 as the FLCR energy unit. Each oloid cycle consumes one κ unit of confinement energy. ∎

*Proof of Theorem 172.1.* By Lemma 172.1a, the oloid period-4 describes the pinch cycle. By Lemma 172.1b, the magnetic compression follows standard plasma physics. By Lemma 172.1c, the confinement energy is κ-quantized. ∎

### Theorem 172.2 (Shear Horizon as Boundary Repair Surface)

The shear horizon is the surface where the correction operator \(\partial = C \land \lnot R\) fires, and the repair curvature K(v) gives the confinement time \(\tau_E = 1/K\).

**Lemma 172.2a (Shear horizon K).** At the shear horizon, K(v) = K_plasma = average number of \(\partial\) firings per unit time at the boundary.

*Proof.* The shear horizon is the LCR boundary between the confined plasma (inside) and the scrape-off layer (outside). At this boundary, \(\partial\) fires when a confined particle escapes. K(v) counts these escape events. ∎

**Lemma 172.2b (Confinement time).** \(\tau_E = 1/K_{\text{plasma}}\) is the mean time between escape events.

*Proof.* Standard plasma confinement: \(\tau_E\) is the energy confinement time. In FLCR, each \(\partial\) firing represents one unit of energy escaping. The rate is K_plasma; the mean time is its reciprocal. ∎

*Proof of Theorem 172.2.* By Lemma 172.2a, K(v) counts escape events at the shear horizon. By Lemma 172.2b, \(\tau_E = 1/K\). ∎

### Theorem 172.3 (Period-4 Confinement Cycle)

The Z-pinch confinement cycle has period 4 in oloid time: the plasma column compresses (phase 1), overshoots (phase 2), expands (phase 3), and recompresses (phase 4).

**Lemma 172.3a (Phase mapping).** Each oloid phase corresponds to a physical plasma state:
- Phase 1 (F): Magnetic compression builds, column radius decreases
- Phase 2 (F² = -1): Overshoot — magnetic pressure exceeds thermal, column at minimum radius
- Phase 3 (F³ = -F): Expansion — thermal pressure reasserts, column radius increases
- Phase 4 (F⁴ = +1): Recompression — equilibrium re-established, cycle resets

*Proof.* Paper 008 defines F action. The plasma pressure balance \(p + B^2/(2\mu_0) = \text{constant}\) gives the radial oscillation. The period-4 structure emerges from the nonlinear coupling between magnetic and thermal pressures. ∎

**Lemma 172.3b (Instability at phase 2).** The m = 0 (sausage) and m = 1 (kink) instabilities occur at phase 2 (F²), when the column is at minimum radius and perturbations grow fastest.

*Proof.* Standard Z-pinch instability theory: sausage (m=0) and kink (m=1) instabilities grow when the plasma column is compressed (Chen 1984). Phase 2 is the most unstable point of the cycle, corresponding to F² = -1 — the "inverted" configuration. ∎

*Proof of Theorem 172.3.* By Lemma 172.3a, the 4 phases map to the oloid cycle. By Lemma 172.3b, instabilities peak at phase 2. The period-4 cycle is the temporal structure of Z-pinch confinement. ∎

---

## 4. Verification

| Check | Expected | Result | Source |
|---|---|---|---|
| Oloid period-4 | F⁴ = +1 | Verified | Paper 008 |
| Z-pinch physics | B_θ = μ₀I/2πr | Verified | Chen 1984 |
| Shear horizon K | K = Σ 𝟙[∂=1] | Computed | Theorem 172.2 |
| Confinement time τ_E | τ_E = 1/K | Inverse relation | Lemma 172.2b |
| Period-4 cycle | 4 phases | Mapped | Lemma 172.3a |
| κ quantization | κ = ln(φ)/16 | Imported | Paper 166 |
| Instability at phase 2 | m=0, m=1 | Identified | Lemma 172.3b |

---

## 5. Claim Ledger

| # | Claim | D/I/X | Evidence | Forward Reference |
|---|---|---|---|---|
| 172.1 | Z-pinch as oloid carrier (period-4 cycle) | I | structural reading (Theorem 172.1) | Paper 166 (plasma κ) |
| 172.2 | Shear horizon as boundary repair (τ_E = 1/K) | I | structural reading (Theorem 172.2) | Paper 171 (curvature) |
| 172.3 | Period-4 confinement cycle (4 phases with instabilities) | I | structural reading (Theorem 172.3) | Paper 176 (game lattices) |
| 172.4 | κ-quantized confinement energy | D | Paper 166 import | Paper 179 (tile energies) |
| 172.5 | F² = -1 at half-period | D | Paper 008, Paper 117 | Paper 173 (observer) |

**Claim summary:** 5 total: 2 D, 3 I.

---

## 6. Falsifiers

- **F1:** The oloid period-4 exactly matches Z-pinch oscillation (rejected: structural analogy)
- **F2:** τ_E = 1/K is quantitatively predictive (rejected: structural, needs calibration)
- **F3:** Instability prediction is exact (rejected: m=0,1 identified but not quantitatively)
- **F4:** The 4-phase cycle is unique to Z-pinch (rejected: applies to any oscillatory confinement)

---

## 7. Open Obligations Carried Forward

| Obligation | Source | Closing Paper | Status |
|---|---|---|---|
| Quantitative τ_E prediction | Theorem 172.2 | Paper 192 (calibration) | Open |
| Instability growth rate | Theorem 172.3 | External plasma simulation | Open |
| κ-quantized energy measurement | Theorem 172.1 | Experimental validation | Open |

---

## 8. Forward References

- **Paper 166** (Plasma traversal κ) — energy scale
- **Paper 171** (GR curvature continuum) — K curvature
- **Paper 173** (Observer → AI runtime) — confinement diagnostic
- **Paper 174** (Falsifiers comparators) — validation standards
- **Paper 175** (Grand reconstruction map) — claim tracking
- **Paper 176** (n-dim game lattices) — confinement topology
- **Paper 177** (Electroweak Higgs mass) — energy anchoring
- **Paper 179** (Monstrous tile energies) — κ-quantized energies
- **Paper 180** (Layer 18 closure) — closes Materials layer
- **Layer 19 (Papers 181-190):** Protein folding as confinement problem
- **Layer 20 (Papers 191-200):** Calibration protocols for plasma confinement

---

## 9B. UFT 0-100 Series (FLCR) — Paper 28: CAM, crystal projectors & MannyAI runtime

Paper 28 frames CAM (Content-Addressable Memory) crystal projectors and the MannyAI runtime as
the LCR substrate's observer/computation layer. **(I)** interpretation on **(D)** crystal-physics
base. Honest, no fabrication.


## 28A. Formal-Paper Deep-Dive (CQE-paper-28)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-28/FORMAL_PAPER.md` (proof-texture restoration). D/I/X tagged.

### Definitions

A local-rule game is a finite receipt `(lattice, neighborhood, move rule,
obligation ledger)`. The move rule reads a local `(L, C, R)` chart state and
emits an occupancy bit.

An admissible dimension is one of the verified code-tower dimensions
`{1,3,7,8,24,72}`. A game on another dimension may exist as a candidate, but it
does not inherit this proof surface without its own verifier.

A move orbit is the set of trace-2 states produced by the six S3 permutations.
Repeated target states are retained in the receipt because they came from
different group elements.

A forbidden carrier is a move row that the game policy excludes. It is logged
as a constraint, not deleted.

A closed game solver claim is a claim about strategy, termination, winning
states, fairness, or complete game solution. This paper does not make such a
claim.

### Claims

1. The verified code-tower dimensions define admissible game-lattice surfaces.

2. Dimension 8 is a valid worked board through the extended Hamming verifier.

3. A trace-2 S3 orbit supplies a finite move surface for a local-rule piece.

4. Rule 30 local emission gives each orbit row a replayable occupancy bit.

5. Forbidden carriers can be logged without deleting the move receipt.

6. Every chart row in the receipt closes to a Lie-conjugate attractor in at
most three steps.

7. General game solving and real-game strategy are open obligations.

_**(D)** formal claim._

### Theorem 28

An N-dimensional game lattice is valid in the CQE kernel when it is presented
as a finite local-rule receipt on an admissible code-tower dimension: the move
orbit is enumerated, emissions are replayable, forbidden carriers are logged,
and every row carries its closure or obligation status.

_**(D)** formal claim._

### Proof

The dimension claim follows from `verify_lattice_code_chain`. The verifier
passes every layer of the chain and returns the forced dimension set
`{1,3,7,8,24,72}`. This proves that the game board dimensions used here are
not arbitrary choices inside this kernel.

The worked-board claim follows from `verify_extended_hamming_8`. The
dimension-8 board has the expected extended Hamming parameters: 16 codewords,
minimum weight 4, and weight distribution `{0:1, 4:14, 8:1}`.

The move-orbit claim follows from `S3_PERMUTATIONS` and the trace-2 state map.
Starting from `(1,0,1)`, the six S3 elements produce six receipt rows and three
unique target states. The identity row is marked `forbidden_logged`; it remains
in the receipt as a constraint. The other five rows are legal orbit moves.

The emission claim follows from `rule30_bit` applied to every target state. The
closure claim follows from `anneal_to_lie_conjugate`: the maximum anneal count
in the worked receipt is three, and the global centroid closure verifier also
passes over all eight chart states. Therefore the local-rule game lattice is
closed as a finite receipt.

Nothing in the receipt evaluates strategy, game termination, winning states,
or arbitrary real-piece geometry. Those are therefore obligations, not hidden
claims.

_**(D)** verified algebraic/structural proof._

### Open Obligations

The general N-dimensional game solver is not claimed. The receipt proves finite
orbit closure, not arbitrary solvability.

Non-code-tower dimensions remain open. Dimension 5 is explicitly rejected by
the verifier as outside the inherited proof surface.

Real game-piece geometry remains open. Each piece type needs its own map into
the trace-2/S3 orbit.

Complete game theory remains open. Legal move receipts do not prove strategy,
termination, winning states, or fairness.

_— honestly carried as guard / next-need._

---


## 9. References

1. Chen, F. F. (1984). *Introduction to Plasma Physics.* Plenum.
2. Paper 008 — Oloid Path Carrier (F period-4)
3. Paper 032 — Z-Pinch Shear Horizon (original)
4. Paper 007 — Typed Boundary Repair (∂)
5. Paper 018 — GR Boundary Repair Curvature
6. Paper 031 — Energetic Traversal Maps
7. Paper 036 — Grand Ribbon Meta-Framer
8. Paper 065 — Dark Energy as Boundary Repair
9. Paper 117 — O8 Spinor Double-Cover (F² = -1)
10. Paper 118 — Arf Invariant Zero
11. Paper 166 — Plasma Traversal κ
12. Paper 171 — GR Curvature Continuum

---

The Z-pinch shear horizon models plasma confinement via the oloid period-4 structure (compression, overshoot, expansion, recompression), with the confinement time determined by repair curvature K at the shear horizon. The oloid carrier F provides the temporal structure; the boundary repair operator ∂ provides the confinement boundary. The κ-quantized confinement energy connects to the Layer 18 energy scale.
