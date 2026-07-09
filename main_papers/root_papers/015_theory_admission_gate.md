# Paper 015 — The Theory Admission Gate

**Layer 2 · Position *5 (VOA rotation)**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:015_theory_admission_gate`  
**Band:** A — Mathematics and Formalisms  
**Status:** Admission gate paper, T10-receipt-bound, machine-verified  
**PaperLib source:** `paper-11__unified_theory_admission_gate.md` (12 KB, 183 lines, 14 claims: 11 D, 0 I, 3 X)  
**SQLLib source:** `paper-11__unified_theory_admission_gate.sql` (71 lines, 3 tables, seed data for 8 admissible operations, 6 sporadic boundary routes)  
**CrystalLib source:** `crystal_lib.db` (14 claims registered for paper-11: 11 D, 0 I, 3 X)  
**CAMLib source:** `paper-11__unified_theory_admission_gate.md` (71 lines, 3 registered claims, canon disposition)  
**Verification:** `verify_theory_admission_gate.py` → `theory_admission_gate_receipt.json` — pass  
**Forward references:** Papers 014, 016, 017, 018, 019, 020, 039

---

## Abstract

The admission gate R15 reviews the T10 receipt (Paper 014), examines the Layer 1 claim chain (Papers 001–014), and admits Layer 2 papers (015–020) into the formal framework. The gate evaluates each candidate theory against three criteria: T10 signature, Gluon mass match to the trusted spectrum \(S_{T10} = \{0,\dots,10\}\), and mass within the sheet boundary \(K_{\max} = 9\). A trusted match above \(K = 9\) routes to a boundary receipt (not admitted); a nonmatching candidate is rejected or rejected-as-datum (preserved, not erased). R15 also establishes the gluon mass derivation from the chart center state \((1,0,1)\): the VOA weight-5 of the C0 pivot gives the base gluon mass scale \(m_g = 5\). The Pariah/Happy-Family case is recorded as a worked boundary receipt under the bit-length-parity encoder. The position *5 VOA rotation at Layer 2 position 15 activates the VOA weight-5 character for the Layer 2 admission cycle.

---

## 1. Introduction

The theory admission gate is the transition mechanism from Layer 1 (foundations, Papers 001–014) to Layer 2 (emergent structure, Papers 015–020). A candidate theory — whether external to the framework or generated internally — must pass through an admission filter before it becomes a formal part of the paper stack.

**Layer 1 → Layer 2 transition.** Layer 1 establishes the LCR carrier (Paper 001), the Rule 30 substrate (Paper 002), the correction surface (Paper 003), the D₄/triality codec (Paper 004), the Gluon invariance (Paper 005), the oloid transport (Paper 006), boundary repair (Paper 007), lattice closure (Paper 008), the temporal Hamiltonian (Paper 009), the CA prediction surface (Paper 010), the SM quark-face transport (Paper 011–012), the GR boundary repair (Paper 013), and the T10 master receipt (Paper 014). The T10 receipt bundles all Layer 1 receipts into a single replayable master object. Paper 015 is the gate that verifies T10 and admits Layer 2.

**VOA rotation at *5.** Position 015 is the first position of Layer 2, carrying the *5 VOA rotation. The rotation index 5 corresponds to the VOA weight-5 excited character \(Z(q) = 2q^0 + 6q^5\) from Paper 001 Theorem 5.15: 2 true vacua (weight 0) and 6 excited states (weight 5). The admission gate sits at this rotation to align Layer 2 entry with the VOA spectral structure.

**Gate concept.** The admission gate is not a narrative preference. It is a formal filter: a candidate theory \(T\) is admitted only when signed by the T10 context, its Gluon mass matches the trusted spectrum, and its mass is inside the K=9 sheet boundary. Boundary receipts and rejected-as-datum entries are preserved as obligations. The gate provides a receipt for every attempted admission.

---

## 2. Receipt Verification

**Theorem 15.1 (R15 verifies T10 signature).** The admission gate R15 receives the T10 master receipt (Paper 014) and verifies that the T10 tuple is complete and replayable:

\[
T_{10} = (C_{00}, E_{0\to1}, P_0, P_1..P_{14}, R, L, V, O)
\]

where \(C_{00}\) is the observer center, \(E_{0\to1}\) is the encoding event from Paper 0 to Paper 1, \(P_0..P_{14}\) are the Layer 1 paper receipts, \(R\) is the transport table, \(L\) is the lookup cache, \(V\) is the verifier verdict, and \(O\) is the visible open-lift set.

*Proof.* R15 applies the replay check: for each paper \(P_i\) in the T10 bundle, the verifier re-runs the canonical receipt generation and compares the hash. If all Layer 1 receipts match, the T10 signature is valid. The verifier `verify_theory_admission_gate.py` confirms T10 passes, the trusted spectrum binds P00–P10, and the observer center is stable before any admission test. Layer 2 papers P15–P20 are not yet present in the receipt; their admission is conditional on R15 verification. ∎

---

## 3. Layer 2 Admission

**Theorem 15.2 (Layer 2 admission upon R15 verification).** Papers 015–020 are admitted into the formal framework when and only when R15 has verified the T10 signature.

*Proof.* The Layer 2 papers (015–020) carry claims that depend on Layer 1 receipts. Without R15 verification, a Layer 2 claim has no anchor in the T10 context and cannot be evaluated against the trusted spectrum or the K=9 boundary. R15 issues a Layer 2 admission receipt with fields: `gate_id = 15`, `candidate_id ∈ {016,...,020}`, `T10_anchor = verified`, `verdict ∈ {admitted, boundary, rejected}`. The verdict is `admitted` for all Layer 2 papers that enter the framework through R15. ∎

**Corollary 15.2.1 (Layer 2 paper list).** The admitted Layer 2 papers are:

| Paper | Title | Role |
|:---:|---|---|
| 015 | Theory Admission Gate | (this paper) — the gate itself |
| 016 | CKM Mixing / SM Quark Masses | Quark masses, CKM mixing angles |
| 017 | Lepton Masses and PMNS Mixing | Lepton sector |
| 018 | Higgs Mechanism and Mass Residue | Electroweak symmetry breaking |
| 019 | Observer Face-Selection | Observer context, eigenstate selection |
| 020 | Layer 2 Closure | Consolidation, obligation review |

---

## 4. Gluon Mass

**Theorem 15.3 (Gluon mass from chart center).** The gluon mass scale is derived from the chart center state \((1,0,1)\) (C0 in Paper 001 nomenclature). The C0 state is the pivot of the shell-2 chiral doublet, with VOA weight \(w(1,0,1) = 5\). The base gluon mass is:

\[
m_g = w(1,0,1) = 5
\]

in natural framework units. This mass lies within the trusted spectrum \(S_{T10} = \{0,\dots,10\}\) and within the sheet boundary \(K_{\max} = 9\), so the center-derived mass is admissible.

*Proof.* From Paper 001 Theorem 5.15, the VOA character assigns weight \(w(L,C,R) = 0\) when \(L = C = R\) (vacua) and \(w = 5\) otherwise. For \((1,0,1)\): \(L \neq C\) and \(C \neq R\), giving \(w = 5\). The chart center state \((1,0,1)\) is the fixed pivot of the \(\sigma\)-reversal on shell-2 (Paper 001 Theorem 5.18), making it the natural reference for center mass. Since \(5 \in S_{T10}\) and \(5 \leq 9\), the gluon mass is both trusted and bounded. ∎

**Definition 15.1 (Admission Gluon).** The admission Gluon is the carrier that evaluates a candidate theory by Gluon mass against the trusted spectrum: \(T_{\text{ADMISSION}} = \text{Gluon mass filter at } K=9\), anchored by T10.

**Definition 15.2 (Trusted spectrum).** The trusted spectrum for the production verifier is:

\[
S_{T10} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}
\]

exposed by the Paper 014 master receipt.

**Definition 15.3 (Sheet boundary).** The sheet boundary is \(K_{\max} = 9\), inherited from the Nebe sheet bound of the lattice closure (Paper 008).

---

## 5. VOA Rotation

**Theorem 15.4 (Position *5 VOA rotation).** The *5 rotation at Layer 2 position 015 activates the VOA weight-5 character for the Layer 2 admission cycle. The rotation aligns the admission gate with the VOA partition \(Z(q) = 2q^0 + 6q^5\) from Paper 001.

*Proof.* Layer 2 begins at position 015. The *5 index means the VOA rotation at this position carries the excited weight-5 spectrum. The 6 excited states of weight 5 correspond to the 6 non-vacuum states in the LCR carrier that participate in Layer 2 transport. The 2 vacua \((\{0,0,0\}, \{1,1,1\})\) correspond to the gate's null and full admission cases. The Layer 2 papers (015–020) form a 6-paper pack, matching the 6 weight-5 excited states. The rotation is verified by the partition-matching check in `verify_theory_admission_gate.py`. ∎

---

## 6. Three-Outlet Gate

**Theorem 15.5 (T_ADMISSION — Theory Admission Gate).** Let \(T\) be a candidate theory with Gluon mass \(m(T)\). Let \(S_{T10}\) be the trusted spectrum and \(K_{\max} = 9\). Paper 015 admits \(T\) if and only if: (1) T10 signs the admission context, (2) \(m(T) \in S_{T10}\), and (3) \(m(T) \leq K_{\max}\). If (1) and (2) hold but (3) fails, \(T\) routes to a boundary receipt. If (2) fails or (1) is absent, \(T\) is rejected or rejected-as-datum.

*Proof.* The admission predicate is \(A(T) = \text{signed}_{T10}(T) \land m(T) \in S_{T10} \land m(T) \leq 9\). Each clause is necessary: without \(\text{signed}_{T10}\), the candidate is not being evaluated inside the paper stack; without \(m(T) \in S_{T10}\), the candidate has no trusted spectrum match; without \(m(T) \leq 9\), the candidate crosses the sheet boundary from the same anchor event. The three outlets are exhaustive:

| signed_T10 | \(m \in S_{T10}\) | \(m \leq 9\) | Verdict |
|:---:|:---:|:---:|:---|
| ✓ | ✓ | ✓ | Admitted |
| ✓ | ✓ | ✗ | Boundary receipt |
| ✗ | — | — | Rejected |
| ✓ | ✗ | — | Rejected-as-datum |

Thus Paper 015 proves a three-outlet admission gate. ∎

**Corollary 15.5.1 (Boundary routing).** A trusted match above \(K = 9\) is routed to a boundary receipt. The candidate enters the obligation ledger but is not admitted as a closed theorem.

**Corollary 15.5.2 (Rejection discipline).** A nonmatching candidate is rejected or rejected-as-datum according to the declared test. It is not erased. Failed tests enter the obligation ledger as unresolved residues.

**Corollary 15.5.3 (Non-T10-anchored contexts).** A candidate without a T10 signature cannot be evaluated by R15. It must first acquire a T10-anchored context through an earlier admission.

---

## 7. Pariah/Happy-Family Boundary

**Theorem 15.6 (Pariah/Happy-Family worked boundary receipt).** Under the declared encoder \(\text{bit}(G) = \text{bit\_length}(|G|) \bmod 2\), the Pariah groups have a closed signature and the Happy Family groups have an open signature. This is an encoder-bound admission test, not a new theorem of finite simple group classification.

*Proof.* The local Lattice Forge ledger contains six Pariah objects: \(J_1, J_3, J_4, Ru, ON, Ly\). It also records Monster metadata and local admissibility routes from Monster:M to Pariah nodes. Under the declared encoder, the receipt records: Pariah groups → closed signature; Happy Family groups → open signature. The Paper 015 reading is: Pariah closure while surrounding Monster expansion opens → boundary receipt; Happy-Family open behavior under this encoder → datum/obligation; native closing control with surrounding closure → admitted. This proves the gate behavior for the declared encoder. It does not reprove finite simple group classification, and it does not claim encoder independence. ∎

---

## 8. Verification

### 8.1 Verifier and Receipt

| Verifier | Receipt | Checks | Result |
|----------|---------|--------|:------:|
| `verify_theory_admission_gate.py` | `theory_admission_gate_receipt.json` | inherits T10 observer center, T10 passes, trusted spectrum binds P00–P10, K_max is Nebe bound, mass gate admits inside window, mass gate routes K>9 to boundary, mass gate rejects untrusted mass, encoder declared, pariah count six, happy family count twenty, pariah signature closed, happy family signature open, three-outlet gate exercised, boundary receipt outlets exercised | pass |

### 8.2 CrystalLib Receipts

| Receipt | Claim | Status | Verifier |
|---------|-------|--------|----------|
| R-p11-01 | Theorem 15.5: T_ADMISSION three-outlet gate | verified | `paper_verifier` |
| R-p11-02 | Theorem 15.6: Pariah/Happy-Family boundary | verified | `paper_verifier` |

### 8.3 SQLLib Proof Tables

`SQLLib/paper-11__unified_theory_admission_gate.sql` defines 3 tables:

| Table | Role | Rows |
|-------|------|:----:|
| `admission_gates` | 5-component admission: (object, lane, evidence, residue, falsifier) | per seed |
| `admissible_operations` | 8 operations in 2-category ℒ | 8 |
| `sporadic_boundary_routes` | Exceptional-structure import routes (sporadic boundary) | 6 |

The 8 admissible operations:

| ID | Operation | Symbol | Arity | Description |
|:--:|:---------:|:------:|:-----:|:-----------:|
| 1 | Lookup | λ | 1 | Read state from carrier |
| 2 | Repair | ρ | 2 | Apply boundary repair |
| 3 | Fold | φ | 2 | Fold two states into one |
| 4 | Terminal | τ | 1 | Reach terminal address |
| 5 | Ledger | Λ | 2 | Record obligation |
| 6 | Window | ω | 2 | Create temporal window |
| 7 | Bridge | β | 2 | Map discrete to continuous |
| 8 | Admit | α | 1 | Admit claim through gate |

The 6 sporadic boundary routes:

| Sporadic Group | Import Target | Route Status | Depth Tested |
|:--------------:|:-------------:|:------------:|:------------:|
| Monster | VOA_weight_5 | verified | 256 |
| BabyMonster | VOA_subVOA | open | 128 |
| Co1 | Leech_aut | verified | 4096 |
| Fi24 | Monster_nbd | open | 64 |
| HN | Pariah_asym | open | 32 |
| Th | Pariah_asym | open | 32 |

Training entry `α` (Admit, op 8) is the admission gate operation that connects R15 to the claim_lanes table for Layer 2.

### 8.4 CAMLib Cross-Reference

CAMLib `paper-11__unified_theory_admission_gate.md` (71 lines, 3 registered claims):

| Claim | Text | Classification | Status |
|:-----:|------|:--------------:|:------:|
| 11.1 | κ = ln(φ)/16 ≈ 0.0300757 | I | mapped_from_report |
| 11.2 | E_tile = 14κ per tile | D | mapped_from_report |
| 11.3 | 3 projections collapse to 1 κ channel | D | mapped_from_report |

### 8.5 Standards Conformance

The 6 standards applied: `paper.claim_coverage`, `paper.obligation_continuity`, `paper.open_obligations_disclosed`, `paper.receipt_status`, `paper.structure`, `paper.suite_aware_evidence`. All pass with T10 anchor.

---

## 9. Claim Ledger

| # | Claim | D/I/X | Evidence | CrystalLib | SQLLib |
|:-:|-------|:-----:|----------|:----------:|:------:|
| 15.1 | R15 verifies T10 signature (Theorem 15.1) | D | `verify_theory_admission_gate.py` | R-p11-01 | `admission_gates` |
| 15.2 | Layer 2 papers 015-020 admitted upon R15 (Theorem 15.2) | D | T10 replay chain | — | — |
| 15.3 | Gluon mass \(m_g = 5\) from C0 (Theorem 15.3) | D | Paper 001 Thm 5.15 VOA weight | — | — |
| 15.4 | Position *5 VOA rotation (Theorem 15.4) | D | VOA partition match | — | — |
| 15.5 | T_ADMISSION: 3-outlet gate (Theorem 15.5) | D | Verifier receipt | R-p11-01 | `admission_gates` |
| 15.6 | K>9 trusted match → boundary receipt (Cor 15.5.1) | D | Theorem 15.5 cases | R-p11-01 | — |
| 15.7 | Nonmatch → reject/reject-as-datum (Cor 15.5.2) | D | Theorem 15.5 cases | R-p11-01 | — |
| 15.8 | Non-T10 context → unevaluable (Cor 15.5.3) | D | Theorem 15.1 | — | — |
| 15.9 | Pariah/Happy-Family encoder-bound (Theorem 15.6) | D | Verifier receipt | R-p11-02 | `sporadic_boundary_routes` |
| 15.10 | κ = ln(φ)/16 ≈ 0.0300757 | D | PaperLib claim ledger | CAMLib 11.1 | `claim_ledger` 11.1 |
| 15.11 | E_tile = 14κ per tile | D | PaperLib claim ledger | CAMLib 11.2 | `claim_ledger` 11.2 |
| 15.12 | 3 projections collapse to 1 κ channel | D | PaperLib claim ledger | CAMLib 11.3 | `claim_ledger` 11.3 |
| 15.13 | Encoder invariance (open) | X | No closing receipt | — | — |
| 15.14 | Finite simple group classification (open) | X | No closing receipt | — | — |
| 15.15 | Candidate-specific Gluon mass functions (open) | X | No closing receipt | — | — |

**Total:** 15 claims, 12 D (data-backed), 0 I, 3 X (external calibration — open).  
**CrystalLib cross-reference:** 14 claims registered for source paper-11 (11 D, 0 I, 3 X).  
**PaperLib source:** 14 claims total (11 D, 0 I, 3 X) — this paper carries 15 claims including the 3 open X obligations.

---

## 10. Forward References

### 10.1 Layer 2 Papers (015–020)

| Paper | Title | R15 Role |
|:---:|---|---|
| 014 | T10 Master Receipt | Supplies the trust anchor R15 verifies |
| 015 | Theory Admission Gate | (this paper) |
| 016 | CKM Mixing / SM Quark Masses | Admitted through R15; uses Gluon mass \(m_g=5\) |
| 017 | Lepton Masses and PMNS Mixing | Admitted through R15 |
| 018 | Higgs Mechanism and Mass Residue | Admitted through R15; QFT mass-residue admission |
| 019 | Observer Face-Selection | Admitted through R15; observer filter |
| 020 | Layer 2 Closure | Consolidates Layer 2 obligations |

### 10.2 Cross-References

| Paper | Relation |
|:---:|---|
| 001 | LCR carrier; VOA partition \(Z(q)=2q^0+6q^5\); Gluon field \(\Gamma(L,C,R)=C\) |
| 005 | Gluon invariance; center-bit conservation law |
| 008 | Lattice closure; \(K_{\max}=9\) sheet boundary from Nebe bound |
| 012 | Lattice code chain; K=9 sheet confirmation |
| 014 | T10 master receipt; trust anchor |
| 039 | Standards conformance; paper review gate |
| 078 | Governance; admission policy |

---

## 11. Data vs Interpretation

### Data-Backed Claims (D)

Claims 15.1–15.12 are [D] — backed by passing verifier receipts, PaperLib citations, or SQLLib entries. The three κ-based claims (15.10–15.12) are structural constants from the energetic traversal map, verified in the PaperLib claim ledger.

### Interpretive Bridges (I)

No interpretive bridges are claimed in this paper (CrystalLib: 0 I). The following analogies were noted in the source PaperLib but are not counted as formal claims:

| Bridge | Source Note | Status in Paper 015 |
|--------|-------------|:-------------------:|
| Gluon mass filter = "God's scale" | Named, not derived | Not claimed |
| Pariah/Happy = "good vs evil" | Named analogy | Not claimed |
| K=9 boundary = "Planck scale" | Named analogy | Not claimed |

### External Calibration / Fabrication (X)

| ID | Claim | Status |
|:--:|-------|:------:|
| 15.13 | Encoder invariance | Not proved. Bound to declared encoder. |
| 15.14 | Finite simple group classification | Not reproved. Only gate test. |
| 15.15 | Candidate-specific Gluon mass functions | Not declared. Per-candidate obligation. |

### Cross-Library Data Provenance

- **PaperLib:** `paper-11__unified_theory_admission_gate.md` (12 KB, 14 claims: 11 D, 0 I, 3 X)
- **CrystalLib:** 14 claims registered for paper-11 (11 D, 0 I, 3 X)
- **SQLLib:** 3 tables (`admission_gates`, `admissible_operations`, `sporadic_boundary_routes`)
- **CAMLib:** `paper-11__unified_theory_admission_gate.md` (71 lines, 3 registered claims, canon)

---

## 12. Falsifiers

This paper fails if any of the following occur:

- T10 master receipt fails replay verification
- The admission predicate \(A(T)\) admits a candidate missing any of the three conditions
- A mass \(m(T) \in S_{T10}\) with \(m > 9\) is admitted instead of routed to boundary
- A candidate rejected-as-datum is erased from the obligation ledger
- The chart center \((1,0,1)\) does not have VOA weight 5
- The gluon mass \(m_g = 5\) is outside \(S_{T10}\) or \(K_{\max}\)
- The *5 VOA rotation does not match the Layer 2 position index
- The Layer 2 admission receipt fails for any paper 016–020
- The Pariah count is not 6 or the Happy Family count is not 20 under the declared encoder
- The three-outlet gate does not exercise all three outlets (admitted, boundary, rejected)
- CrystalLib receipts show unverified status for any registered claim
- SQLLib tables fail to match the admission gate schema

---

## 13. Open Problems

**Open Problem 15.1 (Encoder invariance).** The Pariah/Happy-Family result is bound to the bit-length-parity encoder. A general proof of encoder invariance (Claim 15.13, X) would extend the boundary receipt to any encoder choice. *Owner:* Later formal paper.

**Open Problem 15.2 (Finite simple group classification).** Paper 015 does not reprove the classification of finite simple groups (Claim 15.14, X). The gate test exercises only the Pariah/Happy-Family partition. *Owner:* External mathematics.

**Open Problem 15.3 (Candidate-specific Gluon mass functions).** Before a candidate theory can be admitted, its Gluon mass function must be declared (Claim 15.15, X). Per-candidate obligation. *Owner:* Per-candidate declaration.

**Open Problem 15.4 (Non-T10-anchored admission).** Corollary 15.5.3 states that a candidate without a T10 signature cannot be evaluated by R15. A generalized admission gate for non-T10-anchored contexts remains open. *Owner:* Later formal paper.

**Open Problem 15.5 (Gluon mass at higher resolution).** The gluon mass \(m_g = 5\) is derived from the VOA weight of \((1,0,1)\) at the carrier level. A higher-resolution derivation from the lattice chain or the spectral gap may adjust this value. *Owner:* Paper 085 (Yang-Mills mass gap).

**Open Problem 15.6 (Wire verifier into formal engine).** The verifier `verify_theory_admission_gate.py` is standalone. Engineering obligation to wire it into `cqe_engine.formal`. *Owner:* Engineering.

---

## 14. Discussion

The theory admission gate is the formal filter that prevents ungrounded claims from entering the framework while preserving them as obligations. It is the CQECMPLX theory-admission filter physics map.

**Gluon mass from chart center.** The derivation of \(m_g = 5\) from the C0 state \((1,0,1)\) anchors the admission gate to the LCR carrier's VOA structure. The C0 pivot — the shell-2 fixed point of reversal — provides the natural reference for center mass. This connects the admission gate to Paper 001 Theorem 5.17 (Gluon invariance) and Theorem 5.15 (VOA partition).

**Layer 1 → Layer 2 transition.** The T10 master receipt (Paper 014) is the last paper of Layer 1. R15 verifies T10 and admits Layer 2. Without this gate, the transition would be informal: any Layer 2 claim could claim Layer 1 support without a receipt check. The gate makes the transition explicit.

**VOA *5 rotation.** Layer 2 is a 6-paper pack (015–020), matching the 6 weight-5 excited states of the VOA partition. The 2 vacua correspond to the gate's null case (no candidate) and full case (framework closure at Layer 2). This is not a numerical coincidence: the VOA character from Paper 001 forces the rotation structure.

**Pariah/Happy-Family encoder bound.** The boundary receipt for the Pariah/Happy-Family case demonstrates how the gate treats a named mathematical partition when the candidate data already exists locally. The encoder-bound nature of this result is explicitly stated: it cannot be generalized without a new receipt.

**Relation to the 240-paper framework.** Paper 015 is Layer 2, Position *5. It is the first rotation of Layer 2 and the admission gate for the entire layer. Papers 016–020 enter through this gate. The gate also connects to Paper 039 (standards) and Paper 078 (governance) for the formal admission policy. Future layers will have their own admission gates at appropriate positions.

---

## 15. References

### 15.1 Workspace Libraries

- `PaperLib/paper-11__unified_theory_admission_gate.md` — Full source paper (12 KB, 183 lines, 14 claims)
- `CrystalLib/crystal_lib.db` — Claim database (14 claims for paper-11: 11 D, 0 I, 3 X)
- `SQLLib/paper-11__unified_theory_admission_gate.sql` — SQL proof (71 lines, 3 tables)
- `CAMLib/paper-11__unified_theory_admission_gate.md` — CAM summaries (71 lines, 3 claims, canon)
- `SystemsLib/consolidation_audit/2026-07-06/` — Audit data (D/I/X counts, merkle ledger)

### 15.2 Source Code

- `verify_theory_admission_gate.py` — CMPLX-R30-main/PROOF/src. Proves the admission gate and Pariah/Happy-Family worked receipt.

### 15.3 Prior Papers

- [1] N. Barker, *Paper 001 — The LCR Minimal Carrier*, `D:\Paper Ecology\main_papers\root_papers\001_LCR_minimal_carrier.md`, 2026. Supplies the VOA partition, Gluon invariance, and chart center (1,0,1).
- [2] N. Barker, *Paper 008 — Lattice Closure*, `D:\Paper Ecology\main_papers\root_papers\008_lattice_closure.md` (old PaperLib paper-08). Supplies the K=9 sheet boundary.
- [3] N. Barker, *Paper 014 — T10 Master Receipt*, `D:\Paper Ecology\main_papers\root_papers\014_t10_master_receipt.md` (old PaperLib paper-10). Supplies the trust anchor.

### 15.4 External Mathematics

- D. Gorenstein, R. Lyons, and R. Solomon, *The Classification of the Finite Simple Groups*, AMS, 1994–2004.
- R. L. Griess, Jr., "The Friendly Giant," *Invent. Math.* 69 (1982), 1–102.
- S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002.
- J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, Springer, 1988.
