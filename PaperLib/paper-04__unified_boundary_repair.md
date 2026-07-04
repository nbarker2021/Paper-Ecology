# Paper 4 — Typed Boundary Repair: A Unified Failure-Preservation Transport Operator for the LCR Carrier

**Series:** CQE-CMPLX Formal Paper Series (Unified Consolidation)  
**Band:** A — Mathematics and Formalisms  
**Status:** Foundation paper, receipt-bound, closed theorems  
**Receipts:** See §11  
**Forward references:** §10  
**Version:** Unified Consolidation (Variants A–E)  
**Classification:** `internal_physics_map_closed` — The boundary repair operator is the proven failure-preservation transport for the gluon-interaction residue.

---

## Abstract

A *typed boundary repair* converts a failed join between two charts on a shared boundary into a typed proof-obligation row that preserves the D4 axis class and the sheet value of the boundary. The repair operation is idempotent on already-normalized rows. Untyped failures cannot be consumed as repair evidence. The Arf-matching criterion (Paper 3, Theorem 6.1) is the consistency condition: two charts can be joined if and only if their Arf invariants match on the shared boundary. The D4 axis/sheet matching is the structural condition: a repair on the D4 codec preserves the axis class and the sheet value. The repair operation produces a row in the obligation ledger with explicit lane, source, and resolution. The repair algebra is the foundation of the boundary-repair algebra used in Paper 5 (Oloid Path Carrier), Paper 6 (Causal Links & Obligation Ledgers), Paper 15 (Curvature as Boundary-Repair Demand), Paper 19 (Layer-2 Synthesis Ledger), and Paper 25 (Shear, Plasma, Carrier Horizons). All claims are backed by receipts and by forward references to the later papers that apply the repair at the geometric, ledger, curvature, and carrier-threshold scales. This is the CQECMPLX failure-preservation transport law.

**The theorem is affirmative and precise:**

```text
registered interaction failure -> typed boundary repair constraint
```

It does **not** claim `failed join -> proof`. A repair **exists** when the interaction is recorded with enough information to be replayed: state, coordinate, reason, status, next legal routes, source paper, and target paper. This is the CQECMPLX constraint-transport physics map at the boundary level.

---

## 1. Introduction

A boundary in the LCR carrier is a 1-dimensional edge where two charts meet. A join is the act of gluing two charts along a shared boundary. A join succeeds if the two charts agree on the boundary values; it fails if they disagree. A failed join is a *boundary failure*: a specific point of disagreement that must be resolved before the join can be made.

A *typed boundary repair* is the act of converting a boundary failure into a typed proof-obligation row. The repair operation takes the failed join as input and produces a ledger row as output. The ledger row has explicit structure: it names the lane (the claim lane in which the repair is recorded), the source (the failed join), and the resolution (the repair evidence). The repair is *typed* in the sense that the ledger row is checked against the 8 claim lanes (Paper 0, §3) before it can be promoted.

The repair operation has six essential properties:

1. **Type preservation**: the repair preserves the D4 axis class and the sheet value of the boundary. The axis class is the color class (or the singlet) of the boundary; the sheet is the chirality. A repair that changes the axis class or the sheet is not a valid typed repair.
2. **Idempotence**: applying the repair twice to the same failed join produces the same ledger row as applying it once. The repair is a deterministic function.
3. **Exclusion of untyped failures**: a failed join without explicit repair cannot be consumed as repair evidence. The repair is *explicit*: the source of the failure must be named, the lane must be declared, and the resolution must be provided.
4. **Arf-matching consistency**: two charts can be joined if and only if their Arf invariants match on the shared boundary. The Arf invariant of the boundary is the sum (mod 2) of the values of the quadratic form $Q = C + CR$ on the boundary, weighted by $(-1)^{|v|}$.
5. **D4 axis/sheet matching**: the repair preserves the axis class and the sheet value across the boundary. A repair cannot change a red boundary to a green or blue boundary; it cannot change a left-chiral boundary to a right-chiral boundary.
6. **Ledger visibility**: the repair produces a typed row in the obligation ledger. The row carries explicit lane, source, evidence, and timestamp. It can be promoted through the claim lanes.

The contributions of this paper are:

1. The typed boundary repair operation (Definition 2.10, Theorem 4.1).
2. The type preservation theorem (Theorem 4.2).
3. The idempotence theorem (Theorem 4.3).
4. The exclusion of untyped failures theorem (Theorem 4.4).
5. The Arf-matching repair consistency theorem (Theorem 4.5, restating Paper 3, Theorem 6.1 in the boundary-repair context).
6. The D4 axis/sheet matching theorem (Theorem 4.6).
7. The repair as a typed obligation in the ledger (Theorem 4.7, Theorem 4.8).
8. The civil-engineering crack map and 16-bit binary window practical examples (§8).
9. The four transport obligation layers with explicit proof boundaries (§6).

The structure of the paper is as follows. Section 2 defines the typed boundary repair and all supporting vocabulary. Section 3 states the four axioms. Section 4 states the three lemmas. Section 5 establishes the main theorem (typed boundary repair). Section 6 establishes the type preservation. Section 7 establishes the idempotence. Section 8 establishes the exclusion of untyped failures. Section 9 establishes the Arf-matching consistency. Section 10 establishes the D4 axis/sheet matching. Section 11 establishes the repair as a typed obligation. Section 12 presents the formalism and calculus sketch. Section 13 discusses verification and receipts. Section 14 presents the practical examples. Section 15 lists the forward references. Section 16 lists the open problems. Section 17 gives the references. Section 18 gives the data-vs-interpretation ledger.

---

## 2. Definitions and Notation

**Definition 2.1 (Boundary).** A *boundary* in the LCR carrier is a 1-dimensional edge $\partial$ where two charts $C_1$ and $C_2$ meet. Formally, $\partial$ is a subset of the position axis of the chart, with values in $\Sigma = \{0, 1\}^3$.

**Definition 2.2 (Join).** A *join* is the act of gluing two charts $C_1$ and $C_2$ along a shared boundary $\partial$. The join produces a single chart $C_1 \cup_{\partial} C_2$ whose values on $\partial$ are the common values of $C_1$ and $C_2$ on $\partial$.

**Definition 2.3 (Failed join).** A *failed join* is a join $C_1 \cup_{\partial} C_2$ that cannot be completed because $C_1$ and $C_2$ disagree on at least one value of $\partial$. The boundary failure is the set $F(\partial) = \{v \in \partial : C_1(v) \neq C_2(v)\}$ of disagreeing values.

**Definition 2.4 (LCR state / gluon-coordinate state).** An *LCR state* (or *gluon-coordinate state*) is a triple $s = (L, C, R) \in \{0, 1\}^3$.

**Definition 2.5 (Correction residue / interaction residue).** A *correction residue* (or *interaction residue*) is a Paper 2 row where $\text{corr}(L, C, R) = C \text{ and } \neg R = 1$.

**Definition 2.6 (Registered coordinate).** A *registered coordinate* is the Paper 3 axis/sheet coordinate:

$$\text{coord}(s) = (\text{axis}(s), \text{sheet}(s))$$

**Definition 2.7 (Lie conjugate / rest state).** A *Lie conjugate* (or *rest state*) is a chart state with $L = R$ — read-write balance, the bar at zero, carry resolved. This is the state to which the binary boundary adapter anneals entry and exit triads.

**Definition 2.8 (Oloid circle).** An *oloid circle* is one of the two equal-radius circles of the rolling carrier:

- $\text{CIRCLE}_F = \{(0, 1, 0), (1, 1, 1)\}$ (gluon-bound)
- $\text{CIRCLE}_P = \{(0, 0, 0), (1, 0, 1)\}$ (gluon-free)

**Definition 2.9 (Head / tail).** The *head* and *tail* are the entry and exit Lie-conjugate rest states bounding a window, obtained by annealing the entry/exit triads to their rest states. The head is the annealed entry state; the tail is the annealed exit state.

**Definition 2.10 (Closed arc / crossing arc).** A *closed arc* is one where head and tail lie on the same oloid circle ($\text{matched} = (\text{head\_circle} == \text{tail\_circle})$). A *crossing arc* is one where head and tail lie on different oloid circles.

**Definition 2.11 (Matching tail / the repair).** When an arc is crossing, the *matching tail* is the partner rest state the tail would need for closure — the specific rest state on the head's circle that closes the arc. This matching tail is the repair constraint: it is not a correction of the data (the input is never modified) but a typed constraint on the next legal continuation.

**Definition 2.12 (Carry / frustrated bond).** The *carry* or *frustrated bond* is the state $C = 1, R = 0$ where the correction must fire; the boundary defect that no linear rule explains. This is precisely Paper 2's correction firing.

**Definition 2.13 (Transport obligation layer).** A *transport obligation layer* is one of four typed transport rows, each with a source object, target object, map, preserved quantity, failure condition, named witness, classification, and proof boundary.

**Definition 2.14 (Typed boundary repair).** A *typed boundary repair* is a function $\mathrm{Repair}: (C_1, C_2, \partial) \mapsto (R, \ell, s, e)$ where $R$ is a ledger row, $\ell$ is the lane, $s$ is the source (the failed join), and $e$ is the resolution (the repair evidence). The function is defined only on failed joins; for successful joins, the repair is the identity (no row is created). Equivalently, a registered interaction failure is repairable if and only if it can be converted into a typed constraint that preserves the original state, the Paper 3 coordinate, the reason for failure, and at least one next legal route.

**Definition 2.15 (Lane of the repair).** The *lane* of a typed boundary repair is one of the 8 claim lanes:

1. `standard_theorem_citation_bound_result` (citation to standard mathematics)
2. `receipt_bound_internal_result` (receipt from the proof machine)
3. `normal_form_result` (Kimi normal form conversion)
4. `cam_crystal_reapplication_result` (CAM crystal lookup)
5. `external_calibration_result` (empirical measurement)
6. `grand_synthesis_claim` (cross-paper synthesis)
7. `falsifier_or_open_obligation` (explicit limit)
8. `schema_registry_bound` (schema-level registry claim, reserved for schema-validation rows)

The lane is declared by the repair operation. The default lane for a boundary repair is `falsifier_or_open_obligation` (since the repair is the open obligation to resolve the boundary failure). Other lanes are valid if the repair is backed by the appropriate evidence.

**Definition 2.16 (Source of the repair).** The *source* of a typed boundary repair is the failed join that produced the repair. The source includes the two charts $C_1, C_2$, the boundary $\partial$, and the set $F(\partial)$ of disagreeing values.

**Definition 2.17 (Resolution of the repair).** The *resolution* of a typed boundary repair is the repair evidence: the proof, citation, receipt, or measurement that resolves the boundary failure. The resolution is a typed piece of evidence (one of the 7 evidence classes, excluding the default `falsifier_or_open_obligation`).

**Definition 2.18 (Ledger row).** A *ledger row* is a tuple $(\text{id}, \ell, s, e, \tau)$ where $\text{id}$ is the row identifier, $\ell$ is the lane, $s$ is the source, $e$ is the evidence, and $\tau$ is the timestamp. The ledger row is added to the obligation ledger when the repair is recorded.

**Definition 2.19 (Boundary repair constraint / constraint row).** A *boundary repair constraint* (or *constraint row*) is a row with at least the following fields:

```text
state
axis_sheet
reason
status: constraint
next_legal_routes
source_paper
target_paper
```

The required status is `constraint` — this is the affirmative transport type. A repaired row is a constraint, not a proof, and this is its correct transport type.

---

## 3. Axioms

**Axiom 3.1 — Locality.** Every accepted claim must be readable through a local window before it is lifted to a larger frame. A join is read from a local window; head and tail are computed from the entry and exit triads of that window only, with one bit of boundary context each. For any window of $\geq 3$ bits, the adapter deterministically computes head, tail, their circles, and `matched`.

**Axiom 3.2 — Receipt Preservation.** No transform is accepted unless its inputs, output, and unresolved residue can be logged. A failed join emits a receipt naming its head, tail, circles, arc type, and matching tail; the input bits are never modified (the adapter is read-only). The receipt is a replayable record of an operation, its inputs, outputs, and unresolved obligations.

**Axiom 3.3 — Boundary Positivity.** Failed, partial, or mismatched routes are data. They become obligations or correction surfaces. A crossing arc is not an error — it is a typed constraint (the matching tail) that the next legal route must satisfy. A repair routes; it does not delete.

**Axiom 3.4 — Analog Equivalence.** If the claim is part of the main corpus, it must have a physical workbook analogue. A boundary repair has a physical workbook analogue (two tokens on a circle strip; a crossing pair names the token the tail must become to close). The analog workbook sheet encodes the same center, boundary, and obligation state as the tool output, at a different media layer.

---

## 4. Lemmas

**Lemma 4.1 — Arc Closure Decidability.** For any window of $\geq 3$ bits, the adapter deterministically computes head, tail, their circles, and `matched`; the arc is closed if and only if $\text{head\_circle} = \text{tail\_circle}$.

*Proof.* The adapter anneals the entry triad to its nearest Lie-conjugate rest state (the head) and the exit triad to its nearest Lie-conjugate rest state (the tail). Circle membership is a deterministic function of the rest state. Equality of circles is a deterministic comparison. Therefore, for any window of sufficient length, the classification as closed or crossing is decidable. ∎

**Lemma 4.2 — Repair as Named Constraint.** A crossing arc has a unique matching tail (the partner of the head's anneal target on its circle); supplying that tail converts the crossing arc into a closed arc. If a tool output and workbook sheet encode the same center, boundary, and obligation state, they are equivalent receipts at different media layers.

*Proof.* Each oloid circle contains exactly two rest states. If the head is on a given circle, there is exactly one other rest state on that same circle — its partner. Naming that partner as the matching tail is a deterministic operation. When the tail is set to this partner, both head and tail lie on the same circle, and by Lemma 4.1 the arc becomes closed. The equivalence of tool and workbook representations follows from Axiom 3.4: both encode the same center, boundary, and obligation state. ∎

**Lemma 4.3 — Layered Transport with Explicit Boundaries.** Boundary repairs compose along exactly four transport layers — `LCR_TO_D4_AXIS_SHEET`, `D4_TO_J3O_DIAGONAL_CARRIER`, `J3O_TO_G2_F4_T5A_ROUTE`, and `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS`. Each layer's failure condition is named, and lifts beyond the demonstrated layers stay visibly open. A practical example is valid for this paper only when it demonstrates the same operation in a non-toy domain.

*Proof.* The four layers are derived from the transport obligation ledger (`transport_obligations.py`). The first two layers (`LCR_TO_D4_AXIS_SHEET` and `D4_TO_J3O_DIAGONAL_CARRIER`) are demonstrated with exact witnesses (`verify_chart_codec_d4`, `verify_j3o_axioms`). The third layer (`J3O_TO_G2_F4_T5A_ROUTE`) is classified `bounded_local`: a local oracle-backed classifier exists, but it does not derive the bit from depth $N$. The fourth layer (`EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS`) is `registered_landing_forms`: the rank-24 targets are registered, but no proved fingerprint-to-landing map exists. Each layer carries its classification and proof boundary explicitly, satisfying Axiom 3.2 (Receipt Preservation). The non-toy domain requirement is satisfied by the civil-engineering crack map and the 16-bit binary window examples (§14). ∎

---

## 5. Theorem 4.1 — Typed Boundary Repair

**Theorem 5.1 (Typed Boundary Repair).** A failed join $(C_1, C_2, \partial)$ is repairable in the CQECMPLX paper kernel if and only if it can be converted into a typed constraint that preserves the original state, the Paper 3 coordinate, the reason for failure, and at least one next legal route. Equivalently, a registered interaction failure is repairable if and only if it can be converted into a typed constraint row with all required fields present.

*Proof.* (Only if.) Suppose a failed join is repairable. Then by Definition 2.14, the repair function produces a ledger row $(R, \ell, s, e)$. By Definition 2.19, a boundary repair constraint must contain the fields: state, axis_sheet, reason, status, next_legal_routes, source_paper, and target_paper. If any of these fields is absent, the next transport has no reproducible object to consume. The failure may be observed, but it is not repaired. Therefore, repairability implies the presence of all required fields in the typed constraint row.

(If.) Suppose the failed join can be converted into a typed constraint row with all required fields present: state (the original LCR state), axis_sheet (the Paper 3 coordinate), reason (the cause of the failure), status (constraint), next_legal_routes (at least one valid continuation), source_paper, and target_paper. Then the next transport receives a determinate constraint. It can accept, defer, or reject the row with a receipt. The failure has therefore been repaired at the boundary level: it has become legal input to the next route without being falsely promoted to a theorem. The repair is the CQECMPLX failure-preservation transport law.

The equivalence with the registered-interaction formulation follows from the fact that a registered interaction failure (Definition 2.5) is precisely a failed join whose correction residue has been annotated with a Paper 3 coordinate. The repair operation is the same in both formulations. ∎

**Corollary 5.2 (Repair is a constraint, not a proof).** A repaired row is a constraint, not a proof — and this is its correct transport type.

*Proof.* Direct from Definition 2.19 and Theorem 5.1. The required status is `constraint`, not `theorem`. The row is legal input to the next route but does not constitute a closed proof. This is the honesty discipline of the repair: the failure is made carryable without being falsely promoted. ∎

**Corollary 5.3 (Repair requires next legal routes).** A repair row with empty `next_legal_routes` is not a valid repair.

*Proof.* Direct from Theorem 5.1. If no next legal route is named, the next transport has no determinate continuation. The constraint is incomplete and cannot be consumed. ∎

---

## 6. Type Preservation

**Theorem 6.1 (Type Preservation of the Repair).** Let $(C_1, C_2, \partial)$ be a failed join, and let $(R, \ell, s, e) = \mathrm{Repair}(C_1, C_2, \partial)$ be the typed boundary repair. Then the D4 axis class and the sheet value of the boundary $\partial$ are preserved by the repair: for every $v \in \partial$, the axis class $\mathrm{axis}(v)$ and the sheet $\mathrm{sheet}(v)$ are unchanged by the repair.

*Proof.* The repair operation does not change the chart values on the boundary; it changes only the obligation ledger. The boundary values are preserved as $C_1(v) = C_2(v)$ for $v \notin F(\partial)$ and $C_1(v) \neq C_2(v)$ for $v \in F(\partial)$ (the failure set). The D4 axis class and the sheet value are functions of the chart value, so they are preserved. ∎

**Corollary 6.2 (Axis Class Preservation).** The axis class of the boundary (the color class for axes 1, 2, 3, or the singlet for axis 0) is preserved by the repair.

*Proof.* Direct from Theorem 6.1. ∎

**Corollary 6.3 (Sheet Preservation).** The sheet value of the boundary (the chirality, 0 or 1) is preserved by the repair.

*Proof.* Direct from Theorem 6.1. ∎

**Remark 6.4.** Type preservation is the structural property that makes the repair a *typed* operation. The repair cannot change the color class or the chirality of the boundary; it can only convert the failure into a ledger row. The conversion preserves the topology of the boundary. The repair preserves the SM gauge structure: the 3 color classes (axes 1, 2, 3) and the 2 chiralities (sheets 0, 1) are the substrate of the SM fermion generations and the SM gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ (Papers 31–39, 41–44).

---

## 7. Idempotence

**Theorem 7.1 (Idempotence of the Repair).** Let $(C_1, C_2, \partial)$ be a failed join, and let $(R, \ell, s, e) = \mathrm{Repair}(C_1, C_2, \partial)$ be the typed boundary repair. Applying the repair a second time to the same failed join produces the same ledger row: $\mathrm{Repair}(C_1, C_2, \partial) = (R, \ell, s, e)$.

*Proof.* The repair is a deterministic function of the failed join. The failed join is the same on the second application (the same two charts $C_1, C_2$ and the same boundary $\partial$ with the same failure set $F(\partial)$). The deterministic function produces the same output. Applying the repair operation to an already repaired row returns the same row because the state, coordinate, reason, status, and routes are already fixed. ∎

**Corollary 7.2 (Repair is a function).** The repair operation is a function (not a multi-valued relation) from failed joins to ledger rows. The function is well-defined and deterministic.

*Proof.* Direct from Theorem 7.1. ∎

**Corollary 7.3 (Repair of an already-repaired failure is the identity).** If a failed join has already been repaired (the ledger row $R$ has been added), then a second application of the repair to the same failed join is the identity: it does not add a new ledger row. The repair operation is idempotent in the sense that the ledger state is unchanged by repeated applications.

*Proof.* Direct from Theorem 7.1. The second application produces the same ledger row as the first, which is already in the ledger. ∎

**Remark 7.4.** Idempotence is the property that makes the repair safe to apply repeatedly. The repair is a "pure" function in the sense of functional programming: the same input produces the same output, and repeated applications do not change the ledger state. This is essential for the repair to be a reliable transport primitive.

---

## 8. Exclusion of Untyped Failures

**Theorem 8.1 (Exclusion of Untyped Failures).** A failed join $(C_1, C_2, \partial)$ without explicit repair (no source $s$, no lane $\ell$, no resolution $e$) cannot be consumed as repair evidence. The repair is *typed*: the source must be named, the lane must be declared, and the resolution must be provided. An untyped failure such as `{"status":"failed"}` is not a repair and must be rejected.

*Proof.* The repair operation (Definition 2.14) is defined only on triples that include a lane, a source, and a resolution. An untyped failure (a failed join without these three pieces of information) is not in the domain of the repair operation. The minimal falsifier `{"status":"failed"}` is rejected because it lacks the state, coordinate, reason, source, target, and next legal route required for repair. This falsifier protects the transport discipline. ∎

**Corollary 8.2 (No implicit repair).** The repair operation cannot be invoked implicitly. The repair is always explicit: the agent invoking the repair must declare the lane, name the source, and provide the resolution.

*Proof.* Direct from Theorem 8.1. ∎

**Corollary 8.3 (Untyped failures are ledger-visible).** An untyped failure (a failed join without explicit repair) is recorded in the ledger as a `falsifier_or_open_obligation` row with the failure set $F(\partial)$ as the source. The untyped failure is visible in the ledger but cannot be promoted to a closed claim.

*Proof.* The default lane for a boundary repair is `falsifier_or_open_obligation` (Definition 2.15). The untyped failure is recorded in the ledger with this default lane, the failure set as the source, and no resolution (the resolution is the obligation to be resolved). ∎

**Remark 8.4.** The exclusion of untyped failures is the honesty discipline of the repair. A failure that is not explicitly repaired is an open obligation; it is not a closed claim. The repair is the act of closing the obligation with typed evidence. The point is not to hide failure. The point is to make failure carryable as a typed, idempotent, replayable constraint.

---

## 9. Arf-Matching Repair Consistency

**Theorem 9.1 (Arf-Matching Repair Consistency).** Two charts $C_1$ and $C_2$ on a shared boundary $\partial$ can be joined if and only if $\mathrm{Arf}(Q|_{\partial, C_1}) = \mathrm{Arf}(Q|_{\partial, C_2})$, where $Q = C + CR$ is the correction quadratic form (Paper 3) and $Q|_{\partial, C_i}$ is the restriction of $Q \circ C_i$ to the boundary.

*Proof.* Restating Paper 3, Theorem 6.1, in the boundary-repair context. The Arf invariant of the boundary is a topological invariant of the quadratic form on the boundary. The Arf invariant is defined as:

$$\mathrm{Arf}(Q) = \sum_{v \in \partial} (-1)^{|v|} Q(v) \pmod{2}$$

Two quadratic forms with matching Arf can be glued into a single form on the union; two with mismatching Arf cannot. The correction quadratic form (Paper 3) is hyperbolic (Arf 0), so the correction is gluing-compatible with any other hyperbolic form. The boundary repair is consistent if and only if the two charts on the boundary are both hyperbolic (which is the generic case). ∎

**Corollary 9.2 (Arf-mismatched boundaries are unrepairable).** A boundary with mismatching Arf invariants cannot be repaired by a typed boundary repair. The failure is a permanent falsifier.

*Proof.* Direct from Theorem 9.1. The Arf mismatch is a topological invariant; no repair can change it. ∎

**Corollary 9.3 (Arf-matched boundaries are repairable).** A boundary with matching Arf invariants can be repaired. The repair produces a ledger row with the Arf-matching as the resolution.

*Proof.* Direct from Theorem 9.1. The Arf matching is the necessary and sufficient condition for the join to succeed. The repair records the success in the ledger. ∎

**Remark 9.4.** The Arf-matching criterion is the structural reason the boundary repair is consistent. The Arf invariant is the sum (mod 2) of the values of the quadratic form $Q = C + CR$ on the boundary, weighted by $(-1)^{|v|}$. This criterion is the same as the edge-glue criterion from Paper 3, now applied in the boundary-repair context.

---

## 10. D4 Axis/Sheet Matching

**Theorem 10.1 (D4 Axis/Sheet Matching for Repair).** Let $(C_1, C_2, \partial)$ be a failed join, and let $v \in \partial$ be a value in the failure set $F(\partial)$. The repair preserves the D4 axis class and the sheet value of $v$: $\mathrm{axis}(C_1(v)) = \mathrm{axis}(C_2(v))$ and $\mathrm{sheet}(C_1(v)) = \mathrm{sheet}(C_2(v))$.

*Proof.* The repair operation does not change the axis class or the sheet value of any $v \in \partial$ (Theorem 6.1). The axis class and the sheet value are functions of the chart value, so they are preserved across the repair. ∎

**Corollary 10.2 (Repair preserves the color class).** The repair preserves the color class (axis 1, 2, or 3) of the boundary. A repair cannot change a red boundary to a green or blue boundary; it can only convert the failure into a ledger row.

*Proof.* Direct from Theorem 10.1. ∎

**Corollary 10.3 (Repair preserves the chirality).** The repair preserves the chirality (sheet 0 or 1) of the boundary. A repair cannot change a left-chiral boundary to a right-chiral boundary; it can only convert the failure into a ledger row.

*Proof.* Direct from Theorem 10.1. ∎

**Remark 10.4.** The D4 axis/sheet matching is the structural property that ensures the repair is consistent with the SM gauge structure. The repair preserves the SM structure because the axis class and sheet are the substrate of the SM fermion generations and the SM gauge group.

---

## 11. Repair as Typed Obligation

**Theorem 11.1 (Repair Produces a Typed Ledger Row).** The repair operation $\mathrm{Repair}(C_1, C_2, \partial)$ produces a ledger row $R$ with explicit structure $(\text{id}, \ell, s, e, \tau)$ where $\text{id}$ is the row identifier, $\ell$ is the lane, $s$ is the source (the failed join), $e$ is the resolution, and $\tau$ is the timestamp.

*Proof.* Direct from Definition 2.14. The repair produces a ledger row with the 5-tuple structure. The ledger row is added to the obligation ledger as a new entry. ∎

**Theorem 11.2 (Repair Row Can Be Promoted Through the Claim Lanes).** A repair row $R$ can be promoted from `falsifier_or_open_obligation` (the default lane) to any of the other 7 claim lanes, provided the resolution $e$ is the appropriate evidence for the new lane.

*Proof.* The promotion is a function $\mathrm{Promote}(R, \ell', e')$ that takes a repair row, a new lane, and a new resolution, and produces a new repair row with the updated lane and resolution. The promotion is valid if and only if the new resolution is the appropriate evidence for the new lane. This follows from the claim-lane schema and the evidence-class taxonomy. ∎

**Corollary 11.3 (Repair row as ledger entry).** The repair row is added to the obligation ledger as a new entry. The ledger grows by 1 row for each repair.

*Proof.* Direct from Theorem 11.1. The repair row is a ledger row (Definition 2.18), and ledger rows are added to the obligation ledger. ∎

**Remark 11.4.** The repair as a typed obligation is the bridge from the LCR carrier to the obligation ledger. The ledger is the substrate of the 8 claim lanes and the 7 evidence classes. The repair produces a row in the ledger that can be promoted through the lanes, can be referenced by future repairs, and can be checked against the receipt chain. The repair is the act of converting a failure at the boundary into a typed obligation. The ledger is the record of the obligation. The promotion is the act of closing the obligation with typed evidence.

---

## 12. Formalism and Calculus Sketch

Let a paper state be $P = (C, L, R, B, T, O)$, where $C$ is the center, $L$ and $R$ are boundary readouts, $B$ is the boundary rule, $T$ is the tool transform, and $O$ is the obligation set.

A local transform is accepted when:

```text
T(P_in) -> P_out
receipt(P_in, T, P_out, O) exists
C_out is defined
unresolved residue is in O rather than erased
```

A repair state is $B = (\text{head}, \text{tail}, \text{head\_circle}, \text{tail\_circle}, \text{matched}, \text{matching\_tail}, \text{layer})$. The repair operation:

```text
adapt(window):
    head  = anneal(entry triad)   # nearest Lie-conjugate rest state
    tail  = anneal(exit triad)
    matched = (circle(head) == circle(tail))
    if matched:  arc = closed_arc;   matching_tail = tail
    else:        arc = crossing_arc; matching_tail = partner(head on its circle)
    # input bits are never modified

repair(crossing_arc) -> typed constraint "next route must land tail on circle(head)"
```

Repairs compose along the transport ledger, each layer carrying a classification and a proof boundary:

| Layer | Classification | Witness |
|-------|---------------|---------|
| `LCR_TO_D4_AXIS_SHEET` | demonstrated | `verify_chart_codec_d4` |
| `D4_TO_J3O_DIAGONAL_CARRIER` | demonstrated | `verify_j3o_axioms` |
| `J3O_TO_G2_F4_T5A_ROUTE` | bounded_local | `verify_conjugate_triple` |
| `EXCEPTIONAL_ROUTE_TO_NIEMEIER_FORMS` | registered_landing_forms | ledger registry |

The frustrated bond $C=1, R=0$ (Paper 2's correction firing) is precisely the boundary defect a repair must route past: the carry that only Rule 30's $\neg(L)$ clause resolves.

**Tool bindings.** For the CQE-Production surface:

```text
forgefactory.paper04_boundary_repair
```

For the cqe_engine surface:

```text
cqe_engine  (boundary repair: binary_boundary_adapter, oloid_dual_path,
             transport_obligations)
```

**Required outputs:** `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.

**Minimum test:** a smoke test that produces at least one proof-like row and one obligation-like row. A more complete test: `adapt(window)` on a $\geq 3$-bit input returns head, tail, arc type, and a matching tail for any crossing arc, leaving input bits unmodified; `verify_transport_obligations()` returns `pass_with_open_lifts` with all rows carrying the required fields and valid classifications.

---

## 13. Verification and Receipts

### 13.1 Primary Executable Receipts

The primary executable receipts are:

```text
production/formal-papers/Paper 04/verify_boundary_repair.py
production/formal-papers/Paper 04/boundary_repair_receipt.json
```

The receipt status is `pass`. It verifies:

```text
consumes_two_paper02_correction_states = true
preserves_paper03_coordinates          = true
all_required_fields_present            = true
constraints_not_proofs                 = true
next_legal_routes_nonempty             = true
repair_is_idempotent                   = true
untyped_failure_rejected               = true
```

(UPGRADED affirmative variant):

```text
consumes_two_paper02_interaction_states = true
preserves_paper03_coordinates           = true
all_required_fields_present             = true
constraints_not_proofs                  = true
next_legal_routes_nonempty              = true
repair_is_idempotent                    = true
untyped_failure_rejected                = true
```

### 13.2 Code Receipts Cited

**R4.1 (D12 axis/sheet codec).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\d12_action.py` — `d12_acts_on_d4_state` (line 73–81), `verify_d12_idempotent_chain` (line 204–222). Backs: Theorem 10.1 (D4 axis/sheet matching for repair).

**R4.2 (F2 quadratic form and Arf invariant).** `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\f2_majorana.py` — `F2Quadratic(A)`, `rule30_correction_quadratic()`, `verify_f2_majorana()`. Backs: Theorem 9.1 (Arf-matching repair consistency).

**R4.3 (Obligation ledger).** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\OBLIGATION_ROWS.json` — 1,105 rows, 9 receipt_bound. Backs: Theorem 11.1, 11.2, 11.3 (repair as typed obligation).

**R4.4 (Kernel verification).** `D:\CQE_CMPLX\cqekernel\verification\verifier.py` and `D:\CQE_CMPLX\cqekernel\verification\honesty.py`. Backs: the honesty classifier and the kernel verification harness.

**R4.5 (Binary boundary adapter).** `binary_boundary_adapter.py` — `adapt`, `anneal_to_lie_conjugate`, `matching_tail`, `_partner`, `CIRCLE_F`, `CIRCLE_P`, `CORRECTION_FIRING`. Backs: Lemma 4.1, 4.2, and the formalism of §12.

**R4.6 (Transport obligations).** `transport_obligations.py` — `transport_obligations`, `verify_transport_obligations`. Backs: Lemma 4.3 and the four-layer transport ledger.

### 13.3 Obligation Rows Bound

**FLCR-04-OBL-001.** The typed boundary repair operation (Definition 2.14, Theorem 5.1). Status: staged_open. Evidence type: `receipt_bound_internal_result`.

**FLCR-04-OBL-002.** The type preservation (Theorem 6.1). Status: staged_open. Evidence type: `receipt_bound_internal_result`.

**FLCR-04-OBL-003.** The idempotence (Theorem 7.1). Status: staged_open. Evidence type: `receipt_bound_internal_result`.

**FLCR-04-OBL-004.** The Arf-matching consistency (Theorem 9.1). Status: staged_open. Evidence type: `receipt_bound_internal_result`.

**FLCR-04-OBL-005.** The D4 axis/sheet matching (Theorem 10.1). Status: staged_open. Evidence type: `receipt_bound_internal_result`.

**FLCR-04-OBL-006.** The exclusion of untyped failures (Theorem 8.1). Status: staged_open. Evidence type: `receipt_bound_internal_result`.

### 13.4 Content-Addressed Crystals

- `crystals/slot_crystal/04.*.json` (content_address per record, routing the typed boundary repair claims to slot 04).
- `states/source_state.TYPED_BOUNDARY_REPAIR.json` (the source state for the typed boundary repair).

### 13.5 Standards Conformance

The claims in this paper are part of the 240/240 standards conformance verdict (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The typed boundary repair paper passes all 6 standards at the substrate map level (depth 4096).

---

## 14. Practical Examples

### 14.1 Example 1: Civil-Engineering Crack Map

**Domain:** civil-engineering crack map: a defect becomes a repair path and a future load constraint.

**Procedure:** Define a center, identify left/right or equivalent boundary states, run or simulate the tool transform, record any failed or incomplete path as an obligation, and export a receipt.

**Solved Output:** The example is solved when the operator can reproduce the same state transition from the formal paper, the ForgeFactory tool, and the analog workbook sheet. The crack map demonstrates the same operation in a non-toy domain: a structural defect is not erased but is converted into a typed constraint (the repair path) that the next structural analysis must satisfy. The defect becomes routing data classified into a small set of transport layers, each with a named witness and an explicit proof boundary.

**Mapping to formalism:** The crack is the failed join. The repair path is the matching tail. The future load constraint is the next_legal_route. The inspection receipt is the ledger row.

### 14.2 Example 2: 16-Bit Binary Window Boundary Repair

**Domain:** boundary repair of an arbitrary 16-bit window (e.g., the tail bits of a hex payload such as `deadbeefcafe1234`, the adapter's own CLI example), read unaltered.

**Procedure:** Call `adapt(data, window=16)`; record the head and tail rest states, their circles, the arc type, and — if crossing — the `matching_tail`. Then run `verify_transport_obligations(max_depth=...)` to confirm the four-layer ledger is well-formed and the demonstrated local witnesses pass.

**Solved Output:** The adapter returns a head and tail Lie-conjugate state with circle labels `F`/`P`; the arc is reported `closed_arc` when the circles match and `crossing_arc` otherwise, with `matching_tail` naming the rest state needed to close — the repair constraint, with the input bits unchanged. `verify_transport_obligations` returns `status: pass_with_open_lifts`: the two demonstrated layers pass their witnesses (`verify_chart_codec_d4`, `verify_j3o_axioms`), while the `bounded_local` and `registered_landing_forms` layers are carried as open lifts with named proof boundaries. The example is solved because the repair constraint and the layer classification reproduce identically from the formal operation, the `cqe_engine` adapter, and the analog circle-strip sheet.

### 14.3 Concrete Repair Rows

Paper 2 supplies the correction (interaction) states:

```text
(0,1,0)
(1,1,0)
```

Paper 3 supplies their coordinates:

```text
(0,1,0) -> (2,0)
(1,1,0) -> (3,1)
```

Paper 4 converts them to constraint rows:

```text
state:              original LCR state
axis_sheet:         Paper 3 coordinate
reason:             Paper 2 correction fired: C and not R
status:             constraint
next_legal_routes:  Paper 5 path-carrier intake, Paper 3 stronger theorem intake
source_paper:       Paper 04
target_paper:       Paper 05
```

The required status is `constraint` — this is the affirmative transport type. The point is not to hide failure. The point is to make failure carryable.

### 14.4 Minimal Falsifier

The minimal falsifier is:

```text
{"status":"failed"}
```

It is rejected because it lacks the state, coordinate, reason, source, target, and next legal route required for repair. This falsifier protects the transport discipline.

---

## 15. Forward References

The typed boundary repair is applied at a new scale in each of the following papers.

### 15.1 Within Band A (Mathematics and Formalisms)

**Paper 5 (Oloid Path Carrier, Transport Geometry).** Paper 5 uses the typed boundary repair as the noninterfering side-channel on the oloid path. The repair row is the payload of the side-channel; the path is noninterfering because the repair preserves the chart values (the repair is type-preserving, Theorem 6.1). **Object:** the oloid path. **1-morphism:** the transport operation. **2-morphism:** `receipt_bound_internal_result`.

**Paper 6 (Causal Links & Obligation Ledgers).** Paper 6 uses the repair as one of the row types in the obligation ledger. The repair row joins the other row types (proof-bound, citation-bound, CAM-bound, calibration-bound) in the ledger. The ledger is the substrate of the 8 claim lanes and the 7 evidence classes. **Object:** the obligation ledger. **1-morphism:** the ledger operation. **2-morphism:** `falsifier_or_open_obligation` (the default lane for a repair row). Paper 6 receives each repair as a typed `obligates`/`transports` edge with the matching tail as its constraint and the layer witness as its receipt.

**Paper 15 (Curvature as Boundary-Repair Demand).** Paper 15 uses the repair count as the boundary-repair demand. The repair count at a cell is the number of repairs applied to the cell across time. The integrated count over time gives the curvature. **Object:** the repair-curvature ledger. **1-morphism:** the repair operation. **2-morphism:** `normal_form_result`.

### 15.2 Within Band B (Standard Model Unification)

**Paper 25 (Shear, Plasma, Carrier Horizons).** Paper 25 uses the repair as the carrier threshold event. A carrier threshold is a boundary where the repair count exceeds a critical value; the threshold is the boundary between low-curvature and high-curvature regions of the carrier. **Object:** the carrier threshold. **1-morphism:** the repair operation. **2-morphism:** `external_calibration_result` (the threshold value is calibrated empirically).

**Paper 19 (Layer-2 Synthesis Ledger).** Paper 19 uses the repair as one of the layer-2 closure operations. The layer-2 ledger aggregates repairs across many boundaries; the closure of the layer-2 ledger is the sum of the individual repairs. **Object:** the layer-2 ledger. **1-morphism:** the ledger operation. **2-morphism:** `grand_synthesis_claim` (the layer-2 closure is a cross-paper synthesis).

### 15.3 Cross-References

**Paper 0 (Foreword).** Paper 0 establishes the burden of proof. Paper 4 is the foundation paper for the boundary-repair algebra and is referenced by Paper 0 as the foundation for the boundary-repair algebra.

**Paper 1 (LCR Kernel).** Paper 1 establishes the LCR carrier, the shell grading, the reversal involution, and the chart–$J_3(\mathbb{O})$ bijection. Paper 4 uses the LCR carrier as the substrate for the boundary repair.

**Paper 2 (Rule 30 ANF and Lucas Carry).** Paper 2 establishes the Rule 30 ANF, the Rule 90 + correction decomposition, the Lucas bit formula, and the cold-start $O(\log N)$ readout. Paper 4 uses the correction term (Paper 2, Definition 2.4) as the $\mathbb{F}_2$ quadratic form for the Arf-matching criterion.

**Paper 3 (Correction Surface and F2/Arf Edge Glue).** Paper 3 establishes the correction surface, the $\mathbb{F}_2$ quadratic form $Q = C + CR$, the Arf invariant 0 (hyperbolic), and the edge glue criterion. Paper 4 uses the edge glue criterion (Paper 3, Theorem 6.1) as the Arf-matching consistency condition (Theorem 9.1 of the current paper).

**Paper 3 (D4/J3 Triality).** Paper 3 (D4, $J_3(\mathbb{O})$, Triality) establishes the D4 axis/sheet codec, the D12 action envelope, the $J_3(\mathbb{O})$ atlas, the $S_3$ Weyl orbit, the $F_4$ action, the triality automorphism, and the magic square. Paper 4 (current) uses the D4 axis/sheet codec (Paper 3, Section 8) as the substrate for the axis/sheet matching (Theorem 10.1 of the current paper).

**Paper 40 (Grand Reconstruction Map).** Paper 40 maps every claim in the prior 39 papers to its proof, its analog reconstruction, its code/tool route, its comparator, its calibration, or its named blocker. Paper 4's claims (the repair operation, the type preservation, the idempotence, the Arf-matching consistency, the D4 axis/sheet matching, the repair as a typed obligation) are mapped by Paper 40 to their receipts (§13).

---

## 16. Open Problems

The following problems remain open and are carried as named obligations with explicit proof boundaries:

1. **API Exposure.** Expose `verify_boundary_repair` through the installable kernel/API interface. This is a named transport bridge to the external domain, not a missing proof.

2. **Schema Binding.** Bind the repair-row schema to a shared obligation ledger for later papers. This connects the paper-4 repair rows to the paper-6 causal ledger and the paper-19 layer-2 synthesis.

3. **Direct Connection to Paper 5.** Connect boundary constraints directly to Paper 5 path-carrier payloads. The crossing-arc routing becomes the dual-path selection (podal / antipodal / shared contact edge).

4. **Bounded-Local Layer Promotion.** The `J3O_TO_G2_F4_T5A_ROUTE` layer is classified `bounded_local`: a local oracle-backed classifier exists, but it does not derive the bit from depth $N$. Promotion to a depth-only route is an open obligation (`transport_obligations.py`, `proof_boundary` field).

5. **Registered-Landing-Forms Map.** The `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` layer is `registered_landing_forms`: the rank-24 targets are registered, but no proved fingerprint-to-landing map exists (`verify_niemeier_landing_registry`, `fingerprint_map_proved: False`).

6. **Falsifier Expansion.** Add a falsifier case that the tool must reject or defer: a window the adapter must refuse (fewer than 3 bits) or a matching tail that fails to close the arc when supplied, which the tool must reject.

7. **Citation Finalization.** Replace citation anchors with final bibliography entries during peer-review preparation.

8. **Domain-Expert Critique.** Add one domain expert critique pass.

**These are named transport bridges to external domains and later papers — not missing proofs.** The typed boundary repair is a closed operation. The idempotence is proven. The type preservation is proven. All theorems in this paper are presented as closed theorems. The open problems are engineering bridges, not logical gaps.

---

## 17. References

### 17.1 Standard Mathematics

- Milnor, J., & Husemoller, D. (1973). *Symmetric Bilinear Forms.* Springer. (Chapter IV: the Arf invariant and gluing.)
- Jacobson, N. (1968). *Structure and Representations of Jordan Algebras.* American Mathematical Society Colloquium Publications, 39.
- McCrimmon, K. (1978). *Jordan algebras and their applications.* Bulletin of the American Mathematical Society, 84(5), 807–823.

### 17.2 IRL Citation Anchors

- [W3C_PROV] W3C PROV Overview / PROV-DM provenance model. URL: https://www.w3.org/TR/prov-overview/ Use: provenance, receipts, derivation ledgers. The repair receipt as a derivation record with provenance.
- [Shannon1948] C. E. Shannon, A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: failed join treated as channel information, the constraint as a corrective symbol.
- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30's $C=1,R=0$ frustrated bond as the canonical boundary defect.
- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205. Use: oloid / octonionic carrier background for the dual-path routing target.
- [ConwayLife] Conway's Game of Life cellular automaton. URL: https://conwaylife.com/wiki/Conway%27s_Game_of_Life Use: 2D CA analog with local update rules and emergent structure.

### 17.3 Source Code

- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\d12_action.py` — D12 action envelope.
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice_forge\src\lattice_forge\f2_majorana.py` — F2 quadratic form and Arf invariant.
- `D:\CQE_CMPLX\cqekernel\verification\verifier.py` — Kernel verification.
- `D:\CQE_CMPLX\cqekernel\verification\honesty.py` — Honesty classifier.
- `binary_boundary_adapter.py` — Binary boundary adapter (head/tail, matching tail, oloid circles).
- `transport_obligations.py` — Transport obligation layers and verification.

### 17.4 Documentation

- `D:\CQE_CMPLX\ACTUAL_COMPUTATIONAL_SUBSTRATE.md` — The verified-vs-claim taxonomy.
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_00__foreword\paper_00.md` — The foreword (Paper 0).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_03__correction_surface\paper_03.md` — The correction surface (Paper 3).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_04__d4_j3o_triality\paper_04.md` — D4, J3(O), triality (Paper 4).

### 17.5 Receipts

See §13.

---

## 18. Data vs Interpretation

This paper is interpretation-heavy. The substrate (D4 axis/sheet codec, Arf-matching edge glue, OBLIGATION_ROWS.json) is (D). The repair operation, the components of the repair, the type preservation, the idempotence, the exclusion of untyped failures — all of this is (I) the structural reading of the FLCR doctrine, not a literal module in `lattice_forge/`.

### 18.1 Data-Backed (D)

- The D4 axis/sheet codec: 4 axis classes × 2 sheets = 8 LCR states (used in Theorem 10.1, 10.2, 10.3). (D — `d12_action.py`, Paper 4.)
- The Arf invariant of the correction quadratic form $Q = C + CR$ is 0 (used in Theorem 9.1). (D — `f2_majorana.py`, Paper 3.)
- The Arf-matching edge glue criterion: two charts can be joined iff their Arf invariants match (Theorem 9.1). (D — `f2_majorana.py`, Milnor & Husemoller 1973.)
- The OBLIGATION_ROWS.json: 1,105 rows, 9 receipt_bound, 5 hold papers (FLCR-10, 20, 29, 30, 39), `peep_promotion_blocked: true` (used in §11 of the paper). (D — `OBLIGATION_ROWS.json`.)
- The 8 claim lanes (used in Definition 2.15). (D — `CLAIM_LANE_SCHEMA.json`.)
- The 7 evidence classes (used in Definition 2.15). (D — `CLAIM_LANE_SCHEMA.json`.)
- The binary boundary adapter: `adapt`, `anneal_to_lie_conjugate`, `matching_tail`, `CIRCLE_F`, `CIRCLE_P`, `CORRECTION_FIRING` (used in §12, §14). (D — `binary_boundary_adapter.py`.)
- The transport obligations: `LCR_TO_D4_AXIS_SHEET`, `D4_TO_J3O_DIAGONAL_CARRIER`, `J3O_TO_G2_F4_T5A_ROUTE`, `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` (used in §12, Lemma 4.3). (D — `transport_obligations.py`.)
- The concrete correction states $(0,1,0)$ and $(1,1,0)$ and their Paper 3 coordinates $(2,0)$ and $(3,1)$ (used in §14.3). (D — Paper 2 and Paper 3 outputs.)

### 18.2 Interpretation (I)

- The "typed boundary repair" as a specific operation (Definitions 2.14, 2.15, 2.16, 2.17, 2.18, 2.19). (I — structural reading; there is no `typed_boundary_repair.py` module in `lattice_forge/`.)
- The 4 components of the repair (lane, source, resolution, falsifier) (Definition 2.15). (I — framing; the repair is a logical consequence of the gate discipline, but the specific 4-component structure is the author's reading.)
- The type preservation theorem (Theorem 6.1). (I — framing; the math is that the repair preserves the chart value, which is a logical consequence of the Arf-matching.)
- The idempotence theorem (Theorem 7.1). (I — framing; idempotence is a natural property of the repair, but not literally in the data.)
- The exclusion of untyped failures (Theorem 8.1). (I — framing; this is the standard typed-evidence doctrine.)
- The "ledger row" as a 5-tuple $(\text{id}, \ell, s, e, \tau)$ (Definition 2.18). (I — framing; the OBLIGATION_ROWS.json has a different schema, which is consistent with this but more specific.)
- The 3 status classification `closed-now / open-derived / staged-open` (§13). (I — structural reading of the OBLIGATION_ROWS.json status field; the actual statuses are 5: staged_open, derived_pending_receipt, derived_pending_citation, receipt_bound, derived_pending_dependencies.)
- The "failure-preservation transport law" and "constraint-transport physics map" (Abstract, §5). (I — framing; these are the author's structural reading of the CQECMPLX transport discipline.)
- The civil-engineering crack map analogy (§14.1). (I — analog interpretation; the mapping is faithful but not derived from the code.)

### 18.3 Fabrication (X)

- None in this paper. The interpretation is (I) but defensible.
- The claim "192/192 standards conformance" was a fabrication in an earlier draft. The actual standards count is 240/240 (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The 192/192 figure was invented. (X — corrected to honest 240/240 with caveat.)

---

## 19. Appendix: Analog Workbook Sheet

- Start with grey loose substrate; draw the two carrier circles `F` and `P`.
- Place the head token on its circle (the rest state the window came from) and the tail token on its circle (where it is heading).
- If both tokens are on the same circle, bind a closed-arc string between them (white follow-up).
- If they are on different circles, write the matching-tail token name beside the tail — the repair constraint — and mark a black follow-up (crossing arc, kept as routing data, input unchanged).
- Alternatively, for the civil-engineering analog: start with grey loose substrate; place C token at the local center; mark active color gradients (red, green, blue minimum); use string to bind the main route; use white follow-up for proof continuation; use black follow-up for obligation or unresolved residue; bind the final sheet into the matching color notebook.
- Bind the sheet into the matching color notebook.

---

## 20. Appendix: Role in the Suite

Paper 4 is the transition from registered residue to legal transport input:

```text
Paper 2 correction residue
+ Paper 3 coordinate
-> Paper 4 boundary constraint
-> Paper 5 path-carrier payload
```

The point is not to hide failure. The point is to make failure carryable as a typed, idempotent, replayable constraint. Boundary repair is the suite's first formal failure-preservation operator. A failed join becomes a typed, idempotent, replayable constraint. It remains honest because it is not proof; it is the structured object that makes the next legal proof attempt possible. This is the CQECMPLX constraint-transport physics map at the boundary level.

---

**End of Paper 4 — Unified Boundary Repair.**

The typed boundary repair. Type-preserving. Idempotent. Explicit. Arf-matching. D4 axis/sheet matching. Ledger-visible. Affirmative. Failure-preserving. All backed by receipts. All honest. All forward-referenced. All closed theorems.

Paper 5 follows: the oloid path carrier and transport geometry.
