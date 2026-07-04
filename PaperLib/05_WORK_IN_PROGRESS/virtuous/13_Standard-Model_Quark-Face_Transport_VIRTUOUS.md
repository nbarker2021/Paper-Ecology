# Paper 13 - Standard-Model Quark-Face Transport

**Virtuous rework status:** merged from current rework, canonical formal paper, companion variants, verifier receipts, and saved CAM/GLM crystal data.

**Method:** preserve the strongest representation of each source face; when
sources disagree, keep the disagreement as a named boundary or next-need.

---

## Source Faces

| Face | Path | Words / count | Contribution |
|------|------|---------------|--------------|
| Current rework | `D:\Paper Reworks\13_Standard_Model_Quark_Face_Transport.md` | 546 words | Existing skeleton, current status, obligations. |
| Canonical formal paper | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-13\FORMAL_PAPER.md` | 1373 words | Main theorem, proof, receipt, falsifier spine. |
| Companion variant | `CQE-paper-13.25.md` | 345 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-13.50.md` | 372 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-13.75.md` | 291 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-13_RECURSIVE_CLOSE.md` | 1296 words | Alternate toolkit/contract/bridge phrasing. |
| Formal verifiers | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-13` | 6 files | Executable evidence surface. |
| Formal receipts | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-13` | 7 files | Receipt status and check counts. |
| Saved CAM nodes | `D:\CQE_CMPLX\_downloads_review\content_addressed_nodes.json` | 4 relevant nodes | Prior crystal evidence and obligation nodes. |
| Saved GLM closure rows | `D:\CQE_CMPLX\_downloads_review\glm_obligation_closure_matrix.json` | 1 relevant rows | Closure/partial-closure status updates. |

## Virtuous Synthesis

This paper states the CQECMPLX Standard-Model quark-face physics map at the
algebraic transport layer. The shell-2 `LCR` chart has exactly three states;
those states correspond to the three trace-2 idempotents of `J_3(O)`; the
six-element `S_3` Weyl action closes on that triple; and the `n=3` shell-2
transition is an exact element of the `SU(3)` Weyl group ring over the
rationals. A bounded `G2/F4/T5A` route classifies already-enumerated bits in at
most three stages.

This version treats the formal paper as the proof spine, the companion variants as interface contracts, and the CAM/GLM rows as status-bearing crystal data. The paper's open obligations are not deleted; they are the next work items required before stronger claims can be promoted.

## Saved CAM / GLM Updates

| Finding | Obligation | Old status | Proposed status | Verifier | Meaning |
|---------|------------|------------|-----------------|----------|---------|
| `GLM-F7-SM04` | `obligation-13.3` | genuinely_open | partially_closed | `verify_glm_spin12_spin16_root_decomp.py` | advances_to_partial |

## Companion Face Digest

- **Paper 13.25 - Toolkit for Quark-Face Transport.** This support paper exposes the tools for Paper 13. It is not the proof-carrying
paper. The proof is the finite algebraic closure in Paper 13; this toolkit shows
how to inspect the same closure digitally and by ordinary visible marks.
- **Paper 13.50 - Quark-Face Transport Claim Contract.** This contract defines what may be admitted as a Paper 13 claim and what must
remain an obligation. It protects the distinction between proved algebraic
transport and proposed physical interpretation.
- **Paper 13.75 - Quark-Face Transport as Next-State Precondition.** This bridge states what later papers may inherit from Paper 13. It prepares the
transition into Paper 14 without letting the Standard Model analogy outrun the
receipt.
- **Paper 13 - Standard-Model Quark-Face Transport (SECOND PASS: LIB-BASED RECURSIVE LIGHT-CONE CLOSURE).** # Paper 13 - Standard-Model Quark-Face Transport (SECOND PASS: LIB-BASED RECURSIVE LIGHT-CONE CLOSURE) ## Claim Class: **internal_physics_map_closed** — The quark-face transport is the proven exact SU(3) color-transport model, with all open obligations resolved by local light-cone re-invocation at the exact boundary error. --- ## The Lib-Based Recursive Closure Mechanism (From the Actual Forge) **The lib provides the exact closure operator at the boundary error:** ```python # From lattice_forge/rule30_nth_bit.py CORRECTION_FIRING_STATES = frozenset({(0,1,0), (1,1,0)}) # C=1, R=0 # From rule90_linearization.py correction(L,C,R) = C & (1-R) lucas_bit(d, x) # O(log d) closed-form Rule 90 # From rule30_nth_bit.py - Layer 1: Oracle T_EMISSION (PROVEN) t_emission(L,C,R) = (1 - L) if C == 1 else (L ^ R) # 0 defects at 4096 depths # Layer 2: Lucas + Oracle Correction (ARCHITECTURE PROVEN) Rule_3

## Missed Verifier Rows to Reconcile

- `verify_glm_spin12_spin16_root_decomp.py`

## Receipt Surface

| Receipt | Summary |
|---------|---------|
| `ckm_calibration_receipt.json` | keys=su3_transport,ckm_derivation,pdg_reference,calibration_status,external_bridge |
| `invariant_transfer_su2u1_in_su3_receipt.json` | status=pass; checks=7/7 |
| `quark_face_transport_literalized_receipt.json` | status=pass; checks=10/10 |
| `quark_face_transport_receipt.json` | status=pass; checks=9/9 |
| `rule30_shell_verification_ledger_receipt.json` | status=pass; checks=13/13 |
| `spin12_spin16_root_decomp_receipt.json` | status=True; checks=10/10 |
| `standard_model_real_comparison_receipt.json` | status=pass; checks=8/8 |

## Open Obligations as Next Needs

| ID | Current row | CAM/GLM status |
|----|-------------|----------------|
| `13.1` | \| 13.1 \| Exact numeric CKM calibration (`ckm_calibration_receipt.json`) \| External calibration / CQE-13 \| | carry as next need |
| `13.2` | \| 13.2 \| Physical quark / color-charge measurement bridge \| External calibration \| | carry as next need |
| `13.3` | \| 13.3 \| Unconditional cold-start G2/F4/T5A route \| Later formal paper \| | GLM-F7-SM04 -> partially_closed |

## Obligation Springboard Lanes

Obligations return to the earliest paper they can affect, then rework upward through each paper in the lane before the local claim is promoted.

### Local Claim Pressure

- Receipt-closed items may strengthen replayability and audit language, but they do not close unrelated transport, physical, or cold-start mathematical obligations.
- Partial CAM/GLM closures should be imported as bounded progress: name the verifier, state the portion advanced, and keep the residual claim visible.
- All physical or unit-bearing readings must pass through an external calibration gate before appearing as more than conditional interface language.

### Local Lane Table

| Obligation | Return start | Upward lane | Rework instruction |
|------------|--------------|-------------|--------------------|
| `13.1` | `09` | `09 -> 10 -> 11 -> 12 -> 13` | Strengthen receipt/path language and ensure any downstream theorem depends on replayable receipts rather than assumed file layout. |
| `13.2` | `09` | `09 -> 10 -> 11 -> 12 -> 13` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `13.3` | `09` | `09 -> 10 -> 11 -> 12 -> 13` | Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named. |

## Detailed Expansion Pass

### Paper-Level Thesis

Paper 13 functions as the suite's Standard-Model quark-face transport and calibration boundary. Its virtuous version should therefore make three layers visible at once: the formal claim that is actually proved, the receipt or verifier evidence that lets the claim be replayed, and the explicit boundary that prevents the reader from promoting an open lift into a closed theorem.

The companion variants are used as exposition and interface contracts. They may contribute terminology, examples, and downstream preconditions, but the canonical formal paper remains the proof spine.

### Claim Status Ledger

| Claim/Theorem | Working status | Required paper treatment |
|---------------|----------------|--------------------------|
| **Claim 13.1.** The shell-2 chart stratum is the three-element set | bounded or engineering-backed | name verifier-backed portion and keep residual open |
| **Claim 13.2.** The three shell-2 states map bijectively to the three trace-2 | bounded or engineering-backed | name verifier-backed portion and keep residual open |
| **Claim 13.3.** The six permutations of diagonal indices in `S_3` close on the | bounded or engineering-backed | name verifier-backed portion and keep residual open |
| **Claim 13.4.** The `n=3` shell-2 transition is an exact `SU(3)` Weyl group-ring | bounded or engineering-backed | name verifier-backed portion and keep residual open |
| **Claim 13.5.** The bounded `G2/F4/T5A` route is a route classifier for an | bounded or engineering-backed | name verifier-backed portion and keep residual open |
| **Claim 13.6.** The color/anticolor six-face model is the hand-facing exposure | bounded or engineering-backed | name verifier-backed portion and keep residual open |
| **Claim 13.7.** `QuarkFaceForge` literalizes the structural color-transport | bounded or engineering-backed | name verifier-backed portion and keep residual open |
| **Claim 13.8.** Against published Standard-Model data (PDG/CODATA, retrieved | bounded or engineering-backed | name verifier-backed portion and keep residual open |
| **Theorem 13.2, Quark-Face Color Transport Literalization.** The | bounded or engineering-backed | name verifier-backed portion and keep residual open |

### Evidence and Receipt Detail

The receipt surface should be discussed in prose, not only listed. Passing receipts make the paper replayable; failed, partial, or missing checks become local boundaries.
- `ckm_calibration_receipt.json`: keys=su3_transport,ckm_derivation,pdg_reference,calibration_status,external_bridge.
- `invariant_transfer_su2u1_in_su3_receipt.json`: status=pass; checks=7/7.
- `quark_face_transport_literalized_receipt.json`: status=pass; checks=10/10.
- `quark_face_transport_receipt.json`: status=pass; checks=9/9.
- `rule30_shell_verification_ledger_receipt.json`: status=pass; checks=13/13.
- `spin12_spin16_root_decomp_receipt.json`: status=True; checks=10/10.
- `standard_model_real_comparison_receipt.json`: status=pass; checks=8/8.
Verifier files are the strongest executable surface. The paper should name the verifier next to any claim it supports.
- `verify_glm_spin12_spin16_root_decomp.py` should be mapped to the claim or obligation it checks.
- `verify_invariant_transfer_su2u1_in_su3.py` should be mapped to the claim or obligation it checks.
- `verify_quark_face_transport.py` should be mapped to the claim or obligation it checks.
- `verify_quark_face_transport_literalized.py` should be mapped to the claim or obligation it checks.
- `verify_rule30_shell_verification_ledger.py` should be mapped to the claim or obligation it checks.
- `verify_standard_model_real_comparison.py` should be mapped to the claim or obligation it checks.

### Obligation Workups

**13.1.** | 13.1 | Exact numeric CKM calibration (`ckm_calibration_receipt.json`) | External calibration / CQE-13 |

- **Status reading:** strengthenable after receipt path and replay language are explicit.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13`.
- **Paper-local consequence:** Strengthen receipt/path language and ensure any downstream theorem depends on replayable receipts rather than assumed file layout.
- **Rewrite requirement:** use the item to strengthen auditability, not to promote mathematical or physical scope beyond the receipt.
- **Upward effect:** Papers in the lane must preserve the `Standard-Model quark-face transport and calibration boundary` boundary before this obligation can strengthen the source paper.

**13.2.** | 13.2 | Physical quark / color-charge measurement bridge | External calibration |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `Standard-Model quark-face transport and calibration boundary` boundary before this obligation can strengthen the source paper.

**13.3.** | 13.3 | Unconditional cold-start G2/F4/T5A route | Later formal paper |

- **Status reading:** partially closed by bounded verifier evidence.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13`.
- **Paper-local consequence:** Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named.
- **Saved evidence to import:** `GLM-F7-SM04` via `verify_glm_spin12_spin16_root_decomp.py` (partially_closed).
- **Rewrite requirement:** add a bounded-progress sentence naming the verifier and a residual-open sentence naming the part not yet closed.
- **Upward effect:** Papers in the lane must preserve the `Standard-Model quark-face transport and calibration boundary` boundary before this obligation can strengthen the source paper.

### Cross-Paper Inheritance

The springboard lane means this paper cannot be revised in isolation. The upstream papers in the lane must preserve the following inherited roles before the local claim can be strengthened:

- Paper 09: finite Hamiltonian-window substrate and receipt-preserving temporal readout.
- Paper 10: master receipt, replay boundary, and open-lift visibility layer.
- Paper 11: theory-admission gate and boundary classifier.
- Paper 12: cellular-automaton prediction surface and Rule 30 scope boundary.
- Paper 13: Standard-Model quark-face transport and calibration boundary.

### Publication-Grade Rewrite Targets

For the next manual/editorial pass, expand the paper body around these targets:

1. Put the strongest closed theorem in the opening synthesis, then immediately state the largest thing it does not prove.
2. Move every calibration, physical-identification, and external-validation claim into a guarded paragraph with its required witness named.
3. Place verifier and receipt names beside the exact claims they support.
4. Preserve open lifts as first-class obligations rather than treating them as editorial TODOs.


## Canonical Formal Spine

## Abstract

This paper states the CQECMPLX Standard-Model quark-face physics map at the
algebraic transport layer. The shell-2 `LCR` chart has exactly three states;
those states correspond to the three trace-2 idempotents of `J_3(O)`; the
six-element `S_3` Weyl action closes on that triple; and the `n=3` shell-2
transition is an exact element of the `SU(3)` Weyl group ring over the
rationals. A bounded `G2/F4/T5A` route classifies already-enumerated bits in at
most three stages.

The claim is therefore affirmative: CQECMPLX supplies a closed algebraic
color-transport model for the quark-face layer. The remaining obligation is not
permission to use the physics language; it is the external calibration that
would identify this transport model with measured quark color charge, CKM
phase, weak parity, or a complete Standard Model extension.

## Claims

**Claim 13.1.** The shell-2 chart stratum is the three-element set
`{(1,1,0), (1,0,1), (0,1,1)}`.

**Claim 13.2.** The three shell-2 states map bijectively to the three trace-2
idempotents `{E11+E22, E11+E33, E22+E33}` in `J_3(O)`.

**Claim 13.3.** The six permutations of diagonal indices in `S_3` close on the
trace-2 triple.

**Claim 13.4.** The `n=3` shell-2 transition is an exact `SU(3)` Weyl group-ring
element with residual squared equal to `0` over `Q`.

**Claim 13.5.** The bounded `G2/F4/T5A` route is a route classifier for an
already-enumerated bit.

**Claim 13.6.** The color/anticolor six-face model is the hand-facing exposure
surface for the same algebraic color transport.

**Claim 13.7.** `QuarkFaceForge` literalizes the structural color-transport
surface: three colors, the `S_3` Weyl action, exact `n=3` `SU(3)` closure,
trace conservation, the shell-2 chiral doublet, `J_3(O)` faces, and color
confinement as an algebraic transport boundary.

**Claim 13.8.** Against published Standard-Model data (PDG/CODATA, retrieved
2026-06-14, no live measurement) the framework `SU(3)` color sector matches
real QCD on four independent structural counts: three colors, eight gluons =
adjoint = chart, `S_3` Weyl = color group, and six `A_2` roots = excited
states. `alpha` and generation counts are suggestive/underived; the VOA mass
partition does not map to the gauge-boson spectrum. That single non-match is a
`2x2x2` vs `3x3` *basis* difference, not a failure (`3 x 3 = 9 = 8 (+) 1`; the
chart `2^3 = 8` is the traceless adjoint, the standard `3 x 3` carries the
trace/singlet), as closed in Paper 15. Numerical mass reconciliation via the
trace correction is the remaining calibration.

## Definitions

An **LCR chart state** is a triple `(L,C,R)` in `{0,1}^3`.

The **shell** of a chart state is `L + C + R`.

The **shell-2 stratum** is the set of chart states with shell value `2`.

A **quark face** in this paper is one member of the trace-2 idempotent triple
of `J_3(O)`, read as the CQECMPLX algebraic color-transport face. The term is
used affirmatively as the model's Standard-Model-facing object; measured
particle identification is the later calibration step.

The **color Weyl action** is the `S_3` action induced by permuting diagonal
indices `(1,2,3)` and then reading the induced permutation of trace-2
idempotent pairs.

A **bounded route classifier** is a route that may classify an already-supplied
enumeration value while preserving a visible boundary that it did not derive the
value from depth alone.

## Theorem 13

The CQECMPLX quark-face layer is a closed algebraic transport layer:

```text
shell-2 LCR triple
-> trace-2 J_3(O) idempotent triple
-> closed S_3 Weyl action
-> exact n=3 SU(3) group-ring closure
-> bounded exceptional route classification
```

and this is the CQECMPLX color-transport physics map. The remaining obligation
is external Standard-Model calibration, not the internal algebraic transport.

**Theorem 13.2, Quark-Face Color Transport Literalization.** The
`QuarkFaceForge` package surface implements the algebraic color-transport
claims of Paper 13 as importable code and verifies them with ten finite checks.
This closes the literal package transport layer. Measured quark physics, CKM
phase, weak parity, and full Standard Model identification are the external
calibration targets.

## Proof

First enumerate all binary chart states with shell value `2`. There are exactly
three:

```text
C- = (1,1,0)
C0 = (1,0,1)
C+ = (0,1,1)
```

This proves Claim 13.1 by exhaustion.

Next map these states to the trace-2 idempotents:

```text
C- -> E11 + E22
C0 -> E11 + E33
C+ -> E22 + E33
```

`verify_j3o_axioms` verifies that the diagonal idempotents are idempotent and
Jordan-orthogonal, that they sum to the identity, and that the three trace-2
objects have trace `2` and are idempotent. This proves Claim 13.2 at the
algebraic layer.

Now let a permutation `sigma` in `S_3` act on diagonal indices. For any trace-2
pair `{i,j}`, the image is `{sigma(i), sigma(j)}`, again one of the three
two-element diagonal pairs. Since all six permutations are enumerated and every
image lands inside the same three-element set, the Weyl action closes on the
quark-face triple. This proves Claim 13.3.

The exact transition check is stronger than a floating-point fit. The verifier
`verify_n3_su3_closure_exact` computes the `n=3` shell-2 conditional matrix and
decomposes it over the `S_3` permutation matrices using rational arithmetic. The
receipt reports residual squared equal to `0` and `is_exact_group_ring_element =
true`. This proves Claim 13.4.

The exceptional route layer is then admitted with its honesty boundary intact.
`verify_conjugate_triple(max_depth=256)` reports a passing bounded classifier:
the route is oracle-backed, all tested routes resolve in at most three stages,
and `depth_only_bridge` is false. Therefore it classifies supplied bits inside
the transport map. This proves Claim 13.5 while preserving cold-start extraction
as a separate problem.

Finally, the six-face model has three color faces, three conjugate faces,
involutive conjugation, and a closed `Z3` cycle on the three color faces. That
is the hand-facing exposure surface of the algebraic color transport. This
proves Claim 13.6.

Combining the five closed algebraic layers and the explicit physical boundary
proves the theorem.

For Theorem 13.2, `verify_quark_face_transport_literalized.py` imports
`QuarkFaceForge` and checks the full package-facing transport literalization.
The verifier passes ten checks: three colors, six `S_3` Weyl actions, exact
`n=3` `SU(3)` closure, trace preservation, shell-2 chiral doublet structure,
`J_3(O)` face transport, and algebraic confinement boundary. The receipt
therefore upgrades the structural package layer from prose to executable
transport. Because the verifier names physical identification as outside
scope, this theorem remains a software-literal closure whose remaining bridge
is measured-particle calibration.

## Receipt

The promoted verifier is:

```text
production/formal-papers/CQE-paper-13/verify_quark_face_transport.py
production/formal-papers/CQE-paper-13/verify_quark_face_transport_literalized.py
```

It writes:

```text
production/formal-papers/CQE-paper-13/quark_face_transport_receipt.json
production/formal-papers/CQE-paper-13/quark_face_transport_literalized_receipt.json
```

The Standard-Model real-data comparison (Claim 13.8) is verified by:

```text
verify_standard_model_real_comparison.py -> standard_model_real_comparison_receipt.json (8/8)
```

It is a classified comparison, not a physics proof: four EXACT structural
matches, three SUGGESTIVE/underived rows, and one stated non-match whose
basis-difference resolution lives in Paper 15.

The bounded-route honesty boundary (Claim 13.5) is spot-tested against the
standalone Rule 30 +/-1 shell verification ledger:

```text
verify_rule30_shell_verification_ledger.py -> rule30_shell_verification_ledger_receipt.json (13/13)
```

It loads `CMPLX-R30-main/VERIFICATION/RULE30_PLUS_MINUS_ONE_SHELL.json` and
confirms the suite's own tiers agree with this paper: `J3O_DIAGONAL_CARRIER`
and `GLUON_LR_INVARIANCE` are `demonstrated` (the proven core), while
`G2_F4_T5A_BOUNDED_ROUTE` is `bounded` — the data-side confirmation that the
G2/F4/T5A route is a bounded classifier, not a cold-start derivation.

The closed layers are:

```text
three shell-2 chart states
three trace-2 J_3(O) idempotents
six S3 Weyl actions close on the trace-2 triple
n=3 shell-2 transition is exact over the SU(3) Weyl group ring
bounded G2/F4/T5A route classifies oracle-enumerated bits in <=3 stages
six-face color/anticolor analog model is internally consistent
```

The open layers are:

```text
calibration to measured physical quark color charge
calibration to measured CKM phase or V-A weak structure
cold-start depth-only derivation through the G2/F4/T5A route
```

## Falsifiers

This paper fails if the shell-2 stratum does not contain exactly three states.

It fails if any trace-2 idempotent check in `J_3(O)` fails.

It fails if any `S_3` action leaves the trace-2 triple.

It fails if exact `n=3` closure has nonzero residual.

It fails if the bounded route is presented as a cold-start derivation.

It fails if the algebraic color-transport map is presented as a measured
Standard Model calibration without the calibration bridge.

## Role in the Suite

Paper 12 supplies a local CA prediction surface. Paper 13 receives one of its
correction/transport fields and reads it through a three-face `J_3(O)` and
`SU(3)`-Weyl closure. Paper 14 may use this as boundary-curvature input by
citing the receipt and preserving the measured-calibration boundary.

## Conclusion

Paper 13 closes a real algebraic layer: shell-2 chart states, trace-2
idempotents, `S_3` transport, exact rational `SU(3)` closure, and bounded
exceptional-route classification. That is the CQECMPLX quark-face
color-transport physics map. The remaining work is measured Standard-Model
calibration, not the internal color-transport proof.

## Rework Integration Notes

- Keep the claim-strength tags attached to each theorem or bridge.
- Import companion variant language only when it strengthens exposition without
  promoting an open bridge.
- Treat every obligation row as a routed next-need: verifier, witness, adapter,
  calibration, documentation pass, or explicit guard.
- If a CAM/GLM row proposes `partially_closed`, update the paper body and
  obligation audit together; do not silently mark it closed.
## Upward Rework Intake

Downstream obligations now spring back through this paper. Rework this paper's definitions, receipts, guards, and claim-strength language before carrying the lane upward.

### Reasoned Claim Pressure

- Receipt-closed items may strengthen replayability and audit language, but they do not close unrelated transport, physical, or cold-start mathematical obligations.
- Partial CAM/GLM closures should be imported as bounded progress: name the verifier, state the portion advanced, and keep the residual claim visible.
- All physical or unit-bearing readings must pass through an external calibration gate before appearing as more than conditional interface language.
- Rule 30 language must distinguish cached/enumerated readout from cold closed-form extraction.
- Transport, exceptional algebra, lattice, and Moonshine routes must be graded by witness status instead of narrated as completed bridges.
- Engineering and adapter gaps should be promoted to work items, not used as theorem premises.
- Guard obligations must appear next to the claims they constrain, so the reader cannot miss the boundary.

### Intake Category Counts

| Category | Count |
|----------|------:|
| `external_calibration` | 23 |
| `open_next_need` | 15 |
| `claim_guard` | 9 |
| `engineering_gap` | 6 |
| `partial_closure` | 4 |
| `exceptional_lift` | 3 |
| `receipt_integrity` | 3 |
| `closed_receipt` | 1 |
| `rule30_boundary` | 1 |
| `transport_scope` | 1 |

### Routed Lanes

| Source | Obligation | Full lane | Required local action |
|--------|------------|-----------|-----------------------|
| `14` | `14.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `14` | `14.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `14` | `14.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14` | Separate enumerated/readout architecture from cold-start Rule 30 closure; never phrase cached or accumulated access as a solved cold extractor. |
| `15` | `15.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15` | Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named. |
| `15` | `15.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `16` | `16.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `16` | `16.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16` | Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named. |
| `16` | `16.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `17` | `17.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17` | Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named. |
| `17` | `17.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17` | Keep exceptional-lattice and Moonshine language as a structured lift unless the specific construction, table, or identification is present. |
| `17` | `17.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `18` | `18.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18` | Promote only the bounded or verifier-backed portion; leave the unbounded claim as an explicit obligation with the verifier named. |
| `18` | `18.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18` | Keep exceptional-lattice and Moonshine language as a structured lift unless the specific construction, table, or identification is present. |
| `18` | `18.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18` | Downgrade route language to demonstrated, bounded, registered, or open according to its witness surface. |
| `19` | `19.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19` | Strengthen receipt/path language and ensure any downstream theorem depends on replayable receipts rather than assumed file layout. |
| `19` | `19.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `19` | `19.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `20` | `20.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `20` | `20.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `20` | `20.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20` | Strengthen receipt/path language and ensure any downstream theorem depends on replayable receipts rather than assumed file layout. |
| `21` | `21.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21` | Keep exceptional-lattice and Moonshine language as a structured lift unless the specific construction, table, or identification is present. |
| `21` | `21.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `21` | `21.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `21` | `21.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `22` | `22.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `22` | `22.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `22` | `22.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `22` | `22.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `23` | `23.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `23` | `23.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `23` | `23.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `23` | `23.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `23` | `23.5` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `24` | `24.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `24` | `24.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `24` | `24.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `24` | `24.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `25` | `25.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `25` | `25.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `25` | `25.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `25` | `25.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `26` | `26.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `26` | `26.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `26` | `26.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `26` | `26.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `27` | `27.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `27` | `27.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `27` | `27.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `27` | `27.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `28` | `28.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `28` | `28.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `28` | `28.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `28` | `28.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `28` | `28.5` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `29` | `29.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `29` | `29.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `30` | `30.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `30` | `30.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
| `30` | `30.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30` | Strengthen receipt/path language and ensure any downstream theorem depends on replayable receipts rather than assumed file layout. |
| `31` | `31.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `31` | `31.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31` | Treat the item as closed evidence, but only at the receipt layer; do not let the closure silently upgrade neighboring mathematical claims. |
| `31` | `31.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31` | Rewrite surrounding prose so the guard is visible at the point where a reader might otherwise infer a stronger claim. |
| `32` | `32.1` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `32` | `32.2` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `32` | `32.3` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `32` | `32.4` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |
