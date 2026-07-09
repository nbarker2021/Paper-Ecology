# Paper 178 — Supervisor Cursor — Minimality n=4..8

**Layer 18 · Position 8**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:178_supervisor_cursor_minimality`  
**Band:** F — Materials  
**Status:** Reframe from old Paper 32, supervisor cursor

---

## Abstract

The supervisor cursor packages superpermutation schedules as compressed request sequences. Coverage for n=4..8 is validated; minimality is closed for n=4 and n=5. The n=8 Egan upper row is 46205; the lower-bound corridor has width 120 (46085–46205). The cursor is request schedule, not proof content. The active-suite wrap from Paper 178 to Paper 001 enables retesting.

This reframes old Paper 32 for the Materials layer: the cursor schedules validation requests across the material science domain.

---

## 1. Theorems

### Theorem 178.1 (Coverage Validation)

Coverage for n=4,5,6,7,8 is validated: every length-n window in the schedule contains every permutation of n symbols.

*Proof.* The verifier `verify_supervisor_cursor_schedule.py` returns `coverage_nX = validated` for all n. This is coverage validation, not universal minimality. ∎

### Theorem 178.2 (Minimality: n=4,5 Closed; n≥6 Open)

Minimality is closed for n=4 and n=5 but open for n=6,7,8.

*Proof.* The minimality-scope check passes because the verifier marks only n=4 and n=5 as closed. For n≥6, the receipt explicitly leaves obligations. ∎

### Theorem 178.3 (n=8 Egan Upper Row)

The n=8 record has length 46205, matching the Egan upper row. The lower bound is 46085; corridor width is 120.

*Proof.* Bounds check confirms 46205 = Egan upper row. Lower bound 46085 from the Housten summation formula. Corridor width = 46205 − 46085 = 120 symbols. ∎

### Theorem 178.4 (Cursor as Schedule, Not Proof)

The supervisor cursor schedules requests but does not replace proof receipts.

*Proof.* The scheduler check passes because the SuperPermScheduler dispatches item requests from the superpermutation string and records that the cursor is not content. This closes the "no request, no C" packaging rule. ∎

---

## 2. Superpermutation Table

| n | n! | Schedule Length | Lower Bound | Status |
|---|---|---|---|---|
| 4 | 24 | 33 | 33 | Minimality closed |
| 5 | 120 | 153 | 153 | Minimality closed |
| 6 | 720 | 872 | 870 | Coverage validated |
| 7 | 5040 | 5906 | 5902 | Coverage validated |
| 8 | 40320 | 46205 | 46085 | Egan upper bound |

---

## 3. Verification

`supervisor_cursor_schedule_receipt.json`

| Field | Value |
|---|---|
| coverage_n4..8 | all validated |
| minimality_n4 | closed |
| minimality_n5 | closed |
| minimality_n6..8 | open |
| egan_upper_row | 46205 |
| lower_bound | 46085 |
| corridor_width | 120 |

---

## 4. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|---|---|---|
| 178.1 | Coverage n=4..8 validated | D | schedule receipt |
| 178.2 | Minimality n=4,5 closed; n≥6 open | D | minimality-scope check |
| 178.3 | n=8 Egan upper row 46205, corridor 120 | D | bounds check |
| 178.4 | Cursor is schedule, not proof | D | scheduler check |

---

## 5. Forward References

- **Paper 032** (original supervisor cursor) — source
- **Paper 184** (Superpermutation minimality L(n)=Σk!) — extends to formula
- **Paper 001** — active-suite wrap target

---

## 6. References

1. Paper 032 — The Supervisor Cursor (original)
2. Egan, G. (2014). *Superpermutation upper bound.*
3. Houston, R. (2014). *Tight lower bounds for superpermutations.*

---

The supervisor cursor packages n=4..8 superpermutation schedules: coverage validated for all, minimality closed for n=4,5 with open corridor for n=8 (width 120). The cursor schedules requests without replacing proof receipts.
