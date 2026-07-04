# Paper 11 — Theory Admission Gate

**Status:** IPMC — internal physics map closed for the T10-anchored Gluon mass admission gate at `K=9` and the encoder-bound Pariah/Happy-Family boundary case. Encoder invariance, individual Happy-Family object promotion, and finite simple group classification reproof remain open.

**Source papers:** CQE-paper-11, CQE-paper-11.25.  
**Canonical formal paper:** `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-11/FORMAL_PAPER.md`.  
**Verifiers:** `verify_theory_admission_gate.py`, `verify_sporadic_admission_boundary.py`.

---

## Abstract

Paper 11 proves the admission rule for importing an external theory into the CQECMPLX stack. An outside theory is not accepted because it is rhetorically similar to the framework, and it is not discarded because a first transport attempt fails. It is tested as a candidate against the carried observer center, the Paper 10 master receipt, the trusted Gluon spectrum, and the `K=9` sheet boundary inherited from the lattice closure layer.

The proof-carrying result is `T_ADMISSION`: the admission Gluon is a Gluon mass filter at `K=9`, anchored by the Paper 10 master receipt. A candidate is admitted only when its mass matches the trusted spectrum and remains inside the `K_max = 9` window. A trusted match outside that window is a boundary receipt, not an admission. A nonmatching candidate is rejected as a datum, not erased.

The Pariah/Happy-Family case is included as a worked boundary receipt. Under the declared bit-length-parity encoder, the Pariah set closes while the Happy Family set remains open. This demonstrates how Paper 11 converts failure, closure, and boundary collision into typed receipts without reproving the classification of finite simple groups.

### Keywords

Theory admission; trust anchor; Gluon mass filter; K-boundary; Pariah; Happy Family; Monster; sporadic groups; boundary receipt; encoder-bound; CQECMPLX receipts.

---

## Claim Ledger

| ID | Claim | Tag | Evidence | Boundary |
|----|-------|-----|----------|----------|
| 11.1 | Paper 11 inherits `C₀₀` and `E₀₀→₁` through the Paper 10 master receipt. | [D] | `verify_theory_admission_gate.py`; `theory_admission_gate_receipt.json` (20/20) | Observer lineage |
| 11.2 | The T10 master receipt passes. | [D] | Same verifier | Trust anchor |
| 11.3 | The trusted spectrum binds Papers 00–10. | [D] | Same verifier | Spectrum closure |
| 11.4 | `K_max = 9` is the Nebe bound. | [D] | Same verifier | Lattice closure inheritance |
| 11.5 | The mass gate admits candidates inside the window (`mass ≤ 9`, trusted). | [D] | Same verifier | Admission rule |
| 11.6 | The mass gate routes trusted mass `> 9` to a boundary receipt. | [D] | Same verifier | Boundary rule |
| 11.7 | The mass gate rejects untrusted mass. | [D] | Same verifier | Rejection rule |
| 11.8 | The bit-length-parity encoder is declared and bound. | [D] | Same verifier | Encoder declaration |
| 11.9 | The local Lattice Forge ledger carries six Pariah objects. | [D] | Same verifier | Local substrate |
| 11.10 | The Monster partition metadata is local: 20 Monster-involved + 6 Pariah. | [D] | Same verifier | Local metadata |
| 11.11 | Structural Pariah exit routes and hard-wall routes are present locally. | [D] | Same verifier | Route materialization |
| 11.12 | Pariah prime profiles are present locally. | [D] | Same verifier | Prime profile |
| 11.13 | The Happy Family count is 20. | [D] | Same verifier | Partition count |
| 11.14 | The Pariah signature closes under the declared encoder. | [D] | Same verifier | Encoder closure |
| 11.15 | The Happy Family signature remains open under the declared encoder. | [D] | Same verifier | Encoder openness |
| 11.16 | The three-outlet gate (admitted, boundary, rejected) is exercised. | [D] | Same verifier | Gate completeness |
| 11.17 | Boundary receipt outlets are exercised; failures are retained, not erased. | [D] | Same verifier | Honesty guard |
| 11.18 | Pariahs route to boundary; Happy Family open is datum, not dismissal. | [D] | Same verifier | Routing correctness |
| 11.19 | Proof sources are present. | [D] | Same verifier | Source binding |
| 11.20 | The sporadic total is 26: 20 Happy Family + 6 Pariah. | [D] | `verify_sporadic_admission_boundary.py`; `sporadic_admission_boundary_receipt.json` (12/12) | Classification count |
| 11.21 | Happy Family and Pariah are disjoint, no duplicates. | [D] | Same verifier | Partition integrity |
| 11.22 | Monster and Baby Monster are in the Happy Family. | [D] | Same verifier | Membership |
| 11.23 | The admission gate is structurally the Monster membership filter. | [I] | Same verifier | Structural identification; not a new group theorem |
| 11.24 | The Pariah/Happy-Family result holds for all encoders. | [X] | Encoder-bound | Encoder invariance is future work |
| 11.25 | Individual Happy-Family objects are promoted as closed theorems. | [X] | Happy Family open under encoder | Individual promotion is future work |
| 11.26 | The classification of finite simple groups is reproven. | [X] | Imported as mathematical input | Not claimed |
| 11.27 | A theory may enter without the T10 trust anchor. | [X] | Falsifier rejects | Center must be carried |
| 11.28 | A nonmatching candidate is deleted rather than receipted. | [X] | Falsifier rejects | Rejected as datum |

---

## Definitions

**Definition 11.1 (Observer center).** The observer center `C₀₀` is the center encoded by the requested enumeration event at the Paper 00 to Paper 01 transition. Paper 11 inherits this center through the Paper 10 master receipt unless a later paper explicitly proves a recentering.

**Definition 11.2 (Paper 10 trust anchor).** The Paper 10 trust anchor is the receipt `T10 = (C₀₀, E₀₀→₁, P₀₀, P₀₁..P₀₉, R, L, V, O)` where `R` is the transport table, `L` is the lookup cache, `V` is the verifier verdict, and `O` is the visible open-boundary set.

**Definition 11.3 (Admission Gluon).** The admission Gluon is the Paper 11 carrier that evaluates a candidate theory by Gluon mass against a trusted spectrum. It is registered as `T_ADMISSION: Admission Gluon = Gluon mass filter at K=9; T10 = trust anchor`.

**Definition 11.4 (Trusted spectrum).** The trusted spectrum is the finite mass set `S_T10 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}` exposed by the receipt-bearing stack available to Paper 11.

**Definition 11.5 (Sheet boundary).** The sheet boundary is `K_max = 9`, the Nebe/lattice window used as the maximum sheet depth expressible from one anchor event before the candidate must be reported as a boundary crossing.

**Definition 11.6 (Candidate theory).** A candidate theory is any external theory, model, proof object, package, or tool claim being tested for import into the CQECMPLX stack.

**Definition 11.7 (Admission receipt).** An admission receipt is the typed verdict `(candidate_id, mass, trusted_match, K_max, T10_anchor, verdict)` where `verdict ∈ {admitted, boundary, rejected, rejected_as_datum}`.

**Definition 11.8 (Bit-length-parity encoder).** The bit-length-parity encoder maps a group `G` to `bit(G) = bit_length(|G|) mod 2`.

---

## Theorems and Proofs

**Theorem 11.1 (T_ADMISSION — Theory Admission Gate).** Let `T` be a candidate theory with Gluon mass `m(T)`. Let `S_T10` be the trusted spectrum exposed by the Paper 10 master receipt, and let `K_max = 9`. Paper 11 admits `T` if and only if:

```text
T10 signs the admission context,
m(T) ∈ S_T10,
m(T) ≤ K_max.
```

If `T10` signs the context and `m(T) ∈ S_T10` but `m(T) > K_max`, then `T` is routed to a boundary receipt. If `m(T) ∉ S_T10`, or if the candidate is not bound to the T10 context, the candidate is rejected or rejected as a datum.

*Proof.* Paper 10 proves that `C₀₀`, the `00 → 1` encoding event, and the receipts for Papers 00–09 are present in one replayable master object. Therefore Paper 11 has a stable observer center and a stable receipt anchor before it evaluates any external theory. Admission without that anchor would be a center move with no accounting, so it is rejected by construction. ∎

The admission Gluon is defined as a filter over candidate mass. Its acceptance predicate is `A(T) = signed_T10(T) ∧ m(T) ∈ S_T10 ∧ m(T) ≤ 9`. These three clauses are necessary. Without `signed_T10(T)`, the candidate is not being evaluated inside the carried paper stack. Without `m(T) ∈ S_T10`, the candidate has no trusted spectrum match. Without `m(T) ≤ 9`, the candidate crosses the sheet boundary and cannot be admitted from the same anchor event. ∎

They are also sufficient for Paper 11 admission: a candidate with the T10 anchor, a trusted-spectrum mass, and a mass inside `K=9` is exactly the object the admission Gluon is defined to pass. Therefore the gate is closed under the three predicates. ∎

The remaining cases are exhaustive and disjoint:

```text
signed_T10(T) ∧ m(T) ∈ S_T10 ∧ m(T) ≤ 9  → admitted
signed_T10(T) ∧ m(T) ∈ S_T10 ∧ m(T) > 9   → boundary
m(T) ∉ S_T10 ∨ no T10 context             → rejected / rejected_as_datum
```

Thus Paper 11 proves a real admission rule rather than a narrative preference. ∎

**Theorem 11.2 (Pariah/Happy-Family Boundary Case).** Under the declared bit-length-parity encoder, the Pariah set (6 groups) closes while the Happy Family set (20 groups) remains open. The Pariah signature has `res² = 0` with dominant chain `e → e → e`; the Happy Family signature has `res² = 4/9` and is non-idempotent.

*Proof.* The local Lattice Forge ledger contains Monster metadata recording the sporadic partition "20 Monster-involved + 4 structural pariahs + 2 hard pariahs", six Pariah objects (`J1, J3, J4, Ru, O'N, Ly`), and structural/hard-wall exit routes. The verifier applies the bit-length-parity encoder to each group order and confirms that the Pariah signature closes (`res² = 0`) while the Happy Family signature remains open (`res² = 4/9`). The sporadic admission boundary verifier independently confirms the count: 26 total sporadic groups, 20 Happy Family, 6 Pariah, disjoint, no duplicates, Monster and Baby Monster in Happy Family. All 12 checks pass. ∎

The paper does not reprove the classification of finite simple groups; it imports that classification as mathematical input and proves the CQECMPLX admission and boundary role under the declared encoder. ∎

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Status |
|----------|---------|--------|--------|
| `verify_theory_admission_gate.py` | `theory_admission_gate_receipt.json` | 20 | pass |
| `verify_sporadic_admission_boundary.py` | `sporadic_admission_boundary_receipt.json` | 12 | pass |

**Total checks:** 32/32 pass.

**Mass gate verdicts:**

| Candidate | Mass | Trusted Match | K_max | Verdict |
|-----------|------|---------------|-------|---------|
| native_inside_window | 5 | true | 9 | admitted |
| trusted_k_boundary | 10 | true | 9 | boundary |
| untrusted_external | 11 | false | 9 | rejected |

**Sporadic partition:**

| Set | Count | Status under encoder |
|-----|-------|---------------------|
| Happy Family | 20 | open (res² = 4/9) |
| Pariah | 6 | closed (res² = 0) |
| Total | 26 | — |

---

## Hand Reconstruction

1. Verify Paper 10 master receipt is present and passes.
2. Confirm `C₀₀` and `E₀₀→₁` are inherited.
3. Verify the trusted spectrum `S_T10 = {0,1,...,10}`.
4. Confirm `K_max = 9` is the Nebe bound.
5. Test the mass gate: admit mass 5 (inside, trusted), boundary mass 10 (outside, trusted), reject mass 11 (untrusted).
6. Verify the local Lattice Forge ledger carries 6 Pariah objects.
7. Verify Monster metadata records 20 Monster-involved + 6 Pariah.
8. Verify structural Pariah exit routes and hard-wall routes are present.
9. Apply the bit-length-parity encoder to each sporadic group.
10. Confirm Pariah signature closes (res² = 0).
11. Confirm Happy Family signature remains open (res² = 4/9).
12. Verify the sporadic total is 26, disjoint, no duplicates.
13. Confirm Monster and Baby Monster are in Happy Family.
14. Verify all boundary failures are retained as receipts, not erased.

---

## Falsifiers and Rejected Claims

| Rejected Claim | Reason |
|---------------|--------|
| "A theory may enter without the T10 trust anchor." | Rejected. Admission without the T10 anchor is a center move with no accounting; it is rejected by construction. |
| "A trusted mass above K=9 is admitted without a boundary receipt." | Rejected. Mass 10 is routed to boundary, not admitted. |
| "A nonmatching candidate is deleted rather than receipted." | Rejected. Untrusted mass 11 is rejected as a datum, not erased. |
| "A verdict from one declared encoder may be generalized without a new receipt." | Rejected. The Pariah/Happy-Family result is encoder-bound. Encoder invariance requires a separate proof. |
| "The Pariah boundary reading is a new finite-group classification theorem." | Rejected. Paper 11 imports the classification as mathematical input and proves the CQECMPLX admission role under the declared encoder. |
| "Paper 11 can ignore C₀₀/E₀₀→₁." | Rejected. Every admission verdict is an effect of the carried center chain. |

---

## Relation to Prior and Later Papers

**Paper 10 (T10 Master Receipt):** Supplies the trust anchor `T10 = (C₀₀, E₀₀→₁, P₀₀, P₀₁..P₀₉, R, L, V, O)`. Paper 11 evaluates candidates against this anchor; without it, admission would be a center move with no accounting.

**Papers 00–09:** Supply the receipt-bearing stack that defines the trusted spectrum and the `K=9` boundary inherited from the lattice closure layer.

**Paper 29 (Monster Universal Energy Bound):** The Happy Family lives inside the Monster, whose prime ceiling is `47·59·71` (three largest supersingular primes). The gate's inside/outside boundary is structurally the Monster membership filter.

**Later papers:** A candidate theory that claims a new center must prove the recentering and handoff from the prior center. Until it does, the admission gate evaluates it against the carried center.

---

## Open Obligations

| ID | Disposition |
|----|-------------|
| 11.1 | Prove encoder invariance: the Pariah/Happy-Family result holds for all encoders, not just bit-length-parity. |
| 11.2 | Promote individual Happy-Family objects from open/datum status to closed theorems. |
| 11.3 | Candidate-specific Gluon mass functions must be declared before admission. |
| 11.4 | Prove or import a broader finite-group classification result if needed. |
| 11.5 | Wire all Paper 11 verifiers into `cqe_engine.formal`. |
| 11.6 | Add domain examples (software dependency gates, API admission control, security boundaries) after the formal schema is stable. |

---

## Bibliography

[1] N. Barker, *CQE Paper 10 — T10 Master Receipt*, `papers/active-rework/10_T10_Master_Receipt.md`, 2026. Supplies the trust anchor `T10` and the inherited observer center `C₀₀`.

[2] R. L. Griess, Jr., "The Friendly Giant," *Invent. Math.* 69 (1982), 1–102. Construction of the Monster group and the Happy Family/Pariah partition.

[3] J. H. Conway and S. P. Norton, "Monstrous Moonshine," *Bull. Lond. Math. Soc.* 11 (1979), 308–339. Reference for the Monster group and sporadic structure.

[4] `lattice_forge` substrate modules, CMPLX-PartsFactory-main. Source of the local Ledger Forge with Monster metadata and Pariah routes.

[5] M. Aschbacher, *Finite Group Theory*, 2nd ed., Cambridge University Press, 2000. Reference for the classification of finite simple groups.

---

## Conclusion

Paper 11 closes the admission problem for this stage of the stack. A candidate theory enters only through the T10-anchored Gluon mass filter, inside the `K=9` boundary, against the trusted spectrum. Boundary crossings and failed encoder tests are not discarded; they become receipt-bearing data. The Pariah/Happy-Family case demonstrates how the gate converts failure, closure, and boundary collision into typed receipts without reproving the classification of finite simple groups.

The result is proof-first: the observer center, the T10 anchor, the mass predicate, the K-boundary, the local Lattice Forge Pariah routes, and the encoder-bound verdict are all present in one verifiable object. The honesty guard is the point: the Pariah/Happy-Family result is encoder-bound, individual Happy-Family objects remain open, and the classification is imported, not reproven. This is the architecture that keeps the corpus rigorous: admit what matches, boundary what crosses, reject what fails, and never erase a failure without a receipt.
