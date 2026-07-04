-- ============================================================
-- Paper 05 — Unified Oloid Path Carrier
-- Domain: Carrier Geometry / Deterministic Transducer
-- Cross-references: Paper 01 (LCR states), Paper 06 (causal links),
--                   Paper 25 (energetic traversal)
-- ============================================================

-- Table: rolling_carrier_states
-- Role: 8-segment LCR-parameterized oloid path states.
--       Each state is a position on the rolling carrier.
CREATE TABLE IF NOT EXISTS rolling_carrier_states (
    segment_id      INTEGER PRIMARY KEY CHECK (segment_id BETWEEN 0 AND 7),
    segment_name    TEXT NOT NULL,
    lcr_parameter   TEXT NOT NULL,         -- e.g., "L->C"
    path_coord_x    REAL,
    path_coord_y    REAL,
    path_coord_z    REAL,
    curvature_k     REAL,                  -- local repair curvature
    is_geodesic     INTEGER NOT NULL DEFAULT 1 CHECK (is_geodesic IN (0,1))
);

-- Table: carrier_traces
-- Role: Trace of carrier movement across the lattice (graph-continuous)
CREATE TABLE IF NOT EXISTS carrier_traces (
    trace_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    segment_id      INTEGER NOT NULL,
    from_state      INTEGER NOT NULL,
    to_state        INTEGER NOT NULL,
    action_value    REAL,                  -- S = -m∫ds
    payload_hash    TEXT,                  -- non-interfering payload
    trace_length    REAL,
    FOREIGN KEY (segment_id) REFERENCES rolling_carrier_states(segment_id),
    FOREIGN KEY (from_state) REFERENCES lcr_states(state_id),
    FOREIGN KEY (to_state)   REFERENCES lcr_states(state_id)
);

-- Table: oloid_parameters
-- Role: Geometric parameters of the oloid (two interlocking circles)
CREATE TABLE IF NOT EXISTS oloid_parameters (
    param_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    param_name      TEXT NOT NULL,
    param_value     REAL NOT NULL,
    unit            TEXT
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_trace_segment ON carrier_traces(segment_id);
CREATE INDEX IF NOT EXISTS idx_trace_from    ON carrier_traces(from_state);

-- Seed data: 8 oloid segments
INSERT INTO rolling_carrier_states (segment_id, segment_name, lcr_parameter, path_coord_x, path_coord_y, path_coord_z, curvature_k, is_geodesic) VALUES
(0, 'Origin',      '∅',      0.0,  0.0, 0.0, 0.0, 1),
(1, 'Left Arc',    'L',      1.0,  0.0, 0.0, 0.1, 1),
(2, 'Center Arc',  'C',      0.0,  1.0, 0.0, 0.1, 1),
(3, 'Right Arc',   'R',      0.0,  0.0, 1.0, 0.1, 1),
(4, 'LC Bridge',   'LC',     1.0,  1.0, 0.0, 0.2, 1),
(5, 'LR Bridge',   'LR',     1.0,  0.0, 1.0, 0.2, 1),
(6, 'CR Bridge',   'CR',     0.0,  1.0, 1.0, 0.2, 1),
(7, 'LCR Closure', 'LCR',    1.0,  1.0, 1.0, 0.0, 1);

-- Seed data: oloid geometric parameters
INSERT INTO oloid_parameters (param_name, param_value, unit) VALUES
('circle_radius', 1.0, 'unit'),
('circle_separation', 1.0, 'unit'),
('surface_area', 4.0, 'unit^2'),
('volume', 2.0, 'unit^3');


-- ---------------------------------------------------------------------------
-- AGRM Hierarchy Tables (harvested from 53e25b8d_AGRM_refactored.py, 2026-07-04)
-- ---------------------------------------------------------------------------

-- Table: agrm_hierarchy_config
-- Role: Configuration snapshot for AGRM hierarchy controller.
CREATE TABLE IF NOT EXISTS agrm_hierarchy_config (
    config_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    phi_scale       REAL NOT NULL DEFAULT 1.618033988749895,
    target_load     REAL NOT NULL DEFAULT 0.70,
    floors_per_building INTEGER NOT NULL DEFAULT 3,
    rooms_per_floor INTEGER NOT NULL DEFAULT 64,
    promote_hits    INTEGER NOT NULL DEFAULT 8,
    demote_after_idle INTEGER NOT NULL DEFAULT 10,
    decay_rate      REAL NOT NULL DEFAULT 0.85,
    enable_shortcuts INTEGER NOT NULL DEFAULT 1,
    resize_policy   TEXT NOT NULL DEFAULT 'phi',
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: mdhg_entries
-- Role: Individual entries in the MDHG hash table with hierarchical location.
CREATE TABLE IF NOT EXISTS mdhg_entries (
    entry_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    key_hash        TEXT NOT NULL,
    key_text        TEXT,
    value_json      TEXT,
    building_id     INTEGER NOT NULL DEFAULT 0,
    floor_id        INTEGER NOT NULL DEFAULT 0,
    room_id         INTEGER NOT NULL DEFAULT 0,
    hits            INTEGER NOT NULL DEFAULT 0,
    last_touch      INTEGER NOT NULL DEFAULT 0,
    inserted_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: mdhg_shortcuts
-- Role: Co-visit routing shortcuts between rooms.
CREATE TABLE IF NOT EXISTS mdhg_shortcuts (
    shortcut_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    source_room     INTEGER NOT NULL,
    dest_room       INTEGER NOT NULL,
    visit_count     INTEGER NOT NULL DEFAULT 1,
    building_id     INTEGER NOT NULL DEFAULT 0,
    UNIQUE(source_room, dest_room, building_id)
);

-- Table: agrm_sweep_metrics
-- Role: Per-sweep metrics for adaptive threshold tuning.
CREATE TABLE IF NOT EXISTS agrm_sweep_metrics (
    sweep_id        INTEGER PRIMARY KEY,
    size            INTEGER NOT NULL DEFAULT 0,
    load            REAL NOT NULL DEFAULT 0.0,
    promotions      INTEGER NOT NULL DEFAULT 0,
    demotions       INTEGER NOT NULL DEFAULT 0,
    moves           INTEGER NOT NULL DEFAULT 0,
    lookups         INTEGER NOT NULL DEFAULT 0,
    shortcut_hits   INTEGER NOT NULL DEFAULT 0,
    shortcut_misses INTEGER NOT NULL DEFAULT 0,
    mean_hits       REAL NOT NULL DEFAULT 0.0,
    median_hits     REAL NOT NULL DEFAULT 0.0,
    p90_hits        REAL NOT NULL DEFAULT 0.0,
    recorded_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: agrm_trace_buffer
-- Role: Bounded trace buffer events from MDHG operations.
CREATE TABLE IF NOT EXISTS agrm_trace_buffer (
    trace_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type      TEXT NOT NULL,
    key_hash        TEXT,
    building_id     INTEGER,
    floor_id        INTEGER,
    room_id         INTEGER,
    size_after      INTEGER,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_mdhg_entry_key ON mdhg_entries(key_hash);
CREATE INDEX IF NOT EXISTS idx_mdhg_entry_location ON mdhg_entries(building_id, floor_id, room_id);
CREATE INDEX IF NOT EXISTS idx_shortcuts_source ON mdhg_shortcuts(source_room);
CREATE INDEX IF NOT EXISTS idx_sweep_metrics_id ON agrm_sweep_metrics(sweep_id);
