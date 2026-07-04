-- ============================================================
-- Paper 86 — Unified Riemann Hypothesis Critical Line As Big Bang Crease
-- Domain: Riemann Hypothesis / Clay Millennium
-- Cross-references: Paper 17 (lattice code chain), Paper 91 (Niemeier)
-- ============================================================

-- Table: riemann_hypothesis
-- Role: RH from lattice code chain. Primes = fold points of critical line.
CREATE TABLE IF NOT EXISTS riemann_hypothesis (
    rh_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    claim           TEXT NOT NULL DEFAULT 'All non-trivial zeros have Re(s) = 1/2',
    critical_line   REAL NOT NULL DEFAULT 0.5,
    approach        TEXT DEFAULT 'lattice_code_chain',
    primes_as_folds INTEGER DEFAULT 1,
    arf_matching    INTEGER DEFAULT 0,
    structural_approach INTEGER DEFAULT 1,
    full_proof      INTEGER DEFAULT 0,
    status          TEXT DEFAULT 'structural_approach'
);

-- Table: zeta_zeros
-- Role: Known zeros of Riemann zeta on critical line
CREATE TABLE IF NOT EXISTS zeta_zeros (
    zero_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    zero_number     INTEGER NOT NULL,
    imaginary_part  REAL NOT NULL,
    verified_on_line INTEGER DEFAULT 1
);

-- Seed data: first few zeta zeros
INSERT INTO zeta_zeros (zero_number, imaginary_part) VALUES
(1, 14.1347),
(2, 21.0220),
(3, 25.0109),
(4, 30.4249),
(5, 32.9351);

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 86
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p86 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p86 (claim_ref, claim_text, status, source_file) VALUES
('86.1', 'Paper 86 maps the Riemann hypothesis (10^13 zeros checked, bounded)', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p86 (claim_ref, claim_text, status, source_file) VALUES
('86.2', 'C-86-01 | Riemann ζ-function has trivial zeros at negative even integers | Paper 86, §2 | **(D)** | Number theory | Standard: functional equation | —', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p86 (claim_ref, claim_text, status, source_file) VALUES
('86.3', 'C-86-02 | Non-trivial zeros lie on critical line Re(s) = 1/2 | Paper 86, §3 | **(X)** | Number theory | Riemann Hypothesis is open | Prove RH', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p86 (claim_ref, claim_text, status, source_file) VALUES
('86.4', 'C-86-03 | **1/2 = prime state in FLCR framework** | Paper 86, §4 | **(I)** | Physics/NT | User''s interpretation | Derive from LCR carrier', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p86 (claim_ref, claim_text, status, source_file) VALUES
('86.5', 'C-86-04 | Critical line = crease of fold in FLCR | Paper 86, §5 | **(I)** | Physics/NT | Structural analogy | Prove correspondence', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p86 (claim_ref, claim_text, status, source_file) VALUES
('86.6', 'C-86-05 | **RH from boundary repair framework** | Paper 86, §6 | **(X)** | Number theory | No derivation exists | Derive zero distribution from repair', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p86 (claim_ref, claim_text, status, source_file) VALUES
('86.7', 'C-86-06 | ζ(s) = product over primes | Paper 86, §2 | **(D)** | Number theory | Standard: Euler product | —', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p86 (claim_ref, claim_text, status, source_file) VALUES
('86.8', 'C-86-07 | **Prime distribution from LCR carrier** | Paper 86, §7 | **(X)** | Number theory | No formula exists | Derive π(x) from Rule 30 structure', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p86 (claim_ref, claim_text, status, source_file) VALUES
('86.9', 'C-86-08 | Riemann Hypothesis is open | Paper 86, §2 | **(D)** | Number theory | Clay Mathematics Institute | —', 'I', 'mapped_file_claims_report.md');
