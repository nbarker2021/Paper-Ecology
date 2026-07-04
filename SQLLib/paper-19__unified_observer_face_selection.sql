-- ============================================================
-- Paper 19 — Unified Observer Face Selection
-- Domain: Observer Theory / Face Selection
-- Cross-references: Paper 06 (causal links), Paper 13 (quark faces),
--                   Paper 27 (observer delay), Paper 38 (AI runtime)
-- ============================================================

-- Table: observer_face_selection
-- Role: Process by which the observer chooses the face of the chart.
--       Latent alternatives are tracked.
CREATE TABLE IF NOT EXISTS observer_face_selection (
    selection_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    observer_id     TEXT NOT NULL,
    selected_face   INTEGER NOT NULL,
    latent_faces    TEXT,                  -- JSON array of alternatives
    selection_basis TEXT,                  -- e.g., 'energy_min', 'causal_priority'
    timestamp       DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (selected_face) REFERENCES quark_faces(face_id)
);

-- Table: latent_alternatives
-- Role: Tracks all latent (unselected) face alternatives per observation
CREATE TABLE IF NOT EXISTS latent_alternatives (
    alternative_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    selection_id    INTEGER NOT NULL,
    face_id         INTEGER NOT NULL,
    alternative_weight REAL,               -- probability or priority
    FOREIGN KEY (selection_id) REFERENCES observer_face_selection(selection_id),
    FOREIGN KEY (face_id) REFERENCES quark_faces(face_id)
);

-- Table: observer_registry
-- Role: Registry of all observers in the system
CREATE TABLE IF NOT EXISTS observer_registry (
    observer_id     TEXT PRIMARY KEY,
    observer_type   TEXT CHECK (observer_type IN ('human','agent','SPINOR','cursor','AI')),
    first_observed  DATETIME DEFAULT CURRENT_TIMESTAMP,
    paper_anchor    INTEGER DEFAULT 19
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_sel_observer ON observer_face_selection(observer_id);
CREATE INDEX IF NOT EXISTS idx_sel_face    ON observer_face_selection(selected_face);

-- === BATCH GROUP 1 CLAIMS (paper-19) ===
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (19, '19.1', 'Observer = Boundary Measurement (Paper 019)', 'D', '27_Observer_Delay_and_Shared_Reality.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (19, '19.2', 'In standard quantum mechanics, measurement is a postulate', 'I', '25_Energetic_Traversal_Maps.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (19, '19.3', 'In LCR triality, measurement is a derived boundary event', 'D', '27_Observer_Delay_and_Shared_Reality.md');
