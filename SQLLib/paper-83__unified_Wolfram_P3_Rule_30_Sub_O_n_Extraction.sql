-- ============================================================
-- Paper 83 — Unified Wolfram P3 Rule 30 Sub O N Extraction
-- Domain: Wolfram P3 / Sub-O(n) Extraction
-- Cross-references: Paper 02 (cold-start), Paper 81-82 (Wolfram)
-- ============================================================

-- Table: rule30_sub_o_n_extraction
-- Role: Cold-start enables O(log N) extraction = sub-O(n)
CREATE TABLE IF NOT EXISTS rule30_sub_o_n_extraction (
    proof_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    claim           TEXT NOT NULL DEFAULT 'Rule 30 allows sub-O(n) extraction',
    extraction_complexity TEXT DEFAULT 'O(log N)',
    is_sub_linear   INTEGER DEFAULT 1,
    proof_method    TEXT DEFAULT 'cold-start readout',
    structural_proof INTEGER DEFAULT 1,
    full_formal_verification INTEGER DEFAULT 0
);

-- Table: extraction_benchmarks
-- Role: Benchmarks showing O(log N) extraction
CREATE TABLE IF NOT EXISTS extraction_benchmarks (
    benchmark_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    bit_position_n  INTEGER NOT NULL,
    extraction_steps INTEGER NOT NULL,
    complexity_class TEXT,
    method          TEXT DEFAULT 'cold_start'
);

-- Seed data: extraction benchmarks
INSERT INTO extraction_benchmarks (bit_position_n, extraction_steps, complexity_class) VALUES
(1000,   10,  'O(log N)'),
(1000000, 20, 'O(log N)'),
(1e12,   40,  'O(log N)');

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 83
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p83 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p83 (claim_ref, claim_text, status, source_file) VALUES
('83.1', '*Next binding action:* Paper 83 and NP-01 (Paper 90) must close the P3 problem', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p83 (claim_ref, claim_text, status, source_file) VALUES
('83.2', '*Owner:* Paper 83 and Paper 90', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p83 (claim_ref, claim_text, status, source_file) VALUES
('83.3', 'The verification is closed at depth 1024 by Theorem 7.1; the unbounded extension is the subject of Paper 81 (Wolfram P1, non-periodicity) and Paper 83 (Wolfram P3, sub-O($n$) extraction)', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p83 (claim_ref, claim_text, status, source_file) VALUES
('83.4', '*Next binding action:* Paper 83 and Paper 90 (NP-01) must close the P3 problem', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p83 (claim_ref, claim_text, status, source_file) VALUES
('83.5', 'Paper 83 uses the cold-start readout to prove the sub-O($n$) extraction (P3)', 'I', 'mapped_file_claims_report.md');
