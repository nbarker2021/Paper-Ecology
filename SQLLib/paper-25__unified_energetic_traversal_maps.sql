-- ============================================================
-- Paper 25 — Unified Energetic Traversal Maps
-- Domain: Energy Landscapes / Activation Barriers
-- Cross-references: Paper 05 (oloid carrier), Paper 22 (materials),
--                   Paper 26 (z-pinch), Paper 35 (plasma)
-- ============================================================

-- Table: energetic_traversal_maps
-- Role: Energy landscape as lattice, activation energy as repair curvature
CREATE TABLE IF NOT EXISTS energetic_traversal_maps (
    map_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    map_name        TEXT NOT NULL,
    landscape_type  TEXT NOT NULL,         -- e.g., 'crystal', 'protein', 'plasma'
    state_count     INTEGER,
    activation_energy REAL,                -- repair curvature at barrier
    min_energy      REAL,
    max_energy      REAL,
    forge_id        INTEGER,
    FOREIGN KEY (forge_id) REFERENCES forge_systems(forge_id)
);

-- Table: activation_barriers
-- Role: Activation barriers as typed boundaries with repair curvature
CREATE TABLE IF NOT EXISTS activation_barriers (
    barrier_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    map_id          INTEGER NOT NULL,
    from_state      TEXT NOT NULL,
    to_state        TEXT NOT NULL,
    barrier_height  REAL NOT NULL,         -- activation energy
    curvature_k     REAL,                  -- repair curvature
    barrier_type    TEXT CHECK (barrier_type IN ('type_preserving','arf_matching','curvature_driven')),
    FOREIGN KEY (map_id) REFERENCES energetic_traversal_maps(map_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_etm_type ON energetic_traversal_maps(landscape_type);
CREATE INDEX IF NOT EXISTS idx_barrier_map ON activation_barriers(map_id);
