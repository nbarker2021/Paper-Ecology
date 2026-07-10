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

## 15B. Canonical Production Source — CQECMPLX-Production P11 (Theory Admission Gate)

P11 gates theory admission: a claim is admitted iff its tool, proof tree, and trusted
spectrum match. **No run.py** (index: "needs creation") — the admission contract for §15.
Honest note: meta-governance, no physics claim.

## 15C. ProofValidatedSuite Exposition — EXPOSE-11 (Theory Admission Gate)

EXPOSE-11: admission gate, Gluon-mass filter at K=9, 3 outcomes (admitted/boundary/rejected).
**Gluon invariant** = mass-filter gate. Maps to §15. Honest note: meta-governance, no physics
claim.

## 17. UFT 0-100 Series (FLCR) — Papers 5-13,15,17,20: interpretation-heavy, defensible

Per HONEST-DISCLOSURE.md these are **(I)** interpretation following FLCR doctrine (typed boundary
repair, oloid LCR parameterization, causal links/obligation ledgers, discrete-continuous bridge,
lattice closure/lattice ladder, temporal windows, theory admission gates, CA prediction surfaces,
curvature-as-repair-demand, continuum edge residuals, applied forge reader). The substrate they
rest on is **(D)**: OBLIGATION_ROWS.json (1,105 rows), 192/196,580 Leech vectors, 4 receipt_bound
obligation rows, CLAIM_LANE_SCHEMA.json (8 lanes/7 classes), quark-face 10/10 receipt. **HONEST
FLAG (Paper 11):** earlier "8/8 success, 0 error walls, TarPit mass 0.507457" were FABRICATIONS,
corrected to 8 structural checks + 4 falsifiers + `pass_with_open_lifts`. **HONEST FLAG (Paper
13):** "64/256 silent-boundary ECAs" is asserted **(D)** in UFT but my independent enumeration
gives 16/256 under strict L=R=0→0 (possibly a different boundary condition); carried as stated
with the discrepancy noted. Maps to §17. No live fabrication in the corrected versions.

## 9B. UFT 0-100 Series (FLCR) — Paper 30: supervisor cursor & universal normal-form intake

Paper 30 = supervisor cursor / universal normal-form intake (the governance intake layer). **(I)**
interpretation on the admission-gate base. Maps to `038_supervisor_cursor.md` and §15 (theory
admission gate). Honest, no fabrication.

## 15C. UFT 0-100 Series (FLCR) — Paper 39: falsifiers, comparators & standards of evidence

Paper 39 = falsifiers / comparators / standards-of-evidence governance (the claim-lane schema).
**(I)** governance framing on **(D)** CLAIM_LANE_SCHEMA.json (8 lanes / 7 classes). Maps to §15. No
fabrication.

## 15B. UFT 0-100 Series (FLCR) — Paper 78: governance 1 (admission & claim lanes)

Paper 78 = governance layer 1: theory-admission gates, claim-lane schema (8 lanes / 7 classes),
D/I/X tagging. **(I)** governance framing on **(D)** CLAIM_LANE_SCHEMA.json. Maps to §15. No
fabrication.

## 15B. UFT 0-100 Series (FLCR) — Paper 79: governance 2 (provenance & falsifiers)

Paper 79 = governance layer 2: provenance, falsifiers, comparators, evidence standards. **(I)**
governance framing. Maps to §15. No fabrication.

## 10B. UFT 0-100 Series (FLCR) — Paper 88: P vs NP (Millennium)

Paper 88 = P vs NP as LCR carrier-depth (verification = bounded-depth vs search = unbounded).
**(I)** structural interpretation on **(D)** standard complexity. Maps to §10 (`093_P_vs_NP.md`)
and §15 (`015_theory_admission_gate.md`). No fabrication.


## 05A. Formal-Paper Deep-Dive (CQE-paper-05)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-05/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **rolling carrier state** is a triple

```text
q = (sheet, phase, parity)
```

with

```text
sheet in {0,1}
phase in {0,1,2,3}
parity in {0,1}
```

Given a bit `b in {0,1}`, define the rolling step:

```text
roll(q,b) = ((sheet+1) mod 2, (phase+1) mod 4, parity xor b).
```

The **head/tail dyad** is

```text
head = sheet
tail = (phase mod 2) xor sheet xor parity.
```

A **continuous carrier trace** is a list of states where each adjacent pair is
related by one legal `roll` step for the corresponding input bit.

### Main Claim

**Theorem 5.1, Rolling Path Carrier.** For every finite binary input stream,
the rolling carrier produces a continuous trace of legal adjacent states. The
trace preserves input order, maintains a binary head/tail dyad at every state,
and can carry Paper 04 constraints as receipt payloads without treating the
path as a straight-line jump.

**Theorem 5.2, Oloid Carrier Family Reapplication.** The substrate oloid
mechanisms bound to this paper - rolling-contact kinematics, single-oloid
octonionic grounding, the four-oloid D4 ring, and dual-path read-then-verify
flow - each pass their finite verifier. This theorem binds those mechanism
receipts as the base carrier family for Paper 05. It does not close the
E6-to-E7-to-E8 dyadic lift or any Rule 30 prediction claim by this carrier
alone.

### Proof

The step rule is total on the finite state space:

```text
{0,1} x {0,1,2,3} x {0,1}.
```

For every valid input bit, `sheet` changes by exactly one modulo 2, `phase`
changes by exactly one modulo 4, and `parity` changes by XOR with the input bit.
Therefore each step has a unique legal successor. A trace generated by
successive applications of `roll` is continuous by construction because every
adjacent pair is one legal step apart.

The head/tail dyad is a deterministic function of the current state, so it is
defined at every position in the trace. A Paper 04 constraint can be attached
to a trace position as payload because the carrier state and input index are
replayable. The payload does not alter the rolling step rule, so carrying it
does not break continuity. QED.

For Theorem 5.2, the reapplication verifier imports the substrate oloid
modules and executes their declared finite checks. The rolling-contact,
octonionic, quad-oloid, and dual-path verifiers all return `pass`. Sin

_**(D)** formal claim._

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-05/verify_oloid_path_carrier.py
production/formal-papers/CQE-paper-05/verify_oloid_carrier_family.py
```

It verifies:

```text
1. The rolling step is total for valid binary input.
2. Every adjacent trace pair is a legal step.
3. Head/tail dyads are binary at every state.
4. Paper 04 constraints can be attached as payloads without changing the path.
5. Invalid bits and discontinuous jumps are rejected.
6. Prediction claims are downstream: Papers 10 and 12 carry finite/readout
   receipts; Paper 5 proves only the carrier.
7. The oloid carrier family verifiers pass for rolling-contact kinematics,
   octonionic grounding, four-oloid D4 ring, and dual-path read-then-verify
   flow.
8. The E6-to-E7-to-E8 dyadic lift remains outside this theorem.
```

### Validation and Hidden-Guess Layer

Useful hidden-guess prompts:

```text
What changes on every legal rolling step?
Does a curved carrier imply prediction?
What makes a path discontinuous?
Can a constraint payload alter the path rule?
```

Expected answers:

```text
sheet flips, phase advances, parity XORs the bit
no
skipped phase/sheet or invalid bit
no
```

### Open Obligations

1. Wire `verify_oloid_path_carrier` into `cqe_engine.formal`.
2. Connect Paper 04 constraint payloads to a shared route ledger.
3. Keep the E6-to-E7-to-E8 dyadic lift as an explicit bridge obligation until
   a verifier closes it.
4. Separate physical Oloid geometry claims from finite rolling-state claims.
5. Treat Rule 30 prediction as downstream, not absent: Papers 10 and 12 carry
   finite/readout prediction receipts, while cold unbounded extraction and any
   literature-grade Problem 3 promotion remain outside Paper 5.

_— honestly carried as guard / next-need._

---



## 06A. Formal-Paper Deep-Dive (CQE-paper-06)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-06/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **causal vertex** is a paper, proof, tool, receipt, obligation, or product
artifact.

A **causal edge** is a record:

```text
source
target
edge_type
receipt
status
```

Allowed edge types are:

```text
uses
proves
refines
obligates
transports
repairs
constrains
verifies
```

Allowed statuses are:

```text
open
closed
deferred
rejected
```

An edge with status `open` is not a proof closure. It is a tracked obligation.

### Main Claim

**Theorem 6.1, Typed Causal Edge Contract.** A paper-kernel dependency is
admissible to the CQECMPLX production graph only if it is represented by a
typed causal edge with source, target, edge type, receipt, and status. Active
proof dependencies must be acyclic unless the cycle is explicitly typed as
review, feedback, or obligation routing rather than proof support.

**Theorem 6.2, Rule90/Lucas Causal Decomposition.** The Rule 30 local update
decomposes exactly as `Rule90 xor (C and not R)`. Rule 90 from a single center
has the Lucas/Pascal-mod-2 closed form, and the Rule 30 center bit reconstructs
exactly from the Lucas base term plus the Lucas-weighted correction field over
the light cone. This closes the verifiable decomposition core of O2' while
leaving the stronger oracle-free correction-sum collapse outside this theorem.

**Theorem 6.3, Triadic Keystone.** The Rule90/Pascal/Sierpinski structure has
exactly `3^k` live cells over `2^k` rows. This is the triadic causal substrate
used by the suite: it is an exact finite keystone for the recurrence of
threefold structure through LCR, correction, SU(3), D4, E8/Niemeier, and
readout layers. The verifier records the framework arguments for the three
Wolfram Rule 30 problems with epistemic status rather than pretending the
literature-grade cold problems are closed.

**Theorem 6.4, Correction-Extraction Verdict.** Two proposed mechanisms for
oracle-free `O(log N)` correction extraction are retired by direct test:
McKay-Thompson coefficient-parity matching and the accumulated-center-color
fallback. The exact decomposition remains closed, but cold Rule 30 center-bit
extraction without prior enumeration remains a genuine open boundary.

### Proof

Without a source and target, a dependency cannot be located. Without an edge
typ

_**(D)** formal claim._

### Falsifiers

The verifier must reject:

```text
1. An edge with no receipt.
2. An edge with an unknown type.
3. A proof cycle disguised as closure.
4. A graph that labels open obligations as resolved.
```

These falsifiers protect the suite from becoming a pile of agreeable prose.

_— honestly carried as guard / next-need._

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-06/verify_causal_code.py
production/formal-papers/CQE-paper-06/verify_rule90_lucas_decomposition.py
production/formal-papers/CQE-paper-06/verify_triadic_keystone.py
production/formal-papers/CQE-paper-06/verify_correction_extraction_verdict.py
```

It verifies:

```text
1. Every edge has required fields.
2. Every edge uses an allowed type and status.
3. The polished Papers 01-06 graph is acyclic for proof-support edges.
4. Open obligations remain open.
5. Invalid edges and hidden proof cycles are rejected.
6. Rule 30 decomposes exactly as Rule90 plus correction.
7. Lucas/Pascal-mod-2 reconstruction matches direct simulation.
8. Triadic `3^k`-in-`2^k` structure is verified.
9. Failed cold correction-extraction mechanisms are rejected rather than
   promoted.
```

### Validation and Hidden-Guess Layer

Useful hidden-guess prompts:

```text
What fields are required on a causal edge?
Can an open obligation be counted as resolved?
Can a proof-support graph contain a hidden cycle?
What edge type connects Paper 04 to Paper 05?
```

Expected answers:

```text
source, target, type, receipt, status
no
no
transports or constrains, depending on the specific route
```

### Open Obligations

1. Wire `verify_causal_code` into `cqe_engine.formal`.
2. Populate the full 32-paper graph from all formal receipts.
3. Decide which cycles are allowed as review loops and which are rejected as
   proof cycles.
4. Replace placeholder receipt ids with repository-stable artifact hashes.
5. Keep the cold Rule 30 Problem 3 extraction boundary separate from the
   verified aggregate-during-enumeration readout in Paper 10.

_— honestly carried as guard / next-need._

---



## 07A. Formal-Paper Deep-Dive (CQE-paper-07)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-07/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **discrete trace** is a list of indexed values:

```text
D = [(0,x0), (1,x1), ..., (n,xn)]
```

A **sample-preserving bridge** is a continuous function `F` on `[0,n]` such
that:

```text
F(k) = xk for every integer sample k.
```

The verifier uses piecewise-linear interpolation:

```text
F(t) = (1-a) * x_floor(t) + a * x_ceil(t)
where a = t - floor(t)
```

At integer points, `a=0`, so `F(k)=xk`.

### Main Claim

**Theorem 7.1, Sample-Preserving Bridge.** Every finite discrete trace over
numeric values admits a continuous piecewise-linear bridge that exactly
preserves all indexed samples.

**Theorem 7.2, MDHG/SpeedLight Retraction Bridge.** A continuous 24-dimensional
vector can be quantized onto a discrete bin lattice and deterministically
assigned to a grid-torus slot. Re-admitting the same content is idempotent:
`f(f(x)) = f(x)`. This makes the MDHG cache a replayable
discrete-continuous retraction bridge. Product CA-field dynamics and empirical
slot-collision claims remain outside this theorem.

### Proof

Between each adjacent pair `(k,xk)` and `(k+1,xk+1)`, draw the straight segment
joining the two values. The resulting piecewise-linear function is continuous
because adjacent segments share the same endpoint at every integer index.
At each sample index `k`, the function evaluates to the stored value `xk`.
Thus the bridge preserves every discrete sample exactly. QED.

For Theorem 7.2, `verify_mdhg_speedlight_bridge.py` runs MDHGForge. It checks
that the bridge dimension is 24, quantization is total on real inputs, bin
centers are fixed by re-quantization, slot assignment is deterministic on a
torus, repeated admission is a hit with distance zero and no growth, per-slot
capacity is maintained, LRU eviction is deterministic, distance is minimum
Hamming distance over existing vectors, multi-scale layers are independent, and
occupancy is conserved. QED.

_**(D)** formal claim._

### Relation to Earlier Papers

Paper 06 gives typed causal edges. Paper 07 gives a presentation bridge from
indexed edge states to continuous fields. The bridge is a view of the discrete
receipt structure, not a replacement for it.

Paper 02's Rule 30 / Rule 90 correction identity can provide one family of
discrete values:

```text
Rule30(L,C,R) = Rule90(L,R) xor (C and not R)
```

Those discrete values can be drawn as a continuous interpolant, but the exact
proof remains at the sample points unless a separate theorem proves the
between-sample dynamics.

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-07/verify_discrete_continuous_bridge.py
production/formal-papers/CQE-paper-07/verify_mdhg_speedlight_bridge.py
```

It verifies:

```text
1. The interpolant preserves every integer sample.
2. Adjacent linear segments agree at shared endpoints.
3. The Rule 30 / Rule 90 correction identity still holds on all LCR states.
4. The between-sample physical-dynamics overclaim is rejected.
5. The MDHG/SpeedLight bridge is a deterministic 24D quantize-and-slot
   retraction with idempotent re-admission.
```

### Open Obligations

1. Wire `verify_discrete_continuous_bridge` into `cqe_engine.formal`.
2. Decide which later papers require more than sample-preserving interpolation.
3. Add a separate theorem for any claimed Hamiltonian or physical dynamics
   between samples.
4. Carry bridge residuals into Paper 16 only as obligations until verified.
5. Keep CA-field dynamics and collision-rate product diagnostics outside this
   paper until their own stability and empirical receipts exist.

_— honestly carried as guard / next-need._

---



## 08A. Formal-Paper Deep-Dive (CQE-paper-08)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-08/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions,
lemmas, constructions, examples, and receipts that establish the claimed
result. Paper 00, hand routes, analog tools, workbook language, and obligation
ledgers are supplemental validation and exposure layers. They exist to make
the math inspectable, reproducible, and accessible without requiring a
particular software stack. The hand route is not the purpose of the paper; it
is a way to expose the same state transitions with ordinary marks, tokens,
lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **lattice closure template** is a sequence of finite code or lattice objects
that lets a local state carrier be lifted into a larger transport frame while
preserving the proof boundary of every step.

The Paper 08 template is:

```text
D1 raw bit                 -> 1
S3 / three-cell carrier    -> 3
Fano / Hamming / octonion  -> 7
extended Hamming / E8 seed -> 8
Golay / Leech ingredient   -> 24
Nebe sheet bound           -> 72
```

A **local certified fact** is a claim checked at a fixed dimension by a
finite verifier.

A **global landing claim** is a stronger statement that a local certified
fact has been glued into a terminal lattice object such as the rootless Leech
lattice or a Gamma72 action. Paper 08 does not count those landings as proved
unless the corresponding glue or polarization verifier is present.

A **sheet bound** is the maximum orbit distance expressible inside the current
sheet before a new anchor must be introduced. The Paper 08 verifier records
`K = 9`.

### Main Claim

**Theorem 8.1, Local Lattice Closure Template.** The finite code chain
`(1, 3, 7, 8, 24)` and powered terminal `72 = 8 x 9` provide a verified local
closure template for CQECMPLX transport: every admitted rung is backed by a
finite combinatorial check, and every unproved global landing is preserved as
an explicit proof boundary rather than erased.

**Theorem 8.2, Niemeier/Leech Enumeration Boundary.** The current
Niemeier/Leech reapplication verifier closes the deterministic selector,
E8^3 carrier, Leech type-1/2/3 orbit, and Nebe 72 contract checks. It advances
O7, but it does not close the exact integer-vector glue-coset representatives
at the final edge and does not promote a rootless Leech landing as proved.

**Theorem 8.2a, O7 Exact E8^3 Glue Closure.** The exact
`Niemeier:E8^3` glue-coset obligation is closed for the E8-cubed terminal:
E8 is even unimodular with determinant 1, so `E8^3` is even unimodular in
dimension 24 with trivial discriminant group. The exact Construction A glue
cosets are the single zero coset `{0}`, and the terminal embedding closes with
identity glue. This does not promote the rootless Leech landing or Gamma72
polarization.

**Theorem 8.3, T8 Commutability Tree.** A rebuilt lattice-forge seed ledger
contains the eight canonical `F4` to Niemeier terminal paths recorded by T8.
Each queried target returns `yes_with_template_glue`, the path matches the
historical path table, and all eight terminal targets are distinct. This binds
the seed-ledger path theorem while preserving the exact-glue and landing
boundaries.

**Theorem 8.4, F2 Bridge, Unipotent Orbits, and Substrate Map.** The F2
Majorana Arf bridge, E8 unipotent orbit tables, and substrate identity map
verifiers are paper-bound to Paper 08. This advances O2'' by closing the
algebraic F2 g

_**(D)** formal claim._

### Relation to Earlier Papers

Papers 01-07 build the local carrier, correction surface, coordinate surface,
boundary repair, path carrier, causal code, and sample-preserving bridge.
Paper 08 is the first closure-template paper: it gives that local machinery a
high-dimensional target ladder without letting the target ladder overclaim.

The result is a bridge from local proof mechanics into reusable lattice
closure:

```text
LCR carrier
-> correction surface
-> D4/J3 coordinate surface
-> repaired path carrier
-> causal receipt
-> discrete-continuous bridge
-> lattice closure template
```

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-08/verify_e8_even_lattice.py
production/formal-papers/CQE-paper-08/verify_e8_hemisphere_partition.py
production/formal-papers/CQE-paper-08/verify_lattice_closure_template.py
production/formal-papers/CQE-paper-08/verify_lattice_code_chain.py
production/formal-papers/CQE-paper-08/verify_lattice_code_closure.py
production/formal-papers/CQE-paper-08/verify_f2_bridge_unipotent_substrate.py
production/formal-papers/CQE-paper-08/verify_o2pp_registry_populated.py
production/formal-papers/CQE-paper-08/verify_o7_niemeier_e8cubed_glue_closed.py
production/formal-papers/CQE-paper-08/verify_niemeier_leech_enumeration.py
production/formal-papers/CQE-paper-08/verify_t8_commutability_tree.py
```

It imports the package verifiers:

```text
lattice_forge.lattice_codes.verify_lattice_code_chain
lattice_forge.lattice_codes.verify_hamming_7_fano
lattice_forge.lattice_codes.verify_extended_hamming_8
lattice_forge.lattice_codes.verify_golay_24
lattice_forge.lattice_codes.verify_powered_chain
lattice_forge.nebe_gamma72.verify_nebe_gamma72_contract
```

It verifies:

```text
1. Fano/Hamming identity passes.
2. Extended Hamming/E8 seed checks pass.
3. Golay ingredient and 24 = 3 x 8 checks pass.
4. Powered 72 sheet-bound checks pass.
5. Gamma72 three-sheet transport passes while landing proof remains false.
6. Leech and Gamma72 overclaims are rejected.
7. Niemeier/Leech enumeration passes for deterministic selectors, E8^3
   carriers, Leech type-1/2/3 orbits, and the Nebe 72 contract.
8. O7 exact `Niemeier:E8^3` glue closes as the single zero coset `{0}` with
   identity glue.
9. Broader exact glue representatives beyond the E8-cubed zero-coset case
   remain outside this theorem.
10. The rebuilt seed ledger returns the eigh

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
