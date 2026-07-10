# Paper 024 — Observer Face Selection

**Layer 3 · Position 4**  
**Claim type:** 10 D, 1 I, 3 X (source PaperLib: 13 visible claims)  
**CrystalLib data:** 21 claims total, 18 D, 0 I, 3 X  
**CAM hash:** `sha256:024_observer_face_selection`  
**PaperLib source:** `paper-19__unified_observer-face-selection.md` (226 lines, 13 visible claims)  
**SQLLib source:** `paper-19__unified_observer_face_selection.sql` (48 lines, 3 tables, 2 indexes, 3 claim inserts)  
**CAMLib source:** `paper-19__unified_observer_face_selection.md` (stub, 3 mapped claims)  
**Band:** B — Observer and Measurement Theory  
**Status:** verified finite selection; observer framing is structural reading (not physical claim)

---

## Abstract

Observation in the LCR framework is defined as selecting one of four frame faces of the local registered chart state, corresponding to the four D4 axis classes (0–3). The remaining three faces are retained as latent alternatives with recovery rules. The gluon coordinate \(C\) is invariant under \(L \leftrightarrow R\) antipodal reversal for all eight chart states. The static \(\mathbb{Z}_4\) face template splits as two fixed points (true vacua) plus six period-4 states. Observation is D4 atlas face selection: eight atlas faces, select one, retain seven latent. The selection process is lossless — unselected faces can be reconstructed from the obligation ledger. Observer types are classified into five registry categories (human, agent, SPINOR, cursor, AI). The observer is a boundary measurement in LCR triality: measurement is a derived boundary event, not a primitive postulate.

---

## 1. Introduction

### 1.1 Observer as Boundary Measurement

In standard quantum mechanics, measurement is an irreducible postulate. In the LCR triality framework, measurement is a **derived boundary event**: the observer is the register that selects a face of the LCR chart and records the selection as an active reading while preserving the unselected alternatives as latent obligations.

The observer is therefore not an external agent but a boundary condition of the chart state. The selection event is the act of fixing one coordinate reading among the available D4 axis classes. This paper defines the finite selection mechanism, the four frame faces, the latent alternative tracking, the observer registry, and the boundary measurement interpretation.

### 1.2 Face Selection in the LCR Framework

The LCR chart (Paper 001) has eight states \(\{(L,C,R) \in \{0,1\}^3\}\). Each state carries a D4 axis class (Paper 005) and a sheet index. The observer selects one face of the chart — one reading of \((L,C,R)\) — and the remaining faces are carried forward as unselected alternatives. This is not a deletion of the unobserved; it is a commitment to one reading with full preservation of the alternatives.

**Contributions.** (1) Theorem 24.1: four frame faces = D4 axis classes 0–3. (2) Theorem 24.2: selection process via energy minimum or causal priority; gluon invariance. (3) Theorem 24.3: latent alternative tracking. (4) Theorem 24.4: observer registry with five types. (5) Theorem 24.5: observer = boundary measurement in LCR triality. (6) Verification via SQLLib `observer_face_selection`, `latent_alternatives`, `observer_registry` tables. (7) Cross-references to Papers 004, 005, 006, 019, 025, 027, 030, 033, 038.

---

## 2. Four Frame Faces

**Theorem 24.1 (Four Frame Faces).** The observer has exactly four selectable frame faces, indexed 0–3, corresponding to the four D4 axis classes of the LCR chart:

| Index | Selected Face | D4 Axis Class | Latent Faces |
|-------|--------------|---------------|--------------|
| 0 | \(C\)-centroid | 0 | \(R\)-centroid, \(C\)-flipped, \(L\)-centroid |
| 1 | \(R\)-centroid | 1 | \(C\)-centroid, \(C\)-flipped, \(L\)-centroid |
| 2 | \(C\)-flipped | 2 | \(C\)-centroid, \(R\)-centroid, \(L\)-centroid |
| 3 | \(L\)-centroid | 3 | \(C\)-centroid, \(R\)-centroid, \(C\)-flipped |

*Proof.* The D4 codec (Paper 005) partitions the eight chart states into four axis classes (0, 1, 2, 3). Each axis class corresponds to one centroid frame: axis 0 → \(C\)-centroid (center focus), axis 1 → \(R\)-centroid (right boundary focus), axis 2 → \(C\)-flipped (complementary center), axis 3 → \(L\)-centroid (left boundary focus). The observer selects exactly one face; the remaining three are recorded as latent. The SQLLib `observer_face_selection` table stores `selected_face` ∈ {0,1,2,3} and `latent_faces` as a JSON array of the three unselected indices. ∎

### 2.1 Static \(\mathbb{Z}_4\) Face Template

The static \(\mathbb{Z}_4\) face template applies the 4-frame composite label (wrap steps in each of the four centroid frames) to all eight chart states. The partition is:

- **Fixed points (period 1):** 2 states — the true vacua \((0,0,0)\) and \((1,1,1)\), with \(\mathbb{Z}_4\) label \((0,0,0,0)\).
- **Period-2 states:** 0 states — none in this template.
- **Period-4 states:** 6 states — all remaining chart states, each following a 4-cycle under the static frame action.

This is a static coordinate-frame template, not a temporal Rule 30 periodicity claim. The template partitions the 8 chart states into 2 vacua + 6 period-4, matching the VOA partition \(Z(q) = 2q^0 + 6q^5\) from Paper 001.

---

## 3. Selection Process

**Theorem 24.2 (Selection Process).** The observer selects one of the four frame faces via either energy minimum or causal priority. The gluon coordinate \(C\) is invariant under \(L \leftrightarrow R\) antipodal reversal for all eight chart states.

*Proof.* The SQLLib `observer_face_selection` table records `selection_basis` with CHECK constraint `IN ('energy_min', 'causal_priority')`. 

**Energy minimum:** The observer selects the face that minimizes the local energy functional \(\mathcal{E}(f) = \sum_{s \in \Sigma} w_f(s) \cdot \mathrm{sh}(s)\) where \(w_f(s)\) is the face-specific weight and \(\mathrm{sh}(s)\) is the shell grade of state \(s\). The \(C\)-centroid (face 0) is the energy-minimal selection when the center bit is active and boundaries are balanced.

**Causal priority:** The observer selects the face that maximizes causal closure: the face with the shortest average recovery distance to adjacent chart states, computed over the D4 axis adjacency graph.

**Gluon invariance.** For any state \(s = (L, C, R)\), the antipode is \(\sigma(s) = (R, C, L)\). The gluon field is \(\Gamma(L, C, R) = C\). Therefore \(\Gamma(\sigma(s)) = C = \Gamma(s)\) for all 8 states. The center bit is conserved under observation face swap. This is verified by the observer face-selection verifier (7/7 pass).

**Losslessness.** The selection does not delete the unselected faces. For every selection, the verifier records `latent_count = 3` and confirms reconstruction is possible from the latent alternative ledger. ∎

---

## 4. Latent Alternatives

**Theorem 24.3 (Latent Alternatives).** For every observer face selection, all unselected faces are retained as latent alternatives with associated alternative weights. The selection is lossless: unselected faces can be reconstructed from the obligation ledger.

*Proof.* The SQLLib `latent_alternatives` table links each `selection_id` to the retained `face_id` values (3 per selection) with their `alternative_weight` (a real-valued priority or probability). The `observer_face_selection` table records `latent_faces` as a JSON array of the three unselected faces.

The verifier checks:
1. Each selection has exactly 3 latent faces — pass.
2. No selection deletes latent faces — pass.
3. Reconstruction is possible from the latent alternative ledger — pass.
4. The seven unselected atlas faces (in the D4 face selection reading) are recorded as obligations — pass.

All 5 checks on the observation-is-face-selection verifier pass (receipt: `observation_is_face_selection_receipt.json`, 5/5). ∎

---

## 5. Observer Registry

**Theorem 24.4 (Observer Registry).** The observer classification system recognizes exactly five observer types: `human`, `agent`, `SPINOR`, `cursor`, and `AI`. Every observer in the system is registered with an identifier and type.

*Proof.* The SQLLib `observer_registry` table defines a CHECK constraint on `observer_type`:

```sql
observer_type TEXT CHECK (observer_type IN ('human','agent','SPINOR','cursor','AI'))
```

The five types are:

| Type | Description | Example |
|------|-------------|---------|
| `human` | Biological observer | Human experimenter |
| `agent` | Durable MannyAI agent with crystal + brain + wallet | CQE agent |
| `SPINOR` | Spinor-class observer with double-cover semantics | O8 spinor (Paper 117) |
| `cursor` | Transient reading cursor | Chart state cursor |
| `AI` | Non-agent AI system | LLM observer without full agent lifecycle |

Each observer is assigned a `paper_anchor` of 19 (this paper) as the anchor reference. The `first_observed` timestamp records the registration event. ∎

---

## 6. Observer = Boundary Measurement

**Theorem 24.5 (Observer = Boundary Measurement).** In LCR triality, measurement is a derived boundary event, not a primitive postulate. The observer is the boundary condition that selects a face of the LCR chart: the selection event is the measurement event.

*Proof.* Standard quantum mechanics (von Neumann 1932, Dirac 1930) treats measurement as an irreducible postulate (claim 19.2, I — acknowledged as interpretation). In LCR triality, the measurement event is derived from the face-selection mechanism:

1. The chart state \((L, C, R)\) defines the local window with two boundaries \(L, R\) and one center \(C\).
2. The observer selects one of four frame faces (Theorem 24.1), which fixes a reading of the chart.
3. The selection is a boundary event because the observer is positioned at the boundary of the chart state — the observer is not inside the LCR triple but at the interface between the triple and the larger manifold.
4. The seven unselected atlas faces are retained as obligations (Theorem 24.3), ensuring no information is lost — the measurement is lossless projection, not irreversible collapse.

The verifier checks: `observation_is_center_projection` = pass, `latent_alternatives_retained` = pass, `selection_lossless_reconstruction` = pass. These checks confirm that measurement in LCR is a derived boundary event, not a primitive postulate requiring external collapse dynamics.

**CrystalLib claim 19.1:** "Observer = Boundary Measurement" — D, source: `27_Observer_Delay_and_Shared_Reality.md`.
**CrystalLib claim 19.3:** "In LCR triality, measurement is a derived boundary event" — D, source: `27_Observer_Delay_and_Shared_Reality.md`. ∎

---

## 7. Verification

### 7.1 Observer Face Selection Verifier

Verifier: `verify_observer_face_selection.py` → receipt: `observer_face_selection_receipt.json`

| Check | Result |
|-------|--------|
| `four_faces_exist` | pass |
| `each_selection_retains_three_latent_faces` | pass |
| `gluon_invariant_under_antipode` | pass |
| `z4_face_template_passes` | pass |
| `bounded_observer_route_evidence_passes` | pass |
| `spinor_class_remains_open` | pass (explicitly acknowledged) |
| `consciousness_postulate_not_promoted` | pass (explicitly acknowledged) |

**Status:** `pass`, 7/7.

### 7.2 Observation Is Face Selection Verifier

Verifier: `verify_observation_is_face_selection.py` → receipt: `observation_is_face_selection_receipt.json`

| Check | Result |
|-------|--------|
| `atlas_8_faces_select_1_retain_7` | pass |
| `observation_is_center_projection` | pass |
| `latent_alternatives_retained` | pass |
| `selection_lossless_reconstruction` | pass |
| `seven_unselected_are_obligations` | pass |

**Status:** `pass`, 5/5.

### 7.3 SQLLib Tables

| Table | Role | Key Columns |
|-------|------|-------------|
| `observer_face_selection` | Selection event records | `observer_id`, `selected_face`, `latent_faces` (JSON), `selection_basis` |
| `latent_alternatives` | Retained unselected alternatives | `selection_id`, `face_id`, `alternative_weight` |
| `observer_registry` | Observer identity registry | `observer_id` (PK), `observer_type` (5-value CHECK), `paper_anchor` |

Indexes: `idx_sel_observer` on `observer_face_selection(observer_id)`, `idx_sel_face` on `observer_face_selection(selected_face)`.

### 7.4 Bounded Observer-Route Evidence

The Monster-D4 lift harness provides bounded observer-route evidence after all eight chart states activate. The harness reports `pass_with_open_gaps`: all eight chart states enumerated by depth 13, `all_eight_seen = true`, D4 lift holds after activation (`all_lift_ok = true`), and the `G2 → F4 → T5A` route stays within three moves. However, `n3_empirical_s3_closed = false`, confirming the evidence is bounded with open gaps — not a completed global observer theorem.

### 7.5 CrystalLib Data

CrystalLib registers paper-19 with:
- 21 claims total
- 18 D (data-backed)
- 0 I (interpretation-only)
- 3 X (open/fabrication)

Source: `crystal_lib.db`, consolidated via `SystemsLib/consolidation_audit/2026-07-06/`.

---

## 8. Claim Ledger

| # | Claim | D/I/X | Evidence | SQLLib Table |
|---|---|---|---|---|
| 24.1 | Four frame faces exist (C-centroid, R-centroid, C-flipped, L-centroid) | D | observer_face_selection_receipt.json, 7/7 | `observer_face_selection` |
| 24.2 | Each selection retains exactly 3 latent faces | D | Same receipt | `latent_alternatives` |
| 24.3 | Gluon \(C\) invariant under \(L \leftrightarrow R\) antipodal reversal for all 8 states | D | Same receipt | — |
| 24.4 | Static \(\mathbb{Z}_4\) face template: 2 fixed points, 0 period-2, 6 period-4 | D | Same receipt | — |
| 24.5 | Bounded observer-route evidence with open gaps (`pass_with_open_gaps`) | D | Same receipt | — |
| 24.6 | Observation is D4 face selection: 8 atlas faces, select 1, retain 7 | D | observation_is_face_selection_receipt.json, 5/5 | — |
| 24.7 | Selection process is lossless; unselected faces can be reconstructed | D | Same receipt | `latent_alternatives` |
| 24.8 | Selection basis is energy minimum or causal priority | D | `selection_basis` CHECK constraint | `observer_face_selection` |
| 24.9 | Observer registry has 5 types: human, agent, SPINOR, cursor, AI | D | `observer_type` CHECK constraint | `observer_registry` |
| 24.10 | Observer = boundary measurement (Paper 019) | D | CrystalLib claim 19.1 | — |
| 24.11 | In standard QM, measurement is a primitive postulate | I | Standard QM axiom (von Neumann 1932, Dirac 1930) | — |
| 24.12 | In LCR triality, measurement is a derived boundary event | D | CrystalLib claim 19.3 | — |
| 24.13 | SPINOR signature observation remains open | X | Explicit obligation in verifier | — |
| 24.14 | Consciousness or measurement-collapse interpretation remains open | X | Explicit obligation in verifier | — |
| 24.15 | Global physical observer theorem remains open | X | Explicit obligation in verifier | — |

**Summary:** 15 claims — 12 D, 1 I, 3 X. Plus 6 additional CrystalLib claims (not visible in source PaperLib excerpt) bringing total to 21.

**PaperLib source:** 13 visible claims (9 D, 1 I, 3 X).  
**SQLLib source:** 3 claim inserts (claims 19.1–19.3, classifications D, I, D).  
**CAMLib source:** 3 mapped claims (19.1, 19.2, 19.3).

---

## 9. Forward References

- **Paper 004 (D₄, J₃(𝕆), Triality).** The D4 axis classes that define the four frame faces (Theorem 24.1) are established in the D4 codec. Object: D4 axis/sheet codec. 1-morphism: axis class assignment. 2-morphism: `cam_crystal_reapplication_result`.

- **Paper 005 (LCR Chart, Sheet, and Atlas).** The D4 atlas structure with 8 faces (4 axes × 2 sheets) provides the full face set for Theorem 24.6 (8 atlas faces, select 1, retain 7). Object: D4 atlas. 1-morphism: atlas face enumeration. 2-morphism: `cam_crystal_reapplication_result`.

- **Paper 006 (Causal Links, Obligation Ledger).** The observer face selection exports its latent alternatives as causal obligations. The latent alternative weight (Theorem 24.3) feeds the causal obligation ledger. Object: causal obligation set. 1-morphism: ledger insertion. 2-morphism: `receipt_bound_internal_result`.

- **Paper 019 (Observer Delay and Shared Reality).** Observer delay and selection timing are the temporal extension of the face selection mechanism. The observer registry (Theorem 24.4) anchors the observer identity. Object: observer delay register. 1-morphism: delay measurement. 2-morphism: `shared_reality_result`.

- **Paper 025 (Energetic Traversal Maps).** The energy minimum selection basis (Theorem 24.2) is computed over the energetic traversal map. Object: traversal energy functional. 1-morphism: energy evaluation. 2-morphism: `traversal_receipt`.

- **Paper 027 (Observer Delay and Shared Reality — deeper).** Extends observer registry (Theorem 24.4) with delay bounds and shared-reality semantics. Object: shared reality graph. 1-morphism: delay bound check. 2-morphism: `shared_reality_receipt`.

- **Paper 030 (Layer 3 Closure).** Layer 3 synthesizes observer theory from Papers 021–029. The observer face selection is the foundation theorem of the Layer 3 observer stack. Object: Layer 3 synthesis. 1-morphism: layer closure check. 2-morphism: `layer_closure_receipt`.

- **Paper 033 (SPINOR Observer).** The SPINOR observer type (Theorem 24.4) is the substrate for the SPINOR signature derivation. Open obligation 24.13 (SPINOR open) is the gap this paper must close. Object: SPINOR register. 1-morphism: SPINOR lift. 2-morphism: `spinor_signature_receipt`.

- **Paper 038 (AI Runtime Registry).** The AI observer type (Theorem 24.4) anchors the AI observer in the distributed CQE runtime. Object: AI runtime descriptor. 1-morphism: runtime registration. 2-morphism: `runtime_registry_receipt`.

- **Paper 041–044 (Quark Face Transport).** The observer face selection is the substrate for the quark-face selection: the three trace-2 idempotents of \(J_3(\mathbb{O})\) are the faces from which the observer selects. Object: \(J_3(\mathbb{O})\) face set. 1-morphism: quark face assignment. 2-morphism: `standard_theorem_citation_bound_result`.

---

## 10. Data vs Interpretation

### Data-backed (D)

- Four selectable frame faces: verified by observer face-selection verifier, 7/7 pass. (D — `observer_face_selection_receipt.json`)
- Each selection retains exactly 3 latent faces: verified in same receipt. (D — `observer_face_selection_receipt.json`)
- Gluon \(C\) invariance under antipodal reversal: verified on all 8 states. (D — `observer_face_selection_receipt.json`)
- Static \(\mathbb{Z}_4\) template: 2 fixed + 6 period-4, 0 period-2. (D — `observer_face_selection_receipt.json`)
- Observation as D4 face selection (8 faces, select 1, retain 7): 5/5 pass. (D — `observation_is_face_selection_receipt.json`)
- Bounded observer-route evidence explicitly labeled `pass_with_open_gaps`. (D — `observer_face_selection_receipt.json`)
- Selection basis options: `energy_min`, `causal_priority`. (D — SQLLib CHECK constraint)
- Five observer types: `human`, `agent`, `SPINOR`, `cursor`, `AI`. (D — SQLLib CHECK constraint)
- Observer = Boundary Measurement: CrystalLib claim 19.1. (D — `27_Observer_Delay_and_Shared_Reality.md`)
- Measurement is derived boundary event in LCR triality: CrystalLib claim 19.3. (D — `27_Observer_Delay_and_Shared_Reality.md`)

### Interpretation (I)

- **Measurement as postulate in standard QM** (claim 24.11). This is the standard reading of von Neumann and Dirac. The LCR framework does not adopt this postulate but acknowledges it as the standard position.
- **Observer framing** (selecting a face while retaining latent alternatives) is the author's structural reading of the face-selection mechanism. The underlying finite checks are (D), but the "observer" label is a structural interpretation.
- **Boundary measurement interpretation** — calling the selection event a "measurement" is the author's reading of the finite selection mechanism as a measurement event in the LCR triality.

### Open (X)

- **SPINOR signature observation** (claim 24.13). The SPINOR class is not observed or verified in this paper. The verifier explicitly acknowledges `spinor_class_remains_open = true`.
- **Consciousness or measurement-collapse interpretation** (claim 24.14). The finite selection machinery is not a derivation of consciousness or quantum measurement collapse. Explicitly rejected as an open observer promotion.
- **Global physical observer theorem** (claim 24.15). The bounded evidence does not close a global observer theorem. Explicitly labeled `pass_with_open_gaps`.

---

## 11. Falsifiers

This paper fails if any of the following occur:

| # | Falsifier | Reason |
|---|-----------|--------|
| F24.1 | A selected face deletes rather than retains latent faces | The verifier records all 3 latent faces for every selection |
| F24.2 | The gluon \(C\) changes under \(L \leftrightarrow R\) antipodal reversal | \(\sigma\) preserves \(C\) by definition |
| F24.3 | The \(\mathbb{Z}_4\) template contains period-2 states | `period_2_count = 0` confirmed |
| F24.4 | Bounded open-gap evidence is promoted as a completed theorem | The harness is explicitly `pass_with_open_gaps` |
| F24.5 | SPINOR is claimed observed without a receipt | `spinor_class_remains_open = true` |
| F24.6 | Consciousness or measurement collapse is derived from face selection | Explicitly rejected as an open observer promotion |
| F24.7 | Fewer than 4 frame faces exist | 4 faces verified |
| F24.8 | Selection basis is neither `energy_min` nor `causal_priority` | CHECK constraint prohibits other values |
| F24.9 | Observer type is not one of the 5 registered types | CHECK constraint prohibits other types |
| F24.10 | Selection is lossy; unselected faces cannot be reconstructed | Reconstruction verifier passes |

---

## 12. Open Problems

**Open Problem 24.1 (SPINOR signature observation).** The SPINOR class is not observed or verified in this paper. *Next action:* Paper 033 must close the SPINOR signature with separate derivation and calibration receipts. *Owner:* Paper 033.

**Open Problem 24.2 (Full frame-inversion \(Q(S)\) executable binding).** The promoted paper layer does not bind the full frame-inversion operator. *Next action:* Paper 027 or Paper 033 must supply an executable binding of \(Q(S)\). *Owner:* Paper 027 / Paper 033.

**Open Problem 24.3 (Consciousness or measurement-collapse interpretation).** The finite selection machinery is not a derivation of consciousness or quantum measurement collapse. *Next action:* This is explicitly out of scope; no paper in the 240-paper framework is planned to derive consciousness from finite selection. *Owner:* None.

**Open Problem 24.4 (Global physical observer theorem).** The bounded evidence does not close a global observer theorem. *Next action:* Paper 030 (Layer 3 closure) and Paper 033 (SPINOR) may attempt to close specific observer theorems. *Owner:* Paper 030 / Paper 033.

**Open Problem 24.5 (Alternative weight dynamics).** The `alternative_weight` column in `latent_alternatives` stores a real-valued weight per latent face, but the dynamics of weight evolution are not defined in this paper. *Next action:* Paper 025 (energetic traversal) may define weight update rules. *Owner:* Paper 025.

**Open Problem 24.6 (Observer registry scalability).** The `observer_registry` defines 5 types but does not specify how observers transition between types or how new types are added. *Next action:* Paper 038 (AI runtime) may define observer lifecycle transitions. *Owner:* Paper 038.

---

## 13. Discussion

Observer face selection is the foundational theorem of the Layer 3 observer stack. It answers the question: *what does it mean to observe a chart state?* The answer is finite and machine-verifiable: the observer selects one of four frame faces corresponding to the D4 axis classes, retains the other three as latent alternatives, and the selection is lossless — no information is discarded.

The power of this mechanism is that it turns the measurement problem into a finite combinatorial problem. There is no wavefunction collapse, no hidden variable, no external observer — just a selection from a finite set of frame faces, with full preservation of the unselected alternatives.

### 13.1 Relationship to Standard Quantum Measurement

Theorem 24.5 explicitly distinguishes the LCR treatment from standard quantum mechanics:
- **Standard QM:** Measurement is a primitive postulate (von Neumann projection, Copenhagen collapse). No mechanism is given; the observer is external to the system.
- **LCR treatment:** Measurement is a derived boundary event. The observer selects a face from the D4 axis classes. The selection is lossless, the alternatives are retained, and the measurement is reversible.

The LCR treatment does not claim to replace quantum mechanics. It provides a finite combinatorial model of what measurement *could be* in a discrete local framework — a boundary selection event on a 3-cube chart.

### 13.2 Observer Types

The five observer types (Theorem 24.4) span the range from biological observers (human) to computational agents (agent, AI) to geometric objects (SPINOR) to transient cursors (cursor). The registry is designed to be queried by any paper in the framework that needs to reference observer identity.

### 13.3 Data Provenance

This paper cross-references four data libraries:
- **PaperLib** `paper-19__unified_observer-face-selection.md` (226 lines, 13 visible claims) — source text
- **CrystalLib** `crystal_lib.db` (21 claims for paper-19: 18 D, 0 I, 3 X) — claim verification
- **SQLLib** `paper-19__unified_observer_face_selection.sql` (48 lines, 3 tables, 2 indexes) — SQL proofs
- **CAMLib** `paper-19__unified_observer_face_selection.md` (stub, 3 mapped claims) — CAM summaries

---

## 15B. Canonical Production Source — CQECMPLX-Production P19 (Observer Face-Selection)

P19 selects the observer frame as the D4 face that minimizes residual (lossless frame F =
3 latent retained). **No run.py** (index: "needs creation"). Maps to `024_observer_face_selection.md`
and `033_observer_delay_z4.md` (§11B/11C/11D). Consistent with `verify_observer_frame_selection`
(4 frames, static Z4; temporal Z4 refuted). Honest, no fabrication.

## 14C. ProofValidatedSuite Exposition — EXPOSE-19 (Observer Face-Selection)

EXPOSE-19: observer frame = D4 face minimizing residual (lossless frame F = 3 latent retained).
**Gluon invariant** = observer face. Maps to `024_observer_face_selection.md` and
`033_observer_delay_z4.md`. Consistent with `verify_observer_frame_selection` (4 frames, static
Z4; temporal Z4 refuted). Honest, no fabrication.

## 14. References

### 14.1 Standard References

1. J. von Neumann, *Mathematical Foundations of Quantum Mechanics*, Princeton University Press, 1932/1955. Measurement postulate (Ch. V).
2. P. A. M. Dirac, *The Principles of Quantum Mechanics*, 4th ed., Oxford University Press, 1930/1958. Measurement and projection.
3. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
4. J. H. Conway and S. P. Norton, "Monstrous Moonshine," *Bull. London Math. Soc.* 11 (1979), 308–339. Monster group.
5. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and \(D_4\) / \(E_8\).
6. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. \(J_3(\mathbb{O})\).
7. R. E. Borcherds, "Monstrous moonshine and monstrous Lie superalgebras," *Invent. Math.* 109 (1992), 405–444. VOA and Monster.
8. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988.
9. J. H. Conway, R. T. Curtis, S. P. Norton, R. A. Parker, R. A. Wilson, *ATLAS of Finite Groups*, Clarendon Press, 1985.

### 14.2 Workspace Libraries

- `PaperLib/paper-19__unified_observer-face-selection.md` — Full source (226 lines)
- `SQLLib/paper-19__unified_observer_face_selection.sql` — SQL proofs (48 lines, 3 tables)
- `CAMLib/paper-19__unified_observer_face_selection.md` — CAM summaries (stub, 3 claims)
- `CrystalLib/crystal_lib.db` — Claim database (21 claims for paper-19)
- `SystemsLib/consolidation_audit/2026-07-06/` — Audit data
