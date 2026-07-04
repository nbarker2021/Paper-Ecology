# TarPit Lift Tower Pass

Created: 2026-06-28T21:16:20.961034+00:00

## Claim

All FLCR lifts were fed through the full 2x2x2 LCR enumeration, decomposed into Rule-30/VOA/residue terms, run through TarPit, and recomposed into paper, slot-family, and decade towers.

## Counts

| Item | Count |
|---|---:|
| papers | 40 |
| states_per_paper | 8 |
| enumeration_rows | 320 |
| paper_towers | 40 |
| slot_family_towers | 10 |
| decade_towers | 4 |

## Global Summary

| Metric | Value |
|---|---:|
| rows | 320 |
| successes | 320 |
| success_rate | 1.0 |
| avg_final_mass | 0.509744047836896 |
| min_final_mass | 0.4897345447567536 |
| max_final_mass | 0.5683448089277536 |
| mass_sum | 163.11809530780678 |
| voa_mass_sum | 1200 |
| correction_fires | 80 |
| obstruction_fires | 80 |
| digital_roots | 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| total_output_walls | 320 |
| total_error_walls | 0 |
| total_bonds | 1430 |
| total_triads | 2860 |

## Slot-Family Towers

| Family | Papers | Avg TarPit Mass | VOA Mass Sum | Correction Fires | Error Walls |
|---|---|---:|---:|---:|---:|
| family-01 | FLCR-01, FLCR-11, FLCR-21, FLCR-31 | 0.509490 | 120 | 8 | 0 |
| family-02 | FLCR-02, FLCR-12, FLCR-22, FLCR-32 | 0.511700 | 120 | 8 | 0 |
| family-03 | FLCR-03, FLCR-13, FLCR-23, FLCR-33 | 0.510664 | 120 | 8 | 0 |
| family-04 | FLCR-04, FLCR-14, FLCR-24, FLCR-34 | 0.508927 | 120 | 8 | 0 |
| family-05 | FLCR-05, FLCR-15, FLCR-25, FLCR-35 | 0.514757 | 120 | 8 | 0 |
| family-06 | FLCR-06, FLCR-16, FLCR-26, FLCR-36 | 0.506672 | 120 | 8 | 0 |
| family-07 | FLCR-07, FLCR-17, FLCR-27, FLCR-37 | 0.507568 | 120 | 8 | 0 |
| family-08 | FLCR-08, FLCR-18, FLCR-28, FLCR-38 | 0.510781 | 120 | 8 | 0 |
| family-09 | FLCR-09, FLCR-19, FLCR-29, FLCR-39 | 0.505916 | 120 | 8 | 0 |
| family-10 | FLCR-10, FLCR-20, FLCR-30, FLCR-40 | 0.510965 | 120 | 8 | 0 |

## Decade Towers

| Decade | Papers | Avg TarPit Mass | Mass Sum | Digital Roots |
|---|---|---:|---:|---|
| decade-1 | FLCR-01, FLCR-02, FLCR-03, FLCR-04, FLCR-05, FLCR-06, FLCR-07, FLCR-08, FLCR-09, FLCR-10 | 0.510370 | 40.829567 | 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| decade-2 | FLCR-11, FLCR-12, FLCR-13, FLCR-14, FLCR-15, FLCR-16, FLCR-17, FLCR-18, FLCR-19, FLCR-20 | 0.510236 | 40.818854 | 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| decade-3 | FLCR-21, FLCR-22, FLCR-23, FLCR-24, FLCR-25, FLCR-26, FLCR-27, FLCR-28, FLCR-29, FLCR-30 | 0.509294 | 40.743500 | 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| decade-4 | FLCR-31, FLCR-32, FLCR-33, FLCR-34, FLCR-35, FLCR-36, FLCR-37, FLCR-38, FLCR-39, FLCR-40 | 0.509077 | 40.726174 | 1, 2, 3, 4, 5, 6, 7, 8, 9 |

## Adapter Consequence

Use the tower rows as the input queue for tarpit_kappa_physical_adapter: paper tower mass + slot-family mass + decade mass + sector tag -> unitful physical readout and residual ledger.

The first enumeration is now fully decomposed for every FLCR lift. The recomposed tower rows are the working queue for the next physical adapter pass.
