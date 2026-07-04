-- ============================================================
-- Paper 60 — Unified QCD Phenomenology 4 Lattice QCD
-- Domain: Lattice QCD / Discrete Formulation
-- Cross-references: Paper 02 (CA), Paper 08 (lattice closure),
--                   Paper 57-59 (QCD phenomenology)
-- ============================================================

-- Table: lattice_qcd_parameters
-- Role: Lattice QCD as discrete QCD on FLCR substrate
CREATE TABLE IF NOT EXISTS lattice_qcd_parameters (
    param_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    lattice_spacing REAL,                  -- a (fm)
    lattice_size    INTEGER,               -- N^4
    beta            REAL,                  -- gauge coupling parameter
    quark_mass_mev  REAL,
    continuum_limit INTEGER DEFAULT 0      -- whether extrapolated
);

-- Table: lattice_qcd_observables
-- Role: Observables computed on the lattice
CREATE TABLE IF NOT EXISTS lattice_qcd_observables (
    observable_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    param_id        INTEGER NOT NULL,
    observable_name TEXT NOT NULL,
    lattice_value   REAL,
    continuum_value REAL,
    extrapolation_status TEXT,
    FOREIGN KEY (param_id) REFERENCES lattice_qcd_parameters(param_id)
);

-- Seed data: lattice QCD parameters
INSERT INTO lattice_qcd_parameters (lattice_spacing, lattice_size, beta, quark_mass_mev, continuum_limit) VALUES
(0.1, 32, 6.0, 50.0, 0),
(0.05, 64, 6.5, 25.0, 0);

-- Merged from paper-060__unified_claims.sql
-- paper-060 SQL Claim Ledger

CREATE TABLE IF NOT EXISTS claims_060 (
    claim_id TEXT PRIMARY KEY,
    claim_text TEXT,
    tag TEXT,
    source_file TEXT,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.1', 'Corpus database contains 18 tables, 1665 functions, 31 papers', 'D', 'CQE-PAPER-060.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.2', 'Corpus verifies itself via receipt system with 43 checks, 0 defects', 'D', 'CQE-PAPER-060.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.3', 'Corpus contains 31 formal papers, 420 sections, 298 lib modules, 1665 functions', 'D', 'CQE-PAPER-060.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.4', '9 verifiers perform 43 checks with 100% pass rate (0 defects)', 'D', 'CQE-PAPER-060.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.5', '5 calibration suites with 27 parameters all PASS', 'D', 'CQE-PAPER-060.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.6', 'Self-verification: 9 verifiers / 43 checks / 0 defects (100% PASS)', 'D', 'CQE-PAPER-060.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.7', 'Self-calibration: 5 suites / 27 parameters (all PASS)', 'D', 'CQE-PAPER-060.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.8', 'Narrative queries: 3/3 PASS', 'D', 'CQE-PAPER-060.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.9', 'Corpus Self-Query PASS: 31 papers indexed, 0 defects', 'D', 'CQE-PAPER-060.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.10', '19 tile families in corpus', 'D', 'CQE-PAPER-060.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.11', '8 crystallization scenarios in corpus', 'D', 'CQE-PAPER-060.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.12', 'Self-reference at depth 3', 'I', 'PAPER-060-TILE-INTEGRATION.md');
INSERT INTO claims_060 (claim_id, claim_text, tag, source_file) VALUES ('60.13', '100% coverage = corpus reads all its own tiles completely', 'I', 'PAPER-060-TILE-INTEGRATION.md');
