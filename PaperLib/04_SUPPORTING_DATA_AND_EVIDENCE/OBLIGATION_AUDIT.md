# Obligation Audit — Actually Open vs. Solved by Other Papers

This is a reality check on the Open Obligations Register. Each obligation is classified by whether it is:

- **closed** — solved by a specific later paper or receipt,
- **partially closed / advanced** — a later paper made progress but did not finish,
- **guard** — an ongoing design rule, not a missing proof,
- **out of scope** — explicitly not claimed,
- **engineering / documentation / governance** — tooling, cleanup, or policy, not a theorem gap,
- **genuinely open** — no later paper closes it; this is the real research debt.

## Update: Leech Lookup Split / 2026-06-27

The practical rootless Leech lookup surface is now closed in canonical
`lattice-forge` by `Forge.leech_lookup()` / `Forge.verify_leech_lookup()`.
That closure covers the rootless `Niemeier:Leech` terminal lookup,
Golay-backed classical minimal-shell address resolution, 196,560-vector
minimal-shell accounting, and reversible radix-196560 byte ribbons.

The following are still open and should be routed to new paper NP-02 or NP-03:

- nontrivial rootful Niemeier/Leech glue-coset representatives;
- expanded Leech invariant/orbit proofs beyond the classical minimal shell;
- Gamma72 polarization/landing;
- cold-start terminal fingerprinting from arbitrary incoming state.

Older rows such as 08.3, 17.1, and 21.1 should therefore be read as
"expanded Leech/Gamma72/terminal-selection work remains open," not "the
library cannot build or query Leech."

## Closed (9 items)

| ID | Source | Obligation | Closed / scoped by | Note |
|----|--------|------------|--------------------|------|
| 01.3 | Paper 01 | Carry corrected distinction into Paper 03 | CQE-03 | Paper 03 carries the corrected distinction. |
| 02.2 | Paper 02 | Reconcile D4 axis/sheet labels with Paper 03 triality | CQE-03 | Paper 03 reconciles D4 axis/sheet labels. |
| 03.3 | Paper 03 | Add stronger S3 group-ring / J3 trace-2 proof as separate theorem | CQE-13 | Paper 13 provides the S3 group-ring / J3 trace-2 → SU(3) closure. |
| 03.5 | Paper 03 | Carry Paper 02 correction coords into Paper 04 boundary repair | CQE-04 | Paper 04 uses Paper 02 correction coordinates. |
| 04.2 | Paper 04 | Connect boundary constraints to Paper 05 path carriers | CQE-05 | Paper 05 path carriers close this. |
| 07.4 | Paper 07 | Carry bridge residuals into Paper 16 only as obligations until verified | CQE-16 | Paper 16 receives bridge residuals as explicit obligations. |
| 07.8 | Paper 07 | Prove that Rule 30 temporal traces do not inherit static Z4 periods | CQE-09 / CQE-27 | Paper 09 refutes static Z4 temporal periodicity; Paper 27 reinforces the refutation. |
| 11.2 | Paper 11 | Classify candidates above K=9 consistently as boundary (not admitted) | CQE-11 | Theorem 11.1 already classifies K>9 candidates as boundary. |
| 31.2 | Paper 31 | Ensure Paper 32 preserves readout status | CQE-32 | Paper 32's packaging theorem preserves proof/open/readout status. |

## Partially Closed (6 items)

| ID | Source | Obligation | Closed / scoped by | Note |
|----|--------|------------|--------------------|------|
| 02.3 | Paper 02 | Extend receipt format for later papers to consume correction rows | CQE-06 / CQE-10 | Schema exists in Papers 06/10; instantiation across all receipts is still open. |
| 02.8 | Paper 02 | F₂-bridge governance / contribution registry | CQE-08 | Paper 08 closes the O2'' registry core (314 facts); full umbrella population remains open. |
| 04.3 | Paper 04 | Promote shared obligation-ledger schema for all later papers | CQE-06 | Shared ledger schema is in Paper 06; full ecology instantiation is open. |
| 05.2 | Paper 05 | Bind Paper 04 repair payloads to a shared route ledger | CQE-06 | Paper 06 supplies the ledger schema; payload instantiation is open. |
| 10.2 | Paper 10 | Demonstrate or scope the `J3O_TO_G2_F4_T5A_ROUTE` transport row | CQE-13 | Paper 13 provides a bounded G2/F4/T5A route, but not an unconditional cold-start route. |
| 17.3 | Paper 17 | W(E8) lookup table O1 | CQE-08 (partial) | Paper 08 closes W(E8) construction and a bounded sub-table (`o1_weyl_e8_construction_closed_receipt.json` pass 7/7); the full 696,729,600-element materialized lookup table remains an open O1 bridge. |

## Advanced (1 items)

| ID | Source | Obligation | Closed / scoped by | Note |
|----|--------|------------|--------------------|------|
| 05.6 | Paper 05 | K-window / A64 handling when paths exceed `K_max=9` | CQE-08 | Paper 08 introduces the Nebe K=9 sheet bound; A64/exceedance handling is not fully closed. |

## Guard (23 items)

| ID | Source | Obligation | Closed / scoped by | Note |
|----|--------|------------|--------------------|------|
| 00.2 | Paper 00 | Keep "only addition" boundary sharp in every later paper |  | Ongoing honesty boundary, not a missing proof. |
| 01.4 | Paper 01 | Keep O8 closure scoped until broader physical transport supplied |  | O8 spinor double cover is closed in Paper 01; broader physical transport is intentionally scoped. |
| 03.2 | Paper 03 | Keep D4 tower / `G2->F4` scoped to finite reapplication receipt |  | Finite reapplication scope is intentionally maintained. |
| 05.4 | Paper 05 | Separate finite rolling-state claims from physical Oloid geometry claims |  | Finite vs physical Oloid geometry boundary is maintained. |
| 05.5 | Paper 05 | Treat Rule 30 prediction as downstream; cold unbounded extraction remains outside |  | Cold unbounded extraction is intentionally scoped to downstream papers. |
| 06.5 | Paper 06 | Keep the cold Rule 30 Problem 3 extraction boundary separate from the verified Paper 10 aggregate readout theorem | CQE-12 | Paper 12 keeps the cold Problem 3 boundary explicitly open. |
| 08.6 | Paper 08 | Keep physics identifications (`1/137`, SM, QCD, gravity) scoped as named bridges |  | Physics identifications are intentionally scoped as named bridges in all later papers. |
| 10.4 | Paper 10 | Keep cold Rule 30 Problem 3 extraction as an explicit open obligation | CQE-12 | Paper 12 keeps cold Problem 3 extraction explicitly open. |
| 12.4 | Paper 12 | Keep spectral layer scoped as non-cold-start predictor |  | Spectral layer is intentionally scoped as non-cold-start. |
| 14.3 | Paper 14 | Keep oloid normal form scoped as not an nth-bit extractor |  | Oloid normal form is intentionally scoped as not an nth-bit extractor. |
| 15.2 | Paper 15 | Keep internal substrate claim separate from measured particle mass derivation |  | Internal substrate vs measured mass boundary is maintained. |
| 16.3 | Paper 16 | Power-of-ten windows as methodology, not completed limit |  | Power-of-ten windows are intentionally scoped as samplers. |
| 20.1 | Paper 20 | Preserve `unknown` reachability as open (do not promote to solved) |  | Preserve unknown reachability is a ledger discipline. |
| 20.2 | Paper 20 | Preserve forbidden rows (do not discard) |  | Preserve forbidden rows is a ledger discipline. |
| 21.4 | Paper 21 | Keep open gaps as named failure records |  | Open gaps kept as failure records is a design rule. |
| 25.4 | Paper 25 | Keep NSL unification as a calibration-level research claim |  | NSL unification intentionally scoped as calibration-level research. |
| 27.1 | Paper 27 | Keep human latency unclaimed (anneal steps ≠ response time) |  | Human latency intentionally unclaimed. |
| 27.2 | Paper 27 | Keep shared reality as agreement on `C`, not physical simultaneity |  | Shared reality kept as C-agreement. |
| 27.3 | Paper 27 | Keep consciousness / collapse interpretive |  | Consciousness/collapse kept interpretive. |
| 27.4 | Paper 27 | Any future temporal Z4 period claim must overcome recorded counterexamples |  | Future Z4 period claims must refute existing counterexamples. |
| 30.3 | Paper 30 | Keep transport ledger open lifts visible in ribbon framing |  | Keep open lifts visible is a design rule. |
| 31.1 | Paper 31 | Preserve Paper 31 as downstream of Paper 30 |  | Preserve downstream-of-P30 status is a design rule. |
| 31.3 | Paper 31 | Do not promote retrospective readout to an upstream premise |  | Do not promote retrospective readout is a design rule. |

## Out Of Scope (7 items)

| ID | Source | Obligation | Closed / scoped by | Note |
|----|--------|------------|--------------------|------|
| 01.6 | Paper 01 | Full D4/F4/J₃(O) / Standard Model claims |  | Explicitly deferred / out of scope. |
| 02.5 | Paper 02 | Keep product false-positive claims outside until empirical receipts |  | Product-layer guard, not a theorem gap. |
| 03.6 | Paper 03 | Full D4 triality / full F4 action / off-diagonal octonionic dynamics |  | Explicitly out of scope. |
| 03.7 | Paper 03 | Product-scale cluster scheduling safety/liveness under real capacity constraints |  | Product-layer concern, out of scope. |
| 07.5 | Paper 07 | Keep CA-field dynamics and collision-rate diagnostics outside until they have their own receipts |  | Product-layer diagnostics, not a formal theorem gap. |
| 19.1 | Paper 19 | Physical observer claims (out of scope unless new receipt) |  | Physical observer claims are explicitly not made. |
| 28.2 | Paper 28 | Non-code-tower dimensions (dimension 5 rejected) |  | Dimension 5 is explicitly rejected and documented. |

## Engineering (26 items)

| ID | Source | Obligation | Closed / scoped by | Note |
|----|--------|------------|--------------------|------|
| 00.1 | Paper 00 | Wire verifier into `cqe_engine.formal` |  | Wiring Paper 00 verifier into cqe_engine.formal is tooling; no later paper does it. |
| 01.1 | Paper 01 | Wire finite verifiers into `cqe_engine.formal` |  | Wiring Paper 01 verifiers is still tooling. |
| 02.1 | Paper 02 | Wire verifier into `cqe_engine.formal` |  | Wiring Paper 02 verifier is tooling. |
| 02.6 | Paper 02 | Reconcile competing axis/sheet codings across all D-drive copies |  | Tooling cleanup across D-drive copies still needed. |
| 03.1 | Paper 03 | Wire `verify_triality_surface` into `cqe_engine.formal` |  | Wiring Paper 03 verifier is tooling. |
| 03.4 | Paper 03 | Reconcile axis naming across D drive chart-codec copies |  | Axis naming cleanup across D-drive copies still needed. |
| 04.1 | Paper 04 | Wire `verify_boundary_repair` into `cqe_engine.formal` |  | Wiring Paper 04 verifier is tooling. |
| 05.1 | Paper 05 | Wire `verify_oloid_path_carrier` into `cqe_engine.formal` |  | Wiring Paper 05 verifier is tooling. |
| 06.1 | Paper 06 | Wire `verify_causal_code` into `cqe_engine.formal` |  | Wiring Paper 06 verifier is tooling. |
| 06.4 | Paper 06 | Replace placeholder receipt ids with repository-stable artifact hashes |  | Artifact-hash tooling still pending. |
| 07.1 | Paper 07 | Wire `verify_discrete_continuous_bridge` into `cqe_engine.formal` |  | Wiring Paper 07 verifier is tooling. |
| 08.1 | Paper 08 | Wire all 12 Paper 08 verifiers into `cqe_engine.formal` |  | Wiring Paper 08 verifiers is tooling. |
| 09.1 | Paper 09 | Reconcile/fix `hamiltonian_window_emergence_receipt.json` McKay closed-band mismatch (path normalization / witness promotion) |  | **Closed** — `ROOT` normalized, McKay bands scoped to light-cone-bound witness, receipt regenerated and passes. |
| 10.1 | Paper 10 | Fix T10 receipt path normalization (`ROOT` should be repo root) and regenerate `t10_master_receipt.json` |  | **Closed** — `ROOT` normalized to repo root, Paper-00 source lookup fixed, receipt regenerated and passes. |
| 11.1 | Paper 11 | Fix T10 trust-anchor path normalization in `verify_theory_admission_gate.py` and regenerate receipt |  | **Closed** — `ROOT` normalized, T10 receipt now loads from correct path, receipt regenerated and passes. |
| 12.1 | Paper 12 | Scope or replace `verify_p3_closure.py` so it does not overclaim cold Problem 3 closure |  | P3 verifier overclaims cold closure and needs scoping/replacement. |
| 20.3 | Paper 20 | Expose aggregate ledger tooling across all 32 papers |  | Aggregate ledger tooling across 32 papers not yet wired. |
| 21.2 | Paper 21 | Expanded morphism witnesses |  | Expanded morphism witnesses are tooling/research. |
| 21.3 | Paper 21 | TF1 measurement |  | TF1 measurement tooling missing. |
| 23.3 | Paper 23 | Depth-only winding extraction |  | Depth-only winding extraction tooling missing. |
| 23.4 | Paper 23 | Biological encoding parser |  | Biological parser missing. |
| 28.3 | Paper 28 | Real game-piece geometry per piece type |  | Real piece geometry tooling missing. |
| 30.1 | Paper 30 | Package `cqe_engine.ribbon` module in production root |  | `cqe_engine.ribbon` module not packaged. |
| 32.3 | Paper 32 | Product selectors must preserve proof/open/readout status |  | Product selectors must be wired to preserve status. |
| CC.1 | Cross-cutting | Fix receipt path normalization in Papers 09-11 verifiers and regenerate failing receipts (or scope claims if failures are substantive) |  | **Closed** — all three verifiers normalized and receipts now pass. |
| CC.4 | Cross-cutting | Provide AirLock specs for Papers 06-32 (`CQECMPLX-AirLock/cqe-production-v0.1/papers/` currently has only 01-05) |  | AirLock specs for 06-32 missing. |

## Documentation (15 items)

| ID | Source | Obligation | Closed / scoped by | Note |
|----|--------|------------|--------------------|------|
| 00.3 | Paper 00 | Carry exact citation list into every later paper's burden section |  | Bibliography pass remains to be done. |
| 01.2 | Paper 01 | Update workbook language that confuses direction with value inequality |  | Workbook language cleanup pending. |
| 01.5 | Paper 01 | Peer-review bibliography pass |  | Peer-review bibliography pass pending. |
| 02.4 | Paper 02 | Add peer-review citations |  | Citations pending. |
| 04.6 | Paper 04 | Replace citation anchors with final bibliography entries |  | Bibliography entries still need insertion. |
| 05.7 | Paper 05 | Reconcile scope divergence between current formal paper and stronger claims in `CQECMPLX-Production` mirror / `UPGRADED` backup |  | Scope-divergence cleanup between canonical formal and UPGRADED backup still pending. |
| 06.7 | Paper 06 | Reconcile edge-type schema divergence: formal 8-type vs. historical 5-type |  | Edge-type schema divergence documentation still pending. |
| 07.9 | Paper 07 | Reconcile the narrower current formal paper with the broader R30 `07_universal_n3_closure.md` |  | Reconciliation with R30 umbrella paper still pending. |
| 08.7 | Paper 08 | Reconcile `CQE-paper-08_UPGRADED.md` overclaim with canonical formal paper |  | UPGRADED overclaim reconciliation still pending. |
| 08.8 | Paper 08 | Disambiguate CQE-paper-08 (Lattice Closure) from R30 Paper 08 (`π` VACUUM parameter) |  | R30 namespace disambiguation still pending. |
| 30.2 | Paper 30 | Reconcile legacy '31 beads' workbook language with `00-29` + Paper 31 readout |  | Legacy '31 beads' language reconciliation pending. |
| 32.4 | Paper 32 | Reconcile companion variants (`CQE-paper-32.md` vs `32-obs.md`) and `lib-forge/papers_output` copy |  | Companion-variant reconciliation pending. |
| CC.2 | Cross-cutting | Reconcile `CQE-paper-formal-CLAIM` taxonomy: per-paper classification must retain both IPMC and ECO labels (e.g., Papers 13 and 15) |  | Taxonomy reconciliation still needed. |
| CC.3 | Cross-cutting | Document R30 umbrella mismatch: `CMPLX-R30-main/PROOF/papers/09_*.md`–`16_*.md` are historical cross-references only |  | R30 umbrella mismatch documentation still needed. |
| CC.5 | Cross-cutting | Locate or recreate `.25/.50/.75/_UPGRADED.md` companion variants for Papers 09-32 in primary repo or document them as missing |  | Source-backup variants for 09-32 missing or undocumented. |

## Governance (1 items)

| ID | Source | Obligation | Closed / scoped by | Note |
|----|--------|------------|--------------------|------|
| 06.3 | Paper 06 | Decide which cycles are allowed as review loops vs. rejected as proof cycles |  | Cycle policy decision still pending. |

## Genuinely Open (65 items)

| ID | Source | Obligation | Closed / scoped by | Note |
|----|--------|------------|--------------------|------|
| 00.4 | Paper 00 | Document idempotent-to-one-other-thing dual relationship |  | No later unification paper has closed this dual relationship. |
| 02.7 | Paper 02 | Closed-form `mckay_thompson_coefficient_parity` for Lucas-sparse correction sum |  | No later paper closes unbounded McKay-Thompson parity (Papers 09, 16, 18 keep it open). |
| 02.9 | Paper 02 | E₆→E₇→E₈ lift beyond quaternion-sub-algebra trapping |  | No later paper closes the E6→E7→E8 dyadic lift beyond quaternion-sub-algebra. |
| 04.4 | Paper 04 | Add domain example after formal schema stable |  | No later paper adds the domain example. |
| 04.5 | Paper 04 | 8-state chart sweep for bilateral validator (P02–P06) |  | No later paper performs the 8-state chart sweep for the bilateral validator. |
| 05.3 | Paper 05 | Keep the E6→E7→E8 dyadic lift as an explicit bridge obligation |  | No later paper closes the E6→E7→E8 dyadic lift. |
| 06.2 | Paper 06 | Populate the full 32-paper causal graph from all formal receipts |  | The 32-paper causal graph has not been populated yet (skeletons now exist, but graph tooling does not). |
| 06.6 | Paper 06 | 8-state chart → tool mapping for bilateral validator (P02–P06) |  | 8-state chart → tool mapping for bilateral validator is still missing. |
| 07.2 | Paper 07 | Add a separate theorem for any claimed Hamiltonian or physical dynamics between samples |  | No later paper proves Hamiltonian/physical-dynamics theorem between samples. |
| 07.3 | Paper 07 | Preserve causal receipt links whenever interpolated traces are used |  | Causal receipt links for interpolated traces not yet enforced. |
| 07.6 | Paper 07 | Prove the general universality theorem characterizing which sequences admit a lossless F4 encoder |  | General F4 encoder universality theorem remains open. |
| 07.7 | Paper 07 | Derive the relationship between sampling rate and closure stability |  | Sampling-rate vs closure-stability analysis not done. |
| 08.2 | Paper 08 | Prove exact glue-coset representatives for nontrivial Niemeier/Leech terminals |  | Nontrivial Niemeier/Leech glue-coset representatives are not closed by Paper 17. |
| 08.3 | Paper 08 | Close rootless Leech landing |  | Paper 17 explicitly reports `leech_construction_proved = false`. |
| 08.4 | Paper 08 | Close Gamma72 polarization/landing |  | Paper 17 does not close Gamma72 landing. |
| 08.5 | Paper 08 | Build cold-start fingerprint map from arbitrary depth to Niemeier/Leech |  | No later paper builds a cold-start fingerprint map to Niemeier/Leech. |
| 09.2 | Paper 09 | Unbounded closed-form McKay-Thompson arithmetic |  | Unbounded closed-form McKay arithmetic not available. |
| 09.3 | Paper 09 | McKay-Thompson parity obligation (O2′) |  | O2′ parity remains cross-cutting (Papers 02, 16, 18 also carry it). |
| 09.4 | Paper 09 | Direct VOA route to threshold promotion |  | Direct VOA route remains CONJ. |
| 10.3 | Paper 10 | Demonstrate or scope the `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` transport row |  | Paper 17 does not close the exceptional→Niemeier landing row. |
| 11.3 | Paper 11 | Pariah / Happy-Family encoding-invariance of the boundary |  | Pariah/Happy-Family encoding-invariance not closed by Paper 29. |
| 12.2 | Paper 12 | Infinite non-periodicity proof or explicit horizon status |  | Infinite non-periodicity remains unproven. |
| 12.3 | Paper 12 | EntropyForge extension obligations |  | EntropyForge extension obligations remain. |
| 13.1 | Paper 13 | Exact numeric CKM calibration (`ckm_calibration_receipt.json`) |  | No numeric CKM calibration receipt exists. |
| 13.2 | Paper 13 | Physical quark / color-charge measurement bridge |  | Physical quark/color-charge measurement bridge is external. |
| 13.3 | Paper 13 | Unconditional cold-start G2/F4/T5A route |  | Paper 13 itself keeps the G2/F4/T5A route bounded. |
| 14.1 | Paper 14 | Physical GR curvature measurement bridge |  | Physical GR curvature measurement bridge is external. |
| 14.2 | Paper 14 | Derivation of Einstein field equations from repair-score accounting |  | No derivation of Einstein field equations from repair scores. |
| 15.1 | Paper 15 | Physical Higgs / QFT mass calibration |  | No physical Higgs/QFT mass calibration. |
| 16.1 | Paper 16 | Global continuum limit |  | Global continuum limit is not closed. |
| 16.2 | Paper 16 | Collapse of propagating correction sum from O(N) to O(log N) (McKay-Thompson parity O2′) |  | Correction-sum collapse to O(log N) / O2′ not closed. |
| 17.1 | Paper 17 | Completed Leech lattice construction |  | Paper 17 reports `leech_construction_proved = false`. |
| 17.2 | Paper 17 | Weyl-extractor construction |  | No Weyl-extractor construction receipt. |
| 18.1 | Paper 18 | Full Moonshine identification |  | Full Moonshine identification remains open. |
| 18.2 | Paper 18 | McKay-Thompson fingerprint O2′ |  | O2′ parity remains cross-cutting. |
| 18.3 | Paper 18 | `correction_via_voa` route completion |  | `correction_via_voa` route not completed. |
| 19.2 | Paper 19 | SPINOR observation model |  | SPINOR observation model not built. |
| 19.3 | Paper 19 | Open-gap observer evidence |  | Open-gap observer evidence not provided. |
| 21.1 | Paper 21 | Missing Leech import |  | Paper 17 does not provide a completed Leech construction to import. |
| 22.1 | Paper 22 | Finite-element validation |  | FE validation is external. |
| 22.2 | Paper 22 | Fabrication and load testing |  | Fabrication/load testing is external. |
| 22.3 | Paper 22 | Manufacturability constraints |  | Manufacturability constraints are external. |
| 22.4 | Paper 22 | Relative-density and Poisson-ratio measurement |  | Relative-density/Poisson-ratio measurement is external. |
| 23.1 | Paper 23 | PDB validation |  | PDB validation external. |
| 23.2 | Paper 23 | Native structure prediction |  | Native structure prediction external. |
| 23.5 | Paper 23 | Fold-rate and thermodynamic validation |  | Fold-rate/thermodynamic validation external. |
| 24.1 | Paper 24 | OEIS identity |  | OEIS identity not verified. |
| 24.2 | Paper 24 | N-dimensional playability |  | N-dimensional playability not closed. |
| 24.3 | Paper 24 | Placement-class relation to `2+6` sector split |  | Placement-class to 2+6 sector split beyond local chart not closed. |
| 24.4 | Paper 24 | Combinatorial-game expert review |  | Combinatorial-game expert review pending. |
| 25.1 | Paper 25 | Physical unit calibration (joules conversion) |  | Joules conversion external. |
| 25.2 | Paper 25 | Absorption measurement |  | Absorption measurement external. |
| 25.3 | Paper 25 | Calibrated variational principle for least-action/geodesic/thermo readings |  | Calibrated variational principle not built. |
| 26.1 | Paper 26 | Measured Z-pinch witness |  | Measured Z-pinch witness external. |
| 26.2 | Paper 26 | Controlled plasma observable connected to carrier shear bit |  | Plasma-to-shear-bit observable external. |
| 26.3 | Paper 26 | Friction and generation mechanisms |  | Friction/generation mechanisms external. |
| 26.4 | Paper 26 | Physical collapse calibration |  | Physical collapse calibration external. |
| 28.1 | Paper 28 | General N-dimensional game solver |  | General N-dimensional solver not claimed. |
| 28.4 | Paper 28 | Complete game theory (strategy, termination, winning, fairness) |  | Complete game theory not claimed. |
| 28.5 | Paper 28 | OEIS identity |  | OEIS identity pending. |
| 29.1 | Paper 29 | Physical energy-bound witness function (units bridge) |  | Physical energy-bound witness function external. |
| 29.2 | Paper 29 | Pariah/Happy-Family encoding-invariance of the boundary |  | Pariah/Happy-Family encoding-invariance not closed. |
| 32.1 | Paper 32 | Minimality for `n ≥ 6` without independent exclusion proofs |  | Minimality for n≥6 not claimed. |
| 32.2 | Paper 32 | `n=8` corridor below `46205` |  | n=8 corridor below 46205 not claimed. |
| CC.6 | Cross-cutting | Close or carry global obligations: McKay-Thompson parity O2′, W(E8) lookup table O1, full Moonshine identification, physical-unit/energy bridges |  | Global O2′/O1/Moonshine/energy bridges remain open across papers. |

## Summary

- **Closed by another paper:** 9
- **Partially closed / advanced:** 7 (6 partially closed + 1 advanced)
- **Guards / out-of-scope:** 30
- **Tooling / documentation / governance debt:** 38 (four engineering items closed by path-normalization fix)
- **Genuinely open research obligations:** 65
- **Total non-trivial remaining work (engineering + docs + genuine open):** 103

## Highest-priority genuinely open research items

- **02.7** (Paper 02): Closed-form `mckay_thompson_coefficient_parity` for Lucas-sparse correction sum
- **02.9** (Paper 02): E₆→E₇→E₈ lift beyond quaternion-sub-algebra trapping
- **05.3** (Paper 05): Keep the E6→E7→E8 dyadic lift as an explicit bridge obligation
- **07.6** (Paper 07): Prove the general universality theorem characterizing which sequences admit a lossless F4 encoder
- **08.2** (Paper 08): Prove exact glue-coset representatives for nontrivial Niemeier/Leech terminals
- **08.3** (Paper 08): Close rootless Leech landing
- **08.4** (Paper 08): Close Gamma72 polarization/landing
- **08.5** (Paper 08): Build cold-start fingerprint map from arbitrary depth to Niemeier/Leech
- **09.2** (Paper 09): Unbounded closed-form McKay-Thompson arithmetic
- **09.3** (Paper 09): McKay-Thompson parity obligation (O2′)
- **10.3** (Paper 10): Demonstrate or scope the `EXCEPTIONAL_ROUTE_TO_NIEMEIER_LANDING_FORMS` transport row
- **12.2** (Paper 12): Infinite non-periodicity proof or explicit horizon status
- **13.1** (Paper 13): Exact numeric CKM calibration (`ckm_calibration_receipt.json`)
- **13.3** (Paper 13): Unconditional cold-start G2/F4/T5A route
- **14.2** (Paper 14): Derivation of Einstein field equations from repair-score accounting
- **15.1** (Paper 15): Physical Higgs / QFT mass calibration
- **16.1** (Paper 16): Global continuum limit
- **16.2** (Paper 16): Collapse of propagating correction sum from O(N) to O(log N) (McKay-Thompson parity O2′)
- **17.1** (Paper 17): Completed Leech lattice construction
- **17.3** (Paper 17): Full W(E8) lookup table O1 (construction closed by Paper 08; full materialization open)
- **18.1** (Paper 18): Full Moonshine identification
- **18.3** (Paper 18): `correction_via_voa` route completion
- **21.1** (Paper 21): Missing Leech import
- **29.1** (Paper 29): Physical energy-bound witness function (units bridge)

---

## Update: Rule 30 evidence / 2026-06-26

- Fixed `C3_logistic_conjugate_rule90_21steps` in both:
  - `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-12/verify_glm_rule30_idempotent_connections.py`
  - `_downloads_review/glm/cqecmplx_new/production/prize-submissions/wolfram-rule30/verify_rule30_idempotent_connections.py`
  - Correction: conjugacy is `h(x) = (2/π)·asin(√x)` mapping the logistic orbit to the tent orbit, with inverse `h⁻¹(y) = sin²(πy/2)`. Both verifiers now pass.
- Content-addressed the local 1 Mbit Wolfram Rule 30 center-column reference:
  - Binary: `D:\CQE_CMPLX\_downloads_review\rule30_center_1m.bin` (125 KB)
  - Manifest: `D:\CQE_CMPLX\_downloads_review\rule30_center_1m_manifest.json`
  - Top SHA-256: `4bf71a265b7a3b9847703f274c736c552825a859fd2251d8bfad75b1fe05b3e9`
  - Anchored in the CAM crystal as `RULE30-1MBIT-REFERENCE` (honesty tag `external_calibration_open`).
- Created a named placeholder for the Wolfram 1 Gbit resource:
  - Manifest: `D:\CQE_CMPLX\_downloads_review\rule30_center_1g_resource_manifest.json`
  - Wolfram export helper: `D:\CQE_CMPLX\_downloads_review\export_rule30_1g.wl`
  - The actual 125 MB ByteArray is behind Wolfram Cloud authentication; the export helper can retrieve it from a Wolfram session.
- Obligation status:
  - **12.1** remains **engineering / scoped** — the P3 cold-start bit-exact verifier must not overclaim; the 1 Mbit reference is finite evidence only.
  - **12.2** advanced to **partially closed / finite-evidence** — the 1 Mbit (and pending 1 Gbit) center-column data supply an explicit horizon status, but they do not prove infinite non-periodicity.
