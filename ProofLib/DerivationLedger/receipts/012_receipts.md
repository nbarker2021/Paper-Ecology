# Derivation Receipts — Paper 012

---
## DRV-84b2dec374f4 — 12.1 Rootless Leech landing — The verifier records `leech_landing_proved = false`.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:28.188949Z

**sources:** [CrystalLib#60] paper-08: `leech_landing_proved` remains `false`; exact glue-coset representatives at the final edge (D); [CrystalLib#60] paper-08: `leech_landing_proved` remains `false`; exact glue-coset representatives at the final edge (D); [CrystalLib#60] paper-08: `leech_landing_proved` remains `false`; exact glue-coset representatives at the final edge (D); [CrystalLib#60] paper-08: `leech_landing_proved` remains `false`; exact glue-coset representatives at the final edge (D)

**derivation:**
Internal-synthesis: 31 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-a3ccdb159492 — 12.2 Gamma72 polarization — The Gamma72 contract passes (260 payloads, three-sheet round trips) but `polarization_matrices_supplied = false`.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:28.213977Z

**sources:** [CrystalLib#57] paper-08: The Gamma72 contract checks 260 payloads with exact three-sheet round trips. (D); [CrystalLib#57] paper-08: The Gamma72 contract checks 260 payloads with exact three-sheet round trips. (D); [CrystalLib#57] paper-08: The Gamma72 contract checks 260 payloads with exact three-sheet round trips. (D); [CrystalLib#57] paper-08: The Gamma72 contract checks 260 payloads with exact three-sheet round trips. (D)

**derivation:**
Internal-synthesis: 39 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-8c43a6f9050a — 12.3 Nontrivial glue-coset representatives — Exact glue-coset representatives for nontrivial Niemeier terminals (beyond E8³) are recorded as `pending_invariants`.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:28.717053Z

**sources:** [CrystalLib#60] paper-08: `leech_landing_proved` remains `false`; exact glue-coset representatives at the final edge (D); [CrystalLib#60] paper-08: `leech_landing_proved` remains `false`; exact glue-coset representatives at the final edge (D); [CrystalLib#60] paper-08: `leech_landing_proved` remains `false`; exact glue-coset representatives at the final edge (D); [CrystalLib#60] paper-08: `leech_landing_proved` remains `false`; exact glue-coset representatives at the final edge (D)

**derivation:**
Internal-synthesis: 34 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-ce47053935ab — 12.4 Cold-start fingerprint map — A cold-start map from arbitrary depth to Niemeier/Leech would enable deterministic routing through the ladder without recomputation.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:28.977955Z

**sources:** [CrystalLib#4797] paper-03: Theorem 3.1 (Cold-Start Bijection): .** For any boundary address N, the cold-start bijecti (D); [CrystalLib#59] paper-08: Niemeier/Leech enumeration: deterministic selectors, E8³ carriers, Leech type-1/2/3 orbits (D); [CrystalLib#59] paper-08: Niemeier/Leech enumeration: deterministic selectors, E8³ carriers, Leech type-1/2/3 orbits (D); [CrystalLib#99] paper-10: The Prize 3 lookup substrate keeps `closed_form_claim = false` and does not overclaim cold (D)

**derivation:**
Internal-synthesis: 28 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-e9847a606e6a — 12.5 Depth independence — Terminal addresses are verified at depth 4096.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:29.164288Z

**sources:** [CrystalLib#4006] paper-73: Terminal addresses (Paper 9) are the closure points: after a terminal number of samples, t (D); [CrystalLib#4315] paper-93: Terminal addresses are closure points of the lattice closure (Paper 9). (D); [CrystalLib#4320] paper-93: Terminal addresses are the depth levels of the lattice code chain. (D); [CrystalLib#4006] paper-73: Terminal addresses (Paper 9) are the closure points: after a terminal number of samples, t (D)

**derivation:**
Internal-synthesis: 23 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-f21da708cd55 — 12.6 Uniqueness of closure chain — The 7-rung ladder is the active template but has not been proved unique.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:34.600767Z

**sources:** [CrystalLib#185] paper-17: The `n=24` rung verifies Golay-code ingredients and `3×8` carrier geometry; the Leech glue (D); [CrystalLib#4553] paper-17: The `n=24` rung verifies Golay-code ingredients and `3×8` carrier geometry; the Leech glue (D); [CrystalLib#4785] paper-02: Definition 1.1 (Rung Triality Form) Each rung `(n)` in the ladder is the LCR triality at s (D); [CrystalLib#185] paper-17: The `n=24` rung verifies Golay-code ingredients and `3×8` carrier geometry; the Leech glue (D)

**derivation:**
Internal-synthesis: 38 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-bafd936911f5 — 12.7 Closure verifier table — The SQLLib instructions mention a 4th table `closure_verifiers` that does not yet exist in the seed data.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:35.018395Z

**sources:** [CrystalLib#99] paper-10: The Prize 3 lookup substrate keeps `closed_form_claim = false` and does not overclaim cold (D); [CrystalLib#4113] paper-79: Phase 15 targets hub receipt closure (FLCR-07/10/11) with obligation binding to on-disk ve (D); [CrystalLib#4954] paper-00: Session action: sql_source_wiring — Populated 319 NULL sql_source fields from SQLLib. 100% (D); [CrystalLib#331302] paper-00: D: drive file: SQLLIB_EXISTING_CATALOG.md (.md, 27129b, 2026-07-04) (D)

**derivation:**
Internal-synthesis: 39 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.

---
## DRV-fc600578ddd8 — 12.8 CAMLib harvest — The CAMLib for paper-08 is a stub with no harvested claims.

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T22:53:38.902446Z

**sources:** [CrystalLib#326548] paper-00: D: drive file: 12_CAMLIB_COPY.md (.md, 7221b, 2026-07-04) (D); [CrystalLib#4949] paper-00: Session action: crystal_layer_deep_audit — Found 103 crystals for 1966 claims (5.2% covera (D); [CrystalLib#4958] paper-00: Session action: cqekernel_stub_upgrade — Upgraded 48 stub papers to real status — all have (D); [CrystalLib#6416] paper-00: D: drive file: agrmcontroller_stub.py (.py, 1008b, 2026-03-05) (D)

**derivation:**
Internal-synthesis: 15 existing D-claim(s) in CrystalLib share a specific concept with this claim and already answer it. Connected via receipt chain.
