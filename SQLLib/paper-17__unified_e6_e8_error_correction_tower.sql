-- ============================================================
-- Paper 17 — Unified E6 E8 Error Correction Tower
-- Domain: Exceptional Tower / Lattice Codes
-- Cross-references: Paper 03 (triality), Paper 08 (lattice closure),
--                   Paper 18 (VOA/moonshine), Paper 91 (Niemeier)
-- ============================================================

-- Table: error_correction_tower
-- Role: Towered lattice transitions: E6 → E7 → E8 → Leech
CREATE TABLE IF NOT EXISTS error_correction_tower (
    tower_level     INTEGER PRIMARY KEY CHECK (tower_level BETWEEN 1 AND 4),
    lattice_name    TEXT NOT NULL,
    dimension       INTEGER NOT NULL,
    min_norm        INTEGER,
    kissing_number  INTEGER,
    theta_series    TEXT,                  -- first few terms
    glue_group      TEXT,
    next_level      INTEGER,
    FOREIGN KEY (next_level) REFERENCES error_correction_tower(tower_level)
);

-- Table: lattice_transitions
-- Role: Explicit transitions between adjacent lattice levels
CREATE TABLE IF NOT EXISTS lattice_transitions (
    transition_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    from_level      INTEGER NOT NULL,
    to_level        INTEGER NOT NULL,
    transition_type TEXT CHECK (transition_type IN ('gluing','quotient','extension','embedding')),
    index_value     INTEGER,               -- index of sublattice
    glue_vectors    TEXT,                  -- JSON array of glue vectors
    FOREIGN KEY (from_level) REFERENCES error_correction_tower(tower_level),
    FOREIGN KEY (to_level) REFERENCES error_correction_tower(tower_level)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_tower_level ON error_correction_tower(tower_level);
CREATE INDEX IF NOT EXISTS idx_trans_from  ON lattice_transitions(from_level);

-- Seed data: tower levels
INSERT INTO error_correction_tower (tower_level, lattice_name, dimension, min_norm, kissing_number, theta_series, glue_group, next_level) VALUES
(1, 'E6*',  6,  4, 72,  '1 + 72q^2 + ...', 'Z3', 2),
(2, 'E7*',  7,  3, 126, '1 + 126q^2 + ...', 'Z2', 3),
(3, 'E8',   8,  2, 240, '1 + 240q^2 + ...', 'trivial', 4),
(4, 'Leech', 24, 4, 196560, '1 + 196560q^4 + ...', 'trivial', NULL);
