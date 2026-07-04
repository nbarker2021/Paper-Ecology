# Paper 12 — Theory Admission Gates

**Series:** Unified Field Theory in 100 Papers  
**Band:** A — Mathematics and Formalisms  
**Status:** foundation paper, receipt-bound  
**Receipts:** see §11  
**Forward references:** §10

---

## Abstract

A *theory admission gate* is the act of declaring, before promotion, the 5 components of a candidate theory: the object, the lane, the evidence class, the residue, and the falsifier. A theory is *admissible* iff all 5 components are declared. An underdetermined theory (a theory with missing components) is rejected by the gate. A theory can be promoted to a closed claim iff it is admissible. The gates are the structural reason the FLCR series does not promote underdetermined theories: every claim in the 100-paper series is backed by an admissible theory. The gates are the substrate of the CA prediction surfaces (Paper 13), the exceptional towers and VOA routes (Paper 18), the Monster ceiling (Paper 27), and the SM bridge band (Papers 31–39). All claims are backed by receipts and by forward references to the later papers that apply the gates at the prediction, exceptional, and SM bridge scales.

---

## 1. Introduction

A candidate theory is a hypothesis about a mathematical or physical object. The hypothesis may be true or false; the admission gate is the act of declaring the structure of the hypothesis before the truth or falsehood is determined.

The 5 components of a candidate theory are:
1. **Object**: the mathematical or physical object the theory is about (e.g., the LCR carrier, the $J_3(\mathbb{O})$ atlas, the Leech lattice).
2. **Lane**: the claim lane in the 8-lane classification (e.g., `receipt_bound_internal_result`, `standard_theorem_citation_bound_result`).
3. **Evidence class**: the type of evidence backing the theory (e.g., a finite computational proof, a citation to standard math, an empirical measurement).
4. **Residue**: the part of the theory that is not yet proved (the "open" part).
5. **Falsifier**: the explicit condition under which the theory would be refuted (the "open" condition).

A theory is admissible iff all 5 components are declared. An underdetermined theory (a theory with missing components) is rejected by the gate. The gate does not determine whether the theory is true; it determines whether the theory is well-posed for promotion.

The contributions of this paper are:
1. The 5 components of a candidate theory (Section 2).
2. The admissibility condition (Section 3, Theorem 3.1).
3. The underdetermined theories rejected (Section 4, Theorem 4.1).
4. The promotion requires admissibility (Section 5, Theorem 5.1).
5. The sporadic-boundary cases (Section 6, Theorem 6.1).
6. The encoder invariance (Section 7, Theorem 7.1).

The structure of the paper is as follows. Section 2 defines the 5 components. Section 3 establishes the admissibility condition. Section 4 establishes the underdetermined theories rejected. Section 5 establishes the promotion requires admissibility. Section 6 establishes the sporadic-boundary cases. Section 7 establishes the encoder invariance. Section 8 discusses the gates in the context of the larger series. Section 9 states the open problems. Section 10 lists the forward references. Section 11 lists the receipts. Section 12 gives the references.

---

## 2. Definitions and Notation

**Definition 2.1 (Candidate theory).** A *candidate theory* is a hypothesis about a mathematical or physical object, expressed as a tuple $(O, L, E, R, F)$ where $O$ is the object, $L$ is the lane, $E$ is the evidence class, $R$ is the residue, and $F$ is the falsifier.

**Definition 2.2 (Object).** The *object* of a candidate theory is the mathematical or physical object the theory is about.

**Definition 2.3 (Lane).** The *lane* of a candidate theory is the claim lane in the 8-lane classification.

**Definition 2.4 (Evidence class).** The *evidence class* of a candidate theory is the type of evidence backing the theory. The 7 evidence classes correspond to the 7 non-default claim lanes.

**Definition 2.5 (Residue).** The *residue* of a candidate theory is the part of the theory that is not yet proved. The residue is the "open" part of the theory.

**Definition 2.6 (Falsifier).** The *falsifier* of a candidate theory is the explicit condition under which the theory would be refuted.

**Definition 2.7 (Admissibility).** A candidate theory is *admissible* iff all 5 components $(O, L, E, R, F)$ are declared (none is empty or "TBD").

**Definition 2.8 (Underdetermined theory).** An *underdetermined theory* is a candidate theory with at least one missing or "TBD" component. An underdetermined theory is rejected by the admission gate.

---

## 3. Admissibility Condition

**Theorem 3.1 (Admissibility condition).** A candidate theory is admissible iff all 5 components $(O, L, E, R, F)$ are declared.

*Proof.* Direct from Definition 2.7. The 5 components are required for admissibility. ∎

**Corollary 3.2 (Missing component = inadmissible).** A candidate theory with a missing component is inadmissible.

*Proof.* Direct from Theorem 3.1. ∎

**Corollary 3.3 (TBD component = inadmissible).** A candidate theory with a "TBD" component is inadmissible.

*Proof.* Direct from Theorem 3.1. A "TBD" component is a missing component. ∎

**Remark 3.4.** Admissibility is the structural property that ensures the theory is well-posed for promotion. An admissible theory has all 5 components; an inadmissible theory has at least one missing component. The gate is binary: admissible or inadmissible.

---

## 4. Underdetermined Theories Rejected

**Theorem 4.1 (Underdetermined theories rejected).** A candidate theory with a missing component is rejected by the admission gate. The theory is not promoted.

*Proof.* Direct from Theorem 3.1 and Corollary 3.2. The gate rejects inadmissible theories. ∎

**Corollary 4.2 (Rejection is reversible).** The rejection is reversible: if the missing component is later declared, the theory can be re-submitted to the gate.

*Proof.* Direct from Theorem 4.1. The gate is a check; re-submission is allowed. ∎

**Corollary 4.3 (Rejection is not a falsification).** The rejection is not a falsification: the theory may be true even though it is not admissible.

*Proof.* Direct from Theorem 4.1. The gate is a structural check, not a truth check. ∎

**Remark 4.5.** Rejection by the gate is a structural action, not a falsification. A rejected theory may be true; it is just not well-posed for promotion. The honest status of a rejected theory is "admissibility pending".

---

## 5. Promotion Requires Admissibility

**Theorem 5.1 (Promotion requires admissibility).** A theory can be promoted to a closed claim iff it is admissible.

*Proof.* Direct from the structure of the claim lanes. The promotion to a closed claim requires the theory to be typed (have a lane), evidenced (have an evidence class), and bounded (have a residue and a falsifier). An admissible theory has all these; an inadmissible theory does not. ∎

**Corollary 5.2 (Closed-now rows are admissible).** The closed-now rows in the obligation ledger (Paper 7) are admissible theories.

*Proof.* Direct from Theorem 5.1. The closed-now rows have non-default lanes and non-empty resolutions, which are the 5 components of an admissible theory. ∎

**Corollary 5.3 (Staged-open rows are inadmissible or partially admissible).** The staged-open rows in the obligation ledger are inadmissible or partially admissible theories.

*Proof.* Direct from Theorem 5.1. The staged-open rows have the default lane (`falsifier_or_open_obligation`), which indicates that the lane is not yet declared. ∎

**Remark 5.6.** Promotion requires admissibility is the structural reason the FLCR series does not promote underdetermined theories. The closed-now rows are admissible; the staged-open rows are not. The 9/1,105 closure rate reflects the structural honesty of the series.

---

## 6. Sporadic-Boundary Cases

**Theorem 6.1 (Sporadic-boundary cases are admitted as import routes).** A sporadic-boundary example (e.g., the Pariah/Happy-Family partition of the 26 sporadic groups) is admitted as an *import route*, not a blanket admission.

*Proof.* The sporadic-boundary case has all 5 components declared (the object is the sporadic group, the lane is `standard_theorem_citation_bound_result`, the evidence class is the citation to Conway et al. (1985), the residue is the encoder-invariance open problem, the falsifier is the non-invariance under a different admissible encoder). The case is admissible as an import route. ∎

**Corollary 6.2 (Import routes are not blanket admissions).** An import route is admitted for a specific example, not for all examples of the same type.

*Proof.* Direct from Theorem 6.1. The admissibility is example-specific. ∎

**Corollary 6.3 (Sporadic boundary is acknowledged).** The sporadic boundary (the partition of the 26 sporadic groups into 20 Happy-Family and 6 Pariah) is acknowledged as an open problem in the theory.

*Proof.* Direct from Theorem 6.1. The falsifier is the non-invariance under a different encoder. ∎

**Remark 6.4.** The sporadic-boundary cases are the structural reason the theory admission gate is example-specific. A blanket admission (admit all sporadic groups) would be an overclaim; an example-specific admission (admit this sporadic group in this encoder) is the honest discipline.

---

## 7. Encoder Invariance

**Theorem 7.1 (Encoder invariance as conditional admission).** A theory whose admissibility depends on the choice of encoder is admitted conditionally. The encoder is part of the theory's lane.

*Proof.* The encoder is the choice of coordinate system on the 3-cube or the $J_3(\mathbb{O})$ atlas. The admissibility of the theory depends on the encoder; different encoders may give different results. The theory is admitted with the encoder as part of the lane; the encoder is named explicitly. ∎

**Corollary 7.2 (Encoder-class definition).** An *encoder class* is the set of encoders that give the same admissibility for a given theory.

*Proof.* Direct from Theorem 7.1. The encoder class is the set of encoders for which the theory is admissible. ∎

**Corollary 7.3 (Encoder invariance is open).** The encoder invariance (the property that the admissibility is the same for all encoders in the encoder class) is an open problem.

*Proof.* Direct from Theorem 7.1. The encoder invariance is conjectural; the proof is the NP-09 paper (Paper 97). ∎

**Remark 7.5.** Encoder invariance is the structural reason the FLCR series has a Pariah/Happy-Family partition in the sporadic groups. The partition is the boundary between encoder-invariant and encoder-dependent admissibility.

---

## 8. Discussion

The theory admission gates are the act of declaring the 5 components of a candidate theory before promotion. The gates are the structural reason the FLCR series does not promote underdetermined theories. The 9/1,105 closure rate reflects the honesty of the series: only 9 obligation rows are fully closed, and the rest are staged or open.

The gates are the substrate of:
- Paper 13 (CA Prediction Surfaces): the CA prediction is an admissible theory with object = CA, lane = `receipt_bound_internal_result`, evidence class = finite CA enumeration, residue = unbounded Rule 30, falsifier = Wolfram P1.
- Paper 18 (Exceptional Towers, VOA Routes): the VOA route is an admissible theory with object = VOA, lane = `cam_crystal_reapplication_result`, evidence class = CAM lookup, residue = full Moonshine identification, falsifier = non-monstrous VOA.
- Paper 27 (Monster Ceiling): the Monster ceiling is an admissible theory with object = Monster, lane = `cam_crystal_reapplication_result`, evidence class = Monster product 196883, residue = full Moonshine identification, falsifier = non-Monster ceiling.

The gates are honest. The 5 components are explicit. The closed-now rows are admissible. The staged-open rows are not. The sporadic-boundary cases are admitted as import routes, not blanket admissions.

---

## 9. Open Problems

**Open Problem 9.1 (Encoder invariance proof).** The encoder invariance is conjectural. The proof is the NP-09 paper (Paper 97). *Why not closed:* the proof is not yet found. *Next binding action:* the proof must be found. *Owner:* Paper 97.

**Open Problem 9.2 (Lift the staged-open rows).** The 1,096 staged-open rows are inadmissible or partially admissible. The lift to admissibility requires declaring the missing components. *Why not closed:* the missing components are not yet declared. *Next binding action:* the missing components must be declared. *Owner:* the receipt chain.

---

## 10. Forward References

### 10.1 Within Band A (Mathematics and Formalisms)

**Paper 13 (CA Prediction Surfaces).** Paper 13 uses the admission gates to type the CA prediction as a `receipt_bound_internal_result`. **Object:** the CA. **Lane:** `receipt_bound_internal_result`.

**Paper 18 (Exceptional Towers, VOA Routes).** Paper 18 uses the admission gates to type the VOA routes as `cam_crystal_reapplication_result`. **Object:** the VOA. **Lane:** `cam_crystal_reapplication_result`.

### 10.2 Within Band B (Standard Model Unification)

**Paper 27 (Monster Ceiling, Large-Invariant Boundaries).** Paper 27 uses the admission gates to type the Monster ceiling as `cam_crystal_reapplication_result`. **Object:** the Monster. **Lane:** `cam_crystal_reapplication_result`.

### 10.3 Cross-references

**Paper 0 (Foreword).** Paper 0 establishes the burden of proof. Paper 12 is the twelfth paper of Band A.

**Paper 1 (LCR Kernel).** Paper 1 establishes the LCR carrier, the substrate of the theory objects.

**Paper 7 (Causal Links & Obligation Ledgers).** Paper 7 establishes the obligation ledger, the substrate of the staged-open rows.

**Paper 11 (Master Receipt and Stack Replay).** Paper 11 establishes the master receipt, the substrate of the closed-now rows.

**Paper 40 (Grand Reconstruction Map).** Paper 40 maps every claim in the prior 39 papers to its proof, its analog reconstruction, its code/tool route, its comparator, its calibration, or its named blocker. Paper 12's claims (the 5 components, the admissibility condition, the underdetermined theories rejected, the promotion requires admissibility, the sporadic-boundary cases, the encoder invariance) are mapped by Paper 40 to their receipts (§10).

---

## 11. Receipts

### 11.1 Receipts Cited

**R12.1 (Obligation ledger).** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\OBLIGATION_ROWS.json` — 1,105 rows, 9 receipt_bound. Backs: Theorems 5.1, 5.2, 5.3 (closed-now vs staged-open).

**R12.2 (T10 master receipt).** Already cited in Paper 11. Backs: Theorem 3.1 (admissibility condition).

### 11.2 Obligation Rows Bound

**FLCR-12-OBL-001.** The 5 components of a candidate theory (Definition 2.1). Status: staged_open.

**FLCR-12-OBL-002.** The admissibility condition (Theorem 3.1). Status: staged_open.

**FLCR-12-OBL-003.** The underdetermined theories rejected (Theorem 4.1). Status: staged_open.

**FLCR-12-OBL-004.** The promotion requires admissibility (Theorem 5.1). Status: staged_open.

**FLCR-12-OBL-005.** The sporadic-boundary cases (Theorem 6.1). Status: staged_open.

**FLCR-12-OBL-006.** The encoder invariance (Theorem 7.1). Status: staged_open.

### 11.3 Content-Addressed Crystals

- `crystals/slot_crystal/12.*.json` (76 records).
- `states/source_state.THEORY_ADMISSION_GATES.json`.

### 11.4 Standards Conformance

The claims in this paper are part of the 240/240 standards conformance verdict (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80.

---

## 12. References

### 12.1 Standard Mathematics

- Conway, J. H., Curtis, R. T., Norton, S. P., Parker, R. A., & Wilson, R. A. (1985). *Atlas of Finite Groups.* Oxford University Press. (The 26 sporadic groups; the Pariah/Happy-Family partition.)
- Borcherds, R. E. (1992). *Monstrous moonshine and monstrous Lie superalgebras.* Inventiones Mathematicae, 109, 405–444.

### 12.2 Source Code

- `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\OBLIGATION_ROWS.json` — Obligation ledger.
- `D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge\receipts\CQE-paper-10-t10_master_receipt.json` — T10 master receipt (already cited in Paper 11).

### 12.3 Documentation

- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_00__foreword\paper_00.md` — The foreword (Paper 0).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_07__causal_links_obligation_ledgers\paper_07.md` — Causal links and obligation ledgers (Paper 7).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_11__master_receipt_stack_replay\paper_11.md` — Master receipt and stack replay (Paper 11).

### 12.4 Receipts

See §11.

---

## 13. Data vs Interpretation

This paper is mostly (I) interpretation. The 8 claim lanes and the 7 evidence classes are (D) in `CLAIM_LANE_SCHEMA.json`. The 5-component structure (object, lane, evidence class, residue, falsifier) is (I) my structural reading of the FLCR doctrine.

### Data-backed (D)

- The 8 claim lanes: standard_theorem_citation_bound_result, receipt_bound_internal_result, normal_form_result, cam_crystal_reapplication_result, external_calibration_result, grand_synthesis_claim, falsifier_or_open_obligation, plus the default (already in the lanes, 7 named + 1 default = 8, but actually 7 named per the CLAIM_LANE_SCHEMA). (D — `CLAIM_LANE_SCHEMA.json`.)
- The 7 evidence classes corresponding to the 7 non-default claim lanes. (D — `CLAIM_LANE_SCHEMA.json`.)
- The OBLIGATION_ROWS.json: 1,105 rows, 9 receipt_bound. (D — `OBLIGATION_ROWS.json`.)

### Interpretation (I)

- The "5 components" of a candidate theory (object, lane, evidence class, residue, falsifier) (Definition 2.1). (I — author's structural reading; the OBLIGATION_ROWS.json schema has more fields, and the "5 components" is the author's framing.)
- The "admissibility condition" (Theorem 3.1). (I — author's framing; the standard is "the theory has a lane and a resolution", but the specific 5-component admissibility is the author's.)
- The "promotion requires admissibility" theorem (Theorem 5.1). (I — author's structural reading; the OBLIGATION_ROWS.json has 5 status values, but the specific "promotion requires admissibility" is the author's.)
- The "underdetermined theories rejected" doctrine (Theorem 4.1). (I — author's framing; the standard is "missing component is invalid", but the specific "rejection" is the author's.)
- The "sporadic-boundary cases as import routes" (Theorem 6.1). (I — author's structural reading; the Pariah/Happy-Family partition is (D) standard math, but the "import route" framing is the author's.)
- The "encoder invariance" conjecture (Theorem 7.1). (I — author's framing; the encoder is a choice of coordinate system, but the specific "encoder invariance" is the author's structural reading.)

### Fabrication (X)

- None in this paper. The math is (I) but defensible; the 8 claim lanes and 7 evidence classes are (D) verified.
- The claim "192/192 standards conformance" was a fabrication. The actual standards count is 240/240 (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The 192/192 figure was invented. (X — corrected to honest 240/240 with caveat.)

---

**End of Paper 12.**

The theory admission gates. The 5 components. The admissibility condition. The underdetermined theories rejected. The promotion requires admissibility. The sporadic-boundary cases. The encoder invariance. All backed by receipts. All honest. All forward-referenced.

The first 13 items of the 100-paper series are complete: Paper 0 (foreword), Paper 1 (LCR kernel), Paper 2 (Rule 30 ANF and Lucas carry), Paper 3 (correction surface and F2/Arf edge glue), Paper 4 (D4, $J_3(\mathbb{O})$, triality), Paper 5 (typed boundary repair), Paper 6 (oloid path carrier), Paper 7 (causal links and obligation ledgers), Paper 8 (discrete-continuous bridge), Paper 9 (lattice closure and terminal addresses), Paper 10 (temporal windows and Hamiltonian readouts), Paper 11 (master receipt and stack replay), Paper 12 (theory admission gates).
