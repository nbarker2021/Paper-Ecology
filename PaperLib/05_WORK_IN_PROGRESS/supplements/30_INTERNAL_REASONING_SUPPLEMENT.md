# Paper 30 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** reasoning and possible uses only; NSIT/grading owns promotion.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| Corpus schema | The eight-slot ribbon is a schema for reading each paper as structured data. |
| Provenance as slot invariant | A slot without provenance should not be treated as filled. |
| Sweep as audit pass | The 00-29 sweep is an audit traversal, not content promotion. |
| Terminal lookup bead | No-cost lookup can be a reusable bead if receipt-bound. |
| New-paper routing | Undercovered topics discovered by sweep should become paper needs, not hidden notes. |

## Possible Uses

1. Turn the eight-slot ribbon into a machine-readable paper index.
2. Use sweep results to generate NSIT claim queues.
3. Attach lookup beads and obligation beads as separate slot types.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `30.BA.1` | Eight-slot schema frames Papers 00-29. | Papers 31, 32 and NSIT. | Later passes may add slot subtypes. | Slot provenance remains mandatory. | Schema report. |
| `30.BA.2` | Sweep routes new paper needs. | NP-01..NP-13. | New needs may split/merge. | Routed need source remains traceable. | New-paper ledger update. |
| `30.BA.3` | Lookup beads can be reused. | Papers 08, 17, 29. | More lookup beads may be added. | Lookup receipt remains attached. | Lookup bead receipt. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| What is the machine schema for an eight-slot paper row? | Enables automated corpus reading. |
| Which sweep findings become new papers versus supplements? | Controls topic spread. |

