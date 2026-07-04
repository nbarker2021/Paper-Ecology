# TR-CL-06 Row-by-Row Scope — EQ-REG-0010 Blocked Cluster

**Date:** 2026-06-30 (Cycle 4 — all 5 falsifier templates complete)  
**Parent:** `THEOREM_REGISTRY_PAIR_QUEUE.json` cluster `TR-CL-06`  
**Gate:** `BLOCKED_NO_SCOPED_COMPARATOR` — bulk physics-band PEEP pairing prohibited  
**Source registry:** `suite19_umbrella_math/042-claude-real-math-umbrella-theorem-registry.md`

---

## Scope rule

Each theorem row below must receive an **individual** falsifier row, verifier anchor, and (if any) external comparator **before** promotion. No cluster-level PEEP. Rows marked `EMPIRICAL_ONLY` stay `BOUNDED_EXEC` until a scoped 2025+ comparator is identified.

---

## Row inventory

| Theorem ID | Title (short) | Status tag | Verifier anchor | Scoped comparator lane | Phase 9 action |
|------------|---------------|------------|-----------------|------------------------|----------------|
| **T_UNIVERSAL_CA** | 64 silent-boundary ECAs close at n=3 | EMPIRICAL_ONLY | `experiments/exp_ca_partition.py` | CA universality / elementary CA classification (2025+ survey paper) | **DEFER** — falsifier: promote beyond 256-rule empirical sweep without peer scope |
| **T_UNIVERSAL_NUMBER_THEORY** | Fibonacci/Stern/prime-gap parity closure | EMPIRICAL_ONLY | `experiments/run_all.py` (number theory) | Sequence-closure / Weyl-group literature (not physics-band) | **DEFER** — split per sub-sequence before pairing |
| **T_UNIVERSAL_CMB** | Cumulative Planck TT closure | EMPIRICAL_ONLY | `experiments/exp_relational_qubit.py` | CMB power-spectrum methodology paper (calibration-bound) | **DEFER** — requires unit-bearing Planck comparator rows |
| **T_INV_1** | e, φ, h as CLASSICAL invariants | EMPIRICAL_OVERCLAIM_RISK | `experiments/exp_physical_constants.py` | Continued-fraction / encoding methodology only | **BLOCK** — physics constants need calibration not in verifiers |
| **T_TRANS_1** | Attention as shell operator | EMPIRICAL_ONLY | `experiments/exp_transformer.py` | Transformer architecture survey (2025+) | **DEFER** — isolate attention-head closure claim only |

### Adjacent rows (same registry band, not in TR-CL-06 queue yet)

| Theorem ID | Why excluded from bulk pair | Next scoping step |
|------------|----------------------------|-------------------|
| T_UNIVERSAL_COLLATZ | Orbit-boundary defect claim spans number theory + dynamics | Pair only after T_UNIVERSAL_NUMBER_THEORY sub-scope |
| T_TRANS_2..T_TRANS_5 | Transformer analogy band; empirical simulation only | One row per mechanism (pos-enc, LayerNorm, FFN, grokking) |
| T_VN_1, T_IDEM_2, T_SPIN_DIM | Computational architecture; not universal-closure | Route to slot families 31–40 workbook, not PEEP physics band |

---

## Per-row falsifier template (required before PEEP)

For each promoted row, fill:

1. **Claim boundary** — exact statement from registry (no physics uplift).
2. **Verifier receipt** — PASS or `pass_with_open_gaps` with honesty boundary quoted.
3. **Comparator DOI** — 2025+ peer-reviewed, claim-scoped (not umbrella math).
4. **Falsifier row** — one sentence that would refute promotion within comparator scope.
5. **Slot family** — from `SLOT_1_80_GENERALIZED_ONTOLOGY.json` (31–40 band only when physics-calibrated).

---

## EQ-REG-0010 gate status

| Metric | Value |
|--------|------:|
| TR-CL-06 rows in scope | 5 |
| Falsifier templates complete | 5 |
| Rows with scoped comparator DOI | 0 |
| Rows ready for PEEP | 0 |
| Cluster promotion | **BLOCKED** — templates complete; 0 scoped DOI |

**Honesty gate:** EQ-REG-0010 remains `BLOCKED_MORE_CONTEXT_REQUIRED` at queue level.

---

## Phase 10 — T_UNIVERSAL_CA falsifier template (documentation only)

Filled per-row template for **T_UNIVERSAL_CA** (lowest overclaim risk in TR-CL-06). No PEEP created — comparator search did not yield a claim-scoped 2025+ silent-boundary ECA closure paper.

| Field | Value |
|-------|-------|
| **1. Claim boundary** | Among the 256 elementary CA rules, the 64 **silent-boundary** rules are empirically observed to exhibit **exact 3-step partition closure at n=3** under `experiments/exp_ca_partition.py`. No claim of Wolfram-class universality or physics-band closure. |
| **2. Verifier receipt** | `experiments/exp_ca_partition.py` — **EMPIRICAL_ONLY**; automated receipt not in TR-CL-06 band. Nearest lattice-forge CA receipt lane: **PEEP-2026-018** (`PASS` 9/9) covers Rule 30 **simulation protocol** only, not silent-boundary n=3 closure. |
| **3. Comparator DOI** | **Deferred (honest gap).** Searched 2025+ CA literature: **PEEP-2026-018** external — Fast Simulation of Cellular Automata by Self-Composition, *Complex Systems* 2025, DOI `10.25088/complexsystems.34.3.259` — scoped to Rule 30 chaotic benchmark / self-composition complexity, **not** silent-boundary partition closure. arXiv `2604.00165` (2026, Rule 22 as algebraic reference for Rule 30) — support-set cardinality / symmetry deviation, **not** ECA n=3 closure witness. **No winding-number or silent-boundary n=3 comparator identified.** |
| **4. Falsifier row** | If any silent-boundary ECA in the 256-rule sweep fails 3-step closure at n=3 under the partition witness in `exp_ca_partition.py`, **T_UNIVERSAL_CA** must not be promoted beyond `EMPIRICAL_ONLY`. |
| **5. Slot family** | Workbook band **FLCR-13** (CA Prediction Surface); slot families 31–40 enumeration/residual only when receipt + comparator complete. **Not** physics-calibrated PEEP band. |

**EQ-REG-0010 row status after template:** T_UNIVERSAL_CA template **complete (documentation)**; cluster remains **BLOCKED** (0/5 rows with scoped comparator DOI).

---

## Phase 11 — T_TRANS_1 falsifier template (documentation only)

Filled per-row template for **T_TRANS_1** (attention-as-shell-operator). No PEEP created — no honest 2025+ attention-closure-only comparator identified without overclaim.

| Field | Value |
|-------|-------|
| **1. Claim boundary** | In `experiments/exp_transformer.py`, attention heads are treated as **shell operators** mapping token embeddings through query-key-value projections with empirical closure checks on toy transformer blocks. No claim of universal attention mechanism equivalence or physics-band closure. |
| **2. Verifier receipt** | `experiments/exp_transformer.py` — **EMPIRICAL_ONLY**; automated receipt not in TR-CL-06 band. Nearest method receipt lane: **PEEP-2026-018** covers Rule 30 CA simulation protocol only, **not** transformer attention closure. |
| **3. Comparator DOI** | **Deferred (honest gap).** Searched 2025+ transformer surveys: general architecture reviews (e.g. survey papers on efficient attention) scope to **compute/efficiency**, not shell-operator closure witnesses. **No claim-scoped 2025+ peer-reviewed paper constrains attention-as-shell-operator empirical closure in `exp_transformer.py`.** |
| **4. Falsifier row** | If any toy attention-head closure check in `exp_transformer.py` fails under the declared shell-operator mapping, **T_TRANS_1** must not be promoted beyond `EMPIRICAL_ONLY`. |
| **5. Slot family** | Workbook band **FLCR-31..40** (transformer analogy); slot families 31–40 enumeration/residual only when receipt + scoped comparator complete. **Not** physics-calibrated PEEP band. |

**EQ-REG-0010 row status after Phase 11:** T_TRANS_1 template **complete (documentation)**; cluster remains **BLOCKED** (0/5 rows with scoped comparator DOI).

---

## Phase 12 — T_UNIVERSAL_NUMBER_THEORY falsifier template (documentation only)

Filled per-row template for **T_UNIVERSAL_NUMBER_THEORY** (coherent number sequences). No PEEP created — no honest 2025+ sub-sequence closure comparator without splitting claims.

| Field | Value |
|-------|-------|
| **1. Claim boundary** | Fibonacci parity, Stern-Brocot tree parity, prime-gap parity, continued-fraction parity of √2, and Liouville partial sums exhibit **exact n=3 SU(3) Weyl closure at length 4096** under `experiments/run_all.py` number-theory section. No claim of universal number-theoretic closure or physics-band uplift. |
| **2. Verifier receipt** | `experiments/run_all.py` (number theory section) — **EMPIRICAL_ONLY**; no automated receipt in TR-CL-06 band. Registry status: PROVEN empirically across tested sequences only. |
| **3. Comparator DOI** | **Deferred (honest gap).** Searched 2025+ sequence-closure literature: Stern-Brocot / Fibonacci path work (e.g. arXiv `2205.00565` parity partition, 2022) and SB-tree minimal-path characterizations scope to **rational parity / continued fractions**, not SU(3) Weyl closure witnesses at n=3. **No 2025+ peer-reviewed paper constrains the bundled five-sequence empirical closure claim in `run_all.py`.** Sub-claims (Fibonacci, Stern, prime-gap, √2 CF, Liouville) require **per-sequence** comparator rows before cluster pairing. |
| **4. Falsifier row** | If any listed sub-sequence fails exact n=3 Weyl closure at length 4096 under the witness in `run_all.py`, **T_UNIVERSAL_NUMBER_THEORY** must not be promoted beyond `EMPIRICAL_ONLY` for that sub-sequence. |
| **5. Slot family** | Workbook band **FLCR-01..12** (enumeration/residual); slot families 31–40 only when receipt + per-sequence comparator complete. **Not** physics-calibrated PEEP band. |

**EQ-REG-0010 row status after Phase 12:** T_UNIVERSAL_NUMBER_THEORY template **complete (documentation)**; row remains **DEFER** (split per sub-sequence).

---

## Phase 13 — T_UNIVERSAL_CMB falsifier template (documentation only)

Filled per-row template for **T_UNIVERSAL_CMB** (cumulative Planck TT closure). No PEEP created — no unit-bearing 2025+ CMB comparator scoped to bijective closure claim.

| Field | Value |
|-------|-------|
| **1. Claim boundary** | Partial sums of the Planck 2018 CMB TT power spectrum close exactly under the bijective construction in `experiments/exp_relational_qubit.py` CMB section (`data/planck_TT_R3.txt`). No claim of cosmological parameter inference or physics-band closure beyond the tested cumulative transform. |
| **2. Verifier receipt** | `experiments/exp_relational_qubit.py` (CMB section) — **EMPIRICAL_ONLY**; uses on-disk `data/planck_TT_R3.txt`. No external calibration receipt in TR-CL-06 band. |
| **3. Comparator DOI** | **Deferred (honest gap).** Nearest methodology reference: Planck Collaboration 2018 legacy likelihood — *Astronomy & Astrophysics* 641, A5 (2020), DOI `10.1051/0004-6361/201833910` — scopes to **CMB power-spectrum likelihood / foreground modeling**, not bijective cumulative-closure under the relational-qubit construction. **No 2025+ peer-reviewed paper constrains the exact cumulative-closure witness in `exp_relational_qubit.py`.** Unit-bearing Planck comparator rows with uncertainty propagation required before promotion. |
| **4. Falsifier row** | If cumulative partial sums of Planck TT under the bijective witness in `exp_relational_qubit.py` fail exact closure at any tested multipole band, **T_UNIVERSAL_CMB** must not be promoted beyond `EMPIRICAL_ONLY`. |
| **5. Slot family** | Workbook band **FLCR-41..50** (physics redefinition); slot families 31–40 enumeration/residual only when receipt + unit-bearing comparator complete. **Not** promotable without calibration rows. |

**EQ-REG-0010 row status after Phase 13:** T_UNIVERSAL_CMB template **complete (documentation)**; row remains **DEFER** (unit-bearing Planck comparator).

---

## Phase 14 — T_INV_1 falsifier template (documentation only)

Filled per-row template for **T_INV_1** (physical constants as topological invariants). No PEEP created — physics constants require calibration not present in verifiers.

| Field | Value |
|-------|-------|
| **1. Claim boundary** | Constants `e`, `φ`, and `h` are `CLASSICAL` invariants under relational-qubit continued-fraction parity encoding; `π` does not close; `α` achieves `INVERTED` signature under decimal encoding — all per `experiments/exp_physical_constants.py`. No claim that these encodings establish physical measurement or SI calibration. |
| **2. Verifier receipt** | `experiments/exp_physical_constants.py` — **EMPIRICAL_OVERCLAIM_RISK**; registry status PROVEN empirically on encoding tests only. No unit-bearing calibration receipt. |
| **3. Comparator DOI** | **Blocked (honest gap).** Searched 2025+ metrology: fine-structure reviews (e.g. *Measurement Techniques* 2025, DOI `10.1007/s11018-025-02433-2`) scope to **α measurement methodology**, not continued-fraction parity closure in `exp_physical_constants.py`. Planck/SI constant papers scope to **definitions**, not the registry's encoding-closure witness. **No claim-scoped 2025+ comparator constrains e/φ/h CLASSICAL closure under the tested encodings.** |
| **4. Falsifier row** | If any tested encoding of `e`, `φ`, or `h` fails `CLASSICAL` closure under the relational-qubit witness in `exp_physical_constants.py`, **T_INV_1** must not be promoted; if promotion is attempted without unit-bearing calibration rows, the row stays **BLOCK**. |
| **5. Slot family** | Workbook band **FLCR-41..50** (physics redefinition); requires explicit calibration protocol before any physics-calibrated PEEP. **BLOCK** until calibration comparator attached. |

**EQ-REG-0010 row status after Phase 14:** T_INV_1 template **complete (documentation)**; row remains **BLOCK** (calibration required).

---

## Cycle 4 — TR-CL-06 row summary (2026-06-30)

| Theorem ID | Falsifier template | Scoped 2025+ DOI | Action |
|------------|-------------------|------------------|--------|
| T_UNIVERSAL_CA | Complete | None | **DEFER** |
| T_TRANS_1 | Complete | None | **DEFER** |
| T_UNIVERSAL_NUMBER_THEORY | Complete | None | **DEFER** — split per sub-sequence |
| T_UNIVERSAL_CMB | Complete | None | **DEFER** — unit-bearing Planck comparator |
| T_INV_1 | Complete | None | **BLOCK** — calibration required |

| Metric | Value |
|--------|------:|
| Falsifier templates complete | **5/5** |
| Rows with scoped comparator DOI | **0/5** |
| Rows ready for PEEP | **0** |
| **Advanced this lane** (templates newly filled Cycle 4) | **3** (Phases 12–14) |
| **DEFER** rows | **4** |
| **BLOCK** rows | **1** |

**Cluster gate:** EQ-REG-0010 remains `BLOCKED_MORE_CONTEXT_REQUIRED` (0/5 scoped DOI). No cluster-level PEEP.

---

## Cycle 4 — T_UNIVERSAL_NUMBER_THEORY falsifier template (documentation only)

Filled per-row template for **T_UNIVERSAL_NUMBER_THEORY**. No PEEP created — sequence-closure literature is not claim-scoped to Fibonacci/Stern/prime-gap parity sub-claims without per-sequence split.

| Field | Value |
|-------|-------|
| **1. Claim boundary** | In `experiments/run_all.py` (number-theory band), Fibonacci parity, Stern diatomic parity, and prime-gap parity sequences are empirically observed to exhibit **closure patterns** under declared Weyl-group / parity witnesses. No claim of universal number-theoretic closure or physics-band promotion. |
| **2. Verifier receipt** | `experiments/run_all.py` — **EMPIRICAL_ONLY**; no automated receipt in TR-CL-06 band. Sub-sequences (Fibonacci, Stern, prime-gap) are bundled; each requires independent scoping before pairing. |
| **3. Comparator DOI** | **Deferred (honest gap).** Searched 2025+ sequence-closure / Weyl-group literature: general combinatorial number theory surveys scope to **unrelated parity structures**, not the three bundled sub-sequences in the registry row. **No claim-scoped 2025+ peer-reviewed paper constrains all three parity-closure witnesses jointly.** Per Phase 9 action: split per sub-sequence before any pairing attempt. |
| **4. Falsifier row** | If any Fibonacci, Stern, or prime-gap parity closure check in `run_all.py` fails under its declared witness, **T_UNIVERSAL_NUMBER_THEORY** must not be promoted beyond `EMPIRICAL_ONLY` for that sub-sequence. |
| **5. Slot family** | Workbook band **FLCR-13..20** (number-theory enumeration); slot families 31–40 only when receipt + per-sub-sequence comparator complete. **Not** physics-calibrated PEEP band. |

**EQ-REG-0010 row status:** T_UNIVERSAL_NUMBER_THEORY template **complete (documentation)**; cluster remains **BLOCKED** (0/5 scoped comparator DOI).

---

## Cycle 4 — T_UNIVERSAL_CMB falsifier template (documentation only)

Filled per-row template for **T_UNIVERSAL_CMB** (Cumulative Planck TT closure). No PEEP created — Planck power-spectrum methodology papers require unit-bearing comparator rows not yet attached.

| Field | Value |
|-------|-------|
| **1. Claim boundary** | In `experiments/exp_relational_qubit.py`, cumulative Planck TT power-spectrum residuals are empirically checked for closure under declared relational-qubit witnesses. No claim of cosmological parameter inference or physics-band CMB closure beyond the scripted residual check. |
| **2. Verifier receipt** | `experiments/exp_relational_qubit.py` — **EMPIRICAL_ONLY**; automated receipt not in TR-CL-06 band. Nearest receipt lanes cover relational-qubit construction, **not** Planck TT unit-bearing calibration. |
| **3. Comparator DOI** | **Deferred (honest gap).** Searched 2025+ CMB methodology: Planck 2018/2020 legacy releases and 2025+ reanalysis papers scope to **cosmological parameter fits**, not the specific cumulative-TT closure witness in `exp_relational_qubit.py`. **No unit-bearing Planck comparator rows attached** matching the registry's residual-closure claim. Requires explicit TT residual table with calibration-bound units before pairing. |
| **4. Falsifier row** | If cumulative Planck TT closure in `exp_relational_qubit.py` fails under the declared relational-qubit witness at any checked multipole band, **T_UNIVERSAL_CMB** must not be promoted beyond `EMPIRICAL_ONLY`. |
| **5. Slot family** | Workbook band **FLCR-20..30** (cosmology / relational qubit); slot families 31–40 only when receipt + unit-bearing Planck comparator rows complete. **Not** physics-calibrated PEEP band without calibration tables. |

**EQ-REG-0010 row status:** T_UNIVERSAL_CMB template **complete (documentation)**; cluster remains **BLOCKED** (0/5 scoped comparator DOI).

---

## Cycle 4 — T_INV_1 falsifier template (documentation only)

Filled per-row template for **T_INV_1** (e, φ, h as CLASSICAL invariants). Cluster **BLOCK** row — physics constants lack verifier calibration; template documents falsifier for honesty gate completeness.

| Field | Value |
|-------|-------|
| **1. Claim boundary** | In `experiments/exp_physical_constants.py`, e, φ (golden ratio), and h are treated as **CLASSICAL invariant encodings** under continued-fraction / symbolic-constant witnesses. Tag: **EMPIRICAL_OVERCLAIM_RISK** — encoding methodology must not be uplifted to measured-constant equivalence without calibration. |
| **2. Verifier receipt** | `experiments/exp_physical_constants.py` — **EMPIRICAL_OVERCLAIM_RISK**; verifiers encode symbolic constants but **do not supply SI-traceable calibration** for e or h. φ is mathematical, not a measured physics constant. |
| **3. Comparator DOI** | **Blocked (no honest pairing).** Searched 2025+ continued-fraction / encoding methodology and fine-structure reviews: e.g. fine-structure review DOI `10.1007/s11018-025-02433-2` scopes to **α metrology**, not the bundled e/φ/h CLASSICAL encoding claim. **No 2025+ peer-reviewed paper provides claim-scoped calibration for all three invariants as CLASSICAL encodings in `exp_physical_constants.py`.** |
| **4. Falsifier row** | If any e, φ, or h encoding check in `exp_physical_constants.py` fails under its declared continued-fraction witness, or if promotion is attempted without SI-traceable calibration for e and h, **T_INV_1** must remain **BLOCKED** and must not enter PEEP physics band. |
| **5. Slot family** | **Blocked** from slot families 31–40 physics-calibrated PEEP band until per-constant calibration comparators exist. Route encoding-only claims to FLCR workbook enumeration, not ASSEMBLE. |

**EQ-REG-0010 row status:** T_INV_1 template **complete (documentation)**; row remains **BLOCK**; cluster remains **BLOCKED** (0/5 scoped comparator DOI).

---

## Cycle 4 cluster summary

| Theorem ID | Falsifier template | Scoped comparator DOI | Row gate |
|------------|-------------------|----------------------|----------|
| T_UNIVERSAL_CA | Complete (Phase 10) | Deferred | DEFER |
| T_TRANS_1 | Complete (Phase 11) | Deferred | DEFER |
| T_UNIVERSAL_NUMBER_THEORY | **Complete (Cycle 4)** | Deferred | DEFER |
| T_UNIVERSAL_CMB | **Complete (Cycle 4)** | Deferred | DEFER |
| T_INV_1 | **Complete (Cycle 4)** | Blocked | BLOCK |

| Metric | Value |
|--------|------:|
| TR-CL-06 rows in scope | 5 |
| Rows with falsifier template complete | **5** |
| Rows with scoped comparator DOI | **0** |
| Rows ready for PEEP | **0** |
| Cluster promotion | **BLOCKED** until ≥1 row completes comparator DOI + pairing |
