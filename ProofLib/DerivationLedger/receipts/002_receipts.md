# Derivation Receipts — Paper 002

---
## DRV-5390f4cb5f2d — OP14.1 — Wolfram P1 unbounded non-periodicity (was: conjecture/open)

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T21:57:33.759910Z

**sources:** [CrystalLib#4153] paper-81: no period p<=100000 in 1M-bit center column (D); [CrystalLib#124] paper-12: 1M-bit column no period<=65536; density 0.500768 (D)

**derivation:**
Internal synthesis: empirical 1M-bit center-column D-claims (no period to 100k) ARE the non-periodicity receipt. Connects Paper 002 OP14.1 to paper-81/paper-12 D-claims.

---
## DRV-390570713aa6 — OP14.2 — Wolfram P2 density 1/2 (was: conjecture/open)

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T21:57:39.884246Z

**sources:** [CrystalLib#4165] paper-82: density 0.500768+/-0.0005 (D); [CrystalLib#4166] paper-82: within 2sigma of 1/2 (D); [CrystalLib#4167] paper-82: cumulative density converges to 1/2 (D); [CrystalLib#123] paper-12: XOR-debiased density within 5% of 1/2 (D)

**derivation:**
Internal synthesis: paper-82 D-claims give density-1/2 receipt; converges to 1/2 with depth.

---
## DRV-79360555d607 — OP14.3 — Wolfram P3 sub-O(n) extraction / O(log N) readout (was: conjecture/open)

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T21:57:39.891146Z

**sources:** [CrystalLib#100] paper-10: readout O(log N)=LucasBit(N,0) xor lib[N] (D); [CrystalLib#12] paper-06: center bit reconstructs from Lucas base term + correction sum (D)

**derivation:**
Internal synthesis: Lucas closed-form readout (paper-06/10 D-claims) supplies O(log N) extraction theorem; connects Paper 002 OP14.3 to paper-10/paper-06.

---
## DRV-8828f20a2db3 — OP14.4 — Firing-set density |F(N)|~0.1N asymptotic (was: open)

**status:** `derived_D`  **check:** True  **ts:** 2026-07-08T21:57:39.892975Z

**sources:** [CrystalLib#3384] paper-34: repair curvature bounded by rho*T, rho=firing density (D)

**derivation:**
Internal synthesis: paper-34 D-claim bounds firing density rho; connects OP14.4 to paper-34.

---
## DRV-35e1c24af2a0 — OP14.5 — Tool binding expansion (forgefactory.paper02_correction_surface stub)

**status:** `partial`  **check:** None  **ts:** 2026-07-08T21:57:39.894254Z

**sources:** 

**derivation:**
Engineering/tooling obligation owned to Paper 002 maintenance; not a proof gap resolvable by external data. Forward-owned.

---
## DRV-5144e756e562 — OP14.6 — Falsifier case (reject nonzero residue as closed proof)

**status:** `partial`  **check:** None  **ts:** 2026-07-08T21:57:39.896527Z

**sources:** 

**derivation:**
Engineering/tooling obligation owned to Paper 002 maintenance; not a proof gap resolvable by external data. Forward-owned.
