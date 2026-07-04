-- ============================================================
-- Paper 49 — Unified Mass And Yukawa 1 Mass Hierarchy
-- Domain: Mass Hierarchy / VOA Weight Ladder
-- Cross-references: Paper 15 (mass residue), Paper 50-52 (Yukawa)
-- ============================================================

-- Table: mass_hierarchy
-- Role: Fermion mass hierarchy as VOA weight ladder
CREATE TABLE IF NOT EXISTS mass_hierarchy (
    hierarchy_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    particle_name   TEXT NOT NULL,
    generation      INTEGER NOT NULL,
    voa_weight      INTEGER NOT NULL,
    mass_gev        REAL,
    mass_ratio_up   REAL,                  -- ratio to up quark mass
    hierarchy_rank  INTEGER
);

-- Seed data: fermion mass hierarchy
INSERT INTO mass_hierarchy (particle_name, generation, voa_weight, mass_gev, mass_ratio_up, hierarchy_rank) VALUES
('electron',    1, 1, 0.000511, 0.000232, 1),
('up quark',    1, 1, 2.2,      1.0,      2),
('down quark',  1, 1, 4.7,      2.14,     3),
('muon',        2, 2, 105.7,    48.0,     4),
('strange',     2, 2, 96.0,     43.6,     5),
('charm',       2, 2, 1275.0,   579.5,    6),
('tau',         3, 3, 1777.0,   807.7,    7),
('bottom',      3, 3, 4180.0,   1900.0,   8),
('top',         3, 3, 173100.0, 78681.8,  9);

-- Mapped claims extraction

-- Table: mapped_claims_49
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (49, 1, '**FILE:** `paper_49.md`', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (49, 2, '**TITLE:** Paper 49 — Mass and Yukawa 1: Mass Hierarchy', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (49, 3, '**SUMMARY:** Mass and Yukawa 1: the mass hierarchy', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (49, 4, '26 | Positive Grassmannian bridge as part of recognized positive geometry program | Paper 101__ | §2 (literature context)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (49, 5, '27 | Albert algebra mass predictions: reconcile FLCR VOA weights with Singh eigenvalues | Papers 4/14/16/102__ | §3 (external calibration)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (49, 6, '28 | LZ 2025 dark matter limits as external calibration for Gap 8 | Papers 67–68 / Paper 100 | §5 (dark matter external calibration)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (49, 7, '29 | QCT decoder + SNAQ spin qubits as QEC benchmarks | Paper 17 | New §"External QEC Calibration"', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (49, 8, '30 | CKM CAA as calibration target: predict Δ = | Vud | ²+', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
