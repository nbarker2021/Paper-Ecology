# MannyAI-Frontier

Local-only paper ecology workspace for MannyAI frontier work.

This repository preserves the existing workspace layout and tracks it from
`D:\Paper Ecology`. The FLCR paper corpus is managed as a local Git submodule
at `FLCR`.

## MannyAI Snapshot

The active local MannyAI build from `D:\MannyAI` is mirrored into
`SystemsLib\MannyAI` as a local-only system lane. The 2026-07-06 consolidation
audit verified 373 exact SHA-256 matches, 0 missing MannyAI files, and 0
same-name changed MannyAI files.

Primary audit receipts live under
`SystemsLib\consolidation_audit\2026-07-06`.

## Submodules

- `FLCR` - Formalizing LCR, Unifying SM. Contains the UFT100 paper corpus
  snapshot for Unified Field Theory in 100 Papers.

## Preserved Independent Worktrees

The existing `CMPLX-Standards`, `cqekernel`, and `DockerContainers` directories
already contain their own `.git` directories. They are preserved in place and
ignored by this parent repo unless they are intentionally converted to
submodules later.
