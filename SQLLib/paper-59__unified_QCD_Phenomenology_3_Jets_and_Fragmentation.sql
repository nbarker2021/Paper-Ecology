-- ============================================================
-- Paper 59 — Unified QCD Phenomenology 3 Jets And Fragmentation
-- Domain: Jets / Fragmentation
-- Cross-references: Paper 57-58 (QCD phenomenology)
-- ============================================================

-- Table: jet_events
-- Role: Jets as boundary repair in FLCR substrate
CREATE TABLE IF NOT EXISTS jet_events (
    event_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    energy_gev      REAL NOT NULL,
    jet_count       INTEGER,
    parton_origin   TEXT,                  -- quark or gluon that initiated jet
    boundary_repair_type TEXT DEFAULT 'fragmentation'
);

-- Table: fragmentation_functions
-- Role: Fragmentation as repair process
CREATE TABLE IF NOT EXISTS fragmentation_functions (
    frag_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id        INTEGER NOT NULL,
    parton_type     TEXT NOT NULL,
    hadron_produced TEXT,
    z_fraction      REAL,                  -- energy fraction
    fragmentation_prob REAL,
    FOREIGN KEY (event_id) REFERENCES jet_events(event_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_jet_energy ON jet_events(energy_gev);
CREATE INDEX IF NOT EXISTS idx_frag_event ON fragmentation_functions(event_id);

-- Mapped claims extraction

-- Table: mapped_claims_59
CREATE TABLE IF NOT EXISTS mapped_claims (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_num INTEGER NOT NULL,
    claim_seq INTEGER NOT NULL,
    claim_text TEXT NOT NULL,
    claim_tag TEXT DEFAULT 'D',
    source_file TEXT,
    extraction_date TEXT
);

-- Mapped claims extraction
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (59, 1, '**FILE:** `paper_59.md`', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (59, 2, '**TITLE:** Paper 59 — QCD Phenomenology 3: Jets and Fragmentation', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
INSERT INTO mapped_claims (paper_num, claim_seq, claim_text, claim_tag, source_file, extraction_date) VALUES (59, 3, '**SUMMARY:** QCD phenomenology 3: jets and fragmentation', 'D', 'D:/mapped_file_claims_report.md', '2026-07-04');
