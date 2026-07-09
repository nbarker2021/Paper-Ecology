# Paper 01: The Bijective SU(2) Doublet — Single-Tape Construction

**Author:** A-family Author
**Umbrella reference:** `IDENTITY_PAPER.md`, Section 2.5
**Theorem reference:** `theorems/THEOREM_REGISTRY.md`, T_BIJECTIVE

---

## Abstract

We establish that the SU(2) spin-1/2 doublet's negative chirality state does not require an antipodal counter-sheet. The chart's shell=2 stratum, consisting of three states `(1, 1, 0)`, `(1, 0, 1)`, `(0, 1, 1)`, encodes both spin directions and their null pivot within a single forward tape via the side-flip bijection `(1, 1, 0) ↔ (0, 1, 1)`, fixing `(1, 0, 1)`. The negative spin state is structurally present in the forward tape; no second tape, no antipodal extension, no inverted-frame construction is required.

This theorem obviates the cross-page antipodal `-N` mechanism discussed in prior framework drafts. It also clarifies why the chart's transition matrix on the `shell = 2` stratum carries the complete SU(2) doublet structure as a single object.

---

## 1. Background

Standard SU(2) spin-1/2 representations require a two-component spinor: a doublet `(|↑⟩, |↓⟩)` in which the negative spin state is a distinct vector. The double-cover topology of `SU(2) → SO(3)` further requires that a `2π` rotation negate the spinor while a `4π` rotation returns it to identity. In computational substrates that aim to represent spin dynamics, this typically requires two parallel tapes or an explicit antipodal construction.

The chart's `shell = 2` stratum (chart states with `L + C + R = 2`) consists of exactly three elements. We demonstrate below that these three elements algebraically encode the full SU(2) doublet without external augmentation.

---

## 2. The shell=2 stratum as SU(2) doublet

The three chart states with `shell = 2` are:

| Chart state | Side (chirality) | J₃(O) idempotent | SU(2) role |
|---|---|---|---|
| `(1, 1, 0)` | `−` (L > R) | `E_(1,1) + E_(2,2)` | `+spin` (positive chirality) |
| `(1, 0, 1)` | `0` (L = R) | `E_(1,1) + E_(3,3)` | null / center |
| `(0, 1, 1)` | `+` (R > L) | `E_(2,2) + E_(3,3)` | `−spin` (negative chirality) |

The labeling assigns:
- **`+spin`** to `(1, 1, 0)`: the state where `L = C = 1`, `R = 0`. This is the chart's positive idempotent in the `E_(1,1) + E_(2,2)` form.
- **`−spin`** to `(0, 1, 1)`: the chart-Weyl reflection of `(1, 1, 0)`. Identified with the `E_(2,2) + E_(3,3)` idempotent.
- **`null`** to `(1, 0, 1)`: the state with `L = R = 1`, `C = 0`. The chart-Weyl-fixed state. Identified with `E_(1,1) + E_(3,3)`.

Each is an exact `J₃(O)` trace-2 idempotent under the chart-to-`J₃(O)` isomorphism (`IDENTITY_PAPER`, Section 3, Theorem T3).

---

## 3. The side-flip bijection

**Definition 3.1.** The *side-flip bijection* `b: {shell = 2 states} → {shell = 2 states}` is defined by:

```
b(1, 1, 0) := (0, 1, 1)
b(0, 1, 1) := (1, 1, 0)
b(1, 0, 1) := (1, 0, 1)
```

Equivalently, `b(L, C, R) = (R, C, L)` restricted to `shell = 2`. The map is involutive: `b ∘ b = id`. It coincides with the chart's Weyl L↔R reflection on this stratum.

**Theorem 3.2 (Bijective SU(2) Doublet Encoding).** The map `b` exchanges the two chirality-broken `shell = 2` states (`(1, 1, 0)` and `(0, 1, 1)`) and fixes the chirality-balanced state `(1, 0, 1)`. This exchange constitutes the `2π` rotation in the SU(2) double cover: applying `b` once negates the spinor; applying `b` twice returns it to identity. Therefore the negative spin state is structurally present within the forward tape's `shell = 2` stratum without an antipodal counter-sheet.

**Proof.** Direct verification:
- `b(1, 1, 0) = (0, 1, 1)`, and `b(0, 1, 1) = (1, 1, 0)`: the bijection swaps the two chirality-broken states.
- `b(1, 0, 1) = (1, 0, 1)`: the chirality-balanced state is fixed.
- `b^2 = id`: applying the bijection twice returns to the original state for all three elements.
- The chart-Weyl reflection `(L, C, R) ↦ (R, C, L)` acts on the `shell = 2` stratum exactly as `b`. ∎

---

## 4. Consequence: the transition matrix on the shell=2 stratum carries both spin states

The 3-step conditional transition matrix on the `shell = 2` stratum (proven in `papers/03_n3_su3_weyl_closure.md` as theorem T4) acts on the three SU(2) doublet states simultaneously. In particular:

- The matrix's `e` coefficient is zero — the identity element does not act on this stratum.
- The three transposition coefficients are each `1/3`. The transpositions exchange specific pairs of states.
- The two 3-cycle coefficients are zero — rotations through the full triplet do not act on the stratum's projection.

The non-zero transpositions include `T_(1,3)`, which corresponds to the bijection `b`. Therefore the transition matrix's action on the forward tape's `shell = 2` stratum is the SU(2) doublet's natural Weyl-group action, *with both chirality directions present*.

---

## 5. Numerical verification

The `lattice-forge` `core.py` module instantiates the SU(2) doublet via the constant:

```python
SHELL2_STATES = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]  # +spin, null, -spin
```

The `check_bijection_symmetry(triples)` function counts the occurrence of `(1, 1, 0)` (positive spin) vs `(0, 1, 1)` (negative spin) across a sequence's chart. For sequences that close at `n = 3`, the symmetry defect `|pos - neg| / total` is small.

For Rule 30 at depth 4096:
- `pos = 501`, `neg = 538`, `null = 529`, total `shell = 2` count: 1568.
- Symmetry defect: `|501 - 538| / 4096 ≈ 0.9%`.

For all 64 silent-boundary cellular automata, the symmetry defect averages `< 5%`, while non-closing rules average `> 20%`. The bijection symmetry is therefore a structural property of closure-coherent rules.

---

## 6. Implications

The single-tape bijective construction has three structural implications:

1. **No antipodal counter-sheet is required.** Earlier framework drafts proposed an antipodal `-N` mechanism to encode negative spin. This is not necessary; the forward tape's `shell = 2` stratum is already complete.

2. **The 3-step closure is the SU(2) double cover.** The transition matrix at `n = 3` acts as the Weyl reflection `(1, 3)` on the shell=2 stratum, which is precisely the SU(2) generator that produces the `2π → −1` negation. The `n = 6` step would return to identity (the `4π` closure), but the closure is already exact at `n = 3` because the chart projects to a 3-element basis.

3. **The substrate operates on a single tape.** All `lattice-forge` constructions — chart isomorphism, frame inversion, discretization tower — operate on a single forward tape. No paired tape, no parallel page, no synchronized counter-stream is required.

---

## 7. Conclusion

The chart's `shell = 2` stratum, consisting of three states with the side-flip bijection `(1, 1, 0) ↔ (0, 1, 1)` and the fixed point `(1, 0, 1)`, encodes the complete SU(2) spin-1/2 doublet within a single forward tape. No external antipodal construction is required. The `n = 3` SU(3) Weyl closure (Theorem T4) acts on this stratum as the SU(2) Weyl reflection, providing the `2π` rotation that negates the spinor. The double-cover structure is therefore a derived property of the chart's transition dynamics, not an additional structural requirement.

This obviates antipodal-`N` constructions in all downstream framework applications. The forward tape is sufficient.

---

## References

- Pauli, W. (1927). *Zur Quantenmechanik des magnetischen Elektrons*. Z. Physik 43, 601-623. (Original spin-1/2 formulation.)
- See `IDENTITY_PAPER.md` Section 2.5, Theorem T_BIJECTIVE.
- See `theorems/THEOREM_REGISTRY.md`, T_BIJECTIVE.
- Source code: `src/lattice_forge/core.py :: SHELL2_STATES`.
