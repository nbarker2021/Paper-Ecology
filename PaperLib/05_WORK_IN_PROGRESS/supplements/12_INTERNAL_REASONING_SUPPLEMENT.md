# Paper 12 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** this supplement adds reasoning and possible uses only. NSIT and
the grading tools own validity labels, promotion decisions, and scores.

---

## Core Reading

Paper 12 is about prediction surfaces, not one universal predictor. The useful
reasoning comes from layered solver architecture, oracle/cold-start separation,
finite evidence hygiene, and CA theory.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| Layered prediction stack | Local truth tables, cached sheets, finite experiments, spectral guesses, and cold extraction are different layers and should not be merged. |
| Oracle vs cold-start distinction | A predictor that uses hydrated state, cached data, or generated prior sheets has a different burden than a cold extractor. |
| Local rule as complete finite object | For ECA rules, the radius-1 truth table is a complete local specification; local correctness can be separated from global unpredictability. |
| Entropy as diagnostic, not proof | Entropy receipts can describe distributional behavior while leaving exact next-bit prediction separate. |
| Failed receipt as architectural datum | A failed P3 closure attempt still tells the system which route not to reuse as-is. |
| Silent-boundary ECA classification | Counting silent-boundary rules can become a reusable filter for future CA-family comparisons. |
| Cost-class metadata | Every prediction layer should say whether it is table lookup, local update, bounded simulation, heuristic extrapolation, or cold formula. |

## Possible Uses

1. Turn prediction surfaces into typed solver APIs: input, output, layer, cost,
   cache dependency, defect, and receipt.
2. Store failed P3 attempts as searchable negative evidence.
3. Add a "uses oracle/hydrated state?" field to every Rule 30 claim.
4. Use silent-boundary ECA classification to search adjacent rules with similar
   boundary behavior.
5. Route McKay/correction-collapse attempts through a separate banded theorem
   surface instead of mixing them with finite local readout.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `12.BA.1` | Prediction surface has multiple layers. | Papers 16, 18, 29 and NP-01. | Later papers may add McKay/VOA/spectral layers. | Each layer must keep cost, input dependency, and receipt identity. | New solver receipt or theorem. |
| `12.BA.2` | P3 cold extraction remains separated from finite evidence. | Papers 06, 09, 18 and NP-01. | Later work may close or partially close a different cold route. | Failed P3 receipt remains evidence about that attempted route. | Cold extractor verifier or formal impossibility/result. |
| `12.BA.3` | Entropy/real-data receipts support review. | Applied/product papers and NP-07. | They may become benchmark baselines. | They do not become exact prediction without a predictor. | Benchmark protocol with held-out tests. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| Which claims rely on hydrated state, cache, generated sheets, or prior enumeration? | Keeps oracle-assisted layers separate from cold-start claims. |
| What is the exact schema for a prediction layer? | Makes mixed solver surfaces auditable. |
| Which failed prediction receipts should constrain future search? | Prevents repeated dead routes. |
| How should finite evidence be represented without implying asymptotic proof? | Preserves useful data without overpromotion. |

