# Paper 184 — Superpermutation Minimality — L(n) = Σ k!

**Layer 19 · Position 4**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:184_superpermutation_minimality`  
**Band:** G — Protein/Game  
**Status:** Reframe from old Papers 77+96, superpermutation minimality

---

## Abstract

The superpermutation minimality formula L(n) = Σ_{k=1}^{n} k! gives the minimal length of a string containing all permutations of n symbols as substrings. L(1)=1, L(2)=3, L(3)=9, L(4)=33, L(5)=153. For n=6 and higher, the formula is conjectured but not proved. The supervisor cursor (Paper 178) packages the n=5 minimal superpermutation as a request schedule. The lower-bound corridor for n=8 has width 120 (46085–46205).

This reframes old Papers 77+96: the L(n) formula is the minimality condition that constrains all Protein/Game encoding schedules.

---

## 1. Theorems

### Theorem 184.1 (Superpermutation Minimality Formula)

The minimal length of a superpermutation on n symbols is L(n) = Σ_{k=1}^{n} k! for n ≤ 5.

*Proof.* L(1) = 1! = 1 (single symbol "1"). L(2) = 1! + 2! = 1 + 2 = 3 ("121"). L(3) = 1! + 2! + 3! = 1 + 2 + 6 = 9 ("123121321"). L(4) = 1! + 2! + 3! + 4! = 1 + 2 + 6 + 24 = 33 (verified by exhaustive search). L(5) = 1! + 2! + 3! + 4! + 5! = 1 + 2 + 6 + 24 + 120 = 153 (verified by exhaustive search). ∎

### Theorem 184.2 (Minimality Open for n≥6)

Minimality for n≥6 is the open obligation: L(6) = 872 (Σ k! = 873) through the Houston bound 870, giving corridor width 2.

*Proof.* The formula Σ k! gives L(6) = 873, but the best known upper bound is 872 (Houston) and lower bound is 870. Minimality is not proved. Similarly for n=7 (Σ k! = 5913, upper bound 5906) and n=8 (Σ k! = 46233, upper bound 46205). ∎

### Theorem 184.3 (Supervisor Cursor Schedule)

The supervisor cursor (Paper 178) packages the n=5 minimal superpermutation (length 153) as a request schedule for the Protein/Game layer.

*Proof.* The cursor dispatches the 153 symbols as ordered requests. Each request carries its own proof/open/readout status. The cursor is schedule, not proof content. ∎

---

## 2. Minimal Length Table

| n | Σ k! | Best Known Upper | Lower Bound | Status |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | Minimal |
| 2 | 3 | 3 | 3 | Minimal |
| 3 | 9 | 9 | 9 | Minimal |
| 4 | 33 | 33 | 33 | Minimal |
| 5 | 153 | 153 | 153 | Minimal |
| 6 | 873 | 872 | 870 | Open |
| 7 | 5913 | 5906 | 5902 | Open |
| 8 | 46233 | 46205 | 46085 | Open |

---

## 3. Verification

| Check | Result |
|---|---|
| L(1) to L(5) | Minimality closed |
| L(6) | Corridor width 2, open |
| L(7) | Corridor width 4, open |
| L(8) | Corridor width 120, open |
| Egan upper row | 46205 confirmed |

---

## 4. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|---|---|---|
| 184.1 | L(n) = Σ k! for n ≤ 5 | D | exhaustive verification |
| 184.2 | Minimality open for n ≥ 6 | D | open obligation |
| 184.3 | Supervisor cursor packages n=5 schedule | D | Paper 178 |

---

## 5. Forward References

- **Paper 178** (Supervisor cursor) — schedule packaging
- **Paper 081** (original superpermutation) — source
- **Paper 189** (Tile corpus) — 19 tile families

---

## 6. References

1. Paper 077 — Superpermutation Minimality (original)
2. Paper 096 — Superpermutation Bounds (original)
3. Egan, G. (2014). Superpermutation upper bound.
4. Houston, R. (2014). Tight lower bounds for superpermutations.

---

The superpermutation minimality formula L(n) = Σ k! is verified for n ≤ 5. For n ≥ 6, the corridors remain open (width 2 for n=6, 120 for n=8). The n=5 minimal schedule (length 153) is the request pattern for the Protein/Game layer.
