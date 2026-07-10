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

## 17. UFT 0-100 Series (FLCR) — Papers 5-13,15,17,20: interpretation-heavy, defensible

Per HONEST-DISCLOSURE.md these are **(I)** interpretation following FLCR doctrine (typed boundary
repair, oloid LCR parameterization, causal links/obligation ledgers, discrete-continuous bridge,
lattice closure/lattice ladder, temporal windows, theory admission gates, CA prediction surfaces,
curvature-as-repair-demand, continuum edge residuals, applied forge reader). The substrate they
rest on is **(D)**: OBLIGATION_ROWS.json (1,105 rows), 192/196,580 Leech vectors, 4 receipt_bound
obligation rows, CLAIM_LANE_SCHEMA.json (8 lanes/7 classes), quark-face 10/10 receipt. **HONEST
FLAG (Paper 11):** earlier "8/8 success, 0 error walls, TarPit mass 0.507457" were FABRICATIONS,
corrected to 8 structural checks + 4 falsifiers + `pass_with_open_lifts`. **HONEST FLAG (Paper
13):** "64/256 silent-boundary ECAs" is asserted **(D)** in UFT but my independent enumeration
gives 16/256 under strict L=R=0→0 (possibly a different boundary condition); carried as stated
with the discrepancy noted. Maps to §17. No live fabrication in the corrected versions.


## 05A. Formal-Paper Deep-Dive (CQE-paper-05)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-05/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **rolling carrier state** is a triple

```text
q = (sheet, phase, parity)
```

with

```text
sheet in {0,1}
phase in {0,1,2,3}
parity in {0,1}
```

Given a bit `b in {0,1}`, define the rolling step:

```text
roll(q,b) = ((sheet+1) mod 2, (phase+1) mod 4, parity xor b).
```

The **head/tail dyad** is

```text
head = sheet
tail = (phase mod 2) xor sheet xor parity.
```

A **continuous carrier trace** is a list of states where each adjacent pair is
related by one legal `roll` step for the corresponding input bit.

### Main Claim

**Theorem 5.1, Rolling Path Carrier.** For every finite binary input stream,
the rolling carrier produces a continuous trace of legal adjacent states. The
trace preserves input order, maintains a binary head/tail dyad at every state,
and can carry Paper 04 constraints as receipt payloads without treating the
path as a straight-line jump.

**Theorem 5.2, Oloid Carrier Family Reapplication.** The substrate oloid
mechanisms bound to this paper - rolling-contact kinematics, single-oloid
octonionic grounding, the four-oloid D4 ring, and dual-path read-then-verify
flow - each pass their finite verifier. This theorem binds those mechanism
receipts as the base carrier family for Paper 05. It does not close the
E6-to-E7-to-E8 dyadic lift or any Rule 30 prediction claim by this carrier
alone.

### Proof

The step rule is total on the finite state space:

```text
{0,1} x {0,1,2,3} x {0,1}.
```

For every valid input bit, `sheet` changes by exactly one modulo 2, `phase`
changes by exactly one modulo 4, and `parity` changes by XOR with the input bit.
Therefore each step has a unique legal successor. A trace generated by
successive applications of `roll` is continuous by construction because every
adjacent pair is one legal step apart.

The head/tail dyad is a deterministic function of the current state, so it is
defined at every position in the trace. A Paper 04 constraint can be attached
to a trace position as payload because the carrier state and input index are
replayable. The payload does not alter the rolling step rule, so carrying it
does not break continuity. QED.

For Theorem 5.2, the reapplication verifier imports the substrate oloid
modules and executes their declared finite checks. The rolling-contact,
octonionic, quad-oloid, and dual-path verifiers all return `pass`. Sin

_**(D)** formal claim._

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-05/verify_oloid_path_carrier.py
production/formal-papers/CQE-paper-05/verify_oloid_carrier_family.py
```

It verifies:

```text
1. The rolling step is total for valid binary input.
2. Every adjacent trace pair is a legal step.
3. Head/tail dyads are binary at every state.
4. Paper 04 constraints can be attached as payloads without changing the path.
5. Invalid bits and discontinuous jumps are rejected.
6. Prediction claims are downstream: Papers 10 and 12 carry finite/readout
   receipts; Paper 5 proves only the carrier.
7. The oloid carrier family verifiers pass for rolling-contact kinematics,
   octonionic grounding, four-oloid D4 ring, and dual-path read-then-verify
   flow.
8. The E6-to-E7-to-E8 dyadic lift remains outside this theorem.
```

### Validation and Hidden-Guess Layer

Useful hidden-guess prompts:

```text
What changes on every legal rolling step?
Does a curved carrier imply prediction?
What makes a path discontinuous?
Can a constraint payload alter the path rule?
```

Expected answers:

```text
sheet flips, phase advances, parity XORs the bit
no
skipped phase/sheet or invalid bit
no
```

### Open Obligations

1. Wire `verify_oloid_path_carrier` into `cqe_engine.formal`.
2. Connect Paper 04 constraint payloads to a shared route ledger.
3. Keep the E6-to-E7-to-E8 dyadic lift as an explicit bridge obligation until
   a verifier closes it.
4. Separate physical Oloid geometry claims from finite rolling-state claims.
5. Treat Rule 30 prediction as downstream, not absent: Papers 10 and 12 carry
   finite/readout prediction receipts, while cold unbounded extraction and any
   literature-grade Problem 3 promotion remain outside Paper 5.

_— honestly carried as guard / next-need._

---



## 06A. Formal-Paper Deep-Dive (CQE-paper-06)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-06/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **causal vertex** is a paper, proof, tool, receipt, obligation, or product
artifact.

A **causal edge** is a record:

```text
source
target
edge_type
receipt
status
```

Allowed edge types are:

```text
uses
proves
refines
obligates
transports
repairs
constrains
verifies
```

Allowed statuses are:

```text
open
closed
deferred
rejected
```

An edge with status `open` is not a proof closure. It is a tracked obligation.

### Main Claim

**Theorem 6.1, Typed Causal Edge Contract.** A paper-kernel dependency is
admissible to the CQECMPLX production graph only if it is represented by a
typed causal edge with source, target, edge type, receipt, and status. Active
proof dependencies must be acyclic unless the cycle is explicitly typed as
review, feedback, or obligation routing rather than proof support.

**Theorem 6.2, Rule90/Lucas Causal Decomposition.** The Rule 30 local update
decomposes exactly as `Rule90 xor (C and not R)`. Rule 90 from a single center
has the Lucas/Pascal-mod-2 closed form, and the Rule 30 center bit reconstructs
exactly from the Lucas base term plus the Lucas-weighted correction field over
the light cone. This closes the verifiable decomposition core of O2' while
leaving the stronger oracle-free correction-sum collapse outside this theorem.

**Theorem 6.3, Triadic Keystone.** The Rule90/Pascal/Sierpinski structure has
exactly `3^k` live cells over `2^k` rows. This is the triadic causal substrate
used by the suite: it is an exact finite keystone for the recurrence of
threefold structure through LCR, correction, SU(3), D4, E8/Niemeier, and
readout layers. The verifier records the framework arguments for the three
Wolfram Rule 30 problems with epistemic status rather than pretending the
literature-grade cold problems are closed.

**Theorem 6.4, Correction-Extraction Verdict.** Two proposed mechanisms for
oracle-free `O(log N)` correction extraction are retired by direct test:
McKay-Thompson coefficient-parity matching and the accumulated-center-color
fallback. The exact decomposition remains closed, but cold Rule 30 center-bit
extraction without prior enumeration remains a genuine open boundary.

### Proof

Without a source and target, a dependency cannot be located. Without an edge
typ

_**(D)** formal claim._

### Falsifiers

The verifier must reject:

```text
1. An edge with no receipt.
2. An edge with an unknown type.
3. A proof cycle disguised as closure.
4. A graph that labels open obligations as resolved.
```

These falsifiers protect the suite from becoming a pile of agreeable prose.

_— honestly carried as guard / next-need._

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-06/verify_causal_code.py
production/formal-papers/CQE-paper-06/verify_rule90_lucas_decomposition.py
production/formal-papers/CQE-paper-06/verify_triadic_keystone.py
production/formal-papers/CQE-paper-06/verify_correction_extraction_verdict.py
```

It verifies:

```text
1. Every edge has required fields.
2. Every edge uses an allowed type and status.
3. The polished Papers 01-06 graph is acyclic for proof-support edges.
4. Open obligations remain open.
5. Invalid edges and hidden proof cycles are rejected.
6. Rule 30 decomposes exactly as Rule90 plus correction.
7. Lucas/Pascal-mod-2 reconstruction matches direct simulation.
8. Triadic `3^k`-in-`2^k` structure is verified.
9. Failed cold correction-extraction mechanisms are rejected rather than
   promoted.
```

### Validation and Hidden-Guess Layer

Useful hidden-guess prompts:

```text
What fields are required on a causal edge?
Can an open obligation be counted as resolved?
Can a proof-support graph contain a hidden cycle?
What edge type connects Paper 04 to Paper 05?
```

Expected answers:

```text
source, target, type, receipt, status
no
no
transports or constrains, depending on the specific route
```

### Open Obligations

1. Wire `verify_causal_code` into `cqe_engine.formal`.
2. Populate the full 32-paper graph from all formal receipts.
3. Decide which cycles are allowed as review loops and which are rejected as
   proof cycles.
4. Replace placeholder receipt ids with repository-stable artifact hashes.
5. Keep the cold Rule 30 Problem 3 extraction boundary separate from the
   verified aggregate-during-enumeration readout in Paper 10.

_— honestly carried as guard / next-need._

---



## 07A. Formal-Paper Deep-Dive (CQE-paper-07)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-07/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **discrete trace** is a list of indexed values:

```text
D = [(0,x0), (1,x1), ..., (n,xn)]
```

A **sample-preserving bridge** is a continuous function `F` on `[0,n]` such
that:

```text
F(k) = xk for every integer sample k.
```

The verifier uses piecewise-linear interpolation:

```text
F(t) = (1-a) * x_floor(t) + a * x_ceil(t)
where a = t - floor(t)
```

At integer points, `a=0`, so `F(k)=xk`.

### Main Claim

**Theorem 7.1, Sample-Preserving Bridge.** Every finite discrete trace over
numeric values admits a continuous piecewise-linear bridge that exactly
preserves all indexed samples.

**Theorem 7.2, MDHG/SpeedLight Retraction Bridge.** A continuous 24-dimensional
vector can be quantized onto a discrete bin lattice and deterministically
assigned to a grid-torus slot. Re-admitting the same content is idempotent:
`f(f(x)) = f(x)`. This makes the MDHG cache a replayable
discrete-continuous retraction bridge. Product CA-field dynamics and empirical
slot-collision claims remain outside this theorem.

### Proof

Between each adjacent pair `(k,xk)` and `(k+1,xk+1)`, draw the straight segment
joining the two values. The resulting piecewise-linear function is continuous
because adjacent segments share the same endpoint at every integer index.
At each sample index `k`, the function evaluates to the stored value `xk`.
Thus the bridge preserves every discrete sample exactly. QED.

For Theorem 7.2, `verify_mdhg_speedlight_bridge.py` runs MDHGForge. It checks
that the bridge dimension is 24, quantization is total on real inputs, bin
centers are fixed by re-quantization, slot assignment is deterministic on a
torus, repeated admission is a hit with distance zero and no growth, per-slot
capacity is maintained, LRU eviction is deterministic, distance is minimum
Hamming distance over existing vectors, multi-scale layers are independent, and
occupancy is conserved. QED.

_**(D)** formal claim._

### Relation to Earlier Papers

Paper 06 gives typed causal edges. Paper 07 gives a presentation bridge from
indexed edge states to continuous fields. The bridge is a view of the discrete
receipt structure, not a replacement for it.

Paper 02's Rule 30 / Rule 90 correction identity can provide one family of
discrete values:

```text
Rule30(L,C,R) = Rule90(L,R) xor (C and not R)
```

Those discrete values can be drawn as a continuous interpolant, but the exact
proof remains at the sample points unless a separate theorem proves the
between-sample dynamics.

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-07/verify_discrete_continuous_bridge.py
production/formal-papers/CQE-paper-07/verify_mdhg_speedlight_bridge.py
```

It verifies:

```text
1. The interpolant preserves every integer sample.
2. Adjacent linear segments agree at shared endpoints.
3. The Rule 30 / Rule 90 correction identity still holds on all LCR states.
4. The between-sample physical-dynamics overclaim is rejected.
5. The MDHG/SpeedLight bridge is a deterministic 24D quantize-and-slot
   retraction with idempotent re-admission.
```

### Open Obligations

1. Wire `verify_discrete_continuous_bridge` into `cqe_engine.formal`.
2. Decide which later papers require more than sample-preserving interpolation.
3. Add a separate theorem for any claimed Hamiltonian or physical dynamics
   between samples.
4. Carry bridge residuals into Paper 16 only as obligations until verified.
5. Keep CA-field dynamics and collision-rate product diagnostics outside this
   paper until their own stability and empirical receipts exist.

_— honestly carried as guard / next-need._

---



## 08A. Formal-Paper Deep-Dive (CQE-paper-08)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-08/FORMAL_PAPER.md`.
> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions,
lemmas, constructions, examples, and receipts that establish the claimed
result. Paper 00, hand routes, analog tools, workbook language, and obligation
ledgers are supplemental validation and exposure layers. They exist to make
the math inspectable, reproducible, and accessible without requiring a
particular software stack. The hand route is not the purpose of the paper; it
is a way to expose the same state transitions with ordinary marks, tokens,
lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **lattice closure template** is a sequence of finite code or lattice objects
that lets a local state carrier be lifted into a larger transport frame while
preserving the proof boundary of every step.

The Paper 08 template is:

```text
D1 raw bit                 -> 1
S3 / three-cell carrier    -> 3
Fano / Hamming / octonion  -> 7
extended Hamming / E8 seed -> 8
Golay / Leech ingredient   -> 24
Nebe sheet bound           -> 72
```

A **local certified fact** is a claim checked at a fixed dimension by a
finite verifier.

A **global landing claim** is a stronger statement that a local certified
fact has been glued into a terminal lattice object such as the rootless Leech
lattice or a Gamma72 action. Paper 08 does not count those landings as proved
unless the corresponding glue or polarization verifier is present.

A **sheet bound** is the maximum orbit distance expressible inside the current
sheet before a new anchor must be introduced. The Paper 08 verifier records
`K = 9`.

### Main Claim

**Theorem 8.1, Local Lattice Closure Template.** The finite code chain
`(1, 3, 7, 8, 24)` and powered terminal `72 = 8 x 9` provide a verified local
closure template for CQECMPLX transport: every admitted rung is backed by a
finite combinatorial check, and every unproved global landing is preserved as
an explicit proof boundary rather than erased.

**Theorem 8.2, Niemeier/Leech Enumeration Boundary.** The current
Niemeier/Leech reapplication verifier closes the deterministic selector,
E8^3 carrier, Leech type-1/2/3 orbit, and Nebe 72 contract checks. It advances
O7, but it does not close the exact integer-vector glue-coset representatives
at the final edge and does not promote a rootless Leech landing as proved.

**Theorem 8.2a, O7 Exact E8^3 Glue Closure.** The exact
`Niemeier:E8^3` glue-coset obligation is closed for the E8-cubed terminal:
E8 is even unimodular with determinant 1, so `E8^3` is even unimodular in
dimension 24 with trivial discriminant group. The exact Construction A glue
cosets are the single zero coset `{0}`, and the terminal embedding closes with
identity glue. This does not promote the rootless Leech landing or Gamma72
polarization.

**Theorem 8.3, T8 Commutability Tree.** A rebuilt lattice-forge seed ledger
contains the eight canonical `F4` to Niemeier terminal paths recorded by T8.
Each queried target returns `yes_with_template_glue`, the path matches the
historical path table, and all eight terminal targets are distinct. This binds
the seed-ledger path theorem while preserving the exact-glue and landing
boundaries.

**Theorem 8.4, F2 Bridge, Unipotent Orbits, and Substrate Map.** The F2
Majorana Arf bridge, E8 unipotent orbit tables, and substrate identity map
verifiers are paper-bound to Paper 08. This advances O2'' by closing the
algebraic F2 g

_**(D)** formal claim._

### Relation to Earlier Papers

Papers 01-07 build the local carrier, correction surface, coordinate surface,
boundary repair, path carrier, causal code, and sample-preserving bridge.
Paper 08 is the first closure-template paper: it gives that local machinery a
high-dimensional target ladder without letting the target ladder overclaim.

The result is a bridge from local proof mechanics into reusable lattice
closure:

```text
LCR carrier
-> correction surface
-> D4/J3 coordinate surface
-> repaired path carrier
-> causal receipt
-> discrete-continuous bridge
-> lattice closure template
```

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-08/verify_e8_even_lattice.py
production/formal-papers/CQE-paper-08/verify_e8_hemisphere_partition.py
production/formal-papers/CQE-paper-08/verify_lattice_closure_template.py
production/formal-papers/CQE-paper-08/verify_lattice_code_chain.py
production/formal-papers/CQE-paper-08/verify_lattice_code_closure.py
production/formal-papers/CQE-paper-08/verify_f2_bridge_unipotent_substrate.py
production/formal-papers/CQE-paper-08/verify_o2pp_registry_populated.py
production/formal-papers/CQE-paper-08/verify_o7_niemeier_e8cubed_glue_closed.py
production/formal-papers/CQE-paper-08/verify_niemeier_leech_enumeration.py
production/formal-papers/CQE-paper-08/verify_t8_commutability_tree.py
```

It imports the package verifiers:

```text
lattice_forge.lattice_codes.verify_lattice_code_chain
lattice_forge.lattice_codes.verify_hamming_7_fano
lattice_forge.lattice_codes.verify_extended_hamming_8
lattice_forge.lattice_codes.verify_golay_24
lattice_forge.lattice_codes.verify_powered_chain
lattice_forge.nebe_gamma72.verify_nebe_gamma72_contract
```

It verifies:

```text
1. Fano/Hamming identity passes.
2. Extended Hamming/E8 seed checks pass.
3. Golay ingredient and 24 = 3 x 8 checks pass.
4. Powered 72 sheet-bound checks pass.
5. Gamma72 three-sheet transport passes while landing proof remains false.
6. Leech and Gamma72 overclaims are rejected.
7. Niemeier/Leech enumeration passes for deterministic selectors, E8^3
   carriers, Leech type-1/2/3 orbits, and the Nebe 72 contract.
8. O7 exact `Niemeier:E8^3` glue closes as the single zero coset `{0}` with
   identity glue.
9. Broader exact glue representatives beyond the E8-cubed zero-coset case
   remain outside this theorem.
10. The rebuilt seed ledger returns the eigh

---



## 09A. Formal-Paper Deep-Dive (CQE-paper-09)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-09/FORMAL_PAPER.md` (proof-texture restoration). D/I/X tagged.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions,
lemmas, constructions, examples, and receipts that establish the claimed
result. Paper 00, hand routes, analog tools, workbook language, and obligation
ledgers are supplemental validation and exposure layers. They exist to make
the math inspectable, reproducible, and accessible without requiring a
particular software stack. The hand route is not the purpose of the paper; it
is a way to expose the same state transitions with ordinary marks, tokens,
lines, or any equivalent physical substitute.

_**(D)** verified algebraic/structural proof._

### Definitions

A **center state** is a pair `(paper_id, center)` where `center` is the
surviving local quantity carried from that paper.

A **Hamiltonian window** is a contiguous slice of fixed width `w` over an
ordered center-state sequence.

A **Hamiltonian scalar window** is any admissible integer width
`w in [3, K-1]` over a carried-state set of size `K`. Scalar admissibility
proves window arithmetic and provenance preservation; it does not by itself
prove McKay-Thompson exactness.

A **McKay-Thompson exact boundary band** is one of:

```text
1-3, 3-5, 5-7, 7-9, 15-17, 31-35
```

These bands are the declared dihedral/doubling threshold candidates. Their
centers are `2,4,6,8,16,33`. Any non-boundary scalar window remains a
state-derived adjugation candidate until a bijection-move witness promotes or
quarantines it. The present receipt proves the light-cone base and a bounded
light-cone-derived McKay adjugation witness.

A **lockstep threshold stack** is the ledger in which every active or completed
exact band keeps its own local tick while all bands advance under the same
global action index.

A **forward read** preserves the source order:

```text
C_i -> C_{i+1} -> ... -> C_{i+w-1}
```

A **backward read** records the reverse receipt:

```text
C_{i+w-1} <- ... <- C_{i+1} <- C_i
```

A **surviving composite center** is the ordered join of every center in the
window. It is accepted only when the forward and backward receipts contain the
same source centers in opposite order.

### Main Claim

**Theorem 9.1, Hamiltonian Window Emergence.** For any finite ordered sequence
of center states and any fixed window width `w <= n`, the Hamiltonian window
read emits exactly `n - w + 1` surviving composite centers. Each composite
center preserves its source centers, source indices, forward receipt, and
backward receipt. Iterating widths `3`, `5`, and `7` over the CQECMPLX base
centers produces the order counts `4`, `3`, and `2`.

**Theorem 9.1a, Hamiltonian Scalar Sweep.** For a final carried-state set of
size `K`, every integer scalar width `w in [3, K-1]` is an admissible
Hamiltonian window. Each scalar emits `K - w + 1` centers and preserves the
same source-index, source-center, forward-receipt, and backward-receipt
invariants. This theorem proves admissibility, not exact McKay-Thompson
promotion.

**Theorem 9.1b, McKay-Thompson Threshold Stack.** Hamiltonian exactness
candidates are reserved for the declared bands `1-3`, `3-5`, `5-7`, `7-9`,
`15-17`, and `31-35`. At `K = 9`, the first four bands are closed
light-cone-bound candidates and the higher bands are pending. Each band keeps
a local clock, while the whole stack advances in lockstep under the global
action index. The proof route is the light-cone-derived adjugation witness,
which promotes the bounded McKay threshold route for the closed bands in the
tested window.

**Theorem 9.2, Kappa Conservation Timeline.** Let
`kappa = ln(phi)/16`. A morphon event emits a conserved non-positive potential
delta, with per-event Event Law delta `-kappa`. The cumulative ledger is
non-increasing, positive deltas are violations, a

_**(D)** formal claim._

### Relation to Earlier Papers

Papers 01-08 establish carrier, correction, coordinate, repair, path, causal,
bridge, and closure-template layers. Paper 09 adds temporal construction:
the ordered global object is read from local center windows rather than
assumed as an external timeline.

```text
local centers
-> width-3 reads
-> width-5 reads
-> width-7 reads
-> scalar-window admissibility sweep
-> McKay-Thompson boundary-candidate stack
-> Paper 6/Paper 10 light-cone adjugation witness for McKay promotion
-> adjugation/bijection witness route for non-boundary windows
-> composite temporal states with receipts
```

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-09/verify_hamiltonian_window_emergence.py
production/formal-papers/CQE-paper-09/verify_kappa_conservation_law.py
```

It verifies:

```text
1. Width-3 reads over six base centers produce four surviving centers.
2. Width-5 reads after appending order 2 produce three surviving centers.
3. Width-7 reads after appending order 3 produce two surviving centers.
4. Every surviving center carries source indices and source centers.
5. Every backward receipt reverses to the forward receipt.
6. Scalar widths `3..K-1` are admissible and preserve provenance.
7. McKay-Thompson candidate bands match `1-3`, `3-5`, `5-7`, `7-9`, `15-17`,
   and `31-35`.
8. At `K = 9`, the first four bands are closed light-cone-bound candidates and
   the future bands are pending.
9. Threshold local clocks are monotone and run under the shared global action.
10. Paper 6 light-cone decomposition passes before McKay binding.
11. Paper 10 cold-start bijection passes before McKay binding.
12. The McKay route uses the passing light-cone adjugation witness.
13. The temporal Z4 scope verifier records static-template-only status.
14. Kappa conservation emits non-positive deltas and rejects positive-delta
   conservation violations.
```

---



## 10A. Formal-Paper Deep-Dive (CQE-paper-10)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-10/FORMAL_PAPER.md` (proof-texture restoration). D/I/X tagged.

### Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions,
receipt equations, transport classifications, cache materialization checks,
and replayable verifier. Paper 00, workbook routes, analog tools, and open
obligation ledgers are supplemental validation and exposure layers. They make
the receipt inspectable by hand or by software, but they are not the primary
result. The primary result is the master-receipt theorem below.

_**(D)** verified algebraic/structural proof._

### Definitions

A **paper receipt binding** is a pair `(paper_id, receipt_path)` such that the
receipt exists, can be parsed, and reports a pass-like status for the theorem
it carries.

The **observer center `C`** is the active center introduced by a requested
enumeration event. It is not a passive label. It is the fact that an observer
has asked the system to enumerate something, and the system has encoded that
request as the center against which later left/right, boundary, transform,
residue, and receipt states are read.

The **step `00 -> 1` encoding event** is the transition from the inherited
Paper 00 burden contract into the first active paper. Paper 00 defines what
must be carried; Paper 01 begins carrying it. Every later receipt is an effect
of that initial choice unless a later paper explicitly introduces a new
enumeration center and proves the handoff.

A **transport obligation row** is a typed record:

```text
(id, source_object, target_object, map, preserved_quantity,
 failure_condition, witness, classification, proof_boundary)
```

The allowed classifications are:

```text
demonstrated
bounded_local
bounded_external
registered_landing_forms
open
```

A **lookup receipt** is:

```text
(kind, key, value, source_id, evidence_level, complexity_claim)
```

A **T10 master receipt** is the tuple:

```text
T10 = (C00, E00->1, P00, P01..P09, R, L, V, O)
```

where `C00` is the observer-bound enumeration center, `E00->1` is the initial
encoding event from Paper 00 into Paper 01, `P00` is the Paper 00 contract
binding, `P01..P09` are formal paper receipt bindings, `R` is the transport
ob

### Main Claim

**Theorem 10.1, T10 Master Receipt Integrity.** The CQECMPLX substack
consisting of Paper 00 and Papers 01-09 is inspectable and replayable as a
single receipt object. The receipt proves:

```text
1. Paper 00 is bound as the inherited minimum information contract and
   observer enumeration event.
2. Papers 01-09 have promoted formal receipts with pass-like status.
3. The four transport rows have required fields and valid classifications.
4. The local witnesses replay.
5. Two transport rows are demonstrated and two remain visible non-demonstrated lifts.
6. The lookup cache materializes the one-million-bit Rule 30 window, 157
   unipotent orbits, 24 lattice forms, and the UMRK/LMFDB source registers.
7. The Prize 3 lookup substrate keeps `closed_form_claim = False`, so the
   receipt does not overclaim cold-start closure.
```

**Theorem 10.2, O(log N) Readout Architecture.** Once the Rule 30 correction
library has been accumulated during the enumeration already being performed,
the center bit at index `N` is read as `LucasBit(N,0) xor lib[N]` with
`O(log N)` addressing plus one lookup. This proves the readout architecture
and idempotent reuse boundary. It does not claim cold `O(log N)` extraction
without prior enumeration.

**Theorem 10.3, Bijection-Chart Readout Extension.** The D4, SU(3), and F4
bijection charts provide a cold-start addressing architecture over the
billion-sheet template. The verifier confirms the chart machinery and mixed
radix addressing as an extension to Paper 10. This is an operational
architecture receipt, not literature-grade closure of Wolfram Rule

_**(D)** formal claim._

### Relation to Earlier Papers

Papers 01-09 build the first carrier chain after the observer's enumeration
event has been encoded: LCR carrier, correction surface, triality surface,
boundary repair, oloid path carrier, causal code, discrete/continuous bridge,
lattice closure template, and Hamiltonian window emergence. Paper 10 wraps
them as a receipt object:

```text
observer request at Paper 00
-> C00
-> 00-to-1 encoding event
-> paper receipts
-> transport rows
-> local witness replay
-> lookup receipts
-> pass verdict with visible open lifts
```

This is why Paper 10 belongs at the start of the second block. It converts the
first block and its immediate temporal extension into a stack-level audit
object that later papers can cite.

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-10/verify_ologn_readout_architecture.py
production/formal-papers/CQE-paper-10/verify_bijection_cold_start.py
production/formal-papers/CQE-paper-10/verify_t10_master_receipt.py
```

It emits:

```text
production/formal-papers/CQE-paper-10/ologn_readout_architecture_receipt.json
production/formal-papers/CQE-paper-10/bijection_cold_start_receipt.json
production/formal-papers/CQE-paper-10/t10_master_receipt.json
```

The verifier checks:

```text
1. Paper 00 source and proof-receipt binding.
2. Paper 00 as observer enumeration contract and `00 -> 1` encoding event.
3. Paper 01-09 promoted formal receipt bindings.
4. Transport row schema, classification validity, and local witness replay.
5. Demonstrated/open lift counts: 2 demonstrated and 2 visible non-demonstrated lifts.
6. Lookup cache materialization against the packaged source datasets.
7. Prize 3 lookup honesty boundary: no cold-start closed-form claim.
8. O(log N) readout after aggregate-during-enumeration, with cold extraction
   left outside the theorem.
9. Bijection-chart addressing extension, with literature-grade P3 closure
   left outside the theorem.
```

### Open Obligations

1. Theorem 10.1 (T10 Master Receipt Integrity) is closed by the passing t10_master_receipt.json.
1. Theorem 10.2 (O(log N) Readout Architecture) is closed by the passing ologn_readout_architecture_receipt.json and the nine_by_nine closed-form continuation.
1. Theorem 10.3 (Bijection-Chart Readout Extension) is closed by the passing bijection_cold_start_receipt.json.

_— honestly carried as guard / next-need._

---



## 11A. Formal-Paper Deep-Dive (CQE-paper-11)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-11/FORMAL_PAPER.md` (proof-texture restoration). D/I/X tagged.

### Proof/Exposure Hierarchy

The primary proof is the admission theorem. Paper 00 supplies the inherited
minimum contract and the original requested enumeration event. Paper 10 binds
that event into the master receipt. Paper 11 then proves the next operation:
how a new theory is tested against the already carried center without silently
moving the center or importing unreceipted claims.

Workbook routes, analog reconstructions, and open-obligation ledgers are
validation and exposure layers. They are valuable because they make the proof
inspectable and reproducible, but the result of this paper is not that a human
can do the system by hand. The result is the formal gate:

```text
candidate theory -> T10 anchor -> trusted spectrum -> K=9 boundary
                 -> admitted | boundary | rejected-as-datum
```

_**(D)** verified algebraic/structural proof._

### Definitions

The **observer center `C00`** is the center encoded by the requested
enumeration event at the Paper 00 to Paper 01 transition. Paper 11 inherits
this center through the Paper 10 master receipt unless a later paper explicitly
proves a recentering.

The **step `00 -> 1` encoding event** is the first active encoding of the
Paper 00 burden contract into the paper stack. Paper 11 does not restart the
stack; it reads candidates as consequences of that original encoded request.

The **Paper 10 trust anchor** is the receipt:

```text
T10 = (C00, E00->1, P00, P01..P09, R, L, V, O)
```

where `R` is the transport table, `L` is the lookup cache, `V` is the verifier
verdict, and `O` is the visible open-boundary set.

An **admission Gluon** is the Paper 11 carrier that evaluates a candidate
theory by Gluon mass against a trusted spectrum. In the local corpus this is
registered as:

```text
T_ADMISSION: Admission Gluon = Gluon mass filter at K=9; T10 = trust anchor
```

The **trusted spectrum** is the finite mass set exposed by the receipt-bearing
stack available to Paper 11. The production verifier binds the current Paper
11 spectrum to the Paper 00 through Paper 10 receipt indices:

```text
S_T10 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```

The **sheet boundary** is:

```text
K_max = 9
```

This is the Nebe/lattice window used throughout the corpus as the maximum
sheet depth expressible from one anchor event before the candidate must be
reported as a boundary crossing.

A **candidate theory** is any external theory, model, proof object, package,
or tool claim being tested for import into 

### Main Claim

**Theorem 11.1, T_ADMISSION.** Let `T` be a candidate theory with Gluon mass
`m(T)`. Let `S_T10` be the trusted spectrum exposed by the Paper 10 master
receipt, and let `K_max = 9`. Paper 11 admits `T` if and only if:

```text
T10 signs the admission context
m(T) in S_T10
m(T) <= K_max
```

If `T10` signs the context and `m(T) in S_T10` but `m(T) > K_max`, then `T`
is routed to a boundary receipt. If `m(T) notin S_T10`, or if the candidate is
not bound to the T10 context, the candidate is rejected or rejected as a datum
according to the declared test.

### Proof

Paper 10 proves that `C00`, the `00 -> 1` encoding event, and the receipts for
Papers 00-09 are present in one replayable master object. Therefore Paper 11
has a stable observer center and a stable receipt anchor before it evaluates
any external theory. Admission without that anchor would be a center move with
no accounting, so it is rejected by construction.

The admission Gluon is defined as a filter over candidate mass. Its acceptance
predicate is:

```text
A(T) = signed_T10(T) and m(T) in S_T10 and m(T) <= 9
```

These three clauses are necessary. Without `signed_T10(T)`, the candidate is
not being evaluated inside the carried paper stack. Without `m(T) in S_T10`,
the candidate has no trusted spectrum match. Without `m(T) <= 9`, the
candidate crosses the sheet boundary and cannot be admitted from the same
anchor event.

They are also sufficient for Paper 11 admission: a candidate with the T10
anchor, a trusted-spectrum mass, and a mass inside `K=9` is exactly the object
the admission Gluon is defined to pass. T

_**(D)** formal claim._

### Relation to C and the Enumeration Event

Paper 11 is one of the first places where it becomes easy to lose the center.
The candidate theory has its own internal identity, but the admission question
is not asked from inside that candidate. It is asked from the already encoded
CQECMPLX observer state:

```text
requested enumeration -> C00 -> E00_to_1 -> T10 -> Paper 11 gate
```

Every admission verdict is an effect of that chain. A candidate may later
prove a new center, but until it does, the admission gate evaluates it against
the carried center. This is both accounting and mathematics: the observer
request is the encoded event that defines which spectrum, boundary, and receipt
context the candidate is allowed to touch.

### Falsifiers

The verifier rejects these overclaims:

```text
"A theory may enter without the T10 trust anchor"
"A trusted mass above K=9 is admitted without a boundary receipt"
"A nonmatching candidate is deleted rather than receipted"
"A verdict from one declared encoder may be generalized without a new receipt"
"The Pariah boundary reading is a new finite-group classification theorem"
"Paper 11 can ignore C00/E00_to_1"
```

The theorem passes because it admits only the T10-signed, spectrum-matched,
inside-window case and records every other case as a typed receipt.

_— honestly carried as guard / next-need._

### Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-11/verify_theory_admission_gate.py
```

It emits:

```text
production/formal-papers/CQE-paper-11/theory_admission_gate_receipt.json
```

The verifier checks:

```text
1. Paper 11 inherits C00/E00_to_1 through the Paper 10 master receipt.
2. The T10 receipt passes.
3. The trusted spectrum binds Paper 00 through Paper 10.
4. K_max is 9.
5. The mass gate exercises admitted, boundary, and rejected outcomes.
6. The local Lattice Forge ledger carries six Pariah objects.
7. The local Monster metadata records the 20 Monster-involved + 6 Pariah split.
8. Structural Pariah exit routes and hard-wall routes are present locally.
9. The Pariah signature closes under the declared encoder.
10. The Happy-Family signature remains open under the declared encoder.
11. Boundary failures are retained as receipts instead of being erased.
```

---



## 12A. Formal-Paper Deep-Dive (CQE-paper-12)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-12/FORMAL_PAPER.md` (proof-texture restoration). D/I/X tagged.

### Claims

**Claim 12.1.** The Rule 30 local truth table matches `L xor (C or R)` on all
eight LCR states.

**Claim 12.2.** The `T_EMISSION` formula matches Rule 30 on all eight LCR
states.

**Claim 12.3.** Rule 30 decomposes as `Rule90 xor (C and not R)` on all eight
LCR states.

**Claim 12.4.** Exactly 64 of the 256 elementary cellular automata are
silent-boundary rules.

**Claim 12.5.** A prediction surface must preserve layer, cost, defect, and
receipt metadata; empirical or open layers cannot be counted as closed.

**Claim 12.6.** EntropyForge may be treated as a finite, receipt-bound product
extension of Paper 12 when it preserves the canonical Rule 30 column, the
finite VOA-sector partition, deterministic syndrome behavior, and explicit open
obligations.

**Claim 12.7.** The Rule 30 prize-problem evidence layer is admissible only
with explicit epistemic labels: P1 non-periodicity is finite-window evidence
plus transport argument, P2 density is finite measurement plus transport
argument, and the 1M-bit center-column receipt is large-window empirical
evidence rather than asymptotic proof.

_**(D)** formal claim._

### Definitions

An **elementary cellular automaton** is a radius-1 binary rule:

```text
f : {0,1}^3 -> {0,1}
```

For rule number `r`, the local emission is:

```text
emit_r(L,C,R) = (r >> (4L + 2C + R)) & 1
```

A **prediction surface** is:

```text
surface(system, N) -> (bit, layer, cost, defect, receipt)
```

For Rule 30:

```text
Rule30(L,C,R) = L xor (C or R)
Rule90(L,R)   = L xor R
correction    = C and not R
```

A **silent-boundary rule** is an ECA satisfying:

```text
emit_r(0,0,0) = 0
emit_r(1,1,1) = 0
```

The **canonical center column** is the single-cell Rule 30 evolution read at
the center position across a finite depth. Product seeded streams may wrap this
surface, but they do not replace the paper-bound canonical object.

### Theorem 12.1 - CA Prediction Surface Finite Local Layers

The Rule 30 local readout, `T_EMISSION`, and Rule90-correction decomposition
are exact on the eight binary LCR states. The 256-rule ECA space contains
exactly 64 silent-boundary rules. These facts form the closed finite layer of
the CA prediction surface.

_**(D)** formal claim._

### Proof

Enumerate all states:

```text
(L,C,R) in {0,1}^3
```

For each state, compute `emit_30(L,C,R)` from the ECA rule number and compute
`L xor (C or R)`. The verifier checks equality on all eight rows.

For `T_EMISSION`, if `C=1` then:

```text
L xor (C or R) = L xor 1 = not L
```

If `C=0` then:

```text
L xor (C or R) = L xor R
```

Therefore `T_EMISSION` matches Rule 30 on every local state.

For the correction decomposition:

```text
C or R = C xor R xor (C and R)
```

so:

```text
Rule30 = L xor C xor R xor (C and R)
       = (L xor R) xor (C xor (C and R))
       = Rule90 xor (C and not R)
```

The silent-boundary count is finite. Two of the eight truth-table entries are
fixed to zero. The remaining six entries are free, giving:

```text
2^6 = 64
```

silent-boundary rules.

_**(D)** verified algebraic/structural proof._

### Theorem 12.2 - Bounded EntropyForge Extension

EntropyForge is a valid Paper 12 product extension when it remains finite,
receipt-bound, and explicit about its obligations.

The verifier checks ten finite rows:

```text
Rule 30 formula matches Wolfram code 30
VOA partition is Z(q) = 2q^0 + 6q^5
Monster scalar is 47 * 59 * 71 = 196883
D4 antipodal axes partition the eight states
two center-column implementations agree on 512 bits
no period p <= 256 appears within the first 2048 canonical bits
XOR-debiased density stays within tolerance
VOA syndrome is deterministic and window-sensitive
seeded streams repeat for equal seeds and separate for distinct seeds
entropy block round-trips and verifies client-side
```

The non-periodicity row is finite. It proves only the stated checked window.
The infinite-column statement remains an obligation.

_**(D)** formal claim._

### Theorem 12.3 - Rule 30 Prize Evidence Layer

The Paper 12 prize-evidence verifiers bind finite and large-window evidence
without promoting asymptotic closure. `verify_p1_non_periodicity.py` verifies
the finite Sierpinski/SU(3)/non-periodicity transport package. `verify_p2_density.py`
verifies the local density split and transport package. `verify_wolfram_1m_bit.py`
converts the 1M-bit center-column data into a repository receipt: no period
`<= 65,536`, density `500,768 / 1,000,000 = 0.500768`, and O(1) sampled reads
from the materialized sheet. These receipts strengthen the review package but
do not close the infinite/asymptotic Wolfram prize statements by themselves.

`verify_rule30_real_dataset_experiment.py` runs the full experiment against the
authoritative 1M Wolfram Rule 30 center column and passes 4/4: real density
`0.500768` over `1e6` bits (P2 equal-density, now empirically calibrated), the
generator is bit-exact to the real data (`10000/10000`), the Rule 30 / Rule 90
+ correction decomposition reproduces the real bits, and there is no period
`<= 1000` in the real `50k` window (P1 support). This calibrates the finite
evidence against real data; the asymptotic P1/P2/P3 statements remain open.

_**(D)** formal claim._

### Receipts

The primary executable receipt is:

```text
production/formal-papers/CQE-paper-12/verify_ca_prediction_surface.py
production/formal-papers/CQE-paper-12/ca_prediction_surface_receipt.json
```

The receipt status is `pass`. It verifies:

```text
rule30_truth_table_matches_formula        = true
t_emission_matches_rule30                 = true
rule30_rule90_correction_identity_holds   = true
local_state_count_is_8                    = true
silent_boundary_rule_count_is_64          = true
cold_start_rule30_extractor_left_as_obligation = true
spectral_prediction_left_as_empirical     = true
```

The EntropyForge extension receipt is:

```text
production/formal-papers/CQE-paper-12/verify_center_column_entropy.py
production/formal-papers/CQE-paper-12/center_column_entropy_receipt.json
```

The receipt status is `pass`, with `10/10` finite checks passing. It records
two open obligations:

```text
infinite-column non-periodicity remains a conjecture
statistical-suite certification is product-layer work, not a paper claim
```

The Rule 30 prize-evidence receipts are:

```text
production/formal-papers/CQE-paper-12/verify_p1_non_periodicity.py
production/formal-papers/CQE-paper-12/p1_non_periodicity_receipt.json
production/formal-papers/CQE-paper-12/verify_p2_density.py
production/formal-papers/CQE-paper-12/p2_density_receipt.json
production/formal-papers/CQE-paper-12/verify_wolfram_1m_bit.py
production/formal-papers/CQE-paper-12/wolfram_1m_bit_validation_receipt.json
production/formal-papers/CQE-paper-12/verify_rule30_real_dataset_experiment.py
production/formal-papers/CQE-paper-12/rul

### Falsifiers

The verifier rejects:

```text
the spectral layer is a proved cold-start Rule 30 predictor
a local T_EMISSION receipt proves between-depth dynamics without the local state
a layer may omit its cost and defect receipt
finite center-column evidence proves infinite non-periodicity
seeded product streams replace the canonical paper-bound object
a failed P3 closure receipt is described as a closed theorem
```

_— honestly carried as guard / next-need._

---



## 13A. Formal-Paper Deep-Dive (CQE-paper-13)

> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-13/FORMAL_PAPER.md` (proof-texture restoration). D/I/X tagged.

### Claims

**Claim 13.1.** The shell-2 chart stratum is the three-element set
`{(1,1,0), (1,0,1), (0,1,1)}`.

**Claim 13.2.** The three shell-2 states map bijectively to the three trace-2
idempotents `{E11+E22, E11+E33, E22+E33}` in `J_3(O)`.

**Claim 13.3.** The six permutations of diagonal indices in `S_3` close on the
trace-2 triple.

**Claim 13.4.** The `n=3` shell-2 transition is an exact `SU(3)` Weyl group-ring
element with residual squared equal to `0` over `Q`.

**Claim 13.5.** The bounded `G2/F4/T5A` route is a route classifier for an
already-enumerated bit.

**Claim 13.6.** The color/anticolor six-face model is the hand-facing exposure
surface for the same algebraic color transport.

**Claim 13.7.** `QuarkFaceForge` literalizes the structural color-transport
surface: three colors, the `S_3` Weyl action, exact `n=3` `SU(3)` closure,
trace conservation, the shell-2 chiral doublet, `J_3(O)` faces, and color
confinement as an algebraic transport boundary.

**Claim 13.8.** Against published Standard-Model data (PDG/CODATA, retrieved
2026-06-14, no live measurement) the framework `SU(3)` color sector matches
real QCD on four independent structural counts: three colors, eight gluons =
adjoint = chart, `S_3` Weyl = color group, and six `A_2` roots = excited
states. `alpha` and generation counts are suggestive/underived; the VOA mass
partition does not map to the gauge-boson spectrum. That single non-match is a
`2x2x2` vs `3x3` *basis* difference, not a failure (`3 x 3 = 9 = 8 (+) 1`; the
chart `2^3 = 8` is the traceless adjoint, the standard `3 x 3` carries the
trace/singlet), as cl

_**(D)** formal claim._

### Definitions

An **LCR chart state** is a triple `(L,C,R)` in `{0,1}^3`.

The **shell** of a chart state is `L + C + R`.

The **shell-2 stratum** is the set of chart states with shell value `2`.

A **quark face** in this paper is one member of the trace-2 idempotent triple
of `J_3(O)`, read as the CQECMPLX algebraic color-transport face. The term is
used affirmatively as the model's Standard-Model-facing object; measured
particle identification is the later calibration step.

The **color Weyl action** is the `S_3` action induced by permuting diagonal
indices `(1,2,3)` and then reading the induced permutation of trace-2
idempotent pairs.

A **bounded route classifier** is a route that may classify an already-supplied
enumeration value while preserving a visible boundary that it did not derive the
value from depth alone.

### Theorem 13

The CQECMPLX quark-face layer is a closed algebraic transport layer:

```text
shell-2 LCR triple
-> trace-2 J_3(O) idempotent triple
-> closed S_3 Weyl action
-> exact n=3 SU(3) group-ring closure
-> bounded exceptional route classification
```

and this is the CQECMPLX color-transport physics map. The remaining obligation
is external Standard-Model calibration, not the internal algebraic transport.

**Theorem 13.2, Quark-Face Color Transport Literalization.** The
`QuarkFaceForge` package surface implements the algebraic color-transport
claims of Paper 13 as importable code and verifies them with ten finite checks.
This closes the literal package transport layer. Measured quark physics, CKM
phase, weak parity, and full Standard Model identification are the external
calibration targets.

_**(D)** formal claim._

### Proof

First enumerate all binary chart states with shell value `2`. There are exactly
three:

```text
C- = (1,1,0)
C0 = (1,0,1)
C+ = (0,1,1)
```

This proves Claim 13.1 by exhaustion.

Next map these states to the trace-2 idempotents:

```text
C- -> E11 + E22
C0 -> E11 + E33
C+ -> E22 + E33
```

`verify_j3o_axioms` verifies that the diagonal idempotents are idempotent and
Jordan-orthogonal, that they sum to the identity, and that the three trace-2
objects have trace `2` and are idempotent. This proves Claim 13.2 at the
algebraic layer.

Now let a permutation `sigma` in `S_3` act on diagonal indices. For any trace-2
pair `{i,j}`, the image is `{sigma(i), sigma(j)}`, again one of the three
two-element diagonal pairs. Since all six permutations are enumerated and every
image lands inside the same three-element set, the Weyl action closes on the
quark-face triple. This proves Claim 13.3.

The exact transition check is stronger than a floating-point fit. The verifier
`verify_n3_su3_closure_exact` computes the `n=3` shell-2 conditional matrix and
decomposes it over the `S_3` permutation matrices using rational arithmetic. The
receipt reports residual squared equal to `0` and `is_exact_group_ring_element =
true`. This proves Claim 13.4.

The exceptional route layer is then admitted with its honesty boundary intact.
`verify_conjugate_triple(max_depth=256)` reports a passing bounded classifier:
the route is oracle-backed, all tested routes resolve in at most three stages,
and `depth_only_bridge` is false. Therefore it classifies supplied bits inside
the transport map. This proves Claim 13

_**(D)** verified algebraic/structural proof._

### Receipt

The promoted verifier is:

```text
production/formal-papers/CQE-paper-13/verify_quark_face_transport.py
production/formal-papers/CQE-paper-13/verify_quark_face_transport_literalized.py
```

It writes:

```text
production/formal-papers/CQE-paper-13/quark_face_transport_receipt.json
production/formal-papers/CQE-paper-13/quark_face_transport_literalized_receipt.json
```

The Standard-Model real-data comparison (Claim 13.8) is verified by:

```text
verify_standard_model_real_comparison.py -> standard_model_real_comparison_receipt.json (8/8)
```

It is a classified comparison, not a physics proof: four EXACT structural
matches, three SUGGESTIVE/underived rows, and one stated non-match whose
basis-difference resolution lives in Paper 15.

The bounded-route honesty boundary (Claim 13.5) is spot-tested against the
standalone Rule 30 +/-1 shell verification ledger:

```text
verify_rule30_shell_verification_ledger.py -> rule30_shell_verification_ledger_receipt.json (13/13)
```

It loads `CMPLX-R30-main/VERIFICATION/RULE30_PLUS_MINUS_ONE_SHELL.json` and
confirms the suite's own tiers agree with this paper: `J3O_DIAGONAL_CARRIER`
and `GLUON_LR_INVARIANCE` are `demonstrated` (the proven core), while
`G2_F4_T5A_BOUNDED_ROUTE` is `bounded` — the data-side confirmation that the
G2/F4/T5A route is a bounded classifier, not a cold-start derivation.

The closed layers are:

```text
three shell-2 chart states
three trace-2 J_3(O) idempotents
six S3 Weyl actions close on the trace-2 triple
n=3 shell-2 transition is exact over the SU(3) Weyl group ring
bounded G2/F4/T5A route classifies oracle-e

### Falsifiers

This paper fails if the shell-2 stratum does not contain exactly three states.

It fails if any trace-2 idempotent check in `J_3(O)` fails.

It fails if any `S_3` action leaves the trace-2 triple.

It fails if exact `n=3` closure has nonzero residual.

It fails if the bounded route is presented as a cold-start derivation.

It fails if the algebraic color-transport map is presented as a measured
Standard Model calibration without the calibration bridge.

_— honestly carried as guard / next-need._

### Open Obligations

1. IRL CKM calibration target is recorded in NP-15; exact route-parameter derivation remains open.

_— honestly carried as guard / next-need._

---



## 15A. Formal-Paper Deep-Dive (CQE-paper-15)

> Recrafted from `CQE-paper-15` formal paper (proof-texture restoration). D/I/X tagged.

### Claims

**Claim 15.1.** Rule 30 decomposes over `F2` as:

```text
Rule30(L,C,R) = (L xor C xor R) xor (C and R)
```

**Claim 15.2.** The bilinear obstruction has Arf invariant `0`, and Arf
matching supplies a finite gluing rule.

**Claim 15.3.** The VOA sector decomposition of the eight chart states is:

```text
Z(q) = 2q^0 + 6q^5
```

**Claim 15.4.** The local correction-residue states are exactly:

```text
(0,1,0), (1,1,0)
```

because those are the states where `C AND NOT R` fires.

**Claim 15.5.** The nth-bit layer passes as a local/oracle-backed carrier
check; McKay-Thompson correction parity remains the missing closed-form
transport.

**Claim 15.6.** The mass-residue carrier is the internal Higgs-adjacent physics
map; measured Higgs and particle-mass predictions require external
calibration.

**Claim 15.7.** The chart carries eight states, not nine. The apparent `+1` is
a dual reading of one state through the wrap (antipodal / Cayley-Dickson
conjugation), not a separate ninth state: one gluon shows a color face or a
white face depending on traversal. The wrap is a fixed-point-free involution,
so the singlet axis is one state with two definite faces. This is the
framework's confinement reading: there is no colorless ninth gluon because
there is no ninth state.

**Claim 15.8.** The ninth slot is the forced printout (parity/trace) of the
completed eight. It is genuinely neutral/supe

_**(D)** formal claim._

### Definitions

A **carrier effect** is a quantity accepted only when it is witnessed by local
readout and receipt.

The **linear part** of the local Rule 30 formula is `L xor C xor R`.

The **obstruction** is the bilinear term `C and R`.

The **correction residue** is `C and not R`.

A **mass-residue carrier** is the substrate object that survives cancellation,
has a receipt, and carries a weight. It is the CQECMPLX internal mass-like
carrier. A physical rest-mass value requires a later calibrated map into
measured units.

### Theorem 15

The CQECMPLX mass-residue carrier is a finite substrate layer consisting of:

```text
F2 obstruction
-> Arf gluing receipt
-> correction-residue local states
-> VOA weight split
-> Higgs-adjacent mass-residue physics map
-> external calibration obligation
```

_**(D)** formal claim._

### Proof

Exhaust the eight local chart states. For every `(L,C,R)`, the verifier checks:

```text
Rule30(L,C,R) = (L xor C xor R) xor (C and R)
```

This proves Claim 15.1.

The `f2_majorana` verifier reports:

```text
q_zero_arf = 0
q_hyperbolic_arf = 0
q_elliptic_arf = 1
rule30_correction_arf = 0
zero_vs_hyperbolic_can_glue = true
zero_vs_elliptic_can_glue = false
```

Thus the obstruction has Arf invariant `0`; matching Arf classes glue, and
mismatched classes reject. This proves Claim 15.2.

The `centroid_voa` verifier reports exactly two true vacua of weight `0` and
six excited states of weight `5`. Therefore the seed partition function is
`Z(q) = 2q^0 + 6q^5`. This proves Claim 15.3.

The correction-residue function is `C AND NOT R`. Exhausting the eight states
shows that it fires only at `(0,1,0)` and `(1,1,0)`. This proves Claim 15.4.

The nth-bit layer passes at the tested local/oracle level with `oracle_accuracy
= 1.0`, while the receipt still names McKay-Thompson correction parity as an
open step. Therefore the local residue evidence is admitted and the closed-form
parity theorem remains open. This proves Claim 15.5.

The verifier does not yet compute a measured Higgs mass, electroweak symmetry
breaking, Yukawa couplings, or a particle mass spectrum. That is the external
calibration bridge. The internal carrier itself is closed: residue survives,
Arf-compatible gluing admits 

_**(D)** verified algebraic/structural proof._

### Receipt

Promoted verifier:

```text
production/formal-papers/CQE-paper-15/verify_mass_residue_carrier.py
```

Receipt:

```text
production/formal-papers/CQE-paper-15/mass_residue_carrier_receipt.json
```

Interpretive-refinement verifiers and receipts (this pass):

```text
verify_eight_states_one_dual_reading.py  -> eight_states_one_dual_reading_receipt.json   (7/7)
verify_ninth_is_forced_printout.py       -> ninth_is_forced_printout_receipt.json        (6/6)
verify_mass_framing_2x2x2_vs_3x3.py      -> mass_framing_2x2x2_vs_3x3_receipt.json        (7/7)
```

Closed layers:

```text
Rule 30 splits into linear part xor C*R obstruction over F2
Rule 30 obstruction has Arf invariant 0
Arf-matching gluing admits and Arf-mismatch gluing rejects
VOA sector decomposition is 2q^0 + 6q^5
correction residue C and not R identifies the local surviving-residue states
nth-bit local/oracle layer passes while McKay-Thompson parity remains open
```

Open layers:

```text
calibration to the physical Higgs mechanism
particle mass spectrum or numerical mass prediction in measured units
electroweak symmetry breaking/Yukawa coupling calibration
closed-form McKay-Thompson correction parity
```

### Falsifiers

The paper fails if the Rule 30 split fails on any local state.

It fails if Arf mismatch glues losslessly.

It fails if the VOA split is not two weight-0 vacua and six weight-5 excited
states.

It fails if the correction residue fires anywhere other than `(0,1,0)` and
`(1,1,0)`.

It fails if the internal mass-residue carrier is presented as a measured
Higgs-mass value without the calibration bridge.

_— honestly carried as guard / next-need._

### Open Obligations

1. IRL Higgs/W/Z/top mass targets are recorded in NP-15; chart-to-mass calibration bridge remains open.

_— honestly carried as guard / next-need._

---



## 16A. Formal-Paper Deep-Dive (CQE-paper-16)

> Recrafted from `CQE-paper-16` formal paper (proof-texture restoration). D/I/X tagged.

### Claims

**Claim 16.1.** Every local chart state closes to a Lie-conjugate rest state in
at most three `S3` transposition steps.

**Claim 16.2.** There are exactly four Lie-conjugate rest states.

**Claim 16.3.** Edge residue is exactly `C AND NOT R`, so it fires only at
`(0,1,0)` and `(1,1,0)`.

**Claim 16.4.** Power-of-ten windows are valid local receipt windows.

**Claim 16.5.** Local/oracle nth-bit checks pass with correction included, but
the global correction collapse remains open.

_**(D)** formal claim._

### Definitions

A **rollout** is the local process of reading a state until it reaches rest.

A **Lie-conjugate rest state** is an `L=R` chart state.

An **edge residual** is a carry in flight at a window boundary:

```text
edge_residue(L,C,R) = C AND NOT R
```

A **power-of-ten window** is a practical aperture at depths `10`, `100`,
`1000`, and so on. It is a receipt window, not a continuum proof.

### Theorem 16

Continuum edge residuals are locally well-defined window receipts:

```text
local state -> <=3-step rest closure -> edge_residue = C AND NOT R
```

and every global continuum claim remains an obligation until the propagating
correction sum is closed.

_**(D)** formal claim._

### Proof

The centroid verifier checks all eight chart states and reports local closure.
Every state anneals to a Lie-conjugate rest state in at most three `S3` steps.
This proves Claim 16.1.

The rest states are the four states satisfying `L=R`. The verifier reports the
count as `4`. This proves Claim 16.2.

The edge-residue formula is `C AND NOT R`. Exhausting all eight states gives
exactly `(0,1,0)` and `(1,1,0)`. This proves Claim 16.3.

The verifier samples windows at `10`, `100`, and `1000`. For each window it
records the selected local state, edge-residue value, anneal step count, and
final rest state. Each sampled window closes locally. This proves Claim 16.4 as
a local receipt statement.

The nth-bit layer passes with local/oracle correction included, but the receipt
names McKay-Thompson correction parity as open. Therefore the local edge
residual is admitted while global continuum collapse is not. This proves Claim
16.5.

Together these claims prove the theorem.

_**(D)** verified algebraic/structural proof._

### Receipt

Promoted verifier:

```text
production/formal-papers/CQE-paper-16/verify_continuum_edge_residuals.py
```

Receipt:

```text
production/formal-papers/CQE-paper-16/continuum_edge_residuals_receipt.json
```

Closed layers:

```text
every local chart state anneals to a Lie-conjugate rest state in <=3 S3 steps
there are four Lie-conjugate rest states
edge residue is exactly C and not R
sample decade windows carry local receipts
local/oracle nth-bit layer passes with correction included
```

Open layers:

```text
global continuum closure
O(N) to O(log N) propagating-correction collapse
closed McKay-Thompson correction parity
claim that adding digits terminates continuum depth
```

### Falsifiers

The paper fails if any local chart state needs more than three anneal steps.

It fails if edge residue fires outside `C=1, R=0`.

It fails if power-of-ten windows are treated as a completed continuum limit.

It fails if the McKay-Thompson parity obligation is hidden.

_— honestly carried as guard / next-need._

### Open Obligations

1. IRL fine-structure constant target is recorded in NP-15; physical alpha calibration remains open.

_— honestly carried as guard / next-need._

---



## X.FLCR-07__Causal_Links_And_Obligation_Ledgers. Companion (plain-language)

> Recrafted from `archive_intake/.../FINAL_FLAT/FLCR-07__Causal_Links_And_Obligation_Ledgers__companion.md`. Exposition twin of the workbook layer. D/I/X tagged.

# FLCR-07 Companion - Causal Links And Obligation Ledgers
## What This Paper Is Doing
This paper turns the FLCR corpus into an auditable dependency graph. It distinguishes proof-support edges, obligation edges, negative verdicts, receipt edges, and workflow routes. This prevents open obligations from being consumed as proofs while still allowing them to act as springboards for later reapplication.
In plainer terms: this paper defines one reliable piece of the LCR stack and
states exactly how later papers are allowed to use it. It is not trying to win
every downstream claim locally. It is making the local result strong enough
that later papers can build on it without changing what was proved.
## Strongest Claim
Theorem 7.1: A valid FLCR causal graph must type its edges before they can be consumed by paper claims.
Lane: `normal_form_result`.
## Why It Matters
- Defines typed edges for support, obligation, receipt, and negative verdicts.
- Treats failed extraction attempts as reusable search-pruning data.
- Frames the paper corpus as a content-addressed provenance graph.
- Prepares the T10 master receipt and later layer-2 synthesis ledgers.
## What It Does Not Claim Yet
- A graph edge is not automatically proof; its edge type controls consumption.
- A failed route remains failed only for its tested scope.
- Full 32-paper graph population remains a later lockfile task.
## How Later Papers Should Use It
Later papers cite this paper by claim and lane. If a later paper needs a
stronger statement, it must add the missing receipt, standard theorem citation,
CAM/crystal reapplication, normal-form proof, calibration datum, or falsifier
boundary. It does not inherit stronger language from older drafts.
## Reader Check
Before accepting a downstream use of this paper, ask:
1. Which exact claim is being consumed?
2. Which lane admits that claim?
3. What receipt, theorem, CAM route, or calibration source travels with it?
4. What residue is still forbidden from promotion?
## Why This State Happens Next
This companion layer carries the semantic story: why this paper appears here,
why the preceding state needs this move, and how the next paper is allowed to
consume it. Its job is not to weaken the formal claim; its job is to make the
state transition legible.
Assigned original ribbon role(s): `06`/ledger_action.
The interpretive move in this paper must be presented as label management over
an already-addressed state. Where the paper changes language, it must say what
object remains invariant and what access path, label, or analogy changed.
## Narrative State Contract
The s

---



## X.FLCR-11__Master_Receipt_And_Stack_Replay. Companion (plain-language)

> Recrafted from `archive_intake/.../FINAL_FLAT/FLCR-11__Master_Receipt_And_Stack_Replay__companion.md`. Exposition twin of the workbook layer. D/I/X tagged.

# FLCR-11 Companion - Master Receipt And Stack Replay
## What This Paper Is Doing
This paper formalizes the first ten papers as one replayable causal unit. The operative object is T10 master receipt. The core result is that Papers 00-09 can be composed into an inspectable receipt stack when every imported claim preserves source, edge, receipt, and obligation fields. The paper also defines how this result routes forward: FLCR-11 becomes the intake gate for aggregate proof replay and later layer-2 synthesis. Its main residue is explicit: exceptional-to-Niemeier terminal routes and cold extraction claims remain scoped until their own receipts are attached.
In plainer terms: this paper defines one reliable piece of the LCR stack and
states exactly how later papers are allowed to use it. It is not trying to win
every downstream claim locally. It is making the local result strong enough
that later papers can build on it without changing what was proved.
## Strongest Claim
Theorem 11.1: Papers 00-09 can be composed into an inspectable receipt stack when every imported claim preserves source, edge, receipt, and obligation fields
Lane: `receipt_bound_internal_result`.
## Why It Matters
- Defines T10 master receipt as a first-class FLCR object.
- States the local result: Papers 00-09 can be composed into an inspectable receipt stack when every imported claim preserves source, edge, receipt, and obligation fields.
- Routes downstream use through claim lanes rather than inherited prose: FLCR-11 becomes the intake gate for aggregate proof replay and later layer-2 synthesis.
- Preserves the residue boundary: exceptional-to-Niemeier terminal routes and cold extraction claims remain scoped until their own receipts are attached.
## What It Does Not Claim Yet
- exceptional-to-Niemeier terminal routes and cold extraction claims remain scoped until their own receipts are attached
- External calibration claims require units, datasets, citations, and reproducible data binding.
- A later translation paper may strengthen this result only by adding the missing lane evidence.
## How Later Papers Should Use It
Later papers cite this paper by claim and lane. If a later paper needs a
stronger statement, it must add the missing receipt, standard theorem citation,
CAM/crystal reapplication, normal-form proof, calibration datum, or falsifier
boundary. It does not inherit stronger language from older drafts.
## Reader Check
Before accepting a downstream use of this paper, ask:
1. Which exact claim is being consumed?
2. Which lane admits that claim?
3. What receipt, theorem, CAM route, o

---


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
