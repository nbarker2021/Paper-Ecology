# Standard Model Translation — Master Crosswalk (from maximal FLCR)

**Generated:** 2026-07-01T08:02:12.064965+00:00

This crosswalk is the working surface for **defining and explaining into Standard Model parts** using maximal-claim FLCR manuscripts (LCR voice) + SMD/SMB defining papers (external physics voice) + IRL calibration data already attached in the corpus.

## Architecture

```text
FLCR-01..30 (maximal)  →  internal LCR proof stack
SMD-01..12 + SMB-01    →  external SM definition + closure bridge
FLCR-31..40 (maximal)  →  translation + literal-physics program
IRL registry           →  PDG / CODATA / ATLAS / CMS / domain data
```

## SMD → FLCR translation routing (SMB-01)

| SMD | Definition surface | Translation papers |
|---|---|---|
| `SMD-01` | Standard Model Definition Contract And Evidence Boundary | `FLCR-31`, `FLCR-39`, `FLCR-40` |
| `SMD-02` | Gauge Principle, Connections, And Local Symmetry | `FLCR-31`, `FLCR-35`, `FLCR-40` |
| `SMD-03` | Gauge Group SU3 SU2 U1 And Representation Content | `FLCR-31`, `FLCR-32`, `FLCR-33`, `FLCR-40` |
| `SMD-04` | Fermion Fields, Generations, Flavor, And Mixing | `FLCR-31`, `FLCR-32`, `FLCR-33`, `FLCR-38`, `FLCR-40` |
| `SMD-05` | QCD Color Dynamics And Hadronic Boundary | `FLCR-32`, `FLCR-37`, `FLCR-40` |
| `SMD-06` | Electroweak Interaction And Symmetry Breaking | `FLCR-31`, `FLCR-33`, `FLCR-40` |
| `SMD-07` | Higgs Sector, Vacuum Structure, And Mass Terms | `FLCR-33`, `FLCR-34`, `FLCR-40` |
| `SMD-08` | Renormalization, Effective Field Theory, And Running Parameters | `FLCR-31`, `FLCR-32`, `FLCR-33`, `FLCR-37`, `FLCR-39`, `FLCR-40` |
| `SMD-09` | Neutrino Sector, Oscillation Evidence, And Beyond-Minimal Residues | `FLCR-33`, `FLCR-38`, `FLCR-39`, `FLCR-40` |
| `SMD-10` | Electron Hole Exciton And Condensed Matter Correspondence | `FLCR-34`, `FLCR-36`, `FLCR-40` |
| `SMD-11` | GR Continuum Interface And Units-Bearing Calibration | `FLCR-35`, `FLCR-37`, `FLCR-40` |
| `SMD-12` | Standard Model Comparator And Falsifier Protocol | `FLCR-39`, `FLCR-40` |

## Translation papers explained

| FLCR | SMD deps | IRL sources | Explained doc |
|---|---|---|---|
| `FLCR-31` | `SMD-01`, `SMD-02`, `SMD-03`, `SMD-04`, `SMD-06`, `SMD-08` | `IRL-CODATA-2022-WALLET`, `IRL-NIST-ALPHA-2022`, `IRL-PDG-2026` | [`FLCR-31__sm_translation.md`](FLCR-31__sm_translation_explained.md) |
| `FLCR-32` | `SMD-01`, `SMD-03`, `SMD-05`, `SMD-08`, `SMD-12` | `IRL-PDG-2024`, `IRL-PDG-2026` | [`FLCR-32__sm_translation.md`](FLCR-32__sm_translation_explained.md) |
| `FLCR-33` | `SMD-01`, `SMD-06`, `SMD-07`, `SMD-08`, `SMD-09`, `SMD-12` | `IRL-ATLAS-HIGGS-2012`, `IRL-CMS-HIGGS-2012`, `IRL-CODATA-2022-WALLET` | [`FLCR-33__sm_translation.md`](FLCR-33__sm_translation_explained.md) |
| `FLCR-34` | `SMD-01`, `SMD-07`, `SMD-10`, `SMD-12` | `IRL-EXCITON-2D-REVIEW`, `IRL-EXCITON-SPRINGER`, `IRL-NIST-CARRIER-DYNAMICS`, `IRL-NIST-PV-EXCITON` | [`FLCR-34__sm_translation.md`](FLCR-34__sm_translation_explained.md) |
| `FLCR-35` | `SMD-01`, `SMD-02`, `SMD-11`, `SMD-12` | `IRL-CODATA-2022-WALLET`, `IRL-LRR-GR-HYPERBOLIC` | [`FLCR-35__sm_translation.md`](FLCR-35__sm_translation_explained.md) |
| `FLCR-36` | `SMD-01`, `SMD-10`, `SMD-11`, `SMD-12` | `IRL-EXCITON-2D-REVIEW`, `IRL-NIST-CARRIER-DYNAMICS`, `IRL-NIST-PV-EXCITON` | [`FLCR-36__sm_translation.md`](FLCR-36__sm_translation_explained.md) |
| `FLCR-37` | `SMD-01`, `SMD-05`, `SMD-08`, `SMD-11`, `SMD-12` | `IRL-CODATA-2022-WALLET`, `IRL-PPPL-PLASMA-DIAGNOSTICS-2026`, `IRL-PPPL-PLASMA-MAGNETIC` | [`FLCR-37__sm_translation.md`](FLCR-37__sm_translation_explained.md) |
| `FLCR-38` | `SMD-01`, `SMD-04`, `SMD-09`, `SMD-12` | `IRL-NOBEL-NEUTRINO-2015`, `IRL-PDG-2026` | [`FLCR-38__sm_translation.md`](FLCR-38__sm_translation_explained.md) |
| `FLCR-39` | `SMD-01`, `SMD-08`, `SMD-12` | `IRL-CODATA-2022-WALLET`, `IRL-NIST-ALPHA-2022`, `IRL-PDG-2026` | [`FLCR-39__sm_translation.md`](FLCR-39__sm_translation_explained.md) |
| `FLCR-40` | `SMD-01`, `SMD-02`, `SMD-03`, `SMD-04`, `SMD-05`, `SMD-06` … | — | [`FLCR-40__sm_translation.md`](FLCR-40__sm_translation_explained.md) |

## How to use this layer

1. Read the **maximal FLCR** paper for the full scientific hypothesis.
2. Read the matching **`__sm_translation_explained.md`** for which SMD part defines each external object.
3. Use **closure rows** to see what is already closed by formalism, proof, or attached data.
4. Treat remaining rows as **calibration channels** — attach units, datasets, comparators.

## Attached data surfaces

- IRL registry: [`IRL_STANDARD_MODEL_SOURCE_REGISTRY.md`](../standard_model_defining_papers/IRL_STANDARD_MODEL_SOURCE_REGISTRY.md)
- SMD workbooks + enrichment: `standard_model_defining_papers/SMD_WORKBOOK_ENRICHMENT_REPORT.json`
- PEEP / falsifier digest: assembled audit products per FLCR slot
