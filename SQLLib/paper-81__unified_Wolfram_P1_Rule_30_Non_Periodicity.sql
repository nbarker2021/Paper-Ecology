-- ============================================================
-- Paper 81 — Unified Wolfram P1 Rule 30 Non Periodicity
-- Domain: Wolfram P1 / Rule 30 Non-Periodicity
-- Cross-references: Paper 02 (Rule 30), Paper 90 (McKay-Thompson)
-- ============================================================

-- Table: rule30_non_periodicity
-- Role: Proof status of Rule 30 non-periodicity via Lucas carry + cold-start
CREATE TABLE IF NOT EXISTS rule30_non_periodicity (
    proof_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    claim           TEXT NOT NULL DEFAULT 'Rule 30 is non-periodic',
    proof_method    TEXT NOT NULL DEFAULT 'Lucas carry + cold-start',
    anf_decomposition INTEGER DEFAULT 1,
    structural_proof INTEGER DEFAULT 1,
    full_formal_verification INTEGER DEFAULT 0,
    status          TEXT DEFAULT 'structural_claim'
);

-- Table: non_periodicity_evidence
-- Role: Computational evidence for non-periodicity
CREATE TABLE IF NOT EXISTS non_periodicity_evidence (
    evidence_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    depth_tested    INTEGER NOT NULL,
    cycle_found     INTEGER DEFAULT 0 CHECK (cycle_found IN (0,1)),
    pattern_hash    TEXT
);

-- Seed data
INSERT INTO rule30_non_periodicity (claim, proof_method, status) VALUES
('Rule 30 is non-periodic', 'Lucas carry + cold-start ANF decomposition', 'structural_claim');

INSERT INTO non_periodicity_evidence (depth_tested, cycle_found) VALUES
(1024, 0),
(4096, 0),
(10000, 0);

-- ============================================================
-- NEW: Unmapped file claims harvested 2026-07-04
-- ============================================================

-- Table: rule30_corpus
-- Role: Rule 30 corpus and duplication findings
CREATE TABLE IF NOT EXISTS rule30_corpus (
    corpus_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_text  TEXT NOT NULL,
    count       INTEGER,
    source_file TEXT NOT NULL,
    source_date TEXT NOT NULL
);

INSERT INTO rule30_corpus (claim_text, count, source_file, source_date) VALUES
('Rule 30 function corpus spans 249 verified files', 249, 'gap_analysis.md', '2026-07-03'),
('Historical rule30.py frozen dataclass (277.8 KB) in drive_audit archives', 1, 'bipartite_review_part_a_historical.md', '2026-07-03'),
('wolfram_rule30_center_1m.json appears in 22 duplicate instances', 22, 'deduplication_report.md', '2026-07-03');

CREATE INDEX IF NOT EXISTS idx_rule30_source ON rule30_corpus(source_file);

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 81
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p81 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p81 (claim_ref, claim_text, status, source_file) VALUES
('81.1', '*Owner:* Paper 2 (Lucas carry closed form) and Paper 81 (Rule 30 non-periodicity)', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p81 (claim_ref, claim_text, status, source_file) VALUES
('81.2', '*Why not closed:* the unbounded proof is the P1 Millennium-class problem (Paper 81)', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p81 (claim_ref, claim_text, status, source_file) VALUES
('81.3', '*Next binding action:* Paper 81 must give the unbounded proof via the Lucas carry closed form and the cold-start O(log N) readout', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p81 (claim_ref, claim_text, status, source_file) VALUES
('81.4', 'The verification is closed at depth 1024 by Theorem 7.1; the unbounded extension is the subject of Paper 81 (Wolfram P1, non-periodicity) and Paper 83 (Wolfram P3, sub-O($n$) extraction)', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p81 (claim_ref, claim_text, status, source_file) VALUES
('81.5', '*Next binding action:* Paper 81 must give the unbounded proof via the Lucas carry closed form and the cold-start readout', 'D', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p81 (claim_ref, claim_text, status, source_file) VALUES
('81.6', '*Next binding action:* Paper 81 (or the McKay-Thompson analysis in Paper 90) must close the firing set density conjecture', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p81 (claim_ref, claim_text, status, source_file) VALUES
('81.7', '*Owner:* Paper 81 and Paper 90', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p81 (claim_ref, claim_text, status, source_file) VALUES
('81.8', '*Next binding action:* Paper 81 (Rule 30 non-periodicity) and Paper 90 (McKay-Thompson) must close the firing density conjecture', 'I', 'mapped_file_claims_report.md');
