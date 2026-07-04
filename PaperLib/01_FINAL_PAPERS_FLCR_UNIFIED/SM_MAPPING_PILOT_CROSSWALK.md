# SM Mapping Pilot Crosswalk (FLCR-31..33)

**Generated:** 2026-07-01T08:54:27.066774+00:00
**Total rows:** 44

| FLCR | Rows | Closed | Open | IRL sources |
|---|---:|---:|---:|---|
| `FLCR-31` | 15 | 14 | 1 | `IRL-CODATA-2022-WALLET`, `IRL-NIST-ALPHA-2022`, `IRL-PDG-2026` |
| `FLCR-32` | 14 | 12 | 2 | `IRL-PDG-2024`, `IRL-PDG-2026` |
| `FLCR-33` | 15 | 13 | 2 | `IRL-ATLAS-HIGGS-2012`, `IRL-CMS-HIGGS-2012`, `IRL-CODATA-2022-WALLET` |

## Dependency graph (native FLCR prerequisites)

Translation rows cite internal proofs from FLCR-01..30 maximal manuscripts. See per-row `native_flcr_deps` in `SM_MAPPING_MATRIX.json`.

## SMB-01 closure rule

```text
claim -> SMD definition -> FLCR dependency -> lane -> evidence -> boundary -> falsifier
```