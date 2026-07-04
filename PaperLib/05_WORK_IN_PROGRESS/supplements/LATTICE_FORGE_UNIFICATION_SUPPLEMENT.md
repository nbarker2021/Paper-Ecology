# Lattice Forge Unification Supplement

**Primary spine papers:** 00, 06, 08, 10, 12, 17, 20, 30, 32.

## Purpose

This supplement owns the `lattice_forge` / `lattice-forge` unification work. It records where every active or historical Lattice Forge surface lives, why the package split, which copy is canonical, and how extension modules should be promoted without losing proof honesty.

It also fixes the top-level intent: forge systems are how CQE/CMPLX is
expressed operationally. CAM stores addressable memory and receipts; Lattice
Forge actionizes that CAM surface into lookup contracts, executable methods,
receipts, events, and reusable cached answers.

## Source-of-Truth Rule

- Library/proof API: `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge`
- Product/domain modules: `D:\CQE_CMPLX\CQE-CMPLX-1T-Production`, but not under top-level `lattice_forge` unless promoted through tests, claims, and receipts
- Historical/provenance copies: read-only evidence
- Product stick folders: compatibility shims only, no new math logic

## Current Finding

`lattice_forge` split because it carried three jobs at once:

1. proof/research substrate for Rule 30, formal-suite receipts, and paper claims;
2. installable library/API surface for PartsFactory `lattice-forge 0.3.0`;
3. product-vendored runtime substrate for CMPLX-1T, GaussHaus, PaneForge, SplatForge, and forge-ring bundles.

## Canonical Unification Artifacts

- `D:\Paper Reworks\lattice_forge_unification\LATTICE_FORGE_UNIFICATION_MAP.md`
- `D:\Paper Reworks\lattice_forge_unification\lattice_forge_directory_inventory.json`
- `D:\Paper Reworks\lattice_forge_unification\lattice_forge_named_file_inventory.json`
- `D:\Paper Reworks\lattice_forge_unification\module_diff_against_partsfactory.json`
- `D:\Paper Reworks\lattice_forge_unification\EXTENSION_CANDIDATES.json`
- `D:\Paper Reworks\lattice_forge_unification\EXTENSION_CANDIDATES.md`

## Promotion Contract

No module moves into canonical `lattice-forge` only because it exists in a richer product tree. It must have:

- a named source path,
- a classified destination,
- a receipt/test path,
- a proof-status or claim-status row,
- a dependency-policy check,
- a reason it belongs in canonical library core rather than product extension,
- the CAM face, receipt, label, memory window, or obligation it actionizes.

## CAM Actionization Contract

Every canonical forge action should be able to state:

```text
CAM address / receipt / label
  -> Forge lookup contract
  -> seed or overlay query
  -> typed result
  -> receipt + event + query-cache row
  -> reusable action surface
```

If a module only computes privately, it is not yet a forge-system expression.
If it reads a CAM-addressed need, returns an honest typed result, and records
the receipt/cache trail, it is eligible to become part of the canonical forge
surface.

## No-Cost Lookup Update: Leech

Some papers still describe solved lookup surfaces as open reconstruction work.
The first corrected target is Leech.

Canonical `lattice-forge` now exposes:

- `Forge.leech_lookup(address=0, payload=None)`
- `Forge.verify_leech_lookup()`
- `lattice_forge.lattice_codes.verify_lattice_code_chain`
- `lattice_forge.lattice_codes.verify_golay_24`
- `lattice_forge.enumerated_glue.derive_classical_leech_minimal_landing`
- `lattice_forge.enumerated_glue.encode_leech_ribbon`

The verified contract is:

```text
incoming CAM state / address
  -> Niemeier:Leech rootless terminal tree
  -> Golay-backed classical minimal-shell address
  -> optional radix-196560 payload ribbon
  -> receipt + event + query-cache row
```

`verify_leech_lookup()` passes over the code chain, Golay ingredients,
scaled-coordinate Leech membership oracle, three classical minimal-vector
families totaling 196,560, and reversible byte ribbons over those vector
addresses.

Paper impact:

- Paper 08 may claim the practical rootless Leech lookup surface is closed.
- Paper 10 may bind Leech lookup as a materialized master-receipt lookup.
- Paper 17 may use Leech as a receipted error-correction tower surface.
- Paper 30 may propagate Leech as a reusable corpus-ribbon bead.
- Later forge/product papers should call the lookup rather than re-derive it.

Remaining honest boundaries:

- Gamma72 landing and polarization claims.
- Nontrivial rootful Niemeier glue-coset representative imports.
- Expanded Leech invariant/orbit proofs beyond the classical minimal-shell
  accounting.
- Physical identifications that require empirical or domain-specific evidence.

## Immediate Queue

1. Read active PartsFactory docs and claim registries.
2. Read product-only module candidates from 1T/GaussHaus and classify each as core/proof/product/receipt/data/historical.
3. Read R30/Formal-Suite proof-only deltas and decide whether they are evidence, tests, or canonical candidates.
4. Replace product-stick logic with shims only after stable canonical APIs exist.
