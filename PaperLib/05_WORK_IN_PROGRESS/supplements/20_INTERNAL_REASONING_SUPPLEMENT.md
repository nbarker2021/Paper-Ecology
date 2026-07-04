# Paper 20 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** reasoning and possible uses only; NSIT/grading owns promotion.

## Core Reading

Paper 20 is an aggregation-preservation paper. Its reasoning center is that
summaries must preserve source status, provenance, unknowns, obstructions, and
validator gates.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| Data warehouse / ledger view | Paper 20 acts like a normalized warehouse over receipts and obligations. |
| Status-preserving aggregation | Aggregation should be a functor-like operation that preserves distinctions rather than collapsing them. |
| Unknown as state | Unknown reachability is data, not absence of data. |
| Forbidden rows as constraints | Forbidden rows should remain queryable as obstructions. |
| Validator-gated contribution registry | New durable rows need named validators, like database constraints or CI gates. |

## Possible Uses

1. Build a corpus-wide ledger schema with row type, source, evidence, boundary,
   validator, and downstream uses.
2. Make unknown/forbidden/open-lift rows first-class CAM nodes.
3. Use Paper 20 as the source for cross-paper dashboards without changing row
   meaning.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `20.BA.1` | Synthesis ledger preserves row distinctions. | Papers 30, 32 and NSIT. | It may become the full paper-corpus accounting layer. | Aggregation must not promote rows. | Ledger schema/report. |
| `20.BA.2` | Unknown reachability is retained. | Papers 08, 17, 21, 29. | Later receipts may resolve unknowns. | The original unknown row remains auditable. | Reachability receipt. |
| `20.BA.3` | Contribution registry is validator-gated. | Applied papers 21-28. | Domain validators may add row types. | Validator identity and rationale remain attached. | Domain validator report. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| What is the normalized ledger row schema? | Enables all-paper aggregation. |
| How should unknown and forbidden rows be queried? | Preserves negative/partial knowledge. |
| Which validators can admit new row families? | Controls growth without freezing it. |

