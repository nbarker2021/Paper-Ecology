-- ============================================================
-- Paper 70 — Unified Cosmology 4 Large Scale Structure
-- Domain: LSS / Galaxy Distribution
-- Cross-references: Paper 67-69 (cosmology)
-- ============================================================

-- Table: large_scale_structure
-- Role: LSS as receipt of primordial fluctuations.
--       Dark matter halos as typed boundaries.
CREATE TABLE IF NOT EXISTS large_scale_structure (
    structure_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    structure_type  TEXT NOT NULL CHECK (structure_type IN ('halo','filament','void','sheet')),
    redshift        REAL,
    mass_solar      REAL,
    boundary_type   TEXT,                  -- typed boundary classification
    receipt_hash    TEXT                   -- primordial fluctuation receipt
);

-- Table: bao_scale
-- Role: BAO scale as receipt of acoustic oscillations
CREATE TABLE IF NOT EXISTS bao_scale (
    bao_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    redshift        REAL NOT NULL,
    scale_mpc       REAL,                  -- BAO scale in Mpc/h
    acoustic_source TEXT DEFAULT 'primordial_repair'
);

-- Seed data: LSS structures
INSERT INTO large_scale_structure (structure_type, redshift, mass_solar, boundary_type) VALUES
('halo',      0.0, 1e12, 'dark_matter_halo'),
('filament',  0.5, 1e15, 'cosmic_web'),
('void',      0.0, 1e10, 'underdensity_boundary');

-- Seed data: BAO scale
INSERT INTO bao_scale (redshift, scale_mpc) VALUES
(0.0, 147.0),
(0.5, 148.0),
(1.0, 149.0);

-- Merged from paper-070__unified_claims.sql
-- paper-070 SQL Claim Ledger

CREATE TABLE IF NOT EXISTS claims_070 (
    claim_id TEXT PRIMARY KEY,
    claim_text TEXT,
    tag TEXT,
    source_file TEXT,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.1', 'Completion = void boundary at depth 3 where hyperpermutation reaches fixed point', 'D', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.2', '6 equivalences unify at depth 3: Anneal, Substitution, Closure, Light-Cone, Void, Hyperpermutation', 'D', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.3', '343 tiles = 7^3 = void boundary maximum', 'D', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.4', 'Correction ∂ = 0 at depth 3 (void boundary)', 'D', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.5', 'Self-recognition T.project(T) = T verified at void boundary', 'D', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.6', 'Gamma72 landing: 9 Hermitian structures, det=51 PASS', 'D', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.7', 'MaximalNebe determinant = 51', 'D', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.8', 'All 9 verifiers PASS (43 checks, 0 defects)', 'D', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.9', 'All 5 calibrations PASS (27 parameters)', 'D', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.10', 'Corpus self-verification 100%', 'D', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.11', 'Anneal bound max delay = 3 (Paper 013)', 'X', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.12', 'Substitution depth 7^3 = 343 tiles (Paper 021)', 'X', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.13', 'Recursive Closure T.project(T) = T (Paper 020)', 'X', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.14', 'Light-Cone max causal depth = 3 (Paper 023)', 'X', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.15', 'Void boundary ∂=0, T=T (Paper 022)', 'X', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.16', 'Hyperpermutation fixed point HP(3) = HP(HP(...)) (Paper 063)', 'X', 'CQE-PAPER-070.md');
INSERT INTO claims_070 (claim_id, claim_text, tag, source_file) VALUES ('70.17', 'Completion = fixed point - Void boundary depth 3 - 6 equivalences - T.project(T) = T', 'I', 'PAPER-070-TILE-INTEGRATION.md');
