# Paper 23 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** reasoning and possible uses only; NSIT/grading owns promotion.

## Core Reading

Paper 23 is a protein descriptor kernel. It converts sequences into local
windows, contact maps, bifurcation candidates, and bounded winding witnesses
without claiming native fold prediction by itself.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| Descriptor vs predictor | A descriptor extracts structured features; a predictor must match native structure or dynamics. |
| Contact-map validation | Contact maps can be compared against PDB/native structures when residue indexing and contact predicate are fixed. |
| Encoding burden | Hydrophobic/polar bits are a coarse encoding; richer amino-acid features may be needed. |
| Topological feature caution | Bifurcation and winding marks are candidate topology features until compared to structure. |
| Thermodynamic layer | Free energy, fold rate, and stability need physical models/data. |
| Benchmark comparators | AlphaFold, PDB, MD, and experimental structures are different external comparators. |

## Possible Uses

1. Define a protein validation ladder: descriptor, PDB contact comparison,
   structure prediction, dynamics, thermodynamics.
2. Add parser/adapters for FASTA, PDB/mmCIF, and predicted structures.
3. Store candidate bifurcations as queryable features for later comparison.
4. Treat winding gaps as algorithmic targets, not biological proof gaps only.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `23.BA.1` | FoldForge emits descriptors. | NP-07 and biology adapters. | Later validators may compare descriptors to structures. | Descriptor provenance and encoding remain visible. | PDB/contact-map receipt. |
| `23.BA.2` | Winding witness is bounded. | Papers 05, 17, 21. | Later algorithmic work may extend depth/order. | Bounded witness must not imply all-depth proof. | Winding extractor receipt. |
| `23.BA.3` | Biological claims require external evidence. | NP-07 and external datasets. | Later data may promote specific examples. | Claim must cite sequence, structure, metric, and comparator. | Benchmark report. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| What sequence/structure formats need adapters? | Makes validation executable. |
| Which contact predicate is used, and how is it compared? | Makes contact maps falsifiable. |
| What metrics distinguish descriptor quality from prediction accuracy? | Prevents descriptor/predictor conflation. |

