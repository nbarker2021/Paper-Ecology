# Paper Ecology — AI Constitution

**Read this file first.** Machine-readable companion: `AiGovernance/ECOLOGY.json`.

This workspace is an **active dev ecology** — there is **no canon yet**. All AI tools working
anywhere under `D:\Paper Ecology`, `D:\MannyAI`, or `D:\CQE_CMPLX` must follow the rules in
`D:\Paper Ecology\AiGovernance\rules\`.

## Universal pinned instruction

Before interpreting any MannyAI/CAM/CMPLX request, read and apply:

1. `D:\Paper Ecology\AiGovernance\ECOLOGY.json`
2. `D:\CQE_CMPLX\MANNYAI_METHOD_LOCK.md`
3. `D:\MannyAI\docs\ai-instructions\00-MANNYAI-METHOD-LOCK.md`
4. This file

MannyAI terms override ordinary AI defaults. Do not treat agent, coin, mint, brain, CAM, TarPit,
MDHG, SpeedLight, SplatForge, or Carrier-CEM as generic AI concepts.

## Locked meanings (summary)

| Term | MannyAI meaning | NOT |
|------|-----------------|-----|
| agent | durable identity: crystal + brain + wallet + lifecycle + agent coin | chat persona, task runner |
| coin | content-addressed validation/link handle | currency, token, reward |
| mint | SNAP-label settlement into coverage, wallet, receipts | reward issuance |
| brain | persisted TMNBrain over personal nodes | generic LLM memory |
| CAM-first | seed manifold, then TarPit/MDHG/SpeedLight/coins/writeback | answer-from-memory-and-stop |
| TarPit | fusion of CAM-known + unsaved data until degeneracy | — |
| MDHG | manifold address/shape/traversal | — |
| SpeedLight | compute-once reuse + Merkle receipts | optional cache |
| SplatForge | spatial manifold workbench | visualization only |

## Timestamp-first (no canon yet)

- Choose current/best version by **max(mtime) + hash**, not by reading prose.
- Stale README/info that merely resembles the need is **poison** — do not collapse onto it.
- Demotion: `Ecology\TemporalArchive\demoted_stale_<date>\` + append `DEMOTION_MANIFEST.json`.
  There is **no `_DEMOTED` folder**. Demotion ledger is separate from `merkle_ledger.jsonl`.
- Ground decisions in `SystemsLib\consolidation_audit\2026-07-06\file_manifest.jsonl`.

## Read first, do not guess

- Read authoritative docs **before** designing configs or architecture.
- ~75% prep / ~25% act. Do not decide from the first file found.
- Label evidence: `fact` · `claim` · `inference` · `open_question` · `preview_only`.
- Reuse code freely across the ecosystem.

## Environment contract

- **Python:** `D:\Paper Ecology\EnvLib\.venv\Scripts\python.exe`
- **Bootstrap:** `D:\Paper Ecology\EnvLib\bootstrap_env.ps1` (offline-first; wheelhouse at `EnvLib\wheelhouse\`)
- **Kernel:** `D:\Paper Ecology\cqekernel` — stdlib-only, zero runtime deps, editable install only
- **Shell:** PowerShell 7 with `-ExecutionPolicy Bypass`
- **Forge:** `FORGE_BASE=D:/forge-base/lib`

## Workspace roles

| Path | Role |
|------|------|
| `D:\Paper Ecology` | Accumulation target — papers, libs, env, governance |
| `D:\MannyAI` | Active MannyAI staging — MCP, CEM, plugins |
| `D:\CQE_CMPLX` | Control-plane — multi-repo workspace, method lock source |

## LLM backfill contract

LLM is **gap backfill only** — after SNAP/TarPit/MDHG/gaps are explicit. Output is candidate
structure that re-enters validation; never canonical on its own. Do not use LLM priors to define
methodology before the Manny chain runs.

## Noncanonical gate checklist

Do not call work canonical unless it shows: CAM seed, SpeedLight warm/prefetch, full label
provenance, TarPit fusion, degeneracy receipt, MDHG placement, coin/receipt/crystal links,
local node, identity object (if claiming agent), explicit gap objects (if LLM backfill).
Otherwise label `preview_only` / `noncanonical` and name missing gates.

## Rule files (load all)

```
AiGovernance/rules/000-mannyai-method-lock.md
AiGovernance/rules/010-read-first-no-guess.md
AiGovernance/rules/020-timestamp-first-no-canon.md
AiGovernance/rules/030-environment-contract.md
AiGovernance/rules/040-llm-backfill-contract.md
```

Cursor-format (`.mdc`, alwaysApply): `AiGovernance/cursor-rules/`
