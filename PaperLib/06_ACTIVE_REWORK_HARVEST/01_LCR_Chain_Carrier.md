# Paper 01 — LCR Chain Carrier and Observer-Center Framing

**Status:** IPMC — internal physics map closed for the minimal-carrier, shell-2 doublet, and local O8 frame-inversion theorems. SU(2)/spinor physical transport bridges are named interpretive bridges (IBN) and explicitly scoped.

---

## Abstract

Paper 01 defines the first active carrier used by the CQECMPLX suite after the Paper 00 grounding contract: the ordered local triple `(L, C, R)`. The closed result is deliberately finite: any local machine that must preserve a distinguished center while retaining two addressable boundary directions requires at least three ordered slots. The LCR carrier realizes this lower bound. The verifier receipts enumerate the full binary state space, the center-preserving reversal action, the shell counts, and the address/value distinction that later papers must preserve.

The paper also closes two local interface claims. First, the shell-2 stratum `{(1,1,0), (1,0,1), (0,1,1)}` supports the side-flip doublet used by later trace-2 and closure papers (T_BIJECTIVE). Second, a local O8 frame-inversion verifier realizes the internal double-cover law `F² = −1` at a `2π` advance and `F⁴ = +1` at a `4π` advance. These claims are internal carrier semantics; they do not, by themselves, close physical spinor transport, quantum measurement, full `J₃(𝕆)` off-diagonal physics, `D₄/F₄` extensions, or Standard Model calibration.

---

## Claim Ledger

| Claim | Status | Evidence | Boundary |
|-------|--------|----------|----------|
| Three ordered slots are minimal for one center and two addressable boundaries. | [D] Closed | `verify_lcr_carrier.py` (8/8 checks) | Finite local carrier model |
| The binary LCR inventory has eight states with shell counts `1,3,3,1`. | [D] Closed | `verify_lcr_carrier.py` | Binary alphabet only |
| Left/right opposition is directional address, not boundary-value inequality. | [D] Closed | Rejection of value-inequality claim; `(1,0,1)` counterexample | Later prose must preserve this distinction |
| The shell-2 stratum carries the finite side-flip doublet interface. | [D] Closed | `verify_bijective_shell2_doublet.py` (7/7 checks) | Finite single-tape interface |
| The O8 frame-inversion law closes local double-cover semantics. | [D] Closed as internal carrier semantics | `verify_o8_spinor_double_cover_closed.py` (6/6 checks) | Not a measured physical spinor/QM transport claim |
| "SU(2) doublet" / "+spin / −spin" labels apply to the physical world. | [I] Interpretive bridge | Named in summaries; no physical measurement | Requires physical calibration (P13–P16) |
| Full `D₄/F₄/J₃(𝕆)` / Standard Model extensions follow from this paper alone. | [X] Not claimed | No closing receipt in this paper | Routed to exceptional-route and physical-calibration papers |

---

## Definitions

**Definition 1 (Alphabet).** Let `A` be a finite alphabet. For the binary corpus, `A = {0, 1}`.

**Definition 2 (LCR state).** An LCR state over `A` is an ordered triple `s = (L, C, R) ∈ A³`, where `C` is the distinguished center, `L` is the left boundary read relative to `C`, and `R` is the right boundary read relative to `C`.

**Definition 3 (Center projection).** `π_C(L, C, R) = C`.

**Definition 4 (Left-right reversal).** `ρ(L, C, R) = (R, C, L)`.

**Definition 5 (Binary shell / trace grade).** `shell(L, C, R) = L + C + R`. For binary states, this partitions the eight states into grades of multiplicity `1, 3, 3, 1`.

**Definition 6 (Directional opposition).** The structural fact that `L` and `R` are different addresses relative to `C`. This is independent of **value inequality** (`value(L) ≠ value(R)`), which is state-dependent.

**Definition 7 (Shell-2 stratum).** `S₂ = {(1,1,0), (1,0,1), (0,1,1)}`. The **chiral pair** is `(1,1,0) ↔ (0,1,1)` under reversal. The **balanced pivot / singlet** is `(1,0,1)`, which is reversal-fixed.

**Definition 8 (Frame inversion `F`).** The bit-complement operation used in the O8 closure to encode a `2π` phase advance on the carrier interface.

---

## Theorem 1.1 — Minimal LCR Carrier

**Statement.** Any ordered local carrier that preserves a distinguished center and records two addressable boundary directions requires at least three slots. The carrier `(L, C, R)` realizes this lower bound, and is therefore minimal.

**Proof.** A carrier that preserves a distinguished center must contain at least one address for the center. A carrier that records two boundary directions relative to that center must contain one address for the left boundary and one address for the right boundary. These three roles are pairwise distinct as addresses: if the center address is identified with a boundary address, the center is no longer distinguished; if the two boundary addresses are identified, the carrier cannot distinguish left from right. Hence at least three addresses are required. The ordered triple `(L, C, R)` has exactly these three addresses and no additional address. It preserves the center through `π_C`, records both boundary directions, and supports reversal by `ρ`. Thus it attains the lower bound. ∎

---

## Theorem 1.2 — Shell-2 Doublet Binding

**Statement.** In the binary LCR chart, the shell-2 stratum is exactly `S₂ = {(1,1,0), (1,0,1), (0,1,1)}`. Left-right reversal exchanges `(1,1,0)` and `(0,1,1)` while fixing `(1,0,1)`. Therefore the shell-2 stratum carries the finite single-tape doublet interface used by later trace-2 and closure papers.

**Proof.** By finite enumeration of all 8 binary states. The shell-2 states are precisely those with `L + C + R = 2`, giving the three states listed. Reversal `ρ` maps `(1,1,0) ↦ (0,1,1)` and `(0,1,1) ↦ (1,1,0)`, so the chiral pair is exchanged. Reversal maps `(1,0,1) ↦ (1,0,1)`, so the balanced state is fixed. The orbit structure is therefore one 2-element doublet plus one fixed point. This is the side-flip bijection `T_BIJECTIVE` from the theorem registry, now bound to Paper 01 as a finite carrier theorem. The `verify_bijective_shell2_doublet.py` verifier checks all seven finite facts: shell-2 set equality, reversal involution, chiral-pair exchange, fixed balanced state, orbit structure, center preservation, and shell invariance under reversal across all 8 states (7/7 checks pass). ∎

---

## Theorem 1.3 — O8 Frame-Inversion Double-Cover Closure

**Statement.** The frame-inversion operator `F` realized by the oloid kinematic layer satisfies the local double-cover law: `F²` gives the negative phase state (`−1`) at `2π` and `F⁴` returns to the positive phase state (`+1`) at `4π`. This closes the spinor double-cover obligation for the local carrier interface.

**Proof.** The production verifier `verify_o8_spinor_double_cover_closed.py` composes the existing `oloid_kinematic` checks:
1. Bit complement is verified as frame inversion `F`.
2. The two-period check verifies the `π` phase advance, corresponding to the `−1` spinor sign at `2π`.
3. The four-period check verifies return to origin, corresponding to `+1` at `4π`.
4. The alternating-bit and oloid-kinematic checks confirm consistency of the rolling double-cover carrier.

All six checks pass. This is a closed local carrier semantics claim. The physical reading of this interface as an SU(2) spinor doublet in quantum mechanics is an interpretive bridge (IBN) that requires additional physical calibration and transport receipts outside Paper 01. ∎

---

## Finite Binary Inventory

For the binary corpus case, the state space is `{0,1}³`, so there are exactly eight states:

```text
(0,0,0) shell 0
(0,0,1) shell 1
(0,1,0) shell 1
(0,1,1) shell 2
(1,0,0) shell 1
(1,0,1) shell 2
(1,1,0) shell 2
(1,1,1) shell 3
```

The reversal `ρ` preserves the center: `π_C(ρ(L,C,R)) = π_C(R,C,L) = C = π_C(L,C,R)`. It is also an involution: `ρ(ρ(L,C,R)) = (L,C,R)`.

The fixed states under reversal are exactly the states with `L = R`:
```text
(0,0,0), (0,1,0), (1,0,1), (1,1,1).
```

The non-fixed states form two reversal pairs:
```text
(0,0,1) ↔ (1,0,0)
(0,1,1) ↔ (1,1,0)
```

The state `(1,0,1)` is fixed under reversal and has shell 2. Therefore the statement "all shell-2 states have unequal boundary values" is false. The correct statement is that all states have two addressable boundary directions, and some states assign equal values to those two directions.

---

## Relation to Rule 30 Readout

Rule 30 uses the same local window form. Its Boolean update rule is `f(L,C,R) = L XOR (C OR R)`. Paper 01 does not claim to solve Rule 30. It establishes the carrier on which later Rule 30 and Jordan-algebra arguments can be expressed. In this role, LCR is the local chart: every update reads a center and two relative boundaries. The shell grading supplies a compact inventory of the eight local states; the reversal supplies the left-right symmetry operation that later papers compare with Weyl or Jordan diagonal permutations.

---

## Relation to the Diagonal Jordan Carrier

The binary LCR state can be embedded into the diagonal subalgebra of the exceptional Jordan algebra by `φ(L,C,R) = diag(L,C,R)`. At the level used in this paper, only the diagonal bookkeeping is required. The map preserves the eight binary states, the shell/trace value, and the left-right reversal as a swap of the first and third diagonal positions. Paper 01 does not need the full off-diagonal octonionic structure. That structure becomes relevant later when the corpus asks which additional theorems can be transported through a verified structure-preserving map.

## Fano Lift and Jordan Frame

The diagonal map `φ(L,C,R) = diag(L,C,R)` of Paper 01 is the Boolean shadow of a deeper structure. This section formally defines the Jordan frame, the Fano lift from F₂³ to the octonion basis, and the critical distinction between state bits and basis-address bits.

**Definition 1.9 (Jordan frame).** Let e₁ = E₁₁, e₂ = E₂₂, e₃ = E₃₃ be the diagonal matrix units in the Albert algebra J₃(𝕆). They satisfy:
- e_i ∘ e_j = δ_{ij} e_i,
- e₁ + e₂ + e₃ = 1.

These three objects are mutually orthogonal primitive idempotents summing to the identity. The set {e₁, e₂, e₃} is a **Jordan frame**.

**Definition 1.10 (Boolean LCR states as Jordan frame algebra).** For each binary vector b = (b₁, b₂, b₃) ∈ {0,1}³, define:
p_b = b₁ e₁ + b₂ e₂ + b₃ e₃.

Because b_i² = b_i, we have p_b ∘ p_b = p_b. The eight states p_b are exactly the Boolean algebra generated by the Jordan frame:
B(e₁, e₂, e₃) = { Σ b_i e_i : b_i ∈ {0,1} }.

**Theorem 1.4 (Boolean Frame Theorem).** The eight binary LCR states are exactly the Boolean algebra B(e₁, e₂, e₃) generated by the Jordan frame of primitive idempotents in the diagonal subalgebra of J₃(𝕆). The shell profile 1, 3, 3, 1 is the rank/trace profile of this Boolean subset.

*Proof.* The e_i are primitive idempotents with orthogonal support. For b ∈ {0,1}³, p_b = Σ b_i e_i satisfies p_b ∘ p_b = p_b because b_i² = b_i. There are 2³ = 8 such idempotents, matching the LCR state space. The trace tr(p_b) = b₁ + b₂ + b₃ takes values 0, 1, 2, 3 with multiplicities 1, 3, 3, 1, matching the LCR shell counts. ∎

**Definition 1.11 (Fano lift).** Let V = F₂³. The eight vectors of V are the full LCR binary chart. Remove the zero vector:
V^× = V \ {0} = {001, 010, 011, 100, 101, 110, 111}.

These seven nonzero vectors are the seven points of the Fano plane PG(2,2). Each line is {u, v, u+v} for distinct u, v. Using binary labels 1,…,7, the seven lines are:
123, 145, 167, 246, 257, 347, 356.

**Definition 1.12 (State-bit versus basis-address distinction).** The LCR state bits (L, C, R) ∈ {0,1}³ are **state bits** that select which primitive idempotents appear in p_b. The Fano basis-address bits u ∈ F₂³ \ {0} are **basis-address bits** that label the seven imaginary octonion directions. The zero vector 000 corresponds to the real unit 1 = ι(000). The nonzero vectors correspond to the seven imaginary units e_u = ι(u).

The **Fano lift** is the map:
ι: F₂³ → 𝕆,  ι(000) = 1,  ι(u) = e_u  (u ≠ 0),

where the oriented Fano structure determines the multiplication signs:
e_u² = −1,  e_u e_v = ε(u,v) e_{u+v}  (u ≠ v).

**Theorem 1.5 (Fano lift closure).** The Fano lift makes the binary state space not merely an eight-item analogy, but a carrier with a defined nonassociative multiplication law. The hierarchy is:
F₂³ → oriented Fano plane → (Im𝕆, G₂) → J₃(𝕆) → F₄.

*Proof.* The Fano plane incidence structure encodes which triples of imaginary units multiply associatively (lines) and which do not (non-lines). The oriented Fano structure fixes the signs ε(u,v), determining the full octonion multiplication table. The Albert algebra J₃(𝕆) is built from octonionic entries, and F₄ = Aut(J₃(𝕆)) is its automorphism group. ∎

**Remark (interpretive boundary).** This paper closes the finite LCR carrier and the diagonal Jordan frame. The off-diagonal octonionic dynamics, the full G₂ three-form, and the Spin(8) triality decomposition are routed to Paper 04b. Any physical identification of the eight states with quark colors or the eight directions with gluon generators requires a commutator-preserving representation map Φ_g: T_LCR → su(3) that is not constructed in this paper.

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Result |
|----------|---------|--------|--------|
| `verify_lcr_carrier.py` | `lcr_carrier_receipt.json` | 8 states, center preservation, involution, shell counts `1,3,3,1`, 4 fixed/2 paired orbits, rejection of value-inequality claim, 3-address minimality | pass (8/8) |
| `verify_bijective_shell2_doublet.py` | `bijective_shell2_doublet_receipt.json` | Shell-2 set equality, reversal involution, chiral-pair exchange, fixed balanced state, doublet+singlet orbit, center preservation, shell invariance; binds `T_BIJECTIVE` | pass (7/7) |
| `verify_o8_spinor_double_cover_closed.py` | `o8_spinor_double_cover_closed_receipt.json` | Frame inversion inverts rotation, `F² = −1` at `2π`, `F⁴ = +1` at `4π`, oloid kinematic consistency, alternating-bits zero net, composed double-cover law | pass (6/6) |

---

## Hand Reconstruction

The supplemental hand exposure is intentionally simple:

1. Draw three ordered cells labeled `L`, `C`, and `R`.
2. Place the center token in `C`.
3. Choose or roll binary values for all three cells.
4. Record the shell as the number of occupied cells.
5. Reverse the sheet by swapping the left and right positions.
6. Confirm that the center value did not move.
7. Mark whether the state is reversal-fixed or part of a reversal pair.
8. If a diagnostic claims `L ≠ R`, test it against `(1,0,1)` before accepting it.

This hand exposure is the analog twin of the finite verifier. It is supplemental, not a metaphor for the verifier; it is the same finite enumeration performed with physical tokens.

---

## Falsifiers and Rejected Claims

The following statements are explicitly rejected by this paper:

1. [X] "All shell-2 states have unequal boundary values." *(Counterexample: `(1,0,1)` has `L = R = 1` while `L` and `R` remain distinct boundary addresses.)*
2. [X] "Directional opposition implies value inequality." *(Directional opposition is structural; value inequality is state-dependent.)*
3. [X] "The side-flip bijection requires an antipodal counter-sheet." *(The shell-2 stratum on a single forward tape suffices; T_BIJECTIVE proves this.)*
4. [X] "The O8 closure proves the full Standard Model spinor extension." *(It closes local carrier semantics only; physical transport is a later bridge obligation.)*

---

## Relation to Later Papers

- **Paper 00:** inherits the foundational contract and the T3 chart↔`J₃(𝕆)` diagonal bijection. Paper 01 imports the Weyl `(1 3)` action and the diagonal registration machinery.
- **Paper 02:** correction surface uses the LCR carrier alphabet. The correction firing states `(0,1,0)` and `(1,1,0)` are preconditions on the carrier. `T_BIJECTIVE` predicts where correction fires.
- **Paper 03:** triality surface keeps the Paper 01 address/value correction and maps the shell-2 states to trace-2 diagonal idempotents; adds axis/sheet language. This closes obligation 01.3.
- **Paper 04:** boundary-repair gluon `s* = C` is identified with the oloid midpoint; relies on the antipodal shell-2 pair.
- **Paper 05:** the oloid path carrier `C_accumulated` is born from the repaired boundary.
- **Papers 09/15/17/18/31/32:** downstream uses — Hamiltonian time, Higgs mass-residue, error-correction towers, VOA weights, and the meta wrap `Paper 32 → Paper 01`.

---

## Open Obligations

| ID | Obligation | Likely closure |
|----|------------|--------------|
| 01.1 | Wire finite verifiers into `cqe_engine.formal`. | Engineering (NP-05) |
| 01.2 | Update older workbook language that equates opposed directions with unequal boundary values. | Documentation cleanup (NP-08) |
| 01.3 | Carry the corrected distinction into Paper 03. | **Closed by CQE-paper-03** |
| 01.4 | Keep the O8 closure scoped to the local frame-inversion/spinor double-cover receipt until broader physical transport is supplied. | Later physics papers (P13–P16) / `OPEN_OBLIGATIONS.md` O8 |
| 01.5 | Peer-review bibliography pass. | Bibliography (NP-08) |
| 01.6 | Full `D₄/F₄/J₃(𝕆)` / Standard Model claims. | Explicitly out of scope; routed to later papers |

---

## Bibliography

1. Jordan, P., von Neumann, J., & Wigner, E. (1934). *On an algebraic generalization of the quantum mechanical formalism*. Annals of Mathematics, 35(1), 29–64.
2. Wolfram, S. (2002). *A New Kind of Science*. Champaign, IL: Wolfram Media. (Rule 30 local structure)
3. Conway, J. H., & Sloane, N. J. A. (1988). *Sphere Packings, Lattices and Groups*. New York: Springer. (`D₄`, `E₈` root systems)
4. Cartan, É. (1894). *Sur la structure des groupes de transformations finis et continus*. Thesis. (Weyl groups and root systems)

---

## Conclusion

Paper 01 establishes the smallest local carrier used by the active suite. The corrected formal statement is:

> LCR is the minimal ordered carrier preserving one center and two addressable boundary directions. Directional opposition is structural; boundary-value inequality is not guaranteed.

Without this carrier, later papers have no disciplined way to say what a center is, what its two boundaries are, what reversal preserves, or which failures are real correction data. The SU(2)/spinor language is a named interpretive bridge; the proven core is the finite carrier structure. The only thing that twice is once.
