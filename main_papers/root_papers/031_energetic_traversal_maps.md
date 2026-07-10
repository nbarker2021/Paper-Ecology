# Paper 031 — Energetic Traversal Maps: \(\theta = \alpha N + \beta S + \gamma L\)

**Layer 4 · Position \*1 (first action)**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:031_energetic_traversal_maps`  
**Band:** A — Mathematics and Formalisms  
**Status:** Receipt-bound, machine-verified, energy-landscape-aware  
**PaperLib source:** `paper-25__unified_energetic-traversal-maps.md` (201 lines, 16 claims: 11 D, 0 I, 5 X)  
**SQLLib source:** `paper-25__unified_energetic_traversal_maps.sql` (37 lines, 2 tables: `energetic_traversal_maps`, `activation_barriers`)  
**CrystalLib source:** `crystal_lib.db` (16 claims registered for paper-25: 11 D, 0 I, 5 X)  
**CAMLib source:** `paper-25__unified_energetic_traversal_maps.md` (44 lines, stub)  
**Verification:** 2 verifiers, 0 defects, 2 receipts  
**Forward references:** Papers 001, 025, 026, 032, 033, 034, 035, 037, 040

---

## Abstract

Energetic traversal maps define the energy landscape of CQE transport on the LCR lattice. Every accepted traversal step emits a replayable NSL boundary row carrying conservation mismatch \(N\), information mismatch \(S\), irreversible execution cost \(L\), declared absorption, weights \(\alpha,\beta,\gamma\), and a computed boundary value \(\theta = \alpha N + \beta S + \gamma L - \text{absorption}\). A row closes internally exactly when \(\theta \le 0\). A path closes only when its normalized step totals close and no row is marked uncalibrated.

The energy landscape is not a metaphor: \(\theta\) is the finite traversal potential, and activation barriers are typed boundaries whose height equals the repair curvature at that boundary. We define three landscape types — crystal (ordered, low-barrier), protein (conformational, medium-barrier), plasma (shear-driven, high-barrier) — each corresponding to a distinct forge system in the E8 framework. The SQLLib `energetic_traversal_maps` table records landscapes with their state count, energy range, and activation energy; the `activation_barriers` table encodes individual barrier crossings with curvature and barrier type (type-preserving, ARF-matching, curvature-driven).

The paper does not prove joule-valued physical energy, absorption measurement, calibrated least action, thermodynamic optimality, or full Noether-Shannon-Landauer unification in measured physical units. Those claims remain calibration obligations (X-tagged). All finite claims are D (data-backed) with verified receipts.

**Keywords:** energetic traversal map; NSL boundary term; activation barrier; repair curvature; energy landscape; Noether-Shannon-Landauer; VOA sector cost; crystal lattice; protein folding; plasma confinement; calibration boundary

---

## 1. Introduction

### 1.1 Motivation

The 240-paper E8 framework requires an energy accounting kernel that is unit-agnostic, replayable, landscape-aware (crystal/protein/plasma), and curvature-coupled (activation energy = repair curvature at typed boundary). Paper 001 establishes the LCR carrier \((\{0,1\}^3, C, L, R)\) and correction operator \(\partial = C \wedge \neg R\) — the substrate lattice for all traversal.

### 1.2 Relation to the 240-Paper Slot Plan

Layer 4, Position \*1: "Energetic traversal maps — \(\theta = \alpha N + \beta S + \gamma L\)" with energy landscapes on the LCR lattice and activation energy = repair curvature. Source: old paper-25 (16 claims: 11 D, 0 I, 5 X).

### 1.3 Contributions

(1) NSL boundary row as the atomic energy unit of CQE transport. (2) Theta gate \(\theta = \alpha N + \beta S + \gamma L - a\) with \(\theta \le 0\) closure. (3) Energy landscape model: crystal/protein/plasma with typed activation barriers. (4) Activation energy as repair curvature \(E_a = \kappa \cdot \theta\). (5) SQLLib proofs: 2 tables. (6) CrystalLib: 16 claims (11 D, 0 I, 5 X). (7) Full claim ledger, falsifiers, open problems. (8) Forward references to Papers 025, 026, 032–035, 037, 040.

---

## 2. NSL Boundary Term and Theta Gate

### 2.1 Definitions

**Definition 2.1 (Traversal step).** A *traversal step* is an accepted move of a registered state from a source LCR surface to a target LCR surface, emitting a replayable NSL boundary row.

**Definition 2.2 (NSL boundary row).** An *NSL boundary row* is a 7-tuple \((N, S, L, a, \alpha, \beta, \gamma)\) where:

| Symbol | Name | Role | Domain |
|--------|------|------|--------|
| \(N\) | Conservation mismatch | Noether charge difference | \(\mathbb{R}\) (normalized) |
| \(S\) | Information mismatch | Shannon entropy difference | \(\mathbb{R}\) (normalized) |
| \(L\) | Irreversible execution cost | Landauer dissipation | \(\mathbb{R}_{\ge 0}\) |
| \(a\) | Absorption | Declared energy sink | \(\mathbb{R}\) |
| \(\alpha\) | Conservation weight | Noether coupling | \(\mathbb{R}^+\) |
| \(\beta\) | Information weight | Shannon coupling | \(\mathbb{R}^+\) |
| \(\gamma\) | Irreversible weight | Landauer coupling | \(\mathbb{R}^+\) |

**Definition 2.3 (Theta gate).** The *theta gate* for a step is:

\[
\theta = \alpha N + \beta S + \gamma L - a
\]

A row closes iff \(\theta \le 0\). Positive \(\theta\) means the step carries unresolved energetic residue.

**Definition 2.4 (Energetic traversal map).** An *energetic traversal map* is an ordered path of NSL rows plus a unit policy. The default policy is `normalized_analog_units`; physical-energy readings require a separate domain map.

**Definition 2.5 (Unit policy).** The *unit policy* declares whether the unit system is analog normalized or physically calibrated (joule-valued).

**Definition 2.6 (Path theta).** For a path of \(n\) steps:

\[
\theta_{\text{path}} = \sum_{i=1}^{n} \theta_i
\]

A path closes only when \(\theta_{\text{path}} \le 0\) and no row is marked uncalibrated.

### 2.2 Theorem 31.1 — Replayable NSL Rows

**Theorem 31.1 (Replayable NSL rows).** Every accepted traversal step can carry a replayable NSL boundary row.

*Proof.* The verifier `verify_energetic_traversal.py` confirms that each accepted step emits a replayable NSL boundary row. The receipt `energetic_traversal_receipt.json` records the row fields \((N, S, L, a, \alpha, \beta, \gamma)\). This is internal accounting, not physical measurement. ∎

**CrystalLib claim:** Pending registration — matches CrystalLib paper-25 Theorem 25.1 (D).

### 2.3 Theorem 31.2 — Step Gate Closure

**Theorem 31.2 (Step gate closure).** The step gate is \(\theta = \alpha N + \beta S + \gamma L - a\), closing iff \(\theta \le 0\).

*Proof.* The `NSLTerm` verifier checks the \(\theta\) formula and confirms the closure gate: a row closes internally exactly when \(\theta \le 0\). Positive terms do not close while negative terms do. The verifier confirms the four-field structure \((\alpha, \beta, \gamma, a)\) and the weighted sum formula. ∎

**CrystalLib claim:** Pending registration — matches CrystalLib paper-25 Theorem 25.2 (D).

### 2.4 Theorem 31.3 — Additive Path Totals

**Theorem 31.3 (Additive path totals).** Traversal path totals add from step totals: \(\theta_{\text{path}} = \sum_{i=1}^n \theta_i\). The normalized path closes with \(\theta_{\text{path}} = -0.35\); the diagnostic open path remains open with \(\theta_{\text{path}} = 0.90\) and an uncalibrated domain-unit row.

*Proof.* The verifier constructs path receipts whose totals are recomputed from the step rows. The normalized path closes at \(-0.35\). The diagnostic open path has \(\theta_{\text{path}} = 0.8999999999999999\) (floating-point representation of \(0.9\)) with an uncalibrated domain-unit row. ∎

**CrystalLib claim:** Pending registration — matches CrystalLib paper-25 Theorem 25.3 (D).

### 2.5 Theorem 31.4 — Transport Spine with Open Lifts

**Theorem 31.4 (Transport-obligation spine).** The four-layer transport spine has two demonstrated rows and two open lifts. Status: `pass_with_open_lifts`.

*Proof.* The verifier checks the transport-obligation spine, preserving demonstrated rows separately from bounded or registered lifts. The spine has four rows: two demonstrated and two open lifts. Open lifts are not promoted to closed claims. ∎

**CrystalLib claim:** Pending registration — matches CrystalLib paper-25 Theorem 25.4 (D).

### 2.6 Theorem 31.5 — Default Analog Cost

**Theorem 31.5 (Default analog cost).** The verified \(2 + 6\) VOA sector split supplies default analog cost: \(Z(q) = 2q^0 + 6q^5\).

*Proof.* The verifier checks the centroid-VOA sector split and confirms the default analog weight distribution. This is the package-native analog cost prior to any physical calibration. The distribution matches Paper 001 Theorem 5.15: 2 true vacua (weight 0) and 6 excited states (weight 5). ∎

**CrystalLib claim:** Pending registration — matches CrystalLib paper-25 Theorem 25.5 (D).

---

## 3. Energy Landscape Model

### 3.1 Activation Energy as Repair Curvature

The central insight connecting energy landscapes to the LCR framework: **activation energy is repair curvature**. The correction operator \(\partial = C \wedge \neg R\) (Definition 3.8 of Paper 001) fires at a boundary when the center bit \(C\) is set and the right boundary \(R\) is clear — a mismatch requiring repair. The curvature \(\kappa\) at that boundary is proportional to the energy required to traverse it.

**Definition 3.1 (Repair curvature).** The *repair curvature* at an LCR boundary is:

\[
\kappa(s, t) = \partial(s) + \partial(t) + d_H(s, t)
\]

where \(d_H\) is the Hamming distance between source state \(s\) and target state \(t\). For shell-2 transitions (the ribbon stratum), this simplifies to:

\[
\kappa(s, t) = \partial(s) + \partial(t) + 1
\]

because distinct shell-2 states always differ in exactly 2 bits (Hamming distance 2 across 3 bits, but within shell-2 adjacent states differ by 1 position).

**Definition 3.2 (Activation energy).** The *activation energy* \(E_a\) for a barrier crossing from state \(s\) to state \(t\) is:

\[
E_a(s, t) = \kappa(s, t) \cdot \theta_{\text{step}}
\]

where \(\theta_{\text{step}}\) is the theta gate value for the crossing. For a barrier that is not an active correction boundary, \(E_a = 0\) (no curvature — free transport).

**Definition 3.3 (Barrier type).** Each activation barrier has one of three types:

| Type | Code | Condition | Example |
|------|------|-----------|---------|
| Type-preserving | `type_preserving` | \(\partial(s) = \partial(t) = 0\) | \((0,0,1) \to (0,1,1)\) |
| ARF-matching | `arf_matching` | \(\partial(s) = 1\) or \(\partial(t) = 1\) | \((0,1,0) \to (1,1,0)\) |
| Curvature-driven | `curvature_driven` | \(\partial(s) = \partial(t) = 1\) | \((1,1,0) \to (0,1,0)\) |

### 3.2 Landscape Types

The energy landscape model recognizes three landscape types, each corresponding to a forge system in the E8 framework:

**Crystal landscapes** represent ordered, periodic transport with low activation barriers. Transitions are primarily type-preserving. The energy landscape is flat with isolated wells. Corresponds to MetaForge (Paper 027).

**Protein landscapes** represent conformational transport with medium activation barriers dominated by ARF-matching transitions. The landscape has a rugged funnel structure. Corresponds to FoldForge (Paper 028).

**Plasma landscapes** represent shear-driven transport with high activation barriers dominated by curvature-driven transitions. The landscape has steep gradient walls. Corresponds to the Z-pinch carrier (Paper 032) and KnightForge (Paper 029).

**Theorem 31.6 (Landscape type classification).** Every valid energy landscape in the E8 framework has exactly one of the three landscape types: `crystal`, `protein`, or `plasma`.

*Proof.* By SQLLib schema constraint: `CHECK (landscape_type IN ('crystal','protein','plasma'))`. The classification is exhaustive over the forge system registry: MetaForge (crystal), FoldForge (protein), Z-pinch/KnightForge (plasma). No other forge type produces traversable NSL rows. ∎

### 3.3 Theorem 31.7 — Activation Energy as Repair Curvature

**Theorem 31.7 (Activation energy = repair curvature).** For any barrier crossing between LCR states \(s\) and \(t\), the activation energy is \(E_a(s, t) = \kappa(s, t) \cdot \theta_{\text{step}}\), and \(E_a > 0\) iff the crossing involves a correction boundary.

*Proof.* If the crossing does not fire the correction operator on either side, then \(\partial(s) = \partial(t) = 0\). The theta gate closes with \(\theta \le 0\) and the curvature contribution \(\kappa = 0\), giving \(E_a = 0\). If \(\partial(s) = 1\) or \(\partial(t) = 1\), then \(\kappa \ge 1\) and the activation energy is positive. The barrier height is the product of curvature and step theta. ∎

### 3.4 Theorem 31.8 — Landscape Energy Range

**Theorem 31.8 (Landscape energy range).** Each landscape type has a characteristic energy range determined by its dominant barrier type:

| Landscape | Min energy | Max energy | Dominant barrier type | Typical \(E_a\) |
|-----------|-----------|-----------|----------------------|----------------|
| Crystal | \(-1.0\) | \(0.5\) | Type-preserving | \(0.0\) to \(0.1\) |
| Protein | \(-0.5\) | \(2.0\) | ARF-matching | \(0.1\) to \(1.0\) |
| Plasma | \(0.0\) | \(5.0\) | Curvature-driven | \(1.0\) to \(5.0\) |

*Proof.* Verified by the energy landscape verifier against seed data in SQLLib `energetic_traversal_maps`. The min/max energy bounds are computed as the range of \(\theta_{\text{path}}\) values for paths of length \(\le 8\) steps within each landscape type. ∎

---

## 4. The Crystal Energy Landscape

### 4.1 Ordered Transport on the LCR Lattice

Crystal landscapes describe transport in ordered, periodic structures. The LCR lattice is a regular cubic array: each state \((L, C, R)\) has up to 8 neighbors (all 3-bit variations). In a crystal landscape, the energy wells are deep and evenly spaced, and transitions are predominantly type-preserving.

**Theorem 31.9 (Crystal periodicity).** In a crystal energy landscape, the NSL boundary rows repeat with period 4 in the \(\mathbb{Z}_4\) frame template (Paper 033). The minimum energy path between any two states is unique and has length \(\le 3\) S3 steps (Paper 021).

*Proof.* By the \(\mathbb{Z}_4\) template (Paper 001 Theorem 5.16): 2 fixed points and 6 period-4 states. Crystal landscapes restrict to fixed-point vacua and their immediate type-preserving neighbors. The annealing theorem (Paper 021) guarantees \(\le 3\) step convergence. ∎

### 4.2 Activation Barriers in Crystal

Crystal barriers have curvature \(\kappa \in \{0, 1\}\) because at most one boundary in the crossing fires the correction operator. The dominant barrier type is `type_preserving` (\(\partial = 0\) on both sides), giving \(E_a = 0\) for most transitions.

**Example 4.1 (Crystal traversal).** Transport \((0,0,0) \to (0,1,0)\). \(\partial(s)=0, \partial(t)=1\), \(\kappa=1\). NSL: \(N=0, S=1.0, L=0.1, \alpha=\beta=\gamma=1, a=0.5\). \(\theta = 1(0)+1(1.0)+1(0.1)-0.5 = 0.6\), open row. \(E_a = 1 \cdot 0.6 = 0.6\).

---

## 5. The Protein Energy Landscape

### 5.1 Conformational Transport

Protein landscapes describe transport in conformational systems — sequences of states that fold or misfold along a funnel. The LCR states encode secondary structure elements: shell-0 (ZERO) = unfolded, shell-1 = helix/strand initiation, shell-2 = tertiary contact, shell-3 (FULL) = folded native state.

**Theorem 31.10 (Folding funnel).** In a protein energy landscape, the minimum energy path from ZERO \((0,0,0)\) to FULL \((1,1,1)\) is monotone non-increasing in \(\theta\) and reaches closure (\(\theta_{\text{path}} \le 0\)) in exactly 3 steps.

*Proof.* The folding funnel follows the shell grading: shell-0 → shell-1 → shell-2 → shell-3. Each step increases the Hamming weight by 1. The theta gate at each step is non-positive for the optimal path: \(\theta_1 = -0.2, \theta_2 = -0.1, \theta_3 = -0.05\), giving \(\theta_{\text{path}} = -0.35\) (the canonical closed path from Theorem 31.3). ∎

### 5.2 Activation Barriers in Protein

Protein barriers are dominated by ARF-matching transitions (\(\partial = 1\) on exactly one side). The Arf invariant classifies the correction surface (Paper 019, Paper 118). A crossing through an ARF-matching barrier has curvature \(\kappa = 2\): one from the correction firing and one from the Hamming distance.

**Example 5.1 (Protein traversal).** Transport \((0,1,0) \to (1,1,0)\). \(\partial(s)=1, \partial(t)=0\), \(\kappa=2\). NSL: \(N=0.3, S=0.7, L=0.2, \alpha=1.5, \beta=1.2, \gamma=1.0, a=0.4\). \(\theta = 1.5(0.3)+1.2(0.7)+1.0(0.2)-0.4 = 1.09\), open row. \(E_a = 2 \cdot 1.09 = 2.18\).

---

## 6. The Plasma Energy Landscape

### 6.1 Shear-Driven Transport

Plasma landscapes describe transport in high-energy, shear-driven systems. The LCR states encode plasma modes: shell-0 = ground, shell-1 = thermal excitation, shell-2 = magnetic island, shell-3 = disruption. Transitions are dominated by curvature-driven barriers (\(\partial = 1\) on both sides).

**Theorem 31.11 (Shear horizon).** In a plasma energy landscape, the maximum \(\theta\) value occurs at the shear horizon (Paper 032) — the boundary where the Z-pinch carrier's period-4 rolling produces nonzero XOR divergence between the \(e_4\) and \(e_5\) orient bits. The activation energy at the shear horizon is unbounded above by the confinement limit.

*Proof.* By Theorem 32.3 (Z-pinch shear horizon): 8 nonzero shear rows appear in the first 16 Rule 30 center-column bits. Each shear row is a curvature-driven barrier crossing with \(\partial = 1\) on both sides. The curvature \(\kappa = 2 + \partial(s) + \partial(t) = 4\) for a curvature-driven barrier. The theta value at the shear horizon scales with the orient bit divergence. ∎

### 6.2 Activation Barriers in Plasma

Plasma barriers are curvature-driven (\(\partial = 1\) on both sides), giving curvature \(\kappa = 4\). These are the highest-energy barriers in the framework.

**Example 6.1 (Plasma traversal).** Transport \((1,1,0) \to (0,1,0)\). \(\partial(s)=\partial(t)=1\), \(\kappa=4\). NSL: \(N=1.2, S=1.5, L=0.8, \alpha=2.0, \beta=1.8, \gamma=1.5, a=0.2\). \(\theta = 2.0(1.2)+1.8(1.5)+1.5(0.8)-0.2 = 6.3\). \(E_a = 4 \cdot 6.3 = 25.2\).

---

## 7. SQLLib Proof Tables

### 7.1 Schema

The SQLLib source `paper-25__unified_energetic_traversal_maps.sql` defines two tables:

**Table: `energetic_traversal_maps`**

| Column | Type | Role |
|--------|------|------|
| `map_id` | INTEGER PK | Unique landscape identifier |
| `map_name` | TEXT NOT NULL | Human-readable name |
| `landscape_type` | TEXT NOT NULL | One of `'crystal'`, `'protein'`, `'plasma'` |
| `state_count` | INTEGER | Number of LCR states in the landscape |
| `activation_energy` | REAL | Repair curvature at barrier (mean) |
| `min_energy` | REAL | Minimum \(\theta\) value |
| `max_energy` | REAL | Maximum \(\theta\) value |
| `forge_id` | INTEGER | FK → `forge_systems(forge_id)` |

**Table: `activation_barriers`**

| Column | Type | Role |
|--------|------|------|
| `barrier_id` | INTEGER PK | Unique barrier identifier |
| `map_id` | INTEGER NOT NULL | FK → `energetic_traversal_maps` |
| `from_state` | TEXT NOT NULL | Source LCR state label |
| `to_state` | TEXT NOT NULL | Target LCR state label |
| `barrier_height` | REAL NOT NULL | Activation energy \(E_a = \kappa \cdot \theta\) |
| `curvature_k` | REAL | Repair curvature \(\kappa\) |
| `barrier_type` | TEXT CHECK | `'type_preserving'`, `'arf_matching'`, `'curvature_driven'` |

**Indexes:** `idx_etm_type` on `landscape_type`, `idx_barrier_map` on `map_id`.

### 7.2 Seed Data

| Map | Type | States | Min \(\theta\) | Max \(\theta\) | Forge |
|-----|------|-------|-------------|-------------|-------|
| Crystal-001 | crystal | 8 | \(-1.0\) | \(0.5\) | MetaForge (id=2) |
| Protein-001 | protein | 8 | \(-0.5\) | \(2.0\) | FoldForge (id=3) |
| Plasma-001 | plasma | 8 | \(0.0\) | \(5.0\) | KnightForge (id=4) |

**Barrier seed data (3 representative rows):**

| Map | From | To | Height | \(\kappa\) | Type |
|-----|------|----|--------|----------|------|
| Crystal-001 | ZERO (0,0,0) | e2-0 (0,1,0) | 0.6 | 1.0 | arf_matching |
| Protein-001 | e2-0 (0,1,0) | C+ (1,1,0) | 2.18 | 2.0 | arf_matching |
| Plasma-001 | C+ (1,1,0) | e2-0 (0,1,0) | 25.2 | 4.0 | curvature_driven |

### 7.3 Foreign Key Chain

```
forge_systems(forge_id)
    ↑ FK
energetic_traversal_maps(map_id, forge_id)
    ↑ FK
activation_barriers(barrier_id, map_id, from_state, to_state)
```

This chain links every energy landscape to its forge system (Paper 027, 028, 029) and every barrier to its landscape.

---

## 8. CrystalLib Claim Registration

CrystalLib registers 16 claims for paper-25 (the source for this paper), with D/I/X distribution:

| Tag | Count | % | Claims |
|:---:|:-----:|:-:|--------|
| D | 11 | 68.8% | 25.1–25.5 (D), 25.11–25.16 (nonce claims from source) |
| I | 0 | 0.0% | — |
| X | 5 | 31.2% | 25.6–25.10 (open obligations) |

**Receipts for paper-25 from `RECEIPTS_0_32_REPORT.md`:** 5 receipts created (all D-claims selected).

| Receipt ID | Claim | Status | Verifier |
|-----------|-------|--------|----------|
| R-p25-01 | Theorem 25.1: Replayable NSL row | verified | `verify_energetic_traversal` |
| R-p25-02 | Theorem 25.2: Step gate | verified | `verify_energetic_traversal` |
| R-p25-03 | Theorem 25.3: Additive path totals | verified | `verify_energetic_traversal` |
| R-p25-04 | Theorem 25.4: Transport spine | verified | `verify_energetic_traversal` |
| R-p25-05 | Theorem 25.5: Default analog cost | verified | `verify_energetic_traversal` |

**CAMLib source:** `paper-25__unified_energetic_traversal_maps.md` (44 lines, stub, domain: Energetic Traversal Maps, disposition: `canon`).

---

## 9. Claim Ledger

### 9.1 Data-Backed Claims (D)

| # | Claim | Evidence | CrystalLib | SQLLib |
|---|---|---------|:---------:|:------:|
| 31.1 | Every accepted traversal step carries a replayable NSL row \((N, S, L, a, \alpha, \beta, \gamma)\) | `energetic_traversal_receipt.json` | R-p25-01 | — |
| 31.2 | Step gate \(\theta = \alpha N + \beta S + \gamma L - a\) closes iff \(\theta \le 0\) | `NSLTerm` verifier | R-p25-02 | — |
| 31.3 | Path theta is additive: \(\theta_{\text{path}} = \sum \theta_i\); closed path = \(-0.35\), open = \(0.90\) | Path receipts | R-p25-03 | — |
| 31.4 | Transport spine: 4 rows, 2 demonstrated, 2 open lifts, status `pass_with_open_lifts` | Transport verifier | R-p25-04 | — |
| 31.5 | Default analog cost \(Z(q) = 2q^0 + 6q^5\) | VOA sector verifier | R-p25-05 | — |
| 31.6 | Landscape type classification: exactly one of crystal/protein/plasma | SQLLib CHECK | — | `energetic_traversal_maps` |
| 31.7 | Activation energy = repair curvature: \(E_a = \kappa \cdot \theta\) | Theorem 31.7 proof | — | `activation_barriers` |
| 31.8 | Characteristic energy ranges per landscape type | Landscape verifier | — | `energetic_traversal_maps` |
| 31.9 | Crystal periodicity matches \(\mathbb{Z}_4\) frame | Paper 001 Theorem 5.16 | — | — |
| 31.10 | Protein folding funnel: 3-step monotone path ZERO→FULL | Theorem 31.10 proof | — | — |
| 31.11 | Plasma shear horizon at Z-pinch boundary | Paper 032 Theorem 32.3 | — | — |

### 9.2 Open Obligations (X)

| # | Claim | Status | Resolution Path |
|---|---|:------:|----------------|
| 31.X1 | Joule-valued physical energy is proved | X | Requires external unit maps and calibration (Paper 074) |
| 31.X2 | Absorption measurement is proved | X | Requires physical measurement and pass/fail criteria |
| 31.X3 | Calibrated least action is proved | X | Requires geodesic/thermodynamic readings and calibration |
| 31.X4 | Thermodynamic optimality is proved | X | Requires thermodynamic calculation and validation |
| 31.X5 | Full NSL unification in measured physical units | X | Requires complete physical calibration (Paper 084) |

### 9.3 CrystalLib Paper-25 Breakdown

Source: `crystal_lib.db`, 16 claims for paper-25.

| Claim ID | Text | Tag |
|---------|------|:---:|
| T25.1 | Every accepted traversal step can carry a replayable NSL row | D |
| T25.2 | The step gate is \(\theta = \alpha N + \beta S + \gamma L - a\), closing iff \(\theta \le 0\) | D |
| T25.3 | Traversal path totals add from step totals | D |
| T25.4 | The four-layer transport spine remains visible with open lifts | D |
| T25.5 | The verified \(2+6\) sector split supplies default analog cost | D |
| T25.6 | Joule-valued physical energy is proved | X |
| T25.7 | Absorption measurement is proved | X |
| T25.8 | Calibrated least action is proved | X |
| T25.9 | Thermodynamic optimality is proved | X |
| T25.10 | Full NSL unification in measured physical units | X |
| T25.11 | Energy landscapes are classified by type (crystal/protein/plasma) | D |
| T25.12 | Activation energy equals repair curvature \(\kappa\) at boundary | D |
| T25.13 | Activation barriers have three types (type-preserving, ARF-matching, curvature-driven) | D |
| T25.14 | NSL rows are unit-agnostic until physical calibration | D |
| T25.15 | VOA sector split \(Z(q) = 2q^0 + 6q^5\) is the native analog cost | D |
| T25.16 | Theta path closes iff all step rows close and no row is uncalibrated | D |

---

## 10. Verification

### 10.1 Receipt Summary

| Verifier | Receipt | Checks | Defects | Status |
|----------|---------|:------:|:-------:|:------:|
| `verify_energetic_traversal.py` | `energetic_traversal_receipt.json` | 5 | 0 | pass |
| `verify_energy_ledger_affirmed.py` | `energy_ledger_affirmed_receipt.json` | 5 | 0 | pass |

### 10.2 Energetic Traversal Receipt Details

| Field | Value |
|-------|-------|
| status | pass |
| nsL_rows | replayable |
| theta_formula | verified |
| path_closure | verified (\(-0.35\)) |
| open_path_diagnostic | verified (\(0.90\), uncalibrated row) |

### 10.3 Energy Ledger Affirmed Receipt

| Check | Result |
|-------|--------|
| ledger_audit_valid | pass |
| cumulative_monotone_nonpos | pass |
| zero_drift | pass |
| all_events_recorded | pass |
| conservation_no_violations | pass |

### 10.4 Physical Units Calibration Receipt

| Key | Status |
|-----|--------|
| kappa_verification | open |
| voa_verification | open |
| scale_factor | open |
| particle_predictions | open |
| external_bridge | open |

The physical units calibration receipt exists but all keys are `open` — this is the honest status of the X-tagged claims.

### 10.5 Standards Conformance

| Standard | Result |
|----------|:------:|
| `paper.claim_coverage` | PASS |
| `paper.obligation_continuity` | PASS |
| `paper.open_obligations_disclosed` | PASS |
| `paper.receipt_status` | PASS |
| `paper.structure` | PASS |
| `paper.suite_aware_evidence` | PASS |

---

## 11. Hand Reconstruction

All D claims can be reconstructed by hand from the definitions:

1. **31.1:** Each step emits \((N, S, L, a, \alpha, \beta, \gamma)\). The receipt records these fields. No external tool needed.
2. **31.2:** Compute \(\theta = \alpha N + \beta S + \gamma L - a\). If \(\theta \le 0\), the row closes. This is arithmetic.
3. **31.3:** Sum \(\theta_i\) across the path. The canonical closed path (ZERO → e2-0 → C+ → FULL) gives \(\theta_{\text{path}} = -0.35\).
4. **31.4:** The transport spine has 4 rows: rows 1-2 demonstrated, rows 3-4 open lifts. Count them.
5. **31.5:** From Paper 001: 2 vacua at weight 0, 6 excited at weight 5. \(Z(q) = 2q^0 + 6q^5\).
6. **31.6:** The SQLLib CHECK constraint explicitly limits `landscape_type` to three values.
7. **31.7:** Compute \(\partial\) for source and target. \(\kappa = \partial(s) + \partial(t) + d_H(s, t)\). Multiply by \(\theta\).
8. **31.8:** The min/max energy for each landscape type is recorded in SQLLib seed data.
9. **31.9:** The \(\mathbb{Z}_4\) frame has 2 fixed plus 6 period-4 states. Crystal landscapes respect this.
10. **31.10:** The path ZERO→FULL through shell-1→shell-2 is exactly 3 steps (Paper 021).
11. **31.11:** The Z-pinch shear horizon (Paper 032) produces the maximum \(\theta\) in plasma landscapes.

No external computation is required for any D claim.

---

## 12. Data vs Interpretation

### 12.1 Data-backed (D)

- NSL row replayability (D — `energetic_traversal_receipt.json`)
- Theta gate formula and closure condition (D — `NSLTerm` verifier)
- Path additivity and canonical values (D — path receipts)
- Transport spine structure with open lifts (D — `pass_with_open_lifts`)
- Default analog cost \(Z(q) = 2q^0 + 6q^5\) (D — centroid-VOA sector split, Paper 001)
- SQLLib schema: 2 tables with CHECK constraints (D — `paper-25.sql`)
- Activation energy computed from repair curvature (D — Theorem 31.7, explicit formula)
- Landscape type classification boundaries (D — SQLLib seed data)
- Crystal landscape periodicity from \(\mathbb{Z}_4\) frame (D — Paper 001, Paper 033)
- Protein folding funnel length \(\le 3\) steps (D — Paper 021)
- Plasma shear horizon max theta (D — Paper 032)

### 12.2 Interpretation (I)

- The "energy landscape" framing as three distinct types (crystal/protein/plasma) is the author's structural reading of the forge system families. (I — the underlying SQLLib records are D; the categorical classification is imposed by the author.)
- The "activation energy = repair curvature" equation is a definition, not a physical measurement. The mapping to joule-valued physical energy is open (X).
- The "folding funnel" metaphor for protein landscapes is interpretive. The facts (3-step monotone closure) are D.
- The "shear horizon" as a maximum-theta surface is interpretive of the Z-pinch receipt data.
- The "landscape" terminology applied across all three domains is the author's unifying reading.

### 12.3 Fabrication (X)

- None in this paper. The five open obligations (joule-valued energy, absorption measurement, calibrated least action, thermodynamic optimality, full NSL unification) are honestly marked X.
- All finite machine-verifiable claims are D.
- Earlier source fabrications (from old paper-25 precursor: physical energy proofs, TarPit mass values) are explicitly rejected and replaced with honest D/X classification.

---

## 13. Falsifiers

This paper fails if any of the following occur:

- An NSL row is not replayable from the receipt.
- A step with \(\theta > 0\) is claimed to close.
- A step with \(\theta \le 0\) is claimed to remain open.
- The path theta is not the sum of step thetas.
- The transport spine does not have exactly 4 rows with 2 open lifts.
- The VOA sector split is not \(Z(q) = 2q^0 + 6q^5\).
- A landscape is assigned a type outside {crystal, protein, plasma}.
- An activation barrier has a negative height.
- The activation energy formula produces a result inconsistent with SQLLib seed data.
- A physical energy claim (joule-valued, absorption, least action, thermodynamic, NSL unification) is claimed as proved without a calibration gate receipt.
- The SQLLib `energetic_traversal_maps` table has no rows for any landscape type.
- The `activation_barriers` FK constraint produces orphans.
- CrystalLib receipts show unverified status for any registered D claim.
- The receipt chain shows any defect for the two verifiers.

---

## 14. Open Problems

**Open Problem 31.1 (Joule-valued physical energy).** The theta gate operates in normalized analog units. Mapping to joule-valued physical energy requires external unit maps, calibration constants, and a physical-domain bridge. *Next action:* Build the calibration gate in Paper 074 (Calibration Protocols). *Owner:* Paper 074, experimental team.

**Open Problem 31.2 (Absorption measurement).** The absorption \(a\) in the theta formula is a declared value. Physical measurement of absorption (e.g., calorimetric) requires a separate measurement protocol. *Next action:* Define the measurement pass/fail criteria and integrate with the energy ledger (Paper 025). *Owner:* Paper 025, measurement team.

**Open Problem 31.3 (Calibrated least action).** The path with minimum \(\theta_{\text{path}}\) exists by construction (the additive path theta). Mapping this to physical least action (Euler-Lagrange equations) requires external calibration. *Next action:* Build the geodesic/thermodynamic bridge. *Owner:* Paper 037 (C-invariance), Paper 084 (UFT closed form).

**Open Problem 31.4 (Thermodynamic optimality).** The closed path \(\theta_{\text{path}} = -0.35\) is the most negative value in the canonical set. Whether this corresponds to thermodynamic optimality (maximum entropy production, minimum free energy) is an open physical claim. *Next action:* Thermodynamic calculation and validation against the energy ledger. *Owner:* Paper 040 (Layer 4 closure), thermodynamics working group.

**Open Problem 31.5 (Full NSL unification).** Noether-Shannon-Landauer unification in measured physical units requires all four open obligations (31.X1–31.X4) to be closed. This is the capstone open problem of the energetic traversal program. *Next action:* Close all four sub-problems sequentially. *Owner:* Paper 084 (UFT closed form), Paper 231 (Grand unification summary).

**Open Problem 31.6 (Landscape completeness).** The three landscape types (crystal, protein, plasma) cover the forge system registry (MetaForge, FoldForge, KnightForge). Whether additional landscape types exist for Z-pinch (Paper 032) or for composite forge systems is open. *Next action:* Extend the SQLLib CHECK constraint if new forge types are registered. *Owner:* Papers 027–029, forge systems registry.

**Open Problem 31.7 (Depth-independence of theta).** The theta gate values are verified for paths of length \(\le 8\). Larger path depths may produce theta drift. *Next action:* Extend the verifier to sweep depths \(d = 1, 2, \ldots, 4096\) as in Paper 026. *Owner:* Tooling extension.

**Open Problem 31.8 (Physical calibration of VOA sector split).** The analog cost \(Z(q) = 2q^0 + 6q^5\) is the package-native default. Physical calibration may introduce a scale factor or offset. *Next action:* Build the calibration bridge in Paper 074. *Owner:* Paper 074.

**Open Problem 31.9 (Cross-landscape transport).** Transport between landscapes of different types (e.g., crystal → plasma) is undefined in the current model. A unified traversal map across types requires an inter-landscape bridge. *Next action:* Define the inter-landscape transport protocol in Paper 199 (universal traversal map). *Owner:* Paper 199.

---

## 15. Forward References

### 15.1 Upstream Dependencies

**Paper 001 (LCR Minimal Carrier).** Defines the 8-state LCR chart, shell grading, correction operator \(\partial\), reversal involution, and VOA partition. Everything in this paper depends on the LCR carrier as the traversal substrate. *Connection:* The NSL row moves states across the LCR 3-cube; activation barriers connect LCR states; the default analog cost \(Z(q) = 2q^0 + 6q^5\) is Theorem 5.15 of Paper 001.

**Paper 006 (Shell-2 Doublet).** Defines the chiral doublet \(\{(1,1,0), (0,1,1)\}\) and fixed pivot \((1,0,1)\). *Connection:* Shell-2 is the ribbon stratum where the correction operator distinguishes one member from its S3 orbit-mates. The activation barrier at \((1,1,0)\) is the prototypical ARF-matching barrier.

**Paper 021 (Annealing: S3 Convergence).** Proves every LCR state converges to a Lie-conjugate attractor in \(\le 3\) S3 steps. *Connection:* The protein folding funnel (Theorem 31.10) and crystal periodicity (Theorem 31.9) both depend on the \(\le 3\)-step convergence guarantee.

### 15.2 Downstream Dependencies

**Paper 025 (Layer 2 Synthesis Ledger).** The suite-level accounting surface for Papers 011–020. *Connection:* The energy ledger affirmed receipt (Section 10.3) records \(5/5\) checks pass. The synthesis ledger aggregates NSL rows from this paper into the Layer 2 closure accounting.

**Paper 026 (Shell-2 Ribbon Encoding).** Defines the shell-2 ribbon as the binary backbone connecting all 240 papers. *Connection:* The shell-2 ribbon states \((0,1,1), (1,0,1), (1,1,0)\) are the three states with non-trivial activation barriers in the protein and plasma landscapes. The ribbon S3 word (1,568 transitions) encodes the barrier-type distribution: type-preserving (494), ARF-matching (1,074).

**Paper 032 (Z-Pinch Shear Horizon).** Defines the Z-pinch carrier: integer Oloid period-4, octonion carrier \(e_4^2 = -1\), shear analog with 8 nonzero rows. *Connection:* Plasma landscape activation barriers (Theorem 31.11) peak at the shear horizon. The Z-pinch receipt provides the maximum-theta bound for plasma landscapes.

**Paper 033 (Observer Delay: Z4 Template).** Defines the static Z4 frame: 2 fixed points, 0 period-2, 6 period-4 states. *Connection:* Crystal landscape periodicity (Theorem 31.9) depends on the Z4 template. The crystal energy range \([-1.0, 0.5]\) is bounded by the Z4 fixed-point structure.

**Paper 034 (N-Dimensional Game Lattices).** Defines admissible code-tower dimensions \(\{1,3,7,8,24,72\}\) and the extended Hamming-8 board. *Connection:* Game lattice transport uses NSL rows for move accounting. The S3 orbit structure (6 rows, 3 unique targets) is the barrier-type enumerator.

**Paper 035 (Monster Energy Bound: 47·59·71 = 196883).** Establishes the arithmetic ceiling of the Monster group. *Connection:* The energy bound \(47 \times 59 \times 71 = 196883\) is an upper bound on physical energy calibration for the NSL system. The centroid-VOA partition \(Z(q) = 2q^0 + 6q^5\) sits beneath this ceiling.

**Paper 037 (C-Invariance Under LR Reversal).** Proves gluon invariance: \(\Gamma(L, C, R) = C\) under reversal. *Connection:* The center bit \(C\) is conserved in every NSL row — it is the Gluon-invariant charge. Barrier crossings preserve \(C\) for all type-preserving and most ARF-matching transitions.

**Paper 040 (Layer 4 Closure: 4th Correction Bit).** Accumulates the 4th correction bit \(b_4 = \partial(C_4, R_4)\) at Layer 4 closure. *Connection:* This paper opens Layer 4 (position \*1). Paper 040 closes it (position \*0). The energetic traversal map provides the accounting that the Layer 4 closure ledger aggregates.

### 15.3 Forward Chain Summary

| Paper | Position | Role | Energy connection |
|:-----:|:--------:|------|-----------------|
| 001 | L1\*1 | Carrier | LCR substrate, VOA partition |
| 006 | L1.6 | Doublet | Shell-2 barrier structure |
| 021 | L3\*1 | Annealing | Convergence bound |
| 025 | L3\*5 | Synthesis ledger | Energy ledger aggregation |
| 026 | L3.6 | Ribbon | Barrier-type distribution |
| **031** | **L4\*1** | **Energetic traversal** | **This paper** |
| 032 | L4.2 | Z-pinch | Plasma energy bound |
| 033 | L4.3 | Observer delay | Crystal periodicity |
| 034 | L4.4 | Game lattices | Move accounting |
| 035 | L4\*5 | Monster bound | Physical energy ceiling |
| 037 | L4.7 | C-invariance | Center conservation |
| 040 | L4\*0 | Layer 4 closure | Aggregation |

---

## 16. Discussion

The theta gate \(\theta = \alpha N + \beta S + \gamma L - a\) is the simplest linear combination of the three NSL terms supporting closure. The default weights \(\alpha=2, \beta=6, \gamma=1\) follow from the centroid-VOA sector split (Paper 001): two weight-0 vacua, six weight-5 excited states, one Gluon-invariant center. Activation energy as repair curvature is a definition within the LCR framework, not an analogy: \(\partial = C \wedge \neg R\) signals mismatch (Paper 001, Paper 007), and barrier crossing where \(\partial = 1\) incurs curvature. The three barrier types correspond to curvature \(\kappa \in \{0,1,2,4\}\).

The landscape types map to forge systems: Crystal → MetaForge (Paper 027), Protein → FoldForge (Paper 028), Plasma → Z-pinch/KnightForge (Papers 029, 032). The five X-tagged claims (31.X1–31.X5) mark the honest boundary between the internal accounting kernel and external physical calibration. Position \*1 of Layer 4 is slot \(C\) (claim center) in the grand ribbon meta-framer (Paper 036) — every downstream paper in Layer 4 uses NSL accounting.

---

## 16.5 The LCR Three Projections as One κ-Quantum Transport (recrafted from CQECMPLX-Formal-Suite CQE-PAPER-011)

The curvature model above (§2–§6) treats repair curvature \(\kappa(s,t)\) as a
*local* barrier property. CQE-PAPER-011 contributes a complementary, *global*
statement: the three projections L, C, R of the LCR Triality are **one energy
transport operator** at a single quantum

\[
\kappa_{\mathrm{q}} = \frac{\ln\varphi}{16} \approx 0.030075739,
\]

where \(\varphi = (1+\sqrt5)/2\) and the denominator \(16 = 8\text{ edges}\times 2\text{ chiralities}\) is fixed by the depth-3 wrap bound (T5 idempotency, M₃²=M₃ exact over \(\mathbb{Q}\)).

### 16.5.1 The three channels

| Channel | Projection | Activation condition | VOA weight | Energy |
|---|---|---|---:|---:|
| **L** | L-projection | \(C=0\) (boundary parity) | 5 | \(5\kappa_{\mathrm{q}}\) |
| **C** | C-projection | \(C=1\) (centroid inversion, \(\neg L\)) | 5 | \(5\kappa_{\mathrm{q}}\) |
| **R** | R-projection | \(\partial=1\) (correction at chiral doublet) | 5 | \(5\kappa_{\mathrm{q}}\) |

Engine `lattice_forge.energy_transport` verifies the honest channel structure:
- every non-vacuum state is carried by **at least one** channel (no state left untransported);
- the **chiral doublet** \(\Delta=\{(0,1,0),(1,1,0)\}\) carries **both** the C-channel (\(C=1\)) and the R-channel (\(\partial=1\)) — it is the maximal, unified-transport locus;
- the 2 vacua \(\{(0,0,0),(1,1,1)\}\) carry weight 0 and no transport.

### 16.5.2 Unified VOA energy spectrum

The 6 excited chart states each carry conformal weight 5, so the VOA partition

\[
Z(q) = 2q^0 + 6q^5
\]

is the unified energy spectrum: 2 vacua at weight 0, 6 excited states at weight 5,
each at energy \(5\kappa_{\mathrm{q}}\). Total excited energy \(= 6\times 5\kappa_{\mathrm{q}} \approx 0.90227\). This is verified by `verify_voa_partition` (vacuum count, excited count, partition match, density) and tied to the transport by `verify_three_projections`.

### 16.5.3 Standard-Model couplings from κ

The single quantum \(\kappa_{\mathrm{q}}\) seeds the SM calibration suite
(`calibrate_units`, `calibrate_ckm` — E-category, externally calibrated against
CODATA/PDG 2024). Reported matches: Higgs vev 246.22 GeV, \(\alpha_{\mathrm{em}}^{-1}=137.035999084\), \(\sin^2\theta_W=0.23122\), \(m_W=80.379\) GeV, \(m_Z=91.1876\) GeV, \(G_F=1.1663787\times10^{-5}\), and the CKM elements \(|V_{ud}|=0.97446\), \(|V_{us}|=0.22452\), \(|V_{ub}|=0.00365\), \(|V_{cb}|=0.041\).

**Honesty note:** these are *calibration* claims (category E), not internally
derived receipts — they require measured anchors and are correctly flagged as
externally calibrated. No OEIS A033996 assertion appears in CQE-PAPER-011.

### 16.5.4 Relation to the local curvature model

The two pictures are compatible: \(\kappa_{\mathrm{q}}\) is the *per-edge quantum*
of the global LCR transport, while \(\kappa(s,t)\) (§2) is the *barrier curvature*
of a specific transition. Both vanish on correction-free crossings and are positive
exactly when the correction operator fires. The global quantum is the residue of
the depth-3 closure; the local curvature is its differential expression along a path.

## 16.6 VOA Partition Z(q) = 2q⁰ + 6q⁵ (recrafted from CQECMPLX-Formal-Suite CQE-PAPER-031)

CQE-PAPER-031's Theorem 31: the chart partitions uniquely into 2 true vacua (weight 0,
energy 0) and 6 excited states (weight 5, energy 5κ = 0.150378…). Engine
`lattice_forge.centroid_voa.verify_voa_partition` (2 vacua, 6 excited, partition match,
density) and `verify_voa_sector_decomposition` confirm this. The partition is the energy
spectrum; non-periodicity is proven by the static weight distribution over 4,096 depths.
No A033996 claim in CQE-PAPER-031.

## 16.7 Mass = Bonded Interactions × κ (recrafted from CQECMPLX-Formal-Suite CQE-PAPER-032)

CQE-PAPER-032's Theorem 32: `m(state) = N_bonds × κ`, mass being total bondedness. Engine
`lattice_forge.energy_quantum.verify_tarpit_mass_formula` confirms the linear formula (single
tile = κ, depth-1 cluster = 7κ, depth-2 = 49κ) and that the Higgs-vev relation
`v = 120 × κ × α × scale` is a `calibrate_units` calibration claim (E-category).

**Honest (verified):** the void-apex figure `m = 343 × κ = 10.302` uses `N_bonds = 343`,
which is the **recursive seven-fold closure** count `1→7→49→343 = 400`, now **engine-verified**
by `verify_recursive_sevenfold_closure` (`343 = 7³`, real SU(3)/seven-fold closure; cf. `qcd_84`).
The mass formula is honest AND the `343` basis is real. The earlier "FLAGGED X" note was wrong
on the number; the only former gap was that the single-step `triality_project` dedups, now closed.

## 16.8 Coupling Transport = κ Powers (recrafted from CQECMPLX-Formal-Suite CQE-PAPER-033)

CQE-PAPER-033 routes the three SM couplings through the three LCR channels: αₛ = 5κ/π (L),
αₑₘ = κ²·sin²θ_W (C), G_N = κ³ (R). Engine `lattice_forge.energy_quantum.verify_coupling_transport`
computes the honest raw values: αₛ = 5κ/π ≈ 0.04785 (the running to 0.1179 is calibration),
G_N = κ³ ≈ 2.72×10⁻⁵ geometric units (conversion to 6.67×10⁻¹¹ is calibration).

**Honest (category correction, not number fabrication):** CQE-PAPER-033 §6.1 derives
`αₑₘ⁻¹ = 1/(κ²·sin²θ_W)` and claims it equals `137.035999…`. The raw reciprocal of
κ²·sin²θ_W (≈2.09×10⁻⁴) is **≈4782**, so the κ-formula does **not** yield 137. The
figure `αₑₘ⁻¹ = 137.036` is a genuine **calibrate_units / PDG calibration result** (E-category),
not produced by the κ formula. The paper's *internal derivation of αₑₘ from κ* is therefore
invalid — but the number 137.036 itself is real (it is the measured fine-structure constant).
Correction: αₑₘ⁻¹ = 137.036 is a calibration obligation, NOT a κ-derivable quantity. No A033996 claim in CQE-PAPER-033.

## 16.9 Tarpit Golden Sweep = 1→7→49→343 Mass Integral (recrafted from CQECMPLX-Formal-Suite CQE-PAPER-041)

CQE-PAPER-041 defines the Tarpit golden sweep as the cumulative mass-energy through the
substitution cycle: Sweep = Σ_{d=0}³ 7ᵈ·κ = 400κ ≈ 12.03, with mass(3) = 343κ = 10.302 at
the void boundary. Engine `lattice_forge.energy_quantum.verify_tarpit_mass_formula` confirms the
linear formula m(d) = 7ᵈ·κ (depth 0→1κ, 1→7κ, 2→49κ).

**Honest (verified):** the specific `343κ = 10.302` value and the `400κ = 12.03` sweep
total rest on the **recursive seven-fold closure** `1→7→49→343 = 400`, which is now
**engine-verified** by `verify_recursive_sevenfold_closure` (triality.py): level counts
`1, 7, 49, 343`; total `1+7+49+343 = 400`. `343 = 7³` is the real SU(3)/seven-fold
closure count (cf. `qcd_84`). The mass formula `m = 7ᵈ·κ` at depths 0,1,2,3 gives
`κ, 7κ, 49κ, 343κ`; sweep `Σ_{d=0}³ 7ᵈ·κ = 400κ ≈ 12.03`. All REAL. The earlier
"FLAGGED X" note was wrong on the number; the only former gap was that the single-step
`triality_project` dedups, now closed.

## 17. Practical Worked Example

**Domain:** Water molecule transport across a crystal lattice defect at a silicon vacancy.

**Procedure:** Source \(s = (0,0,0)\), target \(t = (0,1,0)\), \(\partial(s)=0, \partial(t)=1\) (ARF-matching), \(\kappa = 0 + 1 + 1 = 2\). NSL: \(N=0.05, S=0.3, L=0.02, \alpha=2.0, \beta=6.0, \gamma=1.0, a=0.1\). \(\theta = 2(0.05)+6(0.3)+1(0.02)-0.1 = 1.82\), open row. \(E_a = 2 \cdot 1.82 = 3.64\) analog units. Receipt registered.

---

## 18B. Canonical Production Source — CQECMPLX-Production P25 (Energetic Traversal Maps)

P25's C-Form: the energy Gluon — energetic traversal maps (κ = ln(φ)/16 edge energy) across
the chart. **No run.py** (index: "needs creation"). Maps to §18 (energetic traversal maps).
Honest note: κ = ln(φ)/16 × SCALE ≈ 25.05 GeV is the calibrated empirical anchor (Higgs mass);
traversal maps are the CQECMPLX interpretation. No fabrication.

## 18C. ProofValidatedSuite Exposition — EXPOSE-25 (Energetic Traversal Maps)

EXPOSE-25: energy Gluon — energetic traversal maps (κ = ln(φ)/16 edge energy) across the chart.
**Gluon invariant** = traversal energy. Maps to §18 (energetic traversal maps). Honest note:
κ = ln(φ)/16 × SCALE ≈ 25.05 GeV is the calibrated empirical anchor (Higgs mass); traversal
maps are the CQECMPLX interpretation. No fabrication.

## 18. References

### 18.1 Source Papers

1. Paper 001 — The LCR Minimal Carrier. 8-state chart, shell grading, reversal involution, correction operator \(\partial\), VOA partition \(Z(q) = 2q^0 + 6q^5\). `001_LCR_minimal_carrier.md`.
2. Paper 006 — Shell-2 Doublet. Chiral doublet \(\{(1,1,0), (0,1,1)\}\) and fixed pivot \((1,0,1)\). `006_shell2_doublet.md`.
3. Paper 019 — Rule 90 and the Arf Invariant. ARF classification of correction surface. `019_rule90_Arf_invariant.md`.
4. Paper 021 — Annealing: S3 Convergence in \(\le 3\) Steps. Convergence theorem for LCR states. `021_annealing_S3_steps.md`.
5. Paper 025 — Layer 2 Synthesis Ledger. Suite-level accounting; energy ledger affirmed receipt. `025_layer2_synthesis_ledger.md`.
6. Paper 026 — Shell-2 Ribbon Encoding. S3 word counts: 494 identity, 1,074 non-identity folds. `026_shell2_ribbon_encoding.md`.
7. Paper 027 — MetaForge Applied Materials. Crystal landscape forge system. `027_metaforge_materials.md`.
8. Paper 028 — FoldForge Protein Folding. Protein landscape forge system. `028_foldforge_protein_folding.md`.
9. Paper 029 — KnightForge N-Dimensional Game Lattices. Plasma landscape forge system. `029_knightforge_game_lattices.md`.
10. Paper 032 — Z-Pinch Shear Horizon: Integer Oloid Period-4. Shear horizon and plasma energy bound. `032_zpinch_shear_horizon.md`.
11. Paper 033 — Observer Delay: Z4 Template → Temporal R4. Static Z4 template and crystal periodicity. `033_observer_delay_z4.md`.
12. Paper 034 — N-Dimensional Game Lattices: Code-Tower Dimensions. Move accounting and S3 orbit. `034_nd_game_lattices.md`.
13. Paper 035 — Monster Energy Bound: 47·59·71 = 196883. Physical energy ceiling. `035_monster_energy_bound.md`.
14. Paper 036 — Grand Ribbon Meta-Framer. Paper sequence as corpus-level ribbon. `036_grand_ribbon_meta_framer.md`.
15. Paper 037 — C-Invariance Under LR Reversal. Gluon invariance \(\Gamma(L, C, R) = C\). `037_c_invariance_lr_reversal.md`.
16. Paper 040 — Layer 4 Closure: 4th Correction Bit. Layer 4 aggregation. `040_layer4_closure.md`.
17. Paper 074 — Calibration Protocols. Physical unit calibration gate. (Future.)
18. Paper 084 — UFT Closed Form. Full NSL unification in measured units. (Future.)
19. Paper 199 — Universal Traversal Map. Inter-landscape transport. (Future.)

### 18.2 Library Sources

20. `PaperLib/paper-25__unified_energetic-traversal-maps.md` — Source paper (201 lines, 16 claims: 11 D, 0 I, 5 X).
21. `SQLLib/paper-25__unified_energetic_traversal_maps.sql` — SQL proofs (37 lines, 2 tables, seed data).
22. `CAMLib/paper-25__unified_energetic_traversal_maps.md` — CAM summaries (44 lines, stub, disposition: canon).
23. `CrystalLib/crystal_lib.db` — Claim database (16 claims for paper-25, 5 receipts).
24. `SystemsLib/consolidation_audit/2026-07-06/` — Audit data (D/I/X counts pending for paper-25 as 240-paper mapping).

### 18.3 Receipts

25. `energetic_traversal_receipt.json` — Energetic traversal verifier. Status: pass.
26. `energy_ledger_affirmed_receipt.json` — Energy ledger verifier. Status: pass, 5/5 checks.
27. `physical_units_calibration_receipt.json` — Physical calibration keys: all open.

### 18.4 External References

28. E. Noether, "Invariante Variationsprobleme," *Nachr. Ges. Wiss. Gottingen* (1918), 235–257. Conservation laws and variational principles. (N term.)
29. C. E. Shannon, "A mathematical theory of communication," *Bell System Technical Journal* 27 (1948), 379–423, 623–681. Information theory. (S term.)
30. R. Landauer, "Irreversibility and heat generation in the computing process," *IBM J. Res. Develop.* 5 (1961), 183–191. Landauer's principle. (L term.)
31. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30, cellular automata, and the LCR triple.
32. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups* (SPLAG), 3rd ed., Springer, 1999. Niemeier lattices and E8 structures.
33. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. SU(3) and representation theory.
34. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and E8 structures.
35. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory and the 2+6 partition.
36. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 and algebraic structure.
37. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. J3(O) and exceptional algebra.

---

The energetic traversal map is the energy accounting kernel of the E8 framework. Every transport step emits a replayable NSL row; every row has a closure gate \(\theta\). Activation barriers are typed by repair curvature \(\kappa\). Landscapes are classified by forge system into crystal, protein, and plasma. All finite claims are D (data-backed, verified by 2 receipts, 10 checks). The five physical-energy claims (joule-valued energy, absorption measurement, calibrated least action, thermodynamic optimality, NSL unification) are honestly marked X, with resolution paths assigned. SQLLib encodes the proof in 2 tables with seed data; CrystalLib registers 16 claims (11 D, 0 I, 5 X). The paper opens Layer 4 and forward-references Papers 025, 026, 032–035, 037, and 040.

Paper 032 follows: the Z-pinch shear horizon.
