-- ============================================================
-- Paper 92 — Unified F4 Universality Theorem
-- Domain: F4 Universality / Application Band
-- Cross-references: Paper 03 (magic square), Paper 75 (F4 closure)
-- ============================================================

-- Table: f4_universality_theorem
-- Role: F4 encoding is universal. Every FSM on LCR carrier encodes in F4.
CREATE TABLE IF NOT EXISTS f4_universality_theorem (
    theorem_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    theorem_name    TEXT NOT NULL DEFAULT 'F4 Universality Theorem',
    statement       TEXT NOT NULL,
    proof_sketch    TEXT,
    magic_square_used INTEGER DEFAULT 1,
    lattice_code_chain_used INTEGER DEFAULT 1,
    structural_proof INTEGER DEFAULT 1,
    full_formal_proof INTEGER DEFAULT 0,
    status          TEXT DEFAULT 'structural_proof'
);

-- Table: f4_maximal_subgroups
-- Role: F4 maximal subgroups for encoding
CREATE TABLE IF NOT EXISTS f4_maximal_subgroups (
    subgroup_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    subgroup_name   TEXT NOT NULL,
    dimension       INTEGER,
    rank            INTEGER,
    embedding_in_f4 TEXT
);

-- Seed data: F4 maximal subgroups
INSERT INTO f4_maximal_subgroups (subgroup_name, dimension, rank) VALUES
('Spin(9)',    36, 4),
('Sp(3)×Sp(1)', 21, 4),
('SU(3)×SU(3)', 16, 4),
('G2×A1',      17, 3);

-- Seed data: theorem
INSERT INTO f4_universality_theorem (statement, status) VALUES
('The F4 encoding is universal for all finite-state machines on the LCR carrier', 'structural_proof');

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 92
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p92 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p92 (claim_ref, claim_text, status, source_file) VALUES
('92.1', 'Paper 92 (F4 universality): the F4 universality theorem is the open obligation for the E6 glue construction', 'D', 'mapped_file_claims_report.md');
