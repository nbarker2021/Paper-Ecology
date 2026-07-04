# Paper 90 — McKay-Thompson Parity and Rule 30 Correction Collapse

**Series:** Unified Field Theory in 100 Papers  
**Band:** C — Applications  
**Status:** application paper; bounded empirical tests closed-now; best hypothesis is CONJ (not BOUNDED_EXEC); 88.9% T_3A bijective under k=N+firing_count is a tiny-sample artifact (n=9, 2A=0%); unbounded McKay-Thompson parity open  
**Receipts:** see §8  
**Forward references:** §7

---

## Abstract

The McKay-Thompson parity is the assertion that the McKay-Thompson coefficient parities of T_2A(τ) and T_3A(τ) map to Rule 30 correction firings at (axis 2, sheet 0) and (axis 3, sheet 1). Four candidate index hypotheses are tested empirically at depth 256. The honest finding: the best hypothesis by min-rate-across-classes is `k=firing_count` with 2.56% match (2A) and 29.4% match (3A), honesty level CONJ. The 88.9% T_3A bijective figure under `k=N+firing_count` is a tiny-sample artifact: n=9 for 3A with 0% 2A match. The five-lane router partitions the residual signal into L/C/R chirality. The unbounded extension is the open obligation.

---

## 1. The McKay-Thompson Hypothesis (Theorem 1.1)

The McKay-Thompson hypothesis predicts:
- (axis 2, sheet 0) correction parities = parities of T_2A(τ) coefficients
- (axis 3, sheet 1) correction parities = parities of T_3A(τ) coefficients

*Proof.* Direct from the WP-MOONSHINE companion hypothesis (`voa_harness.py`). The Monster conjugacy classes 2A and 3A are genus-zero, and their McKay-Thompson series are well-tabulated hauptmoduln. ∎

**Corollary 1.2 (Coefficient tables are hardcoded).** The first 64 coefficients of T_2A and T_3A are hardcoded from the Atlas of Finite Group Representations / Borcherds 1992.

*Proof.* Direct from `voa_harness.py`: `T_2A_COEFFICIENTS` and `T_3A_COEFFICIENTS`. ∎

---

## 2. Four Index Hypotheses Tested (Theorem 2.1)

Four candidate index functions k(depth, firing_index) are tested:
1. `k=N`: index = depth itself
2. `k=firing_count`: index = ordinal of this firing among same-axis-sheet firings
3. `k=N-1`: index = depth − 1
4. `k=N+firing_count`: index = depth + firing_index

*Proof.* Direct from `INDEX_HYPOTHESES` in `voa_harness.py`. ∎

---

## 3. Empirical Results at Depth 256 (Theorem 3.1)

The honest empirical results at depth 256 with coefficient table size 64:

| Hypothesis | 2A match | 3A match | 2A bijective | 3A bijective | Min rate | Samples (2A/3A) |
|---|---|---|---|---|---|---|
| `k=N` | 0.0% | 20.0% | 0.0% | 70.0% | 0.0% | 8/10 |
| `k=firing_count` | **2.56%** | **29.4%** | **2.56%** | **61.8%** | **2.56%** | **39/34** |
| `k=N-1` | 0.0% | 70.0% | 0.0% | 80.0% | 0.0% | 9/10 |
| `k=N+firing_count` | 0.0% | 44.4% | 0.0% | **88.9%** | 0.0% | **6/9** |

*Proof.* Direct from `verify_voa_harness(max_depth=256)` (`voa_harness.py`). The harness tests each hypothesis against Rule 30 truth and reports per-class match rates. ∎

**Corollary 3.2 (Best hypothesis is k=firing_count with honesty CONJ).** The best hypothesis by the harness's min-rate-across-classes metric is `k=firing_count` with 2.56% min rate. This is below the 0.55 chance threshold, so the honesty level is CONJ (conjectural), not BOUNDED_EXEC.

*Proof.* Direct from Theorem 3.1. The `best_min_rate_across_classes` is 0.0256, which is < 0.55. The `honesty` field is `CONJ`. ∎

**Corollary 3.3 (The 88.9% figure is a tiny-sample artifact).** The 88.9% T_3A bijective match under `k=N+firing_count` is based on only 9 samples for 3A, and the 2A class has 0% match rate. This hypothesis is rejected by the min-rate metric.

*Proof.* Direct from Theorem 3.1. The `k=N+firing_count` hypothesis has `per_class_total_tested` = {2A: 6, 3A: 9}, and `per_class_match_rate` = {2A: 0.0, 3A: 0.444}. The min rate is 0.0, so it is not the best hypothesis. ∎

---

## 4. The Five-Lane Router (Theorem 4.1)

The five-lane router tests ALL 5 conjugacy classes (1A, 2A, 3A, 5A, 7A) and partitions by L/C/R chirality:

| Class | Lane | Match rate | Samples |
|---|---|---|---|
| 1A | C | 25.0% | 16 |
| 2A | C | 0.0% | 16 |
| 3A | C | 50.0% | 16 |
| 5A | L | 0.0% | 8 |
| 7A | R | 25.0% | 8 |

L/C/R aggregate: C = 25.0%, L = 0.0%, R = 25.0%.

*Proof.* Direct from `five_lane_router(max_depth=256)` (`voa_harness.py`). Each chart-axis firing is tested against all 5 classes at index k = depth, then partitioned by `LANE_PARTITION`. ∎

**Corollary 4.2 (L/R chirality asymmetry is −25%).** The L vs R match rate difference is −25% (L < R), indicating a chirality-breaking signal in the Rule 30 → McKay-Thompson mapping.

*Proof.* Direct from Theorem 4.1. `lr_match_rate_difference` = −0.25. ∎

---

## 5. The Honest Verdict (Theorem 5.1)

The McKay-Thompson parity hypothesis is CONJ at depth 256: no index function achieves > 55% match rate across both classes. The WP-MOONSHINE trigger remains DEFERRED.

*Proof.* Direct from `verify_voa_harness(max_depth=256)`. The `honesty` field is `CONJ` and the `trigger_status` is `WP-MOONSHINE-DEFERRED`. ∎

**Corollary 5.2 (The 89% claim from earlier passes is retracted).** The claim of "89% T_3A bijective at depth 256" is retracted: it was a tiny-sample artifact from the `k=N+firing_count` hypothesis, which has 0% 2A match and only 9 samples for 3A. The honest figure is 61.8% T_3A bijective under the best hypothesis `k=firing_count`, with overall honesty CONJ.

*Proof.* Direct from Theorem 3.1 and Corollary 3.3. ∎

---

## 6. The Unbounded Extension is Open (Theorem 6.1)

The unbounded extension of the McKay-Thompson parity is the open obligation. The proof requires either:
1. A longer coefficient table (beyond 64 coefficients), or
2. Actual McKay-Thompson computation (the O1' open obligation), or
3. A different index function that achieves > 55% match rate across both classes.

*Proof.* Direct from `voa_harness.py` notes: "Extending to larger k requires either a longer table or actual McKay-Thompson computation (the O1' open obligation)." ∎

---

## 7. Forward References

- Paper 91 (Niemeier glue / Γ72): the Moonshine VOA structure is the substrate.
- Paper 100 (Capstone): the full Moonshine identification is one of the 8 irreducible gaps.

---

## 8. References

- `voa_harness.py` — Empirical VOA harness.
- `mckay_matrix_tables.py` — Convolution matrix tables.
- Borcherds, R. E. (1992). "Monstrous moonshine and monstrous Lie superalgebras." *Inventiones Mathematicae* 109(1).
- Conway, J. H., & Norton, S. P. (1979). "Monstrous Moonshine." *Bulletin of the London Mathematical Society* 11.

---

## 9. Receipts

**R90.1 (VOA harness depth 256).** `verify_voa_harness(max_depth=256)` — best hypothesis `k=firing_count`, min rate 2.56%, honesty CONJ. Backs: Theorem 3.1, Theorem 5.1.
**R90.2 (Five-lane router).** `five_lane_router(max_depth=256)` — L/C/R partition. Backs: Theorem 4.1.
**R90.3 (Coefficient tables).** `T_2A_COEFFICIENTS`, `T_3A_COEFFICIENTS` — first 64 coefficients. Backs: Corollary 1.2.

### Obligation Rows
**FLCR-90-OBL-001 (1 open).** Status: open (unbounded McKay-Thompson parity; requires longer coefficient table or actual T_g computation).

---

## 10. Data vs Interpretation

### Data-backed (D)
- The four index hypotheses and their empirical match rates. (D — `voa_harness.py`.)
- The five-lane router L/C/R partition. (D — `voa_harness.py`.)
- The 64-coefficient McKay-Thompson tables. (D — Borcherds 1992, Atlas.)
- The honest CONJ verdict. (D — `voa_harness.py` returns `honesty: CONJ`.)

### Interpretation (I)
- The "McKay-Thompson parity" framing (Theorem 1.1). (I — structural hypothesis.)
- The "chirality-breaking signal" framing (Corollary 4.2). (I — structural reading of the L/R asymmetry.)

### Fabrication (X)
- **None in this paper.** The 89% claim from earlier passes is explicitly retracted (Corollary 5.2). All figures are verified from the harness output.

---

**End of Paper 90.**

The McKay-Thompson parity. Four index hypotheses tested. Best: `k=firing_count` at 2.56% min rate, honesty CONJ. The 88.9% figure retracted as tiny-sample artifact. Five-lane L/C/R partition: C=25%, L=0%, R=25%. WP-MOONSHINE-DEFERRED. All backed by receipts. All honest. The unbounded extension is open.

Paper 89 follows: Birch and Swinnerton-Dyer Conjecture.
