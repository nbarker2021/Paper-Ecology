-- ============================================================
-- Paper 50 — Unified Mass And Yukawa 2 CKM PMNS
-- Domain: CKM/PMNS Matrices / D12 Action
-- Cross-references: Paper 49 (mass hierarchy), Paper 51-52 (Yukawa),
--                   Paper 41-43 (SU3 generations)
-- ============================================================

-- Table: ckm_matrix
-- Role: CKM quark mixing matrix derived from D12 action.
--       Rows: up, charm, top. Columns: down, strange, bottom.
CREATE TABLE IF NOT EXISTS ckm_matrix (
    ckm_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    row_quark       TEXT NOT NULL CHECK (row_quark IN ('up','charm','top')),
    col_quark       TEXT NOT NULL CHECK (col_quark IN ('down','strange','bottom')),
    amplitude       REAL NOT NULL,         -- |V_ij|
    amplitude_err   REAL,                  -- uncertainty
    phase_rad       REAL,                  -- CP-violating phase contribution
    d12_action_index INTEGER,              -- which D12 element generates this
    derived_from    TEXT DEFAULT 'D12_action'
);

-- Table: pmns_matrix
-- Role: PMNS lepton mixing matrix derived from D12 action.
--       Rows: e, μ, τ. Columns: ν1, ν2, ν3.
CREATE TABLE IF NOT EXISTS pmns_matrix (
    pmns_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    row_lepton      TEXT NOT NULL CHECK (row_lepton IN ('e','mu','tau')),
    col_neutrino    TEXT NOT NULL CHECK (col_neutrino IN ('nu1','nu2','nu3')),
    amplitude       REAL NOT NULL,
    amplitude_err   REAL,
    phase_rad       REAL,
    d12_action_index INTEGER,
    derived_from    TEXT DEFAULT 'D12_action'
);

-- Table: mixing_angles
-- Role: CKM and PMNS mixing angles
CREATE TABLE IF NOT EXISTS mixing_angles (
    angle_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    matrix_type     TEXT NOT NULL CHECK (matrix_type IN ('CKM','PMNS')),
    angle_name      TEXT NOT NULL,
    angle_value_rad REAL,
    angle_value_deg REAL,
    sin_value       REAL,
    cos_value       REAL
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_ckm_row ON ckm_matrix(row_quark);
CREATE INDEX IF NOT EXISTS idx_ckm_col ON ckm_matrix(col_quark);
CREATE INDEX IF NOT EXISTS idx_pmns_row ON pmns_matrix(row_lepton);
CREATE INDEX IF NOT EXISTS idx_pmns_col ON pmns_matrix(col_neutrino);

-- Seed data: CKM matrix (PDG 2024 central values)
INSERT INTO ckm_matrix (row_quark, col_quark, amplitude, amplitude_err, phase_rad, d12_action_index) VALUES
('up',    'down',     0.97435, 0.00016, 0.0, 1),
('up',    'strange',  0.22500, 0.00070, 0.0, 2),
('up',    'bottom',   0.00369, 0.00011, 0.0, 3),
('charm', 'down',     0.22486, 0.00067, 0.0, 4),
('charm', 'strange',  0.97349, 0.00016, 0.0, 5),
('charm', 'bottom',   0.04182, 0.00075, 0.0, 6),
('top',   'down',     0.00857, 0.00024, 0.0, 7),
('top',   'strange',  0.04079, 0.00110, 0.0, 8),
('top',   'bottom',   0.999118,0.000031,0.0, 9);

-- Seed data: PMNS matrix (approximate)
INSERT INTO pmns_matrix (row_lepton, col_neutrino, amplitude, phase_rad, d12_action_index) VALUES
('e',   'nu1', 0.82, 0.0, 1),
('e',   'nu2', 0.55, 0.0, 2),
('e',   'nu3', 0.15, 0.0, 3),
('mu',  'nu1', 0.36, 0.0, 4),
('mu',  'nu2', 0.60, 0.0, 5),
('mu',  'nu3', 0.71, 0.0, 6),
('tau', 'nu1', 0.44, 0.0, 7),
('tau', 'nu2', 0.58, 0.0, 8),
('tau', 'nu3', 0.69, 0.0, 9);

-- Seed data: mixing angles
INSERT INTO mixing_angles (matrix_type, angle_name, angle_value_rad, angle_value_deg, sin_value, cos_value) VALUES
('CKM', 'theta12', 0.227, 13.02, 0.225, 0.974),
('CKM', 'theta23', 0.042, 2.41,  0.042, 0.999),
('CKM', 'theta13', 0.00369, 0.211, 0.00369, 1.0),
('PMNS', 'theta12', 0.59, 33.8, 0.55, 0.83),
('PMNS', 'theta23', 0.86, 49.3, 0.75, 0.66),
('PMNS', 'theta13', 0.15, 8.6,  0.15, 0.99);

-- Mapped claims extraction

-- Table: mapped_claims_50
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (50, 1, 'SpectreTile (4-fold Z4), HatTile - Observer = Face Selection F - Z4: 2 fixed, 0 period-2, 6 period-4 - 7 latent faces retained', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (50, 2, 'Observer Frame = D4 Face Selection — Tile 4-Fold Z4 Symmetry', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (50, 3, 'Observer Physics (50-53)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (50, 4, 'Observer = selection of 1 D4 face from spectre tile''s 4-fold Z4 symmetry', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
