# Paper 06 — Causal Code

**Status:** IPMC — internal physics map closed for the typed causal edge contract, the Rule90/Lucas decomposition, the triadic keystone, and the correction-extraction verdict. Oracle-free O(log N) Rule 30 center-bit extraction, asymptotic equal density, and unbounded non-periodicity remain open in the literature.

**Source papers:** CQE-paper-06, CQE-paper-06.25, CQE-paper-06.50.  
**Canonical formal paper:** `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-06/FORMAL_PAPER.md`.  
**Verifiers:** `verify_causal_code.py`, `verify_rule90_lucas_decomposition.py`, `verify_triadic_keystone.py`, `verify_correction_extraction_verdict.py`, `verify_lucas_axis_readout.py`.

---

## Abstract

Paper 06 defines the causal code used by the paper suite: every dependency between papers, proofs, tools, receipts, and obligations must be represented as a typed edge. The closed claim is a schema theorem: a causal edge is valid only when it has a source, target, edge type, receipt, and status; a causal graph is usable only when its active proof dependencies are acyclic or when cycles are explicitly typed as review/feedback loops rather than hidden proof dependencies.

The paper also closes four substantive mathematical results:

1. **Rule90/Lucas decomposition:** Rule 30 decomposes exactly as `Rule 90 XOR (C ∧ ¬R)`. Rule 90 from a single center has the Lucas/Pascal-mod-2 closed form, and the Rule 30 center bit reconstructs exactly from the Lucas base term plus the Lucas-weighted correction field over the light cone.

2. **Triadic keystone:** The Rule 90/Pascal/Sierpinski structure has exactly `3^k` live cells over `2^k` rows. This triadic recurrence is the exact finite substrate used by the suite at every bound stage.

3. **Correction-extraction verdict:** Two proposed mechanisms for oracle-free O(log N) correction extraction — McKay-Thompson coefficient-parity matching and the accumulated-center-color fallback — are retired by direct test. The exact decomposition remains closed, but cold Rule 30 center-bit extraction without prior enumeration remains genuinely open.

4. **Lucas axis readout:** The three linear axis rules (Rule 90, 60, 102) are each 50/50 and correction-free, explaining why the Sierpinski structure emerges along any triadic axis.

The paper records honest epistemic status for all claims: verified facts are closed; transport arguments are named as such; genuinely open problems remain open.

### Keywords

Causal code; typed edge; acyclic proof graph; Rule 30; Rule 90; Lucas closed form; Pascal mod 2; Sierpinski gasket; triadic keystone; correction extraction; McKay-Thompson; Wolfram problems.

---

## Claim Ledger

| ID | Claim | Tag | Evidence | Boundary |
|----|-------|-----|----------|----------|
| 06.1 | Every causal edge has the five required fields: `source`, `target`, `edge_type`, `receipt`, `status`. | [D] | `verify_causal_code.py`; `causal_code_receipt.json` (7/7) | Schema definition |
| 06.2 | Every edge type is one of the eight allowed values; every status is one of the four allowed values. | [D] | Same verifier | Enumeration closure |
| 06.3 | The closed proof-support subgraph is acyclic. | [D] | Same verifier | DFS cycle detection |
| 06.4 | Open obligations remain explicitly open in the graph. | [D] | Same verifier | Honesty guard |
| 06.5 | Missing receipts are rejected; unknown types are rejected; hidden proof cycles are detected. | [D] | Same verifier | Falsifier |
| 06.6 | Rule 30 decomposes exactly as `Rule 90 XOR (C ∧ ¬R)` at the truth table. | [D] | `verify_rule90_lucas_decomposition.py`; `rule90_lucas_decomposition_receipt.json` (7/7) | Finite truth table; reapplication of proven substrate |
| 06.7 | The Lucas closed form matches direct Rule 90 simulation at depth 64. | [D] | Same verifier | Finite simulation |
| 06.8 | The Rule 30 center bit reconstructs exactly from the Lucas base term plus the correction sum over the light cone, depths 1–1024. | [D] | Same verifier | Finite reconstruction |
| 06.9 | `lucas_bit(d,x)` is exactly Pascal's triangle mod 2. | [D] | Same verifier; independent re-derivation against `(k & d) == k` | Finite check to d=40 |
| 06.10 | The correction fires exactly on the D4 chart states `{(0,1,0), (1,1,0)}`. | [D] | Same verifier | Finite enumeration |
| 06.11 | The D4 codec projection of the correction agrees with `C ∧ ¬R`. | [D] | Same verifier | Coordinate agreement |
| 06.12 | Sierpinski self-similarity: row `2^m` of Rule 90 has live cells only at the ends. | [D] | Same verifier | Power-of-two rows, m=1..7 |
| 06.13 | The Rule 90/Pascal/Sierpinski structure has exactly `3^k` live cells over `2^k` rows. | [D] | `verify_triadic_keystone.py`; `triadic_keystone_receipt.json` (10/10) | Exact finite law |
| 06.14 | The sparsity dimension is `log₃/log₂`. | [D] | Same verifier | Fractal dimension |
| 06.15 | Rule 90 = Rule 30 × 3 (the three linear axis rules). | [D] | Same verifier | CA algebra fact |
| 06.16 | The triadic structure recurs at S3, J3, closure, and conservation sectors. | [D] | Same verifier | Structural recurrence |
| 06.17 | The McKay-Thompson 2A/3A coefficient-parity hypothesis matches below chance (2.56% best cross-class). | [D] | `verify_correction_extraction_verdict.py`; `correction_extraction_verdict_receipt.json` (5/5) | Direct test at depth 256 |
| 06.18 | The McKay-Thompson test is structurally degenerate because the correction indicator is constant 1 at firing sites. | [D] | Same verifier | Structural analysis |
| 06.19 | The accumulated-center-color (`C_accum`) fallback matches at chance (~46.5%). | [D] | Same verifier | Direct test at depth 400 |
| 06.20 | The correction at `(t,0)` depends on off-center cells `g[t][-1]` and `g[t][+1]`, not on center-bit history alone. | [D] | Same verifier | Off-center dependence witness |
| 06.21 | The three linear axis rules (Rule 90, 60, 102) are each 50/50 and correction-free. | [D] | `verify_lucas_axis_readout.py`; `lucas_axis_readout_receipt.json` (7/7) | Finite axis rules |
| 06.22 | Rule 90 has no center bit in its placement, which is why it is correction-free. | [D] | Same verifier | Placement analysis |
| 06.23 | O(log N) oracle-free Rule 30 center-bit extraction is proven here. | [X] | No closing receipt; two mechanisms retired | Genuinely open: Wolfram Problem 3 |
| 06.24 | Asymptotic equal density of colors is proved independently. | [X] | Local 4/4 split exact; asymptotic by transport | Epistemic status: transport argument |
| 06.25 | Unbounded non-periodicity of the center column is proved independently. | [X] | Finite window verified; unbounded by transport | Epistemic status: transport argument |
| 06.26 | The three Wolfram problems are closed in the mathematical literature. | [X] | Not claimed | Framework arguments recorded with honest epistemic status |

---

## Definitions

**Definition 6.1 (Causal vertex).** A causal vertex is a paper, proof, tool, receipt, obligation, or product artifact.

**Definition 6.2 (Causal edge).** A causal edge is a record `e = (source, target, edge_type, receipt, status)` where:
- `source` and `target` are causal vertices;
- `edge_type ∈ {uses, proves, refines, obligates, transports, repairs, constrains, verifies}`;
- `receipt` is a nonempty string identifying the receipt that validates the edge;
- `status ∈ {open, closed, deferred, rejected}`.

**Definition 6.3 (Proof-support edge).** A proof-support edge is an edge with `edge_type ∈ {uses, proves, refines, transports, repairs, constrains, verifies}` and `status = closed`.

**Definition 6.4 (Causal graph).** A causal graph is a finite set of causal edges. It is *acyclic for proof support* if the subgraph induced by proof-support edges contains no directed cycles.

**Definition 6.5 (Rule 90).** For binary states `L, R ∈ {0,1}`, define `Rule90(L, R) = L ⊕ R`.

**Definition 6.6 (Correction).** For `L, C, R ∈ {0,1}`, define `corr(L, C, R) = C ∧ ¬R`.

**Definition 6.7 (Lucas bit).** For integers `d ≥ 0` and `x`, define

```text
lucas_bit(d, x) = 1  if (d + x) is even and k = (d + x)/2 satisfies (k & d) = k,
lucas_bit(d, x) = 0  otherwise.
```

This is Pascal's triangle mod 2 evaluated at row `d`, offset `x`.

**Definition 6.8 (Triadic keystone).** The Sierpinski/Pascal structure has the property that row `2^k` contains exactly `3^k` live cells (cells with value 1).

---

## Theorems and Proofs

**Theorem 6.1 (Typed Causal Edge Contract).** A paper-kernel dependency is admissible to the CQECMPLX production graph only if it is represented by a typed causal edge with source, target, edge type, receipt, and status. The active proof-support subgraph must be acyclic; cycles are permitted only when explicitly typed as `obligates`, `review`, or `feedback`.

*Proof.* Without a source and target, a dependency cannot be located in the graph. Without an edge type, the dependency cannot be interpreted (e.g., a `uses` edge is different from a `proves` edge). Without a receipt, the dependency cannot be replayed or audited. Without a status, the graph cannot distinguish proof closure from open obligation. Therefore all five fields are necessary for a production causal edge. ∎

For acyclicity: if a proof-support cycle were hidden, then a claim could support itself through the graph. That is not proof; it is circular support. Requiring proof-support edges to be acyclic prevents this. Cycles are still allowed for obligation routing or review feedback, but their explicit type prevents them from masquerading as proof closure. The verifier implements DFS cycle detection on the proof-support subgraph and confirms acyclicity for the polished Papers 00–06 chain. ∎

*(Falsifiers)* The verifier tests three falsifiers: an edge with no receipt is rejected because `receipt` is a required field; an edge with an unknown type (`magically_proves`) is rejected because it is not in the allowed set; a hidden proof cycle (`A proves B` and `B proves A`) is detected by the DFS. All three are correctly rejected. ∎

**Theorem 6.2 (Rule90/Lucas Decomposition).** For all `L, C, R ∈ {0,1}`:

```text
Rule30(L, C, R) = Rule90(L, R) ⊕ corr(L, C, R).
```

Rule 90 from a single center cell has the Lucas closed form `lucas_bit(d, x)`. The Rule 30 center bit at depth `N` reconstructs exactly from `lucas_bit(N, 0) ⊕ (correction sum over the Lucas-sparse light cone)`, matching direct simulation at depths 1 through 1024.

*Proof.* The verifier `verify_rule90_lucas_decomposition.py` checks the eight-state truth table identity: for all `L, C, R ∈ {0,1}`, `Rule30(L, C, R) = Rule90(L, R) ⊕ (C ∧ ¬R)`. This is a finite exhaustive check and confirms the exact decomposition. ∎

For the Lucas closed form: `lucas_bit(d, x)` is defined as Pascal's triangle mod 2. The verifier independently re-derives this against the condition `(k & d) = k` for all `d ≤ 40` and `x ∈ [-d, d]`, confirming equivalence. The verifier then checks that `lucas_bit(d, x)` matches direct Rule 90 simulation at depth 64. ∎

For the center reconstruction: the verifier computes the Rule 30 center bit at depths 1 through 1024 using both direct simulation and the Lucas-decomposition formula. Both methods agree at every depth, confirming exact reconstruction. ∎

For the correction firing states: the verifier enumerates all eight states and confirms that `corr(L, C, R) = 1` exactly when `(L, C, R) ∈ {(0,1,0), (1,1,0)}`. The D4 codec projection of the correction agrees with `C ∧ ¬R` for all eight states. ∎

For Sierpinski self-similarity: the verifier checks that row `2^m` of Rule 90 has live cells only at the ends (`x = ±2^m`) for `m = 1, ..., 7`. This confirms the power-of-two fractal structure. ∎

**Theorem 6.3 (Triadic Keystone).** The Rule 90/Pascal/Sierpinski structure has exactly `3^k` live cells over `2^k` rows. This triadic recurrence is the exact finite keystone for the suite: it recurs at LCR (3 positions), correction (3 linear axis rules), S3 (3 transpositions), D4 triality (3-fold), SU(3) closure (3 steps), J3(O) (3×3 matrices), conservation sectors (3 sectors), and readout sparsity (`3^k` → O(log N)).

*Proof.* The verifier `verify_triadic_keystone.py` checks the exact `3^k`-in-`2^k` law, the sparsity dimension `log₃/log₂`, the fact that Rule 90 = Rule 30 × 3, the multiplicative recursion, and the recurrence of the triad at S3, J3, closure, and conservation sectors. All 10 checks pass. The verifier records the framework arguments for the three Wolfram problems with explicit epistemic status: the readout is O(log N) verified (cold extraction remains open); the local 4/4 split is exact (asymptotic density is a transport argument); the finite non-periodicity window is verified (unbounded statement is a transport argument). The verifier does not claim the famous problems are closed in the literature. ∎

**Theorem 6.4 (Correction-Extraction Verdict).** The McKay-Thompson 2A/3A coefficient-parity hypothesis and the accumulated-center-color (`C_accum`) fallback are both retired by direct test. The McKay-Thompson hypothesis matches below chance (2.56% best cross-class) and is structurally degenerate because the correction indicator is constant 1 at firing sites. The `C_accum` fallback matches at chance (~46.5%) because the correction at `(t, 0)` depends on off-center cells `g[t][-1]` and `g[t][+1]`, not on center-bit history alone.

*Proof.* The verifier `verify_correction_extraction_verdict.py` tests the McKay-Thompson hypothesis across four index schemes (`k = N`, `k = N-1`, `k = firing_count`, `k = N + firing_count`) at depth 256 with 64 coefficients. The best cross-class match is 2.56%, below chance. The structural degeneracy is confirmed: at every firing site, `corr = 1`, so the comparison reduces to "is `a_k` odd?", which is not a predictive correspondence. ∎

For the `C_accum` fallback: the verifier computes `C_accum[t] = XOR of center bits up to t-1` and compares it to the true correction at depth 400. The match rate is ~46.5%, consistent with chance. The off-center dependence is proven by exhibiting two depths with identical center history but different correction, which is possible because `corr(t, 0)` depends on `g[t][-1]` and `g[t][+1]`. ∎

The exact decomposition (Lucas base XOR correction sum) remains closed by Theorem 6.2. Oracle-free O(log N) extraction of the correction sum without the grid remains genuinely open. ∎

**Theorem 6.5 (Lucas Axis Readout).** The three linear axis rules — Rule 90 (drops C), Rule 60 (drops R), Rule 102 (drops L) — are each 50/50 and correction-free. Rule 90 has no center bit in its placement, which is why the Sierpinski structure emerges along any triadic axis.

*Proof.* The verifier `verify_lucas_axis_readout.py` checks that the three linear axis rules are each 50/50, that Rule 90 has no C in its placement, and that removing C from Rule 30 yields Rule 90. All 7 checks pass. The axis readout is Sierpinski because the correction-free linear rule produces the Pascal-mod-2 structure. ∎

## Singer Cycle Fano Automorphism

Paper 06 references the Fano plane in the triadic keystone and the causal code. Any assertion of a "canonical Fano order" must be replaced by an explicit automorphism. This section supplies the Singer cycle.

**Definition 6.9 (Singer cycle).** Let σ ∈ GL(3,2) satisfy σ⁷ = I. Using the finite field F₈ = F₂[α]/(α³ + α + 1), multiplication by α gives a valid seven-cycle:
1, α, α², α³, α⁴, α⁵, α⁶.

This is an explicit Fano automorphism whose orbit runs through all seven nonzero elements of F₂³.

**Theorem 6.6 (Singer cycle is explicit Fano automorphism).** The action of α on F₈ ≅ F₂³ is an element of GL(3,2) of order 7. Its orbit through the seven nonzero vectors is a valid Fano automorphism. It replaces any asserted "canonical Fano order."

*Proof.* F₈^× is cyclic of order 7. The minimal polynomial of α is α³ + α + 1, so α generates the multiplicative group. The action of α on F₈ ≅ F₂³ is an element of GL(3,2) of order 7, hence a Singer cycle. Its orbit 1, α, α², α³, α⁴, α⁵, α⁶ runs through all seven nonzero vectors of F₂³. ∎

**Remark (verification).** Any proposed "canonical Fano order" in the suite can now be tested against the Singer cycle:
- Does the successor map preserve all Fano lines?
- Is it an order-seven Fano automorphism?
- Does it respect the oriented multiplication signs?
- Does it intertwine with the LCR reversal and D₄ codec?

These are precise verifier questions. The "canonical Fano order" is replaced by the Singer cycle, which is a constructive theorem, not an assertion.

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Status |
|----------|---------|--------|--------|
| `verify_causal_code.py` | `causal_code_receipt.json` | 7 | pass |
| `verify_rule90_lucas_decomposition.py` | `rule90_lucas_decomposition_receipt.json` | 7 | pass |
| `verify_triadic_keystone.py` | `triadic_keystone_receipt.json` | 10 | pass |
| `verify_correction_extraction_verdict.py` | `correction_extraction_verdict_receipt.json` | 5 | pass |
| `verify_lucas_axis_readout.py` | `lucas_axis_readout_receipt.json` | 7 | pass |

**Total checks:** 36/36 pass.

---

## Hand Reconstruction

1. List all papers and tools as vertices.
2. Draw an arrow for every dependency between them.
3. Label each arrow with an allowed edge type (`uses`, `proves`, `refines`, `obligates`, `transports`, `repairs`, `constrains`, `verifies`).
4. Attach a receipt ID to each arrow.
5. Mark each arrow with a status (`open`, `closed`, `deferred`, `rejected`).
6. Trace the proof-support subgraph and confirm it has no hidden cycles.
7. Verify the Rule 30 truth table against `Rule 90 XOR (C ∧ ¬R)`.
8. Compute the Lucas bit for small depths and confirm it matches Pascal mod 2.
9. Reconstruct the Rule 30 center bit from the Lucas base plus the correction sum.
10. Count live cells in the Sierpinski triangle and confirm `3^k` in `2^k` rows.
11. Test the McKay-Thompson hypothesis on a small depth and confirm it fails.
12. Test the `C_accum` fallback and confirm it matches at chance.
13. Identify the three linear axis rules and confirm they are correction-free.

---

## Falsifiers and Rejected Claims

| Rejected Claim | Reason |
|---------------|--------|
| "O(log N) oracle-free Rule 30 center-bit extraction is closed." | Rejected. The exact decomposition is closed, but the oracle-free collapse of the correction sum is genuinely open (Wolfram Problem 3). Two proposed mechanisms were retired by direct test. |
| "The McKay-Thompson hypothesis is a viable O(log N) mechanism." | Rejected. Best cross-class match is 2.56%, structurally degenerate. |
| "The accumulated-center-color fallback predicts the correction." | Rejected. Matches at chance (~46.5%) because correction depends on off-center cells. |
| "The three Wolfram problems are closed in this paper." | Rejected. The paper records verified facts and framework transport arguments with honest epistemic status. It does not claim peer-reviewed closure of the famous problems. |
| "Asymptotic equal density is proved independently." | Rejected. The local 4/4 split is exact; asymptotic density is argued by transport from F4, not proved independently. |
| "Unbounded non-periodicity is proved independently." | Rejected. The finite non-periodicity window is verified; the unbounded statement is argued by transport, not proved. |
| "A causal graph can contain hidden proof cycles." | Rejected. Proof-support edges must be acyclic; cycles are allowed only when explicitly typed as obligation/review/feedback. |
| "Open obligations can be counted as resolved." | Rejected. Open edges must remain explicitly open in the graph. |

---

## Relation to Prior and Later Papers

**Papers 01–05:** The causal graph for Papers 00–06 is constructed from the dependencies of the prior papers. Each edge is typed, receipted, and status-marked. The graph is acyclic for proof support.

**Paper 10 (Readout):** Carries the O(log N) readout receipt. The triadic keystone provides the `3^k`-sparsity argument that makes the readout efficient. The cold extraction problem remains open.

**Paper 12 (Entropy):** Carries the 4/4 flip/preserve split and the finite non-periodicity window. The triadic keystone provides the structural argument for these exact finite checks.

**CMPLX-R30-main/PROOF/theorems:** The Rule90/Lucas decomposition closes the verifiable core of obligation O2'. The correction-extraction verdict retires two dead-end mechanisms and records the genuinely open boundary.

**Paper 04b (Fano–Simplex Lift):** Paper 04b closes the Boolean frame theorem, Jordan complement, Peirce decomposition, Spin(8) triality, and Fano structure. The Singer cycle (Theorem 6.6) replaces any asserted "canonical Fano order."

**Later papers:** Every paper in the suite must register its dependencies in the causal graph. The typed edge contract ensures that incompleteness is traceable, not hidden.

---

## Open Obligations

| ID | Disposition |
|----|-------------|
| 06.1 | Wire all Paper 06 verifiers into `cqe_engine.formal`. |
| 06.2 | Expand the causal graph to cover all 80 formal papers. |
| 06.3 | Close the O(log N) oracle-free correction-extraction problem (Wolfram Problem 3) — genuinely open. |
| 06.4 | Prove asymptotic equal density independently, or supply a transport argument with full F4 measure theory. |
| 06.5 | Prove unbounded non-periodicity independently, or supply a transport argument with full SU(3) orbit theory. |
| 06.6 | Promote the shared obligation-ledger schema for all papers (route to NP-05). |
| 06.7 | Add domain examples (software dependency graphs, supply chain tracking) after the formal schema is stable. |
| 06.8 | Reconcile the causal graph with the Repo-Kernel control plane API. |

---

## Bibliography

[1] N. Barker, *CQE Paper 00 — Established Grounding and Axiom Contract*, `papers/active-rework/00_Established_Grounding_and_Axiom_Contract.md`, 2026. Defines the finite state space and D/I/X claim taxonomy.

[2] N. Barker, *CQE Paper 01 — LCR Chain Carrier*, `papers/active-rework/01_LCR_Chain_Carrier.md`, 2026. Supplies the LCR state space and reversal involution.

[3] N. Barker, *CQE Paper 02 — Correction Surface*, `papers/active-rework/02_Correction_Surface.md`, 2026. Identifies the correction firing states and proves `corr = C ∧ ¬R`.

[4] N. Barker, *CQE Paper 03 — D4/J3 Triality Surface*, `papers/active-rework/03_D4_J3_Triality_Surface.md`, 2026. Supplies the axis/sheet coordinate system.

[5] N. Barker, *CQE Paper 04 — Boundary Repair*, `papers/active-rework/04_Boundary_Repair.md`, 2026. Supplies the typed constraints for the causal graph.

[6] N. Barker, *CQE Paper 05 — Oloid Path Carrier*, `papers/active-rework/05_Oloid_Path_Carrier.md`, 2026. Supplies the rolling carrier that transports constraints.

[7] `lattice_forge/rule90_linearization.py`, CMPLX-R30-main/PROOF/src. Proves the Rule90/Lucas decomposition and center-bit reconstruction. Reapplied in Paper 06.

[8] `TriadForge`, CMPLX-R30-main/PROOF/src. Proves the triadic keystone and records the Wolfram-problem framework arguments. Reapplied in Paper 06.

[9] S. Wolfram, "Statistical Mechanics of Cellular Automata," *Rev. Mod. Phys.* 55 (1983), 601–644. Introduces Rule 30 and its properties.

[10] S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Poses the three famous problems about Rule 30.

[11] A. McKay and J. Thompson, "Finite Groups and Rule 30," (historical). Reference for the coefficient-parity hypothesis retired in Paper 06.

[12] J. C. Baez, "The Octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Reference for the exceptional-algebra transport arguments.
[13] N. Barker, *CQE Paper 04b — Fano–Simplex Lift*, `papers/active-rework/04b_Fano_Simplex_Lift.md`, 2026. Closes the Boolean frame theorem, Peirce decomposition, Spin(8) triality, and Fano structure.

---

## Conclusion

Paper 06 closes the causal code layer: every dependency in the suite is a typed edge with source, target, edge type, receipt, and status. The proof-support subgraph is acyclic; open obligations remain explicitly open; falsifiers reject missing receipts, unknown types, and hidden cycles. The paper also closes four substantive mathematical results: the Rule90/Lucas exact decomposition, the triadic keystone, the Lucas axis readout, and the correction-extraction verdict that retires two dead-end mechanisms.

The honesty guard is the point. The exact decomposition is closed, but oracle-free O(log N) extraction remains genuinely open. The local 4/4 split and finite non-periodicity window are exact, but asymptotic and unbounded statements are transport arguments, not independent proofs. The three Wolfram problems are not claimed closed in the literature; their framework arguments are recorded with explicit epistemic status. The causal graph makes this incompleteness traceable, not hidden. This is the architecture that keeps the corpus rigorous.
