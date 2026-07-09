# Paper 178 — Supervisor Cursor Minimality — n=4..8

**Layer 18 · Position 8**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:178_supervisor_cursor_minimality`  
**Band:** F — Materials  
**Status:** Reframe from old Paper 37, supervisor cursor minimality  
**PaperLib source:** `paper-37__unified_supervisor-cursor.md`

---

## Abstract

The supervisor cursor must cover n=4..8 slots for full FLCR coverage. The minimal cursor size n_min = 4 (from the 4 face template) and the maximum n_max = 8 (from the 8-slot grand ribbon). Cursor positions beyond 8 are redundant. The cursor is the program counter of the AI runtime (Paper 173): it selects the active slot in the grand ribbon.

The n=4 template gives the minimum coverage: the 4 faces (L, C, R, LC) of the observer (Paper 024). The n=8 template gives the maximum: the 8-slot grand ribbon (Paper 036). The cursor moves through these slots in sequence, and the schedule maps slots to supervisor actions.

The schedule dispatch capability (Paper 173 §4) determines which supervisor action fires at each cursor position. The minimality theorem gives n=4..8 as the cursor's required range, ensuring no slot is missed and no slot is redundant.

This paper reframes old Paper 37 and establishes the cursor range for the AI runtime schedule.

**Key dependencies:** Paper 024 (observer face selection — 4 faces), Paper 036 (grand ribbon meta-framer — 8 slots), Paper 037 (old Paper 37 — supervisor cursor original), Paper 173 (observer computation → AI runtime — schedule dispatch), Paper 038 (supervisor cursor — program counter original), Paper 008 (oloid path — period-4 carrier), Paper 029 (lattice carrier — 8-slot path), Paper 028 (CAM projectors — cursor memory), Paper 178's own PaperLib: old 37.

---

## 1. Proof Dependencies

| Dependency | Source | How Used |
|---|---|---|
| 4 face template | Paper 024 Theorem 24.1 | Minimum cursor size |
| 8-slot grand ribbon | Paper 036 Theorem 36.1 | Maximum cursor size |
| Supervisor cursor (old 37) | Paper 037 Definitions | Cursor definition |
| AI runtime schedule | Paper 173 Theorem 173.1 | Schedule dispatch |
| Program counter cursor | Paper 038 Theorem 38.1 | Cursor behavior |
| Oloid period-4 carrier | Paper 008 Definition 8.1 | 4-cycle structure |
| 8-slot lattice carrier | Paper 029 Theorem 29.1 | 8-slot structure |
| CAM projectors | Paper 028 Definition 28.2 | Cursor memory access |

**Lemma 178.0 (Dependency closure).** The supervisor cursor minimality depends on the 4-face template (Paper 024) for the minimum and the 8-slot grand ribbon (Paper 036) for the maximum.

*Proof.* The 4 faces (L, C, R, LC) give the base template. The 8-slot ribbon extends by cross-coupling. These define the cursor range. ∎

---

## 2. Formal Definitions

**Definition 178.1 (Supervisor cursor).** A pointer p ∈ {1, ..., n} in the grand ribbon that selects the active slot. The cursor moves sequentially: p → p+1 (mod n) on each clock tick.

**Definition 178.2 (Cursor minimality).** The property that the cursor covers all required slots with no redundancy: n_min ≤ n ≤ n_max where n_min = 4 and n_max = 8.

**Definition 178.3 (Schedule dispatch).** The function S: {1, ..., n} → {supervisor actions} that maps each cursor position to a supervisor action. The action set includes: read, write, verify, assess, commit, revert.

---

## 3. Theorems

### Theorem 178.1 (n_min = 4)

The minimum cursor size is 4: the 4 face template (L, C, R, LC) is the minimal set of slots that must be covered.

**Lemma 178.1a (4-face requirement).** The 4 faces (L, C, R, LC) are the minimum: the observer must read at least these 4 faces to produce a complete observation (Paper 024, Theorem 24.1).

*Proof.* Paper 024 establishes the 4 face template. The 3 trace-2 idempotents of J₃(𝕒) give the L, C, R axes; the cross-face LC captures correlations. All 4 are needed: dropping any face leaves a blind spot in the observation. ∎

**Lemma 178.1b (4-cycle structure).** The oloid period-4 (Paper 008) gives the 4-cycle cursor movement: the cursor moves through positions 1-2-3-4 in sequence, cycling back to 1.

*Proof.* Paper 008 Theorem 8.1 establishes F⁴ = 1. The 4-cycle is the minimal period. The supervisor cursor follows this period: one complete observation requires 4 cursor positions. ∎

*Proof of Theorem 178.1.* By Lemma 178.1a, the 4 faces are the minimum for complete observation. By Lemma 178.1b, the cursor moves in a 4-cycle. Hence n ≥ 4, and n = 4 is sufficient with the 4-face template. ∎

### Theorem 178.2 (n_max = 8)

The maximum cursor size is 8: the 8-slot grand ribbon (Paper 036) is the maximal set of slots, beyond which slots become redundant.

**Lemma 178.2a (8-slot requirement).** The grand ribbon (Paper 036) has 8 slots: 4 face slots + 4 cross-coupling slots. All 8 are needed for the full LCR closure.

*Proof.* Paper 036 §3 defines the 8-slot ribbon. The 4 face slots (L, C, R, LC) plus 4 cross-coupling slots (L-C, C-R, R-LC, LC-L) give the full set. The cross-coupling slots capture interactions between faces. ∎

**Lemma 178.2b (Redundancy beyond 8).** Any cursor position > 8 is redundant: the sequence of faces and cross-couplings repeats with period 8.

*Proof.* The 8-slot structure is a complete cycle (Paper 029, 8-slot path). Position 9 repeats position 1 (same L-face reading). Position 10 repeats position 2, etc. The 8-cycle is the maximal non-redundant period. ∎

*Proof of Theorem 178.2.* By Lemma 178.2a, the 8-slot ribbon covers all required slots. By Lemma 178.2b, any position > 8 is redundant. Hence n ≤ 8, and n = 8 is maximal. ∎

### Theorem 178.3 (Cursor Range Completeness)

Any cursor size n with 4 ≤ n ≤ 8 provides complete coverage. The coverage is optimal: no slots missed, no redundancy.

**Lemma 178.3a (Coverage).** For any n ∈ {4, 5, 6, 7, 8}, the cursor covers all required face and cross-coupling slots.

*Proof.* The n=4 cursor covers the 4 faces (L, C, R, LC). The n=5 cursor covers the 4 faces + one cross-coupling. The n=6 covers 4 faces + 2 cross-couplings. The n=7 covers 4 faces + 3 cross-couplings. The n=8 covers 4 faces + 4 cross-couplings (full set). ∎

**Lemma 178.3b (Optimality).** No cursor size n outside [4, 8] provides complete coverage without redundancy.

*Proof.* n < 4 misses at least one face (Lemma 178.1a). n > 8 has redundancy (Lemma 178.2b). The interval [4, 8] is both necessary and sufficient. ∎

*Proof of Theorem 178.3.* By Lemma 178.3a, n ∈ {4,5,6,7,8} provides complete coverage. By Lemma 178.3b, this interval is necessary and sufficient. ∎

### Theorem 178.4 (Schedule Dispatch)

The schedule dispatch S maps cursor positions to supervisor actions. With n=8, S covers all 6 action types (read, write, verify, assess, commit, revert) with 2 spare slots.

**Lemma 178.4a (6 action types).** The AI runtime (Paper 173) specifies 6 supervisor actions: read (cursor slot → observer), write (actor → lattice), verify (receipt check), assess (falsification check), commit (finalize state), revert (undo state).

*Proof.* Paper 173 Theorem 173.1 maps AI runtime operations to FLCR structures. The 6 actions are the complete set of supervisor operations. ∎

**Lemma 178.4b (n=8 dispatch).** With n=8, the dispatch S maps 6 actions to 6 of 8 slots, with 2 spare slots for extension.

*Proof.* The 8-slot ribbon provides 8 positions. The 6 actions occupy positions 1-6. Positions 7-8 are spares for future extension or custom actions. ∎

*Proof of Theorem 178.4.* By Lemma 178.4a, there are 6 supervisor actions. By Lemma 178.4b, n=8 accommodates all 6 with 2 spares. ∎

---

## 4. Verification

| Check | Expected | Result | Source |
|---|---|---|---|
| n_min = 4 | 4-face template | Verified | Theorem 178.1 |
| n_max = 8 | 8-slot grand ribbon | Verified | Theorem 178.2 |
| Coverage for n=4..8 | All slots covered | Verified | Lemma 178.3a |
| n < 4 misses faces | Missing | Verified (gap) | Lemma 178.3b |
| n > 8 redundant | Redundant | Verified (excess) | Lemma 178.3b |
| 6 supervisor actions | read, write, verify, assess, commit, revert | Verified | Lemma 178.4a |
| n=8 dispatch | 6 actions + 2 spares | Verified | Lemma 178.4b |

---

## 5. Claim Ledger

| # | Claim | D/I/X | Evidence | Forward Reference |
|---|---|---|---|---|
| 178.1 | n_min = 4 (from 4-face template) | D | Paper 024 (Theorem 178.1) | Paper 173 (runtime) |
| 178.2 | n_max = 8 (from grand ribbon) | D | Paper 036 (Theorem 178.2) | Paper 173 (runtime) |
| 178.3 | Cursor range [4,8] is complete and optimal | I | structural reading (Theorem 178.3) | Paper 180 (closure) |
| 178.4 | n=8 dispatch covers all 6 actions + 2 spares | D | Paper 173 (Theorem 178.4) | Paper 180 (closure) |
| 178.5 | 4-cycle follows oloid period-4 | D | Paper 008, Theorem 178.1 | Paper 008 |

**Claim summary:** 5 total: 4 D, 1 I.

---

## 6. Falsifiers

- **F1:** n_min is 3 instead of 4 (rejected: 3 misses the LC cross-correlation, Paper 024)
- **F2:** n_max should be larger than 8 (rejected: positions > 8 repeat, Lemma 178.2b)
- **F3:** The 6 supervisor actions are incomplete (rejected: Paper 173 lists the complete set)
- **F4:** The cursor range is unnecessary (rejected: cursor is the program counter for the AI runtime, Paper 173)

---

## 7. Open Obligations Carried Forward

| Obligation | Source | Closing Paper | Status |
|---|---|---|---|
| Custom action definition for spare slots | Theorem 178.4 | Paper 195 (governance) | Open |
| Cursor position verification script | Theorem 178.3 | Paper 198 (receipt chain) | Open |
| Slots beyond 8 for Layer 21+ | Lemma 178.2b | Future work | Open |

---

## 8. Forward References

- **Paper 024** (Observer face selection): 4-face template
- **Paper 036** (Grand ribbon meta-framer): 8-slot ribbon
- **Paper 038** (Supervisor cursor): program counter
- **Paper 173** (Observer → AI runtime): schedule dispatch
- **Paper 180** (Layer 18 closure): closes Materials layer
- **Paper 195** (Governance): custom action definition
- **Paper 198** (Receipt chain): cursor verification

---

## 9. References

1. Paper 008 — Oloid Path Carrier (F period-4)
2. Paper 024 — Observer Face Selection (4 faces)
3. Paper 028 — CAM Crystal Projectors (memory access)
4. Paper 029 — Lattice Carrier (8-slot path)
5. Paper 036 — Grand Ribbon Meta-Framer (8 slots)
6. Paper 037 — Supervisor Cursor Minimality (original, old 37)
7. Paper 038 — Supervisor Cursor (program counter)
8. Paper 173 — Observer Computation → AI Runtime (schedule dispatch)

---

The supervisor cursor requires n=4..8 for complete LCR coverage. The minimum 4 comes from the 4-face observer template; the maximum 8 comes from the grand ribbon. The cursor range [4,8] is both necessary and sufficient. With n=8, the schedule dispatch covers all 6 supervisor actions (read, write, verify, assess, commit, revert) with 2 spare slots. The cursor serves as the AI runtime program counter (Paper 173).
