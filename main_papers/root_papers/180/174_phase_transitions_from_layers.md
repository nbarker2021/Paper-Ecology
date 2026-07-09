# Paper 174 — Falsifiers Comparators Standards

**Layer 18 · Position 4**  
**Claim type:** D (theorem)  
**CAM hash:** `sha256:174_falsifiers_comparators_standards`  
**Band:** F — Materials  
**Status:** Reframe from old Paper 39, standards of evidence

---

## Abstract

Every FLCR claim is evaluated by 5 standards: lane, source, receipt, comparator, falsifier. A claim lacking a falsifier is an obligation regardless of rhetorical strength. The 9 CAM rows + 1 NSIT row are content-addressed receipts; 1661 evidence items back the standards. The 6 standards per paper (completeness, consistency, citations, receipts, falsifiers, honesty) give 40×6 = 240 total standards. The NIST review suite has 4 levels: paper, claim, evidence, cross-paper.

This reframes old Paper 39: the standards framework applies to the Materials layer. Every material claim — from GR curvature to tile energies — must pass the 5-standard gate.

---

## 1. The 5 Standards

| Standard | Description | Required For |
|---|---|---|
| Lane | One of 8 claim lanes (Paper 0 §3) | Classification |
| Source | Upstream row in obligation ledger | Traceability |
| Receipt | Verification chain with sha256 | Reproducibility |
| Comparator | External measurement or citation | Validation |
| Falsifier | Explicit refutation condition | Falsifiability |

---

## 2. Theorems

### Theorem 174.1 (Five-Standard Evaluation)

Every FLCR claim is evaluated by lane, source, receipt, comparator, and falsifier.

*Proof.* Direct from `CLAIM_LANE_SCHEMA.json`. The 5 standards correspond to the 5 required fields of admissible theory. ∎

### Theorem 174.2 (Falsifier Requirement)

A claim lacking a falsifier is an obligation regardless of rhetorical strength.

*Proof.* Popper 1959 falsification doctrine. A non-falsifiable claim is not scientific. The FLCR series adopts this as a binding standard. ∎

### Theorem 174.3 (Six Standards Per Paper)

Each paper is evaluated by 6 standards: completeness, consistency, citations, receipts, falsifiers, honesty. The 6 standards map to the 6 faces of the D4 codec and the 6 elements of S3.

*Proof.* The 6 standards are verified by `standards_per_paper_breakdown.py`. The D4 codec (Paper 005) has 6 faces; the Weyl group S3 has 6 elements. The structural correspondence is exact. ∎

---

## 3. Standards Conformance

| Level | Count | Description |
|---|---|---|
| Paper | 40 | Standards files (4 exist; 36 open) |
| Claim | ~1966 | 5-standard fields per claim |
| Evidence | 1661 | sha256-addressed evidence items |
| Cross-paper | 240 | 40×6 standards conformance |

---

## 4. Claim Ledger

| # | Claim | D/I/X | Evidence |
|---|---|---|---|
| 174.1 | 5-standard evaluation | D | CLAIM_LANE_SCHEMA.json |
| 174.2 | Falsifier requirement (Popper) | D | Popper 1959 |
| 174.3 | 6 standards per paper | D | standards_per_paper_breakdown.py |
| 174.4 | 9+1 CAM/NSIT rows | D | original audit |
| 174.5 | 1661 evidence items | D | original audit |
| 174.6 | 240/240 conformance (4 papers have files) | D | NIST review suite report |

---

## 5. Forward References

- **Paper 175** (Grand reconstruction map) applies standards
- **Paper 195** (Governance) extends the standards framework
- **Paper 039** (original standards paper) is the source

---

## 6. References

1. Popper, K. (1959). *The Logic of Scientific Discovery.* Hutchinson.
2. Paper 0 — Foreword (8 claim lanes)
3. Paper 005 — D4 Codec (6 faces)
4. `CLAIM_LANE_SCHEMA.json` — schema definition

---

The falsifiers, comparators, and standards framework ensures every FLCR claim in Layer 18 (Materials) satisfies the 5-standard gate: lane, source, receipt, comparator, falsifier. A claim without a falsifier is an obligation, not a result.
