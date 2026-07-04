# Paper 32 - The Supervisor Cursor

**Virtuous rework status:** merged from current rework, canonical formal paper, companion variants, verifier receipts, and saved CAM/GLM crystal data.

**Method:** preserve the strongest representation of each source face; when
sources disagree, keep the disagreement as a named boundary or next-need.

---

## Source Faces

| Face | Path | Words / count | Contribution |
|------|------|---------------|--------------|
| Current rework | `D:\Paper Reworks\32_The_Supervisor_Cursor.md` | 569 words | Existing skeleton, current status, obligations. |
| Canonical formal paper | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-32\FORMAL_PAPER.md` | 946 words | Main theorem, proof, receipt, falsifier spine. |
| Companion variant | `CQE-paper-32.25.md` | 199 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-32.50.md` | 211 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-32.75.md` | 189 words | Alternate toolkit/contract/bridge phrasing. |
| Companion variant | `CQE-paper-32_UPGRADED.md` | 1049 words | Alternate toolkit/contract/bridge phrasing. |
| Formal verifiers | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-32` | 12 files | Executable evidence surface. |
| Formal receipts | `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\papers\formal\CQE-paper-32` | 12 files | Receipt status and check counts. |
| Saved CAM nodes | `D:\CQE_CMPLX\_downloads_review\content_addressed_nodes.json` | 1 relevant nodes | Prior crystal evidence and obligation nodes. |
| Saved GLM closure rows | `D:\CQE_CMPLX\_downloads_review\glm_obligation_closure_matrix.json` | 0 relevant rows | Closure/partial-closure status updates. |

## Virtuous Synthesis

Paper 32 packages superpermutation schedules as supervisor cursors. A
superpermutation is a string whose length-`n` windows cover every ordering of
`n` symbols. In this corpus, that string is not proof content by itself. It is
a compressed request schedule: a cursor that decides which enumeration request
fires next.

This version treats the formal paper as the proof spine, the companion variants as interface contracts, and the CAM/GLM rows as status-bearing crystal data. The paper's open obligations are not deleted; they are the next work items required before stronger claims can be promoted.

## Companion Face Digest

- **Paper 32.25 - Supervisor Cursor Toolkit Supplement.** This supplement shows how to reproduce Paper 32's supervisor-cursor receipt.
The proof is in Paper 32 and its formal verifier. The cursor schedules
requests; it does not replace the proof receipts attached to the requested
items.
- **Paper 32.50 - Supervisor Cursor Claim Contract.** This contract defines when a supervisor-cursor statement is valid. It prevents
the schedule from becoming an untracked substitute for the proof receipts it
routes.
- **Paper 32.75 - Supervisor Cursor Next-State Preconditions.** This supplement defines how Paper 32 exports into deployment. The kernel may
use the supervisor cursor to schedule requests, but every scheduled request
must carry its own proof/open/readout status.
- **Paper 32 - The Supervisor Cursor (UPGRADED: Affirmative Supervisor Cursor Selector Physics Map).** (Affirmative)

## Missed Verifier Rows to Reconcile

- `verify_glm_43200_stratum_terminal.py`

## Receipt Surface

| Receipt | Summary |
|---------|---------|
| `43200_pyramid_structure_receipt.json` | status=pass; checks=10/10 |
| `alena_morph_e8_kit_receipt.json` | status=pass; checks=11/11 |
| `e8_routed_constructor_receipt.json` | status=pass; checks=7/7 |
| `higher_order_superperm_manager_receipt.json` | status=pass; checks=15/15 |
| `houston_872_attempt_receipt.json` | status=pass; checks=5/5 |
| `hyperpermutation_audit_receipt.json` | status=pass; checks=11/11 |
| `lcr_superperm_handbuild_receipt.json` | status=pass; checks=18/18 |
| `n6_871_reduction_receipt.json` | status=pass; checks=9/9 |
| `octad_e8_structure_receipt.json` | status=pass; checks=17/17 |
| `p120_e8_cayley_dickson_doubling_receipt.json` | status=pass; checks=10/10 |
| `stratum_43200_terminal_receipt.json` | status=True; checks=6/6 |
| `supervisor_cursor_schedule_receipt.json` | status=pass_with_open_minimality_obligations |

## Open Obligations as Next Needs

| ID | Current row | CAM/GLM status |
|----|-------------|----------------|
| `32.1` | \| 32.1 \| Minimality for `n ≥ 6` without independent exclusion proofs \| External / later paper \| | carry as next need |
| `32.2` | \| 32.2 \| `n=8` corridor below `46205` \| External / later paper \| | carry as next need |
| `32.3` | \| 32.3 \| Product selectors must preserve proof/open/readout status \| Engineering \| | carry as next need |
| `32.4` | \| 32.4 \| Reconcile companion variants (`CQE-paper-32.md` vs `32-obs.md`) and `lib-forge/papers_output` copy \| Documentation cleanup \| | carry as next need |

## Obligation Springboard Lanes

Obligations return to the earliest paper they can affect, then rework upward through each paper in the lane before the local claim is promoted.

### Local Claim Pressure

- All physical or unit-bearing readings must pass through an external calibration gate before appearing as more than conditional interface language.
- Engineering and adapter gaps should be promoted to work items, not used as theorem premises.

### Local Lane Table

| Obligation | Return start | Upward lane | Rework instruction |
|------------|--------------|-------------|--------------------|
| `32.1` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `32.2` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional. |
| `32.3` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Route this into tooling or adapter work before using it as a premise in the paper's theorem. |
| `32.4` | `09` | `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32` | Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action. |

## Detailed Expansion Pass

### Paper-Level Thesis

Paper 32 functions as the suite's supervisor cursor and final selector/readout-status guard. Its virtuous version should therefore make three layers visible at once: the formal claim that is actually proved, the receipt or verifier evidence that lets the claim be replayed, and the explicit boundary that prevents the reader from promoting an open lift into a closed theorem.

The companion variants are used as exposition and interface contracts. They may contribute terminology, examples, and downstream preconditions, but the canonical formal paper remains the proof spine.

### Claim Status Ledger

No explicit claim/theorem lines were extracted from the formal spine. Use the abstract, proof, receipts, and obligation table to reconstruct the claim ledger before publication.

### Evidence and Receipt Detail

The receipt surface should be discussed in prose, not only listed. Passing receipts make the paper replayable; failed, partial, or missing checks become local boundaries.
- `43200_pyramid_structure_receipt.json`: status=pass; checks=10/10.
- `alena_morph_e8_kit_receipt.json`: status=pass; checks=11/11.
- `e8_routed_constructor_receipt.json`: status=pass; checks=7/7.
- `higher_order_superperm_manager_receipt.json`: status=pass; checks=15/15.
- `houston_872_attempt_receipt.json`: status=pass; checks=5/5.
- `hyperpermutation_audit_receipt.json`: status=pass; checks=11/11.
- `lcr_superperm_handbuild_receipt.json`: status=pass; checks=18/18.
- `n6_871_reduction_receipt.json`: status=pass; checks=9/9.
- `octad_e8_structure_receipt.json`: status=pass; checks=17/17.
- `p120_e8_cayley_dickson_doubling_receipt.json`: status=pass; checks=10/10.
Verifier files are the strongest executable surface. The paper should name the verifier next to any claim it supports.
- `verify_120_e8_cayley_dickson_doubling.py` should be mapped to the claim or obligation it checks.
- `verify_43200_pyramid_structure.py` should be mapped to the claim or obligation it checks.
- `verify_alena_morph_e8_kit.py` should be mapped to the claim or obligation it checks.
- `verify_e8_routed_constructor.py` should be mapped to the claim or obligation it checks.
- `verify_glm_43200_stratum_terminal.py` should be mapped to the claim or obligation it checks.
- `verify_higher_order_superperm_manager.py` should be mapped to the claim or obligation it checks.
- `verify_houston_872_attempt.py` should be mapped to the claim or obligation it checks.
- `verify_hyperpermutation_audit.py` should be mapped to the claim or obligation it checks.
- `verify_lcr_superperm_handbuild.py` should be mapped to the claim or obligation it checks.
- `verify_n6_871_reduction.py` should be mapped to the claim or obligation it checks.
- `verify_octad_e8_structure.py` should be mapped to the claim or obligation it checks.
- `verify_supervisor_cursor_schedule.py` should be mapped to the claim or obligation it checks.

### Obligation Workups

**32.1.** | 32.1 | Minimality for `n ≥ 6` without independent exclusion proofs | External / later paper |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `supervisor cursor and final selector/readout-status guard` boundary before this obligation can strengthen the source paper.

**32.2.** | 32.2 | `n=8` corridor below `46205` | External / later paper |

- **Status reading:** conditional until external calibration exists.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32`.
- **Paper-local consequence:** Push physical, experimental, or unit-bearing claims behind a calibration gate; the internal formal result may survive, but measured-world language must remain conditional.
- **Rewrite requirement:** keep the internal construction as the theorem and move all measured-world, unit-bearing, experimental, or physical identification language into a calibration paragraph.
- **Upward effect:** Papers in the lane must preserve the `supervisor cursor and final selector/readout-status guard` boundary before this obligation can strengthen the source paper.

**32.3.** | 32.3 | Product selectors must preserve proof/open/readout status | Engineering |

- **Status reading:** requires tooling/adapter work before theorem use.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32`.
- **Paper-local consequence:** Route this into tooling or adapter work before using it as a premise in the paper's theorem.
- **Rewrite requirement:** turn the gap into an adapter/tooling task and avoid depending on it as a completed premise.
- **Upward effect:** Papers in the lane must preserve the `supervisor cursor and final selector/readout-status guard` boundary before this obligation can strengthen the source paper.

**32.4.** | 32.4 | Reconcile companion variants (`CQE-paper-32.md` vs `32-obs.md`) and `lib-forge/papers_output` copy | Documentation cleanup |

- **Status reading:** open next-need.
- **Springboard lane:** `09 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32`.
- **Paper-local consequence:** Leave the obligation live and convert it into the next verifier, witness, adapter, or documentation action.
- **Rewrite requirement:** leave the item live as the next verifier, witness, adapter, calibration, or documentation pass.
- **Upward effect:** Papers in the lane must preserve the `supervisor cursor and final selector/readout-status guard` boundary before this obligation can strengthen the source paper.

### Cross-Paper Inheritance

The springboard lane means this paper cannot be revised in isolation. The upstream papers in the lane must preserve the following inherited roles before the local claim can be strengthened:

- Paper 09: finite Hamiltonian-window substrate and receipt-preserving temporal readout.
- Paper 10: master receipt, replay boundary, and open-lift visibility layer.
- Paper 11: theory-admission gate and boundary classifier.
- Paper 12: cellular-automaton prediction surface and Rule 30 scope boundary.
- Paper 13: Standard-Model quark-face transport and calibration boundary.
- Paper 14: GR boundary-repair curvature map and physical-curvature guard.
- Paper 15: QFT/Higgs mass-residue carrier and measured-mass calibration guard.
- Paper 16: continuum-edge residual layer and finite-window-to-limit boundary.
- Paper 17: E6/E8 correction tower and exceptional-lattice lift surface.
- Paper 18: VOA/Moonshine representation route and identification guard.
- Paper 19: observer face-selection and physical-observer boundary.
- Paper 20: layer-2 synthesis ledger and reachability status surface.
- Paper 21: MorphForge/PolyForge/MorphoniX engineering bridge.
- Paper 22: MetaForge applied-materials calibration bridge.
- Paper 23: FoldForge protein-folding calibration bridge.
- Paper 24: KnightForge combinatorial-game surface.
- Paper 25: energetic traversal and unit-calibration bridge.
- Paper 26: Z-pinch/shear-horizon physical-witness bridge.
- Paper 27: observer-delay/shared-reality guard layer.
- Paper 28: N-dimensional game-lattice applied surface.
- Paper 29: Monster/energy-bound hypothesis and encoding-invariance boundary.
- Paper 30: grand ribbon meta-framer and transport-ledger framing layer.
- Paper 31: retrospective LCR readout and downstream-status guard.
- Paper 32: supervisor cursor and final selector/readout-status guard.

### Publication-Grade Rewrite Targets

For the next manual/editorial pass, expand the paper body around these targets:

1. Put the strongest closed theorem in the opening synthesis, then immediately state the largest thing it does not prove.
2. Move every calibration, physical-identification, and external-validation claim into a guarded paragraph with its required witness named.
3. Place verifier and receipt names beside the exact claims they support.
4. Preserve open lifts as first-class obligations rather than treating them as editorial TODOs.


## Canonical Formal Spine

## Abstract

Paper 32 packages superpermutation schedules as supervisor cursors. A
superpermutation is a string whose length-`n` windows cover every ordering of
`n` symbols. In this corpus, that string is not proof content by itself. It is
a compressed request schedule: a cursor that decides which enumeration request
fires next.

The closed result is practical and bounded. The verifier validates
superpermutation coverage records for `n=4` through `n=8`, confirms the
recursive chart-walk construction at `n=8`, records the Egan upper row
`46205`, records the lower-bound corridor of `120`, checks the n=5 octad
structure, and confirms that the paper-kernel selector wraps Paper 32 forward
to Paper 01 for active-suite retest. It claims minimality only where the local
evidence permits it: `n=4` and `n=5`. It does not claim minimality for
`n>=6`.

## Closed Evidence

The receipt is generated by
`production/formal-papers/CQE-paper-32/verify_supervisor_cursor_schedule.py`.
It imports the live `GraphStax.permforge` package surface and writes
`supervisor_cursor_schedule_receipt.json`.

The verifier calls `verify_record(n)` for `n=4..8`. Every record has validated
coverage:

```text
n=4: length 33, coverage true, minimality closed
n=5: length 153, coverage true, minimality closed
n=6: length 873, coverage true, minimality not claimed
n=7: length 5908, coverage true, minimality not claimed
n=8: length 46205, coverage true, minimality not claimed
```

The verifier also constructs the recursive chart-walk string for `n=8`. Its
length is `46233`, and coverage is true. The shipped `n=8` record matches the
Egan upper formula at `46205`, while the lower bound is `46085`. The open
corridor is therefore `120`.

Finally, the verifier checks the scheduler surface. A `SuperPermScheduler`
dispatches enumeration requests over items. The cursor is not ribbon content;
it is the request schedule that tells the kernel which local ordering to read.

## Definitions

An enumeration request is a cursor event. Without a request, the center `C` is
not produced for the readout.

A local chart is a length-`n` window of the schedule string.

Coverage means that the set of length-`n` windows contains every permutation of
the `n` symbols.

Minimality means no shorter covering string exists. This paper treats
minimality as closed only for `n=4` and `n=5`.

A supervisor cursor is a compressed schedule for requests. It tells the suite
which ordering to inspect next; it does not replace the receipt attached to the
thing being inspected.

A selector is a deployable paper-kernel route: suite, block, or individual
paper.

## Claims

1. Coverage for the shipped `n=4..8` schedule records is validated.

2. The recursive chart-walk construction reaches `n=8` with length `46233` and
full coverage.

3. The shipped `n=8` record has length `46205`, matching the Egan upper row.

4. The `n=8` corridor between the lower bound and the Egan upper row has width
`120`.

5. The n=5 octad has eight schedules and a reversal orbit with four fixed
points and two swapped pairs.

6. The supervisor cursor schedules enumeration requests. It is not ribbon
content and not hidden proof support.

7. The paper-kernel selector wraps Paper 32 forward to Paper 01 for active
suite retest, while Paper 00 remains the inherited method contract.

## Theorem 32

The suite can be packaged with a supervisor cursor when the cursor is treated
as a compressed request schedule over validated coverage rows, while each
paper's proof/open/readout status remains attached to its own receipt.

## Proof

Run `verify_supervisor_cursor_schedule.py`.

The coverage checks pass because `verify_record(n)` returns validated records
with coverage true for every `n` from 4 through 8.

The minimality-scope check passes because the verifier marks only `n=4` and
`n=5` as closed minimality rows. For `n=6`, `n=7`, and `n=8`, the records are
validated schedules and bounds rows, not minimality proofs.

The `n=8` bounds checks pass because the shipped record length equals the Egan
upper value `46205`; the lower bound is `46085`; and the open corridor is
`120`. The recursive chart-walk construction also covers at length `46233`.

The scheduler check passes because `SuperPermScheduler(4)` dispatches item
requests from the superpermutation string and reports that the cursor is not
content. This closes the "No request, no C" packaging rule.

The kernel-selector check passes because the paper-kernel registry places
Paper 32 at the suite wrap: the next active-suite paper is Paper 01. Therefore
Paper 32 can serve as a deployable supervisor cursor without hiding proof
status. This proves Theorem 32.

## Worked Example

Take the eight Paper 30 ribbon slots:

```text
C, L, R, B, T, O, W, A
```

The naive way to inspect all orderings of these eight slots is to write every
ordering independently. The schedule way is to walk a superpermutation string:
each length-8 window is one local read order, and overlapping windows reuse
symbols.

The verifier checks the shipped `n=8` schedule at length `46205`. Every one of
the `8! = 40320` orderings appears. The result is not a proof that `46205` is
minimal; it is a validated coverage record at the Egan upper row, with an open
minimality corridor of `120`.

When the cursor fires, it asks for an ordering. The target paper or tool still
brings its own receipt. The cursor only decides the request order.

## Open Obligations

Minimality for `n>=6` remains open unless independent shorter-string
exclusion proofs are supplied.

The `n=8` corridor below `46205` remains open. Any shorter candidate must ship
with a coverage receipt and falsifier rows.

Product selectors must preserve proof/open/readout status. A cursor that makes
navigation easier may not hide obligations.

Older "final observation" language remains reflective only unless a separate
formal claim and verifier are supplied.

## Suite Role

Paper 32 is the deployable selector layer for the paper suite. It lets the
kernel route suite, block, and paper requests while preserving status. Its
wrap to Paper 01 makes the active suite retestable as a loop; Paper 00 remains
the inherited contract outside that active proof window.

## Rework Integration Notes

- Keep the claim-strength tags attached to each theorem or bridge.
- Import companion variant language only when it strengthens exposition without
  promoting an open bridge.
- Treat every obligation row as a routed next-need: verifier, witness, adapter,
  calibration, documentation pass, or explicit guard.
- If a CAM/GLM row proposes `partially_closed`, update the paper body and
  obligation audit together; do not silently mark it closed.
