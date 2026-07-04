# Paper 25 — Energetic Traversal Maps

**Status.** IPMC for the unit-agnostic energetic traversal accounting kernel: replayable NSL boundary rows, package gate `theta = alpha*N + beta*S + gamma*L - absorption`, additive traversal totals, visible open transport lifts, and default analog cost from the verified `2 + 6` VOA sector split. ECO for joule-valued physical energy, absorption measurement, calibrated least action, thermodynamic optimality, and full Noether-Shannon-Landauer unification in measured physical units.

---

## Abstract

Paper 25 defines the energetic traversal map: a unit-agnostic accounting kernel for CQE transports. Each accepted step emits a replayable NSL boundary row carrying conservation mismatch `N`, information mismatch `S`, irreversible execution cost `L`, declared absorption, weights `alpha`, `beta`, `gamma`, and a computed boundary value `theta`. A row closes internally exactly when `theta <= 0`. A path closes only when its normalized step totals close and no row is marked uncalibrated.

The verifier imports `NSLTerm`, the transport-obligation spine, and the centroid-VOA sector decomposition. It confirms the `theta` formula, checks that positive terms do not close while negative terms do, preserves a four-row transport spine with two demonstrated rows and two open lifts, verifies additive path totals, and confirms the default analog weight distribution `Z(q) = 2q^0 + 6q^5`. The worked normalized path closes with `theta_path = -0.35`; the diagnostic open path remains open with `theta_path = 0.8999999999999999` and an uncalibrated domain-unit row.

The paper does not prove joule-valued physical energy, absorption measurement, calibrated least action, thermodynamic optimality, or a full Noether-Shannon-Landauer unification in measured physical units. Those claims remain calibration obligations.

**Keywords:** energetic traversal; NSL boundary term; Noether-Shannon-Landauer; analog units; transport ledger; VOA sector cost; calibration boundary.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 25.1 | Every accepted traversal step can carry a replayable NSL row. | [D] | `verify_energetic_traversal.py`; `energetic_traversal_receipt.json` |
| 25.2 | The step gate is `theta = alpha*N + beta*S + gamma*L - absorption`, closing iff `theta <= 0`. | [D] | `NSLTerm` verifier checks |
| 25.3 | Traversal path totals add from step totals. | [D] | Path receipts recompute `theta_path = sum(theta_i)` |
| 25.4 | The four-layer transport spine remains visible with open lifts. | [D] | `pass_with_open_lifts` rows |
| 25.5 | The verified `2 + 6` sector split supplies default analog cost. | [D] | `Z(q) = 2q^0 + 6q^5` |
| 25.6 | Joule-valued physical energy is proved. | [X] | Explicit open obligation |
| 25.7 | Absorption measurement is proved. | [X] | Explicit open obligation |
| 25.8 | Calibrated least action is proved. | [X] | Explicit open obligation |
| 25.9 | Thermodynamic optimality is proved. | [X] | Explicit open obligation |
| 25.10 | Full NSL unification in measured physical units is proved. | [X] | Explicit open obligation |

---

## 2. Definitions

**Active transport.** A move of a registered state from a source surface to a target surface. Its center `C` is the invariant being carried, while `L` and `R` record preserved content and boundary residue.

**NSL boundary term.** The tuple `(N, S, L, absorption, alpha, beta, gamma)` where `N` is conservation mismatch, `S` is information mismatch, `L` is irreversible execution cost, and `absorption` is the declared absorption.

**Energetic traversal map.** An ordered path of NSL rows, plus a unit policy. The default policy is `normalized_analog_units`; physical-energy readings require a separate domain map.

**Unit policy.** The declaration of whether the unit system is analog normalized or physically calibrated.

---

## 3. Theorems and Proofs

### Theorem 25.1 — Replayable NSL Rows

Every accepted traversal step can carry a replayable NSL row.

**Proof.** The verifier `verify_energetic_traversal.py` confirms that each accepted step emits a replayable NSL boundary row. The receipt `energetic_traversal_receipt.json` records the row fields. This is internal accounting, not physical measurement. ∎

### Theorem 25.2 — Step Gate Closure

The step gate is `theta = alpha*N + beta*S + gamma*L - absorption`, closing iff `theta <= 0`.

**Proof.** The `NSLTerm` verifier checks the `theta` formula and confirms the closure gate: a row closes internally exactly when `theta <= 0`. Positive terms do not close while negative terms do. ∎

### Theorem 25.3 — Additive Path Totals

Traversal path totals add from step totals.

**Proof.** The verifier constructs path receipts whose totals are recomputed from the step rows: `theta_path = sum(theta_i)`. The normalized path closes with `theta_path = -0.35`; the diagnostic open path remains open with `theta_path = 0.8999999999999999` and an uncalibrated domain-unit row. ∎

### Theorem 25.4 — Visible Transport Spine with Open Lifts

The four-layer transport spine remains visible with open lifts.

**Proof.** The verifier checks the transport-obligation spine, preserving demonstrated rows separately from bounded or registered lifts. The spine has four rows: two demonstrated and two open lifts. The status is `pass_with_open_lifts`. Open lifts are not promoted to closed claims. ∎

### Theorem 25.5 — Default Analog Cost from VOA Sector Split

The verified `2 + 6` sector split supplies default analog cost.

**Proof.** The verifier checks the centroid-VOA sector split and confirms the default analog weight distribution `Z(q) = 2q^0 + 6q^5`. This is the package-native analog cost prior to any physical calibration. It is not a joule-valued calibration. ∎

---

## 4. Verifiers and Receipts

### 4.1 Energetic Traversal

`verify_energetic_traversal.py` → `energetic_traversal_receipt.json`

| Field | Value |
|-------|-------|
| status | pass_with_open_obligations |
| nsL_rows | replayable |
| theta_formula | verified |

### 4.2 Energy Ledger Affirmed

`verify_energy_ledger_affirmed.py` → `energy_ledger_affirmed_receipt.json`

| Field | Value |
|-------|-------|
| status | pass |
| checks | 5/5 |

### 4.3 Physical Units Calibration

`verify_physical_units_calibration.py` → `physical_units_calibration_receipt.json`

| Field | Value |
|-------|-------|
| keys | kappa_verification, voa_verification, scale_factor, particle_predictions, external_bridge |

---

## 5. Hand Reconstruction

All claims can be reconstructed by hand from the definitions:

1. **25.1:** Each step emits a replayable NSL row with fields `(N, S, L, absorption, alpha, beta, gamma)`.
2. **25.2:** The step gate closes when `theta = alpha*N + beta*S + gamma*L - absorption <= 0`.
3. **25.3:** Path totals are additive: `theta_path = sum(theta_i)` for all steps in the path.
4. **25.4:** The transport spine has two demonstrated rows and two open lifts; open lifts are visible.
5. **25.5:** The sector split is `Z(q) = 2q^0 + 6q^5`, giving the default analog cost.

No external computation is required.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F25.1 | The NSL row is a physical measurement. | It is internal accounting, not measurement. |
| F25.2 | The theta formula is unverified. | The `NSLTerm` verifier checks it. |
| F25.3 | Path totals are not additive. | The verifier recomputes `theta_path` from step rows. |
| F25.4 | Open lifts are promoted. | The status is `pass_with_open_lifts`; open lifts remain visible. |
| F25.5 | The analog cost is joule-valued. | It is normalized analog, not physical calibration. |
| F25.6 | Physical energy is proved. | Explicitly marked as open obligation. |
| F25.7 | Least action is calibrated. | Explicitly marked as open obligation. |
| F25.8 | Thermodynamic optimality is proved. | Explicitly marked as open obligation. |
| F25.9 | Full NSL unification is proved. | Explicitly marked as open obligation. |

---

## 7. Relation to Later Papers

- **Paper 20** (Layer-2 Synthesis Ledger) exports the transport-obligation spine that the energetic traversal map uses.
- **Paper 22** (MetaForge) may use the energetic traversal map for production-energy accounting in materials.
- **Paper 26** (Z-Pinch and Shear Horizon) may use the energetic traversal map for plasma-energy accounting.
- **Paper 27** (Observer Delay and Shared Reality) may use the energetic traversal map for observer-energy accounting.
- **Later papers** may use the NSL boundary term for energy accounting, but must declare their unit policy and calibration status.

---

## 8. Open Obligations

1. **Joule-valued physical energy (25.6).** Requires external unit maps and calibration.
2. **Absorption measurement (25.7).** Requires physical measurement and pass/fail criteria.
3. **Calibrated least action (25.8).** Requires geodesic/thermodynamic readings and external calibration.
4. **Thermodynamic optimality (25.9).** Requires thermodynamic calculation and validation.
5. **Full NSL unification in measured physical units (25.10).** Requires complete physical calibration and falsification criteria.

---

## 9. Bibliography

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
2. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups* (SPLAG), 3rd ed., Springer, 1999. Niemeier lattices and E8 structures.
3. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. `SU(3)` and representation theory.
4. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. `J_3(O)` and exceptional algebra.
5. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and `E8` structures.
6. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 and algebraic structure.
7. E. Noether, "Invariante Variationsprobleme," *Nachr. Ges. Wiss. Göttingen* (1918), 235–257. Conservation laws and variational principles.
8. C. E. Shannon, "A mathematical theory of communication," *Bell System Technical Journal* 27 (1948), 379–423, 623–656. Information theory.
9. R. Landauer, "Irreversibility and heat generation in the computing process," *IBM J. Res. Develop.* 5 (1961), 183–191. Landauer's principle.
10. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory.

---

## 10. Data vs Interpretation

### Data-backed (D)

- Each accepted step emits a replayable NSL row. (D — `energetic_traversal_receipt.json`)
- The step gate `theta = alpha*N + beta*S + gamma*L - absorption` closes when `theta <= 0`. (D — `NSLTerm` verifier)
- Path totals are additive from step totals. (D — path receipts)
- The transport spine has two demonstrated rows and two open lifts. (D — `pass_with_open_lifts`)
- The default analog cost is `Z(q) = 2q^0 + 6q^5`. (D — centroid-VOA sector split)

### Interpretation (I)

- The "energetic traversal map" framing is the author's structural reading of the NSL accounting tools. (I — the underlying finite checks are (D).)
- The application of the energetic traversal map to later domains (materials, plasma, observer) is the author's structural reading of the broader series.

### Fabrication (X)

- None in this paper. All finite claims are (D) verified. The physical-energy claims (joule-valued, absorption, least action, thermodynamics, NSL unification) are honestly marked as (X) open obligations.

---

## 11. Conclusion

Paper 25 makes traversal energy usable as a precise internal ledger. The CAM can look up the NSL row, path total, closure status, unit policy, and open residue immediately. Physical energy is not lost, but it is placed where it belongs: in the calibration layer.
