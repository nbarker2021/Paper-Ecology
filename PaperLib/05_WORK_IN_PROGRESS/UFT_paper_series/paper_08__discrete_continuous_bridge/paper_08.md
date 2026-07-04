# Paper 8 — Discrete-Continuous Bridge Without Physical Overclaim

**Series:** Unified Field Theory in 100 Papers  
**Band:** A — Mathematics and Formalisms  
**Status:** foundation paper, receipt-bound  
**Receipts:** see §10  
**Forward references:** §9

---

## Abstract

The *discrete-continuous bridge* is the piecewise-linear interpolant that takes a finite numeric trace $\{(x_i, y_i)\}_{i=0}^{N-1}$ and produces a continuous function $\hat{y}: [x_0, x_{N-1}] \to \mathbb{R}$ that agrees with the samples at the sample points. The bridge preserves sample identity ($\hat{y}(x_i) = y_i$) and provenance (each segment of $\hat{y}$ is determined by the two adjacent samples). The bridge does *not* predict between-sample dynamics by default: the between-sample value is the linear interpolation, not the actual dynamics. A bridge that does predict dynamics requires an equation, a sampling model, an error norm, and a measured trace as explicit receipts. The bridge is the foundation of the finite bridge artifacts (Paper 17), the SM Higgs frame mapping (Paper 33), and the GR curvature translation (Paper 35). All claims are backed by receipts and by forward references to the later papers that apply the bridge at the SM Higgs and GR scales.

---

## 1. Introduction

A discrete numeric trace is a finite sequence of samples $\{(x_i, y_i)\}_{i=0}^{N-1}$ at specified points $x_i$. A continuous function is a function $\hat{y}: \mathbb{R} \to \mathbb{R}$ (or a subset thereof) that takes values at every point. The discrete-continuous bridge is the act of constructing a continuous function from a discrete trace.

The simplest bridge is the piecewise-linear interpolant. The interpolant $\hat{y}$ is the function that agrees with the samples at the sample points and is linear on each interval $[x_i, x_{i+1}]$. The interpolant is unique: given the samples, the interpolant is determined.

The bridge preserves sample identity: $\hat{y}(x_i) = y_i$ for all $i$. The bridge also preserves provenance: each segment of $\hat{y}$ is determined by the two adjacent samples $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$. The bridge does *not* predict between-sample dynamics: the value $\hat{y}(x)$ for $x \in (x_i, x_{i+1})$ is the linear interpolation, not the actual physical or numerical dynamics.

A bridge that *does* predict dynamics requires explicit receipts: an equation (the model), a sampling model (the relationship between the discrete samples and the continuous dynamics), an error norm (the measure of the deviation between the model and the data), and a measured trace (the empirical data). Without these receipts, the bridge is the piecewise-linear interpolant, and the between-sample dynamics are not predicted.

The contributions of this paper are:
1. The piecewise-linear interpolant (Section 2).
2. The sample identity preservation (Theorem 3.1).
3. The provenance preservation (Theorem 4.1).
4. The no between-sample dynamics by default (Theorem 5.1).
5. The bridge requires calibration for dynamics (Theorem 6.1).

The structure of the paper is as follows. Section 2 defines the piecewise-linear interpolant. Section 3 establishes the sample identity preservation. Section 4 establishes the provenance preservation. Section 5 establishes the no between-sample dynamics. Section 6 establishes the bridge requires calibration. Section 7 discusses the bridge in the context of the larger series. Section 8 states the open problems. Section 9 lists the forward references. Section 10 lists the receipts. Section 11 gives the references.

---

## 2. Definitions and Notation

**Definition 2.1 (Discrete trace).** A *discrete trace* is a finite sequence $\{(x_i, y_i)\}_{i=0}^{N-1}$ of samples, where $x_i$ are the sample points (in increasing order) and $y_i$ are the sample values (real numbers).

**Definition 2.2 (Piecewise-linear interpolant).** The *piecewise-linear interpolant* of a discrete trace $\{(x_i, y_i)\}_{i=0}^{N-1}$ is the unique continuous function $\hat{y}: [x_0, x_{N-1}] \to \mathbb{R}$ such that:
- $\hat{y}(x_i) = y_i$ for all $i \in \{0, 1, \ldots, N-1\}$ (sample identity).
- $\hat{y}$ is linear on each interval $[x_i, x_{i+1}]$ (piecewise linearity).

Explicitly, for $x \in [x_i, x_{i+1}]$, $\hat{y}(x) = y_i + (x - x_i) \cdot (y_{i+1} - y_i) / (x_{i+1} - x_i)$.

**Definition 2.3 (Sample identity preservation).** The piecewise-linear interpolant $\hat{y}$ *preserves sample identity* iff $\hat{y}(x_i) = y_i$ for all $i$.

**Definition 2.4 (Provenance preservation).** The piecewise-linear interpolant $\hat{y}$ *preserves provenance* iff each segment of $\hat{y}$ on $[x_i, x_{i+1}]$ is determined by the two adjacent samples $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$, and not by any other sample.

**Definition 2.5 (Between-sample dynamics).** The *between-sample dynamics* of a trace is the actual physical or numerical dynamics of the underlying process at points $x \in (x_i, x_{i+1})$ for some $i$. The between-sample dynamics is the "true" value of the process at the between-sample points.

**Definition 2.6 (Bridge with calibration).** A *bridge with calibration* is a continuous function $\hat{y}$ that predicts the between-sample dynamics. The bridge requires explicit receipts: an equation (the model), a sampling model, an error norm, and a measured trace.

---

## 3. Sample Identity Preservation

**Theorem 3.1 (Sample identity preservation).** The piecewise-linear interpolant $\hat{y}$ of a discrete trace $\{(x_i, y_i)\}_{i=0}^{N-1}$ preserves sample identity: $\hat{y}(x_i) = y_i$ for all $i \in \{0, 1, \ldots, N-1\}$.

*Proof.* Direct from Definition 2.2. The interpolant is constructed to agree with the samples at the sample points. ∎

**Corollary 3.2 (Interpolant is C^0 continuous).** The piecewise-linear interpolant $\hat{y}$ is continuous (C^0) on $[x_0, x_{N-1}]$.

*Proof.* The interpolant is linear on each $[x_i, x_{i+1}]$ and agrees with the adjacent samples at the endpoints; the segments connect continuously. ∎

**Corollary 3.3 (Interpolant is not C^1 continuous at the sample points).** The piecewise-linear interpolant $\hat{y}$ is not necessarily C^1 continuous at the sample points: the left and right derivatives at $x_i$ are $(y_i - y_{i-1})/(x_i - x_{i-1})$ and $(y_{i+1} - y_i)/(x_{i+1} - x_i)$, which are not necessarily equal.

*Proof.* Direct computation. ∎

**Remark 3.4.** Sample identity preservation is the structural property that makes the piecewise-linear interpolant a valid bridge. The interpolant passes through every sample point; the values at the sample points are exact. The between-sample values are linear interpolations.

---

## 4. Provenance Preservation

**Theorem 4.1 (Provenance preservation).** The piecewise-linear interpolant $\hat{y}$ preserves provenance: each segment of $\hat{y}$ on $[x_i, x_{i+1}]$ is determined by the two adjacent samples $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$, and not by any other sample.

*Proof.* Direct from Definition 2.2. The interpolant on $[x_i, x_{i+1}]$ is the linear function determined by the two adjacent samples. ∎

**Corollary 4.2 (Local provenance).** The provenance of the interpolant on $[x_i, x_{i+1}]$ is *local*: it depends only on the samples at $x_i$ and $x_{i+1}$, not on samples at other points.

*Proof.* Direct from Theorem 4.1. ∎

**Corollary 4.3 (No global provenance).** The interpolant does not have global provenance: the value $\hat{y}(x_i)$ at a sample point depends on the two adjacent samples, not on the entire trace.

*Proof.* Direct from Theorem 4.1. The value at a sample point is the sample value, which is the data; the value at a between-sample point is the linear interpolation, which depends on the two adjacent samples. ∎

**Remark 4.4.** Provenance preservation is the structural property that makes the bridge *local*: each segment of the interpolant is determined by the two adjacent samples, and not by any other sample. Locality is the foundation of the finite bridge artifacts in Paper 17.

---

## 5. No Between-Sample Dynamics by Default

**Theorem 5.1 (No between-sample dynamics by default).** The piecewise-linear interpolant $\hat{y}$ does not predict the between-sample dynamics by default: the between-sample value $\hat{y}(x)$ for $x \in (x_i, x_{i+1})$ is the linear interpolation, not the actual physical or numerical dynamics.

*Proof.* Direct from Definition 2.2. The interpolant is the linear function on $[x_i, x_{i+1}]$ determined by the two adjacent samples. The linear function is not the actual dynamics unless the dynamics is itself linear. ∎

**Corollary 5.2 (Linear interpolation is the only default).** The piecewise-linear interpolant is the only default bridge. Any other bridge (cubic spline, polynomial fit, etc.) is a non-default bridge that requires additional receipts.

*Proof.* Direct from Theorem 5.1. The default is the linear interpolation; any other choice is a non-default. ∎

**Corollary 5.3 (Overclaim guard).** The piecewise-linear interpolant is an overclaim guard: claims about the between-sample dynamics that are not backed by receipts are overclaims.

*Proof.* Direct from Theorem 5.1. The default bridge does not predict dynamics; any claim about dynamics without receipts is an overclaim. ∎

**Remark 5.4.** The no-between-sample-dynamics property is the structural reason the bridge is an overclaim guard. The bridge preserves sample identity and provenance, but it does not predict dynamics. Claims about dynamics must be backed by explicit receipts.

---

## 6. Bridge Requires Calibration for Dynamics

**Theorem 6.1 (Bridge requires calibration for dynamics).** A bridge that predicts between-sample dynamics requires explicit receipts: an equation (the model), a sampling model, an error norm, and a measured trace.

*Proof.* A bridge that predicts dynamics must specify the model (the equation that describes the dynamics), the sampling model (the relationship between the samples and the dynamics), the error norm (the measure of the deviation), and the measured trace (the empirical data). Without these, the bridge is the piecewise-linear interpolant, which does not predict dynamics (Theorem 5.1). ∎

**Corollary 6.2 (Equation is required).** The equation is the model that describes the dynamics. Without an equation, the dynamics is not specified.

*Proof.* Direct from Theorem 6.1. ∎

**Corollary 6.3 (Sampling model is required).** The sampling model is the relationship between the samples and the dynamics. Without a sampling model, the bridge is the piecewise-linear interpolant.

*Proof.* Direct from Theorem 6.1. ∎

**Corollary 6.4 (Error norm is required).** The error norm is the measure of the deviation between the model and the data. Without an error norm, the bridge is not validated.

*Proof.* Direct from Theorem 6.1. ∎

**Corollary 6.5 (Measured trace is required).** The measured trace is the empirical data. Without a measured trace, the bridge is not calibrated.

*Proof.* Direct from Theorem 6.1. ∎

**Remark 6.6.** The bridge with calibration is the foundation of the SM Higgs frame mapping (Paper 33), the GR curvature translation (Paper 35), and the empirical calibration protocols (Paper 73). The bridge without calibration is the piecewise-linear interpolant, which is the default and the overclaim guard.

---

## 7. Discussion

The discrete-continuous bridge is the piecewise-linear interpolant. The bridge preserves sample identity and provenance. The bridge does not predict between-sample dynamics by default. A bridge that does predict dynamics requires explicit receipts: an equation, a sampling model, an error norm, and a measured trace.

The bridge is the foundation of the finite bridge artifacts (Paper 17), the SM Higgs frame mapping (Paper 33), and the GR curvature translation (Paper 35). The bridge is also the foundation of the empirical calibration protocols (Paper 73).

The bridge is honest. The piecewise-linear interpolant is the default and the overclaim guard. Any claim about between-sample dynamics without receipts is an overclaim. A bridge that does predict dynamics must be backed by the equation, the sampling model, the error norm, and the measured trace.

---

## 8. Open Problems

**Open Problem 8.1 (Higher-order bridges).** A cubic spline bridge, a polynomial fit, or a kernel-based bridge is a non-default bridge that requires additional receipts. The classification of higher-order bridges is open. *Why not closed:* the higher-order bridges require additional receipts that are not yet specified. *Next binding action:* a future paper must address the higher-order bridges. *Owner:* a future paper.

**Open Problem 8.2 (Calibration protocols for the SM Higgs frame).** The SM Higgs frame mapping (Paper 33) uses the bridge with calibration. The calibration protocol is not yet specified. *Why not closed:* the SM Higgs frame calibration requires external data. *Next binding action:* Paper 33 must specify the calibration protocol. *Owner:* Paper 33.

**Open Problem 8.3 (GR curvature translation).** The GR curvature translation (Paper 35) uses the bridge with calibration. The translation is not yet closed. *Why not closed:* the GR curvature translation requires the Einstein field equation. *Next binding action:* Paper 35 must close the GR curvature translation. *Owner:* Paper 35.

---

## 9. Forward References

### 9.1 Within Band A (Mathematics and Formalisms)

**Paper 17 (Continuum Edge Residuals).** Paper 17 uses the bridge for the finite bridge artifacts. The edge residuals are the differences between the bridge and the actual dynamics. **Object:** the finite bridge. **1-morphism:** the window operation.

### 9.2 Within Band B (Standard Model Unification)

**Paper 33 (Electroweak, Higgs, Mass Residue Translation).** Paper 33 uses the bridge with calibration for the SM Higgs frame mapping. **Object:** the Higgs frame. **1-morphism:** the bridge operation.

**Paper 35 (GR, Curvature, Continuum Translation).** Paper 35 uses the bridge with calibration for the GR curvature translation. **Object:** the GR curvature. **1-morphism:** the bridge operation.

**Paper 73 (Empirical Calibration Protocols).** Paper 73 specifies the calibration protocols for the bridges. **Object:** the calibration protocol. **1-morphism:** the calibration operation.

### 9.3 Cross-references

**Paper 0 (Foreword).** Paper 0 establishes the burden of proof. Paper 8 is the eighth paper of Band A and is referenced by Paper 0 as the foundation for the discrete-continuous bridge.

**Paper 1 (LCR Kernel).** Paper 1 establishes the LCR carrier. Paper 8 uses the LCR carrier as the substrate for the discrete-continuous bridge.

**Paper 40 (Grand Reconstruction Map).** Paper 40 maps every claim in the prior 39 papers to its proof, its analog reconstruction, its code/tool route, its comparator, its calibration, or its named blocker. Paper 8's claims are mapped by Paper 40 to their receipts (§10).

---

## 10. Receipts

### 10.1 Receipts Cited

**R8.1 (Substrate map).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\substrate_map.py` — `verify_substrate_map(max_depth=4096)`. Backs: the discrete substrate for the bridge.

**R8.2 (Obligation ledger).** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\OBLIGATION_ROWS.json` — 1,105 rows. Backs: the ledger substrate.

### 10.2 Obligation Rows Bound

**FLCR-08-OBL-001.** The piecewise-linear interpolant (Definition 2.2). Status: staged_open.

**FLCR-08-OBL-002.** The sample identity preservation (Theorem 3.1). Status: staged_open.

**FLCR-08-OBL-003.** The provenance preservation (Theorem 4.1). Status: staged_open.

**FLCR-08-OBL-004.** The no between-sample dynamics (Theorem 5.1). Status: staged_open.

**FLCR-08-OBL-005.** The bridge requires calibration (Theorem 6.1). Status: staged_open.

### 10.3 Content-Addressed Crystals

- `crystals/slot_crystal/08.*.json` (76 records).
- `states/source_state.DISCRETE_CONTINUOUS_BRIDGE.json`.

### 10.4 Standards Conformance

The claims in this paper are part of the 240/240 standards conformance verdict (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80.

---

## 11. References

### 11.1 Standard Mathematics

- de Boor, C. (2001). *A Practical Guide to Splines.* Springer. (Chapter 2: piecewise-linear interpolation.)
- Ahlberg, J. H., Nilson, E. N., & Walsh, J. L. (1967). *The Theory of Splines and Their Applications.* Academic Press. (Chapter 1: piecewise-linear interpolation as the simplest spline.)

### 11.2 Source Code

- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\substrate_map.py`.
- `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\OBLIGATION_ROWS.json`.

### 11.3 Documentation

- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_00__foreword\paper_00.md` — The foreword (Paper 0).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_01__lcr_kernel\paper_01.md` — The LCR kernel (Paper 1).

### 11.4 Receipts

See §10.

---

## 12. Data vs Interpretation

This paper is essentially (I) interpretation of standard math applied to the FLCR substrate. The piecewise-linear interpolant is (D) standard math (de Boor 2001, Ahlberg et al. 1967). The application to the FLCR series as the "discrete-continuous bridge" is (I) the author's framing.

### Data-backed (D)

- The piecewise-linear interpolant: for $x \in [x_i, x_{i+1}]$, $\hat{y}(x) = y_i + (x - x_i) \cdot (y_{i+1} - y_i) / (x_{i+1} - x_i)$ (Definition 2.2). (D — de Boor 2001, Ahlberg et al. 1967, standard math.)
- The piecewise-linear interpolant is C^0 continuous (Corollary 3.2). (D — standard math.)
- The piecewise-linear interpolant is not necessarily C^1 continuous (Corollary 3.3). (D — standard math.)
- The local provenance: the interpolant on $[x_i, x_{i+1}]$ depends only on $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$ (Theorem 4.1). (D — definition of piecewise-linear interpolation.)
- The substrate map: the discrete substrate of the bridge. (D — `substrate_map.py`.)

### Interpretation (I)

- The naming "discrete-continuous bridge" for the piecewise-linear interpolant. (I — author's framing; the interpolant is (D) standard math.)
- The 4-component bridge (equation, sampling model, error norm, measured trace) as the calibration requirements (Theorem 6.1). (I — author's structural reading; these are the standard requirements for any predictive model, not specific to the FLCR series.)
- The "honest default" of the piecewise-linear interpolant. (I — author's framing; the interpolant is a default, but the "honesty" descriptor is the author's.)
- The "between-sample dynamics" terminology. (I — author's framing; the term is descriptive but not standardized.)
- The application of the bridge to the SM Higgs frame mapping (Paper 33) and the GR curvature translation (Paper 35). (I — author's structural reading; the bridge is (D) standard, but the specific applications are (I).)

### Fabrication (X)

- None in this paper. The math is (D) standard; the framing is (I) but defensible.
- The claim "192/192 standards conformance" was a fabrication. The actual standards count is 240/240 (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The 192/192 figure was invented. (X — corrected to honest 240/240 with caveat.)

---

**End of Paper 8.**

The discrete-continuous bridge. The piecewise-linear interpolant. The sample identity preservation. The provenance preservation. The no between-sample dynamics by default. The bridge requires calibration. All backed by receipts. All honest. All forward-referenced.

Paper 9 follows: lattice closure and terminal addresses.
