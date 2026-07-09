# 02 — Timestamp-First, No Canon Yet

Active dev workspaces (especially `D:\Paper Ecology`) have **NO canon** until all asserting
work is unified into ONE form.

- **Choose the current/best version by max(mtime) + hash — NOT by reading prose.** A stale doc
  that merely resembles the need collapses the universe onto it. README/info/summary prose is
  not a decision source. (An AI is time-blind, so make the timestamp the primary key.)
- Every older state is **kept and merkle-chained behind** the newest — never deleted.
- **Demotion destination = `D:\Paper Ecology\Ecology\TemporalArchive\demoted_stale_<YYYY-MM-DD>\<relpath>`**
  (move, never delete). Append a row to that pass's `DEMOTION_MANIFEST.json`
  (`paper_ecology.demotion_manifest.v1`, its OWN merkle chain). **There is no `_DEMOTED` folder.**
  The full-tree `merkle_ledger.jsonl` is a SEPARATE index, not the demotion ledger.
- Ground decisions in the structured indexes (timestamps/hashes), not prose:
  `D:\Paper Ecology\SystemsLib\consolidation_audit\2026-07-06\file_manifest.jsonl` and
  `merkle_ledger.jsonl`.

Do not run destructive moves without a current directive confirming destination + the
newest-tree-keep rule. See `docs\ai-instructions\10-PAPER-ECOLOGY-CONSOLIDATION.md` and
`07-STALENESS-POLICY.md`.