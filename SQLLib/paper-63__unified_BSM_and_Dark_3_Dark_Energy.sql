-- ============================================================
-- Paper 63 — Unified BSM And Dark 3 Dark Energy
-- Domain: Dark Energy / Cosmological Constant
-- Cross-references: Paper 62 (dark matter), Paper 64 (inflation),
--                   Paper 67-68 (cosmology)
-- ============================================================

-- Table: dark_energy
-- Role: Dark energy as cosmological constant = vacuum repair curvature
CREATE TABLE IF NOT EXISTS dark_energy (
    de_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name      TEXT NOT NULL,
    cosmological_constant REAL,            -- Λ in GeV^4
    vacuum_repair_curvature REAL,
    equation_of_state_w REAL,
    density_fraction REAL                  -- Ω_Λ
);

-- Seed data: dark energy (ΛCDM)
INSERT INTO dark_energy (model_name, cosmological_constant, vacuum_repair_curvature, equation_of_state_w, density_fraction) VALUES
('ΛCDM', 1.1e-47, 0.0, -1.0, 0.684);

-- Merged from paper-063__unified_claims.sql
-- paper-063 SQL Claim Ledger

CREATE TABLE IF NOT EXISTS claims_063 (
    claim_id TEXT PRIMARY KEY,
    claim_text TEXT,
    tag TEXT,
    source_file TEXT,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO claims_063 (claim_id, claim_text, tag, source_file) VALUES ('63.1', 'Hyperpermutation = meta-permutation of Supervisor Cursor''s tile ribbon', 'D', 'CQE-PAPER-063.md');
INSERT INTO claims_063 (claim_id, claim_text, tag, source_file) VALUES ('63.2', '6 logical dependencies between preconditions', 'D', 'CQE-PAPER-063.md');
INSERT INTO claims_063 (claim_id, claim_text, tag, source_file) VALUES ('63.3', 'Fixed point at void boundary = tile self-recognition', 'D', 'CQE-PAPER-063.md');
INSERT INTO claims_063 (claim_id, claim_text, tag, source_file) VALUES ('63.4', 'Hyperpermutation = context-bounded superpermutation hypervising corpus tile self-reading', 'D', 'CQE-PAPER-063.md');
INSERT INTO claims_063 (claim_id, claim_text, tag, source_file) VALUES ('63.5', 'Hyperpermutation = meta-permutation - 6 dependencies - Fixed point = self-recognition', 'I', 'PAPER-063-TILE-INTEGRATION.md');
INSERT INTO claims_063 (claim_id, claim_text, tag, source_file) VALUES ('63.6', 'SpectreTile IRL Alignment: 14 edges, aperiodic, chiral', 'X', 'PAPER-063-TILE-INTEGRATION.md');
