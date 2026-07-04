# Paper 24 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** reasoning and possible uses only; NSIT/grading owns promotion.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| Local-rule game kernel | Board states can be represented as local CA rows without solving the whole game. |
| Constraint satisfaction | Non-attacking placement is a finite constraint-satisfaction problem. |
| Greedy algorithm caution | A greedy sweep yields a reproducible construction, not optimality or game strategy. |
| N-dimensional frame operator | Dimension labels can organize surfaces before playability or strategy exists. |
| OEIS/external identity lane | Sequence identity needs external lookup and exact indexing. |

## Possible Uses

1. Store board rows as local CA receipt objects.
2. Separate placement, optimality, strategy, and playability as different solver
   surfaces.
3. Use forbidden/rejected moves as useful constraint rows.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `24.BA.1` | KnightForge emits finite board-automata receipts. | Papers 28, 32 and NP-07. | Later work may add game solvers or strategy. | Greedy finite receipt remains distinct from complete game theory. | Solver/benchmark receipt. |
| `24.BA.2` | N-dimensional lift is a frame operator. | Paper 28. | Later dimensional rules may be added. | Dimension labels need admissibility evidence. | Dimension-admission receipt. |
| `24.BA.3` | OEIS identity is external lookup. | NP-07/NP-08. | Later source binding may identify sequences. | Indexing and formula must be attached. | OEIS/source-map receipt. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| Which claims are placement, optimality, strategy, or playability? | Separates game burdens. |
| What dimensions are admitted and why? | Prevents arbitrary dimensional promotion. |

