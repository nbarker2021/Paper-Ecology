# Paper 03 — D4/J3 Triality Surface

**Status:** IPMC — internal physics map closed for the finite local triality surface (axis/sheet bijection, diagonal carrier, T1–T7 foundation, D12/annealing/atlas, D4 block tower). Full D4 triality, full F4 action, off-diagonal octonionic dynamics, and physical identifications remain open.

**Source papers:** CQE-paper-03, CQE-paper-03.25, CQE-paper-03.50, CQE-paper-03.75, CQE-paper-03_UPGRADED.  
**Canonical formal paper:** `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-03/FORMAL_PAPER.md`.  
**Verifiers:** `verify_triality_surface.py`, `verify_algebra_foundation_T1_T4.py`, `verify_su3_closure_T5_T7.py`, `verify_d12_idempotent_chain.py`, `verify_triality_annealing.py`, `verify_d4_atlas_bijectivity.py`, `verify_d4_block_tower_exceptional.py`.

---

## Abstract

Paper 03 defines the first explicit multi-representation surface in the active CQECMPLX sequence. Paper 01 supplies the LCR carrier; Paper 02 supplies typed correction residue. Paper 03 registers the same eight local binary states in three coordinated readout languages:

```text
LCR state  <->  D4-style axis/sheet coordinate  <->  diagonal J3(O) carrier.
```

The closed claim is a finite registration theorem: the axis/sheet coordinate is a bijection on `{0,1}^3`; the diagonal carrier preserves shell as trace; the shell-2 states map to trace-2 diagonal idempotents; and the Paper 02 correction coordinates are preserved. The paper also binds a stack of finite receipts: algebra foundation T1–T7, D12 idempotent chain, S3 annealing, D4 atlas bijectivity, and D4 block-tower exceptional reapplication.

The guard is essential. Paper 03 does not prove the full D4 triality automorphism theorem, a full continuous F4 action on `J3(O)`, off-diagonal octonionic dynamics, physical quark-face identification, energy quantum calibration, or product-scale cluster scheduling. It proves the finite local surface those later claims must address.

### Keywords

Triality surface; D4 chart; J3(O); diagonal carrier; axis/sheet bijection; S3 annealing; D12 idempotent chain; F4 route guard; CQECMPLX receipts.

---

## Claim Ledger

| ID | Claim | Tag | Evidence | Boundary |
|----|-------|-----|----------|----------|
| 03.1 | The axis/sheet map `(axis, sheet): S → {0,1,2,3} × {0,1}` is bijective. | [D] | `verify_triality_surface.py`; `triality_surface_receipt.json` (6/6) | Finite local registration only |
| 03.2 | The diagonal carrier `phi(L,C,R) = diag(L,C,R)` preserves shell as trace. | [D] | Same verifier; coordinate-wise sum | Diagonal subalgebra only |
| 03.3 | Every shell-2 LCR state maps to a trace-2 diagonal idempotent under coordinate-wise Jordan product. | [D] | Same verifier; `diag(a,b,c) ∘ diag(a,b,c) = diag(a²,b²,c²)` | Diagonal entries only; no off-diagonal dynamics |
| 03.4 | The Paper 02 correction firing states `(0,1,0)` and `(1,1,0)` land at coordinates `(2,0)` and `(3,1)`. | [D] | Same verifier; explicit coordinate check | Production codec |
| 03.5 | The axis pairs are antipodal complements: `axis(σ) = axis(¬σ)` for all `σ ∈ S`. | [D] | Same verifier; complement check | Finite construction |
| 03.6 | T1–T4 octonion axioms, `J3(O)` Jordan axioms, chart-to-`J3(O)` isomorphism, and exact `n=3` SU(3) Weyl closure are paper-bound to Paper 03. | [D] | `verify_algebra_foundation_T1_T4.py`; `algebra_foundation_T1_T4_receipt.json` (8/8) | Reapplication of proven substrate; not first proof |
| 03.7 | T5–T7 closure at scale 3, identical trace-block closure, and exact-rational 8×8 transition matrix are paper-bound to Paper 03. | [D] | `verify_su3_closure_T5_T7.py`; `su3_closure_T5_T7_receipt.json` (10/10) | Same as above |
| 03.8 | The D12 group acts on the D4 chart by idempotents, matches Weyl `(1,3)`, preserves trace-2, and permutes D4 axis classes. | [D] | `verify_d12_idempotent_chain.py`; `d12_idempotent_chain_receipt.json` (6/6) | Reapplication of proven substrate |
| 03.9 | S3 transpositions drive every 3-bit state into the Lie-conjugate basin in at most 3 swaps. | [D] | `verify_triality_annealing.py`; `triality_annealing_receipt.json` (10/10) | Finite annealing bound; cluster scheduling is product-layer |
| 03.10 | The D4 chart atlas has 8 dihedral views, each bijective, closed under composition, with identity, inverses, rotations of order 4, mirrors as involutions, and non-abelian structure. | [D] | `verify_d4_atlas_bijectivity.py`; `d4_atlas_bijectivity_receipt.json` (10/10) | Finite group structure |
| 03.11 | The D4 block tower and `G2 → F4` T5 conjugate triple are paper-bound to Paper 03. | [D] | `verify_d4_block_tower_exceptional.py`; `d4_block_tower_exceptional_receipt.json` (3/3) | Reapplication of proven substrate |
| 03.12 | The full D4 triality automorphism theorem is proven here. | [X] | No closing receipt in Paper 03 | Route to NP-04 / exceptional-route papers |
| 03.13 | A full continuous F4 action on `J3(O)` is proven here. | [X] | No closing receipt | Route to NP-04 |
| 03.14 | Off-diagonal octonionic dynamics are proven here. | [X] | No closing receipt | Requires separate theorem |
| 03.15 | Physical quark-face identification or energy quantum calibration is proven here. | [X] | No closing receipt | Route to calibration papers |
| 03.16 | Product-scale cluster scheduling safety/liveness is proven here. | [X] | No closing receipt | Product-layer work |

---

## Definitions

**Definition 3.1 (LCR state space).** Let `S = {0,1}^3`. An element `σ = (L, C, R) ∈ S` is a local binary state with left boundary `L`, center `C`, and right boundary `R`.

**Definition 3.2 (Shell).** The shell of `σ` is `shell(σ) = L + C + R ∈ {0, 1, 2, 3}`.

**Definition 3.3 (Axis map).** Define `axis: S → {0,1,2,3}` by the four antipodal pairs:

```text
axis(0,0,0) = 0    axis(1,1,1) = 0
axis(1,0,0) = 1    axis(0,1,1) = 1
axis(0,1,0) = 2    axis(1,0,1) = 2
axis(0,0,1) = 3    axis(1,1,0) = 3.
```

**Definition 3.4 (Sheet map).** Define `sheet: S → {0,1}` by

```text
sheet(σ) = 0  if shell(σ) ≤ 1,
sheet(σ) = 1  if shell(σ) ≥ 2.
```

**Definition 3.5 (Diagonal carrier).** Define `phi: S → J3(O)` by

```text
phi(L,C,R) = diag(L, C, R),
```

where `diag(L,C,R)` is the 3×3 diagonal matrix with entries `L, C, R` on the diagonal and zero elsewhere, viewed as an element of the diagonal subalgebra of the exceptional Jordan algebra `J3(O)`.

**Definition 3.6 (Diagonal Jordan product).** On diagonal carriers, the Jordan product is coordinate-wise multiplication:

```text
diag(a,b,c) ∘ diag(a,b,c) = diag(a², b², c²).
```

---

## Theorems and Proofs

**Theorem 3.1 (Local Triality Surface).** The map

```text
tau: S → {0,1,2,3} × {0,1} × J3(O),
tau(σ) = (axis(σ), sheet(σ), phi(σ)),
```

is a faithful three-language presentation of the eight binary LCR states. Specifically:

(a) The axis map partitions `S` into four disjoint antipodal pairs, and `axis(σ) = axis(¬σ)` for every `σ ∈ S`, where `¬σ` denotes bitwise complement.

(b) The map `(axis, sheet): S → {0,1,2,3} × {0,1}` is a bijection.

(c) `trace(phi(σ)) = shell(σ)` for every `σ ∈ S`.

(d) If `shell(σ) = 2`, then `phi(σ)` is a trace-2 diagonal idempotent: `phi(σ) ∘ phi(σ) = phi(σ)` and `trace(phi(σ)) = 2`.

(e) The Paper 02 correction firing states `(0,1,0)` and `(1,1,0)` map to axis/sheet coordinates `(2,0)` and `(3,1)`.

*Proof.* For (a), the axis map is defined by the four antipodal pairs in Definition 3.3. By direct inspection, each pair consists of a state and its bitwise complement: `(0,0,0)` and `(1,1,1)` are complements; `(1,0,0)` and `(0,1,1)` are complements; `(0,1,0)` and `(1,0,1)` are complements; `(0,0,1)` and `(1,1,0)` are complements. Since the four pairs partition `S` and each pair receives a distinct axis value, `axis(σ) = axis(¬σ)` holds for all `σ`. ∎

For (b), consider any axis pair `A_k = {σ, ¬σ}`. By construction, `shell(σ) + shell(¬σ) = 3`. Therefore exactly one member has `shell ≤ 1` and exactly one has `shell ≥ 2`. The sheet bit distinguishes the two members: `sheet(σ) = 0` and `sheet(¬σ) = 1`, or vice versa. Thus `(axis, sheet)` assigns a unique coordinate to each of the eight states. Since the codomain has exactly eight elements, `(axis, sheet)` is bijective. ∎

For (c), `trace(phi(L,C,R)) = L + C + R = shell(L,C,R)` by direct summation of the diagonal entries. ∎

For (d), if `shell(σ) = 2`, then exactly two of `L, C, R` are `1` and one is `0`. The coordinate-wise Jordan product gives `phi(σ) ∘ phi(σ) = diag(L², C², R²) = diag(L, C, R) = phi(σ)`, since `0² = 0` and `1² = 1`. Thus `phi(σ)` is idempotent, and `trace(phi(σ)) = 2` by (c). ∎

For (e), direct substitution: `axis(0,1,0) = 2`, `sheet(0,1,0) = 0` (shell=1); `axis(1,1,0) = 3`, `sheet(1,1,0) = 1` (shell=2). The coordinates are `(2,0)` and `(3,1)`. ∎

**Theorem 3.2 (D4 Block Tower and Exceptional Conjugate Reapplication).** The D4 chart block, D4 block tower, and `G2 → F4` T5 conjugate triple verifiers are paper-bound to the Paper 03 registration surface. The substrate checks for these three mechanisms pass.

*Proof.* The verifier `verify_d4_block_tower_exceptional.py` replays the substrate checks from `lattice_forge.block_d4`, `lattice_forge.block_tower`, and `lattice_forge.g2_f4_t5_conjugate`. All three checks return `pass`. The theorem binds these proven substrate mechanisms to Paper 03; it does not claim any broader D4 or F4 theorem beyond the named verifier rows. ∎

**Theorem 3.3 (Algebra Foundation Stack).** The algebra-foundation receipts T1–T7 are paper-bound to Paper 03: T1–T4 (octonion axioms, `J3(O)` Jordan axioms, chart-to-`J3(O)` isomorphism, exact `n=3` SU(3) Weyl closure) and T5–T7 (closure at scale 3, identical trace-block closure, exact-rational 8×8 transition matrix).

*Proof.* The verifier `verify_algebra_foundation_T1_T4.py` replays T1–T4 from `lattice_forge`: T1 verifies octonion axioms (identity, imaginary square, Fano triples, norm composition, left alternativity); T2 verifies `J3(O)` Jordan axioms (diagonal idempotents, orthogonality, sum-to-identity, trace-2 idempotents, Weyl `(1,3)` chirality); T3 verifies the chart-to-`J3(O)` isomorphism with zero bijection failures and identifies shell-2 with trace-2; T4 verifies exact `n=3` SU(3) Weyl closure as a rational S3 group-ring element with residual squared zero. All 8 checks pass.

The verifier `verify_su3_closure_T5_T7.py` replays T5–T7: T5 verifies closure at scale 3 with residual near zero; T6 verifies that both trace-1 and trace-2 blocks close identically as the same exact S3 element with zero residual; T7 verifies the 8×8 transition matrix has exactly 8 rows and is exactly stochastic. All 10 checks pass. These receipts are reapplications of proven substrate theorems; the theorem binds them to Paper 03. ∎

**Theorem 3.4 (D12 and Atlas Dynamics).** The D12 idempotent chain, S3 triality annealing, and D4 chart-atlas bijectivity receipts are paper-bound to Paper 03.

*Proof.* The verifier `verify_d12_idempotent_chain.py` checks D12 group axioms, idempotent chain, Weyl `(1,3)` matching, trace-2 preservation, axis-class conjugation, and orbit structure. All 6 checks pass.

The verifier `verify_triality_annealing.py` checks that S3 transpositions drive every 3-bit state into the Lie-conjugate basin in at most 3 swaps, with the tight bound attained at `(0,1,1)` and `(1,0,0)`. All 10 checks pass. The theorem notes that multi-node scheduling safety/liveness under real capacity constraints is product-layer work, not a paper claim.

The verifier `verify_d4_atlas_bijectivity.py` checks 8 dihedral views, each bijective, closed under composition, with identity, inverses, rotations of order 4, mirrors as involutions, and non-abelian structure. All 10 checks pass. These receipts are reapplications; the theorem binds them to Paper 03. ∎

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Status |
|----------|---------|--------|--------|
| `verify_triality_surface.py` | `triality_surface_receipt.json` | 6 | pass |
| `verify_algebra_foundation_T1_T4.py` | `algebra_foundation_T1_T4_receipt.json` | 8 | pass |
| `verify_su3_closure_T5_T7.py` | `su3_closure_T5_T7_receipt.json` | 10 | pass |
| `verify_d12_idempotent_chain.py` | `d12_idempotent_chain_receipt.json` | 6 | pass |
| `verify_triality_annealing.py` | `triality_annealing_receipt.json` | 10 | pass |
| `verify_d4_atlas_bijectivity.py` | `d4_atlas_bijectivity_receipt.json` | 10 | pass |
| `verify_d4_block_tower_exceptional.py` | `d4_block_tower_exceptional_receipt.json` | 3 | pass |

**Total checks:** 53/53 pass.

---

## Hand Reconstruction

1. List the eight LCR states: `(0,0,0)`, `(0,0,1)`, `(0,1,0)`, `(0,1,1)`, `(1,0,0)`, `(1,0,1)`, `(1,1,0)`, `(1,1,1)`.
2. Pair each state with its bitwise complement.
3. Assign the four pairs to axes 0 through 3.
4. Mark `sheet = 0` for `shell ≤ 1`; mark `sheet = 1` for `shell ≥ 2`.
5. Confirm that every `(axis, sheet)` coordinate names exactly one LCR state.
6. Draw the diagonal `diag(L,C,R)` for each state.
7. Confirm that `trace = shell` for every state.
8. For shell-2 states, verify that coordinate-wise multiplication leaves the diagonal unchanged (idempotence).
9. Confirm that the Paper 02 correction states `(0,1,0)` and `(1,1,0)` map to `(2,0)` and `(3,1)`.

---

## Falsifiers and Rejected Claims

The following claims were present in historical drafts of Paper 03 and have been rejected:

| Rejected Claim | Reason |
|---------------|--------|
| "The full D4 triality automorphism is proven in Paper 03." | Not proven. The paper proves a finite local registration surface only. Full triality requires a separate theorem. |
| "A full continuous F4 action on `J3(O)` is proven here." | Not proven. Only diagonal carriers and finite reapplications are in scope. |
| "Off-diagonal octonionic dynamics are covered." | Not in scope. The diagonal carrier uses only coordinate-wise multiplication; no octonionic product structure is invoked. |
| "Physical quark-face identification is established." | Not in scope. No physics calibration or particle identification is claimed. |
| Product-scale cluster scheduling safety/liveness is a paper theorem. | Not claimed. The annealing bound is finite (max 3 swaps); scheduling is product-layer. |
| The S3 annealing bound is tight at `(1,1,0)` requiring exactly 3 swaps. | Rejected. The tight bound is at `(0,1,1)` and `(1,0,0)`; `(1,1,0)` requires 2 swaps. The max-3 bound itself is correct. |

---

## Relation to Prior and Later Papers

**Paper 01 (LCR Carrier):** Paper 03 inherits the corrected boundary address/value distinction. The axis/sheet labels classify complete states, not merely boundary values. The reversal involution of Paper 01 corresponds to swapping antipodal states within an axis pair.

**Paper 02 (Correction Surface):** The correction firing states `(0,1,0)` and `(1,1,0)` are preserved under the Paper 03 registration, mapping to coordinates `(2,0)` and `(3,1)`. This lets later papers transport correction residue into the axis/sheet language.

**Paper 04 and beyond:** Paper 03 supplies the coordinate surface that Papers 04–08 consume. The finite local registration is the foundation; stronger exceptional-algebra and physical claims must build on it with their own proofs.

**Paper 04b (Fano–Simplex Lift):** Paper 04b closes the foundational algebraic bridge that Paper 03 leaves open: the Peirce decomposition, Spin(8) triality, Fano incidence structure, and the exact distinction between closed algebraic facts and open physical interpretation. Paper 03 supplies the diagonal carrier; Paper 04b supplies the off-diagonal structure and the Boolean frame theorem.

**Historical divergence:** Older drafts of Paper 03 (03.25, 03.50, 03.75, 03_UPGRADED) made stronger claims about full triality, F4 action, and quark-face identification. These claims have been demoted to open obligations. The current paper is the honest, closed finite surface.

---

## Open Obligations

| ID | Disposition |
|----|-------------|
| 03.1 | Wire `verify_triality_surface` into the installable `cqe_engine.formal` interface. |
| 03.2 | Route the finite-reapplication guard for D4 tower and `G2 → F4` into NP-04/NP-08. |
| 03.3 | Add any stronger S3 group-ring and `J3` trace-2 proof as a separate theorem, not inside this local codec paper. |
| 03.4 | Reconcile axis naming between all chart-codec copies in the D drive. |
| 03.5 | Carry exact Paper 02 correction coordinates into the Paper 04 boundary repair formalism. |
| 03.6 | Prove full D4 triality automorphism theorem (route to NP-04 / exceptional-route papers). **External anchor:** Kollross 2025 (arXiv:2504.16513) derives E8 Lie bracket via octo-octonions; any FLCR E8 derivation must match or cite this result. |
| 03.7 | Prove full F4 action on `J3(O)` (route to NP-04). |
| 03.8 | Prove off-diagonal octonionic dynamics (separate theorem). |
| 03.9 | Physical quark-face identification and energy quantum calibration (route to calibration papers). |
| 03.10 | Product-scale cluster scheduling safety/liveness (product-layer, not a paper theorem). |
| 03.11 | The S3 annealing docstring claimed `(1,1,0)` requires 3 swaps; it requires 2. Correct the documentation. |

---

## Bibliography

[1] N. Barker, *CQE Paper 00 — Established Grounding and Axiom Contract*, `papers/active-rework/00_Established_Grounding_and_Axiom_Contract.md`, 2026. Defines the finite state space `S = {0,1}^3`, the shell grading, and the D/I/X claim-strength taxonomy.

[2] N. Barker, *CQE Paper 01 — LCR Chain Carrier*, `papers/active-rework/01_LCR_Chain_Carrier.md`, 2026. Supplies the reversal involution, shell counts, and the distinction between boundary address and boundary value.

[3] N. Barker, *CQE Paper 02 — Correction Surface*, `papers/active-rework/02_Correction_Surface.md`, 2026. Identifies the correction firing states `(0,1,0)` and `(1,1,0)` and proves the exact correction formula `corr = C ∧ ¬R`.

[4] `lattice_forge/octonion.py`, `lattice_forge/jordan_j3.py`, `lattice_forge/rule30.py`, `lattice_forge/f4_action.py`, `lattice_forge/d12_action.py`, CMPLX-PartsFactory-main packages. Substrate modules proving T1–T7, D12 chain, and annealing. Reapplied in Paper 03.

[5] `lattice_forge/block_d4.py`, `lattice_forge/block_tower.py`, `lattice_forge/g2_f4_t5_conjugate.py`, CMPLX-PartsFactory-main packages. Substrate modules for D4 block tower and exceptional conjugate. Reapplied in Paper 03.

[6] `product_converge/src/state/chart8.py` (historical), `nbarker2021/CMPLX-TMN-main` board atlases. Source of the D4 chart-atlas bijectivity construction. Reapplied and verified in Paper 03.

[7] R. D. Schafer, *An Introduction to Non-Associative Algebras*, Dover, 1995. Standard reference for octonion algebra and Jordan algebras.

[8] J. C. Baez, "The Octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Survey of octonion and exceptional Jordan algebra structure.

[9] N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. Reference for `J3(O)` and Peirce decomposition.

[10] J. H. Conway and D. A. Smith, *On Quaternions and Octonions*, A K Peters, 2003. Reference for octonion arithmetic and triality.
[11] N. Barker, *CQE Paper 04b — Fano–Simplex Lift: Incidence, Associator, and Closure in the LCR–Albert Carrier*, `papers/active-rework/04b_Fano_Simplex_Lift.md`, 2026. Closes the Boolean frame theorem, Peirce decomposition, Spin(8) triality, Fano incidence, and the exact boundary between closed algebra and open physical interpretation.
[12] A. Kollross, "E8 Lie bracket via octo-octonions," arXiv:2504.16513, 2025. Derives the E8 Lie bracket from octo-octonion commutators; external anchor for any FLCR E8 derivation.

---

## Conclusion

Paper 03 closes the finite local registration layer: one binary LCR state can be read without loss as an LCR triple, as a D4-style `(axis, sheet)` coordinate, and as a diagonal `J3(O)` carrier. The axis/sheet bijection is explicit and finite; the diagonal trace and idempotent properties are closed by direct computation; the Paper 02 correction coordinates are preserved. A stack of substrate receipts (T1–T7, D12, annealing, atlas, block tower) is bound to the paper as verified reapplications.

The guard is the point. This paper does not prove the full D4 triality automorphism, a full F4 action, off-diagonal octonionic dynamics, or any physical identification. It supplies the honest finite surface on which those later claims must stand. The distinction between what is closed here and what remains open is not a weakness; it is the architecture that keeps the corpus rigorous.
