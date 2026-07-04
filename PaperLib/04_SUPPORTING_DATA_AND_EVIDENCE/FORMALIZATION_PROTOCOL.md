# Paper Reworks Formalization Protocol

This protocol turns each rework file from a clip ledger into a publication-grade
scientific paper draft while preserving provenance.

## Required Main-Body Structure

Each numbered paper must begin with a clean formal body:

1. Title and status block.
2. Abstract.
3. Keywords.
4. Contribution and scope.
5. Background and related work within the suite.
6. Definitions and notation.
7. Theorem or claim statements.
8. Methods / construction.
9. Results and verifier evidence.
10. Proof or proof sketch.
11. Limitations and open obligations.
12. Reproducibility package.
13. Cross-paper dependencies.
14. Conclusion.

## Evidence Rules

- A theorem may be labeled closed only when the exact verifier or receipt is
  named beside it.
- A physical, empirical, or external-domain claim must be labeled ECO unless a
  calibration receipt is present.
- A source clip is not main-body evidence until synthesized into a claim,
  definition, method step, result, limitation, or citation.
- CAM/crystal/GLM material should appear as receipt-bearing evidence, not as
  pasted narrative.
- Forges are action surfaces. If a result is already a no-cost lookup, the paper
  must cite the lookup contract and receipt instead of re-deriving it in prose.

## Appendix Rule

The source-ingestion dumps remain valuable, but they must be clearly separated
from the paper body. Use appendices:

- Appendix A: Source Integration Archive.
- Appendix B: Receipt and Verifier Catalog.
- Appendix C: Obligation Ledger.
- Appendix D: Cross-Paper Carry-Forward Notes.

The reader should be able to read the formal body without wading through raw
clip imports.

## Section Quality Checklist

Before a paper is marked publication-format-ready:

- The abstract states the closed result and the largest non-result.
- Every symbol used in a theorem is defined before the theorem.
- Each main claim has a status label: IPMC, ECO, IBN, engineering, or open.
- Each verifier row names what claim it supports.
- Open obligations are written as scientific limitations, not editorial TODOs.
- Source clips are below an appendix boundary.
- The conclusion does not exceed the evidence labels.

## Current Application Order

1. Paper 08: lattice closure and no-cost Leech lookup.
2. Paper 17: E6/E8 error-correction tower.
3. Paper 10: master receipt and lookup binding.
4. Paper 30: corpus ribbon framing.
5. Papers 00-07, then 09-16, then 18-32 in sequence.

## Recommended Formal Verification Backbone (TLA⁺/TLAPS)

The CQE claim hierarchy can be specified in TLA⁺ (Temporal Logic of Actions) and checked with TLAPS (TLA⁺ Proof System). Zhou et al. 2026 (arXiv:2602.16554) demonstrated LLM-guided proof automation in TLAPS, achieving 40% proof-step auto-completion on TLA⁺ library lemmas. For CQE, this means:

- **State machines:** Each paper's claim ledger can be modeled as a TLA⁺ state machine with transitions: `staged_open → investigation → hypothesis → proven → IPMC`.
- **Invariants:** The D/I/X taxonomy (Data/Interpretation/Fabrication) can be enforced as type invariants.
- **Proof obligations:** Open obligations (e.g., FLCR-35-OBL-002: EFE identity) can be written as TLA⁺ temporal properties: `□(open_obligation → ◇(proved ∨ falsified ∨ demoted_to_ECO))`.
- **Benchmark:** A `CQE-miniF2F` benchmark (analogous to miniF2F for Lean) would contain 100 CQE-specific proof obligations drawn from the 1,105 obligation rows.

**Status:** Recommended, not yet implemented. Owner: NP-08 (Bibliography, Taxonomy, And Claim-Layer Governance) or dedicated formal-methods supplement.

1. Paper 08: lattice closure and no-cost Leech lookup.
2. Paper 17: E6/E8 error-correction tower.
3. Paper 10: master receipt and lookup binding.
4. Paper 30: corpus ribbon framing.
5. Papers 00-07, then 09-16, then 18-32 in sequence.
