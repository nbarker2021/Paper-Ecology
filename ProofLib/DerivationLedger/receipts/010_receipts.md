# Derivation Receipts — Paper 010

---
## DRV-4b27c87c7b57 — 10.1 Correction word uniqueness — Is the 24-bit correction word uniquely determined by Layer 1? Conjectural.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:00.395243Z

**sources:** [CrystalLib#4701] paper-02: THEOREM Theorem 2.2 — **Theorem 2.2, Correction-Surface Monitor.** The correction surface  (D); [CrystalLib#12] paper-06: The Rule 30 center bit reconstructs exactly from the Lucas base term plus the correction s (D); [CrystalLib#14] paper-06: The correction fires exactly on the $D_4$ chart states $\{(0,1,0), (1,1,0)\}$. (D); [CrystalLib#15] paper-06: The $D_4$ codec projection of the correction agrees with $C \wedge \neg R$. (D)

**derivation:**
Internal-synthesis: 20 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-59d6af1f8e01 — 10.2 Correction word closed form — Does the 24-bit correction word have a closed-form expression independent of direct Rule 30 simulation? Paper 115 (Correction Tower Closed Form) addresses this.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:00.532060Z

**sources:** [CrystalLib#11] paper-06: The Lucas closed form matches direct Rule 90 simulation at depth 64. (D); [CrystalLib#11] paper-06: The Lucas closed form matches direct Rule 90 simulation at depth 64. (D); [CrystalLib#99] paper-10: The Prize 3 lookup substrate keeps `closed_form_claim = false` and does not overclaim cold (D); [CrystalLib#99] paper-10: The Prize 3 lookup substrate keeps `closed_form_claim = false` and does not overclaim cold (D)

**derivation:**
Internal-synthesis: 28 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-aa3f40a761d7 — 10.3 Aperiodicity of correction word — The Rule 30 center column is conjectured to be aperiodic (Wolfram P1, Paper 085).

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:05.183500Z

**sources:** [CrystalLib#124] paper-12: 1M-bit Wolfram center column: no period ≤ 65,536; density 0.500768. (D); [CrystalLib#124] paper-12: 1M-bit Wolfram center column: no period ≤ 65,536; density 0.500768. (D); [CrystalLib#4163] paper-81: The `wolfram_rule30_center_1m.json` data file (1,000,000 bits) appears in 22 duplicate ins (D); [CrystalLib#12] paper-06: The Rule 30 center bit reconstructs exactly from the Lucas base term plus the correction s (D)

**derivation:**
Internal-synthesis: 17 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-6d57d5e8c5a1 — 10.4 General cold-start readout — Cold-start O(log N) readout is verified at depth 1024 (Paper 002 R2.1).

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:05.193023Z

**sources:** [CrystalLib#99] paper-10: The Prize 3 lookup substrate keeps `closed_form_claim = false` and does not overclaim cold (D); [CrystalLib#4176] paper-83: The cold-start O(log N) architecture (Paper 2, Theorem 6.2) reads the center bit in O(log  (D); [CrystalLib#4313] paper-93: The Rule 30 cold-start formula (Paper 2) provides the base case. (D); [CrystalLib#4439] paper-100: The 26 generating relations are the axioms: 8 LCR states + 4 D4 axioms + 7 J₃(𝕆) axioms +  (D)

**derivation:**
Internal-synthesis: 23 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-12b3af70d83d — 10.5 R10 content-addressed hash — The binding receipt R10 is defined as a tuple of receipts plus the correction bit.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:05.210052Z

**sources:** [CrystalLib#4762] paper-01: Definition 2.1 (LCR Triality) The **LCR triality** is the algebraic structure defined by t (D); [CrystalLib#4762] paper-01: Definition 2.1 (LCR Triality) The **LCR triality** is the algebraic structure defined by t (D); [CrystalLib#4113] paper-79: Phase 15 targets hub receipt closure (FLCR-07/10/11) with obligation binding to on-disk ve (D); [CrystalLib#3502] paper-44: The D4 lattice color-confinement boundary is defined by the condition that the J3(O) error (D)

**derivation:**
Internal-synthesis: 36 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-695f8465f27b — 10.6 Closure paper template — This paper establishes the pattern for all 24 closure papers.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:13.664217Z

**sources:** [CrystalLib#150] paper-14: Cayley-Dickson/Oloid normal form verifies the repeating `1,8,8,1` pattern. (D); [CrystalLib#4887] paper-14: Claim 14.5. The Cayley-Dickson/Oloid carrier verifies a repeating `1,8,8,1` normal-form pa (D); [CrystalLib#5642] paper-00: D: drive file: language_pattern.py (.py, 418b, 2026-03-05) (D); [CrystalLib#6318] paper-00: D: drive file: pattern_mining.py (.py, 25422b, 2026-03-05) (D)

**derivation:**
Internal-synthesis: 22 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.
