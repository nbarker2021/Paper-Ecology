# Paper 38: Observer Computation AI Runtime

**Domain:** Observer Computation AI Runtime  
**Disposition:** `canon`  
**CAMLib Entry Date:** 2026-07-04  

---

## Content-Addressed Entries

### Claim 38.1: Observer-Face Translation
- **Claim Text:** Observer-face selection is translated to the AI runtime.
- **CAM Hash:** `sha256:claim38_1`
- **CodeLib Source:** `D:/CodeLib/paper-38__unified_observer_computation_ai_runtime.py`
- **SQLLib Source:** `D:/SQLLib/paper-38__unified_observer_computation_ai_runtime.sql`
- **Status:** `harvested`
- **Verifier:** Structural reading of Paper 18 through AI runtime lens

### Claim 38.4: CAM Projectors as Memory Banks
- **Claim Text:** CAM crystal projectors (Paper 28) are the memory banks that the AI runtime reads and writes.
- **CAM Hash:** `sha256:claim38_4`
- **Status:** `harvested`
- **Verifier:** Paper 28, Theorem 2.1

### Claim 38.11: Server Endpoint Tests
- **Claim Text:** The CQE_CMPLX workspace server provides 13 HTTP endpoints, all passing automated test (100%).
- **CAM Hash:** `sha256:claim38_11`
- **Status:** `harvested`
- **Verifier:** `SERVER_TEST_REPORT.md` (2026-07-01); endpoint-by-endpoint verification against `http://localhost:8787`

### Claim 38.12: FastAPI Server
- **Claim Text:** The workspace server runs FastAPI with HTML dashboard, agent probe, health check, and OpenAPI docs.
- **CAM Hash:** `sha256:claim38_12`
- **Status:** `harvested`
- **Verifier:** `SERVER_TEST_REPORT.md` (2026-07-01); `api.py` implementation

### Claim 38.13: GLM-5.2 + MannyAI Architecture
- **Claim Text:** The AI architecture uses GLM-5.2 (744B MoE) as the remote "body" via API, and MannyAI (~50M param CQE-LM student) as the local "mouth."
- **CAM Hash:** `sha256:claim38_13`
- **Status:** `harvested`
- **Verifier:** `PLAN_GLM_BODY_AGENTS_MOUTH.md` (2026-07-03); GLM-5.2 is MIT open-weights; MannyAI runs on RTX 2060 SUPER (8 GB VRAM)

### Claim 38.14: Four Training Operations
- **Claim Text:** The four cheap training operations are: (1) write validated knowledge to CAM, (2) distill GLM outputs into CQE-LM student, (3) adapt MannyBrain experts by Hebbian `learn(vec, reward)`, (4) curate data via coin economy (SpeedLight dedup).
- **CAM Hash:** `sha256:claim38_14`
- **Status:** `harvested`
- **Verifier:** `PLAN_GLM_BODY_AGENTS_MOUTH.md` (2026-07-03); no backprop through GLM; 300 s training loop per run

### Claim 38.15: Graduation Metric
- **Claim Text:** The graduation metric measures `teacher_agreement` and `teacher_call_rate`; a work stream graduates when `teacher_call_rate < 5%` sustained over N ticks.
- **CAM Hash:** `sha256:claim38_15`
- **Status:** `harvested`
- **Verifier:** `PLAN_GLM_BODY_AGENTS_MOUTH.md` (2026-07-03); self-distillation guard: only standards-board-passed work becomes training targets

---

## Cross-References
- [Paper 09: Hamiltonian Temporal Emergence](paper-09__unified_hamiltonian_temporal_emergence.md)
- [Paper 10: T10 Master Receipt](paper-10__unified_t10_master_receipt.md)
- [Paper 28: N-Dimensional Game Lattices](paper-28__unified_n_dimensional_game_lattices.md)
- [Paper 30: Grand Ribbon Meta-Framer](paper-30__unified_grand_ribbon_meta_framer.md)
- [Paper 39: Falsifiers Comparators Standards](paper-39__unified_falsifiers_comparators_standards.md)
- [Paper 40: Grand Reconstruction Map](paper-40__unified_grand_reconstruction_map.md)
- [Paper 80: UFT Closed Form](paper-80__unified_UFT_Closed_Form_of_the_Language.md)
- [Paper 100: Capstone](paper-100__unified_Capstone_100_Paper_Series_and_Complete_Framework_Synthesis.md)

---

## Recovery Notes
3LSR Stub: Reference entries pending formal paper harvest. Domain: Observer Computation AI Runtime.

---

## Disposition
This paper is classified as **`canon`**. It is part of the core canonical paper series.
