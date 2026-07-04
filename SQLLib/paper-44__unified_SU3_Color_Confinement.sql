-- ============================================================
-- Paper 44 — Unified SU3 Color Confinement
-- Domain: Color Confinement / Boundary Repair
-- Cross-references: Paper 13 (quark faces), Paper 41-43 (quark gens),
--                   Paper 57-60 (QCD phenomenology)
-- ============================================================

-- Table: color_confinement
-- Role: Confinement as boundary repair, gluons as repair carriers,
--       hadron as closed boundary.
CREATE TABLE IF NOT EXISTS color_confinement (
    confinement_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    quark_set       TEXT NOT NULL,         -- JSON array of quark names
    gluon_carrier   TEXT NOT NULL,         -- which gluon mediates
    hadron_result   TEXT NOT NULL,         -- resulting hadron
    boundary_closed INTEGER NOT NULL DEFAULT 1 CHECK (boundary_closed IN (0,1)),
    color_neutral   INTEGER NOT NULL DEFAULT 1 CHECK (color_neutral IN (0,1))
);

-- Table: gluon_repair_carriers
-- Role: 8 gluons = 8 SU(3) roots = repair carriers
CREATE TABLE IF NOT EXISTS gluon_repair_carriers (
    gluon_id        INTEGER PRIMARY KEY CHECK (gluon_id BETWEEN 1 AND 8),
    gluon_name      TEXT NOT NULL,
    root_index      INTEGER,
    color_transition TEXT,                 -- e.g., 'red→green'
    repair_type     TEXT DEFAULT 'color_exchange'
);

-- Seed data: gluon repair carriers
INSERT INTO gluon_repair_carriers (gluon_id, gluon_name, root_index, color_transition) VALUES
(1, 'g_1', 1, 'red ↔ green'),
(2, 'g_2', 2, 'red ↔ blue'),
(3, 'g_3', 3, 'green ↔ blue'),
(4, 'g_4', 4, 'red ↔ anti-green'),
(5, 'g_5', 5, 'green ↔ anti-red'),
(6, 'g_6', 6, 'blue ↔ anti-red'),
(7, 'g_7', 7, 'red ↔ anti-red'),
(8, 'g_8', 8, 'color-neutral');

-- Seed data: sample confinement processes
INSERT INTO color_confinement (quark_set, gluon_carrier, hadron_result, boundary_closed, color_neutral) VALUES
('["up","anti-up"]',   'g_7', 'pion0',  1, 1),
('["up","down"]',      'g_1', 'proton', 1, 1),
('["down","anti-up"]', 'g_1', 'pion+',  1, 1);

-- Mapped claims extraction

-- Table: mapped_claims_44
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
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (44, 1, '**FILE:** `paper_44.md`', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (44, 2, '**TITLE:** Paper 44 — Electroweak Gauge Bosons: W/Z as D4 Sheets, Photon as Vacuum, Weak Mixing as D12 Action', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (44, 3, '**SUMMARY:** Electroweak gauge bosons: W/Z as D4 sheets, photon as vacuum, weak mixing as D12 action', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
