# Paper 32 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** reasoning and possible uses only; NSIT/grading owns promotion.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| Schedule vs proof content | A supervisor cursor schedules inspection; it does not replace target receipts. |
| Coverage vs minimality | Covering all permutations and proving shortest possible length are different combinatorial burdens. |
| Upper/lower bound corridor | The n=8 corridor is a search/exclusion problem, not just a row in a table. |
| Product selector | Deployment selectors must preserve paper status and receipt references. |
| Active-suite wrap | Paper 32 -> Paper 01 is a retest schedule, not a circular proof. |

## Possible Uses

1. Build a selector schema: target, schedule row, receipt status, proof owner,
   and allowed action.
2. Store superpermutation rows as coverage records with separate minimality
   fields.
3. Route n>=6 minimality to a candidate-search/exclusion ledger.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `32.BA.1` | Supervisor cursor schedules requests. | Product selectors and NP-05. | Later deployment may add selector routes. | Selector must preserve proof/open/readout status. | Selector conformance report. |
| `32.BA.2` | Coverage and minimality are separate. | NP-11. | Later search may improve bounds or prove minimality. | Current coverage rows remain coverage rows. | Search/exclusion receipt. |
| `32.BA.3` | Active wrap retests Paper 01. | Larger-window passes. | Retest schedules may be added. | Wrap is not proof cycle. | Retest/scheduler receipt. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| What fields separate coverage from minimality? | Prevents superpermutation overclaim. |
| How do selectors preserve claim status? | Makes product packaging safe. |
| What search ledger is needed for n=8 corridor? | Turns open corridor into work queue. |

