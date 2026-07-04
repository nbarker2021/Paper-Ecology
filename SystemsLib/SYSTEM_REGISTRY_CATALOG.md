# SYSTEM REGISTRY CATALOG — A-Family Mapping

**Workspace:** `D:\CQE_CMPLX`  
**Catalog target:** `D:\Paper Ecology\SystemsLib\SYSTEM_REGISTRY_CATALOG.md`  
**Generated:** Current session  
**Convention:** All content remapped to A-family (paper-00 through paper-100, LCR kernel, D/I/X). B-family identifiers (FLCR, NIST, IRL) are stripped and replaced.

---

## 1. Source Files Read

| File | Path | Lines | Notes |
|------|------|-------|-------|
| Root AGENTS.md | `D:\CQE_CMPLX\AGENTS.md` | 106 | Workspace overview; subproject AGENTS.md files take precedence for their areas. |
| Source Registry | `D:\CQE_CMPLX\flcr_extract\STANDARD_MODEL_DEFINING_PAPERS\IRL_STANDARD_MODEL_SOURCE_REGISTRY.json` | 118 | 16 registered external sources with B-family schema and lane tags. |

---

## 2. Agent Runtime Routing (from AGENTS.md)

### 2.1 Workspace Architecture — A-Family Designation

The workspace is a multi-repository system. Each top-level subdirectory is an independent project. The following table maps each subsystem to its A-family designation.

| A-Family Designation | Directory | Role | D/I/X Tag |
|---|---|---|---|
| **LCR Kernel (paper-00)** | `cqekernel/` | stdlib kernel, zero dependencies | `D` (kernel contracts) |
| **PartsFactory (paper-10–paper-30)** | `CMPLX-PartsFactory-main/` | Service details, MCP routes, hard constraints, ring/runbook | `D` (service contracts) |
| **1T-Production (paper-40–paper-60)** | `CQE-CMPLX-1T-Production/` | Product placement rules, forge routing | `D/I` (product surfaces) |
| **GaussHaus (paper-45)** | `GaussHaus/` | Product surface (Gaussian / Hausdorff lane) | `I` (product implementation) |
| **Standards (paper-70)** | `CMPLX-Standards/` | Validator/grading surface | `D` (verification) |
| **Workbench (paper-90)** | `tools/` | Paper pipeline tooling, registry at `tools/TOOL_REGISTRY.md` | `X` (tooling / open questions) |
| **Showroom (paper-100)** | `g/CMPLX-1T/` | Master showroom navigation | `X` (reference / showroom) |

### 2.2 Subproject AGENTS.md Files (Referenced, Not Read Inline)

The root AGENTS.md delegates to the following subproject files. These contain deeper routing rules that were not expanded in this catalog because the two critical files did not include their full text.

| Subproject AGENTS.md | A-Family Domain | What It Governs |
|---|---|---|
| `CMPLX-PartsFactory-main/AGENTS.md` | paper-10–paper-30 | Service details, MCP routes, hard constraints, ring/runbook |
| `CQE-CMPLX-1T-Production/AGENTS.md` | paper-40–paper-60 | Product placement rules, forge routing |
| `CMPLX-Standards/AGENTS.md` | paper-70 | Validator/grading surface |
| `g/CMPLX-1T/AGENTS.md` | paper-100 | Master showroom navigation |
| `tools/TOOL_REGISTRY.md` | paper-90 | Workspace tooling index |

### 2.3 LCR Kernel Subcommands

The `cqekernel` CLI exposes 11 subcommands. These map directly to the LCR kernel surface (paper-00):

| CLI Subcommand | A-Family Role |
|---|---|
| `observe` | LCR kernel observation mode |
| `run` | Execution runner |
| `replay` | Deterministic replay engine |
| `verify` | **D-verification** |
| `workbook` | Workbook management |
| `firmware` | Firmware bridge |
| `packet` | Packet handling |
| `witness` | Witness generation / forge substrate |
| `d4` | D4 operator |

### 2.4 Forge Runtime Wrapper (Substrate Loader)

Use `tools\forge_runtime_env.ps1` when reasoning tasks need the canonical Lattice Forge substrate ahead of product split copies.

- **A-Family role:** paper-00 substrate loader; prepends `lattice-forge` and `ForgeFactory` `src/` to `PYTHONPATH`, then uses `_runtime\forge_reasoning` for local overlays, receipts, and caches.
- **Constraint:** Throws if either upstream `src/` is missing.
- **Surface:** `lattice-forge[0.3.0]` is current; older `0.2.x` paths are not the default edit target.

### 2.5 Service Ports — Local Control Plane

| Service | Port | Health Check | A-Family Role | Paper Range |
|---|---|---|---|---|
| Repo-Kernel (control plane) | 8786 | `/api/health` | LCR kernel control plane | paper-00 |
| Lattice Forge (witness) | 8845 | `/witness/spec` | Witness / forge substrate | paper-10–paper-30 |
| Proof Lab | 8871–8872 | `/health` | **D-verification lab** | paper-70 |
| Receipt | 8010 | `/health` | Claim receipt service | paper-20 |
| SpeedLight | 8843 | `/health` | SpeedLight service | paper-25 |
| TarPit | 8844 | `/health` | TarPit service | paper-25 |
| SNAP | 8823 | `/health` | SNAP service | paper-25 |

**Routing rule:** Prefer Repo-Kernel `/api/global/...` and `/call-plan` routes over direct upstream ports. Local HTTP services may be **down even when compose files exist** — probe before relying on live control-plane assumptions.

### 2.6 Operating Conventions

| Convention | A-Family Interpretation |
|---|---|
| **State** | Subproject repos are often dirty from active work — check `git status --short` before operations. |
| **DB** | Prefer local SQLite / filesystem for discovery, receipts, caches, dev loops. Avoid silent production writes. |
| **Math** | Do not introduce new private math when a `lattice_forge` contract exists — wrap or adapt. Product surfaces belong in `src/products/`; formal paper validators and receipts in `src/papers/formal/`. |
| **Secrets** | No root `.env`. `CMPLX-PartsFactory-main/.env.template` is the only template. Historical live secrets in `CMPLX-PartsFactory/.env` and `Unification Prototypes/configs/env_template/.env` were deleted 2026-05-17 and must be considered compromised if recovered. |
| **Provenance** | Preserve source path, timestamp, git status, and evidence type (`fact` / `claim` / `inference` / `open_question`). |

---

## 3. IRL Standard Model Source Registry — A-Family Remap

### 3.1 Schema Remap

- **Original (B-family):** `flcr_irl_standard_model_source_registry.v1`  
- **A-Family replacement:** `a_family_source_registry.v1`  
- **Date preserved:** `2026-06-28`

The `IRL-` prefix on all source IDs is B-family branding and has been stripped. The `NIST` institutional branding in titles and IDs has been replaced with generic physics-source identifiers.

### 3.2 Lane Remap

| Original Lane | A-Family Lane | D/I/X Interpretation |
|---|---|---|
| `standard_theorem_citation_bound_result` | `D_claim_citation_bound` | D-verified claim, citation-bound theorem |
| `external_calibration_result` | `I_calibration_input` | External calibration input (I-result) |

### 3.3 Registered Sources — Full A-Family Table

| A-Family ID | Original Title (B-family stripped) | Use | A-Family Lane |
|---|---|---|---|
| `SRC-PDG-2026` | Particle Data Group Review of Particle Physics 2026 | Particle properties, Standard Model reviews, summary tables, gauge boson/Higgs/lepton/quark data | `D_claim_citation_bound` |
| `SRC-PDG-2024` | Review of Particle Physics 2024/2025, Phys. Rev. D 110, 030001 | Stable citable PDG review for particle data and evaluated measurements | `D_claim_citation_bound` |
| `SRC-CODATA-2022` | CODATA Recommended Values of the Fundamental Physical Constants: 2022 | Units-bearing constants and exact SI constants for calibration rows | `I_calibration_input` |
| `SRC-ATLAS-HIGGS-2012` | ATLAS observation of a new particle in the search for the Standard Model Higgs boson | Higgs discovery evidence and mass-scale calibration surface | `I_calibration_input` |
| `SRC-CMS-HIGGS-2012` | CMS observation of a new boson at a mass of 125 GeV | Independent Higgs discovery evidence and mass-scale calibration surface | `I_calibration_input` |
| `SRC-NOBEL-NEUTRINO-2015` | Nobel advanced information: Neutrino Oscillations | Neutrino oscillation evidence and beyond-minimal Standard Model boundary | `D_claim_citation_bound` |
| `SRC-PHYS-CONSTANTS` | Fundamental Physical Constants extensive listing | Numerical constants, units, and uncertainty metadata for calibration tables | `I_calibration_input` |
| `SRC-EXCITON-SPRINGER` | Excitons reference entry, Springer Nature | Electron-hole, exciton, Wannier-Mott/Frenkel, binding-energy and dielectric/effective-mass formalism | `D_claim_citation_bound` |
| `SRC-EXCITON-2D` | Excitons in two-dimensional materials, arXiv:1911.00087 | Modern exciton review and material-dependent exciton evidence boundary | `D_claim_citation_bound` |
| `SRC-ALPHA-2022` | CODATA inverse fine-structure constant | Numerical alpha inverse calibration value: 137.035999177 with standard uncertainty 0.000000021 | `I_calibration_input` |
| `SRC-CODATA-WALLET-2022` | CODATA 2022 wallet card | Compact units and constants reference for calibration tables | `I_calibration_input` |
| `SRC-CARRIER-DYNAMICS` | Carrier dynamics by ultrafast time-resolved terahertz spectroscopy | Exciton/electron-hole separation, recombination, free carrier dynamics, and optoelectronic metrology lane | `I_calibration_input` |
| `SRC-PV-EXCITON` | Optoelectrical characterization of photovoltaic materials and devices | Materials lane for exciton separation into free electrons and holes at heterojunction interfaces | `I_calibration_input` |
| `SRC-GR-HYPERBOLIC` | Living Reviews in Relativity: Hyperbolic Methods for Einstein's Equations | GR/continuum formalism boundary for Einstein equations as PDE/hyperbolic systems after gauge and constraint handling | `D_claim_citation_bound` |
| `SRC-PLASMA-MAGNETIC` | PPPL fusion/plasma magnetic confinement testimony | Plasma boundary row for charged-particle motion and magnetic confinement | `D_claim_citation_bound` |
| `SRC-PLASMA-DIAGNOSTICS-2026` | PPPL Plasma Diagnostics lecture notes | Plasma definition/calibration row: plasma consists of particles and fields; diagnostics are required for measured claims | `I_calibration_input` |

---

## 4. Docker Orchestration Files

### 4.1 PartsFactory (paper-10–paper-30)

Located in `CMPLX-PartsFactory-main/`.

| Compose File | A-Family Role |
|---|---|
| `docker-compose.receipt.yml` | Claim receipt service |
| `docker-compose.speedlight.yml` | SpeedLight service |
| `docker-compose.tarpit.yml` | TarPit service |
| `docker-compose.snap.yml` | SNAP service |
| `docker-compose.lattice-forge.yml` | Lattice Forge witness substrate |
| `docker-compose.proof-lab.yml` | D-verification lab |
| `docker-compose.repo-kernel.yml` | LCR kernel control plane |
| `docker-compose.web.yml` | Web surface |
| `docker-compose.server.yml` | Server runtime |
| `docker-compose.cmplx-discord.yml` | Discord integration |
| `docker-compose.cmplxmcp-runtime.yml` | MCP runtime |
| `docker-compose.backwalk-builder.yml` | Backwalk builder |
| `docker-compose.backwalk-lattice-space.yml` | Backwalk lattice space |
| `docker-compose.backwalk-weyl-bond.yml` | Backwalk Weyl bond |
| `docker-compose.gitnexus-three-space.yml` | GitNexus three-space |
| `docker-compose.morphon-graph.yml` | Morphon graph |
| `docker-compose.dind.yml` | Docker-in-Docker bootstrap |
| `docker-compose.yml` | Top-level umbrella orchestration |

### 4.2 1T-Production (paper-40–paper-60)

Located in `CQE-CMPLX-1T-Production/`.

| Compose File | A-Family Role |
|---|---|
| `docker-compose.yml` | 1T-Production umbrella |
| `src/products/fourpack/docker-compose.fourpack.yml` | Fourpack product v1 |
| `src/products/fourpack/docker-compose.fourpack.v2.yml` | Fourpack product v2 |
| `src/products/fourpack/docker-compose.unified.yml` | Fourpack unified |
| `vendor/GaussHaus/docker-compose.yml` | GaussHaus product surface |

### 4.3 Kernel & Proof Validated Suite (paper-00, paper-70)

Located in `CMPLX-Kernel/` and `CQECMPLX-ProofValidatedSuite/`.

| Compose File | A-Family Role |
|---|---|
| `kernel/deploy/docker/docker-compose.kernel-dind.yml` | Kernel DIND bootstrap |
| `kernel/deploy/docker/docker-compose.kernel-socket.yml` | Kernel socket bootstrap |
| `kernel/docker-compose-kernel-validated.yml` | Kernel validated suite |
| `kernel/docker-compose-kernel-with-opencode.yml` | Kernel + opencode |
| `kernel/lib-forge/meta_material_system/docker-compose.yml` | Meta-material system |
| `kernel/lib-forge/odysseus/docker-compose.yml` | Odysseus base |
| `kernel/lib-forge/odysseus/docker-compose.gpu-amd.yml` | Odysseus AMD GPU |
| `kernel/lib-forge/odysseus/docker-compose.gpu-nvidia.yml` | Odysseus NVIDIA GPU |
| `kernel/modules/meta_material_system/docker-compose.yml` | Meta-material system (modules) |

### 4.4 Production Mirror

Located in `CQECMPLX-Production/`.

| Compose File | A-Family Role |
|---|---|
| `lib-forge/meta_material_system/docker-compose.yml` | Meta-material system mirror |
| `lib-forge/odysseus/docker-compose.yml` | Odysseus base mirror |
| `lib-forge/odysseus/docker-compose.gpu-amd.yml` | Odysseus AMD GPU mirror |
| `lib-forge/odysseus/docker-compose.gpu-nvidia.yml` | Odysseus NVIDIA GPU mirror |

### 4.5 Proof Validated Suite (Additional)

Located in `CQECMPLX-ProofValidatedSuite/`.

| Compose File | A-Family Role |
|---|---|
| `kernel/deploy/docker/docker-compose.kernel-dind.yml` | Kernel DIND bootstrap |
| `kernel/deploy/docker/docker-compose.kernel-socket.yml` | Kernel socket bootstrap |
| `kernel/docker-compose-kernel-validated.yml` | Kernel validated suite |
| `kernel/docker-compose-kernel-with-opencode.yml` | Kernel + opencode |
| `EXPOSE-PAPERS/meta_material_system/docker-compose.yml` | Meta-material system (exposed papers) |

### 4.6 Unassigned Container Experiments

Located in `DockerContainers/` — **not linked to active A-family service ports**.

| Compose File | Status |
|---|---|
| `docker-compose-advanced.yml` | Unassigned experiment |
| `docker-compose-complete-stack.yml` | Unassigned experiment |
| `docker-compose-hardened.yml` | Unassigned experiment |
| `docker-compose-minimal.yml` | Unassigned experiment |
| `docker-compose-with-databases.yml` | Unassigned experiment |
| `docker-compose-working.yml` | Unassigned experiment |

---

## 5. System-Level Metadata — A-Family Mappings

### 5.1 Paper-to-Source Dependencies

The registered sources feed directly into the A-family paper series as follows. These mappings are inferred from the `use` field of each source and the lane tag (`D_claim_citation_bound` vs `I_calibration_input`).

| A-Family Paper | Supported By | Dependency Type | Rationale |
|---|---|---|---|
| **paper-00** (LCR kernel, SI calibration) | `SRC-CODATA-2022`, `SRC-ALPHA-2022`, `SRC-CODATA-WALLET-2022`, `SRC-PHYS-CONSTANTS` | `I_calibration_input` | Exact SI constants and units-bearing calibration rows are kernel-level inputs. |
| **paper-01** (particle properties) | `SRC-PDG-2026`, `SRC-PDG-2024` | `D_claim_citation_bound` | PDG reviews are citation-bound claims for particle data. |
| **paper-02** (symmetry breaking / Higgs) | `SRC-ATLAS-HIGGS-2012`, `SRC-CMS-HIGGS-2012` | `I_calibration_input` | Higgs discovery evidence provides mass-scale calibration surfaces. |
| **paper-03** (beyond-minimal model) | `SRC-NOBEL-NEUTRINO-2015` | `D_claim_citation_bound` | Neutrino oscillation evidence sets a boundary for beyond-minimal claims. |
| **paper-20–paper-30** (exciton / materials formalism) | `SRC-EXCITON-SPRINGER`, `SRC-EXCITON-2D`, `SRC-CARRIER-DYNAMICS`, `SRC-PV-EXCITON` | Mixed (`D_claim_citation_bound` + `I_calibration_input`) | Exciton formalism, electron-hole separation, and optoelectronic metrology span both citation-bound theorems and calibration inputs. |
| **paper-50** (GR / continuum) | `SRC-GR-HYPERBOLIC` | `D_claim_citation_bound` | GR hyperbolic methods provide a citation-bound formalism boundary. |
| **paper-60** (plasma / confinement) | `SRC-PLASMA-MAGNETIC`, `SRC-PLASMA-DIAGNOSTICS-2026` | Mixed (`D_claim_citation_bound` + `I_calibration_input`) | Plasma magnetic confinement is a citation-bound theorem; plasma diagnostics are calibration inputs. |

### 5.2 D/I/X Tagging of the Registry

- **D-claims:** All sources tagged `D_claim_citation_bound` are **D-verified claims** (citation-bound theorems). They must be traceable to a published paper and cannot be overridden by private math.
- **I-inputs:** All sources tagged `I_calibration_input` are **external calibration inputs** (I-results). They feed calibration rows and uncertainty metadata.
- **X-questions:** No source in the registry is explicitly tagged as an open question. If any source later fails verification, it should be re-tagged as `X` and moved to the workbench (paper-90).

### 5.3 Provenance Rules for Source Harvesting

When harvesting old work or pulling from these external sources, the system requires preserving:
- Source path
- Timestamp
- Git status
- Evidence type (`fact` / `claim` / `inference` / `open_question`)

This maps to the A-family **evidence ledger** (paper-00 D-verification surface).

---

## 6. Unassigned Content

### 6.1 B-Family Artifacts (Stripped, Noted as Unassigned)

| B-Family Artifact | A-Family Disposition | Reason |
|---|---|---|
| Schema label `flcr_irl_standard_model_source_registry.v1` | Replaced with `a_family_source_registry.v1` | B-family schema identifier. |
| `IRL-` prefix on all source IDs | Replaced with `SRC-` prefix | B-family naming convention. |
| `NIST` institutional branding in titles/IDs | Replaced with generic `PHYS-` or removed | B-family institutional numbering. |
| `CMPLX` product prefix | Retained as directory name only; A-family papers use `paper-NN` | B-family product branding. |
| `CQE` prefix | Retained as directory name only | B-family project branding. |

### 6.2 Showroom & Historical Archives (Unassigned to Active Paper Series)

| Path | Status | A-Family Disposition |
|---|---|---|
| `g/CMPLX-1T/` | Master showroom | **paper-100** reference showroom; not a production edit target. |
| `g/CMPLXMCP/` | MCP showroom | **paper-100** reference. |
| `CMPLX-Manny/` | Manny Unification 2 lineage | Read-only historical evidence; not a current working target. |
| `_drive-audit/archive_history/unpacked/` | Historical evidence archive | Read-only audit trail; preserve as evidence. |
| `git-hosted-roots/CQECMPLX-Production/` | Production git mirror | Unassigned mirror. |
| `CQECMPLX-AirLock/forgefactory-v0.3-lineage-read/` | ForgeFactory lineage read | Read-only archive; unassigned to active paper series. |
| `CMPLX-Kernel/` | Historical kernel | Read-only evidence. |

### 6.3 Container Experiments (Unassigned)

The `DockerContainers/` directory contains six compose files that are **not linked to any active A-family service port** and do not appear in the root AGENTS.md health-check table. They are treated as unassigned experiments.

- `docker-compose-advanced.yml`
- `docker-compose-complete-stack.yml`
- `docker-compose-hardened.yml`
- `docker-compose-minimal.yml`
- `docker-compose-with-databases.yml`
- `docker-compose-working.yml`

### 6.4 Secrets Rotation Marker

`CMPLX-PartsFactory-main/SECRETS_ROTATION_REQUIRED.md` is a security marker. It is **unassigned** to any paper series but must be honored as a system-level constraint (paper-00 compliance).

---

## 7. Routing Summary

### 7.1 Preferred Routing Rules (A-Family)

1. **Control plane:** Always prefer Repo-Kernel `/api/global/...` and `/call-plan` routes over direct upstream ports.
2. **Math engine:** Do not introduce new private math when a `lattice_forge` contract exists — wrap or adapt.
3. **Product placement:** Product surfaces belong in `src/products/`; formal paper validators and receipts in `src/papers/formal/`.
4. **State:** Prefer SQLite / filesystem for discovery, receipts, caches, and dev loops. Use Postgres only when explicitly required.
5. **Validation:** `make boot validate paper00` triggers: engine arity table → end-to-end validate → **paper-00 smoke test**.

### 7.2 Compliance & Security

- **No root `.env`:** paper-00 environment rule.
- **Template only:** `CMPLX-PartsFactory-main/.env.template` is the only env template.
- **Compromised secrets:** Historical live secrets in `CMPLX-PartsFactory/.env` and `Unification Prototypes/configs/env_template/.env` were deleted 2026-05-17. If recovered, treat as compromised.

---

*Catalog generated from root AGENTS.md and IRL_STANDARD_MODEL_SOURCE_REGISTRY.json, fully remapped to A-family conventions (paper-00 through paper-100, LCR kernel, D/I/X).*
