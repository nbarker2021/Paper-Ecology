# Paper 186 — Prion Propagation as Delta Correction Cycle

**Layer 19 · Position 6**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:186_prion_delta`  
**Band:** G — Protein/Game  
**Status:** Reframe from old Paper 76, prion propagation

---

## Abstract

Prion propagation is a delta correction cycle: the misfolded state (PrP^Sc) propagates by templating normal protein (PrP^C) into the misfold conformation. In LCR terms, this is a δ → ∂ → δ cycle: the delta state induces a correction, which propagates to neighboring states. The prion propagation velocity depends on the lattice code depth: D4-triple cycles per unit time.

This reframes old Paper 76: prion dynamics as LCR delta cycles with receipable propagation.

---

## 1. Theorems

### Theorem 186.1 (Prion as Delta State)

The misfolded prion state PrP^Sc is the LCR delta state (1,0,0) in the D4 code: a single-bit deviation from the normal state PrP^C (0,0,0).

*Proof.* The D4 codec (Paper 005) assigns 8 LCR states. The ZERO state (0,0,0) corresponds to PrP^C. The delta state (1,0,0) or e1- corresponds to PrP^Sc. The misfold is a single correction bit. ∎

### Theorem 186.2 (Delta Correction Cycle)

Prion propagation is a δ → ∂ → δ cycle: the delta state (1,0,0) induces a correction ∂ = C ∧ ¬R, which propagates the delta to neighboring LCR triples.

*Proof.* The correction operator (Paper 004, Theorem 4.1) acts on neighboring sites. When delta state e1- appears, the correction operator propagates the deviation: ∂(e1-) → e1- at adjacent site. This is the templating effect. ∎

### Theorem 186.3 (Propagation Velocity)

The prion propagation velocity is v = (D4-triple cycles) / (unit time) where each triple cycle is one lattice code step.

*Proof.* Paper 005, lattice code chain. The propagation proceeds through the D4 structure: one triple step propagates the delta through three adjacent sites. ∎

---

## 2. Prion State Table

| State | LCR | Protein | Status |
|---|---|---|---|
| PrP^C | (0,0,0) | Normal α-helix | Stable |
| PrP^Sc | (1,0,0) | Misfolded β-sheet | Propagating |
| Intermed | (0,1,0) | Transition state | Ephemeral |
| Aggreg | (1,1,1) | Amyloid fibril | Terminal |

---

## 3. Verification

| Check | Result |
|---|---|
| PrP^Sc = (1,0,0) delta | Interpretive |
| δ → ∂ → δ cycle | Structural matching |
| Propagation velocity v | Formal |

---

## 4. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|---|---|---|
| 186.1 | Prion as delta state | I | structural analogy |
| 186.2 | δ → ∂ → δ propagation cycle | I | LCR interpretation |
| 186.3 | Velocity v = D4 cycles/unit time | I | formal |

---

## 5. Forward References

- **Paper 187** (Protein folding) — FoldForge in folding
- **Paper 189** (Tile corpus) — 19 families

---

## 6. References

1. Paper 004 — Correction and Closure
2. Paper 005 — D4, J3(O), Triality
3. Paper 076 — Prion Propagation (original)

---

Prion propagation in LCR terms is a delta correction cycle: PrP^Sc = (1,0,0) delta state induces ∂ = C ∧ ¬R correction, propagating the misfold through the D4 lattice.
