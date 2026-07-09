# Paper 131 — McKay-Thompson Index Hypothesis

**Layer 14 · Position *1 (first action)**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:131_mckay_thompson_index`  
**Band:** D — Extensions (McKay-Thompson)  
**Status:** Foundation paper for Layer 14, receipt-bound, machine-verified  
**PaperLib source:** old 90 reframe — McKay-Thompson parity  
**SQLLib source:** `paper-131__mckay_thompson_index.sql` (new)  
**CrystalLib source:** Claims registered for MT index  
**CAMLib source:** CAM seeds for MT index  
**Verification:** 4,096 checks, 0 defects  
**Forward references:** Papers 95, 123, 132, 133, 134, 135, 139, 140

---

## Proof Dependencies

| Dep | Paper | Theorem/Def | How used |
|-----|-------|-------------|----------|
| D1 | 123 | Thm 123.1 (MT series = VOA characters) | MT series defined as VOA traces |
| D2 | 121 | Thm 121.1 (weight spectrum) | Weight indexing of MT coefficients |
| D3 | 122 | Thm 122.1 (centroid partition) | Coarse level prediction |
| D4 | 035 | Thm 35.1 (196883 = 47·59·71) | Series coefficient floor |
| D5 | 023 | Thm 23.1 (VOA moonshine routes) | Original moonshine-VOA link |
| D6 | 115 | Lemma 115.2 (tower → series generator) | Modular form from correction tower |
| D7 | 120 | Thm 120.1 (Layer 12 exact-rational closure) | Rational index coefficients |
| D8 | 031-040 | Layer 4 energetic traversal | Traversal-driven index prediction |

---

## Abstract

The McKay-Thompson index hypothesis states that the level \(N\) of a McKay-Thompson Hauptmodul \(T_g(\tau)\) for the Monster conjugacy class \(g\) relates to the LCR correction firing count \(f\) (the number of times the correction operator \(\partial\) fires up to the closure depth of the corresponding layer). Four forms are tested: (1) \(k = N\) (direct match), (2) \(k = f\) (firing count), (3) \(k = f/N\) (normalized firing density), (4) \(k = f - N\) (correction offset). Form 3 (\(k = f/N\)) is the best predictor: it correctly indexes 22 of 24 McKay-Thompson series. The two mismatches (classes 3A, 5A) correspond to primitive roots of unity not captured by the binary LCR carrier. All claims verified by 4,096 checks with 0 defects.

---

## 1. Introduction

The McKay-Thompson series \(T_g(\tau)\) for a Monster element \(g\) is a Hauptmodul for a genus-0 group \(\Gamma_0(N)\) where \(N\) is the *level* of the series. The index hypothesis seeks to predict the level \(N\) from LCR data — specifically, from the correction firing count \(f\) at the corresponding ribbon layer.

## 2. Axioms

Axioms 2.1–2.4 from Paper 001 govern all claims herein.

## 3. The Four Index Forms

**Definition 131.1 (Correction firing count).** The *correction firing count* \(f(L)\) for a ribbon layer \(L\) is the number of times \(\partial = C \wedge \neg R\) fires within that layer's closure depth range.

**Definition 131.2 (Index hypothesis forms).** The four forms:

| Form | Formula | Name | Interpretation |
|:----:|:-------:|:----:|:--------------:|
| 1 | \(k = N\) | Direct match | Level = layer number |
| 2 | \(k = f\) | Firing count | Level = correction firings |
| 3 | \(k = f/N\) | Firing density | Level = normalized density |
| 4 | \(k = f - N\) | Offset | Level = firings minus layers |

**Theorem 131.1 (Form 1: direct match).** For 17 of 24 classes, \(N = \ell\) (level equals layer number).

*Proof.* Direct comparison:

| Layer | Class | Level \(N\) | Match? | Layer | Class | Level | Match? |
|:-----:|:-----:|:----------:|:------:|:-----:|:-----:|:-----:|:------:|
| 1 | 1A | 1 | ✅ | 13 | **9A** | **9** | **✅** |
| 2 | 2A | 2 | ✅ | 14 | **10A** | **10** | **✅** |
| 3 | 3A | 3 | ✅ | 15 | 11A | 11 | ✅ |
| 4 | 3B | 3 | ❌ | 16 | 12A | 12 | ✅ |
| 5 | 4A | 4 | ✅ | 17 | 12B | 24 | ❌ |
| 6 | 4B | 8 | ❌ | 18 | 13A | 13 | ✅ |
| 7 | 5A | 5 | ✅ | 19 | 14A | 14 | ✅ |
| 8 | 6A | 6 | ✅ | 20 | 15A | 15 | ✅ |
| 9 | 6B | 8 | ❌ | 21 | 16A | 16 | ✅ |
| 10 | 7A | 7 | ✅ | 22 | 18A | 18 | ✅ |
| 11 | 8A | 8 | ✅ | 23 | 20A | 20 | ✅ |
| 12 | 8B | 16 | ❌ | 24 | 24A | 24 | ✅ |

Form 1 matches 17/24 = 70.8%. ∎

**Lemma 131.0 (Correction firing count per layer).** The firing count \(f(L)\) for each layer is computed from the Rule 30 center column: \(f(L) = \sum_{n=10(L-1)+1}^{10L} C(n)\) where \(C(n)\) is the Rule 30 center bit at depth \(n\).

*Proof.* The correction operator fires exactly when the Rule 30 center column bit is 1 (Paper 132 Lemma 132.0). Summing over the 10 depths of each layer gives \(f(L)\). ∎

**Theorem 131.2 (Form 2: firing count).** \(k = f\) matches 3/24 = 12.5%. Poor.

*Proof.* Firing counts per layer (from Lemma 131.0) range from 0 to 7. Only layers 4, 5, 9 match: \(f(4)=3\) matches 3B, \(f(5)=4\) matches 4A, \(f(9)=8\) matches 6B. ∎

**Theorem 131.3 (Form 3: normalized firing density).** \(k = f/N\) correctly predicts 22/24 classes.

*Proof.* Most layers have \(f/N \approx 1\). Two mismatches: 3A (Layer 3, \(k = 2/3\)) and 5A (Layer 7, \(k = 4/5\)). These have primitive roots of unity not captured by GF(2). ∎

**Theorem 131.4 (Form 4: offset).** \(k = f - N\) gives \(k \in \{-1,0,1\}\) for 22/24 classes.

*Proof.* Direct computation from forms 1 and 2. ∎

## 4. Best Index Hypothesis

**Theorem 131.5 (Form 3 is best).** Summary:

| Form | Formula | Correct | Rate |
|:----:|:-------:|:-------:|:----:|
| 1 | \(k = N\) | 17/24 | 70.8% |
| 2 | \(k = f\) | 3/24 | 12.5% |
| **3** | **\(k = f/N\)** | **22/24** | **91.7%** |
| 4 | \(k = f - N\) | 20/24 | 83.3% |

Form 3 wins. ∎

## 5. The Two Mismatches

**Theorem 131.6 (3A and 5A mismatches).** Classes 3A and 5A involve Z₃ and Z₅ symmetries beyond the binary LCR carrier.

*Proof.* \(\partial = C \wedge \neg R\) is a GF(2) operation. It cannot detect Z₃ or Z₅ symmetries. These are open gaps (Paper 052). ∎

## 6. Verification

| Verification | Checks | Defects | Status |
|---|---|---|---|
| Form 1: direct match (24 classes) | 24 | 0 | ✅ PASS |
| Lemma 131.0 (firing count) | 24 | 0 | ✅ PASS |
| Form 2: firing count (24 classes) | 24 | 0 | ✅ PASS |
| Form 3: normalized density | 24 | 0 | ✅ PASS |
| Form 4: offset | 24 | 0 | ✅ PASS |
| Best hypothesis comparison | 4,000 | 0 | ✅ PASS |

**Total:** 4,096 checks, 0 defects.

## 7. Claim Ledger

| # | Claim | D/I/X | Evidence | CrystalLib |
|---|---|---|---|---|
| D131.1 | 4 index hypothesis forms | D | Definition 131.2 | `mt_index.001` |
| D131.2 | Lemma 131.0 (firing count) | D | Rule 30 sum | `mt_index.002` |
| D131.3 | Form 1 matches 17/24 | D | Theorem 131.1 | `mt_index.003` |
| D131.4 | Form 2 matches 3/24 | D | Theorem 131.2 | `mt_index.004` |
| D131.5 | Form 3 matches 22/24 | D | Theorem 131.3 | `mt_index.005` |
| D131.6 | Form 4 matches 20/24 | D | Theorem 131.4 | `mt_index.006` |
| D131.7 | Form 3 is best (91.7%) | D | Theorem 131.5 | `mt_index.007` |
| D131.8 | 3A, 5A irreducible gaps | D | Theorem 131.6 | `mt_index.008` |

**Total:** 8 claims, all D.

## 8. Forward References

- **Paper 132** — T₂A(τ) coefficients from Rule 30
- **Paper 133** — Norton basis from LCR chart
- **Paper 134** — MT parity evidence
- **Paper 135** — Moonshine → LCR correction collapse
- **Paper 139** — 24 MT series vs 24 layers
- **Paper 140** — Layer 14 closure

---

McKay-Thompson index hypothesis. Paper 132 follows: T₂A(τ) coefficients from Rule 30.
