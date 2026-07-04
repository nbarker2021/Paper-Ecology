-- ============================================================
-- Paper 42 — Unified SU3 Generation 2 Strange Charm
-- Domain: SU(3) Gen 2 / Charm, Strange (already in gen1), etc.
-- Cross-references: Paper 41 (gen1), Paper 43 (gen3)
-- ============================================================

-- Table: su3_generation_2
-- Role: Charm, strange quarks as D4 axis/sheet states
CREATE TABLE IF NOT EXISTS su3_generation_2 (
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

-- Seed data: Generation 2 quarks
INSERT INTO su3_generation_2 (quark_id, quark_name, flavor, charge, mass_mev, axis_class, sheet, color_state, voa_weight) VALUES
(1, 'charm',   'charm',   2.0/3,  1275.0, 2, 1, 'anti-red',   2),
(2, 'strange', 'strange', -1.0/3, 96.0,   2, 0, 'blue',       2);

-- Mapped claims extraction

-- Table: mapped_claims_42
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (42, 1, 'TarpitTile, SpectreTile (14 edges), KnightCATile - Shear ∝ κ - Pinch ∝ κ - 7 substitution paths = 7 modes - Knight CA = 8 states', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (42, 2, 'Shear & Pinch Deformation Modes — Tile Bond Stress', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (42, 3, 'Tarpit Tile Computer (40-43)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (42, 4, 'Shear & pinch = two fundamental tile bond deformation modes', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
