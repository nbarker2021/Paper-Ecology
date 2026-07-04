-- ============================================================
-- Paper 24 — Unified Knightforge N Dimensional Chess Automata
-- Domain: Game Theory / N-Dimensional Chess
-- Cross-references: Paper 21 (forge systems), Paper 28 (game lattices)
-- ============================================================

-- Table: knightforge_games
-- Role: N-dimensional chess automata configurations
CREATE TABLE IF NOT EXISTS knightforge_games (
    game_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name       TEXT NOT NULL,
    dimension       INTEGER NOT NULL,
    board_size      INTEGER NOT NULL,
    ruleset         TEXT CHECK (ruleset IN ('standard','fairy','automata','quantum')),
    nash_equilibrium INTEGER,              -- terminal address if known
    status          TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active','solved','unsolved','open'))
);

-- Table: knightforge_moves
-- Role: Valid moves in n-dimensional chess
CREATE TABLE IF NOT EXISTS knightforge_moves (
    move_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id         INTEGER NOT NULL,
    piece_type      TEXT NOT NULL,
    from_coords     TEXT NOT NULL,         -- JSON array
    to_coords       TEXT NOT NULL,         -- JSON array
    move_valid      INTEGER NOT NULL DEFAULT 1 CHECK (move_valid IN (0,1)),
    FOREIGN KEY (game_id) REFERENCES knightforge_games(game_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_game_dim ON knightforge_games(dimension);
CREATE INDEX IF NOT EXISTS idx_game_status ON knightforge_games(status);
