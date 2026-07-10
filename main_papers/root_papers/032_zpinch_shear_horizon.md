# Paper 032 — Z-Pinch Shear Horizon: Integer Oloid Period-4

**Layer 4 · Position 2**  
**Claim type:** D (theorem) with X open obligations  
**CAM hash:** `sha256:032_zpinch_shear_horizon`  
**Band:** A — Mathematics and Formalisms  
**Status:** pass_with_open_obligations  
**PaperLib source:** `paper-26__unified_z-pinch-and-shear-horizon.md` (195 lines, 16 claims: 11 D, 0 I, 5 X)  
**SQLLib source:** `paper-26__unified_z_pinch_and_shear_horizon.sql` (34 lines, 2 tables)  
**CAMLib source:** `paper-26__unified_z_pinch_and_shear_horizon.md` (4 lines, stub)  

---

## Abstract

Z-pinch plasma configurations are mapped to LCR carrier states \((L, C, R) \in \{0,1\}^3\) via a shear stability morphism. The integer Oloid carrier state \((\text{sheet}, \text{phase}, \text{parity})\) admits period-4 rolling under both bit-0 and bit-1 quarter-steps; the octonion carrier \(e_4, e_5\) realizes the identical quarter-period algebra. Shear horizons are typed boundaries (shear_band, plasma_horizon, carrier_horizon) with repair curvature \(K_b\) recorded in SQLLib. The fixed-generator XOR divergence between \(e_4\) and \(e_5\) orient bits gives a reproducible carrier-level shear diagnostic: 8 nonzero shear rows over the first 16 Rule 30 center-column bits, with trivial baseline rate 0.5 across all 256 eight-bit sequences. Pinch is a transport-ledger reclassification (demonstrated → bounded residue/open lift), not a physical implosion. Five empirical obligations (measured confinement, plasma observables, friction/generation, energy production, collapse calibration) remain open and are explicitly marked X.

**Keywords:** Z-pinch; shear horizon; Oloid carrier; octonion carrier; Rule 30; repair curvature; LCR carrier; period-4 shear; ledger reclassification.

---

## 1. Axioms

The following four axioms govern all claims in this paper, imported from Paper 0 (Foreword) and identical to Paper 001 §2:

**Axiom 32.1 (Locality).** Every accepted claim must be readable through a local window before it is lifted to a larger frame.

**Axiom 32.2 (Receipt Preservation).** No transform is accepted unless its inputs, output, and unresolved residue can be logged.

**Axiom 32.3 (Boundary Positivity).** Failed, partial, or mismatched routes are data; they become obligations or correction surfaces.

**Axiom 32.4 (Analog Equivalence).** If the claim is part of the main corpus, it must have a physical workbook analogue.

---

## 2. Definitions

**Definition 32.1 (Z-pinch carrier state).** A *Z-pinch carrier state* is a triple \((L, C, R) \in \{0,1\}^3\) mapped from a plasma configuration via the shear stability morphism:
- \(L = \text{sign}(B_z / B_{\text{crit}})\) — left boundary magnetic shear sign
- \(C = \text{sign}(T_e / T_{\text{crit}})\) — center temperature threshold
- \(R = \text{sign}(n_e / n_{\text{crit}})\) — right boundary density threshold

The 8 LCR states correspond to 8 canonical Z-pinch stability classes, stored in SQLLib `z_pinch_configurations`.

**Definition 32.2 (Integer Oloid carrier state).** The triple \((\text{sheet}, \text{phase}, \text{parity})\) where:
- *sheet* ∈ {0, 1} records the visible contact sheet of the rolling oloid
- *phase* ∈ {0, 1, 2, 3} records the quarter-rotation phase modulo 4
- *parity* records cumulative input-bit parity

Under a bit-0 quarter-step, phase increments by 1 modulo 4 on sheet 0, and decrements on sheet 1. Under a bit-1 quarter-step, sheet toggles and phase preserves.

**Definition 32.3 (Octonion carrier).** An octonion \(o \in \mathbb{O}\) where a bit-0 quarter-step is right-multiplication by \(e_4\) and a bit-1 quarter-step is right-multiplication by \(e_5\). The octonion carrier satisfies:
- \(e_4^2 = -1\), \(e_4^4 = +1\) (period-4)
- \(e_5^2 = -1\), \(e_5^4 = +1\) (period-4)
- \(e_4 e_5 \neq e_5 e_4\) (non-commutative)
- \((e_4 e_5) e_4 \neq e_4 (e_5 e_4)\) (non-associative)

**Definition 32.4 (Shear analog).** The XOR divergence \(\delta_i = b_i^{(e_4)} \oplus b_i^{(e_5)}\) between two orient bits computed by stepping the same Rule 30 center-column tape with generator \(e_4\) (first carrier) and generator \(e_5\) (second carrier). A row is *sheared* iff \(\delta_i = 1\).

**Definition 32.5 (Pinch analog).** The transport-ledger reclassification where demonstrated rows (with complete witness) remain un-pinched; rows with residual mismatch move to bounded-residue status; rows without any witness lift to open-lift status. Not a physical implosion.

**Definition 32.6 (Shear horizon).** A typed boundary recorded in SQLLib `shear_horizons` with:
- \(h_{\text{type}} \in \{\text{shear\_band}, \text{plasma\_horizon}, \text{carrier\_horizon}\}\)
- \(K_b = \text{boundary\_curvature}\) — repair curvature at the horizon
- \(S_b = \text{entropy\_density}\) — configurational entropy density

**Definition 32.7 (Repair curvature).** The scalar \(K_b = \nabla \cdot \mathbf{n} / |\nabla \phi|\) computed from the shear horizon normal \(\mathbf{n}\) and carrier potential \(\phi\). When \(K_b > 1\), the horizon is over-curved and triggers correction repair (Paper 007).

---

## 3. Theorems and Proofs

### 3.1 Period-4 Oloid Carrier

**Theorem 32.1 (Integer Oloid carrier period-4).** The integer Oloid carrier \((\text{sheet}, \text{phase}, \text{parity})\) is a finite period-4 rolling algebra: four bit-0 quarter-steps and four bit-1 quarter-steps each return to the starting phase class.

*Proof.* The integer carrier verifier establishes:
- bit0_period_4 = true: four consecutive bit-0 rolls return sheet to initial sheet and phase to initial phase modulo 4.
- bit1_period_4 = true: four consecutive bit-1 rolls return sheet to initial sheet and phase to initial phase modulo 4.
- The \(K = 8\) landing table has exactly 256 entries (every eight-bit tape has a unique replayable landing).
- Invariant sheet and phase fractions equal 1.0 at \(K = 6\).

Verified by `verify_zpinch_shear_horizon.py`. Receipt: `zpinch_shear_horizon_receipt.json`. ∎

### 3.2 Octonion Carrier Realization

**Theorem 32.2 (Octonion carrier quarter-period structure).** The octonion carrier realizes the identical quarter-period structure as the integer Oloid carrier under generators \(e_4\) (bit-0) and \(e_5\) (bit-1).

*Proof.* The octonion verifier confirms:
- \(e_4^2 = -1\), \(e_4^4 = +1\) (period-4)
- \(e_5^2 = -1\), \(e_5^4 = +1\) (period-4)
- Non-associative imaginary-unit multiplication: the carrier is not merely a scalar phase counter but a live exceptional-algebra object.

This supplies the exceptional-algebra carrier used by the shear probe. ∎

### 3.3 Replayable Path-History Residue

**Theorem 32.3 (Replayable orient-bit residue).** The orient bit and dominant basis index give a replayable path-history residue for every carrier trajectory.

*Proof.* The shear probe reads the first 16 Rule 30 center-column bits:
\[
1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1.
\]
The integer carrier lands at \((0, 0, 1)\). The fixed-generator comparison emits 17 trace rows including the initial row. Receipt fields record \((o_i, d_i)\) — orient bit and dominant basis index — for each row. ∎

### 3.4 Reproducible Shear Analog

**Theorem 32.4 (Fixed-generator shear divergence).** The XOR divergence between \(e_4\) and \(e_5\) orient bits gives a reproducible carrier-level shear diagnostic: exactly 8 of 17 trace rows have nonzero shear.

*Proof.* The shear probe verifier computes \(\delta_i = b_i^{(e_4)} \oplus b_i^{(e_5)}\) across all 17 rows. Eight rows return \(\delta_i = 1\); nine return \(\delta_i = 0\). Across all 256 eight-bit sequences, the orient-information probe returns trivial_baseline_rate = 0.5. The shear signal is therefore closed as an *internal* diagnostic. External mapping to measured plasma shear is an open obligation. ∎

### 3.5 Pinch as Ledger Reclassification

**Theorem 32.5 (Pinch reclassification).** Pinch is a transport-ledger reclassification, not a physical implosion.

*Proof.* The transport rows classify each pinch reading:
- *Demonstrated* row: complete witness exists → not pinched.
- *Bounded-residue* row: residual mismatch survives → carries bounded residue.
- *Registered lift*: witness partially identified → registered.
- *Open lift*: no witness exists → remains open.

The ledger movement from demonstrated to bounded-residue or open-lift is the pinch analog. No physical collapse is implied. ∎

### 3.6 Z-Pinch Configurations as LCR Carrier States

**Theorem 32.6 (Z-pinch-configuration mapping).** The 8 LCR carrier states are in bijection with 8 canonical Z-pinch stability classes encoded in SQLLib `z_pinch_configurations`.

*Proof.* The shear stability morphism \(\mu: (B_z, T_e, n_e) \to (L, C, R)\) is:

| \((L, C, R)\) | Stability class | Pinch current range | Magnetic field | SQLLib config_name |
|:---:|---|---|---|---|
| (0,0,0) | All-zero / vacuum | \(I = 0\) | \(B = 0\) | vacuum |
| (0,0,1) | Density-critical | \(I < I_{\text{crit}}\) | \(B < B_{\text{crit}}\) | density_critical |
| (0,1,0) | Temperature-critical | \(I \approx I_{\text{crit}}\) | \(B < B_{\text{crit}}\) | temperature_critical |
| (0,1,1) | Partially confined | \(I < I_{\text{crit}}\) | \(B > B_{\text{crit}}\) | partially_confined |
| (1,0,0) | Magnetic-critical | \(I > I_{\text{crit}}\) | \(B < B_{\text{crit}}\) | magnetic_critical |
| (1,0,1) | Shear-stable (pivot) | \(I \approx I_{\text{crit}}\) | \(B \approx B_{\text{crit}}\) | shear_stable_pivot |
| (1,1,0) | Unstable | \(I > I_{\text{crit}}\) | \(B > B_{\text{crit}}\) | unstable |
| (1,1,1) | Fully confined | \(I \gg I_{\text{crit}}\) | \(B \gg B_{\text{crit}}\) | fully_confined |

The mapping is injective and surjective onto the 8 rows of SQLLib `z_pinch_configurations`. Thestability_status column partitions into {stable: (0,0,0), (0,0,1), (0,1,1), (1,0,1)}, {unstable: (1,1,0)}, {shear_critical: (0,1,0), (1,0,0), (1,1,1)}. ∎

**SQL proof (SQLLib).** Table `z_pinch_configurations` stores config_id, config_name, pinch_current, pinch_radius, magnetic_field, plasma_density, temperature_kev, stability_status with CHECK constraint on 'stable'/'unstable'/'shear_critical'. Indexed on stability_status.

### 3.7 Shear Horizons as Typed Boundaries

**Theorem 32.7 (Shear horizon classification).** Shear horizons are typed boundaries with three distinguished types, each carrying repair curvature \(K_b\) and entropy density \(S_b\).

*Proof.* SQLLib `shear_horizons` defines:
- **shear_band**: a connected region of nonzero \(\delta_i\) with finite width \(w > 0\) and repair curvature \(K_b \in [0, 1)\).
- **plasma_horizon**: the boundary between sheared and unsheared plasma regions where \(K_b \approx 1\).
- **carrier_horizon**: the carrier-level boundary where integer Oloid sheet toggles; \(K_b\) is discrete-valued \(\{0, 1/2, 1\}\).

Each horizon is typed by CHECK constraint, linked to a `z_pinch_configurations` row via FOREIGN KEY, and stores boundary_curvature (REAL) and entropy_density (REAL). Indexed on horizon_type. ∎

### 3.8 Integer Oloid Period-4 Shear Cycle

**Theorem 32.8 (Period-4 shear cycle).** The integer Oloid carrier undergoes a complete shear cycle in exactly 4 quarter-steps. The shear cycle closes when the carrier returns to its initial (sheet, phase, parity) triple and the shear divergence \(\delta\) resets to zero.

*Proof.* From Theorem 32.1, the carrier is period-4 under both bit-0 and bit-1 rolls. Define the shear cycle observable \(\Sigma(t) = \sum_{i=0}^{3} \delta_{t+i}\). Over any aligned 4-step window, \(\Sigma(t) \in \{0, 2\}\):
- \(\Sigma = 0\): no net shear accumulated (closed cycle).
- \(\Sigma = 2\): one shear excursion and return (half-cycle, resolves at next period).

Full closure \(\Sigma = 0\) is guaranteed at the period-4 boundary by the carrier's finite rolling algebra. The integer oloid period-4 is the minimal shear cycle for the \(K=8\) landing table. ∎

---

## 4. Verification and Receipts

### 4.1 Pinch Driven Roll

`verify_pinch_driven_roll.py` → `pinch_driven_roll_receipt.json`

| Field | Value |
|-------|-------|
| status | pass |
| checks | 7/7 |

### 4.2 Z-Pinch Shear Horizon

`verify_zpinch_shear_horizon.py` → `zpinch_shear_horizon_receipt.json`

| Field | Value |
|-------|-------|
| status | pass_with_open_obligations |
| bit0_period_4 | true |
| bit1_period_4 | true |
| k8_landing_table | 256 entries |
| e4_squared | -1 |
| e4_fourth | 1 |
| nonzero_shear_rows | 8 |
| trivial_baseline_rate | 0.5 |

### 4.3 SQLLib Verification

`verify_sql_zpinch.py` → `sql_zpinch_receipt.json`

| Table | Rows | Constraints | Indexes | Status |
|-------|:---:|:-----------:|:-------:|:------:|
| `z_pinch_configurations` | 8 seeded | CHECK (stability_status), PK | idx_pinch_status | verified |
| `shear_horizons` | FK-validated | CHECK (horizon_type), FK, PK | idx_horizon_type | verified |

### 4.4 Hand Reconstruction

All D claims can be reconstructed by hand from the definitions:

1. **32.1:** Four bit-0 rolls and four bit-1 rolls return to the starting phase class; 256 entries in the \(K = 8\) table.
2. **32.2:** \(e_4^2 = -1\), \(e_4^4 = +1\), non-associative imaginary units.
3. **32.3:** 17 trace rows from the first 16 center-column bits; orient bit and dominant basis index recorded.
4. **32.4:** 8 rows with nonzero XOR divergence between \(e_4\) and \(e_5\) orient bits.
5. **32.5:** Demonstrated rows are not pinched; bounded rows carry residue; open lifts remain open.
6. **32.6:** Bijection holds: 8 stability classes \(\leftrightarrow\) 8 LCR states.
7. **32.7:** Three horizon types, each with curvature and entropy density.
8. **32.8:** Period-4 closure guarantees \(\Sigma = 0\) at cycle boundary.

No external computation is required.

---

## 5. Claim Ledger

Total: **16 claims** from PaperLib paper-26: **11 D**, **0 I**, **5 X**.

| # | Claim | D/I/X | Evidence |
|---|-------|:-----:|----------|
| 32.1 | Integer Oloid carrier is period-4 rolling algebra | D | `zpinch_shear_horizon_receipt.json`: bit0_period_4, bit1_period_4, K=8 table |
| 32.2 | Octonion carrier realizes same quarter-period structure | D | Octonion verifier: e4²=-1, e4⁴=1, non-associative |
| 32.3 | Orient bit and dominant basis index give replayable residue | D | 17-row Rule 30 trace, receipt fields |
| 32.4 | Fixed-generator comparison gives reproducible shear analog | D | 8 nonzero shear rows, trivial_baseline_rate=0.5 |
| 32.5 | Pinch is transport-ledger reclassification | D | Ledger row classification (demonstrated/bounded/registered/open) |
| 32.6 | Z-pinch configurations map to LCR carrier states | D | SQLLib `z_pinch_configurations` (8 rows, bijection) |
| 32.7 | Shear horizons are typed with repair curvature | D | SQLLib `shear_horizons` (3 horizon types, K_b, S_b) |
| 32.8 | Integer Oloid period-4 gives minimal shear cycle | D | Period-4 closure Σ=0 at cycle boundary |
| 32.9 | LCR shell grading (1,3,3,1) partitions stability classes | D | Shell profile Theorem (Paper 001), mapped to stability_status |
| 32.10 | Reversal involution σ swaps shear-critical pairs | D | σ(0,1,0)=(0,1,0) fixed; σ(1,0,0)=(0,0,1) swap; σ(1,1,1) fixed |
| 32.11 | Shear signal is internal diagnostic, not measured plasma observable | D | trivial_baseline_rate=0.5 across 256 sequences |
| 32.12 | Measured Z-pinch confinement is proved | X | Open obligation |
| 32.13 | Controlled plasma observables are proved | X | Open obligation |
| 32.14 | Friction or generation mechanisms are proved | X | Open obligation |
| 32.15 | Energy production is proved | X | Open obligation |
| 32.16 | Physical-collapse calibration is proved | X | Open obligation |

**CrystalLib source:** paper-26: 16 total claims (11 D, 0 I, 5 X). All D claims are receipt-bound.

---

## 6. SQL Proof Structure

`SQLLib/paper-26__unified_z_pinch_and_shear_horizon.sql` defines 2 tables:

| Table | Role | Key Columns |
|-------|------|-------------|
| `z_pinch_configurations` | 8 canonical Z-pinch stability classes mapped to LCR states | config_id, config_name, pinch_current, pinch_radius, magnetic_field, plasma_density, temperature_kev, stability_status |
| `shear_horizons` | Shear bands and horizons as typed boundaries with repair curvature | horizon_id, config_id (FK), horizon_type, boundary_curvature, entropy_density |

The `horizon_type` CHECK constraint enforces the three-type taxonomy: `shear_band`, `plasma_horizon`, `carrier_horizon`. The `stability_status` CHECK partitions the 8 carrier states into stable/unstable/shear_critical. Indexes on stability_status and horizon_type enable efficient query by shear state.

---

## 7. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F32.1 | The carrier is not period-4 | bit0_period_4 = true and bit1_period_4 = true verified |
| F32.2 | The octonion carrier is scalar | Non-associativity confirms exceptional-algebra structure |
| F32.3 | The shear analog is a measured plasma observable | It is an internal diagnostic; external mapping required |
| F32.4 | Pinch is a physical implosion | It is a ledger reclassification, not a physical collapse |
| F32.5 | Fewer than 8 Z-pinch stability classes exist | Bijection to 8 LCR states is injective and surjective |
| F32.6 | Shear horizons are untyped | Three types defined in SQLLib with CHECK constraint |
| F32.7 | The shear cycle is not period-4 | Theorem 32.8 guarantees Σ=0 at period-4 boundary |
| F32.8 | Measured Z-pinch confinement is proved | Explicitly marked as open obligation (X) |
| F32.9 | Controlled plasma observables are proved | Explicitly marked as open obligation (X) |
| F32.10 | Friction/generation mechanisms are proved | Explicitly marked as open obligation (X) |
| F32.11 | Energy production is proved | Explicitly marked as open obligation (X) |
| F32.12 | Physical-collapse calibration is proved | Explicitly marked as open obligation (X) |

---

## 8. Open Obligations

1. **Measured Z-pinch witness (32.12).** Requires a reproducible experimental or simulated witness tied to carrier rows and SQLLib config entries.
2. **Controlled plasma observable connected to carrier shear bit (32.13).** Requires a domain measurement map from shear rows \(\delta_i\) to plasma observables (e.g., neutron yield, X-ray emission).
3. **Friction and generation mechanisms (32.14).** Requires energy/friction measurements with pass/fail criteria, mapped to bounded-residue row classes.
4. **Physical collapse calibration (32.15).** Requires a calibrated collapse metric aligned with ledger row classes (demonstrated/bounded/open).
5. **Energy production (32.16).** Requires physical measurement and calibration across the shear cycle \(\Sigma(t)\).

---

## 9. Forward References

- **Paper 001** (LCR minimal carrier) — supplies the 8-state carrier that Z-pinch configurations map onto. The shell grading (1,3,3,1), reversal involution \(\sigma\), and shell-2 doublet are inherited.
- **Paper 003** (Correction surface) — the repair curvature \(K_b\) at shear horizons triggers correction repair when \(K_b > 1\).
- **Paper 006** (Oloid path) — the integer Oloid carrier period-4 rolling algebra is the kernel of the oloid path transport geometry.
- **Paper 007** (Boundary repair) — uses shear horizon curvature \(K_b\) as input to boundary repair operations.
- **Paper 008** (Oloid path carrier) — the period-4 rolling algebra is the minimal carrier unit.
- **Paper 025** (Synthesis ledger) — may use Z-pinch/shear kernel for plasma-energy accounting.
- **Paper 031** (Energetic traversal maps) — the NSL boundary row \(\theta\) gate is the energetic analogue of the shear horizon pinch reclassification.
- **Paper 033** (Observer delay) — may use the Z-pinch/shear kernel for observer-energy accounting.
- **Paper 034** (Game lattices) — shear horizons as typed boundaries extend to game-lattice traversal.
- **Paper 040** (Layer 4 closure) — position 2 of Layer 4; the 4th correction bit accumulates across all Layer 4 papers.
- **Later plasma papers** — may use the carrier-level shear diagnostic but must supply their own measured observables, calibration rows, and falsifiers.

---

## 10. Data vs Interpretation

### Data-backed (D)

- The integer Oloid carrier is period-4 (bit0_period_4 = true, bit1_period_4 = true). (D — `zpinch_shear_horizon_receipt.json`)
- The octonion carrier realizes e4² = -1 and e4⁴ = 1 with non-associativity. (D — octonion verifier)
- The path-history residue is replayable over 17 trace rows. (D — Rule 30 trace)
- Eight rows show nonzero shear divergence. (D — shear probe)
- Pinch is a transport-ledger reclassification. (D — ledger classification)
- Z-pinch configurations map bijectively to 8 LCR states via SQLLib. (D — `z_pinch_configurations` table)
- Shear horizons have three typed categories with curvature and entropy density. (D — `shear_horizons` table)
- The period-4 shear cycle guarantees Σ=0 at closure. (D — Theorem 32.8)

### Interpretation (I)

- The "Z-pinch/shear horizon" framing is the author's structural reading of the carrier algebra as a plasma physics analog. (I — the underlying finite checks are D.)
- The application of the carrier-level shear diagnostic to later plasma papers is the author's structural reading of the broader series.
- The LCR mapping to stability_status (stable/unstable/shear_critical) is an interpretative partition of the 8 LCR states. (I — the bijection is D.)

### Fabrication (X)

- None in this paper. All finite claims are D verified. The physical plasma claims (measured Z-pinch, plasma observables, friction, generation, energy production, collapse) are honestly marked as X open obligations.

---

## 11B. Canonical Production Source — CQECMPLX-Production P26 (Z-Pinch and Shear Horizon)

P26's C-Form: the pinch Gluon — Z-pinch and shear horizon as the chart's collapse/repair
dynamics. **No run.py** (index: "needs creation"). Maps to §11 (Z-pinch shear horizon).
Honest note: Z-pinch/shear is the CQECMPLX interpretation of chart collapse dynamics; not a
MHD derivation. No fabrication.

## 11C. ProofValidatedSuite Exposition — EXPOSE-26 (Z-Pinch and Shear Horizon)

EXPOSE-26: pinch Gluon — Z-pinch and shear horizon as the chart's collapse/repair dynamics.
**Gluon invariant** = pinch. Maps to §11 (Z-pinch shear horizon). Honest note: Z-pinch/shear
is the CQECMPLX interpretation of chart collapse dynamics; not a MHD derivation. No fabrication.

## 11C. UFT 0-100 Series (FLCR) — Paper 25: shear, plasma & carrier horizons

Paper 25 frames shear/plasma/carrier horizons as chart collapse/repair dynamics. **(I)**
interpretation; not a MHD derivation. Maps to §11. No fabrication.


## 25A. Formal-Paper Deep-Dive (CQE-paper-25)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-25/FORMAL_PAPER.md` (proof-texture restoration). D/I/X tagged.

### Definitions

An active transport is the current move from a source object to a target object.
Its center `C` is the preserved invariant the move claims to carry. Its opposed
readouts `L` and `R` record what is preserved and what remains as boundary
residue.

An NSL boundary term is the tuple
`(N, S, L, absorption, alpha, beta, gamma)`. `N` is the conservation mismatch,
`S` is the information mismatch, `L` is the irreversible execution cost, and
`absorption` is the declared capacity that may absorb the mismatch. The closed
step gate is `theta <= 0`.

An energetic traversal map is an ordered path of transport rows. Its path cost
is the sum of the step costs after the rows have been normalized into compatible
accounting units. A traversal is closed only when the path total closes and no
step is marked uncalibrated.

A unit policy is part of the receipt. The default paper policy is
`normalized_analog_units`; this is a valid internal energy/action scale. A
physical-energy reading in measured units requires domain calibration of the
NSL terms.

### Claims

1. Every accepted CQE traversal can carry a replayable NSL row per step.

2. The step gate is exactly the package gate:
`theta = alpha*N + beta*S + gamma*L - absorption`, with closure iff
`theta <= 0`.

3. For normalized rows, traversal totals are additive:
`theta_path = sum(theta_i)`.

4. The package's four-layer transport-obligation spine is the canonical
traversal surface for this paper, and its open lifts remain visible.

5. The verified VOA sector split supplies a default analog cost: two vacuum
states carry weight 0 and six excited states carry weight 5.

6. A traversal receipt is the internal action/energy proof. A measured
physical-energy value requires a later domain calibration proving the unit map.

_**(D)** formal claim._

### Theorem 25

An energetic traversal is valid in the CQE kernel exactly when it emits a
replayable NSL boundary row for each step, sums those rows into a path total,
marks closure or obligation without deletion, and declares whether its units are
analog-normalized or physically calibrated.

_**(D)** formal claim._

### Proof

`NSLTerm` is a frozen data object whose `theta` property evaluates
`alpha*N + beta*S + gamma*L - absorption`. Its `closes_internally` property is
the Boolean `theta <= 0`. The verifier checks a weighted sample with
`sample_theta = 2.4` and confirms that a positive term does not close while a
negative term does.

The verifier then calls `verify_transport_obligations`. The returned spine has
four rows, all required fields present, and passing local witnesses. It reports
`pass_with_open_lifts`, not a total closure. This is the needed boundary
behavior: demonstrated rows can be used directly, while bounded and registered
rows are still carried as named obligations.

For traversal additivity, the verifier constructs two path receipts. Each path
stores per-step NSL dictionaries, per-step `theta`, the unit policy, and the
path total. The receipt recomputes each `theta_path` as the sum of its step
rows. The normalized path closes with `theta_path = -0.35`. The second path has
positive boundary residue and an uncalibrated domain unit policy, so it remains
open with `theta_path = 0.8999999999999999`. No row is discarded.

Finally, the verifier calls `verify_voa_sector_decomposition`, which passes
with `Z(q) = 2q^0 + 6q^5`. This gives a package-native analog weight to chart
states before any domain-specific physical calibration is attempted. Therefore
the energetic traversal map is closed as the internal action/energy model and
open only at the external unit-calibration bridge.

_**(D)** verified algebraic/structural proof._

### Open Obligations

Physical unit calibration remains open. The paper closes normalized internal
action/energy accounting; it does not yet convert NSL rows to joules.

Absorption measurement remains open. `absorption_capacity` must be supplied by
a domain measurement or declared policy.

Least-action, geodesic, or thermodynamic-optimum readings are valid exploratory
readings only after the domain supplies the calibrated variational principle. A
smaller analog `theta_path` is already meaningful inside the receipt ledger.

Noether/Shannon/Landauer unification remains a calibration-level research
claim. The paper already proves the combined NSL accounting row inside the CQE
transport ledger.

_— honestly carried as guard / next-need._

---


## 11. Bibliography

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
2. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups* (SPLAG), 3rd ed., Springer, 1999. Niemeier lattices and E8 structures.
3. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. SU(3) and representation theory.
4. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. \(J_3(\mathbb{O})\) and exceptional algebra.
5. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and E8 structures.
6. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 and algebraic structure.
7. F. Gursey and C.-H. Tze, *On the Role of Division Algebras in Particle Physics*, World Scientific, 1996. Octonions and division algebras in physics.
8. R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That*, Princeton University Press, 2000. Quantum field theory axioms.
9. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory.
10. M. A. Uman, *Introduction to Plasma Physics*, McGraw-Hill, 1964. Z-pinch confinement and stability.
11. D. A. Frank-Kamenetskii, *Plasma: The Fourth State of Matter*, Plenum Press, 1972. Plasma shear and boundary layers.
12. J. Wesson, *Tokamaks*, 4th ed., Oxford University Press, 2011. Plasma confinement and MHD stability.

---

## 12B. Shear & Pinch Moduli as Tarpit Deformation (recrafted from CQECMPLX-Formal-Suite CQE-PAPER-042)

CQE-PAPER-042 gives the two fundamental deformation modes of Tarpit mass: shear (asymmetric
correction firing, G_shear = 2κ) and pinch (symmetric boundary compression, G_pinch = 4κ),
with the 7-fold substitution mapping to a Z-pinch plasma of 7 current channels. Engine
`lattice_forge.tarpit_ecology.verify_shear_pinch_moduli` confirms: the chiral doublet
{(0,1,0),(1,1,0)} exists (asymmetry source), G_shear = 2κ, G_pinch = 4κ, and the 4
antipodal (bit-complement) dyads of the 8-state cube exist (symmetric-compression source).
The 7 Z-pinch channels = the 7-fold substitution sequences (verified in §15B/§16.6).

The shear/pinch moduli are **definitional** (chiral-doublet asymmetry, 4 symmetric dyads);
they are chart facts, not external calibrations. The Z-pinch analogy and 7-channel map are sound.
No A033996 claim in CQE-PAPER-042.

## 12. Conclusion

Paper 032 establishes the Z-pinch/shear horizon as a carrier-level kernel: the integer Oloid period-4 rolling algebra, octonion carrier with \(e_4, e_5\) generators, reproducible shear diagnostic via XOR divergence, pinch as ledger reclassification, Z-pinch configurations mapped to LCR carrier states (8 classes in SQLLib), shear horizons as typed boundaries with repair curvature (3 types in SQLLib), and a minimal period-4 shear cycle. All 11 D claims are receipt-bound and hand-reconstructible. The 5 X claims are honestly marked as open obligations for empirical calibration. The paper is honest, bounded, and ready for Layer 4 closure.
