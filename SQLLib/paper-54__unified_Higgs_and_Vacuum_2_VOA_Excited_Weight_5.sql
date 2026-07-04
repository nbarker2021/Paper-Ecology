-- ============================================================
-- Paper 54 — Unified Higgs And Vacuum 2 VOA Excited Weight 5
-- Domain: VOA Weight 5 / Higgs Identification
-- Cross-references: Paper 15 (mass residue), Paper 53 (Higgs mechanism),
--                   Paper 18 (moonshine)
-- ============================================================

-- Table: voa_excited_weight_5
-- Role: Higgs boson identified with VOA excited weight 5.
--       Mass = 5 × κ = 125.25 GeV.
CREATE TABLE IF NOT EXISTS voa_excited_weight_5 (
    state_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    particle_name   TEXT NOT NULL DEFAULT 'Higgs boson',
    voa_weight      INTEGER NOT NULL DEFAULT 5,
    mass_formula    TEXT NOT NULL DEFAULT '5 * κ',
    mass_gev        REAL NOT NULL DEFAULT 125.25,
    voa_module      TEXT,                  -- which VOA module
    monster_coeff_link INTEGER,            -- linked Monster coefficient
    structural_derived INTEGER DEFAULT 1
);

-- Table: voa_weight_ladder
-- Role: Full VOA weight ladder for SM particles
CREATE TABLE IF NOT EXISTS voa_weight_ladder (
    ladder_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    voa_weight      INTEGER NOT NULL,
    particle_name   TEXT,
    mass_gev        REAL,
    mass_formula    TEXT
);

-- Seed data: VOA excited weight 5 = Higgs
INSERT INTO voa_excited_weight_5 (particle_name, voa_weight, mass_formula, mass_gev, voa_module, monster_coeff_link) VALUES
('Higgs boson', 5, '5 * κ', 125.25, 'Monster_VOA_weight_5', 196883);

-- Seed data: VOA weight ladder
INSERT INTO voa_weight_ladder (voa_weight, particle_name, mass_gev, mass_formula) VALUES
(0, 'Photon',     0.0,      '0 * κ'),
(1, 'Electron',   0.000511, '2e-5 * κ'),
(2, 'Muon',       0.1057,   '0.004 * κ'),
(3, 'W boson',    80.38,    '3.2 * κ'),
(4, 'Z boson',    91.19,    '3.6 * κ'),
(5, 'Higgs',      125.25,   '5 * κ'),
(6, 'Tau',        1.777,    '0.07 * κ'),
(7, 'Top quark',  173.1,    '6.9 * κ');

-- Mapped claims extraction

-- Table: mapped_claims_54
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (54, 1, '**FILE:** `paper_54.md`', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (54, 2, '**TITLE:** Paper 54 — Higgs and Vacuum 2: VOA Excited Weight 5 = Higgs', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (54, 3, '**SUMMARY:** Higgs and vacuum 2: VOA excited weight 5 = Higgs', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
