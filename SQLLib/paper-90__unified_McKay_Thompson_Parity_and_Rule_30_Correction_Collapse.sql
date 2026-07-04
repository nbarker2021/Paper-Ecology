-- ============================================================
-- Paper 90 — Unified McKay Thompson Parity And Rule 30 Correction Collapse
-- Domain: McKay-Thompson / Monster Connection
-- Cross-references: Paper 18 (moonshine), Paper 81-83 (Rule 30)
-- ============================================================

-- Table: mckay_thompson_parity
-- Role: Parity of c_n determines correction collapse.
--       Correction collapse converges Rule 30 to Monster VOA.
CREATE TABLE IF NOT EXISTS mckay_thompson_parity (
    parity_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    conjugacy_class TEXT NOT NULL,
    coefficient_n   INTEGER,
    coefficient_value INTEGER,
    parity          INTEGER CHECK (parity IN (0,1)),
    correction_collapse INTEGER DEFAULT 1
);

-- Table: rule30_correction_collapse
-- Role: Convergence of Rule 30 correction to Monster VOA
CREATE TABLE IF NOT EXISTS rule30_correction_collapse (
    collapse_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    generation      INTEGER,
    correction_parity INTEGER,
    monster_coeff_linked INTEGER,
    convergence_status TEXT
);

-- Seed data: McKay-Thompson parity
INSERT INTO mckay_thompson_parity (conjugacy_class, coefficient_n, coefficient_value, parity) VALUES
('1A', 1, 196884, 0),
('2A', 1, 43724,  0),
('3A', 1, 8424,   0),
('4A', 1, 2148,   0);

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 90
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p90 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p90 (claim_ref, claim_text, status, source_file) VALUES
('90.1', 'Paper 90 follows: McKay-Thompson Parity and Rule 30 Correction Collapse', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p90 (claim_ref, claim_text, status, source_file) VALUES
('90.2', '*Next binding action:* Paper 83 and NP-01 (Paper 90) must close the P3 problem', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p90 (claim_ref, claim_text, status, source_file) VALUES
('90.3', '*Owner:* Paper 83 and Paper 90', 'I', 'mapped_file_claims_report.md');
