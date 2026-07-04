# Paper 02 — Correction Surface

**Status:** IPMC — internal physics map closed for the correction decomposition, exact firing set, and D4 axis/sheet projection under the production codec. Physics/emission/telemetry bridges are named and scoped.

---

## Abstract

Paper 02 formalizes the first repair layer after the LCR carrier. Given a local state `(L, C, R)`, the paper defines a correction surface as the typed residue left when a simpler transport fails to reproduce a target transition. The closed finite theorem is the Rule 30 / Rule 90 decomposition

```text
R30(L, C, R) = R90(L, R) xor corr(L, C, R)
corr(L, C, R) = C and not R
```

over all eight binary LCR states. The correction surface fires exactly on `(0,1,0)` and `(1,1,0)`. The result is not that every failure is automatically a theorem. The result is that failure becomes addressable data: a typed, localized, replayable obligation that later papers can transport, repair, curve, lift, or falsify.

The D4 axis/sheet projection is closed only under the declared production codec. The paper explicitly rejects competing claims that the correction fires on three states or includes `(1,1,1)`. Physical readings such as gluon vertex, light-cone boundary, Higgs carrier, or product telemetry remain named bridges until separate calibration receipts exist.

---

## Claim Ledger

| Claim | Status | Evidence | Boundary |
|-------|--------|----------|----------|
| Rule 30 decomposes as Rule 90 plus `C and not R`. | [D] Closed | `verify_correction_surface.py`; `correction_surface_receipt.json` (5/5) | Binary radius-1 LCR window |
| The correction fires exactly on `(0,1,0)` and `(1,1,0)`. | [D] Closed | Full eight-state enumeration; 5/5 verifier checks | Excludes three-state summary variants |
| Nonzero correction is typed obligation data, not proof by itself. | [D] Closed as paper discipline | Claim contract and receipt wording | Later papers must consume receipts explicitly |
| The correction rows project to `(2,0)` and `(3,1)` under the production D4 codec. | [D] Closed within codec | Verifier and Paper 03 preservation check | Competing codecs remain governance work |
| The monitor partition and exact binomial logging are finite receipt surfaces. | [D] Closed | `verify_correction_surface_monitor.py`; 10/10 checks | Not empirical product telemetry |
| McKay parity, F2 governance, and E6/E7/E8 lifting follow from this paper alone. | [X] Not claimed | No closing theorem here | Route to NP-01, NP-05, and NP-02 |
| "Correction = gluon vertex / 3-gluon vertex" in physical QCD. | [I] Interpretive bridge | Named in summaries; no physical measurement | Requires calibration (P13–P16) |

---

## Definitions

Let `A = {0, 1}` and let an LCR state be `s = (L, C, R) ∈ A³`.

**Definition 1 (Rule 30 local update).** `R30(L, C, R) = L XOR (C OR R)`.

**Definition 2 (Rule 90 local update).** `R90(L, R) = L XOR R`.

**Definition 3 (Correction map).** `corr(L, C, R) = C AND (NOT R)`.

**Definition 4 (Correction surface).** The set of local states where `corr` is nonzero, together with the receipt that records how that residue is fed to the next transport step.

**Definition 5 (Residue ledger row).** A typed record `(state, residue, status, next_route)` where `status ∈ {obligation, closed}` and `next_route` names the consuming paper or verifier.

---

## Theorem 2.1 — Correction Decomposition

**Statement.** For every binary LCR state,

```text
R30(L, C, R) = R90(L, R) XOR corr(L, C, R).
```

Moreover, `corr` is nonzero exactly on `{(0,1,0), (1,1,0)}`.

**Proof.** Over Boolean values, the inclusive OR decomposes as

```text
C OR R = C XOR R XOR (C AND R).
```

Therefore

```text
R30(L, C, R)
  = L XOR (C OR R)
  = L XOR C XOR R XOR (C AND R)
  = (L XOR R) XOR (C XOR (C AND R))
  = R90(L, R) XOR (C AND NOT R).
```

The last equality holds because `C XOR (C AND R)` is `1` exactly when `C = 1` and `R = 0`, and is `0` otherwise. Thus the correction is `C AND NOT R`.

Enumerating the eight LCR states, `C = 1` and `R = 0` occurs only for `(0,1,0)` and `(1,1,0)`. The `verify_correction_surface.py` verifier checks all five finite facts: the identity holds for all 8 states, the firing set is exact, the D4 projection is exact, and nonzero residues are typed as obligations (5/5 checks pass). ∎

---

## Theorem 2.2 — Correction-Surface Monitor

**Statement.** The correction surface admits a finite monitor layer: the eight LCR triads partition as `2/2/4` (2 deep invariants, 2 level-1 invariants, 4 variable states), the Rule 30 = Rule 90 plus correction identity remains exact, and deviation from the expected correction ratio is logged by exact two-tailed binomial receipts.

**Proof.** The `verify_correction_surface_monitor.py` verifier runs `SentinelForge.verify()`, which checks 10 finite properties (10/10 pass):

1. The 8 triads partition `2/2/4`: deep invariants `{000, 111}`, level-1 invariants `{010, 101}`, variable `{001, 011, 100, 110}`.
2. Lie conjugates (`L = R`) are exactly deep union level-1.
3. `R30 = R90 XOR correction` on all 8 states.
4. The correction bit `C AND (NOT R)` fires on exactly 2 of 8 states.
5. Geometry levels `0/1/2` partition as `2/2/4`.
6. Bonded frames are the cyclic rotations plus the LR mirror; the antipodal frame is an involution.
7. An exactly balanced stream yields ratio `0.25`, sigma `0`, severity nominal.
8. A frozen all-vacuum stream is an emergency with `p < 1e-9`.
9. The exact binomial machinery: total mass 1, `p = 1` at the mean.
10. The severity ladder is monotone in sigma.

The detection-quality claims of any product (false-positive rates against real infrastructure telemetry) are NOT claimed here; they remain product obligations. Only the finite partition and proof machinery is bound. ∎

---

## D4 Chart Projection

Under the production lattice-forge axis/sheet codec, the correction firing states map as:

```text
(0,1,0) -> axis 2, sheet 0
(1,1,0) -> axis 3, sheet 1
```

Thus the correction tape can be read as a one-bit projection of the D4 chart state:

```text
corr != 0 iff (axis, sheet) in {(2,0), (3,1)}.
```

Paper 02 does not require later D4 or triality claims to be proven here. It only records the projection that later papers consume. Paper 03 preserves these coordinates in its triality presentation under the production codec.

---

## Important Cross-Corpus Conflict

`CMPLX-Kernel/lib-forge/summary_papers/SUMMARY-I-Gluon-at-Center.md` states that `corr = C ∧ ¬R` fires on **three** states including `(1,1,1)` and maps to D4 axes `{0, 2, 3}`. This is inconsistent with the closed formal theorem, the verifier, and `CQE-paper-02.50`, all of which give **two** firing states `{(0,1,0), (1,1,0)}` mapped to `(2,0)` and `(3,1)`. The summary paper is therefore an interpretive/erroneous overstatement relative to the closed proof.

The production codec and verifier are the current source of truth. Axis naming reconciliation remains an open tooling obligation (02.6).

---

## Verifiers and Receipts

| Verifier | Receipt | Checks | Result |
|----------|---------|--------|--------|
| `verify_correction_surface.py` | `correction_surface_receipt.json` | 8 states, identity for all states, firing states exact, D4 projection exact, nonzero residue is obligation not proof | pass (5/5) |
| `verify_correction_surface_monitor.py` | `correction_surface_monitor_receipt.json` | Partition `2/2/4`, Lie conjugates, Rule 30 = Rule 90 XOR correction, correction fires on exactly 2 states, geometry levels, bonded frames/antipodal involution, balanced/frozen streams, binomial exact mass/mean p, monotone severity ladder | pass (10/10) |

---

## Hand Reconstruction

1. Draw the three LCR cells.
2. Fill each cell with a binary token.
3. Compute `Rule 30 = L XOR (C OR R)`.
4. Compute `Rule 90 = L XOR R`.
5. Compute `corr = C AND (NOT R)`.
6. Verify that `Rule 30 = Rule 90 XOR corr`.
7. If `corr = 1`, mark a black residue token.
8. Copy the residue into an obligation row rather than erasing it.

The supplemental hand exposure should produce two firing states and six non-firing states. The firing states are `(0,1,0)` and `(1,1,0)`.

---

## Falsifiers and Rejected Claims

1. [X] "The correction fires on three states including `(1,1,1)`." *(Rejected: the verifier confirms exactly two firing states: `(0,1,0)` and `(1,1,0)`.)*
2. [X] "A nonzero correction automatically proves the original route." *(Rejected: correction creates an obligation, not a theorem.)*
3. [X] "The D4 axes `{0,2,3}` are the correction firing axes." *(Rejected: the production codec maps to `(2,0)` and `(3,1)`.)*
4. [X] "Product telemetry false-positive rates are proven by this paper." *(Rejected: detection-quality claims remain product-layer empirical work.)*

---

## Relation to Later Papers

- **Paper 00:** supplies the foundational axioms, the `(L,C,R)` chart, and the T3–T7 chart↔`J₃(𝕆)` / SU(3) substrate.
- **Paper 01:** supplies the side-flip bijection / LCR carrier; Paper 02 preserves `C` under `L↔R` and uses the same 8-state window.
- **Paper 03:** receives the two correction firing rows as registered D4/`J₃` coordinates; `verify_triality_surface.py` explicitly checks that Paper 02 coordinates `(2,0)` and `(3,1)` are preserved. This closes obligation 02.2.
- **Paper 04:** receives correction rows as typed boundary-repair constraints (oloid midpoint, `Dust(N,-N)`, `MIRROR_REQUIRED`).
- **Paper 05:** receives the correction carrier / `C_accumulated` for the oloid path / Wilson-loop interpretation.
- **Paper 06:** receives correction firings as typed causal edges (`transports`, `obligates`, `refines`) with receipts.
- **Papers 07–08:** receive correction traces for the discrete-continuous bridge and lattice-defect closure.
- **CQE-PAPER-020–023** (recursive-closure track): re-use `∂ = C ∧ ¬R` as the light-cone boundary operator; depth-3 void where correction = 0.

---

## Open Obligations

| ID | Obligation | Likely closure |
|----|------------|--------------|
| 02.1 | Wire verifier into `cqe_engine.formal`. | Engineering (NP-05) |
| 02.2 | Reconcile D4 axis/sheet labels with Paper 03's triality presentation. | **Closed by CQE-paper-03** (production codec) |
| 02.3 | Extend receipt format so later papers consume correction rows directly. | CQE-paper-06 / ecology receipt layer |
| 02.4 | Add peer-review citations for Rule 30, Rule 90, Boolean normal forms, cellular automaton linearization. | Bibliography (NP-08) |
| 02.5 | Keep product telemetry false-positive claims outside the paper until empirical product receipts exist. | Product layer; not paper-closable |
| 02.6 | Reconcile competing axis/sheet codings across all D-drive copies (production `(2,0)/(3,1)` vs. summary `{0,2,3}` vs. R30 `chart_codec_d4.py`). | Tooling cleanup; single canonical `chart_codec_d4.py` |
| 02.7 | Closed-form `mckay_thompson_coefficient_parity` for Lucas-sparse correction sum (R30 O2′). | `lattice_forge/rule90_linearization.py` + `voa_lookup.py` |
| 02.8 | F₂-bridge governance / contribution registry (R30 O2″). | `lattice_forge/f2_majorana.py`, `contributions_registry.py` |
| 02.9 | E₆→E₇→E₈ lift beyond quaternion-sub-algebra trapping (R30 O2‴). | `lattice_forge/quad_oloid.py`, `oloid_dual_path.py` |

---

## Bibliography

1. Wolfram, S. (2002). *A New Kind of Science*. Champaign, IL: Wolfram Media. (Rule 30 and elementary cellular automata)
2. Boole, G. (1847). *The Mathematical Analysis of Logic*. Cambridge: Macmillan. (Boolean algebra foundations)
3. Lucas, É. (1878). *Théorie des fonctions numériques simplement périodiques*. American Journal of Mathematics, 1(2), 184–196. (Lucas theorem; Rule 90 closed form)
4. Conway, J. H., & Sloane, N. J. A. (1988). *Sphere Packings, Lattices and Groups*. New York: Springer. (`D₄` root system, axis/sheet codec)

---

## Conclusion

Paper 02 converts mismatch into structured work. The finite identity is closed: the correction surface of Rule 30 relative to Rule 90 is exactly `C AND NOT R`, and it fires on two of the eight binary LCR states. The scientific discipline is equally finite: the residue is useful only when it is preserved as a replayable obligation. This is why correction becomes a surface rather than a trash bin. Competing axis/sheet codings in summary papers are a tooling reconciliation problem, not a theorem gap. The only thing that twice is once.
