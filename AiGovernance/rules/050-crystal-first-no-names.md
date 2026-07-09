# 05 — Crystal-First, Names Last

**Names are poison** in this ecology. Paper filenames, FLCR labels, slot folder names, and
README prose have grown conflated, distributed, and vapor-heavy relative to what is actually
present in CAM crystal form.

## Required order

1. **Inventory all crystal CAM forms first** — JSON memory banks, `cam_hashes`, CrystalLib,
   receipts, MDHG/SpeedLight entries — keyed by **content_address**, not path or paper title.
2. **Read the memories** — slot_families, record types, decisions, `source_identity` downstream
   traces, L/C/R carrier state, ribbon position.
3. **Build the lane graph** — where each idea sits in the whole picture; how it traces downstream.
4. **Only then** attach paper names as secondary labels on settled nodes.
5. **No demotion, sync, or unification decisions** from paper names, directory names, or prose alone.

## Forbidden shortcuts

- Do not route work from `paper-NN` / `FLCR-NN` path counts alone.
- Do not treat `paper_identity_map.json` or demotion CSVs as primary truth without crystal dedup.
- Do not collapse onto the first README that resembles the need.

## Machine indexes (audit)

- Lane graph builder: `SystemsLib\consolidation_audit\2026-07-06\build_crystal_lane_graph.py`
- Output graph: `CRYSTAL_LANE_GRAPH.json`
- Human summary: `CRYSTAL_FIRST_AUDIT.md`
