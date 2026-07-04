# Paper 05 — Oloid Path Carrier

**Status:** IPMC — internal physics map closed for the finite rolling-state carrier and the oloid carrier family base. E6→E7→E8 dyadic lift, Rule 30 standalone prediction, and physical gluon/QCD identification remain open.

**Source papers:** CQE-paper-05, CQE-paper-05.25.  
**Canonical formal paper:** `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-05/FORMAL_PAPER.md`.  
**Verifiers:** `verify_oloid_path_carrier.py`, `verify_oloid_carrier_family.py`, `verify_cd_conjugation_gluon_oloid_theta0.py`, `verify_gluon_oloid_worldline.py`.

---

## Abstract

Paper 05 formalizes the path carrier that receives repaired boundary constraints from Paper 04. The closed claim is structural: a rolling-state carrier can preserve adjacency, order, and receipt state across a curved or cyclic path without requiring a straight-line jump between source and target.

The carrier state is a triple `(sheet, phase, parity)` with a total deterministic step rule. For every finite binary input stream, the carrier produces a continuous trace of legal adjacent states, maintains a binary head/tail dyad at every position, and can carry Paper 04 constraints as replayable payloads. The paper also binds the oloid carrier family substrate: rolling-contact kinematics, single-oloid octonionic grounding, the four-oloid D4 ring, and dual-path read-then-verify flow.

The guard is essential. Paper 05 does not prove that the carrier alone predicts Rule 30 future bits, that the physical Oloid geometry is fully formalized here, or that every curved path is a valid carrier. It proves a finite rolling-state carrier and records the stronger claims as obligations. The E6→E7→E8 dyadic lift is explicitly left open. Physical gluon/QCD identification is a named external bridge, not a closed theorem.

### Keywords

Oloid path carrier; rolling state; head/tail dyad; continuity; constraint payload; oloid family; Cayley-Dickson transfer; gluon worldline; CQECMPLX receipts.

---

## Claim Ledger

| ID | Claim | Tag | Evidence | Boundary |
|----|-------|-----|----------|----------|
| 05.1 | The rolling step `roll(q, b)` is total for every carrier state `q` and every binary input bit `b`. | [D] | `verify_oloid_path_carrier.py`; `oloid_path_carrier_receipt.json` (7/7) | Finite state space `{0,1}×{0,1,2,3}×{0,1}` |
| 05.2 | For every finite binary input stream, the trace produced by successive `roll` applications has length `n+1` and every adjacent pair is a legal step. | [D] | Same verifier | Finite construction |
| 05.3 | The head/tail dyad is binary at every state in the trace. | [D] | Same verifier | Dyad definition |
| 05.4 | A Paper 04 constraint payload can be attached to any trace position without altering the rolling step rule. | [D] | Same verifier | Payload invariance |
| 05.5 | Invalid input bits (non-binary) are rejected with `ValueError`. | [D] | Same verifier | Input validation |
| 05.6 | Discontinuous jumps (skipping intermediate states) are structurally impossible under the step rule. | [D] | Same verifier | Step determinism |
| 05.7 | The oloid carrier family substrate verifiers pass: rolling-contact kinematics, octonionic grounding, four-oloid D4 ring, dual-path read-then-verify. | [D] | `verify_oloid_carrier_family.py`; `oloid_carrier_family_receipt.json` (4/4) | Reapplication of proven substrate |
| 05.8 | The CD-conjugation / oloid-transfer / theta_0 algebra checks pass: home, midpoint, C-bar copy, antipode, zero balance, equal weight, orthogonal conservation, self-adjointness, distinct rungs. | [D] | `verify_cd_conjugation_gluon_oloid_theta0.py`; `cd_conjugation_gluon_oloid_theta0_receipt.json` (9/9) | Finite algebraic checks on the doubling plane |
| 05.9 | The gluon oloid worldline checks pass: conservation, antipode invariance, shedding, bounded error, Mobius twist, orientation flip, Klein closure, quark-to-resolution. | [D] | `verify_gluon_oloid_worldline.py`; `gluon_oloid_worldline_receipt.json` (8/8) | Finite topological checks on the chart |
| 05.10 | The E6→E7→E8 dyadic lift is proven in this paper. | [X] | No closing receipt | Named open bridge (O2'''); route to exceptional papers |
| 05.11 | The oloid carrier alone predicts Rule 30 future bits without later readout/prediction receipts. | [X] | No closing receipt | Papers 10 and 12 carry finite/readout prediction receipts |
| 05.12 | Physical gluon/QCD identification or measured mass/gravity drive is a closed theorem. | [X] | No closing receipt | Named external bridge (P05/P26/PH-3); model reading |
| 05.13 | Every curved path is a valid carrier. | [X] | Not claimed | Only the specific rolling step rule is verified |

---

## Definitions

**Definition 5.1 (Carrier state space).** Let `Q = {0,1} × {0,1,2,3} × {0,1}`. An element `q = (sheet, phase, parity) ∈ Q` is a rolling carrier state.

**Definition 5.2 (Rolling step).** Given a carrier state `q = (s, p, r) ∈ Q` and an input bit `b ∈ {0,1}`, define

```text
roll(q, b) = ((s + 1) mod 2, (p + 1) mod 4, r ⊕ b).
```

**Definition 5.3 (Head/tail dyad).** Given `q = (s, p, r)`, define

```text
head(q) = s,
tail(q) = ((p mod 2) ⊕ s ⊕ r) mod 2.
```

**Definition 5.4 (Trace).** Given a finite binary input stream `b₁, b₂, ..., bₙ` and an initial state `q₀ ∈ Q`, the trace is the sequence `q₀, q₁, ..., qₙ` where `qᵢ = roll(qᵢ₋₁, bᵢ)` for `i = 1, ..., n`.

**Definition 5.5 (Continuous carrier trace).** A trace is continuous if every adjacent pair `(qᵢ₋₁, qᵢ)` satisfies `qᵢ = roll(qᵢ₋₁, bᵢ)` for the corresponding input bit `bᵢ`.

**Definition 5.6 (Payload attachment).** A payload is an arbitrary record (e.g., a Paper 04 constraint). Attaching a payload to a trace position means including it as metadata without modifying the carrier state or the step rule.

---

## Theorems and Proofs

**Theorem 5.1 (Rolling Path Carrier).** For every finite binary input stream `b₁, ..., bₙ` and every initial state `q₀ ∈ Q`, the trace `q₀, ..., qₙ` is continuous, has length `n+1`, preserves input order, maintains a binary head/tail dyad at every state, and can carry Paper 04 constraints as payloads without altering the path.

*Proof.* The step rule `roll(q, b)` is a total function on `Q × {0,1}` because `(s+1) mod 2 ∈ {0,1}`, `(p+1) mod 4 ∈ {0,1,2,3}`, and `r ⊕ b ∈ {0,1}` for all `s, p, r, b`. Thus for every valid `q` and `b`, a unique successor exists. By induction on `n`, the trace has length `n+1` and every adjacent pair `(qᵢ₋₁, qᵢ)` satisfies `qᵢ = roll(qᵢ₋₁, bᵢ)`, so the trace is continuous by construction. Input order is preserved because the trace is generated by successive application of the input bits in order. ∎

For the head/tail dyad: `head(q) = s ∈ {0,1}` and `tail(q) = ((p mod 2) ⊕ s ⊕ r) mod 2 ∈ {0,1}` for all `q ∈ Q`. Therefore the dyad is binary at every state. ∎

For payload attachment: by Definition 5.6, the payload is metadata. The step rule depends only on `q` and `b`, not on any payload. Therefore attaching a payload does not alter `roll(q, b)` and does not break continuity. ∎

*(Invalid bit rejection)* If `b ∉ {0,1}`, the step rule raises `ValueError` by definition. The verifier confirms this by attempting `roll(q, 2)` and catching the exception. ∎

*(Discontinuous jump rejection)* A discontinuous jump would require `qᵢ = roll(qᵢ₋₂, bᵢ)` for some `i`, but the step rule is deterministic and each state has exactly one legal successor for a given input bit. The verifier confirms that `roll(q₀, b₁) ≠ q₂` (the state after two steps is not reachable in one step from the initial state). ∎

**Theorem 5.2 (Oloid Carrier Family Reapplication).** The substrate oloid mechanisms — rolling-contact kinematics, single-oloid octonionic grounding, the four-oloid D4 ring, and dual-path read-then-verify flow — are paper-bound to Paper 05. All four mechanism verifiers pass.

*Proof.* The verifier `verify_oloid_carrier_family.py` replays the substrate checks from `lattice_forge.oloid_rolling`, `lattice_forge.oloid_octonionic`, `lattice_forge.quad_oloid`, and `lattice_forge.oloid_dual_path`. All four checks return `pass`. The theorem binds these proven substrate mechanisms to Paper 05 as the carrier-family base. It does not close the E6→E7→E8 dyadic lift, which remains a named open bridge. ∎

**Theorem 5.3 (CD Conjugation and Gluon Worldline).** The Cayley-Dickson conjugation / oloid-transfer / theta₀ algebra and the gluon oloid worldline are paper-bound to Paper 05 as finite algebraic and topological checks. All checks pass.

*Proof.* The verifier `verify_cd_conjugation_gluon_oloid_theta0.py` checks that theta₀=0 is the gluon's home, the transfer to C-bar copy occurs at π/2, the midpoint is at π/4, the antipode is at π, and the orthogonal transfer conserves C. All 9 checks pass. The verifier `verify_gluon_oloid_worldline.py` checks gluon conservation, antipode invariance, shedding, bounded error, Mobius half-twist, orientation flip, Klein closure, and quark-to-resolution. All 8 checks pass.

The honesty notes in both receipts state that the physical gluon/QCD identification and measured mass/gravity drive are the model's reading plus named external bridges (P05/P26/PH-3), not closed theorems in this paper. The finite algebraic and topological checks are closed; the physical interpretation is IBN. ∎

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Status |
|----------|---------|--------|--------|
| `verify_oloid_path_carrier.py` | `oloid_path_carrier_receipt.json` | 7 | pass |
| `verify_oloid_carrier_family.py` | `oloid_carrier_family_receipt.json` | 4 | pass |
| `verify_cd_conjugation_gluon_oloid_theta0.py` | `cd_conjugation_gluon_oloid_theta0_receipt.json` | 9 | pass |
| `verify_gluon_oloid_worldline.py` | `gluon_oloid_worldline_receipt.json` | 8 | pass |

**Total checks:** 28/28 pass.

**Check details for path carrier:**

| Check | Description | Result |
|-------|-------------|--------|
| `trace_length_is_input_length_plus_one` | `len(trace) = len(bits) + 1` | pass |
| `adjacent_pairs_are_legal_rolls` | Every `(qᵢ₋₁, qᵢ)` satisfies `qᵢ = roll(qᵢ₋₁, bᵢ)` | pass |
| `head_tail_dyads_are_binary` | `head(q), tail(q) ∈ {0,1}` for all `q` in trace | pass |
| `payload_does_not_alter_path_rule` | Metadata attachment does not change step rule | pass |
| `invalid_bit_rejected` | `roll(q, 2)` raises `ValueError` | pass |
| `discontinuous_jump_rejected` | `roll(q₀, b₁) ≠ q₂` | pass |
| `prediction_claim_left_out_of_scope` | Explicit scope boundary recorded | pass |

---

## Hand Reconstruction

1. Draw the eight carrier positions: `sheet ∈ {0,1}`, `phase ∈ {0,1,2,3}`.
2. Start at `(sheet=0, phase=0, parity=0)`.
3. Read a binary input bit.
4. Flip `sheet`, advance `phase` by 1 (mod 4), and XOR `parity` with the bit.
5. Record the new head/tail dyad: `head = sheet`, `tail = (phase mod 2) ⊕ sheet ⊕ parity`.
6. Attach any Paper 04 constraint as a payload at the current step.
7. Repeat for the input stream.
8. Reject any input that is not binary, or any path that skips a phase or sheet flip.
9. Confirm that the payload does not change the step rule.

---

## Falsifiers and Rejected Claims

| Rejected Claim | Reason |
|---------------|--------|
| "The oloid carrier alone predicts Rule 30 future bits." | Rejected. The carrier proves structural continuity, not prediction. Prediction claims are downstream in Papers 10 and 12. |
| "The E6→E7→E8 dyadic lift is closed in this paper." | Rejected. The carrier family verifier returns `pass_with_open_bridge` for the dyadic lift. It is a named obligation, not a closed theorem. |
| "Physical gluon/QCD identification is a closed theorem." | Rejected. The gluon worldline checks are finite algebraic/topological checks on the chart. The physical identification is a named external bridge (IBN). |
| "Every curved path is a valid carrier." | Rejected. Only the specific rolling step rule is verified. Other curved paths may or may not be valid carriers. |
| "The oloid model itself is the complete Rule 30 predictor." | Rejected. The paper proves the carrier property, not standalone prediction. |

---

## Relation to Prior and Later Papers

**Paper 01 (LCR Carrier):** Supplies the local state space `S = {0,1}^3` and the shell grading. The oloid carrier operates on a different state space `Q` but consumes the same binary input language.

**Paper 02 (Correction Surface):** Supplies the correction firing states. These states may appear as inputs to the carrier, but the carrier does not interpret them; it only transports them.

**Paper 03 (D4/J3 Triality Surface):** Supplies the axis/sheet coordinate system. The carrier can preserve these coordinates as metadata during transport.

**Paper 04 (Boundary Repair):** Supplies the typed constraints that the carrier transports. The payload attachment mechanism carries Paper 04 constraints without altering the path.

**Papers 10 and 12:** Carry downstream finite/readout prediction receipts. The carrier (Paper 05) provides the structural continuity they need; the prediction claims are separate and later.

**Paper 26 / PH-3:** The physical gluon/QCD identification and measured mass/gravity drive are external bridges. The finite algebraic checks in Paper 05 support these later claims but do not close them.

## Nonholonomic Geometry and Rolling Holonomy

Paper 05 proves a finite rolling-state carrier. The proper mathematical framework for "rolling" as a universal mechanism is nonholonomic geometry. This section records the exact formalism and the boundary between the finite carrier and the full geometric theory.

**Definition 5.7 (Configuration bundle).** Let `Q → B` be a configuration bundle. The base `B` tracks visible placement; the total space `Q` includes orientation, contact, linking, internal phase, and constraint state.

**Definition 5.8 (Rolling distribution).** A rolling constraint defines an allowed distribution `D ⊂ TQ`. It is nonholonomic when `D` is not integrable into fixed configuration submanifolds.

**Definition 5.9 (Local connection).** A local connection on the configuration bundle is written schematically:
```
g⁻¹ ġ = −A(x) ẋ,
```
where `g` is the group element recording orientation, `A(x)` is the connection 1-form, and `ẋ` is the base velocity.

**Definition 5.10 (Holonomy).** Closed transport along a loop `γ` gives:
```
g(T) = P exp(−∮_γ A) g(0).
```
Then `x(T) = x(0)` does not imply `g(T) = g(0)`. The holonomy is the group element accumulated by transport around the loop.

**Theorem 5.4 (Rolling Holonomy).** The oloid carrier of Paper 05 is a discrete model of rolling holonomy. The step rule `roll(q, b)` preserves a nonholonomic constraint: the carrier state advances in the base `B` (phase) while the orientation `g` (sheet, parity) changes according to a discrete connection. The holonomy is nontrivial: a closed base path (returning to the same phase) does not necessarily return to the same carrier state.

*Proof.* The carrier state is `q = (sheet, phase, parity)`. The base variable is `phase`. The step rule advances `phase` by 1 (mod 4) and updates `sheet` and `parity` according to the input bit. After 4 steps, `phase` returns to its initial value, but `(sheet, parity)` may have changed. Thus a closed base path (4 steps) produces a holonomy in the `(sheet, parity)` fiber. The holonomy is nontrivial because `sheet` flips every step and `parity` XORs with the input bits. ∎

**Remark (interpretive boundary).** Nonholonomic geometry is the correct framework for rolling. The claim that "all stable matter is recurrently closed nonholonomic transport" remains a physical hypothesis requiring an action, conservation law, spectrum, and empirical test. The finite carrier of Paper 05 is a discrete model, not a proof of the universal hypothesis.

---

## Open Obligations

| ID | Disposition |
|----|-------------|
| 05.1 | Wire `verify_oloid_path_carrier` into `cqe_engine.formal`. |
| 05.2 | Connect Paper 04 constraint payloads to a shared route ledger. |
| 05.3 | Close the E6→E7→E8 dyadic lift (O2''') with a separate verifier. |
| 05.4 | Separate physical Oloid geometry claims from finite rolling-state claims. |
| 05.5 | Treat Rule 30 prediction as downstream: Papers 10 and 12 carry finite/readout prediction receipts. |
| 05.6 | Physical gluon/QCD identification and measured mass/gravity drive (route to P26/PH-3). |
| 05.7 | Prove that the carrier state space `Q` is minimal: no proper subset supports the rolling step, dyad, and payload properties. |
| 05.8 | Add domain examples (mechanical rolling contact, signal routing) after the formal schema is stable. |

---

## Bibliography

[1] N. Barker, *CQE Paper 00 — Established Grounding and Axiom Contract*, `papers/active-rework/00_Established_Grounding_and_Axiom_Contract.md`, 2026. Defines the finite state space and D/I/X claim taxonomy.

[2] N. Barker, *CQE Paper 01 — LCR Chain Carrier*, `papers/active-rework/01_LCR_Chain_Carrier.md`, 2026. Supplies the LCR state space and reversal involution.

[3] N. Barker, *CQE Paper 02 — Correction Surface*, `papers/active-rework/02_Correction_Surface.md`, 2026. Identifies the correction firing states and proves `corr = C ∧ ¬R`.

[4] N. Barker, *CQE Paper 03 — D4/J3 Triality Surface*, `papers/active-rework/03_D4_J3_Triality_Surface.md`, 2026. Supplies the axis/sheet coordinate system.

[5] N. Barker, *CQE Paper 04 — Boundary Repair*, `papers/active-rework/04_Boundary_Repair.md`, 2026. Supplies the typed constraints that the carrier transports.

[6] `lattice_forge` oloid modules (`oloid_rolling`, `oloid_octonionic`, `quad_oloid`, `oloid_dual_path`), CMPLX-PartsFactory-main. Substrate modules for the oloid carrier family. Reapplied in Paper 05.

[7] J. C. Baez, "The Octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Survey of octonion and exceptional algebra structure.

[8] N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. Reference for `J3(O)` and Peirce decomposition.

[9] J. H. Conway and D. A. Smith, *On Quaternions and Octonions*, A K Peters, 2003. Reference for octonion arithmetic and Cayley-Dickson doubling.

[10] R. D. Schafer, *An Introduction to Non-Associative Algebras*, Dover, 1995. Standard reference for non-associative algebra and Jordan structures.

---

## Conclusion

Paper 05 proves a path-carrier property, not a standalone prophecy. A rolling carrier can preserve continuity across a non-straight path, carry repaired constraints from Paper 04, and emit replayable dyads at each step. The step rule is total, deterministic, and idempotent in the sense that the trace is uniquely determined by the input. The carrier rejects invalid bits and discontinuous jumps by construction.

The oloid carrier family is bound as a verified substrate: rolling-contact kinematics, octonionic grounding, four-oloid D4 ring, and dual-path flow all pass their finite checks. The CD conjugation and gluon worldline checks pass as finite algebraic and topological structures on the chart. The honesty guard is the point: the E6→E7→E8 dyadic lift is left open, Rule 30 prediction is routed to later papers, and physical gluon/QCD identification is named as an external bridge. The carrier is the kernel used by later readout and finite prediction papers — strong enough to transport constraints, narrow enough to keep stronger claims honest.
