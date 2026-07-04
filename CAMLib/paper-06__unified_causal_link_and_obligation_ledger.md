# Paper 6: Causal Link / Obligation Ledger

**Domain:** Causal Link / Obligation Ledger  
**Disposition:** `canon`  
**CAMLib Entry Date:** 2026-07-04  

---

## Content-Addressed Entries

### Claim 06.1: Typed Causal Edge
- **Claim Text:** Every causal edge has the five required fields: `source`, `target`, `edge_type`, `receipt`, `status`.
- **CAM Hash:** `sha256:claim06_1`
- **CodeLib Source:** `D:/CodeLib/paper-06__unified_causal_link_and_obligation_ledger.py`
- **SQLLib Source:** `D:/SQLLib/paper-06__unified_causal_link_and_obligation_ledger.sql`
- **Status:** `harvested`
- **Verifier:** `verify_causal_code.py`; `causal_code_receipt.json` (7/7)

### Claim 06.6: Rule 30 Decomposition
- **Claim Text:** Rule 30 decomposes exactly as Rule90 ⊕ (C ∧ ¬R) at the truth table.
- **CAM Hash:** `sha256:claim06_6`
- **Status:** `harvested`
- **Verifier:** `verify_rule90_lucas_decomposition.py`; `rule90_lucas_decomposition_receipt.json` (7/7)

### Claim 06.13: Triadic Keystone
- **Claim Text:** The Rule 90/Pascal/Sierpinski structure has exactly 3^k live cells over 2^k rows.
- **CAM Hash:** `sha256:claim06_13`
- **Status:** `harvested`
- **Verifier:** `verify_triadic_keystone.py`; `triadic_keystone_receipt.json` (10/10)

### Claim 06.23: Singer Cycle Fano Automorphism
- **Claim Text:** The Singer cycle in GL(3, F_2) is an explicit order-7 Fano automorphism.
- **CAM Hash:** `sha256:claim06_23`
- **Status:** `harvested`
- **Verifier:** Finite group computation

### Claim 06.28: MannyAI Daemon Ring
- **Claim Text:** The MannyAI daemon loop (`src/daemon/ring.py`, 12,570 bytes) implements a causal ring architecture for agent lifecycle management with board state and conservation delta-phi.
- **CAM Hash:** `sha256:claim06_28`
- **Status:** `harvested`
- **Verifier:** `MannyAI/src/daemon/ring.py` (2026-07-03); `SERVER_TEST_REPORT.md` (2026-07-01)

### Claim 06.29: SpeedLight Dedup
- **Claim Text:** The SpeedLight deduplication engine (`src/speedlight/speedlight.py`, 9,409 bytes) eliminates redundant causal computations by coin-economy curation.
- **CAM Hash:** `sha256:claim06_29`
- **Status:** `harvested`
- **Verifier:** `MannyAI/src/speedlight/speedlight.py` (2026-07-03); `PLAN_GLM_BODY_AGENTS_MOUTH.md` (2026-07-03)

### Claim 06.30: MCP Plugin System
- **Claim Text:** The MannyAI MCP plugin system (`src/manny_mcp/plugins/`, 4,831 bytes `__init__.py`) provides 45+ tools for causal link management across the FLCR substrate.
- **CAM Hash:** `sha256:claim06_30`
- **Status:** `harvested`
- **Verifier:** `MannyAI/src/manny_mcp/plugins/__init__.py` (2026-07-04); `PLAN_GLM_BODY_AGENTS_MOUTH.md` (2026-07-03)

---

## Cross-References
- [Paper 01: LCR Chain Carrier](paper-01__unified_lcr_kernel_and_chart.md)
- [Paper 02: Correction Surface](paper-02__unified_correction_surface_and_rule30_decomposition.md)
- [Paper 03: D4 J3 Triality Surface](paper-03__unified_d4_j3_triality_and_correction_surface.md)
- [Paper 05: Oloid Path Carrier](paper-05__unified_oloid_path_carrier.md)
- [Paper 07: Discrete Continuous Bridge](paper-07__unified_discrete_continuous_bridge.md)
- [Paper 26: Z-Pinch and Shear Horizon](paper-26__unified_z_pinch_and_shear_horizon.md)
- [Paper 38: Observer Computation AI Runtime](paper-38__unified_observer_computation_ai_runtime.md)
- [Paper 100: Capstone](paper-100__unified_Capstone_100_Paper_Series_and_Complete_Framework_Synthesis.md)

---

## Recovery Notes
3LSR Stub: Reference entries pending formal paper harvest. Domain: Causal Link / Obligation Ledger.

---

## Disposition
This paper is classified as **`canon`**. It is part of the core canonical paper series.
