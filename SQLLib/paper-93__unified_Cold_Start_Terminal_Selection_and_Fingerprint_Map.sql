-- ============================================================
-- Paper 93 — Unified Cold Start Terminal Selection And Fingerprint Map
-- Domain: Cold-Start Terminal / O(log N) Readout
-- Cross-references: Paper 02 (cold-start), Paper 83 (Wolfram P3)
-- ============================================================

-- Table: cold_start_terminal
-- Role: O(log N) readout algorithm. Terminal as 1-morphism in 2-category ℒ.
CREATE TABLE IF NOT EXISTS cold_start_terminal (
    terminal_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    algorithm_name  TEXT NOT NULL DEFAULT 'Cold-Start Terminal',
    complexity_class TEXT DEFAULT 'O(log N)',
    terminal_as_morph INTEGER DEFAULT 1,   -- is 1-morphism in ℒ
    boundary_repair INTEGER DEFAULT 1,
    fingerprint_map TEXT                   -- content hash of algorithm
);

-- Table: terminal_addresses
-- Role: Terminal addresses where cold-start readout is complete
CREATE TABLE IF NOT EXISTS terminal_addresses (
    address_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    bit_position    INTEGER NOT NULL,
    terminal_coords TEXT,
    readout_complete INTEGER DEFAULT 1
);

-- Seed data
INSERT INTO cold_start_terminal (algorithm_name, complexity_class) VALUES
('Cold-Start Terminal v1', 'O(log N)');

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 93
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p93 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p93 (claim_ref, claim_text, status, source_file) VALUES
('93.1', 'Each 4 bits of the center column correspond to one Spectre tile (4 bits', 'I', 'mapped_file_claims_report.md');
