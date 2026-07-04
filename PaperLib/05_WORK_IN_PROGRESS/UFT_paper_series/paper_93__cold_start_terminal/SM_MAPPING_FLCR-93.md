# SM Mapping File for FLCR-93: Cold-Start Terminal Selection

## The Cold-Start Terminal Selection Algorithm

The explicit cold-start terminal selection algorithm is specified in Theorem 1.2 of Paper 93.

### Algorithm Steps

Given an arbitrary state S of size n (bitstring of length n):

1. **Compute initial fingerprint**: f₀(S) = lucas_bit(n, 0)
   - Computable in O(log n) time via bitwise operations
   - The Lucas bit formula: 1 iff (n even) ∧ (k = n/2 ≤ n) ∧ (k & n) == k

2. **Map to lattice depth**: d = n mod 72, then d_t = argmin_{d' ∈ {1,3,7,8,24,72}} |d - d'|
   - Constant-time lookup in the 6-element lattice code chain

3. **Select terminal form**: Higgs state (weight w = 5)
   - Independent of d_t; d_t determines the path, not the terminal form
   - Mass: m_H = 5·κ·SCALE = 125.25 GeV

4. **Compute terminal fingerprint**: c_5 (McKay-Thompson coefficient at weight 5)
   - Counts the degeneracy of the weight-5 state in the Monster VOA

5. **Output**: (T = Higgs, fingerprint = c_5)

### Complexity

- Total: O(log n) + O(1) + O(1) + O(1) = O(log n)
- The O(log n) bound comes from the Rule 90 cold-start formula (Lucas bit)
- Remaining steps are constant-time

## Receipt Chain

- Paper 2 (Rule 30 ANF): The Lucas bit formula and O(log d) computability
- Paper 4 (Lattice code chain): The terminal depths {1, 3, 7, 8, 24, 72}
- Paper 16 (Mass residue): The VOA weight assignment, Higgs at w=5
- Paper 90 (McKay-Thompson): The Monster coefficient c_5
- Paper 9 (Lattice closure): The terminal address convergence

## Data vs Interpretation

- **(D)**: The explicit algorithm, the Lucas bit formula, the lattice code chain, the VOA weight assignment, the Monster coefficient c_5.
- **(I)**: The identification of the Higgs state as the "terminal form", the framing of the algorithm as "cold-start terminal selection", the cosmological framework as the "ultimate cold-start".
- **(X)**: None. The algorithm is explicit; the fingerprint map is explicit; the O(log n) proof is given.

## References

- Paper 93 (Cold-Start Terminal Selection): FLCR framework application.
- Paper 2 (Rule 30 ANF): Lucas bit formula, O(log N) readout.
- Paper 4 (D4, J3(O), Triality): Lattice code chain.
- Paper 16 (Mass Residue): VOA weight assignment.
- Paper 90 (McKay-Thompson Parity): Monster coefficients.
- Paper 9 (Lattice Closure): Terminal addresses.

---

*File created for FLCR-93-OBL-001. Status: closed.*
