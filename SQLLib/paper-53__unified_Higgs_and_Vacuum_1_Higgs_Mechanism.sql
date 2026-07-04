-- ============================================================
-- Paper 53 — Unified Higgs And Vacuum 1 Higgs Mechanism
-- Domain: Higgs Mechanism / Boundary Repair
-- Cross-references: Paper 15 (mass residue), Paper 46 (symmetry breaking),
--                   Paper 54-56 (Higgs and vacuum)
-- ============================================================

-- Table: higgs_mechanism
-- Role: Higgs mechanism as boundary repair giving masses to W/Z
CREATE TABLE IF NOT EXISTS higgs_mechanism (
    mechanism_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    process_name    TEXT NOT NULL,
    gauge_boson     TEXT NOT NULL,
    symmetry_broken TEXT NOT NULL,
    repair_curvature REAL,                 -- Higgs field as repair curvature
    generated_mass  REAL,                  -- GeV
    voa_weight      INTEGER DEFAULT 5,
    status          TEXT DEFAULT 'verified'
);

-- Table: vacuum_states
-- Role: Vacuum states and their repair status
CREATE TABLE IF NOT EXISTS vacuum_states (
    vacuum_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    vacuum_name     TEXT NOT NULL,
    vev_gev         REAL,
    repair_complete INTEGER NOT NULL DEFAULT 1 CHECK (repair_complete IN (0,1)),
    is_stable       INTEGER DEFAULT 1
);

-- Seed data: Higgs mechanism processes
INSERT INTO higgs_mechanism (process_name, gauge_boson, symmetry_broken, generated_mass, voa_weight) VALUES
('W mass generation', 'W+', 'SU(2)_L × U(1)_Y → U(1)_EM', 80.38, 5),
('W mass generation', 'W-', 'SU(2)_L × U(1)_Y → U(1)_EM', 80.38, 5),
('Z mass generation', 'Z0', 'SU(2)_L × U(1)_Y → U(1)_EM', 91.19, 5);

-- Seed data: vacuum states
INSERT INTO vacuum_states (vacuum_name, vev_gev, repair_complete, is_stable) VALUES
('Electroweak vacuum', 246.0, 1, 1),
('Symmetric vacuum',   0.0,   0, 0);

-- Mapped claims extraction

-- Table: mapped_claims_53
CREATE TABLE IF NOT EXISTS mapped_claims (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_num INTEGER NOT NULL,
    claim_seq INTEGER NOT NULL,
    claim_text TEXT NOT NULL,
    claim_tag TEXT DEFAULT 'D',
    source_file TEXT,
    extraction_date TEXT
);

-- Mapped claims extraction
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (53, 1, 'SpectreTile (Z4 faces), HatTile, CrystalTile - Measurement = Face Selection - 1 selected / 7 latent - Lossless = no information loss', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (53, 2, 'Measurement = D4 Face Selection — Tile Observer Event', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (53, 3, 'Observer Physics (50-53)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (53, 4, 'Quantum measurement IS the observer''s selection of 1 of 4 D4 faces on spectre tile', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (53, 5, 'The operator encodes the frame selection F = D₄ face choice (Paper 053''s chiral doublet → observer frame)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
