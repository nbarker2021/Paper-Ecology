# Source Placement - FLCR-19 - Layer-2 Synthesis Ledger

This file answers the routing question for this paper:

> What, across all locations, needs to live here fully, partially, or transiently
> to make the proof as complete as possible?

Placement meanings:

- **Full:** material should be integrated into the formal paper body, definitions,
  proof sketch, claim table, or workbook because it is local to this paper.
- **Partial:** material should be mined for relevant rows, receipts, guard
  language, cross-paper dependencies, or obligations, but should not be copied
  wholesale.
- **Transient:** material should be queried during drafting or validation, but
  the paper should retain only resulting citations, receipt hashes, lane rows,
  or source references.

## Full Placement

| Source | Why it belongs here |
|---|---|
| `20_Layer_2_Synthesis_Ledger.md` | primary assigned source for the paper's formal spine |
| `supplements/20_INTERNAL_REASONING_SUPPLEMENT.md` | paper-local reasoning supplement; should be integrated into definitions, proof sketch, and limitations |
| `virtuous\20_Layer-2_Synthesis_Ledger_VIRTUOUS.md` | prior enriched paper body; should be mined for mature claims and proof ordering |

## Partial Placement

| Source | Why it belongs here |
|---|---|
| `supplements/SM_BRIDGE_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/OBLIGATION_LEDGER_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/RECEIPT_VERIFIER_CATALOG.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_PYRAMID_INDEX.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_5P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_7P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `supplements/INTERNAL_REASONING_9P_WINDOW_SUPPLEMENT.md` | cross-cutting supplement; import only paper-relevant rows, receipts, or guard language |
| `CAM_CLAIM_100_SCORE_AUDIT.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NSIT_TOOL_CLOSURE_MATRIX.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NSIT_REASONED_CLOSURE_PASS.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `ORBITAL_DATA_CROSS_POPULATION_AUDIT.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `AGENT_CRYSTAL_WORK_HARVEST.md` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `PAPER_REWORKS_CRYSTAL_PROJECTION.json` | series-wide audit/score/closure evidence; import paper-specific rows and leave global context outside the body |
| `NEW_PAPER_NEEDS.md` | route relevant obligations into this paper's burden table: NP-05 Receipt Ecology And 32-Paper Causal Graph |
| `NEW_PAPER_NEEDS.md` | route relevant obligations into this paper's burden table: NP-08 Bibliography, Taxonomy, And Claim-Layer Governance |
| `NEW_PAPER_NEEDS.md` | route relevant obligations into this paper's burden table: NP-13 Reasoned Reapplication Of Standard Formalism Across The Corpus |
| `ORBITAL_DATA_CROSS_POPULATION_AUDIT.md` | claim-nature split required here: receipts/governance formal evidence |

## Transient Placement

| Source | Why it belongs here |
|---|---|
| `D:\DockerContainers\Manny Docker Starter\mannyai\brain\window_summary.json` | intake/query source; use to locate claims, assets, prompts, crystals, windows, or nodes, but do not embed wholesale |
| `D:\DockerContainers\Manny Docker Starter\mannyai\papers\nodes` | intake/query source; use to locate claims, assets, prompts, crystals, windows, or nodes, but do not embed wholesale |
| `D:\DockerContainers\Manny Docker Starter\database\nodes` | intake/query source; use to locate claims, assets, prompts, crystals, windows, or nodes, but do not embed wholesale |
| `D:\DockerContainers\Manny Docker Starter\database\windows` | intake/query source; use to locate claims, assets, prompts, crystals, windows, or nodes, but do not embed wholesale |
| `C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers\NOTEBOOKLM_REVIEW_PROMPTS.md` | intake/query source; use to locate claims, assets, prompts, crystals, windows, or nodes, but do not embed wholesale |
| `C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers\SERIES_INDEX.csv` | intake/query source; use to locate claims, assets, prompts, crystals, windows, or nodes, but do not embed wholesale |
| `C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers\CAM_ADDRESS_GRAMMAR.md` | intake/query source; use to locate claims, assets, prompts, crystals, windows, or nodes, but do not embed wholesale |
| `C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers\MannyAI_Unified_Crystal_Manifest_v0.yaml` | intake/query source; use to locate claims, assets, prompts, crystals, windows, or nodes, but do not embed wholesale |
| `C:\Users\nbark\Downloads\Papers-20260626T194053Z-3-001\Papers\ANALOG_WORKBOOK_ASSEMBLY.json` | intake/query source; use to locate claims, assets, prompts, crystals, windows, or nodes, but do not embed wholesale |

## Rewrite Instruction

During the next body rewrite, move the **Full** items into the paper's actual
argument. Convert **Partial** items into claim-lane rows, evidence rows,
obligations, or citations. Use **Transient** items as query surfaces and record
only stable outputs.
