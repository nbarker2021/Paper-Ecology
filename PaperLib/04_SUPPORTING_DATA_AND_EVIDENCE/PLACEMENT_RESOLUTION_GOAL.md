# CMPLX Unified Paper Suite: Placement Resolution Goal
## Instructions for Blocks 9+ (Papers 9–100+)

**Version:** 1.0 — For all future consolidation blocks  
**Prior:** Papers 0–8 are FIXED and IMMUTABLE. No edits to them except error fixes.  
**Scope:** This instruction governs all paper consolidation from Block 3 (Papers 9–11) onward.

---

## The Core Problem

The D drive contains fragments from **multiple independent numbering systems** that must be merged into one coherent 100+ paper suite. The old systems include:

- **UFT 0–100** (unified field theory, ~100 papers)
- **CQE 00–31** (production, 32 papers + sub-papers .25/.50/.75)
- **Formal-Suite** (papers 000, 001, 011, 012, 013, 020–024, etc.)
- **ForgeFactory v0.3** (papers 00–30 + formal papers)
- **R30 Proof papers** (papers 07–15, 16, 17, etc. with different numbering)

**The old names do NOT determine the new slots.** A file named `CQE-paper-09.md` does NOT necessarily belong in unified Paper 9. The content does.

---

## The Ordering Principle

### 1. Dependency-First Assignment

Papers are placed in **numerical order based on what they depend on**, not on what they were called in the old system.

> **Rule:** A paper MUST be placed AFTER every paper whose theorems, definitions, or objects it references. It MAY be placed BEFORE papers that depend on it.

### 2. The Earliest-Best Continuation Rule

When multiple candidate variants could fill a slot, choose the one that **most naturally continues from the immediately prior paper**.

> **Rule:** If two variants both contain theorem X, and theorem X depends on Paper 4 but not on Paper 5, the variant with theorem X goes in the earlier slot (closer to Paper 4). If theorem X depends on Paper 5 and builds on it, it goes later (closer to Paper 6).

### 3. The Split-or-Merge Decision

If a single old paper contains content that logically belongs in TWO different unified slots, **split it**. If two old papers contain overlapping content that belongs in the same slot, **merge them**.

> **Rule:** Never force-fit content into a slot just because the old filename has a matching number. The unified paper is a dependency graph, not a rename operation.

---

## The Placement Algorithm (Use This Every Block)

### Step 1: Scan All Variants for the Block

Use `variant_discovery.py --block N` to find all variants for papers N*3 through N*3+2. But also:
- Check if any old paper from OTHER numbering systems could belong here
- Look at the cross-references in the prior papers (Papers 0–8) to see what forward references exist
- Check the old UFT `paper_intent_index.json` for paper titles/theses

### Step 2: Map Content to the Dependency Chain

For each candidate variant, identify:
- **What it depends on** (which prior papers' theorems/objects it uses)
- **What it enables** (which later papers' theorems depend on it)
- **Whether it is a continuation** (builds directly on prior paper) or a **lateral** (introduces new machinery)

### Step 3: Assign to the Earliest Valid Slot

Place the paper in the **lowest numbered slot** that satisfies:
1. All of its dependencies are in earlier papers (verified)
2. It does not introduce concepts that earlier papers already assumed
3. It is not better placed later (where its content would enable more papers)

### Step 4: Handle Divergence Explicitly

If an old paper's content must be split across multiple unified slots, or if an old paper's content belongs in a slot with a different number:

- **Document the mapping** in a `PLACEMENT_DIVERGENCE_LOG.md`
- **Preserve old references** by adding notes like "This was previously CQE-paper-09 (Hamiltonian) and R30-paper-09 (π vacuum parameter); the Hamiltonian content is now unified Paper 9, the vacuum parameter is now Paper 10"
- **Never silently remap** — always note when the unified numbering diverges from the old

---

## Expected Divergence Patterns (Known in Advance)

Based on the prior papers' forward references, these divergences are expected:

| Old System | Old Paper | Content | Likely Unified Slot | Reason |
|------------|-----------|---------|---------------------|--------|
| UFT | Paper 9 | Hamiltonian temporal emergence | Paper 9 | Direct continuation from Paper 8 lattice |
| CQE | Paper 09 | Kappa conservation / electroweak | Paper 10 or 11 | Depends on Hamiltonian (Paper 9) and lattice (Paper 8) |
| R30 | Paper 09 | π vacuum parameter | Paper 10 or separate | Different topic, may merge with electroweak |
| CQE | Paper 10 | T10 master receipt | Paper 12–14 | Master receipt should bind Papers 0–9, not appear too early |
| UFT | Paper 10 | P3 cold-start readout | Paper 12 or 13 | P3 extraction is a late result, needs all prior machinery |
| Formal | Paper 011 | LCR energy transport | Paper 9 or 11 | Depends on lattice closure (Paper 8) |
| Formal | Paper 012 | S3 action | Paper 11 or 12 | Depends on Paper 3 + Paper 8 |
| Formal | Paper 013 | Anneal delay bound | Paper 13 or 14 | Depends on Papers 3, 7, 8 |
| Formal | Paper 020 | Recursive closure | Paper 20+ | Explicitly named as late paper |
| Formal | Paper 021 | Spectre substitution | Paper 21+ | Explicitly named as late paper |

**These are estimates.** The actual placement must be determined by dependency analysis during consolidation.

---

## Block Workflow (Same as Before, Plus Placement Gate)

For each block N (Papers N*3 to N*3+2):

1. **Discovery:** Run `variant_discovery.py --block N` to find candidates
2. **Placement Analysis:** For each candidate, determine which unified slot it belongs in. If the content doesn't fit the block, reassign it to the correct block and note the divergence.
3. **Read Variants:** Read all variants assigned to this block (may include variants from old papers with different numbers)
4. **Consolidate:** Write unified papers using the best content from all assigned variants
5. **Cross-Check:** Verify all cross-references to Papers 0–(N*3-1) use the unified numbering
6. **Document Divergence:** Update `PLACEMENT_DIVERGENCE_LOG.md` with any remappings

---

## What to Watch For (Anti-Patterns)

1. **Name-Binding Trap:** "The file is called `paper_09.md` so it must be Paper 9." — WRONG. The content determines the slot.
2. **Late-Introduction Trap:** "Paper 10 should come right after Paper 9 because 10 = 9 + 1." — WRONG. The master receipt (T10) may need to bind Papers 0–15, so it might belong in Paper 14 or 15.
3. **Underspecified Dependency Trap:** "This paper uses D4 so it can go anywhere after Paper 3." — WRONG. If it also uses lattice closure (Paper 8), it must go after Paper 8.
4. **Merge-Everything Trap:** "These two papers are both about the Standard Model so they should be one paper." — WRONG. If one is about electroweak (early SM) and one is about QCD (late SM), they may belong in different slots.
5. **Split-Nothing Trap:** "This old paper is 100KB so it must be one unified paper." — WRONG. If the first 30KB depends on Paper 8 and the last 70KB depends on Paper 12, split it.

---

## The Honesty Discipline

Every placement decision must be **explicitly justified** in the consolidation analysis. The justification format is:

```
PLACEMENT DECISION: [Old paper name] → [Unified slot]
DEPENDS ON: [List of prior papers whose theorems are used]
ENABLES: [List of later papers whose content depends on this]
REASON: [One sentence explaining why this slot is correct]
DIVERGENCE: [Yes/No — does this diverge from old numbering?]
```

If a paper is placed in a slot DIFFERENT from its old number, the divergence must be documented in `PLACEMENT_DIVERGENCE_LOG.md`.

---

## Metadata Files (Maintain These)

- `D:\PaperLib\PLACEMENT_DIVERGENCE_LOG.md` — Records every case where unified numbering diverges from old numbering
- `D:\PaperLib\UNIFIED_PAPER_INDEX.md` — Master index of all unified papers with titles, theorems, and placement rationale
- `D:\PaperLib\DEPENDENCY_GRAPH.md` — Explicit dependency graph (paper → depends on → papers)
- `D:\PaperLib\scripts\output\variant_report_block_N.json` — Raw variant discovery per block

---

## Final Instruction

**The unified paper suite is a dependency graph. The old numbering systems are source material. The content determines the placement. The prior papers (0–8) are fixed. Every new paper must be placed where it best continues the chain, not where the old name said it should go.**

When in doubt, apply the **Earliest-Best Continuation Rule**: the content that most naturally extends the immediately prior paper goes in the earliest valid slot. Content that requires more machinery to be built first goes later. Content that is independent lateral machinery goes in its own slot, placed after its own dependencies.

---

*Generated for Block 3+ consolidation. Prior papers: 0–8 (fixed).*
