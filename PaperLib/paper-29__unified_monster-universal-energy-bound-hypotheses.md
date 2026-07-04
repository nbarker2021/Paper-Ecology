# Paper 29 — Monster/Universal Energy-Bound Hypotheses

**Status.** IPMC for the Monster/Moonshine ceiling and horizon-bound claim-separation: arithmetic row `47 * 59 * 71 = 196883`, McKay row `196884 = 1 + 196883`, finite centroid-VOA partition `Z(q) = 2q^0 + 6q^5`, external mathematical anchor that `47, 59, 71` are the three largest supersingular primes, and prime-tower ceiling fact that `73` does not divide `|M|`. ECO for measured physical energy bound, units-bearing witness function, and Pariah/Happy-Family encoding-invariance of the boundary.

---

## Abstract

Paper 29 states the CQECMPLX Monster/Moonshine/Pariah ceiling while keeping the physical energy reading under quarantine. The central structural identity is affirmative: `196883 = 47 * 59 * 71`, where `47`, `59`, and `71` are the three largest supersingular primes at the top of the Monster prime tower. The next prime, `73`, does not divide the Monster order, so the product is a structural ceiling of the supersingular/Monster layer. The McKay row `196884 = 1 + 196883` and the finite centroid-VOA partition `Z(q) = 2q^0 + 6q^5` sit beneath that ceiling as the finite excitation surface.

The receipt surface separates mathematical proof rows from horizon readings. `supersingular_prime_ceiling_receipt.json` passes all 12 checks; `lmfdb_moonshine_anchor_real_data_receipt.json` passes all 13 checks; `moonshine_real_data_experiment_receipt.json` passes all 6 checks; and `monster_internal_map_receipt.json` passes all 5 checks. `monster_energy_bound_hypotheses_receipt.json` returns `pass_with_quarantined_hypotheses`, because physical energy-bound language still lacks a units-bearing witness function. Later papers may cite the Monster prime-tower ceiling as a closed structural fact, but any measured energy or physical supercriticality reading must carry the NP-06 calibration gate.

**Keywords:** Monster group; supersingular primes; Monstrous Moonshine; McKay row; centroid VOA; universal ceiling; energy-bound hypothesis; witness function; Pariah boundary; encoding invariance.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 29.1 | `47 * 59 * 71 = 196883`. | [D] | Arithmetic verifier; `supersingular_prime_ceiling_receipt.json` |
| 29.2 | `196884 = 1 + 196883`. | [D] | McKay row verifier; Moonshine anchor receipts |
| 29.3 | `47, 59, 71` are the top supersingular primes and `73` does not divide `|M|`. | [D] | Published-data receipts and Monster-order check |
| 29.4 | The eight-state centroid-VOA chart has partition `Z(q) = 2q^0 + 6q^5`. | [D] | `verify_voa_sector_decomposition`; centroid chain |
| 29.5 | The prime-tower ceiling is the structural twin of Paper 26's carrier-collapse boundary. | [I] | Shared ceiling/supercriticality framing; analogy, not physical units |
| 29.6 | `196883` is a measured universal energy bound. | [X] | No witness function; no physical units; routed to NP-06 |
| 29.7 | Pariah/Happy-Family boundary is encoding-invariant. | [X] | Boundary named but not invariant over encoder class; routed to NP-09 |

---

## 2. Definitions

**VOA weight.** The output of `voa_weight(s)`, a wrap-step count assigned to state `s` in the eight-state chart. These weights are internal horizon-energy analogs; calibrated energy values require units and measurement.

**Monster representation row.** The integer `196883`, the dimension of the smallest nontrivial irreducible representation of the Monster.

**McKay row.** `196884 = 1 + 196883`, the decomposition of the Moonshine j-function coefficient.

**Horizon hypothesis.** A useful candidate reading admitted into the corpus only when it is marked unwitnessed and falsifiable.

**Witness function.** The missing promotion object: it must state input domain, output domain, physical units when relevant, verifier, receipt, and falsifier.

---

## 3. Theorems and Proofs

### Theorem 29.1 — Arithmetic Identity

`47 * 59 * 71 = 196883`.

**Proof.** The arithmetic verifier multiplies the three listed primes and obtains `196883`. This is a closed integer identity. ∎

### Theorem 29.2 — McKay Row

`196884 = 1 + 196883`.

**Proof.** The McKay row verifier confirms the decomposition. The observer row `1` plus the Monster representation row `196883` equals the Moonshine j-function coefficient `196884`. This is a reference decomposition, not a new Moonshine theorem. ∎

### Theorem 29.3 — Supersingular Prime Ceiling

`47, 59, 71` are the top supersingular primes and `73` does not divide `|M|`.

**Proof.** The supersingular-prime ceiling verifier checks the Monster order against the published prime list, confirms that `47`, `59`, and `71` are the top supersingular primes, and confirms that `73` does not divide `|M|`. This closes the structural ceiling as an external mathematical anchor. ∎

### Theorem 29.4 — Centroid-VOA Partition

The eight-state centroid-VOA chart has partition `Z(q) = 2q^0 + 6q^5`.

**Proof.** The verifier `verify_voa_sector_decomposition` returns `Z(q) = 2q^0 + 6q^5` with weight distribution `{0: 2, 5: 6}`. The two weight-0 states are `(0,0,0)` and `(1,1,1)`; the six remaining chart states are the excited finite orbit. The centroid chain confirms the same two fixed points and six period-4 states. ∎

### Theorem 29.5 — Monster Ceiling with Quarantined Energy Hypotheses

A Monster/energy-bound statement is valid in the CQECMPLX kernel exactly when it separates closed finite and external-mathematical evidence from the external witness bridge.

**Proof.** Arithmetic, supersingular-prime, McKay-row, and finite centroid-VOA rows pass as proof rows (Theorems 29.1–29.4). Physical energy-bound readings remain falsifiable horizon hypotheses because the energy-bound hypothesis rows have no witness function and no physical units (Claim 29.6). The Pariah/Happy-Family boundary row has no encoding-invariance theorem over an admissible encoder class (Claim 29.7). Therefore the structural theorem is closed, and the physical/invariance readings remain routed obligations. ∎

---

## 4. Verifiers and Receipts

### 4.1 Supersingular Prime Ceiling

`verify_supersingular_prime_ceiling.py` → `supersingular_prime_ceiling_receipt.json`

| Field | Value |
|-------|-------|
| status | pass |
| checks | 12/12 |

### 4.2 LMFDB Moonshine Anchor

`verify_lmfdb_moonshine_anchor.py` → `lmfdb_moonshine_anchor_real_data_receipt.json`

| Field | Value |
|-------|-------|
| status | pass |
| checks | 13/13 |

### 4.3 Moonshine Real Data Experiment

`verify_moonshine_real_data_experiment.py` → `moonshine_real_data_experiment_receipt.json`

| Field | Value |
|-------|-------|
| status | pass |
| checks | 6/6 |

### 4.4 Monster Internal Map

`verify_monster_internal_map.py` → `monster_internal_map_receipt.json`

| Field | Value |
|-------|-------|
| status | pass |
| checks | 5/5 |

### 4.5 Monster Energy Bound Hypotheses

`verify_monster_energy_bound_hypotheses.py` → `monster_energy_bound_hypotheses_receipt.json`

| Field | Value |
|-------|-------|
| status | pass_with_quarantined_hypotheses |

---

## 5. Hand Reconstruction

All claims can be reconstructed by hand from the definitions:

1. **29.1:** `47 * 59 = 2773; 2773 * 71 = 196883`. Direct multiplication.
2. **29.2:** `196883 + 1 = 196884`. Direct addition.
3. **29.3:** The Monster order is known; `47, 59, 71` divide it; `73` does not.
4. **29.4:** The VOA partition has two weight-0 states and six weight-5 states.
5. **29.5:** The proof rows are closed; the horizon hypotheses lack witness functions.

No external computation is required.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F29.1 | `47 * 59 * 71 ≠ 196883`. | Direct multiplication gives `196883`. |
| F29.2 | `73` divides `|M|`. | The Monster order check confirms `73` does not divide it. |
| F29.3 | `196883` is a measured energy bound. | No witness function; no physical units; quarantined. |
| F29.4 | Pariah/Happy-Family boundary is encoding-invariant. | No invariance theorem over an admissible encoder class. |
| F29.5 | The VOA partition is different from `2q^0 + 6q^5`. | The verifier confirms the partition. |

---

## 7. Relation to Later Papers

- **Paper 8** (Lattice Closure) exports the Leech lookup that Paper 29 uses as structural context.
- **Paper 17** (E6–E8 Error-Correction Tower) exports the coding theory that underlies the Monster ceiling.
- **Paper 18** (VOA-Moonshine-Monster) exports the VOA and Moonshine content that Paper 29 builds on.
- **Paper 26** (Z-Pinch and Shear Horizon) shares the carrier-collapse boundary framing with Paper 29.
- **Paper 27** (Observer Delay) may use the Monster ceiling as a horizon-energy analog.
- **Later papers** may cite the Monster prime-tower ceiling as a closed structural fact, but any measured energy or physical supercriticality reading must carry the NP-06 calibration gate.

---

## 8. Open Obligations

1. **Physical energy-bound witness function (29.6).** Requires a units-bearing witness function with verifier, receipt, and falsifier.
2. **Pariah/Happy-Family encoding-invariance (29.7).** Requires an admissible encoder class plus invariance theorem or counterexample family.

---

## 9. Bibliography

1. J. H. Conway and S. P. Norton, "Monstrous Moonshine," *Bull. London Math. Soc.* 11 (1979), 308–339. Monster group and Moonshine.
2. R. E. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras," *Invent. Math.* 109 (1992), 405–444. VOA and Monster group.
3. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory.
4. J. H. Conway, R. T. Curtis, S. P. Norton, R. A. Parker, R. A. Wilson, *ATLAS of Finite Groups*, Clarendon Press, 1985. Finite group data.
5. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and `E8` structures.
6. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. `J_3(O)` and exceptional algebra.
7. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. `SU(3)` and representation theory.
8. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
9. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 and algebraic structure.
10. D. E. Knuth, *The Art of Computer Programming, Volume 2: Seminumerical Algorithms*, Addison-Wesley, 1997. Finite fields and arithmetic.

---

## 10. Data vs Interpretation

### Data-backed (D)

- `47 * 59 * 71 = 196883` is a verified arithmetic identity. (D — `supersingular_prime_ceiling_receipt.json`)
- `196884 = 1 + 196883` is a verified McKay row. (D — Moonshine anchor receipts)
- `47, 59, 71` are the top supersingular primes and `73` does not divide `|M|`. (D — published-data receipts)
- The centroid-VOA partition is `Z(q) = 2q^0 + 6q^5`. (D — `verify_voa_sector_decomposition`)

### Interpretation (I)

- The "Monster prime-tower ceiling" framing is the author's structural reading of the arithmetic identity as a supercriticality bound. (I — the underlying arithmetic is (D).)
- The "structural twin of Paper 26's carrier-collapse boundary" is the author's analogical reading of the two papers. (I — the analogy is stated but not proved as a physical identity.)

### Fabrication (X)

- The claim that `196883` is a measured universal energy bound is a fabrication (rejected). The actual status is `pass_with_quarantined_hypotheses` with no witness function. (X — replaced with honest quarantine in Theorem 29.5.)
- The claim that Pariah/Happy-Family boundary is encoding-invariant is a fabrication (rejected). The actual status is open with no invariance theorem. (X — replaced with honest open obligation in Claim 29.7.)

---

## 11. Conclusion

Paper 29 now has a sharper scientific shape: the Monster prime-tower ceiling is not merely a metaphor, and the measured energy-bound claim is not silently closed. The arithmetic, published mathematical anchors, and finite VOA rows are usable immediately. The physical energy bridge and encoder-invariance boundary remain live obligations with their own proposed follow-on papers.
