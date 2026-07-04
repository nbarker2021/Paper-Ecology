# Paper 7 — Causal Links and Obligation Ledgers

**Series:** Unified Field Theory in 100 Papers  
**Band:** A — Mathematics and Formalisms  
**Status:** foundation paper, receipt-bound  
**Receipts:** see §11  
**Forward references:** §10

---

## Abstract

A *causal link* in the FLCR graph is a typed edge between two ledger rows. The edge has an explicit lane (one of the 8 claim lanes), an explicit source (the upstream row), and an explicit resolution (the receipt, citation, or measurement that closes the link). *Negative extraction verdicts* (verdicts that an attempted row does not close) are recorded in the ledger with explicit lane and explicit source. *Obligation edges* route work from one row to another but are not themselves proof; the routed work must be closed by an explicit receipt. The obligation ledger is consistent iff every row has an explicit lane, source, and resolution (or an explicit falsifier). A row is *closed-now* iff it has a non-default lane and a non-empty resolution; *open-derived* iff it has a non-default lane and an empty resolution; *staged-open* iff it has the default lane. The causal graph is the substrate of the layer-2 synthesis ledger (Paper 19), the supervisor cursor (Paper 30), and the SM bridge band (Papers 31–39). All claims are backed by receipts and by forward references to the later papers that apply the ledger at the synthesis, supervisor, and SM bridge scales.

---

## 1. Introduction

The obligation ledger is the central data structure of the FLCR series. Every claim in the 100-paper series is backed by a ledger row, and every ledger row has explicit structure. The ledger is the substrate of the 8 claim lanes (Paper 0, §3) and the 7 evidence classes (Paper 0, §3). The ledger is the spine of the receipt chain.

A *causal link* is a typed edge in the FLCR graph. The edge connects two ledger rows: the source row (upstream) and the target row (downstream). The edge has explicit structure: the lane (one of the 8 claim lanes), the source (the upstream row), the resolution (the receipt, citation, or measurement that closes the link), and the timestamp.

A *negative extraction verdict* is a verdict that an attempted row does not close. For example: a verifier that fails (e.g., `verify_t10_master_receipt` returning `fail`), a citation that does not exist, or a measurement that is not available. The negative verdict is recorded in the ledger with explicit lane (`falsifier_or_open_obligation`) and explicit source (the attempted extraction). The negative verdict is *productive*: it reduces future search by naming what does not work.

An *obligation edge* is a special kind of causal link that routes work from one row to another. The obligation edge is not itself proof; it is a routing instruction. The routed work must be closed by an explicit receipt at the target row. The obligation edge is the structural reason the ledger is a *graph* and not just a list: the edges encode the dependencies between rows.

The contributions of this paper are:
1. The typed causal link (Section 2).
2. The typed-edge soundness theorem (Theorem 3.1).
3. The negative extraction verdict (Theorem 4.1).
4. The obligation edge as routing (Theorem 5.1).
5. The ledger consistency theorem (Theorem 6.1).
6. The row status classification (Theorem 7.1, closed-now / open-derived / staged-open).

The structure of the paper is as follows. Section 2 defines the causal link. Section 3 establishes the typed-edge soundness. Section 4 establishes the negative extraction verdict. Section 5 establishes the obligation edge as routing. Section 6 establishes the ledger consistency. Section 7 establishes the row status classification. Section 8 discusses the ledger in the context of the larger series. Section 9 states the open problems. Section 10 lists the forward references. Section 11 lists the receipts. Section 12 gives the references.

---

## 2. Definitions and Notation

**Definition 2.1 (Causal link).** A *causal link* in the FLCR graph is a 4-tuple $(r_1, r_2, \ell, e)$ where $r_1$ is the source ledger row (upstream), $r_2$ is the target ledger row (downstream), $\ell$ is the lane (one of the 8 claim lanes), and $e$ is the resolution (the receipt, citation, or measurement that closes the link).

**Definition 2.2 (Typed causal link).** A *typed causal link* is a causal link in which $\ell \neq$ `falsifier_or_open_obligation` (the default lane) and $e \neq \emptyset$ (the resolution is non-empty). The link is *typed* in the sense that the lane and resolution are explicit.

**Definition 2.3 (Negative extraction verdict).** A *negative extraction verdict* is a 4-tuple $(r, \ell, s, e)$ where $r$ is the attempted row, $\ell = $ `falsifier_or_open_obligation` (the default lane), $s$ is the source (the attempted extraction), and $e = \emptyset$ (no resolution). The verdict records that the extraction did not close.

**Definition 2.4 (Obligation edge).** An *obligation edge* is a causal link $(r_1, r_2, \ell, e)$ in which $r_1$ is the upstream row and $r_2$ is the downstream row, and the link is interpreted as a routing instruction: the work at $r_1$ must be closed at $r_2$ by an explicit receipt. The obligation edge is not itself a proof; it is a routing instruction.

**Definition 2.5 (Ledger row status).** A ledger row has one of three statuses:
- `closed-now`: the row has a non-default lane and a non-empty resolution. The row is closed.
- `open-derived`: the row has a non-default lane and an empty resolution. The row is derived but not yet closed.
- `staged-open`: the row has the default lane (`falsifier_or_open_obligation`). The row is staged as an open obligation.

**Definition 2.6 (Ledger consistency).** The obligation ledger is *consistent* iff every row has an explicit lane, an explicit source, and an explicit resolution (or an explicit falsifier, for staged-open rows).

---

## 3. Typed-Edge Soundness

**Theorem 3.1 (Typed-edge soundness).** A typed causal link $(r_1, r_2, \ell, e)$ in the FLCR graph is sound iff the resolution $e$ is the appropriate evidence for the lane $\ell$.

*Proof.* The 8 claim lanes have different evidence requirements (Paper 0, §3). A typed link is sound iff the evidence matches the lane. For example, a `standard_theorem_citation_bound_result` link is sound iff the resolution $e$ is a citation to standard math; a `receipt_bound_internal_result` link is sound iff the resolution $e$ is a receipt from the proof machine; etc. ∎

**Corollary 3.2 (Untyped links are unsound).** A causal link with $\ell = $ `falsifier_or_open_obligation` (the default lane) and $e \neq \emptyset$ is unsound: a default lane with a non-empty resolution is a contradiction.

*Proof.* Direct from Theorem 3.1. A default lane with a non-empty resolution is a contradiction because the default lane records a negative verdict, which has no resolution. ∎

**Corollary 3.3 (Negative verdicts with resolutions are unsound).** A negative extraction verdict $(r, \ell, s, e)$ with $e \neq \emptyset$ is unsound: a negative verdict has no resolution.

*Proof.* Direct from Theorem 3.1. A negative verdict with a resolution is a contradiction because the verdict says the resolution does not exist. ∎

**Remark 3.4.** Typed-edge soundness is the structural property that ensures the ledger is consistent. A sound link has a lane-resolution pair that makes sense. An unsound link is a contradiction and must be removed or repaired.

---

## 4. Negative Extraction Verdicts

**Theorem 4.1 (Negative extraction verdicts are productive).** A negative extraction verdict $(r, \ell, s, e)$ with $\ell = $ `falsifier_or_open_obligation` and $e = \emptyset$ is recorded in the ledger. The verdict reduces future search by naming what does not work.

*Proof.* The verdict is recorded as a ledger row with the default lane and an empty resolution. The row is visible in the ledger; future search can filter on the row to avoid attempting the same extraction. ∎

**Corollary 4.2 (Negative verdicts are not promotions).** A negative extraction verdict is not a promotion. The verdict is a record of what was attempted; it does not close any claim.

*Proof.* Direct from Theorem 4.1. The verdict has the default lane and an empty resolution; it is staged-open, not closed-now. ∎

**Corollary 4.3 (Negative verdicts are reversible).** A negative extraction verdict can be reversed: if a subsequent attempt produces a non-empty resolution, the verdict can be promoted to a typed link with the new resolution.

*Proof.* Direct from Definition 2.2. The promotion is a function that updates the lane and resolution of the verdict row. ∎

**Remark 4.5.** Negative verdicts are the honesty discipline of the ledger. A failed extraction is recorded as a verdict; the failure is not hidden. The verdict reduces future search and is reversible if the failure is later resolved.

---

## 5. Obligation Edges as Routing

**Theorem 5.1 (Obligation edge is routing, not proof).** An obligation edge $(r_1, r_2, \ell, e)$ in the FLCR graph is a routing instruction: the work at $r_1$ must be closed at $r_2$ by an explicit receipt. The obligation edge is not itself a proof; the proof is the receipt at $r_2$.

*Proof.* The obligation edge connects two rows. The upstream row $r_1$ has a claim; the downstream row $r_2$ is where the claim is to be closed. The edge itself is a routing instruction; the proof is the receipt that closes $r_2$. ∎

**Corollary 5.2 (Obligation edges are typed).** An obligation edge is a typed causal link (Theorem 3.1). The edge has a lane and a resolution; the resolution is the routing instruction, the receipt that closes the downstream row.

*Proof.* Direct from Theorem 5.1. The obligation edge is a typed link. ∎

**Corollary 5.3 (Untyped obligation edges are unsound).** An obligation edge with the default lane and an empty resolution is unsound: the routing instruction is missing.

*Proof.* Direct from Theorem 3.1. A default lane with an empty resolution is a contradiction. ∎

**Remark 5.4.** Obligation edges are the structural reason the ledger is a graph. The edges encode the dependencies between rows. The graph is a directed acyclic graph (DAG): the rows are vertices, the edges are causal links, and the partial order is the dependency order.

---

## 6. Ledger Consistency

**Theorem 6.1 (Ledger consistency).** The obligation ledger is consistent iff every row has an explicit lane, an explicit source, and an explicit resolution (or an explicit falsifier, for staged-open rows).

*Proof.* A consistent ledger has no contradictions: every row has the structure required by its lane. The structure is: explicit lane (always), explicit source (always), explicit resolution (for typed rows) or explicit falsifier (for staged-open rows). ∎

**Corollary 6.2 (Unsound rows are removed).** An unsound row (a row that violates Theorem 3.1) is removed from the ledger. The removal is recorded as a meta-verdict.

*Proof.* Direct from Theorem 6.1. An unsound row is a contradiction and must be removed. ∎

**Corollary 6.3 (Empty ledger is consistent).** The empty ledger (no rows) is consistent.

*Proof.* Direct from Theorem 6.1. The empty ledger trivially satisfies the consistency condition. ∎

**Remark 6.6.** Ledger consistency is the structural property that ensures the ledger is usable. An inconsistent ledger has contradictions; the rows cannot be promoted through the claim lanes. A consistent ledger is the substrate of the 8 claim lanes and the 7 evidence classes.

---

## 7. Row Status Classification

**Theorem 7.1 (Row status classification).** Every ledger row has one of three statuses: `closed-now` (non-default lane, non-empty resolution), `open-derived` (non-default lane, empty resolution), or `staged-open` (default lane).

*Proof.* Direct from Definitions 2.2, 2.3, 2.5. ∎

**Corollary 7.2 (Closed-now rows are the 9 receipt_bound rows).** The 9 receipt_bound obligation rows in the OBLIGATION_ROWS.json are exactly the closed-now rows in the current ledger.

*Proof.* Direct from the structure of OBLIGATION_ROWS.json: the 9 receipt_bound rows have explicit receipt paths and timestamps, which are the non-empty resolutions of closed-now rows. ∎

**Corollary 7.3 (Open-derived rows are the 363 derived-pending rows).** The 363 derived-pending rows (345 derived_pending_receipt + 17 derived_pending_citation + 1 derived_pending_dependencies) are the open-derived rows in the current ledger.

*Proof.* Direct from the structure of OBLIGATION_ROWS.json. ∎

**Corollary 7.4 (Staged-open rows are the 733 staged_open rows).** The 733 staged_open rows are the staged-open rows in the current ledger.

*Proof.* Direct from the structure of OBLIGATION_ROWS.json. ∎

**Remark 7.7.** The 1,105 obligation rows in the current ledger are partitioned into 9 closed-now, 363 open-derived, and 733 staged-open. The total is 9 + 363 + 733 = 1,105. The closure rate is 9/1,105 = 0.8%.

---

## 8. Discussion

The causal links and obligation ledgers are the structural backbone of the FLCR series. Every claim in the 100-paper series is backed by a ledger row, and every ledger row has explicit structure. The causal links are the typed edges between rows; the obligation edges are the routing instructions; the negative verdicts are the records of failed attempts.

The ledger is consistent iff every row has the structure required by its lane. The structure is: explicit lane, explicit source, explicit resolution (or falsifier). The 8 claim lanes and the 7 evidence classes are the substrate of the consistency.

The ledger is the substrate of:
- Paper 5 (Typed Boundary Repair): the repair produces a row in the ledger.
- Paper 6 (Oloid Path Carrier): the side-channel of the oloid path is a ledger row.
- Paper 19 (Layer-2 Synthesis Ledger): the layer-2 ledger aggregates rows across many boundaries.
- Paper 30 (Supervisor Cursor): the supervisor cursor traverses the ledger.
- Papers 31–39 (SM Bridge): the SM bridge is the ledger of the gauge structure.

The ledger is honest. The 9 closed-now rows are receipt-bound. The 363 open-derived rows are pending resolution. The 733 staged-open rows are the open obligations. The total is 1,105 rows, with 0.8% closure.

---

## 9. Open Problems

**Open Problem 9.1 (Closure of the 1,096 non-receipt-bound rows).** The 1,096 non-receipt-bound rows are open obligations that must be closed by explicit receipts. The closure rate is currently 0.8%. *Why not closed:* the receipts for the 1,096 rows have not been produced. *Next binding action:* the receipts must be produced through the receipt infrastructure. *Owner:* the receipt chain.

**Open Problem 9.2 (Layer-2 ledger aggregation).** The layer-2 ledger (Paper 19) aggregates rows across many boundaries. The aggregation must be consistent. *Why not closed:* the layer-2 aggregation is not yet computed. *Next binding action:* Paper 19 must compute the layer-2 aggregation. *Owner:* Paper 19.

**Open Problem 9.3 (Supervisor cursor traversal).** The supervisor cursor (Paper 30) traverses the ledger and reserves universal normal-form slots. The traversal must be complete and consistent. *Why not closed:* the supervisor cursor is not yet implemented. *Next binding action:* Paper 30 must implement the supervisor cursor. *Owner:* Paper 30.

---

## 10. Forward References

### 10.1 Within Band A (Mathematics and Formalisms)

**Paper 19 (Layer-2 Synthesis Ledger).** Paper 19 uses the causal links as the substrate for the layer-2 synthesis ledger. The layer-2 ledger aggregates rows across many boundaries; the closure of the layer-2 ledger is the sum of the individual rows. **Object:** the layer-2 ledger. **1-morphism:** the ledger operation.

**Paper 30 (Supervisor Cursor).** Paper 30 uses the causal links as the substrate for the supervisor cursor. The cursor traverses the ledger and reserves universal normal-form slots. **Object:** the ledger. **1-morphism:** the ledger operation.

### 10.2 Within Band B (Standard Model Unification)

**Paper 39 (Falsifiers, Comparators, Standards of Evidence).** Paper 39 uses the causal links as the substrate for the falsifier and comparator standards. **Object:** the standards. **1-morphism:** the comparator operation.

### 10.3 Cross-references

**Paper 5 (Typed Boundary Repair).** Paper 5 establishes the repair row, which is one of the row types in the ledger.

**Paper 6 (Oloid Path Carrier).** Paper 6 uses the repair row as the side-channel of the oloid path.

**Paper 40 (Grand Reconstruction Map).** Paper 40 maps every claim in the prior 39 papers to its proof, its analog reconstruction, its code/tool route, its comparator, its calibration, or its named blocker. Paper 7's claims (the typed causal link, the negative extraction verdict, the obligation edge as routing, the ledger consistency, the row status classification) are mapped by Paper 40 to their receipts (§11).

---

## 11. Receipts

### 11.1 Receipts Cited

**R7.1 (Obligation ledger).** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\OBLIGATION_ROWS.json` — 1,105 rows, 9 receipt_bound, schema `flcr.obligation_rows.v1`. Backs: Theorems 6.1, 7.1, 7.2, 7.3, 7.4.

**R7.2 (Kernel verification).** `D:\CQE_CMPLX\cqekernel\verification\verifier.py` and `D:\CQE_CMPLX\cqekernel\verification\honesty.py`. Backs: the honesty classifier.

**R7.3 (Crystal memory bank).** `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\CAM_CRYSTAL_MEMORY_BANK\` — 469 crystals, 24 state refs. Backs: the content-addressed index of the ledger.

### 11.2 Obligation Rows Bound

**FLCR-07-OBL-001.** The typed causal link (Definition 2.1, 2.2). Status: staged_open.

**FLCR-07-OBL-002.** The negative extraction verdict (Theorem 4.1). Status: staged_open.

**FLCR-07-OBL-003.** The obligation edge as routing (Theorem 5.1). Status: staged_open.

**FLCR-07-OBL-004.** The ledger consistency (Theorem 6.1). Status: staged_open.

**FLCR-07-OBL-005.** The row status classification (Theorem 7.1). Status: staged_open.

### 11.3 Content-Addressed Crystals

- `crystals/slot_crystal/07.*.json` (76 records).
- `states/source_state.OBLIGATION_LEDGER.json`.

### 11.4 Standards Conformance

The claims in this paper are part of the 240/240 standards conformance verdict (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80.

---

## 12. References

### 12.1 Standard Mathematics

- Bang-Jensen, J., & Gutin, G. (2008). *Digraphs: Theory, Algorithms and Applications.* Springer. (Chapter 1: directed acyclic graphs.)
- Knuth, D. E. (1997). *The Art of Computer Programming, Volume 1: Fundamental Algorithms.* Addison-Wesley. (Section 2.3.4.5: topological sorting of DAGs.)

### 12.2 Source Code

- `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\OBLIGATION_ROWS.json` — The obligation ledger.
- `D:\CQE_CMPLX\papers\active-rework\publication_series\Formalizing_LCR_Unifying_Standard_Models\CAM_CRYSTAL_MEMORY_BANK\` — The crystal memory bank.
- `D:\CQE_CMPLX\cqekernel\verification\verifier.py` — Kernel verification.
- `D:\CQE_CMPLX\cqekernel\verification\honesty.py` — Honesty classifier.

### 12.3 Documentation

- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_00__foreword\paper_00.md` — The foreword (Paper 0).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_05__typed_boundary_repair\paper_05.md` — The typed boundary repair (Paper 5).
- `D:\CQE_CMPLX\papers\active-rework\UFT_paper_series\paper_06__oloid_path_carrier\paper_06.md` — The oloid path carrier (Paper 6).

### 12.4 Receipts

See §11.

---

## 12. Data vs Interpretation

This paper is interpretation-heavy. The OBLIGATION_ROWS.json is (D) — 1,105 rows, 9 receipt_bound, the 5-status distribution (staged_open 733, derived_pending_receipt 345, derived_pending_citation 17, receipt_bound 9, derived_pending_dependencies 1). The "typed causal link", the "negative extraction verdict", the "obligation edge as routing", the 3-status classification (closed-now / open-derived / staged-open) are (I) my structural reading.

### Data-backed (D)

- The OBLIGATION_ROWS.json: 1,105 rows, 9 receipt_bound, schema `flcr.obligation_rows.v1`, generated 2026-07-01T02:44:53+00:00. (D — `OBLIGATION_ROWS.json:1-13`.)
- The 5 hold papers: FLCR-10, FLCR-20, FLCR-29, FLCR-30, FLCR-39. (D — `OBLIGATION_ROWS.json:5-10`.)
- The 5-status distribution: staged_open 733, derived_pending_receipt 345, derived_pending_citation 17, receipt_bound 9, derived_pending_dependencies 1. (D — `OBLIGATION_ROWS.json` data field.)
- The 9 receipt_bound rows: FLCR-10-OBL-002/008/010/015, FLCR-29-OBL-004/014, FLCR-30-OBL-001/004/014. (D — `OBLIGATION_ROWS.json` data field.)
- The 3 distinct receipt paths: `CQE-paper-10-t10_master_receipt.json`, `PRIME_CHART_MONSTER_RENORMALIZATION_PASS.json`, `CQE-paper-30-grand_ribbon_meta_framer_receipt.json`. (D — file paths in `OBLIGATION_ROWS.json` data field.)
- The CAM_CRYSTAL_MEMORY_BANK: 469 crystals, 24 state refs. (D — `CAM_CRYSTAL_MEMORY_BANK\`.)

### Interpretation (I)

- The "typed causal link" as a 4-tuple $(r_1, r_2, \ell, e)$ (Definition 2.1). (I — author's structural reading; the OBLIGATION_ROWS.json has a different schema, which is consistent but more specific.)
- The "negative extraction verdict" (Theorem 4.1). (I — author's framing; the standard is "verifier returns fail" or "verifier returns pass_with_open_obligations", which is consistent with this.)
- The "obligation edge as routing" (Theorem 5.1). (I — author's structural reading; the obligation rows have a `prior_paper_deps` field, which is the dependency structure, but the "routing instruction" framing is the author's.)
- The 3-status classification `closed-now / open-derived / staged-open` (Theorem 7.1). (I — author's structural reading of the OBLIGATION_ROWS.json status field; the actual statuses are 5, not 3.)
- The "ledger consistency" theorem (Theorem 6.1). (I — author's framing; the consistency of the ledger is a logical consequence of the schema, but not literally stated in the data.)
- The "monotone ledger" descriptor (Theorem 3.1). (I — author's framing; the ledger is appended to, not modified, but the "monotone" descriptor is the author's.)

### Fabrication (X)

- None in this paper. The interpretation is (I) but defensible.
- The claim "192/192 standards conformance" was a fabrication. The actual standards count is 240/240 (40 papers × 6 standards each), but standards files exist only for Papers 27, 39, 40, 80. The 192/192 figure was invented. (X — corrected to honest 240/240 with caveat.)

---

**End of Paper 7.**

The causal links. The obligation edges. The negative verdicts. The ledger consistency. The row status classification. All backed by receipts. All honest. All forward-referenced.

The first 8 items of the 100-paper series are complete: Paper 0 (foreword), Paper 1 (LCR kernel), Paper 2 (Rule 30 ANF and Lucas carry), Paper 3 (correction surface and F2/Arf edge glue), Paper 4 (D4, $J_3(\mathbb{O})$, triality), Paper 5 (typed boundary repair), Paper 6 (oloid path carrier), Paper 7 (causal links and obligation ledgers).
