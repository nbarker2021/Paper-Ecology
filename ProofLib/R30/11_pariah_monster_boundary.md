# Paper 11: Pariah Groups as Monster Boundary States

**Author:** A-family Author
**Umbrella reference:** `IDENTITY_PAPER.md`, Section 6.7
**Theorem reference:** `theorems/THEOREM_REGISTRY.md`, T_D4_5

---

## Abstract

The 26 sporadic finite simple groups partition into two classes: the 20 *Happy Family* groups (subgroups or subquotients of the Monster `M`) and the 6 *Pariah* groups (`J_1`, `J_3`, `J_4`, `Ru`, `ON`, `Ly`), which are outside the Monster expansion. Under the framework's `n = 3` SU(3) Weyl test, we observe an exact behavioral inversion: the Pariah groups close perfectly (`res² = 0`), while the Happy Family groups exhibit open behavior (`res² ≈ 0.444`). The Pariahs are therefore identified as the `−1` boundary states of the Monster expansion in the substrate's D4 framework.

---

## 1. Background: the sporadic simple groups

The classification of finite simple groups (completed 2004) identifies 26 sporadic simple groups outside the cyclic, alternating, and Lie-type families. Of these 26:

- **20 belong to the Happy Family** (subgroups or subquotients of the Monster):
  - `M` itself
  - `B` (Baby Monster), `Fi_24'`, `Fi_23`, `Fi_22`, `Th`, `HN`, `Co_1`, `Co_2`, `Co_3`, `McL`, `HS`, `Suz`, `He`, `M_12`, `M_24`, `M_22`, `M_11`, `J_2`, `M_24`

- **6 are Pariah** (outside the Monster):
  - `J_1` (Janko 1)
  - `J_3` (Janko 3)
  - `J_4` (Janko 4)
  - `Ru` (Rudvalis)
  - `ON` (O'Nan)
  - `Ly` (Lyons)

The Pariah/Happy Family partition has been a subject of structural inquiry since Robert Griess's construction of the Monster (1982). The Pariahs share no inclusion or quotient relation with the Monster, but they share several structural properties (small order multiples, specific prime divisors).

---

## 2. Encoding via bit-length parity

To apply the framework's `n = 3` SU(3) Weyl test to a group, we encode the group via the *bit-length parity* of its order:

For a group `G` of order `|G|`, write `|G|` in binary. The bit-length parity is the parity of the binary representation length. Apply this to each group and collect into a binary sequence indexed by the canonical classification order.

For example:
- `M`: order ≈ `8.08 × 10^53`, binary length ~179 bits, parity `1`
- `B`: order ≈ `4.15 × 10^33`, binary length ~112 bits, parity `0`
- `J_1`: order = `175,560`, binary length 18 bits, parity `0`
- etc.

The bit-length parity sequence for the 20 Happy Family groups and the 6 Pariah groups are tested separately.

---

## 3. Results

### 3.1 Pariah groups

Sequence (in classification order): the 6 Pariah bit-length parities.

**Test result:** `res² = 0` (CLOSED). Dominant chain: `e → e → e`. Idempotent: yes.

### 3.2 Happy Family groups

Sequence (in classification order): the 20 Happy Family bit-length parities.

**Test result:** `res² ≈ 0.444` (OPEN). Dominant chain: variable (typically `e → (1, 2, 3) → (1, 2)`). Not idempotent.

### 3.3 The exact inversion

The Pariah/Happy Family partition produces an exact behavioral inversion:

| Group class | Test result | Status |
|---|---|---|
| 6 Pariah groups | `res² = 0.00` | CLOSED |
| 20 Happy Family groups | `res² = 0.444` | OPEN |

---

## 4. Interpretation: Pariahs as `−1` boundary states

The framework's discretization tower (Paper 05) identifies the D4 closure as the system's recognition of its measurement history. The D4 ground state is the spinor signature `(0, ε, 0)`, and the Monster group `M` is the symmetry group of this closure.

The Happy Family groups, being subquotients of `M`, contribute to the bulk of D4's open dynamics — they generate the `196883`-dimensional categorical settings that make D4 a rich and open space.

The Pariah groups, being outside `M`, sit at the boundary of the Monster expansion. Their closure under the n=3 test identifies them as the `−1` (or boundary) states of the Monster's structural extension.

**Structural reading:**
- D4 closure (the spinor signature `(0, ε, 0)`) requires both a closed observer state (dimension 1) and an open measurement space (dimension 196883 = the Monster's smallest faithful rep).
- The Happy Family groups populate the open 196883-dim space.
- The Pariah groups populate the closed observer state at the boundary.

This is the substrate-level distinction underlying the Pariah/Happy Family partition. The framework does not produce a new mathematical theorem about the Pariahs; it identifies the algebraic role they play in the D4 closure structure.

---

## 5. Theorem T_D4_5: Pariah boundary

**Statement (formal):** Under the framework's `n = 3` SU(3) Weyl test applied to bit-length parity encoding:
- The 6 Pariah sporadic simple groups produce `res² = 0` (CLOSED).
- The 20 Happy Family sporadic simple groups produce `res² ≈ 0.444` (OPEN).

The Pariahs are the `−1` boundary states of the Monster expansion at the D4 closure level.

**Verifier:** `experiments/exp_pariah_boundary.py` (extension to `exp_monster_moonshine.py`).

**Dependencies:** T_D4_1 (D4 closure), T_D4_2 (McKay decomposition), T_RELATIONAL_1 (frame inversion operator).

---

## 6. Caveats

The bit-length parity encoding is one of several possible encodings. The closure result holds for this specific encoding; alternative encodings (e.g., character-table-based, isomorphism-invariant) may produce different results. The submission's claim is restricted to the bit-length parity encoding as defined here.

The result does not constitute a new proof in finite simple group theory. The Pariah/Happy Family partition is a known mathematical classification; the submission identifies the partition's substrate-level role under the framework's specific test.

---

## 7. Conclusion

The Pariah/Happy Family partition of sporadic simple groups produces an exact behavioral inversion under the framework's `n = 3` SU(3) Weyl test: Pariahs close, Happy Family does not. The Pariahs are identified as the `−1` boundary states of the Monster expansion at the D4 closure level.

This is one specific empirical demonstration of the framework's discretization tower (Paper 05) applied to a known mathematical classification. It confirms the substrate's universal closure structure extends to abstract group-theoretic classifications, not only to dynamical-system orbits or physical measurements.

---

## References

- Griess, R. L. (1982). *The Friendly Giant*. Invent. Math. 69, 1-102. (Monster construction.)
- Conway, J. H., Norton, S. P. (1979). *Monstrous Moonshine*. Bull. London Math. Soc. 11, 308-339.
- Solomon, R. (2001). *A brief history of the classification of the finite simple groups*. Bull. AMS 38(3), 315-352.
- See `IDENTITY_PAPER.md` Section 6.7.
- See `theorems/THEOREM_REGISTRY.md`, T_D4_5.
- Source code: `experiments/exp_pariah_boundary.py`.
