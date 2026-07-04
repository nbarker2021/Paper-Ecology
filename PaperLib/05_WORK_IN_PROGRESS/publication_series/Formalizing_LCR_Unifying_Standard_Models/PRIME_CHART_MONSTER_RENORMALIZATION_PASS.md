# Prime-Chart Monster Renormalization Pass

Created: 2026-06-28T21:45:37.412171+00:00

## Result

The 29,30,31 -> 31,33,37 lift is a usable LCR prime-mask transition: both charts preserve prime/composite/prime and the Rule-30 parity output. Upward traversal should therefore keep two accounts: a Happy-family Monster-admitted supersingular account and a Pariah/asymmetry bridge account. At 47,59,71 the Monster renormalizes the admitted side into 196883 and leaves off-chain bridge residues as a separate LCR asymmetry body.

## Chart Trace

| Chart | Account | L | C | R | Prime Mask | Parity | Rule30 Prime | Rule30 Parity | Off-Chain | TarPit Mass |
|---|---|---:|---:|---:|---|---|---:|---:|---|---:|
| seed_29_30_31 | seed | 29 | 30 | 31 | 101 | 101 | 0 | 0 | 30 | 0.504896 |
| encoded_31_33_37 | pariah_asymmetry | 31 | 33 | 37 | 101 | 111 | 0 | 0 | 33, 37 | 0.515418 |
| bridge_37_39_41 | pariah_asymmetry | 37 | 39 | 41 | 101 | 111 | 0 | 0 | 37, 39 | 0.521583 |
| bridge_41_44_47 | pariah_asymmetry | 41 | 44 | 47 | 101 | 101 | 0 | 0 | 44 | 0.499872 |
| bridge_47_53_59 | pariah_asymmetry | 47 | 53 | 59 | 111 | 111 | 0 | 0 | 53 | 0.506773 |
| bridge_59_65_71 | pariah_asymmetry | 59 | 65 | 71 | 101 | 111 | 0 | 0 | 65 | 0.506814 |
| happy_29_31_41 | happy_family | 29 | 31 | 41 | 111 | 111 | 0 | 0 |  | 0.511471 |
| happy_31_41_47 | happy_family | 31 | 41 | 47 | 111 | 111 | 0 | 0 |  | 0.510313 |
| happy_41_47_59 | happy_family | 41 | 47 | 59 | 111 | 111 | 0 | 0 |  | 0.507879 |
| happy_47_59_71 | happy_family | 47 | 59 | 71 | 111 | 111 | 0 | 0 |  | 0.514710 |

## Account Summary

| Account | Charts | Rule30 Parity Outputs | Prime-Mask Outputs | Off-Chain Values | Avg TarPit Mass | Pair Bonds | Triads |
|---|---:|---|---|---|---:|---:|---:|
| happy_family | 4 | 0 | 0 |  | 0.511093 | 12 | 12 |
| pariah_asymmetry | 5 | 0 | 0 | 33, 37, 39, 44, 53, 65 | 0.510092 | 15 | 15 |
| seed | 1 | 0 | 0 | 30 | 0.504896 | 3 | 3 |

## Monster Renormalization

| Field | Value |
|---|---|
| Top Monster triple | [47, 59, 71] |
| Top product | 196883 |
| McKay row | 196884 |
| Next prime after ceiling | 73 |
| Pariah/asymmetry values | [33, 37, 39, 44, 53, 65] |

At the 47,59,71 ceiling, the Happy-family account keeps the Monster-admitted supersingular product 196883 and McKay row 196884. The Pariah/asymmetry account keeps off-chain bridge centers and primes as boundary residues instead of forcing them into the Monster product.

## Claim Lanes

| ID | Lane | Claim | Result |
|---|---|---|---|
| PCM-01 | `normal_form_result` | The seed 29,30,31 and encoded 31,33,37 charts preserve the prime/composite/prime LCR mask. | prime-mask LCR = 1,0,1 for both charts |
| PCM-02 | `receipt_bound_internal_result` | The prime-mask and parity charts can be run through the same Rule-30 bit/correction readout. | seed and encoded charts both produce Rule-30 parity output 0 and no correction fire |
| PCM-03 | `CAM_crystal_reapplication_result` | Upward prime charts should be carried as two ledgers rather than collapsed into one interpretation. | Happy-family ledger for Monster-admitted primes; Pariah/asymmetry ledger for off-chain bridge residues |
| PCM-04 | `standard_theorem_or_code_bound_result` | The Monster ceiling row remains 47*59*71=196883 and 196884=1+196883. | 196883 and 196884 |
| PCM-05 | `grand_synthesis_claim_with_dependencies` | The Monster acts as a renormalization boundary distributing admitted structure and asymmetry residues into two accounts. | At the 47,59,71 ceiling, the Happy-family account keeps the Monster-admitted supersingular product 196883 and McKay row 196884. The Pariah/asymmetry account keeps off-chain bridge centers and primes as boundary residues instead of forcing them into the Monster product. |
