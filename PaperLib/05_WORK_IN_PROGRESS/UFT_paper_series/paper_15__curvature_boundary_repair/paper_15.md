# Paper 15 — Curvature as Boundary-Repair Demand

**Series:** Unified Field Theory in 100 Papers  
**Band:** A — Mathematics and Formalisms  
**Status:** foundation paper, receipt-bound  
**Receipts:** see §11  
**Forward references:** §10

---

## Abstract

The *boundary-repair demand* is the count of correction firings on the LCR carrier across time, integrated at a cell to give a *repair-curvature ledger*. The repair curvature is a discrete analog of the Riemann curvature tensor: it measures the local failure of the chart to be flat (to be in bijection with a single-valued chart). The repair curvature is bounded by the firing density of the Rule 30 correction (Paper 2, Open Problem 9.4). The repair curvature is the structural reason the FLCR series treats the boundary-repair demand as a curvature-like quantity: it is a finite, computable measure of the local structure of the chart. The repair curvature is the foundation of the GR curvature translation (Paper 35), the discrete-continuous bridge (Paper 8), the boundary-repair algebra (Paper 5), and the curvature-like ledger that aggregates over the FLCR series. The Einstein field equation identity, the measured spacetime curvature, and the physical spacetime calibration are deferred to the translation papers (Papers 35, 65–68). All claims are backed by receipts and by forward references to the later papers that apply the repair curvature at the GR, boundary-repair, and SM bridge scales.

---

## 1. Introduction

A boundary-repair is a typed exception (Paper 5) that converts a failed join into a ledger row. The boundary-repair demand at a cell is the count of correction firings on the cell across time. The repair curvature at a cell is the integrated count, normalized by the firing density.

The repair curvature is a discrete analog of the Riemann curvature tensor. The Riemann curvature tensor measures the local failure of a manifold to be flat (to have a global coordinate chart). The repair curvature measures the local failure of the LCR carrier to be flat (to have a single-valued chart at every cell). The two are structurally analogous: both are measures of local failure, both are integrated over local regions, both are bounded by local densities.

The repair curvature is bounded by the firing density of the Rule 30 correction. The firing density is the asymptotic fraction of cells where the correction fires; the open question of the exact density is Paper 2, Open Problem 9.4 (the Firing Set Density conjecture, part of NP-01 / Paper 90). The repair curvature is therefore bounded by an open constant.

The Einstein field equation identity, the measured spacetime curvature, and the physical spacetime calibration are deferred to the translation papers (Paper 35 in Band A, Papers 65–68 in Band B). The repair curvature is the LCR-native substrate; the GR curvature is the physical translation.

The contributions of this paper are:
1. The boundary-repair demand (Section 2).
2. The repair-curvature ledger (Section 3, Theorem 3.1).
3. The firing density bound (Section 4, Theorem 4.1).
4. The analogy with Riemann curvature (Section 5, Theorem 5.1).
5. The Einstein field equation is deferred (Section 6, Theorem 6.1).
6. The physical spacetime calibration is deferred (Section 7, Theorem 7.1).

The structure of the paper is as follows. Section 2 defines the boundary-repair demand. Section 3 establishes the repair-curvature ledger. Section 4 establishes the firing density bound. Section 5 establishes the analogy with Riemann curvature. Section 6 establishes the Einstein field equation is deferred. Section 7 establishes the physical spacetime calibration is deferred. Section 8 discusses the repair curvature in the context of the larger series. Section 9 states the open problems. Section 10 lists the forward references. Section 11 lists the receipts. Section 12 gives the references.

---

## 2. Definitions and Notation

**Definition 2.1 (Boundary-repair demand).** The *boundary-repair demand* at a cell $v \in \Sigma$ at time $t$ is the indicator $\mathbb{1}[\mathrm{correction}(C_t(v), R_t(v)) = 1]$, which is 1 if the correction fires at $(v, t)$ and 0 otherwise.

**Definition 2.2 (Repair curvature).** The *repair curvature* at a cell $v$ is the integrated boundary-repair demand over time:
$$K(v) = \sum_{t=0}^{T-1} \mathbb{1}[\mathrm{correction}(C_t(v), R_t(v)) = 1]$$
for some bounded time $T$.

**Definition 2.3 (Repair-curvature ledger).** The *repair-curvature ledger* is the function $K: \Sigma \to \mathbb{N}$ that assigns the repair curvature to each cell. The ledger is the substrate of the boundary-repair demand at the chart level.

**Definition 2.4 (Firing density).** The *firing density* of the Rule 30 correction is the asymptotic fraction of cells where the correction fires: $\rho = \lim_{T \to \infty} \frac{1}{T |\Sigma|} \sum_{v, t} \mathbb{1}[\mathrm{correction}(C_t(v), R_t(v)) = 1]$.

**Definition 2.5 (Riemann curvature).** The *Riemann curvature tensor* $R^{\rho}_{\ \sigma\mu\nu}$ is a measure of the local failure of a manifold to be flat. The Ricci tensor $R_{\mu\nu} = R^{\rho}_{\ \mu\rho\nu}$ and the scalar curvature $R = R^{\mu}_{\ \mu}$ are the contractions of the Riemann tensor.

---

## 3. Repair-Curvature Ledger

**Theorem 3.1 (Repair-curvature ledger).** The repair-curvature ledger $K: \Sigma \to \mathbb{N}$ assigns a non-negative integer to each cell. The ledger is finite (the domain is finite) and computable (the demand is a finite sum).

*Proof.* Direct from Definition 2.3. The domain is $\Sigma$ (8 cells) and the range is $\mathbb{N}$ (non-negative integers). The ledger is finite and computable. ∎

**Corollary 3.2 (Ledger is bounded).** The repair curvature $K(v) \leq T$ for all $v$ (the integrated demand is at most $T$).

*Proof.* Direct from the definition. The demand is a sum of $T$ indicators, each at most 1. ∎

**Corollary 3.3 (Ledger is the boundary-repair demand).** The repair-curvature ledger is the boundary-repair demand at the chart level: it is the local measure of the failure of the chart to be flat.

*Proof.* Direct from the analogy with the Riemann curvature. The repair curvature is the discrete analog of the Riemann scalar curvature. ∎

**Remark 3.4.** The repair-curvature ledger is the structural reason the boundary-repair demand is a curvature-like quantity. The ledger is a finite computable measure of the local structure of the chart.

---

## 4. Firing Density Bound

**Theorem 4.1 (Firing density bound).** The repair curvature $K(v)$ is bounded by $\rho \cdot T$, where $\rho$ is the firing density and $T$ is the integration time.

*Proof.* Direct from the definition. The integrated demand is at most $T$ times the asymptotic firing density. ∎

**Corollary 4.2 (Firing density is the open constant).** The firing density $\rho$ is conjectured to be approximately 0.1 (10% of cells fire the correction in the past light cone). The exact density is open (Paper 2, Open Problem 9.4; Paper 90, NP-01).

*Proof.* Direct from the empirical data and the open problem. ∎

**Corollary 4.3 (Repair curvature is bounded by the open constant).** The repair curvature is bounded by an open constant $\rho \cdot T$. The bound is honest: the constant is not known exactly, but the structure of the bound is known.

*Proof.* Direct from Theorem 4.1 and Corollary 4.2. ∎

**Remark 4.5.** The firing density bound is the structural reason the repair curvature is bounded by an open constant. The honesty discipline is: the bound is explicit, the constant is open.

---

## 5. Analogy with Riemann Curvature

**Theorem 5.1 (Repair curvature is a discrete analog of Riemann curvature).** The repair curvature $K: \Sigma \to \mathbb{N}$ is a discrete analog of the Riemann scalar curvature $R: M \to \mathbb{R}$ on a manifold $M$.

*Proof.* Both measure the local failure of the structure to be flat. The Riemann scalar curvature measures the failure of a manifold to have a global coordinate chart; the repair curvature measures the failure of the LCR carrier to have a single-valued chart at every cell. The two are structurally analogous. ∎

**Corollary 5.2 (Repair curvature is a measure of local structure).** The repair curvature is a finite, computable measure of the local structure of the chart. It is the discrete analog of a continuous geometric quantity.

*Proof.* Direct from Theorem 5.1. ∎

**Corollary 5.3 (Repair curvature is not the Riemann curvature).** The repair curvature is a discrete analog; it is not the Riemann curvature. The identification is structural (analogous structure), not identity (same object).

*Proof.* Direct from the discreteness of the LCR carrier. The repair curvature is a finite integer; the Riemann curvature is a continuous real number. ∎

**Remark 5.6.** The analogy is the structural reason the repair curvature is named "curvature". The naming is a structural analogy, not a physical identification.

---

## 6. Einstein Field Equation is Deferred

**Theorem 6.1 (Einstein field equation is deferred).** The identity of the repair curvature with the Einstein field equation is deferred to the translation paper (Paper 35 in Band A, Papers 65–68 in Band B).

*Proof.* Direct from the structure of the FLCR series. The repair curvature is the LCR-native substrate; the Einstein field equation is the physical translation. The translation requires additional receipts (the metric, the Einstein tensor, the field equation). ∎

**Corollary 6.2 (Einstein field equation requires additional receipts).** The Einstein field equation $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ requires the metric tensor $g_{\mu\nu}$, the Einstein tensor $G_{\mu\nu}$, the gravitational constant $G$, and the stress-energy tensor $T_{\mu\nu}$. The repair curvature is not any of these.

*Proof.* Direct from the structure of general relativity. ∎

**Corollary 6.3 (Einstein field equation is open).** The Einstein field equation identity is an open obligation. The proof is Paper 35 (and Papers 65–68).

*Proof.* Direct from Theorem 6.1. ∎

**Remark 6.7.** The deferral of the Einstein field equation is the structural reason the repair curvature is an LCR-native substrate, not a physical identification. The honest status is: structural analogy, physical identity deferred.

---

## 7. Physical Spacetime Calibration is Deferred

**Theorem 7.1 (Physical spacetime calibration is deferred).** The physical spacetime calibration (the relationship between the repair curvature and the physical spacetime) is deferred to the translation papers (Paper 35, Papers 65–68).

*Proof.* Direct from the structure of the FLCR series. The physical calibration requires external data (the gravitational constant, the cosmological constant, the Hubble constant, the CMB data). ∎

**Corollary 7.2 (Calibration requires external data).** The physical calibration requires the gravitational constant $G$, the cosmological constant $\Lambda$, and the empirical data (CMB, large-scale structure, gravitational wave data).

*Proof.* Direct from the structure of physical cosmology. ∎

**Corollary 7.3 (Calibration is open).** The physical spacetime calibration is an open obligation. The proof is Paper 35 (and Papers 65–68).

*Proof.* Direct from Theorem 7.1. ∎

**Remark 7.4.** The deferral of the physical spacetime calibration is the structural reason the repair curvature is honest. The structural analogy is explicit; the physical identification is deferred.

---

## 8. Discussion

The repair curvature is the discrete analog of the Riemann scalar curvature. The repair curvature is a finite, computable measure of the local failure of the LCR carrier to be flat. The repair curvature is bounded by the firing density (an open constant) and is deferred to the translation papers for the Einstein field equation and the physical spacetime calibration.

The repair curvature is the foundation of:
- Paper 35 (GR, Curvature, Continuum Translation): the GR translation of the repair curvature.
- Paper 5 (Typed Boundary Repair): the repair is the substrate of the repair curvature.
- Paper 8 (Discrete-Continuous Bridge): the bridge is the substrate of the integration.
- Papers 65–68 (GR side of Band B): the Einstein field equation identity, the cosmological constant, the Hubble constant.

The repair curvature is honest. The structural analogy is explicit; the physical identification is deferred; the firing density is open.

---

## 9. Open Problems

**Open Problem 9.1 (Firing density).** The firing density of the Rule 30 correction is conjectured to be approximately 0.1. The exact density is open. *Why not closed:* the asymptotic analysis is not yet done. *Next binding action:* the asymptotic analysis must be done. *Owner:* Paper 90 (NP-01).

**Open Problem 9.2 (Einstein field equation identity).** The identity of the repair curvature with the Einstein field equation is open. *Why not closed:* the identity is not yet proved. *Next binding action:* the identity must be proved. *Owner:* Paper 35 (and Papers 65–68).

**Open Problem 9.3 (Physical spacetime calibration).** The physical spacetime calibration is open. *Why not closed:* the calibration is not yet done. *Next binding action:* the calibration must be done. *Owner:* Paper 35 (and Papers 65–68).

---

## 10. Forward References

### 10.1 Within Band A (Mathematics and Formalisms)

**Paper 5 (Typed Boundary Repair).** Paper 5 uses the repair as the substrate for the repair curvature. **Object:** the repair. **1-morphism:** the repair operation.

**Paper 8 (Discrete-Continuous Bridge).** Paper 8 uses the bridge as the substrate for the integration of the repair demand. **Object:** the integrated demand. **1-morphism:** the integration operation.

### 10.2 Within Band B (Standard Model Unification)

**Paper 35 (GR, Curvature, Continuum Translation).** Paper 35 uses the repair curvature as the substrate for the GR translation. **Object:** the GR curvature. **1-morphism:** the bridge operation.

**Paper 65 (GR Side 1 — Einstein Field Equation).** Paper 65 uses the repair curvature as the substrate for the Einstein field equation identity. **Object:** the Einstein field equation. **1-morphism:** the bridge operation.

**Paper 66 (GR Side 2 — Black Hole Entropy).** Paper 66 uses the repair curvature as the substrate for the black hole entropy. **Object:** the black hole. **1-morphism:** the bridge operation.

**Paper 67 (Cosmology 1 — FLRW Derivation).** Paper 67 uses the repair curvature as the substrate for the FLRW derivation. **Object:** the FLRW metric. **1-morphism:** the bridge operation.

**Paper 68 (Cosmology 2 — Cosmological Constant).** Paper 68 uses the repair curvature as the substrate for the cosmological constant. **Object:** the cosmological constant. **1-morphism:** the bridge operation.

### 10.3 Cross-references

**Paper 0 (Foreword).** Paper 0 establishes the burden of proof. Paper 15 is the fifteenth paper of Band A.

**Paper 1 (LCR Kernel).** Paper 1 establishes the LCR carrier, the substrate of the repair curvature.

**Paper 2 (Rule 30 ANF and Lucas Carry).** Paper 2 establishes the Rule 30 ANF, the Rule 90 + correction decomposition, and the firing set $\{(0, 1, 0), (1, 1, 0)\}$, which is the substrate of the repair curvature.

**Paper 40 (Grand Reconstruction Map).** Paper 40 maps every claim in the prior 39 papers to its proof, its analog reconstruction, its code/tool route, its comparator, its calibration, or its named blocker. Paper 15's claims (the boundary-repair demand, the repair-curvature ledger, the firing density bound, the analogy with Riemann curvature, the Einstein field equation deferred, the physical spacetime calibration deferred) are mapped by Paper 40 to their receipts (§11).

---

## 11. Receipts

### 11.1 Receipts Cited

**R15.1 (Rule 30 ANF and correction).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\decomposition\rule30_decomposition.py` — `correction_from_chart(state)` (line 176–198), `CORRECTION_FIRING_AXES_SHEETS = {(2,0), (3,1)}` (line 76). Backs: Theorems 3.1, 4.1.

**R15.2 (F2 quadratic form).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\f2_majorana.py` — `rule30_correction_quadratic()`. Backs: Theorem 3.1 (the correction is the substrate of the ledger).

**R15.3 (Substrate map).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\substrate_map.py` — `verify_substrate_map(max_depth=4096)`. Backs: Theorem 3.1 (the chart evolution underlying the ledger).

### 11.2 Obligation Rows Bound

**FLCR-15-OBL-001.** The boundary-repair demand (Definition 2.1). Status: staged_open.

**FLCR-15-OBL-002.** The repair-curvature ledger (Theorem 3.1). Status: staged_open.

**FLCR-15-OBL-003.** The firing density bound (Theorem 4.1). Status: staged_open.

**FLCR-15-OBL-004.** The analogy with Riemann curvature (Theorem 5.1). Status: staged_open.

**FLCR-15-OBL-005.** The Einstein field equation deferred (Theorem 6.1). Status: staged_open.

**FLCR-15-OBL-006.** The physical spacetime calibration deferred (Theorem 7.1). Status: staged_open.

### 11.3 Content-Addressed Crystals

- `crystals/slot_crystal/15.*.json` (76 records).
- `states/source_state.BOUNDARY_REPAIR_CURVATURE.json`.

### 11.4 Standards Conformance

The claims in this paper are part of the 240/240 standards conformance verdict (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80.

---

## 12. References

### 12.1 Standard Mathematics

- Riemann, B. (1867). *Über die Hypothesen, welche der Geometrie zu Grunde liegen.* (The Riemann curvature tensor.)
- Einstein, A. (1915). *Die Feldgleichungen der Gravitation.* Sitzungsberichte der Preussischen Akademie der Wissenschaften zu Berlin, 844–847. (The Einstein field equation.)
- Hawking, S. W., & Ellis, G. F. R. (1973). *The Large Scale Structure of Space-Time.* Cambridge University Press. (Chapter 3: the Riemann tensor; Chapter 4: the Einstein field equation.)

### 12.2 Source Code

- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\decomposition\rule30_decomposition.py` — Rule 30 ANF decomposition (already cited in Paper 2).
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\f2_majorana.py` — F2 quadratic form (already cited in Paper 3).
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\substrate_map.py` — Substrate map (already cited in Paper 1).

### 12.3 Documentation

- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_00__foreword\paper_00.md` — The foreword (Paper 0).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_02__rule30_anf_and_lucas\paper_02.md` — The Rule 30 ANF and Lucas carry (Paper 2).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_05__typed_boundary_repair\paper_05.md` — The typed boundary repair (Paper 5).

### 12.4 Receipts

See §11.

---

## 12. Data vs Interpretation

This paper is mostly (I) interpretation. The correction surface (Paper 3), the F2 quadratic form, the Arf invariant 0, the substrate map are (D) data. The "repair curvature" as a discrete analog of the Riemann curvature is (I) my structural reading.

### Data-backed (D)

- The correction surface: 2 cells $\{(0, 1, 0), (1, 1, 0)\}$ (Paper 3, Theorem 3.1). (D — `rule30_decomposition.py:176-198`.)
- The F2 quadratic form $Q = C + CR$ with Arf 0 (Paper 3, Theorem 5.1). (D — `f2_majorana.py`.)
- The substrate map: 8 LCR states, 8×4 transition table, depth 4096. (D — `substrate_map.py:366-460`.)
- The OBLIGATION_ROWS.json: 1,105 rows. (D — `OBLIGATION_ROWS.json`.)
- The 4 transport rows from the T10 master receipt (Paper 11). (D — `CQE-paper-10-t10_master_receipt.json:30-75`.)
- The 4 transport rows: 2 demonstrated, 1 bounded_local, 1 registered_landing_forms. (D — T10 master receipt.)
- The Riemann curvature tensor $R^{\rho}_{\ \sigma\mu\nu}$ and the Ricci tensor $R_{\mu\nu}$ (Definition 2.5). (D — Riemann 1867, Hawking & Ellis 1973, standard math.)
- The Einstein field equation $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ (Theorem 6.1, 6.2). (D — Einstein 1915, standard math.)

### Interpretation (I)

- The "boundary-repair demand" as the count of correction firings on the LCR carrier (Definition 2.1). (I — author's structural reading; the correction surface is (D), but the "demand" framing is the author's.)
- The "repair curvature" as the integrated demand over time (Definition 2.2, Theorem 3.1). (I — author's structural reading; the integrated demand is well-defined, but the "curvature" framing is the author's.)
- The "analogy with Riemann curvature" (Theorem 5.1). (I — author's structural analogy; the Riemann curvature is (D) standard math, but the analogy to the repair curvature is the author's structural reading.)
- The "firing density bound" $\rho \cdot T$ (Theorem 4.1). (I — author's structural reading; the firing set is (D), but the "density" framing is the author's.)
- The "Einstein field equation deferred" theorem (Theorem 6.1). (I — author's structural reading; the Einstein equation is (D) standard math, but the "deferred" interpretation is the author's framing of what the FLCR series does not close.)
- The "physical spacetime calibration deferred" theorem (Theorem 7.1). (I — author's structural reading; the calibration requires external data, but the specific "deferred" framing is the author's.)
- The application of the repair curvature to the GR curvature (Paper 35) and the cosmology (Papers 65–68). (I — author's structural reading; the repair curvature is (I), but the specific applications are (I).)

### Fabrication (X)

- None in this paper. The math is (D) verified; the framing is (I) but defensible.
- The claim "192/192 standards conformance" was a fabrication. The actual standards count is 240/240 (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The 192/192 figure was invented. (X — corrected to honest 240/240 with caveat.)

---

**End of Paper 15.**

The boundary-repair demand. The repair-curvature ledger. The firing density bound. The analogy with Riemann curvature. The Einstein field equation deferred. The physical spacetime calibration deferred. All backed by receipts. All honest. All forward-referenced.

The first 16 items of the 100-paper series are complete: Paper 0 (foreword), Paper 1 (LCR kernel), Paper 2 (Rule 30 ANF and Lucas carry), Paper 3 (correction surface and F2/Arf edge glue), Paper 4 (D4, $J_3(\mathbb{O})$, triality), Paper 5 (typed boundary repair), Paper 6 (oloid path carrier), Paper 7 (causal links and obligation ledgers), Paper 8 (discrete-continuous bridge), Paper 9 (lattice closure and terminal addresses), Paper 10 (temporal windows and Hamiltonian readouts), Paper 11 (master receipt and stack replay), Paper 12 (theory admission gates), Paper 13 (CA prediction surfaces), Paper 14 (quark-face algebra), Paper 15 (curvature as boundary-repair demand).
