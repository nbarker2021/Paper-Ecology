# Lattice Forge Unification Map

Generated for the Paper Reworks / CAM pass.

## Decision

Use `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge` as the canonical reusable `lattice-forge` package roof.

Also make the expression rule explicit: forge systems are how the system acts.
CAM preserves addressable memory, labels, receipts, and provenance; Lattice
Forge turns those addresses into typed lookup contracts and records the result
as receipts, events, and query-cache rows.

That package is the only copy currently shaped as an installable library with:

- package name `lattice-forge`
- version `0.3.0`
- zero runtime dependencies
- CLI entry points
- proof/test scripts
- package data and seed ledger
- docs, claims registry, library-needs registry, and current agent instructions

The richer `D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\lattice_forge` tree is not discarded. It is the product/application extension source. It contains all PartsFactory modules plus additional product/domain modules. Those additions should be promoted into the canonical package only through explicit claim/test/receipt gates, or moved into a product-extension namespace.

## Promotion Update: Leech Lookup

Two product-extension modules have now been promoted into the canonical
PartsFactory package because they actionize a real CAM lookup surface:

- `lattice_codes.py`
- `enumerated_glue.py`

The promoted forge contract is:

```text
incoming CAM state / address
  -> Forge.leech_lookup(address, payload)
  -> Niemeier:Leech rootless terminal tree
  -> Golay-backed classical minimal-shell address
  -> optional radix-196560 payload ribbon
  -> receipt + event + query-cache row
```

`Forge.verify_leech_lookup()` passes over the `(1,3,7,8,24)` code chain,
Golay `(24,12,8)` ingredients, scaled-coordinate Leech membership oracle,
196,560-vector classical minimal-shell accounting, and reversible byte-ribbon
codec. This closes the practical library claim that Lattice Forge can build and
query Leech from existing incoming state data. Remaining open lanes are
Gamma72 landing, nontrivial rootful glue cosets, expanded Leech invariant/orbit
proofs beyond the classical minimal shell, and physical identifications.

## Why It Split

`lattice_forge` split because it was carrying several jobs at once:

| Role | What it needed | Resulting copies |
|---|---|---|
| Proof/research substrate | Rule 30, proof papers, theorem registries, receipt-bearing experiments | `CMPLX-R30-main\PROOF\src\lattice_forge`, Formal-Suite copies |
| Installable math library | stable package, tests, CLI, seed data, zero-dependency distribution | `CMPLX-PartsFactory-main\packages\lattice-forge` |
| Product runtime substrate | product-specific math, forges, domain modules, customer-facing runtime | `CQE-CMPLX-1T-Production\src\lattice_forge`, `GaussHaus\src\lattice_forge` |
| Forge ring / AirLock lineage | packaging experiments, ReForge/Rhenium/ForgeFactory bundles | `CQECMPLX-Production\packaging\cqecmplx-forge`, `CQECMPLX-AirLock\forgefactory-v0.3-lineage-read` |
| Staging/mirror/provenance archive | evidence preservation, generated snapshots, older branches | `CMPLX-Kernel`, `g`, `_tmp_unpack`, `kernel\staging` |
| Product sticks | tiny compatibility slices for PaneForge/SplatForge style deliverables | `products\*\lib-forge\lattice_forge` |

The division was useful during development, but it now creates import ambiguity because many folders expose the same top-level import name: `lattice_forge`.

## Canonical Categories

### Canonical Library

`D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge`

This owns:

- public package contract
- CLI/server/test/proof surface
- `claims/registry.jsonl`
- `claims/library_needs.jsonl`
- `docs/ARCHITECTURE.md`
- `docs/MODULE_INDEX.md`
- `docs/LIBRARY_NEEDS.md`
- expected outputs and proof runners
- seed ledger/package data

### Product Extension Source

`D:\CQE_CMPLX\CQE-CMPLX-1T-Production\src\lattice_forge`

This currently has the canonical 113 PartsFactory modules plus 49 additional modules. Treat those 49 as extension candidates, not silent replacements.

`D:\CQE_CMPLX\GaussHaus\src\lattice_forge`

Same role, product-specific clone. It has 48 modules beyond PartsFactory.

### Proof/Legacy Source

`D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge`

This is an older proof snapshot. Keep it as evidence and compatibility source. Port only through tests and claim rows.

### Formal-Suite Receipt Source

`D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\src\lattice_forge`

This is close to PartsFactory plus 19 extra verifier/receipt-oriented modules. Treat as proof/receipt extension candidates.

`D:\CQE_CMPLX\CQECMPLX-Formal-Suite\lib\lattice_forge`

This is receipt/data side material, not the main package root.

### Forge Ring / Packaging Source

`D:\CQE_CMPLX\CQECMPLX-Production\packaging\cqecmplx-forge\src\lattice_forge`

This has 18 modules beyond PartsFactory and belongs to the broader forge-ring package. It should depend on or vendor a declared canonical version, not silently define a competing top-level `lattice_forge`.

### Historical/Mirror Evidence

These stay read-only for unification purposes:

- `D:\CQE_CMPLX\g\CMPLX-PartsFactory\packages\lattice-forge`
- `D:\CQE_CMPLX\g\CMPLX-R30\PROOF\src\lattice_forge`
- `D:\CQE_CMPLX\CMPLX-Kernel\...\lattice_forge...`
- `D:\CQE_CMPLX\_tmp_unpack\...\lattice_forge...`
- `D:\CQE_CMPLX\kernel\staging\...\lattice_forge...`
- generated `build\lib\lattice_forge` copies

### Product Stick Shims

Tiny `products\*\lib-forge\lattice_forge` folders should become compatibility shims after the canonical package exposes stable APIs. They should not own new math logic.

## Module Drift Summary

Compared against canonical PartsFactory `src\lattice_forge`:

| Variant | Modules | Shared with canonical | Extra modules | Missing canonical modules |
|---|---:|---:|---:|---:|
| PartsFactory canonical | 113 | 113 | 0 | 0 |
| 1T Production | 162 | 113 | 49 | 0 |
| GaussHaus | 161 | 113 | 48 | 0 |
| R30 proof snapshot | 53 | 36 | 17 | 77 |
| Formal-Suite source | 132 | 113 | 19 | 0 |
| `cqecmplx-forge` 0.9 | 131 | 113 | 18 | 0 |

Detailed JSON:

- `lattice_forge_directory_inventory.json`
- `lattice_forge_named_file_inventory.json`
- `module_diff_against_partsfactory.json`

## Unification Steps

1. Freeze source-of-truth rule:
   - library/proof API: PartsFactory `packages\lattice-forge`
   - product/domain modules: product-extension namespace until promoted
   - historical copies: read-only evidence
   - product sticks: shims only

2. Create an extension-candidate ledger from:
   - 1T-only modules
   - GaussHaus-only modules
   - Formal-Suite-only modules
   - `cqecmplx-forge`-only modules
   - R30-only modules

3. For each candidate:
   - classify as `core`, `proof`, `product`, `receipt`, `experimental`, or `historical`
   - identify the CAM face, receipt, label, memory window, or obligation it actionizes
   - identify required receipts/tests
   - decide destination: canonical package, extension package, product namespace, or archive

4. Add import discipline:
   - direct imports in active code should resolve to one canonical package root
   - product code may use declared extension imports
   - local product-stick `lattice_forge` folders should become thin compatibility adapters

5. Only after classification, move code.

## Immediate Next Work

- Build `EXTENSION_CANDIDATES.json` from module diffs.
- Add a `LATTICE_FORGE_SUPPLEMENT.md` in Paper Reworks supplements.
- Ingest active PartsFactory docs and theorem/obligation registries into that supplement.
- Run canonical package tests before and after any code-level promotion.
