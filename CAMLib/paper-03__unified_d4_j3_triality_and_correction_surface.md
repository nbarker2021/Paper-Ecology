# Paper 03: D4/J3 Triality Surface

**Domain:** Triality / Exceptional Algebra  
**Disposition:** `canon`  
**CAMLib Entry Date:** 2026-07-04  

---

## Content-Addressed Entries

### Claim 3.1: Local Triality Surface

- **Claim Text:** The map tau(L,C,R) = (axis(L,C,R), sheet(L,C,R), diag(L,C,R)) is a faithful three-language presentation of the eight binary LCR states. The axis/sheet part is a bijection from S to {0,1,2,3} x {0,1}. The diagonal part preserves shell as trace. The shell-2 states map to trace-2 diagonal idempotents.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-03__unified_d4_j3_triality_and_correction_surface.py`
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_triality_surface()`

### Claim 3.2: D4 Block Tower and Exceptional Conjugate Reapplication

- **Claim Text:** The local Paper 03 surface is bound to the substrate D4 block, D4 block tower, and G2 -> F4 T5 conjugate triple verifiers. This closes the paper-binding gap for those proven substrate mechanisms.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-03__unified_d4_j3_triality_and_correction_surface.py`
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_d4_block_tower_exceptional()`

### Claim 3.3: Algebra Foundation Stack

- **Claim Text:** The Paper 03 triality surface is paper-bound to the algebra-foundation receipts T1-T7: octonion axioms, J3(O) Jordan axioms, chart-to-J3(O) isomorphism, exact n=3 SU(3) Weyl closure, closure scale 3, identical trace-block closure, and the exact-rational 8x8 transition matrix.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-03__unified_d4_j3_triality_and_correction_surface.py`
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_algebra_foundation_T1_T4() / verify_su3_closure_T5_T7()`

### Claim 3.4: D12 and Atlas Dynamics

- **Claim Text:** The D12 idempotent chain, S3 triality annealing, and D4 chart-atlas bijectivity receipts are paper-bound to Paper 03. These receipts close the named finite group-action and atlas claims.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-03__unified_d4_j3_triality_and_correction_surface.py`
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_d12_idempotent_chain() / verify_triality_annealing() / verify_d4_atlas_bijectivity()`

---

## Cross-References

- [Paper 01: LCR Chain Carrier](paper-01__unified_lcr_kernel_and_chart.md)
- [Paper 02: Correction Surface](paper-02__unified_correction_surface_and_rule30_decomposition.md)
- [Paper 04: Boundary Repair](paper-04__unified_boundary_repair.md)
- [Paper 05: Oloid Path Carrier](paper-05__unified_oloid_path_carrier.md)
- [Paper 17: E6/E8 Error Correction Tower](paper-17__unified_e6_e8_error_correction_tower.md)

---

## Recovery Notes

3LSR Recovered: Axis/sheet bijective encoding, trace-2 idempotent diagonal carrier, D4 block tower substrate, T1-T7 algebra foundation stack, D12 idempotent chain, S3 annealing basin convergence.

---

## Disposition

This paper is classified as **`canon`**.
It is part of the core canonical paper series.


## Content-Addressed Entries (Harvester Pass 2026-07-04)

### Claim 3.1.1: Grid Bijective Encoding (axis/sheet analog)

- **Claim Text:** The multi-dimensional Grid class with dimensions=(4,2) encodes a bijection between the 8 binary LCR states and section IDs [0,7] via mixed-radix coordinate mapping. This is the axis/sheet analog for Theorem 3.1.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-03__triality_surface.py` (harvested from `unified_complex_t.py`)
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_grid_bijection()`

### Claim 3.3.1: Permutation Hash Bijection

- **Claim Text:** `hash_permutation` and `unhash_permutation` form a bijection between permutation tuples of 1..n and integers in [0, n**n - 1]. This is the canonical encoding for the algebra foundation stack (Theorem 3.3).
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-03__triality_surface.py`
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_hash_permutation_bijection()`

### Claim 3.4.1: De Bruijn Graph Adjacency Preservation

- **Claim Text:** `build_debruijn_graph` constructs a directed graph where every edge connects two (k-1)-mers that are consecutive in at least one valid permutation of n symbols. This preserves permutation adjacency for atlas dynamics (Theorem 3.4).
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-03__triality_surface.py`
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_debruijn_graph()`

### Claim 3.4.2: Golden Ratio Subdivision

- **Claim Text:** `calculate_golden_ratio_points` generates bounded, monotonic subdivision points based on phi = (1+sqrt(5))/2. This is the diagonal-carrier subdivision used in the D4 block tower and prodigal assembly scoring (Theorem 3.4).
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-03__triality_surface.py`
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_golden_ratio_points()`

### Claim 3.4.3: Permutation Validity and Enumeration

- **Claim Text:** `generate_permutations` enumerates all n! permutations of 1..n, and `is_valid_permutation` correctly identifies them. This closes the finite enumeration gap for the atlas dynamics verifier (Theorem 3.4).
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-03__triality_surface.py`
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_permutation_validity()`


## Content-Addressed Entries (Harvester Pass 2026-07-04)

### Claim 3.4.4: On-Demand Permutation Generation (Dynamic Assembly)

- **Claim Text:** `generate_permutations_on_demand` produces a filtered set of candidate permutation hashes for extending a superpermutation by scanning prodigal and hypothetical-prodigal sequences for prefix/suffix matches, excluding already-used permutations and loser k-mers. This is the canonical candidate generator for the D12 Atlas dynamics assembly loop (Theorem 3.4).
- **CAM Hash:** `sha256://29e9750d84e06cc364f51208df346fd2a5971536c4f58d19c48aefc48f089d71`
- **CodeLib Source:** `D:/CodeLib/paper-03__triality_surface.py` (harvested from `generation_code_n7_dynamic.py`)
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_generate_permutations_on_demand()`

### Claim 3.4.5: Hypothetical Prodigal Extension Generation

- **Claim Text:** `generate_permutations_on_demand_hypothetical` enumerates all permutations of `1..n` whose prefix or suffix matches a given k-mer, then filters out those containing high-weight loser k-mers (threshold > 5). This is the deterministic hypothetical-candidate generator used in the prodigal-extension phase of dynamic assembly (Theorem 3.4).
- **CAM Hash:** `sha256://d7cb0f9045c500cb3be2bde3009c1fba8d08eb76b8bad8e266229cbc77b60b9b`
- **CodeLib Source:** `D:/CodeLib/paper-03__triality_surface.py` (harvested from `generation_code_n7_dynamic.py`)
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_generate_permutations_on_demand_hypothetical()`

### Claim 3.4.6: Cyclic Distinctness of Superpermutations

- **Claim Text:** `is_cyclically_distinct` determines whether two strings are cyclically distinct by checking whether one is a substring of the double concatenation of the other. This is the canonical distinctness test for the D12 Atlas dynamics enumeration (Theorem 3.4), ensuring that collected minimal superpermutations are unique up to cyclic rotation.
- **CAM Hash:** `sha256://1238d85ae9ec927a95659f424bb4614b4aa59e2ad402ec5a89943d0518f3002c`
- **CodeLib Source:** `D:/CodeLib/paper-03__triality_surface.py` (harvested from `generation_code_n7_dynamic.py`)
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_is_cyclically_distinct()`

### Claim 3.4.7: Dynamic Assembly Data Initialization

- **Claim Text:** `initialize_data` sets up the six core data structures (`prodigal_results`, `winners`, `losers`, `meta_hierarchy`, `limbo_list`, `eput`) for the dynamic prodigal assembly loop. It converts initial prodigal sequences into `ProdigalResult` objects and returns the initial `next_prodigal_id` counter. This is the initialization substrate for the D12 Atlas dynamics (Theorem 3.4).
- **CAM Hash:** `sha256://7a162e6596bcc9ad1d7b7006fb8f43d6921b463e27e29581d0c49a60c7c4eea9`
- **CodeLib Source:** `D:/CodeLib/paper-03__triality_surface.py` (harvested from `generation_code_n7_dynamic.py`)
- **SQLLib Source:** `D:/SQLLib/paper-03__unified_d4_j3_triality_and_correction_surface.sql`
- **Status:** verified
- **Verifier:** `verify_initialize_data()`
