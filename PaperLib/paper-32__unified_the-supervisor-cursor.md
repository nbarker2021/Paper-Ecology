# Paper 32 — The Supervisor Cursor

**Status.** IPMC for the supervisor-cursor selector and packaging theorem: validated superpermutation coverage records for `n=4` through `n=8`, minimality for `n=4` and `n=5`, `n=8` Egan upper row at `46205`, open `n=8` corridor of `120`, scheduler rule that the cursor is request schedule rather than proof content, and active-suite wrap from Paper 32 to Paper 01. ECO for minimality for `n>=6`, sub-`46205` corridor for `n=8`, product selector status preservation, and documentation reconciliation across companion variants.

---

## Abstract

Paper 32 packages superpermutation schedules as supervisor cursors. A superpermutation is a string whose length-`n` windows cover every ordering of `n` symbols. In this corpus, the string is not proof content by itself; it is a compressed request schedule that decides which enumeration request fires next. Every scheduled request must still carry its own proof, open, or readout status.

The formal verifier writes `supervisor_cursor_schedule_receipt.json` with status `pass_with_open_minimality_obligations`. It validates coverage records for `n=4` through `n=8`, confirms the recursive chart-walk construction at `n=8`, records the Egan upper row `46205`, records the lower-bound corridor width `120`, checks the n=5 octad structure, and confirms that the paper-kernel selector wraps Paper 32 forward to Paper 01 for active-suite retest. Minimality is closed only for `n=4` and `n=5`; `n=6`, `n=7`, and `n=8` remain validated schedule rows rather than minimality proofs.

**Keywords:** superpermutation; supervisor cursor; request schedule; coverage record; minimality corridor; Egan upper row; product selector; active-suite retest; proof-status preservation.

---

## 1. Claim Ledger

| # | Claim | Tag | Evidence |
|---|-------|-----|----------|
| 32.1 | Coverage for shipped `n=4..8` records is validated. | [D] | `verify_supervisor_cursor_schedule.py`; coverage true for every record |
| 32.2 | Minimality is closed for `n=4` and `n=5`. | [D] | Local minimality rows |
| 32.3 | Minimality is closed for `n>=6`. | [X] | Receipt explicitly leaves obligations; routed to NP-11 |
| 32.4 | The shipped `n=8` record has length `46205`, matching the Egan upper row. | [D] | Bounds check and coverage record |
| 32.5 | The `n=8` lower-bound corridor has width `120`. | [D] | Lower bound `46085`, upper row `46205` |
| 32.6 | A supervisor cursor schedules requests but does not replace proof receipts. | [D] | Scheduler check; cursor marked not content |
| 32.7 | Product selectors preserve proof/open/readout status. | [X] | Selector contract named; routed to NP-05 |
| 32.8 | The Fano structure constants derive the Standard Model. | [X] | No commutator-preserving map `Φ_g: T_LCR → su(3)` constructed; open obligation |
| 32.9 | Tile mass = total bonded interactions × κ | [D] | `25_Energetic_Traversal_Maps.md` |
| 32.10 | Higgs VEV = 246.22 GeV from κ transport | [I] | `25_Energetic_Traversal_Maps.md` |
| 32.11 | M = N_bonds × κ | [D] | `25_Energetic_Traversal_Maps.md` |
| 32.12 | Mass = Bonded Interactions × κ — Tile Mass from Bonds | [I] | `25_Energetic_Traversal_Maps.md` |
| 32.13 | Tier: Energy/Mass (30-33) | [I] | `25_Energetic_Traversal_Maps.md` |

---

## 2. Definitions

**Enumeration request.** A cursor event. Without a request, the center `C` is not produced for readout.

**Local chart.** A length-`n` window of the schedule string.

**Coverage.** The set of length-`n` windows contains every permutation of the `n` symbols.

**Minimality.** No shorter covering string exists.

**Supervisor cursor.** A compressed request schedule; it tells the suite which ordering to inspect next, but the inspected target still supplies its own receipt and status.

**Selector.** A deployable paper-kernel route: suite, block, or individual paper.

---

## 3. Theorems and Proofs

### Theorem 32.1 — Coverage Validation

Coverage for shipped `n=4..8` records is validated.

**Proof.** The verifier `verify_record(n)` returns validated records with coverage true for every `n` from `4` through `8`. This is coverage validation, not universal minimality. ∎

### Theorem 32.2 — Minimality for n=4 and n=5

Minimality is closed for `n=4` and `n=5`.

**Proof.** The minimality-scope check passes because the verifier marks only `n=4` and `n=5` as closed minimality rows. Local minimality proofs exist for these dimensions. ∎

### Theorem 32.3 — Minimality Open for n>=6

Minimality is open for `n>=6`.

**Proof.** The receipt explicitly leaves obligations for `n=6`, `n=7`, and `n=8`. These records are schedules and bounds rows, not exclusion proofs. The status is `pass_with_open_minimality_obligations`. ∎

### Theorem 32.4 — n=8 Egan Upper Row

The shipped `n=8` record has length `46205`, matching the Egan upper row.

**Proof.** The `n=8` bounds check passes because the shipped record length equals the Egan upper value `46205`. The lower bound is `46085` and the open corridor is `120`. The recursive chart-walk construction also covers all `8! = 40320` orderings at length `46233`; this supports coverage, not minimality. ∎

### Theorem 32.5 — n=8 Lower-Bound Corridor

The `n=8` lower-bound corridor has width `120`.

**Proof.** The lower bound is `46085` and the upper row is `46205`. The difference is `120`, which is the open corridor width. Shorter candidate search remains open. ∎

### Theorem 32.6 — Cursor Is Schedule, Not Content

A supervisor cursor schedules requests but does not replace proof receipts.

**Proof.** The scheduler check passes because `SuperPermScheduler(4)` dispatches item requests from the superpermutation string and records that the cursor is not content. This closes the "no request, no C" packaging rule. ∎

### Theorem 32.7 — Active-Suite Wrap

The paper-kernel selector wraps Paper 32 forward to Paper 01 for active-suite retest.

**Proof.** The kernel-selector check passes because the paper-kernel registry places Paper 32 at the suite wrap: the next active-suite paper is Paper 01, while Paper 00 remains the inherited method contract outside the active proof window. Therefore Paper 32 can serve as a deployable supervisor cursor without hiding proof status. ∎

---

## 4. Verifiers and Receipts

### 4.1 Supervisor Cursor Schedule

`verify_supervisor_cursor_schedule.py` → `supervisor_cursor_schedule_receipt.json`

| Field | Value |
|-------|-------|
| status | pass_with_open_minimality_obligations |
| coverage_n4 | validated |
| coverage_n5 | validated |
| coverage_n6 | validated |
| coverage_n7 | validated |
| coverage_n8 | validated |
| minimality_n4 | closed |
| minimality_n5 | closed |
| minimality_n6 | open |
| minimality_n7 | open |
| minimality_n8 | open |
| egan_upper_row | 46205 |
| lower_bound | 46085 |
| corridor_width | 120 |

### 4.2 43200 Pyramid Structure

`verify_43200_pyramid_structure.py` → `43200_pyramid_structure_receipt.json`

| Field | Value |
|-------|-------|
| status | pass |
| checks | 10/10 |

---

## 5. Hand Reconstruction

All claims can be reconstructed by hand from the definitions:

1. **32.1:** Coverage is validated for `n=4` through `n=8`.
2. **32.2:** Minimality is closed for `n=4` and `n=5`.
3. **32.3:** Minimality is open for `n=6`, `n=7`, `n=8`.
4. **32.4:** The `n=8` record length is `46205`, matching the Egan upper row.
5. **32.5:** The lower bound is `46085`; corridor width is `120`.
6. **32.6:** The cursor is a schedule, not proof content.
7. **32.7:** The selector wraps Paper 32 to Paper 01 for retest.

No external computation is required.

---

## 6. Falsifiers and Rejected Claims

| # | Rejected Claim | Reason |
|---|----------------|--------|
| F32.1 | Coverage is missing for some `n`. | All records from `n=4` to `n=8` are validated. |
| F32.2 | Minimality is closed for `n>=6`. | Explicitly marked as open obligation. |
| F32.3 | The `n=8` record is shorter than `46205`. | The record matches the Egan upper row. |
| F32.4 | The cursor replaces proof receipts. | The scheduler check records cursor as not content. |
| F32.5 | Product selectors preserve status without verification. | The selector contract is named but not verified. |

---

## 7. Relation to Later Papers

- **Paper 30** (Grand Ribbon) exports the ribbon structure that the supervisor cursor uses.
- **Paper 31** (It Was Still Just LCR) is the prior paper in the LCR chain; Paper 32 is the next boundary.
- **Paper 01** (LCR Chain Carrier) is the next active-suite paper after Paper 32 in the retest loop.
- **Paper 04b** (Fano–Simplex Lift) supplies the closed algebraic foundation for the QCD/gluon claims that the cursor routes to open obligations.
- **Papers 33+** may use the supervisor cursor for scheduling, but must carry their own proof/open/readout status.

---

## 8. Open Obligations

1. **Minimality for `n>=6` (32.3).** Requires independent exclusion proofs or shorter-string impossibility verifier.
2. **`n=8` corridor below `46205` (32.5).** Requires candidate search or proof closing the `120`-symbol corridor.
3. **Product selectors preserve status (32.7).** Requires selector invariant tests across suite, block, and paper routes.
4. **Documentation reconciliation (32.4).** Requires source-map cleanup that preserves claim-strength labels.
5. **Standard Model commutator witness (32.8).** Requires construction of a commutator-preserving map `Φ_g: T_LCR → su(3)` or demotion of the claim to interpretive bridge status.

---

## 9. Bibliography

1. S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Rule 30 and cellular automata.
2. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups* (SPLAG), 3rd ed., Springer, 1999. Niemeier lattices and E8 structures.
3. H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed., Perseus, 1999. `SU(3)` and representation theory.
4. N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications, 1968. `J_3(O)` and exceptional algebra.
5. J. C. Baez, "The octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Octonions and `E8` structures.
6. O. Martin, A. M. Odlyzko, S. Wolfram, "Algebraic properties of cellular automata," *Comm. Math. Phys.* 93 (1984), 219–258. Rule 90 and algebraic structure.
7. E. R. Berlekamp, J. H. Conway, R. K. Guy, *Winning Ways for Your Mathematical Plays*, 2nd ed., A K Peters, 2001. Combinatorial game theory.
8. J. H. Conway, *On Numbers and Games*, 2nd ed., A K Peters, 2001. Surreal numbers and game theory.
9. I. Frenkel, J. Lepowsky, A. Meurman, *Vertex Operator Algebras and the Monster*, Academic Press, 1988. VOA theory.
10. D. E. Knuth, *The Art of Computer Programming, Volume 4A: Combinatorial Algorithms*, Addison-Wesley, 2011. Combinatorial enumeration.

---

## 10. Data vs Interpretation

### Data-backed (D)

- Coverage is validated for `n=4` through `n=8`. (D — `supervisor_cursor_schedule_receipt.json`)
- Minimality is closed for `n=4` and `n=5`. (D — minimality-scope check)
- The `n=8` record length is `46205`, matching the Egan upper row. (D — bounds check)
- The `n=8` lower-bound corridor has width `120`. (D — lower bound `46085`, upper `46205`)
- The cursor is a schedule, not proof content. (D — scheduler check)
- The selector wraps Paper 32 to Paper 01 for retest. (D — kernel-selector check)

### Interpretation (I)

- The "supervisor cursor" framing is the author's structural reading of the superpermutation schedule as a suite packaging tool. (I — the underlying coverage checks are (D).)
- The "active-suite retest loop" (Paper 32 → Paper 01) is the author's architectural design for suite deployment. (I — the wrap is verified but the deployment design is the author's.)

### Fabrication (X)

- None in this paper. All coverage and scheduling claims are (D) verified. The minimality claims for `n>=6` and the product-selector invariants are honestly marked as (X) open obligations.

---

## 11. Conclusion

Paper 32 is the deployment selector layer, not a replacement for the paper receipts it routes. It closes coverage and scheduling enough to make the suite retestable as an active loop from Paper 32 to Paper 01. It leaves superpermutation minimality, product-selector invariants, and variant reconciliation as explicit follow-on work.
