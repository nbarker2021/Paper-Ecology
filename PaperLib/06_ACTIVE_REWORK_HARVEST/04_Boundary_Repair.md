# Paper 04 — Boundary Repair

**Status:** IPMC — internal physics map closed for the typed boundary repair construction. Full obligation-ledger schema and domain examples remain open.

**Source papers:** CQE-paper-04, CQE-paper-04.25.  
**Canonical formal paper:** `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-04/FORMAL_PAPER.md`.  
**Verifiers:** `verify_boundary_repair.py`.

---

## Abstract

Paper 04 formalizes boundary repair as the operation that converts a failed or nonclosing join into a typed constraint for the next legal route. The paper consumes Papers 01–03: Paper 01 supplies the LCR state; Paper 02 supplies the correction firing states and typed residue; Paper 03 supplies the axis/sheet coordinate system. Paper 04 turns the correction residue plus coordinate into a determinate constraint record.

The closed claim is a constructive equivalence: a failed join is repairable if and only if it can be converted into a typed constraint preserving the original state, the Paper 03 coordinate, the reason for failure, and at least one next legal route. The repair operation is idempotent. Untyped failures are rejected.

The paper does not claim that every failure is repaired merely by naming it. A repair exists only when the failed join is converted into a replayable constraint with enough information for the next transport to act. It does not promote failed joins to proof.

### Keywords

Boundary repair; typed constraint; failed join; correction residue; idempotent operation; CQECMPLX paper kernel.

---

## Claim Ledger

| ID | Claim | Tag | Evidence | Boundary |
|----|-------|-----|----------|----------|
| 04.1 | The two Paper 02 correction states `(0,1,0)` and `(1,1,0)` are consumed and converted into constraint records. | [D] | `verify_boundary_repair.py`; `boundary_repair_receipt.json` (7/7) | Finite local construction |
| 04.2 | The Paper 03 axis/sheet coordinates `(2,0)` and `(3,1)` are preserved in the repaired constraints. | [D] | Same verifier | Coordinate preservation |
| 04.3 | Every repaired constraint contains all required fields: `state`, `axis_sheet`, `reason`, `status`, `next_legal_routes`, `source_paper`, `target_paper`. | [D] | Same verifier | Schema completeness |
| 04.4 | The status of every repaired constraint is `constraint`, not `proof`. | [D] | Same verifier | Honesty guard |
| 04.5 | Every repaired constraint has at least one next legal route. | [D] | Same verifier | Routability |
| 04.6 | The repair operation is idempotent: `repair(repair(x)) = repair(x)` for every repairable input `x`. | [D] | Same verifier | Algebraic closure |
| 04.7 | Untyped failures (inputs lacking required fields) are rejected with a `ValueError`. | [D] | Same verifier | Falsifier |
| 04.8 | A failed join is repairable iff it can be converted into a typed constraint with the required fields. | [I] | Constructive equivalence proven in Theorem 4.1 | Logical characterization; depends on prior definitions |
| 04.9 | Full obligation-ledger schema shared across all papers. | [X] | Not in scope | Route to NP-05 / obligation-registry paper |
| 04.10 | Domain examples (civil crack repair, inventory exception routing). | [X] | Not in scope | Route to applied papers (81–100) |
| 04.11 | All failures in the corpus are repairable by this construction. | [X] | Not claimed | The construction handles Paper 02 correction states only |

---

## Definitions

**Definition 4.1 (LCR state).** An LCR state is `σ = (L, C, R) ∈ {0,1}^3`.

**Definition 4.2 (Correction residue).** A correction residue is a state `σ` for which `corr(σ) = C ∧ ¬R = 1`. By Paper 02, the correction firing states are exactly `(0,1,0)` and `(1,1,0)`.

**Definition 4.3 (Local coordinate).** The local coordinate of `σ` is `coord(σ) = (axis(σ), sheet(σ))` from Paper 03.

**Definition 4.4 (Failed join).** A failed join is a correction residue that lacks a legal next route in the current paper kernel.

**Definition 4.5 (Boundary repair constraint).** A boundary repair constraint is a record `r` with fields:

```text
state:             the original LCR state σ
axis_sheet:        the Paper 03 coordinate (axis(σ), sheet(σ))
reason:            the cause of failure
tatus:            "constraint" (not "proof")
next_legal_routes: a nonempty list of legal next papers
source_paper:      the paper that produced the constraint
target_paper:      the intended next paper
```

**Definition 4.6 (Repair operation).** Define `repair` on a repairable object `x` as follows:
- If `x` is a correction state `σ ∈ {(0,1,0), (1,1,0)}`, construct the constraint record with the fields above.
- If `x` is already a constraint record containing all required fields, return `x` unchanged.
- Otherwise, raise `ValueError("untyped failure is not repairable")`.

---

## Theorem and Proof

**Theorem 4.1 (Typed Boundary Repair).** A failed join is repairable in the CQECMPLX paper kernel if and only if it can be converted into a typed boundary repair constraint preserving the original state, the Paper 03 coordinate, the reason for failure, and at least one next legal route. Moreover, the repair operation is idempotent.

*Proof.* We prove the equivalence in two directions.

*(Only if)* Suppose a failed join is repairable. By Definition 4.6, the only repairable inputs are the two correction states `(0,1,0)` and `(1,1,0)`, or an already-complete constraint record. In the first case, the repair operation constructs a constraint record with all required fields: `state` is the original `σ`, `axis_sheet` is the Paper 03 coordinate `(axis(σ), sheet(σ))`, `reason` is `"Paper 02 correction fired: C and not R"`, `status` is `"constraint"`, `next_legal_routes` contains at least one entry, and `source_paper`/`target_paper` are set. In the second case, the constraint record already contains all required fields by hypothesis. Thus every repairable failed join yields a typed constraint with the required fields. ∎

*(If)* Suppose a failed join can be converted into a typed constraint preserving the original state, Paper 03 coordinate, reason, and at least one next legal route. Then the constraint record contains all required fields. By Definition 4.6, applying `repair` to this record returns it unchanged. Therefore the join is repairable. ∎

*(Idempotence)* Let `x` be repairable. If `x` is a correction state, `repair(x)` produces a constraint record `r`. Applying `repair` to `r` returns `r` unchanged because `r` contains all required fields. If `x` is already a constraint record, `repair(x) = x` by definition, and `repair(repair(x)) = repair(x) = x`. Thus `repair ∘ repair = repair`. ∎

*(Falsifier)* An untyped failure is an input lacking the required fields. By Definition 4.6, such an input raises `ValueError`. The verifier confirms this by attempting `repair({"status": "failed"})` and catching the exception. ∎

## G₂ Fano Three-Form and Off-Diagonal Multiplication

Paper 04 closes the boundary-repair construction for finite typed constraints. The algebraic substrate that supports the repair operation is the Fano incidence structure. This section adds the G₂ three-form, corrects the G₂ versus F₄ distinction, and derives the off-diagonal multiplication layer.

**Definition 4.7 (G₂ three-form).** Let φ be the oriented Fano three-form:
φ = Σ_{ℓ=(i,j,k)} ε_{ijk} e_i ∧ e_j ∧ e_k,

where the sum runs over the seven oriented lines of the Fano plane. The structure constants ε_{ijk} are fixed by the oriented incidence structure.

**Definition 4.8 (Octonionic cross product).** The G₂ three-form defines the octonionic cross product through:
⟨u × v, w⟩ = φ(u,v,w).

For imaginary octonions, multiplication decomposes as:
uv = −⟨u,v⟩ + u × v.

**Theorem 4.2 (G₂ versus F₄ distinction).** The stabilizer of the three-form φ is G₂ = Aut(𝕆), the automorphism group of the octonions. The automorphism group of the Albert algebra is F₄ = Aut(J₃(𝕆)). These are distinct groups with distinct roles:

- G₂ preserves octonion multiplication.
- F₄ preserves the Albert algebra built from octonions.

The proper hierarchy is:
F₂³ → oriented Fano plane → (Im𝕆, φ, G₂) → J₃(𝕆) → F₄.

*Proof.* By definition, G₂ is the stabilizer of the associative 3-form on the imaginary octonions. F₄ acts on the full 27-dimensional Albert algebra, preserving the Jordan product. Since J₃(𝕆) is built from octonions but has additional structure (the Jordan product and cubic norm), its automorphism group is larger than G₂. The chain is standard exceptional Lie theory. ∎

**Theorem 4.3 (Off-diagonal multiplication layer).** For X ∈ J₃(𝕆) with diagonal entries α_i and off-diagonal entries x, y, z ∈ 𝕆, the three off-diagonal entries are each octonions:
x, y, z ∈ 𝕆 = ℝ ⊕ Im𝕆 = 1 ⊕ 7.

The Fano structure controls the multiplication among the imaginary components of x, y, and z. The Albert cubic norm is:
N(X) = α₁α₂α₃ − α₁|x|² − α₂|y|² − α₃|z|² + 2 Re(xyz).

The final term 2 Re(xyz) is irreducibly triadic and requires the oriented Fano product.

*Proof.* The off-diagonal entries of a Jordan algebra element are octonions. The norm formula is the standard determinant-like expression for the Albert algebra. The term 2 Re(xyz) cannot be obtained from diagonal data alone; it requires ordered octonion multiplication of the three off-diagonal entries, which is governed by the oriented Fano structure. ∎

**Remark (interpretive boundary).** The G₂ three-form and the off-diagonal multiplication layer are closed algebraic facts. The claim that these structure constants serve as color-transition data for a physical gauge theory requires a commutator-preserving map Φ_g: T_LCR → su(3) that has not yet been constructed. This boundary is preserved in all downstream papers.

## Tetrad, Solder Form, and Light-Cone Transport

Paper 14 defines curvature as boundary-repair demand. The proper mathematical framework for "a carrier can relate to any local arrow" is the tetrad or solder form. This section records the exact formalism and its boundary.

**Definition 4.9 (Tetrad / solder form).** A tetrad `e^a_μ` identifies an internal local Lorentz frame with spacetime tangent directions:
```
g_{μν} = e^a_μ e^b_ν η_{ab},
```
where `η_{ab}` is the Minkowski metric. The spin connection transports the local orientation between events.

**Definition 4.10 (Null spinor).** For null directions, `k_{AA'} = λ_A λ̄_{A'}`, where `λ_A` is a two-component spinor. Projective spinors `[λ] ∈ CP¹` label points of the celestial sphere.

**Theorem 4.4 (Tetrad and Carrier Transport).** The LCR carrier of Paper 01 is a discrete model of the tetrad: the three coordinates `(L, C, R)` are a discrete local frame, and the reversal involution `ρ(L,C,R) = (R,C,L)` is a discrete model of frame transport. The light-cone direction is the null spinor `k` that labels the observer's past and future boundaries.

*Proof.* The LCR state is a local frame with three distinguished directions: left boundary, center, and right boundary. The reversal involution swaps the two boundary directions while preserving the center, analogous to a Lorentz boost that reverses spatial direction while preserving the timelike component. The null spinor `k` labels the light-cone direction that separates past and future in the observer's local frame. ∎

**Remark (interpretive boundary).** The tetrad is the rigorous framework for relating local frames to spacetime geometry. The claim that the LCR carrier "is" a tetrad is a discrete model, not a derivation of the Einstein field equations. The EFE derivation requires a separate action principle and calibration.

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Status |
|----------|---------|--------|--------|
| `verify_boundary_repair.py` | `boundary_repair_receipt.json` | 7 | pass |

**Check details:**

| Check | Description | Result |
|-------|-------------|--------|
| `consumes_two_paper02_correction_states` | Both `(0,1,0)` and `(1,1,0)` are converted. | pass |
| `preserves_paper03_coordinates` | `(0,1,0) → (2,0)` and `(1,1,0) → (3,1)`. | pass |
| `all_required_fields_present` | Every constraint has all 7 required fields. | pass |
| `constraints_not_proofs` | Status is `"constraint"` in all cases. | pass |
| `next_legal_routes_nonempty` | Every constraint has at least one next route. | pass |
| `repair_is_idempotent` | `repair(repair(x)) = repair(x)` for all repairable `x`. | pass |
| `untyped_failure_rejected` | `{"status": "failed"}` raises `ValueError`. | pass |

**Total:** 7/7 pass.

---

## Hand Reconstruction

1. Start with the two Paper 02 correction states: `(0,1,0)` and `(1,1,0)`.
2. Look up the Paper 03 axis/sheet coordinate for each: `(2,0)` and `(3,1)`.
3. Construct a constraint record for each state with all required fields.
4. Verify that `status` is `"constraint"`, not `"proof"`.
5. Verify that `next_legal_routes` is nonempty.
6. Apply the repair operation again to each constraint record and confirm it does not change.
7. Attempt to repair an untyped failure `{"status": "failed"}` and confirm it is rejected.

---

## Falsifiers and Rejected Claims

| Rejected Claim | Reason |
|---------------|--------|
| "Boundary repair promotes failed joins to proof." | Rejected. The status is explicitly `"constraint"`, not `"proof"`. The operation preserves the epistemic distinction between a failed join and a proven theorem. |
| "All failures in the corpus are repairable." | Rejected. The construction handles only the two Paper 02 correction states. General failure repair is not claimed. |
| "Boundary repair is a theorem about the entire paper suite." | Rejected. The theorem is local to the Paper 02 → Paper 03 → Paper 04 chain. It does not claim global repairability. |
| "Untyped failures are silently ignored." | Rejected. Untyped failures raise `ValueError` and are explicitly rejected. |

---

## Relation to Prior and Later Papers

**Paper 01 (LCR Carrier):** Supplies the local state space `S = {0,1}^3` and the shell grading. The boundary repair operates on LCR states.

**Paper 02 (Correction Surface):** Supplies the correction firing states `(0,1,0)` and `(1,1,0)` and the exact formula `corr = C ∧ ¬R`. These are the only inputs to the repair operation.

**Paper 03 (D4/J3 Triality Surface):** Supplies the axis/sheet coordinates `(2,0)` and `(3,1)` for the correction states. Boundary repair preserves these coordinates.

**Paper 05 (Path Carrier):** The intended target paper for the repaired constraints. The `next_legal_routes` field routes to Paper 05 and optionally back to Paper 03 for stronger theorem intake.

**Later papers:** Boundary repair is the mechanism that keeps the corpus honest after failure. Each later paper that consumes constraints from a prior paper must either accept them as legal input or reject them with a receipt. The boundary repair schema is the contract for this interaction.

---

## Open Obligations

| ID | Disposition |
|----|-------------|
| 04.1 | Wire `verify_boundary_repair` into `cqe_engine.formal`. |
| 04.2 | Connect boundary constraints to Paper 05 path carriers. |
| 04.3 | Promote a shared obligation-ledger schema for all later papers (route to NP-05). |
| 04.4 | Add domain examples (civil crack repair, inventory exception routing) after the formal schema is stable (route to applied papers 81–100). |
| 04.5 | Generalize repair to handle failures beyond the two Paper 02 correction states (route to later formal papers). |
| 04.6 | Prove that the constraint schema is minimal: no proper subset of the required fields suffices for legal next-route consumption. |

---

## Bibliography

[1] N. Barker, *CQE Paper 00 — Established Grounding and Axiom Contract*, `papers/active-rework/00_Established_Grounding_and_Axiom_Contract.md`, 2026. Defines the finite state space and D/I/X claim taxonomy.

[2] N. Barker, *CQE Paper 01 — LCR Chain Carrier*, `papers/active-rework/01_LCR_Chain_Carrier.md`, 2026. Supplies the LCR state space and reversal involution.

[3] N. Barker, *CQE Paper 02 — Correction Surface*, `papers/active-rework/02_Correction_Surface.md`, 2026. Identifies the correction firing states and proves `corr = C ∧ ¬R`.

[4] N. Barker, *CQE Paper 03 — D4/J3 Triality Surface*, `papers/active-rework/03_D4_J3_Triality_Surface.md`, 2026. Supplies the axis/sheet coordinate system and diagonal carrier.

[5] `lattice_forge` substrate modules, CMPLX-PartsFactory-main. Source of the finite algebraic substrate consumed by Papers 01–04.

[6] E. W. Dijkstra, *A Discipline of Programming*, Prentice-Hall, 1976. Reference for the concept of weakest precondition and the constructive treatment of failed states.

[7] C. A. R. Hoare, "An Axiomatic Basis for Computer Programming," *Comm. ACM* 12(10), 1969, 576–580. Reference for pre/postcondition contracts and the logical treatment of program failure.

---

## Conclusion

Boundary repair is the operation that keeps the corpus honest after failure. It does not turn failed joins into proven claims. It turns them into typed, idempotent, replayable constraints that later papers can legally consume. The construction is finite, explicit, and closed: two correction states from Paper 02, two coordinates from Paper 03, seven required fields, and a rejection of untyped failures. The idempotence of the repair operation ensures that applying it twice does not change the result. The honesty guard — that the status is `constraint`, not `proof` — prevents the epistemic error of promoting failed joins to theorems. This is the correct next step after triality registration: not stronger mathematics, but disciplined handling of what the mathematics has not yet closed.
