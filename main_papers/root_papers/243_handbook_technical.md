# Reader's Handbook — Technical Edition

> Recrafted from `CQECMPLX-ProofValidatedSuite/Handbooks/Handbook-Technical.md` as a 240-form root (whole-suite reader guide). D/I/X tagged.

# Reader's Handbook — Technical Edition
**Who this is for**: Software engineers, mathematicians, and technically-minded readers. Assumes comfort with binary arithmetic, data structures, basic algebra, and code.
**What this does**: Maps each paper's core mechanism to its data structures, algorithms, and verifier interfaces.
---
## How to Use This Handbook
Each chapter gives you:
- The core computation being performed
- Key data structures and their types
- The tool binding (Python module/function that implements the claim)
- The verifier (function that checks the claim)
- The workbook companion (physical protocol that isomorphically matches the tool)
- File paths to FORMAL.md, run.py, and WORKBOOK.md
The corpus is organized as a stack. Each paper's C-form carries a Gluon — a typed proof-mass object — forward through the stack. The Gluon state in each paper is a specific mathematical object (a bit, a class instance, a centroid, an accumulated XOR value).
---
## The Workbook Companion System
Every paper has a WORKBOOK.md whose Sheet ⇄ Tool Isomorphism table maps each analog operation to a Python function and data structure. Lemma 00.2 establishes that the workbook receipt and the tool receipt are equivalent when both encode the same (center, boundary, obligation) state.
Physical protocol materials needed: colored tokens (C = one color, L/R = another), string (red for swap bindings, blue for trajectories), colored notebook per paper.
Path pattern: `D:\CQECMPLX-Production\papers\CQE-paper-{NN}\03-CQE-workbook\WORKBOOK.md`
---
## Chapter 0: The Transport Contract (Paper 00)
### Core Mechanism
Paper 00 defines the invariants that ALL claims in this corpus must satisfy. It is not a theorem paper — it is the schema paper. The four axioms define the constraint space; the three lemmas define the portability conditions.
### Axioms and Lemmas
| ID | Kind | Statement |
|----|------|-----------|
| 00.1 | Axiom | Locality: every accepted claim must be readable through a local window before it is lifted to a larger frame. |
| 00.2 | Axiom | Receipt Preservation: no transform is accepted unless its inputs, output, and unresolved residue can be logged. |
| 00.3 | Axiom | Boundary Positivity: failed, partial, or mismatched routes are data. They become obligations or correction surfaces. |
| 00.4 | Axiom | Analog Equivalence: if the claim is part of the main corpus, it must have a physical workbook analogue. |
| 00.1 | Lemma | If a local state preserves C and records L/R residue, it can be transported into a proof ledger without erasing unresolved alternatives. |
| 00.2 | Lemma | If a tool output and workbook sheet encode the same center, boundary, and obligation state, they are equivalent receipts at different media layers. |
| 00.3 | Lemma | A practical example is valid for this paper only when it demonstrates the same operation in a non-toy domain. |
All axioms and lemmas have scope="global" — they govern every paper in the corpus, not just P00.
### The Ribbon Data Structure
Every paper carries an 8-slot ribbon. Slots:
```python
class SlotName(Enum):
    C = "C"   # center/title — default-filled
    A = "A"   # anchor/citation — default-filled
    B = "B"   # binary rule
    L = "L"   # left boundary
    R = "R"   # right boundary
    W = "W"   # workbook
    T = "T"   # test
    O = "O"   # obligation
```
P00 smoke test fills B, L, R, W. After filling: `obligation_delta = {"closed": ["B","L","R","W"], "opened": []}`. Remaining obligated slots: T, O.
### Foundation Verifiers (T3-T7)
| Theorem | Verifier | What it checks |
|---------|----------|---------------|
| T3 | `verify_T3_chart_j3o_isomorphism()` | Bijection between 8 chart states (L,C,R) and J₃(O) trace-k idempotents |
| T4 | `verify_T4_n3_closure_exact()` | M₃ = ⅓(T₁₂+T₁₃+T₂₃); residual ℚ = 0 |
| T5 | `verify_T5_M3_idempotent()` | M₃² = M₃ |
| T6 | `verify_T6_trace_blocks()` | Row/column trace block identity |
| T7 | `verify_T7_8x8_transition_exact()` | 8×8 transition matrix entries ∈ {
