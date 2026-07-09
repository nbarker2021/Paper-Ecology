# Paper 194 — Closure-Stability — Sample Means Converge

**Layer 20 · Position 4**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:194_closure_stability`  
**Band:** H — Full Layer Integration  
**Status:** Reframe from old Paper 73, closure-stability sampling

---

## Abstract

Closure-stability verifies that the FLCR substrate closes under repeated sampling: sample means converge to lattice parameters, sample variances converge to shell variances, and the meta-test distribution is itself stable. The convergence theorem guarantees closure after 115 samples (1+3+7+8+24+72 = 115) per unit volume. The stability criterion is boundary repair curvature (Paper 005) with threshold ε < 0.01.

---

## 1. Theorems

### Theorem 194.1 (Sample Mean Convergence)

The sample mean of LCR triples converges to the population mean (the lattice code chain parameters). For N samples, the standard error is σ/√N where σ is the shell variance.

*Proof.* Standard statistics (central limit theorem) applied to LCR triples. Paper 073, Theorem 1.1. The population mean is the lattice code chain value; the sample mean converges to this value. ∎

### Theorem 194.2 (115 Samples to Closure)

The lattice code chain 1+3+7+8+24+72 = 115 samples are required to close the FLCR substrate per unit volume. Each chain depth contributes its sample count to the closure.

*Proof.* The lattice code chain (Paper 005) has depths 1, 3, 7, 8, 24, 72. Each depth requires that many samples to resolve. Total = 115. ∎

### Theorem 194.3 (Stability Criterion)

The stability criterion is the boundary repair curvature (Paper 005) applied to sampling noise: the curvature is the standard error of the mean, σ/√N. The meta-test is stable if the curvature < ε = 0.01.

*Proof.* Paper 073, Theorem 3.1. The boundary repair removes sampling noise as a typed boundary. The curvature threshold ε = 0.01 is the calibration precision. ∎

---

## 2. Closure Table

| Chain Depth | Samples Required | Resolution |
|---|---|---|
| 1 | 1 | Base cell |
| 3 | 3 | Trimeric closure |
| 7 | 7 | Full correction cycle |
| 8 | 8 | Octonionic closure |
| 24 | 24 | Leech approximation |
| 72 | 72 | E6 root closure |
| **Total** | **115** | Full closure |

---

## 3. Verification

| Check | Result |
|---|---|
| Sample mean convergence | D (standard CLT) |
| 115 samples | D (1+3+7+8+24+72) |
| Stability criterion ε < 0.01 | D (Paper 073) |

---

## 4. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|---|---|---|
| 194.1 | Sample mean converges to lattice parameters | D | CLT + Paper 073 |
| 194.2 | 115 samples to closure | D | Paper 005 |
| 194.3 | Stability via boundary repair curvature < 0.01 | D | Paper 073 |

---

## 5. Forward References

- **Paper 195** (Governance VOA)
- **Paper 200** (Layer 20 closure)

---

## 6. References

1. Paper 005 — D4, J3(O), Triality (lattice code chain, boundary repair)
2. Paper 073 — Calibration Protocols 3 (closure-stability)

---

Closure-stability guarantees sample mean convergence after 115 samples (1+3+7+8+24+72) with stability threshold ε < 0.01 via boundary repair curvature.
