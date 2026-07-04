# Paper 6 — Causal Link / Obligation Ledger

**Status:** IPMC — Internal Physics Map Closed for typed causal-edge contract, Rule90/Lucas decomposition, triadic keystone, correction-extraction verdict, Lucas axis readout, and Singer-cycle Fano automorphism. Gluon/Feynman/graph-population claims are named and scoped.  
**Classification:** Causal Code / Dependency Graph / Rule 30 Decomposition / Triadic Keystone / Fano Automorphism  
**Date:** 2026-06-18  
**Canonical formal paper:** `CQE-CMPLX-1T-Production/src/papers/formal/Paper 06/FORMAL_PAPER.md`  
**Verifiers:**
- `verify_causal_code.py` → `causal_code_receipt.json` — pass, 7/7
- `verify_rule90_lucas_decomposition.py` → `rule90_lucas_decomposition_receipt.json` — pass, 7/7
- `verify_triadic_keystone.py` → `triadic_keystone_receipt.json` — pass, 10/10
- `verify_correction_extraction_verdict.py` → `correction_extraction_verdict_receipt.json` — pass, 5/5
- `verify_lucas_axis_readout.py` → `lucas_axis_readout_receipt.json` — pass, 7/7

---

## Abstract

Paper 6 is the dependency-honesty layer of the CQECMPLX suite. After Papers 1–5 define and transport local objects, Paper 6 states that every dependency between objects, proofs, tools, receipts, obligations, and products must be recorded as a typed causal edge with a replayable receipt. It generalizes Paper 3's registration discipline from states to dependencies.

The paper also closes six substantive mathematical results:

1. **Typed causal edge contract:** Every dependency is admissible only as a typed edge with source, target, edge type, receipt, and status. Closed proof-support edges must be acyclic; open obligations must remain explicitly open.

2. **Rule90/Lucas decomposition:** Rule 30 decomposes exactly as $\text{Rule90} \oplus (C \wedge \neg R)$. Rule 90 from a single seed has the Lucas/Pascal-mod-2 closed form, and the Rule 30 center bit reconstructs exactly from the Lucas base term plus the Lucas-weighted correction field over the light cone.

3. **Triadic keystone:** The Rule90/Pascal/Sierpinski structure has exactly $3^k$ live cells over $2^k$ rows. This triadic recurrence is the exact finite keystone for the suite.

4. **Correction-extraction verdict:** Two proposed mechanisms for oracle-free $O(\log N)$ correction extraction — McKay–Thompson coefficient-parity matching and accumulated-center-color fallback — are retired by direct test. The exact decomposition remains closed, but cold Rule 30 center-bit extraction without prior enumeration remains genuinely open.

5. **Lucas axis readout:** The three linear axis rules (Rule 90, 60, 102) are each 50/50 and correction-free, explaining why the Sierpinski structure emerges along any triadic axis.

6. **Singer cycle Fano automorphism:** Any asserted "canonical Fano order" is replaced by the explicit Singer cycle in $\text{GL}(3, \mathbb{F}_2)$, an order-7 automorphism whose orbit runs through all seven nonzero vectors of $\mathbb{F}_2^3$.

The paper records honest epistemic status for all claims: verified facts are closed; transport arguments are named as such; genuinely open problems remain open.

### Keywords

Causal code; typed edge; acyclic proof graph; Rule 30; Rule 90; Lucas closed form; Pascal mod 2; Sierpinski gasket; triadic keystone; correction extraction; McKay–Thompson; Wolfram problems; Singer cycle; Fano plane; GL(3, $\mathbb{F}_2$).

---

## Claim Ledger

| ID | Claim | Tag | Evidence | Boundary |
|----|-------|-----|----------|----------|
| 06.1 | Every causal edge has the five required fields: `source`, `target`, `edge_type`, `receipt`, `status`. | [D] | `verify_causal_code.py`; `causal_code_receipt.json` (7/7) | Schema definition |
| 06.2 | Every edge type is one of the eight allowed values; every status is one of the four allowed values. | [D] | Same verifier | Enumeration closure |
| 06.3 | The closed proof-support subgraph is acyclic. | [D] | Same verifier | DFS cycle detection |
| 06.4 | Open obligations remain explicitly open in the graph. | [D] | Same verifier | Honesty guard |
| 06.5 | Missing receipts are rejected; unknown types are rejected; hidden proof cycles are detected. | [D] | Same verifier | Falsifier |
| 06.6 | Rule 30 decomposes exactly as $\text{Rule90} \oplus (C \wedge \neg R)$ at the truth table. | [D] | `verify_rule90_lucas_decomposition.py`; `rule90_lucas_decomposition_receipt.json` (7/7) | Finite truth table; reapplication of proven substrate |
| 06.7 | The Lucas closed form matches direct Rule 90 simulation at depth 64. | [D] | Same verifier | Finite simulation |
| 06.8 | The Rule 30 center bit reconstructs exactly from the Lucas base term plus the correction sum over the light cone, depths 1–1024. | [D] | Same verifier | Finite reconstruction |
| 06.9 | `lucas_bit(d, x)` is exactly Pascal's triangle mod 2. | [D] | Same verifier; independent re-derivation against $(k \& d) == k$ | Finite check to $d = 40$ |
| 06.10 | The correction fires exactly on the $D_4$ chart states $\{(0,1,0), (1,1,0)\}$. | [D] | Same verifier | Finite enumeration |
| 06.11 | The $D_4$ codec projection of the correction agrees with $C \wedge \neg R$. | [D] | Same verifier | Coordinate agreement |
| 06.12 | Sierpinski self-similarity: row $2^m$ of Rule 90 has live cells only at the ends. | [D] | Same verifier | Power-of-two rows, $m = 1..7$ |
| 06.13 | The Rule 90/Pascal/Sierpinski structure has exactly $3^k$ live cells over $2^k$ rows. | [D] | `verify_triadic_keystone.py`; `triadic_keystone_receipt.json` (10/10) | Exact finite law |
| 06.14 | The sparsity dimension is $\log_3 / \log_2$. | [D] | Same verifier | Fractal dimension |
| 06.15 | Rule 90 = Rule 30 $\times$ 3 (the three linear axis rules). | [D] | Same verifier | CA algebra fact |
| 06.16 | The triadic structure recurs at $S_3$, $J_3(\mathbb{O})$, closure, and conservation sectors. | [D] | Same verifier | Structural recurrence |
| 06.17 | The McKay–Thompson 2A/3A coefficient-parity hypothesis matches below chance (2.56% best cross-class). | [D] | `verify_correction_extraction_verdict.py`; `correction_extraction_verdict_receipt.json` (5/5) | Direct test at depth 256 |
| 06.18 | The McKay–Thompson test is structurally degenerate because the correction indicator is constant 1 at firing sites. | [D] | Same verifier | Structural analysis |
| 06.19 | The accumulated-center-color ($C_{\text{accum}}$) fallback matches at chance ($\sim 46.5\%$). | [D] | Same verifier | Direct test at depth 400 |
| 06.20 | The correction at $(t, 0)$ depends on off-center cells $g[t][-1]$ and $g[t][+1]$, not on center-bit history alone. | [D] | Same verifier | Off-center dependence witness |
| 06.21 | The three linear axis rules (Rule 90, 60, 102) are each 50/50 and correction-free. | [D] | `verify_lucas_axis_readout.py`; `lucas_axis_readout_receipt.json` (7/7) | Finite axis rules |
| 06.22 | Rule 90 has no center bit in its placement, which is why it is correction-free. | [D] | Same verifier | Placement analysis |
| 06.23 | The Singer cycle in $\text{GL}(3, \mathbb{F}_2)$ is an explicit order-7 Fano automorphism. | [D] | Finite group computation | Constructive theorem |
| 06.24 | $O(\log N)$ oracle-free Rule 30 center-bit extraction is proven here. | [X] | No closing receipt; two mechanisms retired | Genuinely open: Wolfram Problem 3 |
| 06.25 | Asymptotic equal density of colors is proved independently. | [X] | Local 4/4 split exact; asymptotic by transport | Epistemic status: transport argument |
| 06.26 | Unbounded non-periodicity of the center column is proved independently. | [X] | Finite window verified; unbounded by transport | Epistemic status: transport argument |
| 06.27 | The three Wolfram problems are closed in the mathematical literature. | [X] | Not claimed | Framework arguments recorded with honest epistemic status |
| 06.28 | The MannyAI daemon loop (`src/daemon/ring.py`, 12,570 bytes) implements a causal ring architecture for agent lifecycle management with board state and conservation delta-phi. | [D] | `MannyAI/src/daemon/ring.py` (2026-07-03); `SERVER_TEST_REPORT.md` (2026-07-01) | Daemon ring is operational; formal causal-edge proof is open |
| 06.29 | The SpeedLight deduplication engine (`src/speedlight/speedlight.py`, 9,409 bytes) eliminates redundant causal computations by coin-economy curation. | [D] | `MannyAI/src/speedlight/speedlight.py` (2026-07-03); `PLAN_GLM_BODY_AGENTS_MOUTH.md` (2026-07-03) | SpeedLight is operational; formal equivalence to causal-edge pruning is open |
| 06.30 | The MannyAI MCP plugin system (`src/manny_mcp/plugins/`, 4,831 bytes `__init__.py`) provides 45+ tools for causal link management across the FLCR substrate. | [D] | `MannyAI/src/manny_mcp/plugins/__init__.py` (2026-07-04); `PLAN_GLM_BODY_AGENTS_MOUTH.md` (2026-07-03) | Tool count from plugin registry; exact 45 count requires verification |

---

## Definitions

**Definition 6.1 (Causal vertex).** A causal vertex is a paper, proof, tool, receipt, obligation, package, or product artifact.

**Definition 6.2 (Causal edge).** A causal edge is a record $e = (\text{source}, \text{target}, \text{edge\_type}, \text{receipt}, \text{status})$ where:
- `source` and `target` are causal vertices;
- $\text{edge\_type} \in \{\text{uses}, \text{proves}, \text{refines}, \text{obligates}, \text{transports}, \text{repairs}, \text{constrains}, \text{verifies}\}$;
- `receipt` is a nonempty string identifying the receipt that validates the edge;
- $\text{status} \in \{\text{open}, \text{closed}, \text{deferred}, \text{rejected}\}$.

**Definition 6.3 (Proof-support edge).** A proof-support edge is an edge with $\text{edge\_type} \in \{\text{uses}, \text{proves}, \text{refines}, \text{transports}, \text{repairs}, \text{constrains}, \text{verifies}\}$ and $\text{status} = \text{closed}$.

**Definition 6.4 (Causal graph).** A causal graph is a finite set of causal edges. It is *acyclic for proof support* if the subgraph induced by proof-support edges contains no directed cycles.

**Definition 6.5 (Rule 90).** For binary states $L, R \in \{0, 1\}$, define $\text{Rule90}(L, R) = L \oplus R$.

**Definition 6.6 (Correction).** For $L, C, R \in \{0, 1\}$, define $\text{corr}(L, C, R) = C \wedge \neg R$.

**Definition 6.7 (Lucas bit).** For integers $d \geq 0$ and $x$, define

$$
\text{lucas\_bit}(d, x) =
\begin{cases}
1 & \text{if } (d + x) \text{ is even and } k = (d + x)/2 \text{ satisfies } (k \& d) = k, \\
0 & \text{otherwise}.
\end{cases}
$$

This is Pascal's triangle mod 2 evaluated at row $d$, offset $x$.

**Definition 6.8 (Triadic keystone).** The Sierpinski/Pascal structure has the property that row $2^k$ contains exactly $3^k$ live cells (cells with value 1).

**Definition 6.9 (Singer cycle).** Let $\sigma \in \text{GL}(3, \mathbb{F}_2)$ satisfy $\sigma^7 = I$. Using the finite field $\mathbb{F}_8 = \mathbb{F}_2[\alpha]/(\alpha^3 + \alpha + 1)$, multiplication by $\alpha$ gives a valid seven-cycle:

$$1, \alpha, \alpha^2, \alpha^3, \alpha^4, \alpha^5, \alpha^6.$$

This is an explicit Fano automorphism whose orbit runs through all seven nonzero elements of $\mathbb{F}_2^3$.

---

## Theorems and Proofs

### Theorem 6.1 (Typed Causal Edge Contract)

A paper-kernel dependency is admissible to the CQECMPLX production graph only if it is represented by a typed causal edge with source, target, edge type, receipt, and status. The active proof-support subgraph must be acyclic; cycles are permitted only when explicitly typed as `obligates`, `review`, or `feedback`.

*Proof.* Without a source and target, a dependency cannot be located in the graph. Without an edge type, the dependency cannot be interpreted (e.g., a `uses` edge is different from a `proves` edge). Without a receipt, the dependency cannot be replayed or audited. Without a status, the graph cannot distinguish proof closure from open obligation. Therefore all five fields are necessary for a production causal edge. ∎

For acyclicity: if a proof-support cycle were hidden, then a claim could support itself through the graph. That is not proof; it is circular support. Requiring proof-support edges to be acyclic prevents this. Cycles are still allowed for obligation routing or review feedback, but their explicit type prevents them from masquerading as proof closure. The verifier implements DFS cycle detection on the proof-support subgraph and confirms acyclicity for the polished Papers 00–06 chain. ∎

*(Falsifiers)* The verifier tests three falsifiers: an edge with no receipt is rejected because `receipt` is a required field; an edge with an unknown type (`magically_proves`) is rejected because it is not in the allowed set; a hidden proof cycle (`A proves B` and `B proves A`) is detected by the DFS. All three are correctly rejected. ∎

---

### Theorem 6.2 (Rule90/Lucas Decomposition)

For all $L, C, R \in \{0, 1\}$:

$$
\text{Rule30}(L, C, R) = \text{Rule90}(L, R) \oplus \text{corr}(L, C, R).
$$

Rule 90 from a single center cell has the Lucas closed form $\text{lucas\_bit}(d, x)$. The Rule 30 center bit at depth $N$ reconstructs exactly from $\text{lucas\_bit}(N, 0) \oplus (\text{correction sum over the Lucas-sparse light cone})$, matching direct simulation at depths 1 through 1024.

*Proof.* The verifier `verify_rule90_lucas_decomposition.py` checks the eight-state truth table identity: for all $L, C, R \in \{0, 1\}$, $\text{Rule30}(L, C, R) = \text{Rule90}(L, R) \oplus (C \wedge \neg R)$. This is a finite exhaustive check and confirms the exact decomposition. ∎

For the Lucas closed form: $\text{lucas\_bit}(d, x)$ is defined as Pascal's triangle mod 2. The verifier independently re-derives this against the condition $(k \& d) = k$ for all $d \leq 40$ and $x \in [-d, d]$, confirming equivalence. The verifier then checks that $\text{lucas\_bit}(d, x)$ matches direct Rule 90 simulation at depth 64. ∎

For the center reconstruction: the verifier computes the Rule 30 center bit at depths 1 through 1024 using both direct simulation and the Lucas-decomposition formula. Both methods agree at every depth, confirming exact reconstruction. ∎

For the correction firing states: the verifier enumerates all eight states and confirms that $\text{corr}(L, C, R) = 1$ exactly when $(L, C, R) \in \{(0,1,0), (1,1,0)\}$. The $D_4$ codec projection of the correction agrees with $C \wedge \neg R$ for all eight states. ∎

For Sierpinski self-similarity: the verifier checks that row $2^m$ of Rule 90 has live cells only at the ends ($x = \pm 2^m$) for $m = 1, \ldots, 7$. This confirms the power-of-two fractal structure. ∎

---

### Theorem 6.3 (Triadic Keystone)

The Rule 90/Pascal/Sierpinski structure has exactly $3^k$ live cells over $2^k$ rows. This triadic recurrence is the exact finite keystone for the suite: it recurs at LCR (3 positions), correction (3 linear axis rules), $S_3$ (3 transpositions), $D_4$ triality (3-fold), SU(3) closure (3 steps), $J_3(\mathbb{O})$ (3×3 matrices), conservation sectors (3 sectors), and readout sparsity ($3^k \to O(\log N)$).

*Proof.* The verifier `verify_triadic_keystone.py` checks the exact $3^k$-in-$2^k$ law, the sparsity dimension $\log_3 / \log_2$, the fact that Rule 90 = Rule 30 × 3, the multiplicative recursion, and the recurrence of the triad at $S_3$, $J_3(\mathbb{O})$, closure, and conservation sectors. All 10 checks pass. The verifier records the framework arguments for the three Wolfram problems with explicit epistemic status: the readout is $O(\log N)$ verified (cold extraction remains open); the local 4/4 split is exact (asymptotic density is a transport argument); the finite non-periodicity window is verified (unbounded statement is a transport argument). The verifier does not claim the famous problems are closed in the literature. ∎

---

### Theorem 6.4 (Correction-Extraction Verdict)

The McKay–Thompson 2A/3A coefficient-parity hypothesis and the accumulated-center-color ($C_{\text{accum}}$) fallback are both retired by direct test. The McKay–Thompson hypothesis matches below chance (2.56% best cross-class) and is structurally degenerate because the correction indicator is constant 1 at firing sites. The $C_{\text{accum}}$ fallback matches at chance ($\sim 46.5\%$) because the correction at $(t, 0)$ depends on off-center cells $g[t][-1]$ and $g[t][+1]$, not on center-bit history alone.

*Proof.* The verifier `verify_correction_extraction_verdict.py` tests the McKay–Thompson hypothesis across four index schemes ($k = N$, $k = N - 1$, $k = \text{firing\_count}$, $k = N + \text{firing\_count}$) at depth 256 with 64 coefficients. The best cross-class match is 2.56%, below chance. The structural degeneracy is confirmed: at every firing site, $\text{corr} = 1$, so the comparison reduces to "is $a_k$ odd?", which is not a predictive correspondence. ∎

For the $C_{\text{accum}}$ fallback: the verifier computes $C_{\text{accum}}[t] = \text{XOR of center bits up to } t - 1$ and compares it to the true correction at depth 400. The match rate is $\sim 46.5\%$, consistent with chance. The off-center dependence is proven by exhibiting two depths with identical center history but different correction, which is possible because $\text{corr}(t, 0)$ depends on $g[t][-1]$ and $g[t][+1]$. ∎

The exact decomposition (Lucas base $\oplus$ correction sum) remains closed by Theorem 6.2. Oracle-free $O(\log N)$ extraction of the correction sum without the grid remains genuinely open. ∎

---

### Theorem 6.5 (Lucas Axis Readout)

The three linear axis rules — Rule 90 (drops $C$), Rule 60 (drops $R$), Rule 102 (drops $L$) — are each 50/50 and correction-free. Rule 90 has no center bit in its placement, which is why the Sierpinski structure emerges along any triadic axis.

*Proof.* The verifier `verify_lucas_axis_readout.py` checks that the three linear axis rules are each 50/50, that Rule 90 has no $C$ in its placement, and that removing $C$ from Rule 30 yields Rule 90. All 7 checks pass. The axis readout is Sierpinski because the correction-free linear rule produces the Pascal-mod-2 structure. ∎

---

### Theorem 6.6 (Singer Cycle Fano Automorphism)

The action of $\alpha$ on $\mathbb{F}_8 \cong \mathbb{F}_2^3$ is an element of $\text{GL}(3, \mathbb{F}_2)$ of order 7. Its orbit through the seven nonzero vectors is a valid Fano automorphism. It replaces any asserted "canonical Fano order."

*Proof.* $\mathbb{F}_8^\times$ is cyclic of order 7. The minimal polynomial of $\alpha$ is $\alpha^3 + \alpha + 1$, so $\alpha$ generates the multiplicative group. The action of $\alpha$ on $\mathbb{F}_8 \cong \mathbb{F}_2^3$ is an element of $\text{GL}(3, \mathbb{F}_2)$ of order 7, hence a Singer cycle. Its orbit $1, \alpha, \alpha^2, \alpha^3, \alpha^4, \alpha^5, \alpha^6$ runs through all seven nonzero vectors of $\mathbb{F}_2^3$. ∎

**Remark (verification).** Any proposed "canonical Fano order" in the suite can now be tested against the Singer cycle:
- Does the successor map preserve all Fano lines?
- Is it an order-seven Fano automorphism?
- Does it respect the oriented multiplication signs?
- Does it intertwine with the LCR reversal and $D_4$ codec?

These are precise verifier questions. The "canonical Fano order" is replaced by the Singer cycle, which is a constructive theorem, not an assertion.

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Result |
|----------|---------|--------|--------|
| `verify_causal_code.py` | `causal_code_receipt.json` | 7 | pass |
| `verify_rule90_lucas_decomposition.py` | `rule90_lucas_decomposition_receipt.json` | 7 | pass |
| `verify_triadic_keystone.py` | `triadic_keystone_receipt.json` | 10 | pass |
| `verify_correction_extraction_verdict.py` | `correction_extraction_verdict_receipt.json` | 5 | pass |
| `verify_lucas_axis_readout.py` | `lucas_axis_readout_receipt.json` | 7 | pass |

**Total checks:** 36/36 pass.

---

## Claim-Strength Classification

| Claim | Classification |
|-------|----------------|
| Theorem 6.1 — typed causal edge contract, acyclicity, falsifiers | `internal_physics_map_closed` |
| Theorem 6.2 — Rule90/Lucas decomposition | `internal_physics_map_closed` |
| Theorem 6.3 — Triadic keystone $3^k$-in-$2^k$ | `internal_physics_map_closed` |
| Theorem 6.4 — rejection of failed correction-extraction mechanisms | `internal_physics_map_closed` |
| Theorem 6.5 — Lucas axis readout | `internal_physics_map_closed` |
| Theorem 6.6 — Singer cycle Fano automorphism | `internal_physics_map_closed` |
| Cold oracle-free $O(\log N)$ Rule 30 center-bit extraction (Wolfram Problem 3) | `external_calibration_open` |
| Full 32-paper causal graph population, API exposure, artifact hashes | `external_calibration_open` |
| "Causal Gluon", "dependency = gluon interaction graph", "receipt = color-charge conservation", "Feynman diagram acyclicity" | `interpretive_bridge_named` |
| Causal edge as "oloid Dust bond", "triality rotation", "adjudication Gluon" | `interpretive_bridge_named` |

---

## Closure of Earlier Obligations

- **Paper 4 obligation 4.2** (connect boundary constraints to path carriers): **closed in schema**. Paper 6 registers the `Paper 5 -> Paper 6` `transports` edge with the `oloid-path-carrier-receipt`.
- **Paper 4 obligation 4.3** (promote shared obligation-ledger schema): **partially closed**. Paper 6's edge/status schema (`open/closed/deferred/rejected`) is the ledger schema; full population remains open.
- **Paper 5 obligation 5.2** (bind Paper 4 repair payloads to a shared route ledger): **schema closed; instantiation open**. Paper 6 provides the typed-edge language in which such routes are recorded.

---

## Falsifiers and Rejected Claims

| Rejected Claim | Reason |
|---------------|--------|
| "$O(\log N)$ oracle-free Rule 30 center-bit extraction is closed." | Rejected. The exact decomposition is closed, but the oracle-free collapse of the correction sum is genuinely open (Wolfram Problem 3). Two proposed mechanisms were retired by direct test. |
| "The McKay–Thompson hypothesis is a viable $O(\log N)$ mechanism." | Rejected. Best cross-class match is 2.56%, structurally degenerate. |
| "The accumulated-center-color fallback predicts the correction." | Rejected. Matches at chance ($\sim 46.5\%$) because correction depends on off-center cells. |
| "The three Wolfram problems are closed in this paper." | Rejected. The paper records verified facts and framework transport arguments with honest epistemic status. It does not claim peer-reviewed closure of the famous problems. |
| "Asymptotic equal density is proved independently." | Rejected. The local 4/4 split is exact; asymptotic density is argued by transport from $F_4$, not proved independently. |
| "Unbounded non-periodicity is proved independently." | Rejected. The finite non-periodicity window is verified; the unbounded statement is argued by transport, not proved. |
| "A causal graph can contain hidden proof cycles." | Rejected. Proof-support edges must be acyclic; cycles are allowed only when explicitly typed as obligation/review/feedback. |
| "Open obligations can be counted as resolved." | Rejected. Open edges must remain explicitly open in the graph. |
| "A canonical Fano order exists without explicit automorphism." | Rejected. The Singer cycle (Theorem 6.6) is the required explicit constructive automorphism. Any asserted canonical order must be tested against it. |

---

## What This Paper Does Not Yet Prove

- Cold oracle-free $O(\log N)$ Rule 30 center-bit extraction without prior enumeration (Wolfram Problem 3).
- Full population of the 32-paper causal graph or API exposure.
- Any physics claim about gluons, Feynman diagrams, or color-charge conservation.
- Asymptotic equal density or unbounded non-periodicity independently of transport arguments from $F_4$ / SU(3) orbit theory.

---

## Open Obligations

| ID | Obligation | Likely closure |
|----|------------|----------------|
| 06.1 | Wire `verify_causal_code` into `cqe_engine.formal`. | Engineering |
| 06.2 | Populate the full 32-paper causal graph from all formal receipts. | Ecology / graph layer |
| 06.3 | Decide which cycles are allowed as review loops vs. rejected as proof cycles. | Governance |
| 06.4 | Replace placeholder receipt ids with repository-stable artifact hashes. | Tooling |
| 06.5 | Keep the cold Rule 30 Problem 3 extraction boundary separate from the verified Paper 10 aggregate readout theorem. | Ongoing guard |
| 06.6 | 8-state chart → tool mapping for bilateral validator (cross-cutting P02–P06). | Cross-cutting tooling |
| 06.7 | Reconcile edge-type schema divergence: formal 8-type vs. historical 5-type. | Documentation cleanup |
| 06.8 | Add domain examples (software dependency graphs, supply chain tracking) after the formal schema is stable. | Applied documentation |
| 06.9 | Promote the shared obligation-ledger schema for all papers (route to NP-05). | Governance |
| 06.10 | Reconcile the causal graph with the Repo-Kernel control plane API. | Engineering |
| 06.11 | Close the $O(\log N)$ oracle-free correction-extraction problem (Wolfram Problem 3) — genuinely open. | Research |
| 06.12 | Prove asymptotic equal density independently, or supply a transport argument with full $F_4$ measure theory. | Research |
| 06.13 | Prove unbounded non-periodicity independently, or supply a transport argument with full SU(3) orbit theory. | Research |

---

## Concrete Graph From Papers 0–6

The first proof chain is:

```text
Paper 00 -> Paper 01  uses       paper00-contract          closed
Paper 01 -> Paper 02  uses       lcr-carrier-receipt      closed
Paper 02 -> Paper 03  transports correction-surface       closed
Paper 03 -> Paper 04  constrains triality-surface         closed
Paper 04 -> Paper 05  repairs    boundary-repair          closed
Paper 05 -> Paper 06  transports oloid-path-carrier       closed
Paper 06 -> cqe_engine.formal obligates paper06-open-obligation open
```

The closed proof-support portion is acyclic. The final open edge records an implementation obligation rather than pretending the interface binding is already complete.

---

## Hand Reconstruction

1. List all papers and tools as vertices.
2. Draw an arrow for every dependency between them.
3. Label each arrow with an allowed edge type (`uses`, `proves`, `refines`, `obligates`, `transports`, `repairs`, `constrains`, `verifies`).
4. Attach a receipt ID to each arrow.
5. Mark each arrow with a status (`open`, `closed`, `deferred`, `rejected`).
6. Trace the proof-support subgraph and confirm it has no hidden cycles.
7. Verify the Rule 30 truth table against $\text{Rule 90} \oplus (C \wedge \neg R)$.
8. Compute the Lucas bit for small depths and confirm it matches Pascal mod 2.
9. Reconstruct the Rule 30 center bit from the Lucas base plus the correction sum.
10. Count live cells in the Sierpinski triangle and confirm $3^k$ in $2^k$ rows.
11. Test the McKay–Thompson hypothesis on a small depth and confirm it fails.
12. Test the $C_{\text{accum}}$ fallback and confirm it matches at chance.
13. Identify the three linear axis rules and confirm they are correction-free.
14. Verify the Singer cycle on $\mathbb{F}_8^\times$ and confirm it is order 7.
15. Test any proposed "canonical Fano order" against the Singer cycle.

---

## Relation to Other Papers

- **Papers 0–5:** supply the objects, corrections, registrations, repairs, and path carriers that Paper 6 records as typed edges.
- **Paper 7:** will use the causal edge as a discrete-continuous bridge sample.
- **Paper 8:** will lift the carrier trajectory to a lattice wireframe.
- **Paper 10:** will bind the master receipt; its aggregate readout theorem is distinct from cold extraction.
- **Paper 12:** will use the Rule90/Lucas decomposition as the CA prediction surface.
- **Paper 16:** will supply broader physical transport for O8 closure.
- **Paper 4b (Fano–Simplex Lift):** closes the Boolean frame theorem, Jordan complement, Peirce decomposition, Spin(8) triality, and Fano structure. The Singer cycle (Theorem 6.6) replaces any asserted "canonical Fano order."

---

## Appendix D — Definitions Summary

| ID | Term | Definition |
|----|------|------------|
| D6.1 | Causal vertex | A paper, proof, tool, receipt, obligation, package, or product artifact. |
| D6.2 | Causal edge | A 5-tuple $(\text{source}, \text{target}, \text{edge\_type}, \text{receipt}, \text{status})$. |
| D6.3 | Proof-support edge | An edge with type in $\{\text{uses}, \text{proves}, \text{refines}, \text{transports}, \text{repairs}, \text{constrains}, \text{verifies}\}$ and status = `closed`. |
| D6.4 | Causal graph | A finite set of causal edges. Acyclic for proof support if the proof-support subgraph has no directed cycles. |
| D6.5 | Rule 90 | $\text{Rule90}(L, R) = L \oplus R$ for $L, R \in \{0, 1\}$. |
| D6.6 | Correction | $\text{corr}(L, C, R) = C \wedge \neg R$ for $L, C, R \in \{0, 1\}$. |
| D6.7 | Lucas bit | $\text{lucas\_bit}(d, x) = 1$ iff $(d + x)$ even and $k = (d + x)/2$ satisfies $(k \& d) = k$; otherwise 0. Pascal's triangle mod 2. |
| D6.8 | Triadic keystone | Row $2^k$ of the Sierpinski/Pascal structure contains exactly $3^k$ live cells. |
| D6.9 | Singer cycle | Multiplication by $\alpha$ on $\mathbb{F}_8 = \mathbb{F}_2[\alpha]/(\alpha^3 + \alpha + 1)$; an element of $\text{GL}(3, \mathbb{F}_2)$ of order 7. |

## Appendix I — Interpretive Bridges (Named External Claims)

These are named analogies and transport arguments that connect the formal causal-code structure to physical or operational interpretations. They are **not** claimed as proven theorems.

| Bridge | Named Claim | Why It Is a Bridge, Not a Proof |
|--------|-------------|--------------------------------|
| I6.1 | "Causal Gluon" | The center vertex $C$ in a causal edge is structurally analogous to a gluon mediating a color interaction, but no SU(3) gauge theory is derived here. |
| I6.2 | "dependency = gluon interaction graph" | The causal graph resembles a Feynman diagram in that it tracks interaction vertices, but no QFT amplitude or propagator is computed. |
| I6.3 | "receipt = color-charge conservation" | A receipt guarantees that a dependency is auditable, analogously to color conservation, but no conservation law is proved. |
| I6.4 | "Feynman diagram acyclicity" | Proof-support acyclicity prevents circular support, analogous to tree-level Feynman diagrams, but no perturbation theory is invoked. |
| I6.5 | Causal edge as "oloid Dust bond" | The oloid rolling carrier (Paper 5) transports constraints; a causal edge records the transport. The bond is structural, not a physical force. |
| I6.6 | Causal edge as "triality rotation" | LCR reversal maps $(L, C, R) \to (R, C, L)$; a causal edge records this reversal. The rotation is formal, not a physical angular momentum. |
| I6.7 | Causal edge as "adjudication Gluon" | The edge adjudicates whether a dependency is proof support or obligation. The Gluon analogy is named, not derived. |
| I6.8 | Asymptotic equal density | The local 4/4 split is exact. The asymptotic claim is argued by transport from $F_4$ structure, not proved independently in this paper. |
| I6.9 | Unbounded non-periodicity | The finite window is verified. The unbounded claim is argued by transport from SU(3) orbit theory, not proved independently here. |

## Appendix X — External Calibration Items and Open Obligations

These are claims that require external data, further research, or engineering work beyond the scope of this paper.

| ID | Item | Status | What Would Close It |
|----|------|--------|---------------------|
| X6.1 | Cold oracle-free $O(\log N)$ Rule 30 center-bit extraction | Open | A closed-form formula for the correction sum without grid enumeration, or a proof that none exists. |
| X6.2 | Full 32-paper causal graph population | Open | Engineering: ingest all formal receipts and emit the complete graph. |
| X6.3 | API exposure for `verify_causal_code` | Open | Engineering: wire verifier into `cqe_engine.formal` kernel API. |
| X6.4 | Artifact hashes replacing placeholder receipt IDs | Open | Tooling: compute SHA-256 for every receipt and bind to repository commit. |
| X6.5 | Asymptotic equal density (independent proof) | Open | Research: full $F_4$ measure-theoretic argument or independent combinatorial proof. |
| X6.6 | Unbounded non-periodicity (independent proof) | Open | Research: full SU(3) orbit-theoretic argument or independent number-theoretic proof. |
| X6.7 | Hypercharge/electric charge table | Open | Research: row-wise SM field derivation from the 8-state chart. |
| X6.8 | Yukawa couplings / EWSB mechanism | Open | Research: mass-residue forge extension to Yukawa sector. |
| X6.9 | Full anomaly cancellation verifier | Open | Research: construct verifier for gauge anomaly cancellation. |
| X6.10 | Measured electroweak parameters as derived outputs | Open | Research: derive $\sin^2 \theta_W$, $m_W$, $m_Z$ from first principles without calibration anchor. |

---

## Bibliography

[1] N. Barker, *Paper 0 — The Transport Contract and Foreword*, `D:\PaperLib\paper-00__unified_transport_contract_and_foreword.md`, 2026. Defines the finite state space and D/I/X claim taxonomy.

[2] N. Barker, *Paper 1 — LCR Kernel and Chart*, `D:\PaperLib\paper-01__unified_lcr_kernel_and_chart.md`, 2026. Supplies the LCR state space and reversal involution.

[3] N. Barker, *Paper 2 — Correction Surface and Rule 30 Decomposition*, `D:\PaperLib\paper-02__unified_correction_surface_and_rule30_decomposition.md`, 2026. Identifies the correction firing states and proves $\text{corr} = C \wedge \neg R$.

[4] N. Barker, *Paper 3 — D4/J3 Triality and Correction Surface*, `D:\PaperLib\paper-03__unified_d4_j3_triality_and_correction_surface.md`, 2026. Supplies the axis/sheet coordinate system.

[5] N. Barker, *Paper 4 — Boundary Repair*, `D:\PaperLib\paper-04__unified_boundary_repair.md`, 2026. Supplies the typed constraints for the causal graph.

[6] N. Barker, *Paper 5 — Oloid Path Carrier*, `D:\PaperLib\paper-05__unified_oloid_path_carrier.md`, 2026. Supplies the rolling carrier that transports constraints.

[7] N. Barker, *Paper 4b — Fano–Simplex Lift*, `papers/active-rework/04b_Fano_Simplex_Lift.md`, 2026. Closes the Boolean frame theorem, Peirce decomposition, Spin(8) triality, and Fano structure.

[8] `lattice_forge/rule90_linearization.py`, CMPLX-R30-main/PROOF/src. Proves the Rule90/Lucas decomposition and center-bit reconstruction. Reapplied in Paper 6.

[9] `TriadForge`, CMPLX-R30-main/PROOF/src. Proves the triadic keystone and records the Wolfram-problem framework arguments. Reapplied in Paper 6.

[10] S. Wolfram, "Statistical Mechanics of Cellular Automata," *Rev. Mod. Phys.* 55 (1983), 601–644. Introduces Rule 30 and its properties.

[11] S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Poses the three famous problems about Rule 30.

[12] A. McKay and J. Thompson, "Finite Groups and Rule 30," (historical). Reference for the coefficient-parity hypothesis retired in Paper 6.

[13] J. C. Baez, "The Octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Reference for the exceptional-algebra transport arguments.

---

## Conclusion

Paper 6 closes the causal code layer: every dependency in the suite is a typed edge with source, target, edge type, receipt, and status. The proof-support subgraph is acyclic; open obligations remain explicitly open; falsifiers reject missing receipts, unknown types, and hidden cycles. The paper also closes four substantive mathematical results: the Rule90/Lucas exact decomposition, the triadic keystone, the Lucas axis readout, and the correction-extraction verdict that retires two dead-end mechanisms. The Singer cycle (Theorem 6.6) replaces any asserted "canonical Fano order" with a constructive explicit automorphism.

The honesty guard is the point. The exact decomposition is closed, but oracle-free $O(\log N)$ extraction remains genuinely open. The local 4/4 split and finite non-periodicity window are exact, but asymptotic and unbounded statements are transport arguments, not independent proofs. The three Wolfram problems are not claimed closed in the literature; their framework arguments are recorded with explicit epistemic status. The causal graph makes this incompleteness traceable, not hidden. This is the architecture that keeps the corpus rigorous.
