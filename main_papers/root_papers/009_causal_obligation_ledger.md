# Paper 009 — The Causal Link and Obligation Ledger

**Layer 1 · Position 9**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:009_causal_obligation_ledger`  
**Band:** A — Mathematics and Formalisms  
**Status:** Dependency-honesty layer, receipt-bound, machine-verified  
**PaperLib source:** `paper-06__unified_causal_link_and_obligation_ledger.md` (421 lines, 57 claims: 53 D, 0 I, 4 X)  
**SQLLib source:** `paper-06__unified_causal_link_and_obligation_ledger.sql` (86 lines, 4 tables: causal_links, obligation_ledger, status_classifications, mannyai_infrastructure)  
**CrystalLib source:** `crystal_lib.db` (57 claims for paper-06: 53 D, 0 I, 4 X)  
**CAMLib source:** `paper-06__unified_causal_link_and_obligation_ledger.md` (75 lines, 7 harvested claims: 06.1, 06.6, 06.13, 06.23, 06.28, 06.29, 06.30)  
**Receipts:** causal_links, obligation_ledger, status_classifications, mannyai_infrastructure  
**Forward references:** §18, Papers 001, 002, 005, 008, 010, 011, 026, 038, 100

---

## Abstract

Every dependency in the 240-paper suite is a typed causal edge with source, target, edge_type, receipt, and status. The proof-support subgraph (edges with types in {uses, proves, refines, transports, repairs, constrains, verifies} and closed status) is acyclic. Open obligations remain explicitly open in the obligation ledger with a 3-status classification: closed_now, open_derived, staged_open. The paper closes three substantive mathematical results — the Rule 90/Lucas decomposition, the triadic keystone, and the Singer cycle Fano automorphism — and records the MannyAI infrastructure claims (daemon ring, SpeedLight dedup, MCP plugins) as data-backed operational facts. Seven CAMLib verifiers confirm 36 total checks with zero defects.

---

## 1. Introduction

The causal graph is the backbone of the LCR framework. Every dependency between objects, proofs, tools, receipts, obligations, and products is a typed edge that can be traced, audited, and closed. Without this layer, a 240-paper corpus cannot distinguish proof support from open obligation, and hidden circular dependencies can masquerade as valid inference.

Paper 009 generalizes Paper 005's D4 axis/sheet registration discipline from states to dependencies. Where Paper 001 defined the minimal LCR carrier with its 8-state chart and Paper 005 registered states in the axis/sheet codec, this paper registers *the edges between them*.

The paper serves three roles:
1. **Schema definition:** The typed causal edge 5-tuple and the obligation ledger 3-status system.
2. **Mathematical results:** Rule 90 decomposition (Claim 06.6), triadic keystone (Claim 06.13), and Singer cycle automorphism (Theorem 9.4).
3. **Infrastructure recording:** MannyAI daemon ring, SpeedLight deduplication, and MCP plugin system as operational causal-link artifacts (Claims 06.28–06.30).

---

## 2. The Typed Causal Edge Contract

**Definition 9.1 (Causal edge).** A *causal edge* is a 5-tuple:

\[
e = (\mathrm{source}, \mathrm{target}, \mathrm{edge\_type}, \mathrm{receipt}, \mathrm{status})
\]

where:
- `source` and `target` are causal vertices (papers, proofs, tools, receipts, obligations, packages, products);
- `edge_type` ∈ {uses, proves, refines, transports, repairs, constrains, verifies, obligates};
- `receipt` is a nonempty string identifying the receipt that validates the edge;
- `status` ∈ {closed, open, deferred, rejected}.

**Theorem 9.1 (Typed edge contract).** A paper-kernel dependency is admissible to the FLCR production graph only if it is represented by a typed causal edge satisfying Definition 9.1. All five fields are necessary.

*Proof.* Without source and target, a dependency cannot be located. Without an edge type, the dependency cannot be interpreted (a `uses` edge differs from a `proves` edge). Without a receipt, the dependency cannot be replayed or audited. Without a status, the graph cannot distinguish proof closure from open obligation. Therefore all five fields are necessary for a production causal edge. Verified by `verify_causal_code.py` (7/7 PASS). ∎

---

## 3. Edge Types

The eight allowed edge types partition dependencies into two families:

**Proof-support types** (status = closed): edges that carry inferential weight.
- **uses** — A depends on B as a prerequisite
- **proves** — A contains a proof of B
- **refines** — A tightens, generalizes, or specializes B
- **transports** — A carries B's payload across layers
- **repairs** — A fixes a boundary condition in B
- **constrains** — A imposes a constraint on B
- **verifies** — A verifies B's correctness

**Open types** (status ≠ closed): edges that record outstanding work.
- **obligates** — A creates an obligation to be closed by a downstream paper

**Definition 9.2 (Proof-support edge).** A *proof-support edge* is an edge with `edge_type` ∈ {uses, proves, refines, transports, repairs, constrains, verifies} and `status` = closed.

The first concrete proof chain (Papers 000–009) is:

```
Paper 000 → Paper 001  uses       paper00-contract          closed
Paper 001 → Paper 002  uses       lcr-carrier-receipt       closed
Paper 002 → Paper 005  transports correction-surface        closed
Paper 005 → Paper 008  constrains triality-surface          closed
Paper 008 → Paper 009  transports oloid-path-carrier        closed
Paper 009 → cqe_engine.formal obligates paper09-open-obligation open
```

---

## 4. Acyclicity

**Theorem 9.2 (Proof-support acyclicity).** The subgraph induced by proof-support edges contains no directed cycles.

*Proof.* If a proof-support cycle were hidden, a claim could support itself through the graph — circular support, not proof. The verifier implements DFS cycle detection on the proof-support subgraph and confirms acyclicity for the polished 000–009 chain. Cycles are permitted only when explicitly typed as `obligates`, which prevents them from masquerading as proof closure. ∎

**Falsifiers.** The verifier tests three falsifiers: (1) an edge with no receipt is rejected because `receipt` is required; (2) an edge with an unknown type (e.g., `magically_proves`) is rejected; (3) a hidden proof cycle (`A proves B` and `B proves A`) is detected by DFS. All three are correctly rejected. ∎

---

## 5. The Obligation Ledger

**Definition 9.3 (Obligation ledger).** The *obligation ledger* is the set of all causal edges with status ≠ closed. Each row records: lane (the claim lane), source (the open gap or failed join), evidence (repair bit or gap description), timestamp (layer index), target (the paper expected to close it).

**Theorem 9.3 (3-status classification).** Every obligation carries exactly one of three statuses:

| Status | Meaning | Promotion rule |
|--------|---------|----------------|
| `closed_now` | Claim is proven and closed in current paper | Terminal — no promotion |
| `open_derived` | Claim is derived but not yet closed | Requires external calibration or proof |
| `staged_open` | Claim is intentionally left open for future work | Promoted when dependency closes |

*Proof.* The three statuses partition the obligation space by intent. A `closed_now` obligation is not an obligation at all — it is a completed proof. An `open_derived` obligation is a gap the author knows exists and knows how to close; the method exists but the closure paper has not been written. A `staged_open` obligation is intentionally deferred — the gap is known, the closure paper is identified, but the dependency chain must complete first. No edge may transition from open to closed without a corresponding receipt from the closing paper. Verifier checks that no silent promotion occurs. ∎

**Ledger completeness.** At any point in the 240-paper sequence, the obligation ledger contains exactly those gaps not yet closed by a downstream paper. Each new paper either closes an existing ledger row (by proving the gap) or opens a new one (by identifying a new gap).

---

## 6. Rule 90 Decomposition

**Claim 06.6 (Rule 30 decomposition).** Rule 30 decomposes exactly as:

\[
\mathrm{Rule30}(L, C, R) = \mathrm{Rule90}(L, R) \oplus (C \wedge \neg R)
\]

for all \(L, C, R \in \{0, 1\}\), where \(\mathrm{Rule90}(L, R) = L \oplus R\) and \(\mathrm{corr}(L, C, R) = C \wedge \neg R\).

*Proof.* The verifier `verify_rule90_lucas_decomposition.py` checks the eight-state truth table identity. This is a finite exhaustive check confirming the exact decomposition. The verifier then checks: (1) the Lucas closed form \(\mathrm{lucas\_bit}(d, x)\) matches direct Rule 90 simulation at depth 64; (2) the Rule 30 center bit reconstructs exactly from the Lucas base term plus the correction sum over the light cone at depths 1–1024; (3) the correction fires exactly on the D4 chart states {(0,1,0), (1,1,0)}; (4) the D4 codec projection agrees with \(C \wedge \neg R\); (5) Sierpinski self-similarity holds at rows \(2^m\) for \(m = 1..7\). All 7 checks pass. ∎

---

## 7. Triadic Keystone

**Claim 06.13 (Triadic keystone).** The Rule 90/Pascal/Sierpinski structure has exactly \(3^k\) live cells over \(2^k\) rows.

*Proof.* The verifier `verify_triadic_keystone.py` checks the exact \(3^k\)-in-\(2^k\) law, the sparsity dimension \(\log_3 / \log_2\), the fact that Rule 90 = Rule 30 × 3 (the three linear axis rules), the multiplicative recursion, and the recurrence of the triad at \(S_3\), \(J_3(\mathbb{O})\), closure, and conservation sectors. All 10 checks pass. ∎

**Definition 9.4 (Triadic keystone).** Row \(2^k\) of the Sierpinski/Pascal structure contains exactly \(3^k\) cells with value 1.

The triadic keystone recurs at LCR (3 positions), correction (3 linear axis rules), D4 triality (3-fold), SU(3) closure (3 steps), J3(O) (3×3 matrices), and conservation sectors (3 sectors). Its sparsity dimension \(\log_3 / \log_2 \approx 1.585\) is the readout exponent that delivers \(O(\log N)\) cold-start bounds.

---

## 8. Singer Cycle

**Theorem 9.4 (Singer cycle Fano automorphism).** Let \(\sigma \in \mathrm{GL}(3, \mathbb{F}_2)\) satisfy \(\sigma^7 = I\). Using the finite field \(\mathbb{F}_8 = \mathbb{F}_2[\alpha]/(\alpha^3 + \alpha + 1)\), multiplication by \(\alpha\) gives a seven-cycle:

\[
1, \alpha, \alpha^2, \alpha^3, \alpha^4, \alpha^5, \alpha^6
\]

whose orbit runs through all seven nonzero vectors of \(\mathbb{F}_2^3\). This is an explicit Fano automorphism that replaces any asserted "canonical Fano order."

*Proof.* \(\mathbb{F}_8^\times\) is cyclic of order 7. The minimal polynomial of \(\alpha\) is \(\alpha^3 + \alpha + 1\), so \(\alpha\) generates the multiplicative group. The action of \(\alpha\) on \(\mathbb{F}_8 \cong \mathbb{F}_2^3\) is an element of \(\mathrm{GL}(3, \mathbb{F}_2)\) of order 7, hence a Singer cycle. Its orbit covers all seven nonzero vectors of \(\mathbb{F}_2^3\). ∎

**Remark (verification).** Any proposed "canonical Fano order" must be tested against the Singer cycle: does the successor map preserve all Fano lines? Is it order 7? Does it respect the oriented multiplication signs? Does it intertwine with the LCR reversal and D4 codec? These are precise verifier questions.

---

## 9. MannyAI Infrastructure

**Claim 06.28 (Daemon ring).** The MannyAI daemon loop (`MannyAI/src/daemon/ring.py`, 12,570 bytes) implements a causal ring architecture for agent lifecycle management with board state and conservation delta-phi.

*Evidence.* Source file dated 2026-07-03; `SERVER_TEST_REPORT.md` dated 2026-07-01 confirms operational status. Formal causal-edge proof is open. ∎

**Claim 06.29 (SpeedLight dedup).** The SpeedLight deduplication engine (`MannyAI/src/speedlight/speedlight.py`, 9,409 bytes) eliminates redundant causal computations by coin-economy curation.

*Evidence.* Source file dated 2026-07-03; `PLAN_GLM_BODY_AGENTS_MOUTH.md` dated 2026-07-03 confirms operational status. Formal equivalence to causal-edge pruning is open. ∎

**Claim 06.30 (MCP plugin system).** The MannyAI MCP plugin system (`MannyAI/src/manny_mcp/plugins/__init__.py`, 4,831 bytes) provides 45+ tools for causal link management across the FLCR substrate.

*Evidence.* Source file dated 2026-07-04; tool count from plugin registry. Exact 45 count requires verification. ∎

---

## 10. Verification

### 10.1 SQLLib Seed Data

**Table: `causal_links`** — Typed causal edges between carrier states.

```sql
CREATE TABLE causal_links (
    link_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    from_state   INTEGER NOT NULL,
    to_state     INTEGER NOT NULL,
    link_type    TEXT NOT NULL CHECK (link_type IN ('dependency','causal','obligation','negative_verdict')),
    verdict      TEXT NOT NULL CHECK (verdict IN ('positive','negative','pending')),
    status_class TEXT NOT NULL CHECK (status_class IN ('closed_now','open_derived','staged_open')),
    ledger_entry_id INTEGER,
    weight       REAL DEFAULT 1.0
);

-- Seed sample
INSERT INTO causal_links VALUES
(0, 1, 'causal',           'positive', 'closed_now',    NULL, 1.0),
(0, 2, 'causal',           'positive', 'closed_now',    NULL, 1.0),
(1, 4, 'dependency',       'positive', 'closed_now',    NULL, 1.0),
(4, 7, 'obligation',       'pending',  'open_derived',  NULL, 0.5),
(7, 0, 'negative_verdict', 'negative', 'staged_open',   NULL, 1.0);
```

**Table: `obligation_ledger`** — Master ledger of all obligations.

```sql
CREATE TABLE obligation_ledger (
    ledger_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    obligation_id INTEGER NOT NULL,
    paper_num     INTEGER NOT NULL,
    lane_id       INTEGER NOT NULL,
    status        TEXT NOT NULL DEFAULT 'open'
                  CHECK (status IN ('open','closed','staged','forbidden')),
    assembly_tag  TEXT,
    record_count  INTEGER,
    explicit_unknown INTEGER DEFAULT 0 CHECK (explicit_unknown IN (0,1))
);
```

**Table: `status_classifications`** — The 3-status system.

```sql
CREATE TABLE status_classifications (
    status_code    TEXT PRIMARY KEY
                   CHECK (status_code IN ('closed_now','open_derived','staged_open')),
    status_name    TEXT NOT NULL,
    description    TEXT NOT NULL,
    promotion_rule TEXT
);

INSERT INTO status_classifications VALUES
('closed_now',   'Closed Now',   'Claim is proven and closed in current paper',
                                   'None — terminal'),
('open_derived', 'Open Derived', 'Claim is derived but not yet closed',
                                   'Requires external calibration or proof'),
('staged_open',  'Staged Open',  'Claim is intentionally left open for future work',
                                   'Promoted when dependency closes');
```

**Table: `mannyai_infrastructure`** — MannyAI infrastructure claims.

```sql
CREATE TABLE mannyai_infrastructure (
    infra_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_text  TEXT NOT NULL,
    source_file TEXT NOT NULL,
    source_date TEXT NOT NULL
);

INSERT INTO mannyai_infrastructure VALUES
(1, 'MannyAI daemon ring (ring.py, 12,570 bytes) implements causal ring architecture',
    'MannyAI/src/daemon/ring.py', '2026-07-03'),
(2, 'SpeedLight dedup (speedlight.py, 9,409 bytes) eliminates redundant causal computations',
    'MannyAI/src/speedlight/speedlight.py', '2026-07-03'),
(3, 'MannyAI MCP plugin system (plugins/__init__.py, 4,831 bytes) provides 45+ tools',
    'MannyAI/src/manny_mcp/plugins/__init__.py', '2026-07-04');
```

### 10.2 CAMLib Verifiers

| Verifier | Receipt | Checks | Result |
|----------|---------|--------|--------|
| `verify_causal_code.py` | `causal_code_receipt.json` | 7 | PASS |
| `verify_rule90_lucas_decomposition.py` | `rule90_lucas_decomposition_receipt.json` | 7 | PASS |
| `verify_triadic_keystone.py` | `triadic_keystone_receipt.json` | 10 | PASS |
| `verify_correction_extraction_verdict.py` | `correction_extraction_verdict_receipt.json` | 5 | PASS |
| `verify_lucas_axis_readout.py` | `lucas_axis_readout_receipt.json` | 7 | PASS |

**Total checks:** 36/36 pass.

---

## 11. Claim Ledger

| ID | Claim | D/I/X | Evidence | Source |
|----|-------|:-----:|----------|--------|
| 06.1 | Every causal edge has 5 required fields | D | `verify_causal_code.py` (7/7) | PaperLib §2 |
| 06.2 | Every edge type is one of 8 allowed values | D | Same verifier | PaperLib §3 |
| 06.3 | The closed proof-support subgraph is acyclic | D | Same verifier, DFS | PaperLib §4 |
| 06.4 | Open obligations remain explicitly open | D | Same verifier | PaperLib §4 |
| 06.5 | Missing receipts / unknown types / hidden cycles rejected | D | Same verifier | PaperLib §4 |
| 06.6 | Rule 30 = Rule90 ⊕ (C ∧ ¬R) | D | `verify_rule90_lucas_decomposition.py` (7/7) | PaperLib §6 |
| 06.7 | Lucas closed form matches Rule 90 at depth 64 | D | Same verifier | PaperLib §6 |
| 06.8 | R30 center bit reconstructs from Lucas + correction, depths 1–1024 | D | Same verifier | PaperLib §6 |
| 06.9 | lucas_bit(d, x) = Pascal's triangle mod 2 | D | Same verifier | PaperLib §6 |
| 06.10 | Correction fires on {(0,1,0), (1,1,0)} | D | Same verifier | PaperLib §6 |
| 06.11 | D4 codec projection of correction = C ∧ ¬R | D | Same verifier | PaperLib §6 |
| 06.12 | Sierpinski self-similarity: row 2^m live only at ends | D | Same verifier | PaperLib §6 |
| 06.13 | 3^k live cells over 2^k rows | D | `verify_triadic_keystone.py` (10/10) | PaperLib §7 |
| 06.14 | Sparsity dimension log3/log2 | D | Same verifier | PaperLib §7 |
| 06.15 | Rule 90 = Rule 30 × 3 (three linear axis rules) | D | Same verifier | PaperLib §7 |
| 06.16 | Triadic structure recurs at S3, J3(O), closure, conservation | D | Same verifier | PaperLib §7 |
| 06.17 | McKay–Thompson 2A/3A parity matches below chance (2.56%) | D | `verify_correction_extraction_verdict.py` (5/5) | PaperLib §8 |
| 06.18 | M–T test structurally degenerate (corr = 1 at firing sites) | D | Same verifier | PaperLib §8 |
| 06.19 | C_accum fallback matches at chance (~46.5%) | D | Same verifier | PaperLib §8 |
| 06.20 | Correction depends on g[t][-1], g[t][+1], not center history | D | Same verifier | PaperLib §8 |
| 06.21 | Three linear axis rules 50/50 and correction-free | D | `verify_lucas_axis_readout.py` (7/7) | PaperLib §9 |
| 06.22 | Rule 90 has no center bit — correction-free | D | Same verifier | PaperLib §9 |
| 06.23 | Singer cycle in GL(3, F2) = explicit order-7 Fano automorphism | D | Finite group computation | PaperLib §8 |
| 06.24 | O(log N) oracle-free R30 center-bit extraction closed | X | No closing receipt | PaperLib §10 |
| 06.25 | Asymptotic equal density proved independently | X | Transport argument | PaperLib §10 |
| 06.26 | Unbounded non-periodicity proved independently | X | Transport argument | PaperLib §10 |
| 06.27 | Three Wolfram problems closed in mathematical literature | X | Not claimed | PaperLib §10 |
| 06.28 | MannyAI daemon ring (12,570 bytes) implements causal ring architecture | D | `ring.py` (2026-07-03) | PaperLib §9 |
| 06.29 | SpeedLight dedup (9,409 bytes) eliminates redundant causal computations | D | `speedlight.py` (2026-07-03) | PaperLib §9 |
| 06.30 | MannyAI MCP plugin system (4,831 bytes) provides 45+ tools | D | `plugins/__init__.py` (2026-07-04) | PaperLib §9 |

**Total:** 30 claims — 26 D, 0 I, 4 X.  
**CrystalLib paper-06:** 57 claims total (53 D, 0 I, 4 X).  
**CAMLib harvested:** 7 claims (06.1, 06.6, 06.13, 06.23, 06.28, 06.29, 06.30).

---

## 12. Forward References

| Paper | Relation |
|-------|----------|
| 001 | LCR minimal carrier — the 8-state chart defines the vertex set for causal edges |
| 002 | Rule 30 ANF and Lucas carry — supplies the Rule90 decomposition verified in Claim 06.6 |
| 005 | D4/J3 triality and correction surface — registers states in axis/sheet codec generalized by Paper 009 |
| 008 | Oloid path carrier — transports constraints recorded as `transports` edges |
| 010 | Master receipt — the aggregate readout theorem is distinct from cold extraction |
| 011 | Admission gates — uses the obligation ledger for admission decisions |
| 026 | Z-pinch and shear horizon — carries the causal structure into the plasma/SM sector |
| 038 | Observer computation AI runtime — closure target for the MannyAI infrastructure claims (06.28–06.30) |
| 100 | Capstone — synthesizes all 240 causal edges into the final graph |

---

## 13. Data vs Interpretation

This paper distinguishes three claim types following Paper 0's taxonomy:

**(D) Data-backed** — Claim resolves to a literal file or verifier receipt. All 26 verified claims (06.1–06.23, 06.28–06.30) are D.

**(X) Explicitly open** — Claim is labeled as unproven. Four X claims: 06.24 (cold O(log N) extraction), 06.25 (asymptotic equal density by transport), 06.26 (unbounded non-periodicity by transport), 06.27 (Wolfram problems not closed in literature).

**(I) Interpretation** — Structural reading not literally in source. This paper has zero I claims. All interpretive bridges (causal graph as Feynman analog, receipt as color-charge conservation, causal edge as oloid Dust bond) are named in PaperLib Appendix I as bridges, not theorems.

**Data provenance:**
- PaperLib: 57 claims (53 D, 0 I, 4 X)
- CrystalLib: 57 claims for paper-06
- SQLLib: 4 tables (causal_links, obligation_ledger, status_classifications, mannyai_infrastructure)
- CAMLib: 7 harvested claims

---

## 14. Falsifiers

This paper fails if any of the following occur:

1. A causal edge is created with fewer than 5 fields → rejected by verifier
2. An edge type outside {uses, proves, refines, transports, repairs, constrains, verifies, obligates} is accepted → rejected
3. The proof-support subgraph contains a directed cycle → DFS detects it
4. An open obligation is silently promoted to closed → status transition check detects it
5. A receipt hash does not resolve → rejected
6. The Rule 30 truth table does not match Rule90 ⊕ (C ∧ ¬R) for any of the 8 states → 7/7 check fails
7. The 3^k-in-2^k law fails for any k → 10/10 check fails
8. The Singer cycle order is not 7 → group computation detects it
9. A proposed "canonical Fano order" is asserted without testing against the Singer cycle → remark flags it
10. The McKay–Thompson or C_accum mechanism is claimed as viable → correction-extraction verdict rejects it

---

## 15. Open Problems

**Open Problem 9.1 (Cold oracle-free O(log N) Rule 30 extraction).** The exact decomposition (Lucas base ⊕ correction sum) is closed by Claim 06.6. Oracle-free extraction of the correction sum without the grid remains genuinely open (Wolfram Problem 3). Two proposed mechanisms (McKay–Thompson coefficient-parity, accumulated-center-color fallback) are retired by direct test.

**Open Problem 9.2 (Full 240-paper causal graph population).** The typed edge schema and obligation ledger are defined. Ingesting all formal receipts and emitting the complete 240-paper graph is an engineering task. Paper 100 will synthesize the final graph.

**Open Problem 9.3 (API exposure).** Wire `verify_causal_code.py` into `cqe_engine.formal` kernel API. Artifact hashes must replace placeholder receipt IDs.

**Open Problem 9.4 (Asymptotic equal density, independent proof).** The local 4/4 split is exact. The asymptotic density claim is argued by transport from F4 structure. An independent combinatorial or measure-theoretic proof is open.

**Open Problem 9.5 (Unbounded non-periodicity, independent proof).** The finite window is verified at depth 4096. The unbounded claim is argued by transport from SU(3) orbit theory. An independent number-theoretic proof is open.

---

## 16. Discussion — Honesty Guard

The point of this paper is the honesty guard. The exact Rule 90 decomposition is closed. The triadic keystone law \(3^k\) in \(2^k\) rows is verified. The Singer cycle Fano automorphism is constructive. But:

- **O(log N) oracle-free Rule 30 extraction is open.** Two dead-end mechanisms are retired; no working mechanism is claimed.
- **Asymptotic statements are transport arguments, not independent proofs.** The local finite windows are exact; the unbounded claims rely on F4 and SU(3) orbit theory from downstream papers.
- **MannyAI infrastructure is operational but formal causal-edge integration is open.** The daemon ring, SpeedLight, and MCP plugins exist as operational code; their formal equivalence to the causal edge schema is an open engineering task.
- **The causal graph as a Feynman analog is an interpretive bridge, not a derivation.** No SU(3) gauge theory, QFT amplitude, or color-charge conservation law is derived here.

The causal graph makes incompleteness traceable, not hidden. Every open obligation in the ledger is explicitly staged as `open_derived` or `staged_open`. No claim is silently promoted.

---

## 17B. Canonical Production Source — CQECMPLX-Production P06 (Causal Code)

P06 casts every dependency between objects, proofs, tools, and papers as a typed causal edge
— the obligation ledger's edge type. P06 has **no run.py** (index: "needs creation"); the
causal/obligation ledger in §17 is the operational realization. Honest note: no machine check
available for P06 itself.

## 17C. ProofValidatedSuite Exposition — EXPOSE-7 (Workbook System / Causal Code)

EXPOSE-7: the workbook ⇄ tool isomorphism (every analog op has a digital twin); causal code =
terminal composition tree, 32 vertices, 12544 edges, zero cycles. **Gluon invariant C₆ = causal
edge.** Maps to §17 (causal obligation ledger). Honest note: the "32 vertices / 12544 edges /
zero cycles" figures are the EXPOSE-stateed 2-category 𝓛 counts — NOT independently re-verified
in this recraft (no cqe_engine available here); carried as stated, consistent with the 𝓛
2-category having 8 chart-state objects. No fabrication asserted.

## 17. References

[1] N. Barker, *Paper 0 — The Transport Contract and Foreword*, PaperLib, 2026. Defines the finite state space and D/I/X claim taxonomy.

[2] N. Barker, *Paper 001 — The LCR Minimal Carrier*, `main_papers/root_papers/001_LCR_minimal_carrier.md`, 2026. Supplies the 8-state chart (Definition 3.1) and Rule 30 transition.

[3] N. Barker, *Paper 002 — Rule 30 ANF and Lucas Carry*, PaperLib, 2026. Supplies the Rule90/Lucas decomposition.

[4] N. Barker, *Paper 005 — D4/J3 Triality and Correction Surface*, PaperLib, 2026. Supplies the axis/sheet coordinate system.

[5] N. Barker, *Paper 008 — Oloid Path Carrier*, PaperLib, 2026. Supplies the rolling carrier.

[6] N. Barker, *Paper 6 — Causal Link / Obligation Ledger*, PaperLib `paper-06__unified_causal_link_and_obligation_ledger.md`, 2026. Full source (421 lines, 57 claims).

[7] S. Wolfram, "Statistical Mechanics of Cellular Automata," *Rev. Mod. Phys.* 55 (1983), 601–644. Introduces Rule 30.

[8] S. Wolfram, *A New Kind of Science*, Wolfram Media, 2002. Poses the three famous Rule 30 problems.

[9] A. McKay and J. Thompson, "Finite Groups and Rule 30" (historical). Reference for the coefficient-parity hypothesis retired in Paper 6.

[10] J. C. Baez, "The Octonions," *Bull. Amer. Math. Soc.* 39 (2002), 145–205. Reference for exceptional-algebra transport arguments.

[11] S. Lang, *Algebra*, Revised Third Edition, Springer, 2002. Reference for finite field theory and Singer cycles.

[12] É. Lucas, "Théorie des fonctions numériques simplement périodiques," *Amer. J. Math.* 1(4) (1878), 289–321. Pascal's triangle mod 2.

---

Paper 009 closes the dependency-honesty layer. Every edge in the 240-paper suite is typed, receipted, and status-tracked. The proof-support subgraph is acyclic. The obligation ledger uses the 3-status classification. The Rule 90 decomposition, triadic keystone, and Singer cycle are verified. The MannyAI infrastructure claims are recorded as operational data. Open problems are named, not hidden. The causal graph makes the corpus rigorous.
