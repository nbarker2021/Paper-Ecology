# Paper 06 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** this supplement adds reasoning and possible uses only. NSIT and
the grading tools own validity labels, promotion decisions, and scores.

---

## Core Reading

Paper 06 is the paper where the corpus stops being a line of arguments and
becomes an auditable dependency system. Its strongest extra value is that it
can be read with the standard machinery of graphs, build systems, provenance,
and proof-carrying artifacts.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| Directed acyclic proof graph | The proof-support subgraph can be treated like a build dependency graph: cycles are not automatically bad, but cycles in already-promoted proof support need explicit handling. |
| Obligation edge as non-proof edge | An obligation edge is closer to an issue tracker or proof obligation than to a theorem dependency. That distinction lets later papers carry live work without contaminating proof support. |
| Provenance graph / Merkle DAG | Receipts, artifact hashes, and graph edges naturally form a content-addressed provenance graph. This gives Paper 06 a path toward reproducible corpus state, not only prose dependency notes. |
| Package-manager analogy | Papers and tools behave like packages with dependencies, versions, constraints, and lockfiles. A full 32-paper graph can use dependency-resolution ideas to detect incompatible claims. |
| Negative result as stored knowledge | The correction-extraction verdict should be treated as a reusable result: failed shortcuts reduce search space and prevent repeated work. |
| Lucas decomposition as base/residue split | The Rule90/Lucas side gives a standard "solvable base plus carried residual" pattern, useful for later papers that need to separate lookup, reconstruction, and missing extraction. |
| Triadic keystone as complexity signal | The `3^k` in `2^k` law supplies a sparsity/dimension signal that may guide later search, compression, and sampling heuristics. |

## Possible Uses

1. Build a corpus lockfile: paper id, theorem id, receipt id, hash, dependency
   edges, and unresolved obligation edges.
2. Treat failed extraction mechanisms as first-class search-pruning data.
3. Attach graph queries to CAM: "what receipts support this claim?", "what
   obligations can flow backward to Paper 02?", "which route would change if a
   later verifier lands?"
4. Use dependency-resolution language to reconcile historical variants without
   needing to erase them.
5. Turn edge-type reconciliation into a schema migration problem with adapters.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `06.BA.1` | Causal links are typed edge records. | Papers 10, 20, 30, 32 and NP-05. | The graph may become a full corpus lockfile or CAM query graph. | Edges must remain typed and receipt-bearing. | Full graph population or lockfile receipt. |
| `06.BA.2` | Failed extraction mechanisms are recorded verdicts. | Papers 09, 12, 16, 18 and NP-01. | Later math may explain why a failed shortcut failed, or replace it with a different extraction route. | The tested mechanisms remain failed for their tested form unless a new test changes scope. | New extraction theorem, counterexample audit, or verifier receipt. |
| `06.BA.3` | Rule90/Lucas plus correction is the decomposition lane. | Papers 08, 09, 12, 18, 29. | Later papers may bind lattice/VOA/Moonshine structure to the correction field. | The local decomposition remains the base/residue split. | Cross-paper receipt that maps correction sums into the later structure. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| Which edge types are semantic proof support, and which are workflow routing? | Prevents issue-tracking edges from being consumed as proof edges. |
| What minimal receipt fields are required for a graph edge? | Enables a paper-corpus lockfile. |
| Can historical edge schemas be normalized by adapters instead of rewritten? | Preserves provenance while allowing unified querying. |
| Which negative extraction results should be searchable as reusable constraints? | Prevents repeated failed routes and improves future search. |

