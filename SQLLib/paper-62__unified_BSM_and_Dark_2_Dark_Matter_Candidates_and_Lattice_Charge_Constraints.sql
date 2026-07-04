-- ============================================================
-- Paper 62 — Unified BSM And Dark 2 Dark Matter Candidates
-- Domain: Dark Matter / Lattice Charge Constraints
-- Cross-references: Paper 61 (neutrino), Paper 63 (dark energy)
-- ============================================================

-- Table: dark_matter_candidates
-- Role: Dark matter candidates as lattice charges
CREATE TABLE IF NOT EXISTS dark_matter_candidates (
    candidate_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_name  TEXT NOT NULL,
    candidate_type  TEXT CHECK (candidate_type IN ('WIMP','axion','sterile_neutrino','primordial_black_hole','lattice_charge')),
    lattice_charge  INTEGER,
    mass_gev        REAL,
    cross_section   REAL,                  -- cm^2
    detection_status TEXT DEFAULT 'undetected'
);

-- Table: lattice_charge_constraints
-- Role: Lattice charge constraints limiting DM candidates
CREATE TABLE IF NOT EXISTS lattice_charge_constraints (
    constraint_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    charge_value    INTEGER,
    max_candidates  INTEGER,
    constraint_rule TEXT
);

-- Seed data: dark matter candidates
INSERT INTO dark_matter_candidates (candidate_name, candidate_type, lattice_charge, mass_gev, detection_status) VALUES
('Sterile neutrino', 'sterile_neutrino', 1, 1.0, 'undetected'),
('Axion-like',       'axion',            0, 1e-9, 'undetected'),
('Lattice charge',   'lattice_charge',   2, 10.0, 'undetected');

-- Merged from paper-062__unified_claims.sql
-- paper-062 SQL Claim Ledger

CREATE TABLE IF NOT EXISTS claims_062 (
    claim_id TEXT PRIMARY KEY,
    claim_text TEXT,
    tag TEXT,
    source_file TEXT,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO claims_062 (claim_id, claim_text, tag, source_file) VALUES ('62.1', 'Grand Ribbon encodes 6 preconditions for corpus next self-reading cycle', 'D', 'CQE-PAPER-062.md');
INSERT INTO claims_062 (claim_id, claim_text, tag, source_file) VALUES ('62.2', 'All 6 Grand Ribbon preconditions PASS: Verifiers, Calibrations, Coverage, Atlas, Lib, Schema', 'D', 'CQE-PAPER-062.md');
INSERT INTO claims_062 (claim_id, claim_text, tag, source_file) VALUES ('62.3', 'Verifiers PASS: 9/9 PASS, 43/43 checks', 'D', 'CQE-PAPER-062.md');
INSERT INTO claims_062 (claim_id, claim_text, tag, source_file) VALUES ('62.4', 'Calibrations PASS: 5/5 PASS (units, ckm, gamma72, games, protein)', 'D', 'CQE-PAPER-062.md');
INSERT INTO claims_062 (claim_id, claim_text, tag, source_file) VALUES ('62.5', 'Coverage 100%: Supervisor Cursor reports 1.0', 'D', 'CQE-PAPER-062.md');
INSERT INTO claims_062 (claim_id, claim_text, tag, source_file) VALUES ('62.6', 'Lib Stable: 298 modules, 1665 functions exact', 'D', 'CQE-PAPER-062.md');
INSERT INTO claims_062 (claim_id, claim_text, tag, source_file) VALUES ('62.7', 'Ribbon = 6 logical preconditions - Contract for next cycle - Tile state constraints', 'I', 'PAPER-062-TILE-INTEGRATION.md');
INSERT INTO claims_062 (claim_id, claim_text, tag, source_file) VALUES ('62.8', 'SpectreTile IRL Alignment: 14 edges, aperiodic, chiral', 'X', 'PAPER-062-TILE-INTEGRATION.md');
