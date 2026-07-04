-- ============================================================
-- Paper 35 — Unified Electron Hole Exciton Accounting
-- Domain: Semiconductors / Carrier-Boundary-Repair Triad
-- Cross-references: Paper 32 (electron-hole), Paper 36 (metamaterials),
--                   Paper 97 (EHX open math)
-- ============================================================

-- Table: ehx_accounting
-- Role: Electron-hole-exciton accounting tables.
--       Electron = carrier, Hole = boundary, Exciton = repair.
CREATE TABLE IF NOT EXISTS ehx_accounting (
    ehx_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_type     TEXT NOT NULL CHECK (entity_type IN ('electron','hole','exciton')),
    state_id        INTEGER,               -- LCR state mapping
    energy_ev       REAL,
    mobility        REAL,
    lifetime_ps     REAL,
    paper_ref       INTEGER DEFAULT 35
);

-- Table: semiconductor_mappings
-- Role: FLCR substrate mappings for semiconductor physics
CREATE TABLE IF NOT EXISTS semiconductor_mappings (
    mapping_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    physics_concept TEXT NOT NULL,
    flcr_entity     TEXT NOT NULL,
    flcr_type       TEXT CHECK (flcr_type IN ('carrier','boundary','repair'))
);

-- Seed data: semiconductor mappings
INSERT INTO semiconductor_mappings (physics_concept, flcr_entity, flcr_type) VALUES
('electron', 'carrier', 'carrier'),
('hole', 'boundary', 'boundary'),
('exciton', 'repair', 'repair'),
('dislocation', 'repair', 'repair'),
('defect', 'boundary', 'boundary'),
('phonon', 'carrier', 'carrier');
