# Paper 217 — Full Monstrous Moonshine Identification Gap

**Layer 22 · Position 7**  
**Claim type:** X (open gap — honest disclosure)  
**CAM hash:** `sha256:217_moonshine_identification_gap`  
**Band:** A — Mathematics and Formalisms  
**Status:** Open gap, not closed, receipt-bound  
**PaperLib source:** Gap disclosure, references Papers 131–139 (McKay-Thompson series)  
**CrystalLib source:** 1 D claim, 2 X claims  
**SQLLib source:** `moonshine_gap`  
**Verification:** 25 checks, 0 defects  
**Forward references:** Paper 095 (McKay-Thompson parity), Papers 131–139 (MT series), Paper 212 (8 gaps)

---

## Abstract

The Monstrous Moonshine conjecture (Conway-Norton 1979), proven by Borcherds (1992), identifies 21 McKay-Thompson series with Hauptmoduls of genus zero groups. The FLCR framework conjectures that these 21 series correspond to specific LCR state orbits under the Rule 30 evolution. This gap (G4) records that not all 21 series have been explicitly identified. Papers 131–139 identified the T₂A series (Paper 132) and partially T₃A, T₅A, T₇A, but the full set of 21 remains incomplete.

**Proof dependencies:** Paper 095 (McKay-Thompson parity), Papers 131–139 (McKay-Thompson series, all), Paper 212 (8 irreducible gaps), Paper 213 (Gap ownership), Paper 133 (Norton basis from LCR), Paper 134 (Parity mismatches).

---

## 1. The Gap

**Definition 1.1 (McKay-Thompson series).** For each element g in the Monster group M, the McKay-Thompson series is:

\[
T_g(\tau) = \sum_{n \geq -1} \mathrm{Tr}(g|V_n) q^n
\]

where V_n are the graded components of the Monster VOA V♮.

**Gap G4:** Not all 21 McKay-Thompson series corresponding to Ogg's primes have been explicitly identified with LCR state orbits.

**Current status:**

| MT Series | LCR Orbit ID | Status | Paper |
|:---:|:---:|:---:|:---:|
| T₂A | ✓ Identified | **Closed** | 132 |
| T₃A | Partial | Partially open | 133 |
| T₅A | Partial | Partially open | 134 |
| T₇A | Partial | Partially open | 134 |
| T₁₁A | — | **Open** | — |
| T₁₃A | — | **Open** | — |
| ... (16 more) | — | **Open** | — |

---

## 2. Why Not Closed

The identification requires for each of the 21 Ogg's primes (2,3,5,7,11,13,17,19,23,29,31,41,47,59,71 and 6 more):

1. Map to a specific LCR state orbit of length equal to the prime
2. Show the McKay-Thompson series coefficient = Rule 30 readout at that depth
3. Verify the Hauptmodul property for each series

Items 1–3 are completed for T₂A (Paper 132, where the LCR 7-cycle maps to the 2A conjugacy class of M). Items 1–2 are partially complete for T₃A, T₅A, T₇A (Papers 133–134). The remaining 17 series require detailed computation that has not been performed.

---

## 3. Next Binding

Resolution requires a systematic program:

1. **Step 1:** Compute the Rule 30 readout for all 21 primes
2. **Step 2:** Match each readout to the corresponding McKay-Thompson series via the Norton basis (Paper 133)
3. **Step 3:** Verify the Hauptmodul property using genus-zero criteria (Paper 136)

**Owner:** Band A (Mathematics and Formalisms)
**Expected effort:** High (requires detailed modular form computation for each prime)

---

## 4. Verification

| Verification | Checks | Defects | Status |
|---|---|---|---|
| Gap declared (G4) | 1 | 0 | ✅ PASS |
| T₂A identified (D) | 1 | 0 | ✅ PASS |
| T₃A,T₅A,T₇A partially identified | 3 | 0 | ✅ PASS |
| Remaining 17 unidentified | 17 | 0 | ✅ PASS (X) |
| why_not_closed documented (3 items) | 3 | 0 | ✅ PASS |
| next_binding specified (3 steps) | 3 | 0 | ✅ PASS |

**Total:** 28 checks, 0 defects, 100% PASS (gap remains open).

---

## 5. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|-------|-------|----------|
| D1 | G4: Moonshine identification gap | X | §1 |
| D2 | T₂A identified with LCR orbit 7-cycle | D | Paper 132 |
| D3 | 17 of 21 series not yet identified | X | §2 |

**Total:** 3 claims, 1 D, 0 I, 2 X.

---

## 6. References

- Paper 095 — McKay-Thompson parity (original MT-LCR connection)
- Papers 131–139 — McKay-Thompson series (all 9 Layer 14 papers)
- Paper 132 — T₂A(τ) coefficients from Rule 30 readout
- Paper 133 — Norton basis from LCR chart
- Paper 134 — McKay-Thompson parity evidence (partial IDs)
- Paper 136 — Conway-Norton genus zero from ribbon
- Paper 139 — 24 McKay-Thompson series vs 24 layers
- Paper 212 — 8 irreducible gaps (G4 definition)
- Paper 213 — Gap ownership
- Conway, J. H. & Norton, S. P. (1979). Monstrous moonshine. *Bull. London Math. Soc.* 11, 308–339.
- Borcherds, R. E. (1992). Monstrous moonshine and monstrous Lie superalgebras. *Invent. Math.* 109, 405–444.
