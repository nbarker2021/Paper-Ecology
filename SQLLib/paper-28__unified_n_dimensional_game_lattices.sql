-- ============================================================
-- Paper 28 — Unified N Dimensional Game Lattices
-- Domain: Game Theory / Lattice Games
-- Cross-references: Paper 21 (forge), Paper 24 (knightforge),
--                   Paper 31 (it_was_still_just_lcr)
-- ============================================================

-- Table: game_lattices
-- Role: N-dimensional game lattices with terminal addresses as equilibria
CREATE TABLE IF NOT EXISTS game_lattices (
    lattice_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name       TEXT NOT NULL,
    dimension       INTEGER NOT NULL,
    player_count    INTEGER NOT NULL DEFAULT 2,
    state_space_size INTEGER,
    nash_terminal   INTEGER,               -- terminal address (LCR state)
    equilibrium_type TEXT CHECK (equilibrium_type IN ('nash','correlated','bayesian','quantum')),
    FOREIGN KEY (nash_terminal) REFERENCES lcr_states(state_id)
);

-- Table: game_tree_paths
-- Role: Game trees as paths through the lattice
CREATE TABLE IF NOT EXISTS game_tree_paths (
    path_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    lattice_id      INTEGER NOT NULL,
    path_sequence   TEXT NOT NULL,         -- JSON array of state_ids
    path_length     INTEGER,
    is_equilibrium  INTEGER NOT NULL DEFAULT 0 CHECK (is_equilibrium IN (0,1)),
    FOREIGN KEY (lattice_id) REFERENCES game_lattices(lattice_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_game_dim ON game_lattices(dimension);
CREATE INDEX IF NOT EXISTS idx_game_eq  ON game_lattices(equilibrium_type);
