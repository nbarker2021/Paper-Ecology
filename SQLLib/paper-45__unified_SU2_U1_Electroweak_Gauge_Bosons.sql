-- ============================================================
-- Paper 45 — Unified SU2 U1 Electroweak Gauge Bosons
-- Domain: Gauge Bosons / Electroweak
-- Cross-references: Paper 33 (electroweak), Paper 46-48 (EW sector)
-- ============================================================

-- Table: electroweak_gauge_bosons
-- Role: W/Z as D4 sheets, photon as vacuum, weak mixing as D12 action
CREATE TABLE IF NOT EXISTS electroweak_gauge_bosons (
    boson_id        INTEGER PRIMARY KEY,
    boson_name      TEXT NOT NULL,
    symbol          TEXT NOT NULL,
    charge          REAL,
    mass_gev        REAL,
    d4_sheet        INTEGER,
    d12_action_index INTEGER,
    is_vacuum       INTEGER DEFAULT 0 CHECK (is_vacuum IN (0,1)),
    voa_weight      INTEGER
);

-- Seed data: electroweak gauge bosons
INSERT INTO electroweak_gauge_bosons (boson_id, boson_name, symbol, charge, mass_gev, d4_sheet, d12_action_index, is_vacuum, voa_weight) VALUES
(1, 'Photon',    'γ',   0,   0.0,   NULL, NULL, 1, 0),
(2, 'W boson +', 'W+', +1,  80.38, 0,    1,    0, 3),
(3, 'W boson -', 'W-', -1,  80.38, 1,    1,    0, 3),
(4, 'Z boson',   'Z0',  0,  91.19, NULL, 2,    0, 4);
