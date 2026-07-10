# Reader's Handbook — Layman Edition

> Recrafted from `CQECMPLX-ProofValidatedSuite/Handbooks/Handbook-Layman.md` as a 240-form root (whole-suite reader guide). D/I/X tagged.

# Reader's Handbook — Layman Edition
**Who this is for**: Anyone curious about what these papers are doing. No math required.
**What this does**: Walks you through the nine thematic sections of the CQE/CMPLX corpus in plain language, with analogies, and shows you where to look when you want to go deeper.
---
## How to Use This Handbook
Read each section in order. They build on each other. Each section ends with:
- **By Hand**: what the physical workbook companion lets you try yourself
- **Go Deeper**: exact file paths to the formal papers and tests
You do not need to run any code. Every proof in this system also has a physical version you can do with a notebook, colored tokens, and string.
---
## The Workbook Companion System
Every paper in this corpus has a companion workbook — a physical notebook page you can fill out by hand that produces the exact same proof as the computer. This is not a simplification. The workbook IS the proof. From Axiom 00.4:
> "If the claim is part of the main corpus, it must have a physical workbook analogue."
When you see a **By Hand** section below, it refers to the instructions in the matching WORKBOOK.md file. Those files live at:
```
D:\CQECMPLX-Production\papers\CQE-paper-{NN}\03-CQE-workbook\WORKBOOK.md
```
The general workbook setup for all papers:
- Get a physical notebook in the paper's color (each paper assigns a color)
- Mark a **C token** at the center of your page
- Mark **L** on the left, **R** on the right
- Use string to bind proof routes
---
## Chapter 0: Preparing the Space (Paper 00)
### What Is Actually Happening
Before any claim can be made in this system, four agreements must be in place. Think of it like a shipping contract: before you send a package, you agree on the rules of shipment. Paper 00 is that contract.
The four rules (called axioms) are:
1. **Locality**: You can only claim something if you can see it through a small window. No claims about "everything everywhere at once" — every claim must be demonstrable locally first.
2. **Receipt Preservation**: Every operation leaves a receipt. Nothing disappears without a trace. If you transform something, you keep a record of what went in, what came out, and what was left unresolved.
3. **Boundary Positivity**: When something fails — a route that doesn't work, a mismatched pairing — that failure is DATA, not garbage. Failed routes become "obligations" (things to resolve later) or "correction surfaces" (something you can use).
4. **Analog Equivalence**: If a claim is real, you must be able to do it by hand. Every digital proof has a physical counterpart. This is how we know the proof is not an artifact of the computer.
### The Delivery Label
Every claim travels through this system with an 8-slot label — like a shipping label with 8 fields. The slots are:
| Slot | Name | What it holds |
|------|------|---------------|
| C | Center | The claim's title and core operation |
| A | Anchor | Where the claim came from (citation) |
| B | Binary rule | The rule that governs the claim |
| L | Left | Left boundary reading |
| R | Right | Right boundary reading |
| W | Workbook | The by-hand proof |
| T | Test | The automated test |
| O | Obligation | What is still owed (unresolved) |
When Paper 00 runs its smoke test, it fills slots B, L, R, and W. The T and O slots remain open — meaning the system knows they still need to be addressed.
### Why This Chapter Comes First
This is not about the math. It is about making math accountable. Before Rule 30 starts generating proofs, before lattices get stacked, before anything — there is a contract that says: every step is visible, every failure is kept, every proof has a hand-done version.
All nine following chapters operate under these four rules. If anything breaks one of these rules, the receipt will say so.
### By Hand
Paper 00's workbook is the Foundation Sheet. It uses white paper (the neutral color — not yet colored by any specific claim).
Steps:
1. Roll three coins. The result is your (L,C
