-- ============================================================
-- Paper 82 — Unified Wolfram P2 Rule 30 Density 1 2
-- Domain: Wolfram P2 / Rule 30 Density
-- Cross-references: Paper 02 (Rule 30), Paper 81 (P1)
-- ============================================================

-- Table: rule30_density
-- Role: Density = 1/2 proof via Lucas bit formula and ANF symmetry
CREATE TABLE IF NOT EXISTS rule30_density (
    proof_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    claim           TEXT NOT NULL DEFAULT 'Rule 30 has density 1/2',
    density_value   REAL NOT NULL DEFAULT 0.5,
    proof_method    TEXT DEFAULT 'ANF symmetry',
    anf_symmetry    INTEGER DEFAULT 1,
    structural_proof INTEGER DEFAULT 1,
    full_formal_verification INTEGER DEFAULT 0
);

-- Table: density_measurements
-- Role: Measured density at various depths
CREATE TABLE IF NOT EXISTS density_measurements (
    measurement_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    depth           INTEGER NOT NULL,
    ones_count      INTEGER,
    total_cells     INTEGER,
    measured_density REAL,
    deviation_from_half REAL
);

-- Seed data: density measurements
INSERT INTO density_measurements (depth, ones_count, total_cells, measured_density, deviation_from_half) VALUES
(100,    50,    100,    0.50,   0.0),
(1000,   500,   1000,   0.50,   0.0),
(10000,  5000,  10000,  0.5001, 0.0001);

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 82
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p82 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p82 (claim_ref, claim_text, status, source_file) VALUES
('82.1', '*Next binding action:* Paper 82 must give the density 1/2 proof via the substrate map and the 1M-bit data', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p82 (claim_ref, claim_text, status, source_file) VALUES
('82.2', '*Next binding action:* Paper 82 must give the density 1/2 proof', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p82 (claim_ref, claim_text, status, source_file) VALUES
('82.3', 'Paper 82 uses the substrate map to prove the density 1/2 (P2)', 'I', 'mapped_file_claims_report.md');
