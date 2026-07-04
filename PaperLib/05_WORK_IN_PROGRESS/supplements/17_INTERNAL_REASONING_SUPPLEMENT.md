# Paper 17 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** reasoning and possible uses only; NSIT/grading owns promotion.

## Core Reading

Paper 17 is a code/lattice tower paper. It extends Paper 08's ladder into an
error-correction narrative while keeping lookup, invariant, terminal-selection,
and physical-error-correction burdens separable.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| Error-correcting-code ladder | Hamming, extended Hamming, Golay, and Leech-facing rungs can be explained with classical code parameters. |
| Tower as typed pipeline | Each rung should expose input object, output object, invariant checked, and receipt. |
| Lookup vs terminal semantics | Leech lookup can provide addressability without solving arbitrary semantic landing. |
| Weyl extraction burden | A Weyl-table/extractor claim should name compression target, complexity, and invariant preservation. |
| Physical error correction caution | Mathematical error correction and physical error correction are related only after a channel/noise model is attached. |

## Possible Uses

1. Create a tower-rung table with parameters, checks, and dependent papers.
2. Use Leech lookup as a CAM address service for applied papers.
3. Route physical error-correction claims through channel/noise-model fields.
4. Keep Weyl extraction as an algorithmic problem with complexity metadata.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `17.BA.1` | Code tower reaches Leech-facing lookup. | Papers 21, 29, 30 and NP-02/NP-03. | Later work may add terminal selectors or invariants. | Lookup remains distinct from full invariant classification. | Terminal/invariant receipt. |
| `17.BA.2` | E6/E7/E8 language is tower-scoped. | Papers 05, 08, 21. | Later receipts may refine exceptional lift role. | No physical error-correction claim without channel model. | Lift or channel receipt. |
| `17.BA.3` | Weyl extraction is a future algorithmic object. | NP-02 and NP-04. | Complexity and extractor design may change. | It must preserve named invariants. | Extractor verifier. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| What is each tower rung's exact input/output contract? | Makes the ladder executable. |
| What distinguishes lookup, construction, invariant, and extractor claims? | Avoids burden merging. |
| What physical channel model would be needed for physical error correction? | Separates math code from lab physics. |

