
-- Table: claims
-- Role: Claim ledger entries from mapped file reports
CREATE TABLE IF NOT EXISTS claims (
    claim_id        TEXT PRIMARY KEY,
    paper_num       INTEGER NOT NULL,
    claim_text      TEXT NOT NULL,
    tag             TEXT CHECK (tag IN ('D','I','X')),
    source_file     TEXT,
    FOREIGN KEY (paper_num) REFERENCES papers(paper_num)
);

-- ============================================================
-- Paper 32 — Unified The Supervisor Cursor
-- Domain: Cursor / Agent Navigation
-- Cross-references: Paper 06 (causal links), Paper 19 (observer),
--                   Paper 27 (shared reality), Paper 38 (AI runtime)
-- ============================================================

-- Table: supervisor_cursors
-- Role: Supervisor cursor registry and navigation state
CREATE TABLE IF NOT EXISTS supervisor_cursors (
    cursor_id       TEXT PRIMARY KEY,
    cursor_name     TEXT NOT NULL,
    current_state   INTEGER NOT NULL,
    current_face    INTEGER,
    navigation_mode TEXT CHECK (navigation_mode IN ('manual','auto','hybrid','SPINOR')),
    observer_id     TEXT,
    FOREIGN KEY (current_state) REFERENCES lcr_states(state_id),
    FOREIGN KEY (current_face) REFERENCES quark_faces(face_id),
    FOREIGN KEY (observer_id) REFERENCES observer_registry(observer_id)
);

-- Table: cursor_movements
-- Role: Cursor movement log — each move is a boundary repair
CREATE TABLE IF NOT EXISTS cursor_movements (
    movement_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    cursor_id       TEXT NOT NULL,
    from_state      INTEGER NOT NULL,
    to_state        INTEGER NOT NULL,
    repair_type     TEXT NOT NULL,
    timestamp       DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cursor_id) REFERENCES supervisor_cursors(cursor_id),
    FOREIGN KEY (from_state) REFERENCES lcr_states(state_id),
    FOREIGN KEY (to_state) REFERENCES lcr_states(state_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_cursor_state ON supervisor_cursors(current_state);
CREATE INDEX IF NOT EXISTS idx_move_cursor  ON cursor_movements(cursor_id);

-- Added claims from mapped file report for paper-032
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (32, 32.9, 'Tile mass = total bonded interactions × κ', 'D', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (32, 32.10, 'Higgs VEV = 246.22 GeV from κ transport', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (32, 32.11, 'M = N_bonds × κ', 'D', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (32, 32.12, 'Mass = Bonded Interactions × κ — Tile Mass from Bonds', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (32, 32.13, 'Tier: Energy/Mass (30-33)', 'I', '25_Energetic_Traversal_Maps.md');
