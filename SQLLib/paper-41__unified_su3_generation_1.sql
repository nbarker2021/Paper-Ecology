-- ============================================================
-- Paper 41 — Unified Su3 Generation 1
-- Domain: SU(3) Gen 1 / Up, Down, Strange
-- Cross-references: Paper 13 (quark faces), Paper 42-43 (other gens)
-- ============================================================

-- Table: su3_generation_1
-- Role: Up, down, strange quarks as D4 axis/sheet states
CREATE TABLE IF NOT EXISTS su3_generation_1 (
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

-- Seed data: Generation 1 quarks
INSERT INTO su3_generation_1 (quark_id, quark_name, flavor, charge, mass_mev, axis_class, sheet, color_state, voa_weight) VALUES
(1, 'up',      'up',      2.0/3,  2.2,   1, 0, 'red',   1),
(2, 'down',    'down',   -1.0/3,  4.7,   1, 1, 'green', 1),
(3, 'strange', 'strange', -1.0/3, 96.0,  2, 0, 'blue',  2);

-- Mapped claims extraction

-- Table: mapped_claims_41
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (41, 1, 'Tarpit Mass = Bonded Tile Interactions', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (41, 2, 'Tarpit Tile Computer (40-43)', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (41, 3, 'Tarpit mass = bonded tile interactions × κ = deformation energy of tile cluster', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
