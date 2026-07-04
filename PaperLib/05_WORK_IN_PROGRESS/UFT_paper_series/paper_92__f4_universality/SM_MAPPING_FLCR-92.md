# SM Mapping File for FLCR-92: F4 ⊃ SU(3)×SU(3) ⊃ SU(3)×SU(2)×U(1)

## The Embedding Chain

The Standard Model gauge group SU(3)_C × SU(2)_L × U(1)_Y embeds in F4 via the chain:

```
F4 ⊃ SU(3)×SU(3) ⊃ SU(3)×SU(2)×U(1)
```

- **F4**: The exceptional Lie group of dimension 52, rank 4.
- **SU(3)×SU(3)**: Maximal subgroup of F4 (dimension 16, rank 4). The first SU(3) is identified with SU(3)_C (color).
- **SU(3)×SU(2)×U(1)**: Obtained by breaking the second SU(3) to SU(2)_L × U(1)_Y (electroweak).

## Adjoint Representation Branching

Under F4 ⊃ SU(3)×SU(3):

```
52 = (8, 1) + (1, 8) + (3, 3) + (3̄, 3̄) + (3, 3̄) + (3̄, 3)
```

- (8,1): SU(3)_C gluons (8 generators)
- (1,8): SU(3)_EW gauge bosons (8 generators, before breaking)
- (3,3), (3̄,3̄), (3,3̄), (3̄,3): Off-diagonal generators connecting the two SU(3) factors (36 generators)

Under SU(3)×SU(3) ⊃ SU(3)×SU(2)×U(1):

```
52 = (8, 1)_0           # SU(3)_C gluons
     + (1, 3)_0         # SU(2)_L gauge bosons (W±, W3)
     + (1, 2)_{+1/2}    # SU(2)_L doublet (before breaking)
     + (1, 2)_{-1/2}    # SU(2)_L doublet (before breaking)
     + (1, 1)_0         # U(1)_Y gauge boson
     + (3, 2)_{+1/2}    # Leptoquark-like bosons (color-triplet, weak-doublet)
     + (3, 1)_{-1}      # Color-triplet, weak-singlet
     + (3̄, 2)_{-1/2}    # Anti-leptoquark-like bosons
     + (3̄, 1)_{+1}      # Anti-color-triplet, weak-singlet
     + (3, 2)_{-1/2}    # (conjugate of above)
     + (3, 1)_{+1}      # (conjugate of above)
     + (3̄, 2)_{+1/2}    # (conjugate of above)
     + (3̄, 1)_{-1}      # (conjugate of above)
```

## F4 Maximal Subgroups (Complete List)

| Subgroup | Dimension | Rank | Dynkin Diagram | How to Obtain |
|----------|-----------|------|----------------|---------------|
| Spin(9) = SO(9) | 36 | 4 | B4 | Remove α4 from extended F4 |
| Sp(3) × SU(2) | 24 | 4 | C3 × A1 | Remove α1 from extended F4 |
| SU(3) × SU(3) | 16 | 4 | A2 × A2 | Remove α2 from extended F4 |

## Key Identities

- F4 is the unique exceptional Lie algebra that is a subalgebra of all other exceptional algebras (E6, E7, E8).
- F4 = Aut(J3(O)) — the automorphism group of the exceptional Jordan algebra.
- The F4 root system has 48 roots: 24 long (norm 2) and 24 short (norm 1).
- Weyl group order: |W(F4)| = 1152 = 2^7 × 3^2.

## Data vs Interpretation

- **(D)**: The F4 root system, maximal subgroups, and branching rules are standard Lie algebra theory (Dynkin 1952, Adams 1996, Bourbaki 1968).
- **(I)**: The identification of the first SU(3) with SU(3)_C and the second SU(3) with the electroweak sector is the author's structural framing.
- **(I)**: The claim that F4 is the "minimal exceptional group containing the SM" is a structural framing (E6 also contains the SM, but F4 is smaller).

## References

- Adams, J. F. (1996). *Lectures on Exceptional Lie Groups.* University of Chicago Press.
- Bourbaki, N. (1968). *Groupes et Algèbres de Lie, Chapitres 4–6.* Hermann.
- Dynkin, E. B. (1952). Semisimple subalgebras of semisimple Lie algebras. *Mat. Sbornik*, 30(2), 349–462.
- Minchenko, A. N. (2006). The semisimple subalgebras of exceptional Lie algebras. *Trans. Moscow Math. Soc.*, 67, 225–259.
- Paper 92 (F4 Universality): FLCR framework application.

---

*File created for FLCR-92-OBL-001. Status: closed.*
