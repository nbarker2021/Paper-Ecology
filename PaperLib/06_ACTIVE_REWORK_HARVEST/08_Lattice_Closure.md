# Paper 08 — Lattice Closure Template

**Status:** IPMC — internal physics map closed for the local lattice closure template, Niemeier/Leech enumeration, E8³ glue closure, T8 commutability tree, F2 bridge, E8 support stack, O2'' registry population, Weyl-E8 construction, and ATLAS unipotent-orbit spot-test. Rootless Leech landing, Gamma72 polarization, exact glue-coset representatives beyond E8³, and general uniqueness of closure templates remain open.

**Source papers:** CQE-paper-08, CQE-paper-08.25, CQE-paper-08.50.  
**Canonical formal paper:** `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-08/FORMAL_PAPER.md`.  
**Verifiers:** `verify_lattice_closure_template.py`, `verify_niemeier_leech_enumeration.py`, `verify_o7_niemeier_e8cubed_glue_closed.py`, `verify_t8_commutability_tree.py`, `verify_f2_bridge_unipotent_substrate.py`, `verify_e8_even_lattice.py`, `verify_e8_hemisphere_partition.py`, `verify_lattice_code_chain.py`, `verify_lattice_code_closure.py`, `verify_o2pp_registry_populated.py`, `verify_o1_weyl_e8_construction_closed.py`, `verify_atlas_unipotent_orbits_real_data.py`, `verify_glm_riemann_zeta_gap_anchor.py`.

---

## Abstract

Paper 08 formalizes the lattice closure template used by the CQECMPLX suite after the discrete-continuous bridge. The paper closes a substantial window of mathematical results:

1. **Local lattice closure template:** The code chain `1 → 3 → 7 → 8 → 24 → 72` with powered terminal `1²=1, 3²=9, 7²=49, 8×9=72` is a verified closure scaffold. Each rung is backed by finite combinatorial checks: Fano/Hamming identity at dimension 7, extended Hamming self-duality at dimension 8, Golay ingredients and `24 = 3×8` at dimension 24, and the Nebe 72 sheet bound.

2. **Niemeier/Leech enumeration:** Deterministic selectors, E8³ carriers, Leech type-1/2/3 orbits, and the Nebe 72 contract are paper-bound. O7 is closed for `Niemeier:E8³` as the exact zero-coset/identity-glue terminal.

3. **T8 commutability tree:** Eight canonical F4 → Niemeier terminal paths are verified, each returning `yes_with_template_glue`.

4. **F2 bridge and E8 support:** The F2 Majorana Arf bridge, E8 unipotent orbits, E8 even lattice (240 roots), and hemisphere partition are paper-bound.

5. **Registry population:** O2'' is populated by tool unison with 314 accepted facts. O1 (Weyl-E8 construction) is closed.

6. **External validation:** The suite's exceptional-group constants are spot-tested against the published ATLAS of Lie Groups unipotent-orbit database.

The guard is extensive: rootless Leech landing, Gamma72 polarization, exact glue-coset representatives beyond E8³, and the uniqueness of the closure chain are all left as explicit audit boundaries.

### Keywords

Lattice closure; Hamming code; Fano plane; extended Hamming; E8; Golay code; Leech lattice; Niemeier lattice; Nebe 72; Gamma72; T8 commutability; F2 bridge; Weyl group; ATLAS unipotent orbits; registry population; CQECMPLX receipts.

---

## Claim Ledger

| ID | Claim | Tag | Evidence | Boundary |
|----|-------|-----|----------|----------|
| 08.1 | The `(7,4,3)` Hamming code has 16 codewords, min weight 3, and its 7 weight-3 supports are the Fano-plane lines. | [D] | `verify_lattice_closure_template.py`; `lattice_closure_template_receipt.json` (8/8) | Finite combinatorial check |
| 08.2 | The `(8,4,4)` extended Hamming code has 16 codewords, min weight 4, all weights divisible by 4, and is self-dual. | [D] | Same verifier | Finite combinatorial check |
| 08.3 | The Golay code has 12 generator rows, weights divisible by 4, zero orthogonality errors, and `24 = 3×8` carrier geometry. | [D] | Same verifier | Finite combinatorial check |
| 08.4 | The powered chain satisfies `1²=1, 3²=9, 7²=49, 8×9=72`, with sheet bound `K=9`. | [D] | Same verifier | Finite arithmetic |
| 08.5 | The Gamma72 contract checks 260 payloads with exact three-sheet round trips. | [D] | Same verifier | Finite transport check |
| 08.6 | Leech landing, Gamma72 polarization, and uniqueness of the closure chain are rejected as overclaims. | [D] | Same verifier | Falsifier |
| 08.7 | Niemeier/Leech enumeration: deterministic selectors, E8³ carriers, Leech type-1/2/3 orbits, and Nebe 72 contract pass. | [D] | `verify_niemeier_leech_enumeration.py`; `niemeier_leech_enumeration_receipt.json` (6/6) | Reapplication of proven substrate |
| 08.8 | `leech_landing_proved` remains `false`; exact glue-coset representatives at the final edge remain pending. | [D] | Same verifier | Honesty guard |
| 08.9 | O7 exact `Niemeier:E8³` glue closes as the single zero coset `{0}` with identity glue. | [D] | `verify_o7_niemeier_e8cubed_glue_closed.py`; `o7_niemeier_e8cubed_glue_closed_receipt.json` (7/7) | E8 unimodularity composition |
| 08.10 | E8³ has 720 roots (norm 2), distinguishing it from the rootless Leech case. | [D] | Same verifier | Root count |
| 08.11 | Eight canonical F4 → Niemeier terminal paths return `yes_with_template_glue` and match the historical T8 table. | [D] | `verify_t8_commutability_tree.py`; `t8_commutability_tree_receipt.json` (9/9) | Finite seed-ledger theorem |
| 08.12 | All eight terminals are distinct; every path starts at F4 and ends at the requested target. | [D] | Same verifier | Path completeness |
| 08.13 | Exact glue-coset representatives remain outside the T8 claim. | [D] | Same verifier | Honesty guard |
| 08.14 | The F2 Majorana Arf bridge, E8 unipotent orbit tables, and substrate identity map pass. | [D] | `verify_f2_bridge_unipotent_substrate.py`; `f2_bridge_unipotent_substrate_receipt.json` (3/3) | Reapplication of proven substrate |
| 08.15 | O2'' is advanced by the F2 algebraic core, not fully discharged across the umbrella. | [D] | Same verifier | Scope boundary |
| 08.16 | E8 has exactly 240 roots: 112 integer + 128 half-integer, minimum norm 2, closed under addition, Cartan determinant 1. | [D] | `verify_e8_even_lattice.py`; `e8_even_lattice_receipt.json` (10/10) | E8Forge reapplication |
| 08.17 | E8 roots split into 120 antipodal pairs with a clean 120/120 hemisphere partition. | [D] | `verify_e8_hemisphere_partition.py`; `e8_hemisphere_partition_receipt.json` (5/5) | Hemisphere reapplication |
| 08.18 | The PFC-2 arithmetic `120 + 13 + 4 = 137` is recorded without promoting physical fine-structure claims. | [I] | Same verifier | Named arithmetic; physical identification is external bridge |
| 08.19 | The lattice code chain `1→3→7→8→24→72` passes all checks. | [D] | `verify_lattice_code_chain.py`; `lattice_code_chain_receipt.json` (6/6) | Reapplication |
| 08.20 | The lattice code closure `[1,3,7,21,137]` with CRT residue `119 mod 153` passes. | [D] | `verify_lattice_code_closure.py`; `lattice_code_closure_receipt.json` (10/10) | AuthenticaForge reapplication |
| 08.21 | O2'' registry is populated by 314 accepted facts with 0 rejections across 4 validators. | [D] | `verify_o2pp_registry_populated.py`; `o2pp_registry_populated_receipt.json` (6/6) | Tool unison |
| 08.22 | O1 Weyl-E8 construction: 8 simple reflections are involutions, satisfy Coxeter relations, act transitively on 240 roots, order 696,729,600. | [D] | `verify_o1_weyl_e8_construction_closed.py`; `o1_weyl_e8_construction_closed_receipt.json` (7/7) | E8Forge composition |
| 08.23 | ATLAS unipotent-orbit data matches suite constants: G2 max=12, F4 max=48, E6 max=72, E7 max=126, E8 max=240. | [D] | `verify_atlas_unipotent_orbits_real_data.py`; `atlas_unipotent_orbits_real_data_receipt.json` (36/36) | External database spot-test |
| 08.24 | Riemann zeta gap = 1/3 exact fraction, structurally anchored to E8 hemisphere. | [I] | `verify_glm_riemann_zeta_gap_anchor.py`; `riemann_zeta_gap_anchor_receipt.json` (6/6) | Structural argument; analytic bridge open |
| 08.25 | Rootless Leech landing is proven. | [X] | `leech_landing_proved = false` | Requires explicit glue-action verifier |
| 08.26 | Gamma72 polarization action is proven. | [X] | `polarization_matrices_supplied = false` | Requires Hermitian polarization matrices |
| 08.27 | Exact glue-coset representatives for nontrivial Niemeier terminals are closed. | [X] | `pending_invariants` recorded | Separate obligation |
| 08.28 | The closure chain is the only possible one. | [X] | Not claimed | Paper 08 proves this chain as the active template |
| 08.29 | Physical `1/137` identification is a closed theorem. | [X] | Not claimed | PFC-2 arithmetic only; physical hypothesis is external bridge |
| 08.30 | Anti-counterfeit strength is a lattice theorem. | [X] | Not claimed | Unforgeability rests on HMAC/product layer |

---

## Definitions

**Definition 8.1 (Lattice closure template).** A lattice closure template is a sequence of finite code or lattice objects that lets a local state carrier be lifted into a larger transport frame while preserving the proof boundary of every step.

**Definition 8.2 (Local certified fact).** A local certified fact is a claim checked at a fixed dimension by a finite verifier.

**Definition 8.3 (Global landing claim).** A global landing claim is a stronger statement that a local certified fact has been glued into a terminal lattice object such as the rootless Leech lattice or a Gamma72 action. Paper 08 does not count those landings as proved unless the corresponding glue or polarization verifier is present.

**Definition 8.4 (Hamming code).** The `(7,4,3)` Hamming code is the binary linear code of length 7, dimension 4, and minimum distance 3. Its 16 codewords have weight distribution `{0:1, 3:7, 4:7, 7:1}`.

**Definition 8.5 (Extended Hamming code).** The `(8,4,4)` extended Hamming code is the self-dual doubly-even binary code obtained by adding an overall parity bit to the `(7,4,3)` Hamming code. It has 16 codewords, minimum weight 4, and weight distribution `{0:1, 4:14, 8:1}`.

**Definition 8.6 (E8 root lattice).** The E8 root lattice is the even unimodular lattice in 8 dimensions generated by the 240 roots of the E8 Lie algebra. It has minimum norm 2 and determinant 1.

**Definition 8.7 (Golay code).** The binary Golay code is the `[24,12,8]` linear code with 12 generator rows, generator weights divisible by 4, and zero generator-pair orthogonality errors.

**Definition 8.8 (Niemeier lattice).** A Niemeier lattice is an even unimodular lattice in 24 dimensions with roots. The `Niemeier:E8³` lattice is the direct sum of three E8 root lattices.

**Definition 8.9 (Leech lattice).** The Leech lattice is the unique even unimodular lattice in 24 dimensions with no roots (minimum norm 4).

**Definition 8.10 (Sheet bound).** The sheet bound is the maximum orbit distance expressible inside the current sheet before a new anchor must be introduced. The Paper 08 verifier records `K = 9`.

---

## Theorems and Proofs

**Theorem 8.1 (Local Lattice Closure Template).** The finite code chain `(1, 3, 7, 8, 24)` and powered terminal `72 = 8×9` provide a verified local closure template for CQECMPLX transport. Every admitted rung is backed by a finite combinatorial check, and every unproved global landing is preserved as an explicit proof boundary.

*Proof.* The verifier establishes five local facts:

1. **Fano/Hamming identity (dimension 7):** The `(7,4,3)` Hamming code has 16 codewords, minimum weight 3, and weight distribution `{0:1, 3:7, 4:7, 7:1}`. Exactly seven weight-3 codewords exist, and their supports are the seven lines of the Fano plane. Therefore the Hamming code, Fano plane, and octonion-imaginary incidence structure are identified at dimension 7. ∎

2. **Extended Hamming/E8 seed (dimension 8):** The `(8,4,4)` extended Hamming code has 16 codewords, minimum weight 4, weight distribution `{0:1, 4:14, 8:1}`, all weights divisible by 4, and pairwise self-orthogonality. Therefore it is a self-dual doubly-even binary code and supplies the Construction A seed for the E8 root lattice. ∎

3. **Golay ingredients (dimension 24):** The Golay code has 12 generator rows, generator weights divisible by 4, zero generator-pair orthogonality errors, and the carrier geometry `24 = 3×8` (three copies of the 8-dimensional D4 chart). Therefore it supplies the binary Golay ingredients and three-copy D4 carrier geometry needed for Leech-facing work. ∎

4. **Powered chain (dimension 72):** The chain satisfies `1² = 1`, `3² = 9`, `7² = 49`, and `8×9 = 72`. The verifier records `sheet_K_bound = 9` and the dimension-72 extremal minimum norm calculation `2·floor(72/24) + 2 = 8`. ∎

5. **Gamma72 contract:** The verifier checks 260 payloads and confirms exact round trips into three Leech sheets. It records `polarization_matrices_supplied = false` and `gamma72_landing_proved = false`. Therefore the transport is verified but the landing is not claimed. ∎

Together these checks prove the local closure template and its audit boundary. The theorem does not require the global Leech or Gamma72 landing to be closed; instead, it proves that the local lattice closure surface is valid and that unproved landings remain visible. ∎

**Theorem 8.2 (Niemeier/Leech Enumeration Boundary).** The Niemeier/Leech enumeration verifier closes the deterministic selector, E8³ carrier, Leech type-1/2/3 orbit, and Nebe 72 contract checks. It advances O7 but does not close the exact integer-vector glue-coset representatives at the final edge or promote a rootless Leech landing as proved.

*Proof.* The verifier `verify_niemeier_leech_enumeration.py` runs the enumerated-glue and Nebe-72 substrate checks. The selector contract is deterministic, block orders are permutations, all carriers are E8³, the Leech type-1/2/3 orbit checks pass, and the Nebe 72 contract passes. The receipt explicitly records `leech_landing_proved = false` and pending invariants for `rank_24`, `even`, `unimodular`, `root_count_norm2_zero`, and `minimum_norm_4`. Therefore the enumeration layer is paper-bound as a partial O7 resolution, not as a hidden proof of the full landing. ∎

**Theorem 8.2a (O7 Exact E8³ Glue Closure).** The exact `Niemeier:E8³` glue-coset obligation is closed for the E8-cubed terminal: E8 is even unimodular with determinant 1, so `E8³` is even unimodular in dimension 24 with trivial discriminant group. The exact Construction A glue cosets are the single zero coset `{0}`, and the terminal embedding closes with identity glue.

*Proof.* The E8 Cartan determinant is 1, so each E8 block is unimodular and self-dual. The direct sum of three unimodular blocks has determinant `1³ = 1`. A trivial discriminant group has exactly one coset, the zero coset, so the exact Construction A glue for `Niemeier:E8³` is `{0}` and the embedding closes with identity glue. The verifier also checks the expected 720-root count, distinguishing this terminal from the rootless Leech case (which has no roots). ∎

**Theorem 8.3 (T8 Commutability Tree).** A rebuilt lattice-forge seed ledger contains eight canonical F4 → Niemeier terminal paths. Each queried target returns `yes_with_template_glue`, the path matches the historical path table, and all eight terminals are distinct.

*Proof.* The verifier builds a temporary seed database, queries `Forge.can_close("F4", target)` for the eight named terminals, and checks that every answer is `yes_with_template_glue`. Each returned path starts at `F4`, ends at the requested terminal, matches the historical T8 path table, and uses the expected trunk nodes `G2×F4`, `E8`, `E6`, `E7`, and `D4`. The resulting theorem is a finite seed-ledger path theorem. Because every answer is `template_glue`, exact glue representatives remain outside the claim. ∎

**Theorem 8.4 (F2 Bridge, Unipotent Orbits, and Substrate Map).** The F2 Majorana Arf bridge, E8 unipotent orbit tables, and substrate identity map verifiers are paper-bound to Paper 08. This advances O2'' by closing the algebraic F2 governance core.

*Proof.* The verifier runs `f2_majorana`, `unipotent_orbits`, and `substrate_map`. The F2 Majorana row verifies the quadratic-form/Arf-invariant governance core and edge-glue isometry. The unipotent orbit and substrate-map rows verify the supporting E8 orbit table and identity map. Since the receipt explicitly leaves registry-wide population outside scope, the paper records O2'' as advanced by a closed algebraic core, not fully discharged. ∎

**Theorem 8.5 (E8 and Lattice-Code Support Stack).** The E8 arithmetic, hemisphere partition, lattice-code chain, and AuthenticaForge closure verifiers are paper-bound as the support stack under the closure template. They prove exact finite lattice facts: the 240-root E8 frame, the 120/120 antipodal hemisphere split, the `1→3→7→8→24→72` code chain, and the `[1,3,7,21,137]` closure identity.

*Proof.* Four support verifiers are bound:

- `verify_e8_even_lattice.py` checks the exact E8 root enumeration in doubled integer coordinates: 240 roots (112 integer + 128 half-integer), minimum norm 2, root-addition closure, E8 Cartan determinant 1, and Weyl-order arithmetic.

- `verify_e8_hemisphere_partition.py` confirms antipodal pairing, a clean 120/120 hemisphere split, and the arithmetic `120 + 13 + 4 = 137`, while explicitly leaving the geometric boundary-vignette and fine-structure hypotheses unproved.

- `verify_lattice_code_chain.py` reapplies the Hamming/Fano, extended Hamming/E8, Golay, parameter-chain, and powered-chain verifiers as the T8-family code spine.

- `verify_lattice_code_closure.py` binds the AuthenticaForge `[1,3,7,21,137]` closure identity and its CRT residue `119 mod 153` while quarantining product-side unforgeability claims.

All checks pass. The theorem does not promote the physical `1/137` hypothesis, rootless Leech landing, Gamma72 polarization, or anti-counterfeit strength claims. ∎

**Theorem 8.6 (O2'' Registry Population by Tool Unison).** The `T_F2_BRIDGE` contributions registry is populated across the current core proof surface by four deterministic validators: `f2_arf`, `lucas_recurrence`, `rule30_decomposition`, and `f2_edge_glue`. This exercises the O2'' registry population procedure with 314 accepted durable facts and zero rejections.

*Proof.* The verifier `verify_o2pp_registry_populated.py` installs the four registry validators, proposes durable facts from the F2 Arf bridge, Lucas recurrence, Rule 30 decomposition, and edge-glue identity layers, and records 314 accepted facts with zero rejections. The receipt converts O2'' from an unpopulated registry obligation into an exercised registry procedure over the current paper-bound proof surface. It does not claim that every future fact has already been populated. ∎

**Theorem 8.7 (O1 Weyl-E8 Construction).** The Weyl group `W(E8)` is constructed from the 8 simple reflections generated by E8Forge's 240 roots. The reflections are involutions, satisfy the E8 Coxeter relations, act transitively on the 240 roots (single orbit), and have order `4!·6!·8! = 696,729,600`. A bounded sub-table demonstrates the lookup construction procedure.

*Proof.* The verifier `verify_o1_weyl_e8_construction_closed.py` composes E8Forge reflections. It checks that the 8 simple reflections permute the 240 roots, are involutions, satisfy the E8 Coxeter relations, act transitively (single orbit), and produce the correct Weyl order. A bounded sub-table of 5000 entries is constructed to demonstrate the procedure. The full 696,729,600-element table is a storage decision, not a missing capability. ∎

**Theorem 8.8 (ATLAS Unipotent Orbit Spot-Test).** The suite's exceptional-group constants are spot-tested against the published ATLAS of Lie Groups unipotent-orbit database. For each of `G2, F4, E6, E7, E8`, the published orbit counts and maximum orbit dimensions match the suite's internal constants.

*Proof.* The verifier `verify_atlas_unipotent_orbits_real_data.py` loads the real records from the ATLAS database and confirms: G2 has 5 orbits (max dim 12), F4 has 16 orbits (max dim 48), E6 has 21 orbits (max dim 72), E7 has 45 orbits (max dim 126), E8 has 70 orbits (max dim 240). It checks that `max_dim = dim(G) - rank(G)` for each group. It then binds these external numbers to the suite's internal constants: E8 max orbit 240 = E8 root count, E6 max orbit 72 = code-tower top/Nebe Gamma72, F4 max orbit 48 = F4/J3(O) trace substrate, G2 max orbit 12 = G2 route stage. All 36 checks pass. This is a structural match between published data and documented suite constants; no extension of unipotent/Jordan/lattice theory is claimed. ∎

**Theorem 8.9 (Riemann Zeta Gap Anchor).** The Riemann zeta gap is structurally anchored to `1/3` exact fraction via the E8 hemisphere: `120 / (3×120) = 1/3`, where 120 is the dimension of `Spin(16)` and the number of E8 roots in one hemisphere.

*Proof.* The verifier `verify_glm_riemann_zeta_gap_anchor.py` checks the structural argument: the seam 33% firing rate equals `1/3`, the E8 hemisphere has 120 roots, `Spin(16)` has dimension 120, and the gap from E8 is `120/(3×120) = 1/3`. The spectral weight is positive and bilateral symmetry forces the critical line. All 6 checks pass. The analytic bridge from discrete E8 to continuous operator remains open. The physical `1/137` identification is not claimed as a closed theorem. ∎

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Status |
|----------|---------|--------|--------|
| `verify_lattice_closure_template.py` | `lattice_closure_template_receipt.json` | 8 | pass |
| `verify_niemeier_leech_enumeration.py` | `niemeier_leech_enumeration_receipt.json` | 6 | pass |
| `verify_o7_niemeier_e8cubed_glue_closed.py` | `o7_niemeier_e8cubed_glue_closed_receipt.json` | 7 | pass |
| `verify_t8_commutability_tree.py` | `t8_commutability_tree_receipt.json` | 9 | pass |
| `verify_f2_bridge_unipotent_substrate.py` | `f2_bridge_unipotent_substrate_receipt.json` | 3 | pass |
| `verify_e8_even_lattice.py` | `e8_even_lattice_receipt.json` | 10 | pass |
| `verify_e8_hemisphere_partition.py` | `e8_hemisphere_partition_receipt.json` | 5 | pass |
| `verify_lattice_code_chain.py` | `lattice_code_chain_receipt.json` | 6 | pass |
| `verify_lattice_code_closure.py` | `lattice_code_closure_receipt.json` | 10 | pass |
| `verify_o2pp_registry_populated.py` | `o2pp_registry_populated_receipt.json` | 6 | pass |
| `verify_o1_weyl_e8_construction_closed.py` | `o1_weyl_e8_construction_closed_receipt.json` | 7 | pass |
| `verify_atlas_unipotent_orbits_real_data.py` | `atlas_unipotent_orbits_real_data_receipt.json` | 36 | pass |
| `verify_glm_riemann_zeta_gap_anchor.py` | `riemann_zeta_gap_anchor_receipt.json` | 6 | pass |

**Total checks:** 119/119 pass.

---

## Hand Reconstruction

1. Verify the `(7,4,3)` Hamming code: 16 codewords, weight distribution `{0:1, 3:7, 4:7, 7:1}`, 7 weight-3 supports = Fano lines.
2. Verify the `(8,4,4)` extended Hamming code: 16 codewords, all weights divisible by 4, self-dual.
3. Verify the Golay code: 12 generators, weights divisible by 4, zero orthogonality errors, `24 = 3×8`.
4. Check the powered chain: `1²=1, 3²=9, 7²=49, 8×9=72`, sheet bound `K=9`.
5. Confirm Gamma72 transport of 260 payloads into 3 Leech sheets without claiming landing.
6. Verify Niemeier enumeration: deterministic selectors, E8³ carriers, Leech type-1/2/3 orbits, Nebe 72 contract.
7. Verify O7 E8³ glue: Cartan det=1, trivial discriminant, zero coset `{0}`, identity glue, 720 roots.
8. Query the T8 seed ledger for 8 F4 → Niemeier paths and confirm `yes_with_template_glue`.
9. Verify F2 bridge: Arf invariants, edge-glue isometry, unipotent orbit tables, substrate map.
10. Verify E8: 240 roots (112+128), min norm 2, Cartan det 1, Weyl order 696,729,600.
11. Verify E8 hemisphere: 120 antipodal pairs, 120/120 split, `120+13+4=137` arithmetic.
12. Verify lattice code chain: `1→3→7→8→24→72` and `[1,3,7,21,137]` closure.
13. Populate O2'' registry: 4 validators, 314 facts, 0 rejections.
14. Verify O1 Weyl-E8: 8 reflections, involutions, Coxeter relations, transitive action.
15. Spot-test ATLAS data: confirm orbit counts and max dimensions match suite constants.
16. Verify Riemann gap anchor: `1/3` structural argument from E8 hemisphere.

---

## Falsifiers and Rejected Claims

| Rejected Claim | Reason |
|---------------|--------|
| "Golay ingredients alone prove the rootless Leech landing." | Rejected. `leech_landing_proved = false`. The Golay code supplies ingredients but the landing requires an explicit glue-action verifier. |
| "Three Leech-sheet round trips prove the Gamma72 polarization action." | Rejected. `polarization_matrices_supplied = false`. Transport is verified; polarization is not. |
| "The chain proves that no other closure template exists." | Rejected. Paper 08 proves this chain as the suite's active template, not as the unique possible one. |
| "The PFC-2 arithmetic `120+13+4=137` proves the physical fine-structure constant." | Rejected. The arithmetic is exact; the physical identification is a hypothesis, not a theorem. |
| "Anti-counterfeit strength is a lattice theorem." | Rejected. Lattice closure is public math; unforgeability rests on the HMAC/product layer. |
| "Exact glue-coset representatives for all Niemeier terminals are closed." | Rejected. Only `Niemeier:E8³` is closed (zero coset). Nontrivial terminals remain open. |
| "The full 696,729,600-element Weyl table is materialized." | Rejected. A bounded sub-table demonstrates the construction; the full table is a storage decision. |
| "The Riemann zeta gap anchor proves the Riemann Hypothesis." | Rejected. The structural argument anchors the gap to `1/3`; the analytic bridge remains open. |

---

## Relation to Prior and Later Papers

**Papers 01–07:** Build the local carrier, correction surface, coordinate surface, boundary repair, path carrier, causal code, and sample-preserving bridge. Paper 08 is the first closure-template paper: it gives that local machinery a high-dimensional target ladder without letting the target ladder overclaim.

**Paper 17 (Leech Lattice):** The 24-dimensional bridge from Paper 07 connects to LeechForge, which constructs the Leech lattice exactly. Paper 08 addresses the code ingredients and E8³ carrier; Paper 17 constructs the lattice.

**Paper 28:** The code tower `{1,3,7,8,24,72}` is the top of the lattice-code chain, linking to later exceptional-group work.

**CMPLX-R30-main/PROOF/theorems:** O7 is closed for `Niemeier:E8³`; O2'' is populated; O1 is closed. Remaining obligations (exact glue for nontrivial terminals, rootless Leech landing, Gamma72 polarization) remain in the open obligations registry.

---

## Open Obligations

| ID | Disposition |
|----|-------------|
| 08.1 | Close exact glue-coset representatives for nontrivial Niemeier or Leech-facing terminals. |
| 08.2 | Prove rootless Leech landing with an explicit glue-action verifier setting `leech_landing_proved = true`. |
| 08.3 | Prove Gamma72 landing with selected Hermitian polarization matrices. |
| 08.4 | Build cold-start map from arbitrary depth to Niemeier/Leech fingerprint. |
| 08.5 | Prove or refute uniqueness of the closure chain as the only possible template. |
| 08.6 | Prove geometric 13-boundary count or supply independent physical `1/137` identification. |
| 08.7 | Close anti-counterfeit strength as a product-layer HMAC claim, not a lattice theorem. |
| 08.8 | Materialize the full Weyl-E8 lookup table (storage decision, not missing capability). |
| 08.9 | Close analytic bridge from discrete E8 to continuous operator for Riemann zeta gap. |
| 08.10 | Wire all Paper 08 verifiers into `cqe_engine.formal`. |
| 08.11 | Extend ATLAS spot-test to additional exceptional-group data. |
| 08.12 | Add domain examples (coding theory, sphere packing, cryptography) after the formal schema is stable. |

---

## Bibliography

[1] N. Barker, *CQE Paper 01–07*, `papers/active-rework/`, 2026. The chain of local papers that Paper 08 lifts into high-dimensional lattice closure.

[2] `lattice_forge.lattice_codes`, `lattice_forge.nebe_gamma72`, `lattice_forge.f2_majorana`, `lattice_forge.unipotent_orbits`, `lattice_forge.substrate_map`, CMPLX-PartsFactory-main. Substrate modules for lattice codes, F2 bridge, and unipotent orbits. Reapplied in Paper 08.

[3] `E8Forge`, `LeechForge`, `MDHGForge`, `TriadForge`, CMPLX-R30-main/PROOF/src. Forge family proving E8, Leech, and triadic structures. Reapplied in Paper 08.

[4] J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed., Springer, 1999. Standard reference for E8, Leech, Golay, and Niemeier lattices.

[5] N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. Reference for exceptional algebra structure.

[6] Atlas of Lie Groups, `liegroups.org`; Spaltenstein/Carter tables. External database for unipotent orbit counts and dimensions. Spot-tested in Paper 08.

[7] J. H. Conway, "A Characterization of Leech's Lattice," *Invent. Math.* 7 (1969), 137–142. Reference for the uniqueness of the Leech lattice.

[8] G. Nebe, "Some Cyclo-Quaternionic Lattices," *J. Algebra* 234 (2000), 99–121. Reference for the Nebe 72-dimensional lattice.

[9] F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes*, North-Holland, 1977. Reference for Hamming and Golay codes.

[10] J. C. Baez, "The Octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Reference for octonion and exceptional algebra structure.

---

## Conclusion

Paper 08 closes the first eight-paper window by giving CQECMPLX a verified lattice closure scaffold. The proof is not that every global lattice landing has been solved. The proof is sharper: local closure facts are certified, their transport role is explicit, and every stronger landing remains visible as an audit boundary.

The code chain `1 → 3 → 7 → 8 → 24 → 72` is backed by finite combinatorial checks at every rung. The Fano/Hamming identity, extended Hamming self-duality, Golay ingredients, and Nebe sheet bound are all closed. The Niemeier/Leech enumeration, E8³ glue closure, T8 commutability tree, F2 bridge, E8 support stack, and O2'' registry population are all paper-bound. The Weyl-E8 construction and ATLAS spot-test provide external validation.

The honesty guard is the point: rootless Leech landing, Gamma72 polarization, exact glue beyond E8³, and the uniqueness of the chain are all left open. The arithmetic `120 + 13 + 4 = 137` is exact but does not prove the physical fine-structure constant. The Riemann gap anchor is structural but does not prove the Hypothesis. This is the architecture that keeps the corpus rigorous: close what can be closed, name what remains open, and never let a local fact masquerade as a global theorem.
