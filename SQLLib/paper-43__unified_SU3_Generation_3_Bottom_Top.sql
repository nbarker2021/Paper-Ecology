-- ============================================================
-- Paper 43 — Unified SU3 Generation 3 Bottom Top
-- Domain: SU(3) Gen 3 / Bottom, Top
-- Cross-references: Paper 41-42 (gen1-2)
-- ============================================================

-- Table: su3_generation_3
-- Role: Bottom, top quarks as D4 axis/sheet states
CREATE TABLE IF NOT EXISTS su3_generation_3 (
    quark_id        INTEGER PRIMARY KEY,
    quark_name      TEXT NOT NULL,
    flavor          TEXT NOT NULL,
    charge          REAL NOT NULL,
    mass_mev        REAL,
    axis_class      INTEGER,
    sheet           INTEGER,
    color_state     TEXT,
    voa_weight      INTEGER
);

-- Seed data: Generation 3 quarks
INSERT INTO su3_generation_3 (quark_id, quark_name, flavor, charge, mass_mev, axis_class, sheet, color_state, voa_weight) VALUES
(1, 'bottom', 'bottom', -1.0/3, 4180.0, 3, 0, 'anti-green', 3),
(2, 'top',    'top',     2.0/3, 173100.0, 3, 1, 'anti-blue', 3);

-- Mapped claims extraction

-- Table: mapped_claims_43
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (43, 1, 'KnightCATile, TarpitTile, SpectreTile - OEIS A033996 = Knight moves - 8 states = 8 chart states - Calibration = state verification', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (43, 2, 'Knight CA Calibration — Tile Computer Empirical Verification', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (43, 3, 'Tarpit Tile Computer (40-43)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (43, 4, 'Knight CA on 3×3 = empirical verification of tile computer via OEIS A033996', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
