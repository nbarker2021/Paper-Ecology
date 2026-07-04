# External Paper Explorer Scale Protocol

Date: 2026-06-30

## Working hypothesis

The working hypothesis is that a large-scale attachment pass over current scientific publications will close many open CQE/CMPLX gaps when each paper is reviewed against:

1. data already proven or recorded locally,
2. the content-addressed claim/topic memory,
3. existing LCR topic boundaries,
4. the paper's actual equations, observables, data, and limitations.

This is not a blanket closure rule. A new publication can support, constrain, falsify, or route a local claim. It closes a gap only when the derivation chain is explicit and legal to the full system.

## Local anchors

Use these as routing context, not as source material for the external review itself:

| Anchor | Purpose |
|---|---|
| `CQE-CMPLX-1T-Production/WORK-AUDIT.md` | Proven vs received vs open status, including 149-tile topology and 13,157 claim-record substrate. |
| `CQE-CMPLX-1T-Production/src/papers/master_topics/MASTER_TOPIC_INDEX.json` | Master topic packages and primary paper routes. |
| `CQE-CMPLX-1T-Production/src/corpus/extracts/promoted-2026-06-19/current-governance/master_gap_registry_FINAL.csv` | Open source/layer gaps that may need external attachments. |
| `CMPLX-R30-main/CATALOG/claim_catalog.json` | Content-addressed claim/source records with hashes and source locators. |
| `papers/active-rework/FINAL_PAPERS_FLCR_UNIFIED/CAM_CRYSTAL_MEMORY_BANK/` | CAM crystal memory routing surface. |
| `PAIRWISE_EXTERNAL_EVIDENCE_PACKAGE_PROTOCOL.md` | Existing pair-package format for internal/external evidence coupling. |
| `NOVEL_EXTERNAL_PUBLICATION_DISCOVERY_PASS_2026_06_30.md` | Novel external-publication queue; only papers outside existing local discovery chains belong here. |

## Review unit

Each review unit is one real external scientific publication. It must carry:

| Field | Required content |
|---|---|
| `external_id` | DOI, arXiv ID, PubMed ID, or publisher URL. |
| `novelty_status` | `new_to_local_chain`, `known_existing_chain`, or `duplicate_reject`. |
| `scientific_claim` | What the paper itself claims, without local-system interpretation. |
| `evidence_type` | Experiment, simulation, theorem, model, survey, measurement, dataset, or review. |
| `variables_observables` | The actual quantities used by the paper. |
| `local_data_anchor` | Local claim, dataset, verifier, receipt, CAM crystal, topic, or gap. |
| `lcr_attachment` | L, C, R, and T/readout mapping, if bounded. |
| `topic_route` | Existing LCR topic/package/paper if one exists. |
| `derivation_obligation` | Required when no existing topic or claim boundary can legally absorb the paper. |
| `status` | `candidate`, `attached`, `derivation_required`, `falsifier`, `gap_closed_pending_review`, or `rejected`. |

## Closure rule

A publication may move a gap toward closure only if all five conditions hold:

1. The publication is real and traceable to a primary source.
2. The local claim or gap is content-addressed or otherwise source-located.
3. The mapping preserves the publication's own variables and limits.
4. The LCR route is explicit enough to be falsified.
5. The missing derivation, if any, is written before promotion.

If any condition fails, the paper remains useful but does not close the gap. It becomes either a comparator, a route suggestion, or a derivation obligation.

## Status lanes

| Lane | Meaning |
|---|---|
| `external_comparator` | Paper constrains or compares against a local claim but does not validate it. |
| `external_support` | Paper supplies independent evidence for a bounded local pattern. |
| `external_falsifier` | Paper contradicts or narrows a local claim. |
| `topic_extension` | Paper fits an existing LCR topic but adds new observables or boundary cases. |
| `new_derivation_required` | Paper appears relevant, but no existing local topic/claim can legally absorb it yet. |
| `gap_closure_candidate` | Paper plus local data appear sufficient to close a named open gap, pending review. |

## Scale pass

Run the explorer in batches:

1. Build/update the known external ID exclusion set from existing discovery, PEEP, and attachment ledgers.
2. Search current primary scientific sources for papers outside that exclusion set.
3. Add only novel candidates to the novel-discovery pass.
4. For each candidate, extract the paper's own variables, equations, measurements, and stated limits.
5. Route against master topics, claim catalog, gap registry, and CAM crystal memory.
6. If the route is absent, write the derivation obligation immediately.
7. Promote only reviewed attachments into pairwise evidence packages.

## Non-promotion guard

No paper should be described as proving CQE/CMPLX merely because it resembles an LCR pattern. The allowed language before full derivation is:

- constrains,
- supports,
- supplies a comparator,
- suggests a topic extension,
- provides a falsifier,
- creates a derivation obligation,
- becomes a gap-closure candidate.

The forbidden language before full derivation is:

- proves the model,
- validates the full system,
- closes the gap,
- confirms universality,
- establishes equivalence.

