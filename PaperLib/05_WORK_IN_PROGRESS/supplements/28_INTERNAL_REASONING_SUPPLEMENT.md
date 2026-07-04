# Paper 28 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** reasoning and possible uses only; NSIT/grading owns promotion.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| Local-rule game lattice | A game surface can be represented as local transition receipts without full strategy. |
| Admissible dimension set | Code-tower dimensions act as a dimension admission filter. |
| Move orbit vs game solver | An S3 move orbit is a move surface, not a solution of the game. |
| Forbidden carrier logging | Rejected moves are constraints and should remain in the ledger. |
| OEIS lookup readiness | Formula readiness and external sequence identity are different tasks. |

## Possible Uses

1. Generalize KnightForge into a local-rule game receipt schema.
2. Build dimension-admission adapters.
3. Store forbidden carriers as training constraints for game solvers.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `28.BA.1` | Game-lattice kernel is local-rule receipt. | Papers 24, 32 and NP-07. | Later game solvers may consume it. | Move receipt remains distinct from strategy proof. | Solver benchmark. |
| `28.BA.2` | Dimension set is code-tower-admitted. | Papers 08, 17. | Later dimensions may be added. | Admission reason must be attached. | Dimension verifier. |
| `28.BA.3` | OEIS identity is query-ready. | NP-08. | External source may bind identity. | Formula and indexing remain attached. | OEIS/source receipt. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| What schema defines a local-rule game receipt? | Reuses game lattice work. |
| Which game claims need strategy/termination/fairness proofs? | Separates solver burdens. |

