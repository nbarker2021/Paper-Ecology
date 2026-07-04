-- ============================================================
-- Paper 03 — Unified D4 J3 Triality And Correction Surface
-- Domain: Exceptional Algebra / D4-J3(𝕆) Triality
-- Cross-references: Paper 01 (LCR kernel), Paper 04 (boundary repair),
--                   Paper 17 (E6-E8 tower), Paper 92 (F4 universality)
-- ============================================================

-- Table: axis_sheet_map
-- Role: D4 axis/sheet codec: 4 axis classes × 2 sheets = 8 states.
--       This is the fundamental partition of the LCR carrier.
CREATE TABLE IF NOT EXISTS axis_sheet_map (
    map_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    axis_class      INTEGER NOT NULL CHECK (axis_class BETWEEN 0 AND 3),
    sheet           INTEGER NOT NULL CHECK (sheet IN (0,1)),
    state_id        INTEGER NOT NULL,
    d4_root_index   INTEGER,               -- index in D4 root system
    d4_root_vector  TEXT,                  -- 4D vector as JSON
    triality_role   TEXT CHECK (triality_role IN ('vector','spinor','conjugate')),
    FOREIGN KEY (state_id) REFERENCES lcr_states(state_id)
);

-- Table: diagonal_carriers
-- Role: Triality-diagonal carriers that are invariant under S3 Weyl orbit.
--       These are the trace-2 idempotents of J₃(𝕆).
CREATE TABLE IF NOT EXISTS diagonal_carriers (
    carrier_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    carrier_name    TEXT NOT NULL,
    triality_label  TEXT NOT NULL CHECK (triality_label IN ('T0','T1','T2','T3')),
    j3o_idempotent  TEXT NOT NULL,         -- matrix representation
    trace           INTEGER NOT NULL DEFAULT 2,
    generation      INTEGER CHECK (generation BETWEEN 1 AND 3),
    associated_quark TEXT                   -- e.g., 'up', 'charm', 'top'
);

-- Table: triality_automorphisms
-- Role: The S3 Weyl group action on the D4 triality (outer aut group)
CREATE TABLE IF NOT EXISTS triality_automorphisms (
    aut_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    permutation     TEXT NOT NULL,         -- e.g., "(V,S,C)"
    order_element   INTEGER NOT NULL CHECK (order_element IN (1,2,3)),
    fixed_subspace  TEXT
);

-- Table: magic_square_entries
-- Role: Freudenthal-Tits magic square entries (A,B) ↦ Lie algebra
CREATE TABLE IF NOT EXISTS magic_square_entries (
    entry_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    row_alg         TEXT NOT NULL,         -- A: R, C, H, O
    col_alg         TEXT NOT NULL,         -- B: R, C, H, O
    lie_algebra     TEXT NOT NULL,
    dimension       INTEGER NOT NULL,
    rank            INTEGER NOT NULL
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_axis_class  ON axis_sheet_map(axis_class);
CREATE INDEX IF NOT EXISTS idx_axis_sheet  ON axis_sheet_map(axis_class, sheet);
CREATE INDEX IF NOT EXISTS idx_diag_triality ON diagonal_carriers(triality_label);

-- Seed data: axis/sheet map (links to LCR states)
INSERT INTO axis_sheet_map (axis_class, sheet, state_id, d4_root_index, triality_role) VALUES
(0, 0, 0, 0, 'vector'),    -- ∅
(1, 0, 1, 1, 'spinor'),    -- L
(1, 1, 2, 2, 'conjugate'), -- C
(2, 0, 3, 3, 'vector'),    -- R
(2, 1, 4, 4, 'spinor'),    -- LC
(3, 0, 5, 5, 'conjugate'), -- LR
(3, 1, 6, 6, 'vector'),    -- CR
(0, 1, 7, 7, 'spinor');    -- LCR

-- Seed data: diagonal carriers = 3 fermion generations
INSERT INTO diagonal_carriers (carrier_name, triality_label, j3o_idempotent, trace, generation, associated_quark) VALUES
('Generation 1', 'T1', 'diag(1,0,0)', 2, 1, 'up/down'),
('Generation 2', 'T2', 'diag(0,1,0)', 2, 2, 'charm/strange'),
('Generation 3', 'T3', 'diag(0,0,1)', 2, 3, 'top/bottom');

-- Seed data: magic square (upper triangle)
INSERT INTO magic_square_entries (row_alg, col_alg, lie_algebra, dimension, rank) VALUES
('R', 'R', 'so(3)',    3,  1),
('R', 'C', 'su(3)',    8,  2),
('R', 'H', 'sp(6)',   21,  3),
('R', 'O', 'f4',      52,  4),
('C', 'R', 'su(3)',    8,  2),
('C', 'C', 'su(3)+su(3)', 16, 4),
('C', 'H', 'su(6)',   35,  5),
('C', 'O', 'e6',      78,  6),
('H', 'R', 'sp(6)',   21,  3),
('H', 'C', 'su(6)',   35,  5),
('H', 'H', 'so(12)',  66,  6),
('H', 'O', 'e7',     133,  7),
('O', 'R', 'f4',      52,  4),
('O', 'C', 'e6',      78,  6),
('O', 'H', 'e7',     133,  7),
('O', 'O', 'e8',     248,  8);


-- ============================================================
-- Harvested tables from unified_complex_t.py (Paper 03 canon)
-- ============================================================

-- Table: permutation_registry
-- Role: Bijective registry for hash_permutation / unhash_permutation.
--       Stores the mixed-radix encoding of every permutation of 1..n.
CREATE TABLE IF NOT EXISTS permutation_registry (
    registry_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    n               INTEGER NOT NULL CHECK (n > 0),
    permutation     TEXT NOT NULL,         -- e.g. "(1,2,3)"
    perm_hash       INTEGER NOT NULL,      -- mixed-radix hash
    UNIQUE(n, permutation),
    UNIQUE(n, perm_hash)
);

-- Table: superpermutation_graphs
-- Role: De Bruijn graph edges harvested from build_debruijn_graph.
CREATE TABLE IF NOT EXISTS superpermutation_graphs (
    graph_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    n               INTEGER NOT NULL,
    k               INTEGER NOT NULL,
    source_node     TEXT NOT NULL,         -- JSON tuple
    target_node     TEXT NOT NULL,         -- JSON tuple
    edge_weight     INTEGER DEFAULT 1,
    UNIQUE(n, k, source_node, target_node)
);

-- Table: prodigal_sequences
-- Role: ProdigalResult sequences and their overlap rates.
CREATE TABLE IF NOT EXISTS prodigal_sequences (
    sequence_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    result_id       INTEGER NOT NULL UNIQUE,
    sequence        TEXT NOT NULL,
    length          INTEGER NOT NULL,
    overlap_rate    REAL NOT NULL,
    num_permutations INTEGER NOT NULL
);

-- Table: grid_section_neighbors
-- Role: Cache of Grid.get_neighbors output for canonical dimensions.
CREATE TABLE IF NOT EXISTS grid_section_neighbors (
    neighbor_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    dimensions      TEXT NOT NULL,         -- JSON tuple, e.g. "[4,2]"
    section_id      INTEGER NOT NULL,
    neighbor_id_val INTEGER NOT NULL,
    UNIQUE(dimensions, section_id, neighbor_id_val)
);

-- Indexes for harvested tables
CREATE INDEX IF NOT EXISTS idx_perm_reg_n_hash ON permutation_registry(n, perm_hash);
CREATE INDEX IF NOT EXISTS idx_perm_reg_n_perm ON permutation_registry(n, permutation);
CREATE INDEX IF NOT EXISTS idx_graph_n_k ON superpermutation_graphs(n, k);
CREATE INDEX IF NOT EXISTS idx_prodigal_rate ON prodigal_sequences(overlap_rate);
