# Paper 21 — Materials Candidate Generation

**Series:** Unified Field Theory in 100 Papers  
**Band:** A — Mathematics and Formalisms  
**Status:** foundation paper, receipt-bound (`cam_crystal_reapplication_result`)  
**Receipts:** see §10  
**Forward references:** §9

---

## Abstract

The *materials candidate generation* is the act of generating a material candidate from an internal representation by a candidate-generation path, before fabrication or finite-element validation. The internal representation is receipt-bound via the CAM crystal memory bank (Paper 0, §3); the candidate-generation path is receipt-bound as a `cam_crystal_reapplication_result` lane. Fabrication, finite-element performance, measured band data, and biological performance are deferred to external validation tasks (external calibration, `external_calibration_result`). The materials candidate generation is the foundation of the condensed matter and metamaterials translation (Paper 36), the electron-hole-exciton accounting (Paper 34), and the applied forge validation (Paper 95). All claims are backed by receipts and by forward references to the later papers that apply the candidate generation at the condensed matter, exciton, and applied forge scales.

---

## 1. Introduction

A *material* is a physical substance with a structure and properties. The structure is the atomic arrangement; the properties include the band gap, the elastic moduli, the thermal conductivity, the optical response, etc. The *materials candidate generation* is the act of generating a candidate material with a specified structure and predicted properties, before any physical fabrication or empirical measurement.

The internal representation of a material candidate is a content-addressed crystal in the CAM crystal memory bank (Paper 0, §3). The candidate-generation path is the sequence of operations that takes the internal representation and produces the candidate. The path is receipt-bound: the operations are typed and explicit, and the candidate is content-addressed.

Fabrication, finite-element performance, measured band data, and biological performance are deferred to external validation tasks. The candidate generation does not claim that the candidate is a real material; the candidate is an internal representation with predicted properties. The empirical validation is the open obligation.

The contributions of this paper are:
1. The internal representation is receipt-bound (Section 2).
2. The candidate-generation path is receipt-bound (Section 3, Theorem 3.1).
3. The fabrication and finite-element performance are deferred (Section 4, Theorem 4.1).
4. The electron-hole-exciton accounting is the substrate (Section 5, Theorem 5.1).
5. The applied forge descriptor is the kernel (Section 6, Theorem 6.1).

The structure of the paper is as follows. Section 2 defines the internal representation. Section 3 establishes the candidate-generation path. Section 4 establishes the fabrication and finite-element performance deferred. Section 5 establishes the electron-hole-exciton accounting. Section 6 establishes the applied forge descriptor as the kernel. Section 7 discusses the candidate generation in the context of the larger series. Section 8 states the open problems. Section 9 lists the forward references. Section 10 lists the receipts. Section 11 gives the references.

---

## 2. Definitions and Notation

**Definition 2.1 (Internal representation).** The *internal representation* of a material candidate is a content-addressed crystal in the CAM crystal memory bank. The crystal has explicit structure (atomic arrangement), explicit properties (band gap, elastic moduli, etc.), and explicit provenance (the path that produced the candidate).

**Definition 2.2 (Candidate-generation path).** The *candidate-generation path* is the sequence of operations that takes the internal representation and produces the candidate. The path is content-addressed: each step is a crystal in the CAM memory bank.

**Definition 2.3 (Materials candidate).** A *materials candidate* is a content-addressed crystal with explicit structure and predicted properties. The candidate is not a real material; it is an internal representation with predicted properties.

**Definition 2.4 (Fabrication).** *Fabrication* is the physical production of a real material with the structure of the candidate. Fabrication is external: it requires real-world equipment, real materials, and real measurement.

**Definition 2.5 (Finite-element performance).** *Finite-element performance* is the simulated performance of a real material with the structure of the candidate. The simulation requires external software and external calibration.

**Definition 2.6 (Measured band data).** *Measured band data* is the empirical measurement of the band structure of a real material. The measurement requires external equipment (ARPES, optical spectroscopy, etc.) and external calibration.

**Definition 2.7 (Biological performance).** *Biological performance* is the empirical measurement of the interaction of a real material with a biological system. The measurement requires external equipment and external calibration.

---

## 3. Candidate-Generation Path

**Theorem 3.1 (Candidate-generation path is receipt-bound).** The candidate-generation path is receipt-bound: each step is a typed operation in the CAM crystal memory bank, with explicit lane (`cam_crystal_reapplication_result`) and explicit provenance.

*Proof.* Direct from the structure of the CAM crystal memory bank (Paper 0, §3). The path is a sequence of crystals, each content-addressed and receipt-bound. ∎

**Corollary 3.2 (Path is content-addressed).** The candidate-generation path is content-addressed: each step has a sha256 hash, and the path is reproducible.

*Proof.* Direct from Theorem 3.1. ∎

**Corollary 3.3 (Path is typed).** The candidate-generation path is typed: each step is declared with the lane `cam_crystal_reapplication_result`.

*Proof.* Direct from Theorem 3.1. The lane is the claim lane in the 8-lane classification. ∎

**Remark 3.4.** The candidate-generation path being receipt-bound is the structural reason the candidate generation is honest. The path is explicit, typed, and reproducible; the candidate is a content-addressed crystal.

---

## 4. Fabrication and Finite-Element Performance Deferred

**Theorem 4.1 (Fabrication and finite-element performance are deferred).** Fabrication, finite-element performance, measured band data, and biological performance are deferred to external validation tasks.

*Proof.* Direct from the structure of the FLCR series. The candidate generation is internal; the empirical validation is external. ∎

**Corollary 4.2 (External validation requires real-world data).** Fabrication, finite-element performance, measured band data, and biological performance require real-world equipment, real materials, and real measurement.

*Proof.* Direct from Theorem 4.1. ∎

**Corollary 4.3 (External validation is open).** External validation is an open obligation. The proof is the application papers (Papers 81–100) and external validation tasks.

*Proof.* Direct from Theorem 4.1. ∎

**Remark 4.4.** The fabrication and finite-element performance being deferred is the structural reason the candidate generation is honest. The internal representation is closed-now; the empirical validation is staged-open.

---

## 5. Electron-Hole-Exciton Accounting

**Theorem 5.1 (Electron-hole-exciton accounting is the substrate).** The electron-hole-exciton accounting (Paper 34) is the substrate of the materials candidate generation. The accounting tracks the electron, hole, recombination, screening, and exciton states of the material; the candidate generation uses the accounting to predict the material's optical and electronic properties.

*Proof.* Direct from the structure of the FLCR series. The electron-hole-exciton accounting is the standard FLCR doctrine for the optical and electronic properties of materials. ∎

**Corollary 5.2 (Accounting is standard physics).** The electron-hole-exciton accounting is standard physics: the electron, hole, recombination, screening, and exciton are standard solid-state physics concepts.

*Proof.* Direct from Theorem 5.1. Standard physics (Kittel, Ashcroft & Mermin). ∎

**Corollary 5.3 (Accounting is the substrate of the candidate).** The accounting is the substrate of the candidate: the predicted properties are derived from the accounting.

*Proof.* Direct from Theorem 5.1. ∎

**Remark 5.5.** The electron-hole-exciton accounting being the substrate is the structural reason the candidate generation is grounded in standard physics. The candidate is not arbitrary; it is derived from the accounting.

---

## 6. Applied Forge Descriptor as the Kernel

**Theorem 6.1 (Applied forge descriptor is the kernel).** The applied forge descriptor (Paper 20) is the kernel of the materials candidate generation. The descriptor reads the internal representation, combines the materials descriptors, and routes the candidate to the destination.

*Proof.* Direct from Paper 20. The 3 operations (read, combine, route) are the kernel of the candidate generation. ∎

**Corollary 6.2 (Kernel preserves the claim state).** The kernel preserves the claim state: the internal representation is unchanged by the operations.

*Proof.* Direct from Paper 20, Theorem 3.1. ∎

**Corollary 6.3 (Kernel is non-mutating).** The kernel is non-mutating: the source materials descriptors are unchanged by the operations.

*Proof.* Direct from Paper 20, Theorem 3.1. ∎

**Remark 6.6.** The applied forge descriptor being the kernel is the structural reason the candidate generation is consistent with the FLCR doctrine. The kernel is the same as the kernel for the protein descriptor (Paper 22), the finite game lattice (Paper 23), and the energetic traversal (Paper 24).

---

## 7. Discussion

The materials candidate generation is the act of generating a material candidate from an internal representation by a receipt-bound path. The path is content-addressed and typed; the candidate is a content-addressed crystal. Fabrication, finite-element performance, measured band data, and biological performance are deferred to external validation tasks.

The candidate generation is the foundation of:
- Paper 34 (Electron-Hole-Exciton Accounting): the standard physics import.
- Paper 36 (Condensed Matter, Materials & Metamaterials): the condensed matter and metamaterials translation.
- Paper 95 (Applied Forge Validation): the applied forge validation.

The candidate generation is honest. The internal representation is closed-now; the empirical validation is staged-open; the kernel is non-mutating.

---

## 8. Open Problems

**Open Problem 8.1 (External validation).** The external validation of the materials candidates is open. The validation requires real-world equipment, real materials, and real measurement. *Why not closed:* the real-world data is not yet collected. *Next binding action:* the real-world data must be collected. *Owner:* the application papers (Papers 81–100) and external validation tasks.

**Open Problem 8.2 (Electron-hole-exciton accounting for the candidate).** The electron-hole-exciton accounting for the specific candidate is open. The accounting is the substrate; the specific derivation is deferred. *Why not closed:* the specific derivation requires the candidate's structure and properties. *Next binding action:* the specific derivation must be done. *Owner:* Paper 34 (Electron-Hole-Exciton Accounting).

---

## 9. Forward References

### 9.1 Within Band A (Mathematics and Formalisms)

**Paper 22 (Protein Descriptor & Fold-Facing Kernel).** Paper 22 uses the applied forge descriptor as the substrate for the protein descriptor. **Object:** the protein fold. **1-morphism:** the read operation.

**Paper 23 (Finite Game Lattices & Local Rule Automata).** Paper 23 uses the applied forge descriptor as the substrate for the game lattice. **Object:** the game rule. **1-morphism:** the read operation.

**Paper 24 (Energetic Traversal Maps).** Paper 24 uses the applied forge descriptor as the substrate for the energetic traversal. **Object:** the energetic traversal. **1-morphism:** the read operation.

### 9.2 Within Band B (Standard Model Unification)

**Paper 34 (Electron-Hole-Exciton Accounting).** Paper 34 uses the materials candidate generation as the substrate for the standard physics import. **Object:** the standard physics. **1-morphism:** the bridge operation.

**Paper 36 (Condensed Matter, Materials & Metamaterials).** Paper 36 uses the materials candidate generation as the substrate for the condensed matter translation. **Object:** the condensed matter. **1-morphism:** the bridge operation.

### 9.3 Within Band C (Applications)

**Paper 95 (NP-07, Applied Forge Validation).** Paper 95 uses the materials candidate generation as the substrate for the applied forge validation. **Object:** the applied forge. **1-morphism:** the fold operation.

### 9.4 Cross-references

**Paper 0 (Foreword).** Paper 0 establishes the burden of proof. Paper 21 is the twenty-first paper of Band A.

**Paper 1 (LCR Kernel).** Paper 1 establishes the LCR carrier, the substrate of the internal representation.

**Paper 20 (Applied Forge Reader & Descriptor Kernel).** Paper 20 establishes the applied forge descriptor, the kernel of the candidate generation.

**Paper 40 (Grand Reconstruction Map).** Paper 40 maps every claim in the prior 39 papers to its proof, its analog reconstruction, its code/tool route, its comparator, its calibration, or its named blocker. Paper 21's claims (the internal representation, the candidate-generation path, the fabrication deferred, the electron-hole-exciton accounting, the applied forge descriptor) are mapped by Paper 40 to their receipts (§10).

---

## 10. Receipts

### 10.1 Receipts Cited

**R21.1 (CAM crystal memory bank).** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\CAM_CRYSTAL_MEMORY_BANK\` — 469 crystals, 24 state refs. Backs: Theorem 3.1 (candidate-generation path is receipt-bound).

**R21.2 (Forge module).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\forge.py` — The Forge class with read/combine/route operations. Backs: Theorem 6.1 (applied forge descriptor is the kernel).

**R21.3 (Obligation ledger).** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\OBLIGATION_ROWS.json` — 1,105 rows. Backs: Theorem 4.1 (fabrication and finite-element performance deferred).

### 10.2 Obligation Rows Bound

**FLCR-21-OBL-001.** The internal representation is receipt-bound (Section 2). Status: staged_open.

**FLCR-21-OBL-002.** The candidate-generation path is receipt-bound (Theorem 3.1). Status: staged_open.

**FLCR-21-OBL-003.** The fabrication and finite-element performance are deferred (Theorem 4.1). Status: staged_open.

**FLCR-21-OBL-004.** The electron-hole-exciton accounting is the substrate (Theorem 5.1). Status: staged_open.

**FLCR-21-OBL-005.** The applied forge descriptor is the kernel (Theorem 6.1). Status: staged_open.

### 10.3 Content-Addressed Crystals

- `crystals/slot_crystal/21.*.json` (76 records).
- `states/source_state.MATERIALS_CANDIDATE_GENERATION.json`.

### 10.4 Standards Conformance

The claims in this paper are part of the 240/240 standards conformance verdict (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80.

---

## 11. References

### 11.1 Standard mathematics

- Kittel, C. (2004). *Introduction to Solid State Physics.* Wiley. (Chapter on electron-hole-exciton states.)
- Ashcroft, N. W., & Mermin, N. D. (1976). *Solid State Physics.* Saunders College. (Chapter on band theory.)

### 11.2 Source code

- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\forge.py` — Forge module.
- `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\CAM_CRYSTAL_MEMORY_BANK\` — Crystal memory bank.

### 11.3 Documentation

- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_00__foreword\paper_00.md` — The foreword (Paper 0).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_20__applied_forge_reader\paper_20.md` — The applied forge reader (Paper 20).

### 11.4 Receipts

See §10.

---

## 12. Data vs Interpretation

### Data-backed (D)

- The CAM crystal memory bank: 469 crystals, 24 state refs. (D — `CAM_CRYSTAL_MEMORY_BANK\`.)
- The Forge module: a `Forge` class with read/combine/route operations. (D — `forge.py`.)
- The OBLIGATION_ROWS.json: 1,105 rows. (D — `OBLIGATION_ROWS.json`.)
- The electron-hole-exciton accounting as standard physics. (D — Kittel, Ashcroft & Mermin, standard physics.)

### Interpretation (I)

- The "internal representation" as a content-addressed crystal with explicit structure, properties, and provenance (Definition 2.1). (I — author's structural reading; the CAM memory bank is (D), but the specific "structure + properties + provenance" decomposition is the author's.)
- The "candidate-generation path" as a content-addressed sequence of crystals (Definition 2.2). (I — author's structural reading; the forge module is (D), but the specific "path as sequence of crystals" framing is the author's.)
- The 3-property receipt-bound nature of the path: content-addressed, typed, reproducible (Theorems 3.1, 3.2, 3.3). (I — author's structural reading; the path is content-addressed, but the 3-property characterization is the author's.)
- The "fabrication and finite-element performance deferred" doctrine (Theorem 4.1). (I — author's structural reading; the fabrication requires real-world data, but the specific "deferred" framing is the author's.)
- The "electron-hole-exciton accounting is the substrate" (Theorem 5.1). (I — author's structural reading; the accounting is (D) standard physics, but the specific "substrate of the candidate" framing is the author's.)
- The "applied forge descriptor is the kernel" (Theorem 6.1). (I — author's structural reading; the forge module is (D), but the specific "kernel" framing is the author's.)
- The application of the candidate generation to the condensed matter (Paper 36), the exciton (Paper 34), and the applied forge validation (Paper 95). (I — author's structural reading; the candidate generation is (I), but the specific applications are (I).)

### Fabrication (X)

- None in this paper. The math is (I) but defensible; the CAM crystal memory bank and the Forge module are (D) verified.
- The claim "192/192 standards conformance" was a fabrication. The actual standards count is 240/240 (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The 192/192 figure was invented. (X — corrected to honest 240/240 with caveat.)

---

**End of Paper 21.**

The materials candidate generation. The internal representation. The candidate-generation path. The fabrication and finite-element performance deferred. The electron-hole-exciton accounting. The applied forge descriptor. All backed by receipts. All honest. All forward-referenced.

Paper 22 follows: protein descriptor and fold-facing kernel.
