-- ============================================================
-- Paper 08 — Unified Lattice Closure
-- Domain: Lattice Theory / 7-Rung Ladder
-- Cross-references: Paper 03 (triality), Paper 07 (bridge),
--                   Paper 17 (E6-E8 tower), Paper 91 (Niemeier glue)
-- ============================================================

-- Table: lattice_closure_ladder
-- Role: The 7-rung ladder: LCR → D4 → J₃(𝕆) → D12 → F4 → E8 → Leech
CREATE TABLE IF NOT EXISTS lattice_closure_ladder (
    rung_id         INTEGER PRIMARY KEY CHECK (rung_id BETWEEN 1 AND 7),
    rung_name       TEXT NOT NULL,
    lattice_code    INTEGER NOT NULL,      -- 1,3,7,8,24,72, etc.
    structure_name  TEXT NOT NULL,
    dimension       INTEGER NOT NULL,
    root_count      INTEGER,
    closure_type    TEXT CHECK (closure_type IN ('simple','simply_laced','unimodular','even','Leech')),
    lookup_cost     TEXT NOT NULL DEFAULT 'computed' CHECK (lookup_cost IN ('computed','no_cost','deferred'))
);

-- Table: cross_block_vectors
-- Role: 192 cross-block vectors verified in lattice closure
CREATE TABLE IF NOT EXISTS cross_block_vectors (
    vector_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    rung_id         INTEGER NOT NULL,
    vector_coords   TEXT NOT NULL,         -- JSON array
    block_source    TEXT NOT NULL,
    block_target    TEXT NOT NULL,
    verified        INTEGER NOT NULL DEFAULT 1 CHECK (verified IN (0,1)),
    FOREIGN KEY (rung_id) REFERENCES lattice_closure_ladder(rung_id)
);

-- Table: terminal_addresses
-- Role: Closure points where the lattice is fully closed
CREATE TABLE IF NOT EXISTS terminal_addresses (
    address_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    rung_id         INTEGER NOT NULL,
    address_coords  TEXT NOT NULL,
    closure_depth   INTEGER NOT NULL DEFAULT 4096,
    is_terminal     INTEGER NOT NULL DEFAULT 1 CHECK (is_terminal IN (0,1)),
    FOREIGN KEY (rung_id) REFERENCES lattice_closure_ladder(rung_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_ladder_rung ON lattice_closure_ladder(rung_id);
CREATE INDEX IF NOT EXISTS idx_cbv_rung    ON cross_block_vectors(rung_id);
CREATE INDEX IF NOT EXISTS idx_term_rung   ON terminal_addresses(rung_id);

-- Seed data: 7-rung ladder
INSERT INTO lattice_closure_ladder (rung_id, rung_name, lattice_code, structure_name, dimension, root_count, closure_type, lookup_cost) VALUES
(1, 'LCR Carrier',   1,  'A1',        1,   2,  'simple',       'computed'),
(2, 'D4 Codec',      3,  'D4',        4,  24,  'simply_laced', 'computed'),
(3, 'J3(O) Atlas',   7,  'J3(O)',    27,  78,  'simple',       'computed'),
(4, 'D12 Envelope',  8,  'D12',      12,  96,  'simply_laced', 'computed'),
(5, 'F4 Action',    24,  'F4',       24,  48,  'simple',       'computed'),
(6, 'E8 Closure',   72,  'E8',       48, 240,  'simply_laced', 'no_cost'),
(7, 'Leech Lattice', 0,  'Leech',    24,   0,  'Leech',        'no_cost');
