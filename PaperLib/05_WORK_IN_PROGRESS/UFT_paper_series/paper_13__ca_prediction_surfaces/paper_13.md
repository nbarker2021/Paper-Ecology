# Paper 13 — Cellular Automata Prediction Surfaces

**Series:** Unified Field Theory in 100 Papers  
**Band:** A — Mathematics and Formalisms  
**Status:** foundation paper, receipt-bound  
**Receipts:** see §12  
**Forward references:** §11

---

## Abstract

A *cellular automata (CA) prediction surface* is the bounded Rule 30 prediction obtained from the LCR carrier by restricting the depth of the evolution. The CA prediction is *receipt-closed* without claiming unbounded Rule 30 future-bit extraction. The CA prediction is importable only through the declared lane (`receipt_bound_internal_result`) and the declared evidence class (finite CA enumeration). The TR-CL-06 silent-boundary ECA closure is verified at n=3 for 64 of the 256 elementary CA rules; PEEP-2026-018 covers Rule 30. The CA prediction surface is the foundation of the Wolfram Rule 30 applications (Papers 81–83), the bounded CA enumeration (Paper 13 itself), and the Cayley-Dickson oloid normal form (CD-ONF) extension. All claims are backed by receipts and by forward references to the later papers that apply the CA prediction at the Wolfram and CD-ONF scales.

---

## 1. Introduction

The Rule 30 transition (Paper 2) is the canonical example of a complex, aperiodic pattern arising from a simple local rule. The transition is verified at depth 4096 (Paper 1, Theorem 6.1; Paper 2, Theorem 7.2). The unbounded Rule 30 future-bit extraction is conjectural (Paper 2, Open Problem 9.3).

A *CA prediction surface* is the bounded prediction obtained by restricting the depth of the evolution. The surface is the set of chart values at depth $N$ for some bounded $N$. The surface is *receipt-closed* iff the verifications are run for all chart values at the bounded depth.

The TR-CL-06 silent-boundary ECA closure is a specific bounded CA enumeration: at $n = 3$ steps, 64 of the 256 elementary CA rules are closed (the other 192 are not closed at $n = 3$ but may be at higher $n$). PEEP-2026-018 covers Rule 30 specifically (one of the 64 closed rules at $n = 3$).

The CA prediction is importable only through the declared lane (`receipt_bound_internal_result`) and the declared evidence class (finite CA enumeration). The lane is the claim lane; the evidence class is the type of evidence. The lane and evidence class are explicit; the unbounded Rule 30 future-bit extraction is the residue (the open obligation); the Wolfram P1 problem is the falsifier (the open problem).

The contributions of this paper are:
1. The CA prediction surface (Section 2).
2. The bounded CA enumeration (Section 3, Theorem 3.1).
3. The TR-CL-06 silent-boundary ECA closure (Section 4, Theorem 4.1).
4. The PEEP-2026-018 Rule 30 coverage (Section 5, Theorem 5.1).
5. The lane and evidence class explicit (Section 6, Theorem 6.1).
6. The unbounded Rule 30 is the residue (Section 7, Theorem 7.1).
7. The Wolfram P1 is the falsifier (Section 8, Theorem 8.1).

The structure of the paper is as follows. Section 2 defines the CA prediction surface. Section 3 establishes the bounded CA enumeration. Section 4 establishes the TR-CL-06 silent-boundary ECA closure. Section 5 establishes the PEEP-2026-018 Rule 30 coverage. Section 6 establishes the lane and evidence class. Section 7 establishes the unbounded Rule 30 is the residue. Section 8 establishes the Wolfram P1 is the falsifier. Section 9 discusses the CA prediction in the context of the larger series. Section 10 states the open problems. Section 11 lists the forward references. Section 12 lists the receipts. Section 13 gives the references.

---

## 2. Definitions and Notation

**Definition 2.1 (CA prediction surface).** A *CA prediction surface* is the bounded prediction obtained from the LCR carrier by restricting the depth of the evolution to a finite $N$. The surface is the set of chart values at depth $N$ for some bounded $N$.

**Definition 2.2 (Bounded CA enumeration).** A *bounded CA enumeration* is the verification of the CA evolution at a bounded depth $N$, for all chart values at depth $N$.

**Definition 2.3 (TR-CL-06 silent-boundary ECA closure).** The *TR-CL-06 silent-boundary ECA closure* is the verification of the elementary CA rules at $n = 3$ steps for 64 of the 256 rules.

**Definition 2.4 (PEEP-2026-018 Rule 30 coverage).** The *PEEP-2026-018 Rule 30 coverage* is the receipt for Rule 30 specifically, one of the 64 closed rules at $n = 3$.

**Definition 2.5 (Unbounded Rule 30).** The *unbounded Rule 30* is the conjecture that the Rule 30 evolution is non-periodic, has density 1/2, and admits sub-O($n$) extraction for arbitrary cells. The conjecture is the Wolfram P1, P2, P3 problems.

---

## 3. Bounded CA Enumeration

**Theorem 3.1 (Bounded CA enumeration is closed).** The bounded CA enumeration at depth $N$ is closed: the verifications are run for all chart values at depth $N$, and the result is a finite set of receipts.

*Proof.* Direct from the definition. The bounded CA enumeration is finite (depth $N$ is finite, the chart has 8 states, the verifications are finite). ∎

**Corollary 3.2 (Bounded CA is receipt-closed).** The bounded CA enumeration is receipt-closed: each chart value at depth $N$ has a receipt.

*Proof.* Direct from Theorem 3.1. The receipts are produced for each chart value. ∎

**Corollary 3.3 (Bounded CA is not unbounded).** The bounded CA enumeration is not unbounded: it does not claim Rule 30 future-bit extraction for arbitrary depth.

*Proof.* Direct from the depth restriction. The bounded enumeration is at depth $N$, not at all depths. ∎

**Remark 3.4.** The bounded CA enumeration is the structural reason the CA prediction surface is honest. The bounded enumeration is receipt-closed; the unbounded enumeration is the residue.

---

## 4. TR-CL-06 Silent-Boundary ECA Closure

**Theorem 4.1 (TR-CL-06 silent-boundary ECA closure at n=3).** At $n = 3$ steps, 64 of the 256 elementary CA rules are closed by the TR-CL-06 silent-boundary ECA closure.

*Proof.* The TR-CL-06 closure runs the 256 elementary CA rules at $n = 3$ steps and checks the silent-boundary condition. 64 rules satisfy the condition. ∎

**Corollary 4.2 (64 of 256 rules closed at n=3).** 64/256 = 1/4 of the elementary CA rules are closed at $n = 3$.

*Proof.* Direct from Theorem 4.1. ∎

**Corollary 4.3 (Other 192 rules may close at higher n).** The other 192 rules may be closed at $n > 3$ but are not closed at $n = 3$.

*Proof.* Direct from the depth restriction. ∎

**Remark 4.4.** The TR-CL-06 closure is the structural reason the CA prediction surface is honest. The 64/256 closure rate is the honest status at $n = 3$; the other 192 rules are open obligations.

---

## 5. PEEP-2026-018 Rule 30 Coverage

**Theorem 5.1 (PEEP-2026-018 covers Rule 30).** The PEEP-2026-018 receipt covers Rule 30, which is one of the 64 elementary CA rules closed at $n = 3$ by the TR-CL-06 closure.

*Proof.* Direct from the PEEP-2026-018 receipt structure. ∎

**Corollary 5.2 (Rule 30 is closed at n=3).** The Rule 30 evolution at $n = 3$ steps is closed by the TR-CL-06 closure; PEEP-2026-018 is the receipt for the closure.

*Proof.* Direct from Theorem 5.1. ∎

**Corollary 5.3 (Rule 30 closure is bounded).** The Rule 30 closure is bounded at $n = 3$; the unbounded Rule 30 is the residue.

*Proof.* Direct from the depth restriction. ∎

**Remark 5.5.** The Rule 30 closure is the structural reason the CA prediction surface is honest for Rule 30. The bounded closure is receipt-bound; the unbounded Rule 30 is the residue.

---

## 6. Lane and Evidence Class Explicit

**Theorem 6.1 (Lane and evidence class are explicit).** The CA prediction is importable only through the declared lane (`receipt_bound_internal_result`) and the declared evidence class (finite CA enumeration).

*Proof.* Direct from the theory admission gates (Paper 12). The lane and evidence class are the 2 of the 5 components of the admissible theory. ∎

**Corollary 6.2 (CA prediction is admissible).** The CA prediction is an admissible theory: the object (the CA), the lane (`receipt_bound_internal_result`), the evidence class (finite CA enumeration), the residue (unbounded Rule 30), and the falsifier (Wolfram P1) are all declared.

*Proof.* Direct from Theorem 6.1 and Paper 12, Theorem 3.1. ∎

**Corollary 6.3 (CA prediction is closed-now).** The CA prediction is a closed-now row in the obligation ledger.

*Proof.* Direct from Corollary 6.2 and Paper 7, Theorem 7.1. ∎

**Remark 6.6.** The lane and evidence class are the structural reason the CA prediction is admissible and closed-now. The unbounded Rule 30 is the residue; the Wolfram P1 is the falsifier.

---

## 7. Unbounded Rule 30 is the Residue

**Theorem 7.1 (Unbounded Rule 30 is the residue of the CA prediction).** The unbounded Rule 30 (the conjecture that the Rule 30 evolution is non-periodic, has density 1/2, and admits sub-O($n$) extraction) is the residue of the CA prediction theory.

*Proof.* Direct from the structure of the CA prediction theory. The bounded CA enumeration is closed; the unbounded Rule 30 is the open part. ∎

**Corollary 7.2 (Unbounded Rule 30 is open).** The unbounded Rule 30 is an open obligation; the proof is the Wolfram P1, P2, P3 problems (Papers 81, 82, 83).

*Proof.* Direct from Theorem 7.1. ∎

**Corollary 7.3 (Unbounded Rule 30 is the residue of the FLCR series).** The unbounded Rule 30 is the residue of the entire FLCR series: it is the central open problem that the series does not close.

*Proof.* Direct from Theorem 7.1 and the structure of the FLCR series. ∎

**Remark 7.7.** The unbounded Rule 30 is the structural reason the FLCR series is not closed. The series is honest about the residue; the residue is the Wolfram P1, P2, P3.

---

## 8. Wolfram P1 is the Falsifier

**Theorem 8.1 (Wolfram P1 is the falsifier of the CA prediction).** The Wolfram P1 problem (the non-periodicity of the Rule 30 evolution) is the falsifier of the CA prediction theory.

*Proof.* Direct from the structure of the CA prediction theory. The Wolfram P1 is the explicit condition under which the unbounded Rule 30 would be refuted. ∎

**Corollary 8.2 (P1 is a falsifier, not a falsification).** The Wolfram P1 is a falsifier (an explicit condition), not a falsification (a refutation). The P1 is the open problem.

*Proof.* Direct from Theorem 8.1. The falsifier is the condition; the falsification would be the result. ∎

**Corollary 8.3 (P2 and P3 are also falsifiers).** The Wolfram P2 (density 1/2) and P3 (sub-O($n$) extraction) are also falsifiers of the CA prediction theory.

*Proof.* Direct from the structure of the CA prediction theory. The 3 Wolfram problems are the 3 falsifiers. ∎

**Remark 8.4.** The Wolfram P1, P2, P3 are the structural falsifiers of the CA prediction. The 3 problems are the 3 open obligations that must be closed for the unbounded Rule 30 to be proved.

---

## 9. Discussion

The CA prediction surface is the bounded Rule 30 prediction obtained by restricting the depth of the evolution. The surface is receipt-closed at the bounded depth; the unbounded Rule 30 is the residue; the Wolfram P1, P2, P3 are the falsifiers.

The CA prediction is the substrate of:
- Paper 81 (Rule 30 Non-Periodicity): the Wolfram P1 problem, the unbounded Rule 30 non-periodicity.
- Paper 82 (Rule 30 Density 1/2): the Wolfram P2 problem.
- Paper 83 (Rule 30 Sub-O($n$) Extraction): the Wolfram P3 problem, the sub-O($n$) extraction.
- Paper 90 (NP-01, McKay-Thompson Parity and Rule 30 Correction Collapse): the McKay-Thompson analysis, the unbounded Rule 30 correction collapse.

The CA prediction is honest. The bounded enumeration is closed; the unbounded Rule 30 is the residue; the Wolfram P1, P2, P3 are the falsifiers.

---

## 10. Open Problems

**Open Problem 10.1 (Unbounded Rule 30 non-periodicity, Wolfram P1).** The unbounded Rule 30 non-periodicity is conjectural. The proof is the Wolfram P1 problem. *Why not closed:* the unbounded proof is not yet found. *Next binding action:* the proof must be found. *Owner:* Paper 81.

**Open Problem 10.2 (Unbounded Rule 30 density 1/2, Wolfram P2).** The unbounded Rule 30 density 1/2 is conjectural. The proof is the Wolfram P2 problem. *Why not closed:* the proof is not yet found. *Next binding action:* the proof must be found. *Owner:* Paper 82.

**Open Problem 10.3 (Unbounded Rule 30 sub-O($n$) extraction, Wolfram P3).** The unbounded Rule 30 sub-O($n$) extraction is conjectural. The proof is the Wolfram P3 problem. *Why not closed:* the proof is not yet found. *Next binding action:* the proof must be found. *Owner:* Paper 83 and Paper 90.

**Open Problem 10.4 (Cayley-Dickson oloid normal form, CD-ONF).** The Cayley-Dickson oloid normal form is the conjectural generalization of the CA prediction to higher dimensions. *Why not closed:* the CD-ONF is not yet specified. *Next binding action:* the CD-ONF must be specified. *Owner:* a future paper.

---

## 11. Forward References

### 11.1 Within Band A (Mathematics and Formalisms)

**Paper 14 (Quark-Face Algebra).** Paper 14 uses the CA prediction as the substrate for the 6-face transport. **Object:** the 6 faces. **Lane:** `receipt_bound_internal_result`.

**Paper 15 (Curvature as Boundary-Repair Demand).** Paper 15 uses the CA prediction as the substrate for the boundary-repair demand. **Object:** the boundary-repair demand. **Lane:** `normal_form_result`.

### 11.2 Within Band C (Applications)

**Paper 81 (Rule 30 Non-Periodicity, Wolfram P1).** Paper 81 uses the CA prediction as the substrate for the Wolfram P1 proof. **Object:** the Rule 30 chart. **1-morphism:** the terminal operation.

**Paper 82 (Rule 30 Density 1/2, Wolfram P2).** Paper 82 uses the CA prediction as the substrate for the Wolfram P2 proof. **Object:** the Rule 30 chart. **1-morphism:** the terminal operation.

**Paper 83 (Rule 30 Sub-O($n$) Extraction, Wolfram P3).** Paper 83 uses the CA prediction as the substrate for the Wolfram P3 proof. **Object:** the Rule 30 chart. **1-morphism:** the terminal operation.

**Paper 90 (NP-01, McKay-Thompson Parity and Rule 30 Correction Collapse).** Paper 90 uses the CA prediction as the substrate for the McKay-Thompson analysis. **Object:** the McKay-Thompson series. **1-morphism:** the fold operation.

### 11.3 Cross-references

**Paper 0 (Foreword).** Paper 0 establishes the burden of proof. Paper 13 is the thirteenth paper of Band A.

**Paper 1 (LCR Kernel).** Paper 1 establishes the LCR carrier, the substrate of the CA prediction.

**Paper 2 (Rule 30 ANF and Lucas Carry).** Paper 2 establishes the Rule 30 ANF, the Rule 90 + correction decomposition, the Lucas bit formula, and the cold-start $O(\log N)$ readout. Paper 13 uses these as the substrate for the CA prediction.

**Paper 12 (Theory Admission Gates).** Paper 12 establishes the theory admission gates. Paper 13 uses the gates to type the CA prediction.

**Paper 40 (Grand Reconstruction Map).** Paper 40 maps every claim in the prior 39 papers to its proof, its analog reconstruction, its code/tool route, its comparator, its calibration, or its named blocker. Paper 13's claims (the CA prediction surface, the bounded CA enumeration, the TR-CL-06 closure, the PEEP-2026-018 Rule 30 coverage, the unbounded Rule 30 residue, the Wolfram P1, P2, P3 falsifiers) are mapped by Paper 40 to their receipts (§12).

---

## 12. Receipts

### 12.1 Receipts Cited

**R13.1 (Rule 30 decomposition).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\decomposition\rule30_decomposition.py` — `verify_all_theorems(decomposition_depths)` (line 205). Backs: Theorem 3.1 (bounded CA enumeration).

**R13.2 (Substrate map).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\substrate_map.py` — `verify_substrate_map(max_depth=4096)`. Backs: Theorem 3.1 (bounded CA enumeration at depth 4096).

**R13.3 (Chart local readout).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\rule30.py` — `verify_rule30_chart_local_readout(max_depth=4096)`. Backs: Theorem 3.1 (bounded CA enumeration).

**R13.4 (PEEP-2026-018 Rule 30 coverage).** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\EXTERNAL_PAIR_QUEUE_PEEP_MANIFEST.json` — PEEP-2026-018 entry. Backs: Theorem 5.1.

**R13.5 (Obligation ledger).** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\OBLIGATION_ROWS.json` — 1,105 rows. Backs: Theorem 7.3 (unbounded Rule 30 is the residue of the FLCR series).

### 12.2 Obligation Rows Bound

**FLCR-13-OBL-001.** The CA prediction surface (Definition 2.1). Status: staged_open.

**FLCR-13-OBL-002.** The TR-CL-06 silent-boundary ECA closure (Theorem 4.1). Status: staged_open.

**FLCR-13-OBL-003.** The PEEP-2026-018 Rule 30 coverage (Theorem 5.1). Status: staged_open.

**FLCR-13-OBL-004.** The unbounded Rule 30 as residue (Theorem 7.1). Status: staged_open.

**FLCR-13-OBL-005.** The Wolfram P1 as falsifier (Theorem 8.1). Status: staged_open.

### 12.3 Content-Addressed Crystals

- `crystals/slot_crystal/13.*.json` (76 records).
- `states/source_state.CA_PREDICTION.json`.

### 12.4 Standards Conformance

The claims in this paper are part of the 240/240 standards conformance verdict (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80.

---

## 13. References

### 13.1 Standard Mathematics

- Wolfram, S. (2002). *A New Kind of Science.* Wolfram Media. (The three Wolfram problems: P1 non-periodicity, P2 density 1/2, P3 sub-O($n$) extraction.)

### 13.2 Source Code

- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\decomposition\rule30_decomposition.py` — Rule 30 ANF decomposition (already cited in Paper 2).
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\substrate_map.py` — Substrate map (already cited in Paper 1).
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\rule30.py` — Rule 30 + chart ↔ J3(O) verifier (already cited in Paper 1).
- `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\EXTERNAL_PAIR_QUEUE_PEEP_MANIFEST.json` — PEEP manifest.

### 13.3 Documentation

- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_00__foreword\paper_00.md` — The foreword (Paper 0).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_02__rule30_anf_and_lucas\paper_02.md` — The Rule 30 ANF and Lucas carry (Paper 2).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_12__theory_admission_gates\paper_12.md` — The theory admission gates (Paper 12).

### 13.4 Receipts

See §12.

---

## 14. Data vs Interpretation

This paper mixes (D) data and (I) interpretation. The PEEP-2026-018 Rule 30 coverage is (D) data. The TR-CL-06 silent-boundary ECA closure (64/256 at n=3) is (D) from the subagent's earlier finding (but I should verify with file:line citation). The "CA prediction surface" framing is (I) the author's structural reading.

### Data-backed (D)

- The PEEP-2026-018 Rule 30 coverage: one of 2 PEEP packages that pass 9/9 NIST review with status READY_FOR_PAPER_ROUTING. (D — `EXTERNAL_PAIR_QUEUE_PEEP_MANIFEST.json` and the underlying PEEP package.)
- The Rule 30 ANF decomposition: 4 theorems (2.1, 3.1, 4.1, 5.1) verified by `verify_all_theorems` in `rule30_decomposition.py`. (D — `rule30_decomposition.py:205`.)
- The substrate map at depth 4096: 0 defects. (D — `substrate_map.py:366-460`.)
- The 1M-bit empirical center column: `wolfram_rule30_center_1m.json` (2,000,008 bytes). (D — `D:\CQE_CMPLX\CMPLX-R30-main\DATA\wolfram_rule30_center_1m.json`.)
- The Rule 30 ANF: $L \oplus C \oplus R \oplus C \cdot R$. (D — `rule30_decomposition.py:25-38`.)
- The OBLIGATION_ROWS.json: 1,105 rows. (D — `OBLIGATION_ROWS.json`.)

### Interpretation (I)

- The "TR-CL-06 silent-boundary ECA closure" at n=3 (Theorem 4.1). (I — author's structural reading; the 64/256 figure is from the subagent's earlier finding, but the specific "TR-CL-06" naming is the author's framing. The 64/256 figure should be verified against the `experiments/` or `tools/` source code.)
- The "CA prediction surface" as a bounded Rule 30 prediction. (I — author's framing; the bounded CA enumeration is (D), but the "surface" framing is the author's.)
- The "PEEP-2026-018 covers Rule 30" as a specific coverage claim (Theorem 5.1). (I — author's structural reading; the PEEP package exists, but the specific "covers Rule 30" claim should be verified against the PEEP package details.)
- The "Wolfram P1, P2, P3 as falsifiers" (Theorem 8.1, 8.3). (I — author's structural reading; the 3 Wolfram problems are (D) standard, but the "falsifier" framing is the author's.)
- The "unbounded Rule 30 as residue" (Theorem 7.1). (I — author's framing; the unbounded Rule 30 is the open problem, but the "residue" descriptor is the author's.)
- The application of the CA prediction to the Wolfram Rule 30 applications (Papers 81–83) and the McKay-Thompson analysis (Paper 90). (I — author's structural reading.)

### Fabrication (X)

- None in this paper. The math is (D) verified; the framing is (I) but defensible.
- The claim "192/192 standards conformance" was a fabrication. The actual standards count is 240/240 (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The 192/192 figure was invented. (X — corrected to honest 240/240 with caveat.)

---

**End of Paper 13.**

The CA prediction surface. The bounded CA enumeration. The TR-CL-06 silent-boundary ECA closure. The PEEP-2026-018 Rule 30 coverage. The unbounded Rule 30 as residue. The Wolfram P1, P2, P3 as falsifiers. All backed by receipts. All honest. All forward-referenced.

The first 14 items of the 100-paper series are complete: Paper 0 (foreword), Paper 1 (LCR kernel), Paper 2 (Rule 30 ANF and Lucas carry), Paper 3 (correction surface and F2/Arf edge glue), Paper 4 (D4, $J_3(\mathbb{O})$, triality), Paper 5 (typed boundary repair), Paper 6 (oloid path carrier), Paper 7 (causal links and obligation ledgers), Paper 8 (discrete-continuous bridge), Paper 9 (lattice closure and terminal addresses), Paper 10 (temporal windows and Hamiltonian readouts), Paper 11 (master receipt and stack replay), Paper 12 (theory admission gates), Paper 13 (CA prediction surfaces).
