# Paper 05: Oloid Path Carrier

**Domain:** Path Carrier / Kinematics  
**Disposition:** `canon`  
**CAMLib Entry Date:** 2026-07-04  

---

## Content-Addressed Entries

### Claim 5.1: Rolling Path Carrier

- **Claim Text:** For every finite binary input stream, the rolling carrier produces a continuous trace of legal adjacent states. The trace preserves input order, maintains a binary head/tail dyad at every state, and can carry Paper 04 constraints as receipt payloads without treating the path as a straight-line jump.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-05__unified_oloid_path_carrier.py`
- **SQLLib Source:** `D:/SQLLib/paper-05__unified_oloid_path_carrier.sql`
- **Status:** verified
- **Verifier:** `verify_oloid_path_carrier()`

### Claim 5.2: Oloid Carrier Family Reapplication

- **Claim Text:** The substrate oloid mechanisms bound to this paper - rolling-contact kinematics, single-oloid octonionic grounding, the four-oloid D4 ring, and dual-path read-then-verify flow - each pass their finite verifier.
- **CAM Hash:** `sha256://...`
- **CodeLib Source:** `D:/CodeLib/paper-05__unified_oloid_path_carrier.py`
- **SQLLib Source:** `D:/SQLLib/paper-05__unified_oloid_path_carrier.sql`
- **Status:** verified
- **Verifier:** `verify_oloid_carrier_family()`

---

## Cross-References

- [Paper 01: LCR Chain Carrier](paper-01__unified_lcr_kernel_and_chart.md)
- [Paper 02: Correction Surface](paper-02__unified_correction_surface_and_rule30_decomposition.md)
- [Paper 03: D4/J3 Triality Surface](paper-03__unified_d4_j3_triality_and_correction_surface.md)
- [Paper 04: Boundary Repair](paper-04__unified_boundary_repair.md)
- [Paper 10: Master Receipt](paper-10__unified_t10_master_receipt.md)
- [Paper 12: CA Prediction Surface](paper-12__unified_ca_prediction_surface.md)


---

## Harvested Claims (from 53e25b8d_AGRM_refactored.py, 2026-07-04)

### Claim 5.3: AGRM Hierarchical Hash Table (Building→Floor→Room→Entry)

- **Claim Text:** The Multi-Dimensional Hamiltonian Golden-ratio Hash Table (MDHG) organizes entries into a hierarchical structure of Buildings → Floors (velocity tiers) → Rooms (buckets). Each entry carries metadata tracking hits, floor, room, and building assignment. The hierarchy supports φ-resizing, promotion/demotion between velocity tiers, and bounded tracing.
- **CAM Hash:** `sha256://d0f1d65d8a55ddee4897821287b8be6cb8602bf4543df3dc94c031161b4cdced`
- **CodeLib Source:** `D:/CodeLib/paper-05__unified_oloid_path_carrier.py`
- **SQLLib Source:** `D:/SQLLib/paper-05__unified_oloid_path_carrier.sql`
- **Status:** verified
- **Verifier:** `verify_agrm_hierarchy()`

### Claim 5.4: φ-Resizing and Load Balancing

- **Claim Text:** The MDHG hash table resizes according to a configurable policy: φ-scaling (golden ratio), doubling, or none. Resize triggers when load exceeds a target threshold. The hash table uses stable 64-bit FNV-1a hashing with power-of-two fast paths for room selection.
- **CAM Hash:** `sha256://a633c265473e602b94bf27a03079a8b00f2f66442eb3810900cd63caf1620cae`
- **CodeLib Source:** `D:/CodeLib/paper-05__unified_oloid_path_carrier.py`
- **SQLLib Source:** `D:/SQLLib/paper-05__unified_oloid_path_carrier.sql`
- **Status:** verified
- **Verifier:** `verify_hash_table_properties()`

### Claim 5.5: Co-Visit Routing (Shortcuts)

- **Claim Text:** The Shortcuts class learns co-visit patterns between rooms and uses them to bias placement via next-hop routing. This reduces churn by keeping frequently co-visited entries in adjacent or nearby rooms. Hamiltonian traversal variants (base, reverse, rot3, stride2, stride3, block_serp) provide deterministic floor traversal orders.
- **CAM Hash:** `sha256://34b057b8fa1dd2a131e1bb4fb9841923eb4af3b124de7838600cfe13793163bd`
- **CodeLib Source:** `D:/CodeLib/paper-05__unified_oloid_path_carrier.py`
- **SQLLib Source:** `D:/SQLLib/paper-05__unified_oloid_path_carrier.sql`
- **Status:** verified
- **Verifier:** `verify_routing_correctness()`

### Claim 5.6: Adaptive Promotion and Demotion

- **Claim Text:** Entries are promoted to higher-velocity floors when their hit count exceeds a threshold, and demoted after idle periods. Hit counts decay exponentially to prevent stale entries from monopolizing high-velocity tiers. The AGRMHierarchyController adapts thresholds across sweeps using empirical median and p90 hit statistics.
- **CAM Hash:** `sha256://bc5ad016256b07b3ab44232de01e9d7b5062478be83c6faef21fa0ebdc9f41cf`
- **CodeLib Source:** `D:/CodeLib/paper-05__unified_oloid_path_carrier.py`
- **SQLLib Source:** `D:/SQLLib/paper-05__unified_oloid_path_carrier.sql`
- **Status:** verified
- **Verifier:** `verify_agrm_hierarchy()` (promotion/demotion sub-checks)

### Claim 5.7: Integration with Rolling Carrier

- **Claim Text:** The UnifiedOloidPathCarrier integrates the rolling path carrier (Theorem 5.1) with the AGRM hierarchy, storing rolling states in the MDHG table and using head/tail dyads to guide shortcut routing. This demonstrates that the carrier family substrate can carry structured state payloads without violating continuity.
- **CAM Hash:** `sha256://2b1323e0e371a9825259c7a90bcb457f31c41038d2ca87a318c2e78d4c53346c`
- **CodeLib Source:** `D:/CodeLib/paper-05__unified_oloid_path_carrier.py`
- **SQLLib Source:** `D:/SQLLib/paper-05__unified_oloid_path_carrier.sql`
- **Status:** verified
- **Verifier:** `UnifiedOloidPathCarrier.verify_integration()`


---

## Harvested Claims (from Layout Memory and Data Persistence.py, 2026-07-04)

### Claim 5.8: LayoutMemory In-Memory Adjacency Index

- **Claim Text:** `LayoutMemory` maintains an in-memory adjacency index mapping `(kmer1, kmer2)` tuples to count, source provenance, and unit-distance records. It supports sequence ingestion via `add_sequence()` and rolling-carrier trace ingestion via `add_trace()`, which flattens `(sheet, phase, parity)` triples into a spatially indexed key space. The index provides count-based layout scoring, source tracking, and distance histograms without external persistence.
- **CAM Hash:** `sha256://` (to be computed after final file freeze)
- **CodeLib Source:** `D:/CodeLib/paper-05__unified_oloid_path_carrier.py`
- **SQLLib Source:** `D:/SQLLib/paper-05__unified_oloid_path_carrier.sql`
- **Status:** verified
- **Verifier:** `verify_layout_memory()`

### Claim 5.9: Spatial Indexing and Histogram Substrate

- **Claim Text:** The `LayoutMemory` adjacency histogram (`adjacency_histogram()`) and memory estimate (`memory_estimate()`) provide spatial indexing introspection for the oloid carrier family substrate. Keys are tuples of integer tuples, enabling multi-dimensional spatial indexing over rolling-carrier state traces. The histogram maps adjacency count frequencies and is non-negative for all entries.
- **CAM Hash:** `sha256://` (to be computed after final file freeze)
- **CodeLib Source:** `D:/CodeLib/paper-05__unified_oloid_path_carrier.py`
- **SQLLib Source:** `D:/SQLLib/paper-05__unified_oloid_path_carrier.sql`
- **Status:** verified
- **Verifier:** `verify_layout_indexing()`

### Claim 5.10: Layout Consistency and Multi-Source Provenance

- **Claim Text:** `LayoutMemory` preserves consistency: for every indexed pair, `count == len(distances)`. Overlapping sequences from different sources merge their source sets. Empty memory reports `size == 0` and `all_keys() == []`. These invariants hold for arbitrary sequences and rolling-carrier traces.
- **CAM Hash:** `sha256://` (to be computed after final file freeze)
- **CodeLib Source:** `D:/CodeLib/paper-05__unified_oloid_path_carrier.py`
- **SQLLib Source:** `D:/SQLLib/paper-05__unified_oloid_path_carrier.sql`
- **Status:** verified
- **Verifier:** `verify_layout_consistency()`

