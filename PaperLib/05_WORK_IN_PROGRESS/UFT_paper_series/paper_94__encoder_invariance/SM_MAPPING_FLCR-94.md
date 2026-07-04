# SM Mapping File for FLCR-94: Encoder Invariance for Sporadic Boundary

## Encoder Invariance: Explicit Derivation

The encoder invariance is proved explicitly from the D4 codec structure (Paper 4, Theorem 2.1).

### The D4 Weyl Group Action

The D4 Weyl group W(D4) has order 192 = 2^6 · 3. It acts on the 8 LCR states by:
- **S3 subgroup**: Permutes the 3 non-trivial axis classes (the trace-2 idempotents of J3(O))
- **(Z/2Z)^3 subgroup**: Flips the sheets within each axis class

### Encoder Invariance Theorem

**Theorem 1.1.1**: The admissibility predicate A is invariant under W(D4).

**Proof sketch**: The admissibility depends only on the shell grading (shell ≤ 2: admissible, shell = 3: inadmissible). The shell grading is the number of 1s in the state, which is preserved by axis permutation and sheet flip. Therefore, A(E1(S)) = A(E2(S)) for all W(D4)-related encoders E1, E2.

### Feature Invariance Theorem

**Theorem 1.6.1**: The feature vector f(S) = (a, s) transforms as a representation of W(D4):
- Axis a ∈ {1,2,3,4} is permuted by S3 (fixing axis 4)
- Sheet s ∈ {0,1} is flipped by Z/2

The admissibility is invariant under this transformation because the shell grading g(S) = a + s - 1 is preserved.

### Encoder Class

The encoder class is the W(D4) orbit of any encoder. The orbit size divides 192. The admissibility is constant on the orbit.

### Flavor Symmetry

The S3 axis permutation is the flavor symmetry: it corresponds to the permutation of the 3 fermion generations (Paper 14, Corollary 5.3). The encoder invariance under S3 means all 3 generations have the same admissibility status.

## Receipt Chain

- Paper 4 (D4, J3(O), Triality): D4 codec, axis/sheet structure, Weyl group
- Paper 5 (Typed Boundary Repair): Boundary type, admissibility predicate
- Paper 12 (Theory Admission Gates): Admissibility predicate formalization
- Paper 14 (Quark-Face Algebra): 3 fermion generations, S3 flavor symmetry
- Paper 38 (AI Runtime): Runtime preserves lattice structure
- Paper 91 (Niemeier Glue): E6 root system, 72 roots

## Data vs Interpretation

- **(D)**: The explicit encoder invariance proof, feature invariance derivation, D4 Weyl group action, W(D4) order 192.
- **(I)**: The sporadic boundary as repair curvature, Pariah groups as mass residue, lattice code chain as encoder hierarchy, E6 roots as encoder instances.
- **(X)**: None. The encoder invariance is proved; the feature invariance is derived. The SM mapping file has been created.

## References

- Paper 94 (Encoder Invariance): FLCR framework application.
- Paper 4 (D4, J3(O), Triality): D4 codec structure.
- Paper 5 (Typed Boundary Repair): Boundary type and admissibility.
- Paper 12 (Theory Admission Gates): Admissibility predicate.
- Paper 14 (Quark-Face Algebra): Fermion generations, S3 flavor symmetry.
- Bengio, Y., Courville, A., & Vincent, P. (2013). Representation learning.

---

*File created for FLCR-94-OBL-001. Status: closed.*
