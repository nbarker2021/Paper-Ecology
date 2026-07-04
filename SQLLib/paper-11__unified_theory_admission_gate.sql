-- ============================================================
-- Paper 11 — Unified Theory Admission Gate
-- Domain: Admission Logic / 5-Component Admissibility
-- Cross-references: Paper 10 (receipt), Paper 12 (CA prediction),
--                   Paper 39 (standards), Paper 78 (governance)
-- ============================================================

-- Table: admission_gates
-- Role: Theory admission gates with 5 components:
--       (object, lane, evidence, residue, falsifier)
CREATE TABLE IF NOT EXISTS admission_gates (
    gate_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    gate_name       TEXT NOT NULL,
    object_ref      TEXT NOT NULL,         -- what is being admitted
    lane_id         INTEGER NOT NULL,
    evidence_id     INTEGER,
    residue_desc    TEXT,
    falsifier_id    INTEGER,
    admissible      INTEGER NOT NULL DEFAULT 0 CHECK (admissible IN (0,1)),
    encoder_used    TEXT,                  -- encoder choice for invariance test
    FOREIGN KEY (lane_id) REFERENCES claim_lanes(lane_id)
);

-- Table: admissible_operations
-- Role: The 8 admissible operations in the 2-category ℒ
CREATE TABLE IF NOT EXISTS admissible_operations (
    op_id           INTEGER PRIMARY KEY CHECK (op_id BETWEEN 1 AND 8),
    op_name         TEXT NOT NULL UNIQUE,
    op_symbol       TEXT NOT NULL,
    arity           INTEGER NOT NULL,
    description     TEXT NOT NULL
);

-- Table: sporadic_boundary_routes
-- Role: Exceptional-structure import routes (sporadic boundary)
CREATE TABLE IF NOT EXISTS sporadic_boundary_routes (
    route_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    sporadic_group  TEXT NOT NULL,         -- e.g., 'Monster', 'BabyMonster'
    import_target   TEXT NOT NULL,         -- where it maps into ℒ
    route_status    TEXT NOT NULL DEFAULT 'open' CHECK (route_status IN ('open','verified','blocked')),
    depth_tested    INTEGER DEFAULT 256
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_gate_lane ON admission_gates(lane_id);
CREATE INDEX IF NOT EXISTS idx_gate_adm  ON admission_gates(admissible);

-- Seed data: 8 admissible operations
INSERT INTO admissible_operations (op_id, op_name, op_symbol, arity, description) VALUES
(1, 'Lookup',   'λ', 1, 'Read state from carrier'),
(2, 'Repair',   'ρ', 2, 'Apply boundary repair'),
(3, 'Fold',     'φ', 2, 'Fold two states into one'),
(4, 'Terminal', 'τ', 1, 'Reach terminal address'),
(5, 'Ledger',   'Λ', 2, 'Record obligation'),
(6, 'Window',   'ω', 2, 'Create temporal window'),
(7, 'Bridge',   'β', 2, 'Map discrete to continuous'),
(8, 'Admit',    'α', 1, 'Admit claim through gate');

-- Seed data: sporadic boundary import routes
INSERT INTO sporadic_boundary_routes (sporadic_group, import_target, route_status, depth_tested) VALUES
('Monster',        'VOA_weight_5',  'verified', 256),
('BabyMonster',    'VOA_subVOA',    'open',     128),
('Co1',            'Leech_aut',     'verified', 4096),
('Fi24',           'Monster_nbd',   'open',      64),
('HN',             'Pariah_asym',   'open',      32),
('Th',             'Pariah_asym',   'open',      32);

-- === BATCH GROUP 1 CLAIMS (paper-11) ===
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (11, '11.1', 'κ = ln(φ)/16 ≈ 0.0300757', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (11, '11.2', 'E_tile = 14κ per tile', 'D', '25_Energetic_Traversal_Maps.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (11, '11.3', '3 projections collapse to 1 κ channel', 'D', '25_Energetic_Traversal_Maps.md');
