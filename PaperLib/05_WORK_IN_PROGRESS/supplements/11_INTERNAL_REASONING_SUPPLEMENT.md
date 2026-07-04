# Paper 11 Internal Reasoning Supplement

**Attachment type:** internally supplied reasoning.  
**Method note:** this supplement adds reasoning and possible uses only. NSIT and
the grading tools own validity labels, promotion decisions, and scores.

---

## Core Reading

Paper 11 is an admission filter. It decides how a candidate external theory or
object is represented, tested against a trust anchor, and preserved when it
does not pass the current gate. The useful outside reasoning is from type
checking, firewall policy, model admission, anomaly preservation, and benchmark
protocols.

## Reasoning Additions

| Addition | Use for this paper |
|----------|--------------------|
| Type checker analogy | A candidate theory has a declared type: id, mass, anchor, spectrum, boundary, receipt. Admission is type checking against the current stack. |
| Firewall / policy engine | The gate can be read as a policy engine: admit, route to boundary, reject, or store as datum. |
| Rejected datum as training signal | A rejected candidate still teaches the corpus about the boundary. This is useful for future search and invariance testing. |
| Trust-anchor versioning | Admission decisions depend on the exact T10 receipt version. Later T10 deltas should not silently alter prior admission rows. |
| Encoder-dependence audit | The Pariah/Happy-Family example is really a test of whether a boundary survives encoder choice. This is a standard invariance problem. |
| Benchmark protocol | External-theory admission can borrow ML/benchmark practice: candidate set, scoring function, thresholds, ablations, and held-out counterexamples. |
| Monotonicity of promotion | A boundary datum should not strengthen later claims unless a new receipt states the new promoted object. |

## Possible Uses

1. Write the admission gate as a policy table with required fields and outputs.
2. Store every rejected/boundary candidate as searchable data for later
   invariance and counterexample work.
3. Create an encoder-class registry for the Pariah/Happy-Family boundary.
4. Attach T10 version identifiers to every admission row.
5. Let NSIT compare candidate admission across multiple T10 versions or encoder
   choices.

## Deferred Back-Application Slots

| Slot | Current local reading | Later source allowed to refine it | What may change | What must remain invariant | Trigger |
|------|-----------------------|-----------------------------------|-----------------|----------------------------|---------|
| `11.BA.1` | Admission depends on T10 trust anchor and declared spectrum. | Papers 20, 30, 32 and NP-05. | Later stack versions may expand or version the trusted spectrum. | Every admission row must keep the anchor it used. | T10 migration or stack-version receipt. |
| `11.BA.2` | Pariah/Happy-Family boundary is encoder-bound. | Papers 29, 32 and NP-09. | Later work may prove invariance or identify counterexample encoder classes. | The declared encoder for the current receipt must remain visible. | Encoder-class theorem or counterexample suite. |
| `11.BA.3` | Rejected candidates are retained as data. | Applied/external papers 21-29. | Later papers may reuse rejection rows as training, falsifier, or boundary evidence. | Reuse must cite the original admission context. | Candidate registry or NSIT admission report. |

## NSIT Questions To Hand Off

| Question | Why it matters |
|----------|----------------|
| What candidate fields are mandatory for admission? | Prevents external theories from entering by resemblance alone. |
| How are T10 anchor versions represented? | Makes admissions replayable after stack updates. |
| What encoder classes must be tested for sporadic-boundary invariance? | Converts a one-encoder receipt into a real invariance program. |
| How should rejected-as-datum rows be queried later? | Turns failed admission into useful corpus memory. |

