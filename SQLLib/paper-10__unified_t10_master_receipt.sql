-- ============================================================
-- Paper 10 — Unified T10 Master Receipt
-- Domain: Receipt Protocol / Stack Replay
-- Cross-references: Paper 09 (temporal windows), Paper 11 (admission gates),
--                   Paper 06 (obligation ledger)
-- ============================================================

-- Table: master_receipts
-- Role: Master receipt structure with 4 transport rows and 8 structural checks
CREATE TABLE IF NOT EXISTS master_receipts (
    receipt_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    receipt_hash    TEXT NOT NULL UNIQUE,  -- content-addressed
    paper_num       INTEGER NOT NULL,
    transport_row   TEXT NOT NULL CHECK (transport_row IN ('demonstrated','bounded_local','registered_landing_forms','inferred')),
    status          TEXT NOT NULL DEFAULT 'valid' CHECK (status IN ('valid','invalid','pass_with_open_lifts')),
    structural_checks_passed INTEGER NOT NULL DEFAULT 0 CHECK (structural_checks_passed BETWEEN 0 AND 8),
    falsifier_count INTEGER NOT NULL DEFAULT 0 CHECK (falsifier_count BETWEEN 0 AND 4),
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (paper_num) REFERENCES papers(paper_num)
);

-- Table: structural_checks
-- Role: The 8 structural checks for receipt validity
CREATE TABLE IF NOT EXISTS structural_checks (
    check_id        INTEGER PRIMARY KEY CHECK (check_id BETWEEN 1 AND 8),
    check_name      TEXT NOT NULL,
    description     TEXT NOT NULL,
    verifier_func   TEXT                   -- name of verification function
);

-- Table: receipt_falsifiers
-- Role: The 4 falsifiers that define receipt failure conditions
CREATE TABLE IF NOT EXISTS receipt_falsifiers (
    falsifier_id    INTEGER PRIMARY KEY CHECK (falsifier_id BETWEEN 1 AND 4),
    falsifier_name  TEXT NOT NULL,
    condition       TEXT NOT NULL,
    failure_mode    TEXT NOT NULL
);

-- Table: receipt_stack_replay
-- Role: Stack replay log for verifiable replay of receipts
CREATE TABLE IF NOT EXISTS receipt_stack_replay (
    replay_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    receipt_id      INTEGER NOT NULL,
    replay_sequence INTEGER NOT NULL,
    operation       TEXT NOT NULL,
    result_hash     TEXT,
    timestamp       DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (receipt_id) REFERENCES master_receipts(receipt_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_receipt_hash ON master_receipts(receipt_hash);
CREATE INDEX IF NOT EXISTS idx_receipt_paper ON master_receipts(paper_num);
CREATE INDEX IF NOT EXISTS idx_replay_receipt ON receipt_stack_replay(receipt_id);

-- Seed data: 8 structural checks
INSERT INTO structural_checks (check_id, check_name, description, verifier_func) VALUES
(1, 'Hash Integrity',      'Receipt hash matches content',         'verify_hash'),
(2, 'Signature Valid',     'Digital signature is valid',           'verify_sig'),
(3, 'Chain Continuity',    'Previous receipt hash links correctly','verify_chain'),
(4, 'Timestamp Order',     'Timestamps are monotonic',             'verify_time'),
(5, 'Lane Consistency',    'Claim lane is consistent',             'verify_lane'),
(6, 'Source Check',        'Source paper exists and is published', 'verify_source'),
(7, 'Evidence Present',    'Evidence is non-empty and typed',      'verify_evidence'),
(8, 'Residue Named',       'All open residues are explicitly named','verify_residue');

-- Seed data: 4 falsifiers
INSERT INTO receipt_falsifiers (falsifier_id, falsifier_name, condition, failure_mode) VALUES
(1, 'Hash Mismatch',       'receipt_hash != hash(content)',        'INVALID_RECEIPT'),
(2, 'Broken Chain',        'previous_hash not found',              'ORPHAN_RECEIPT'),
(3, 'Future Timestamp',    'timestamp > now()',                    'TIME_TRAVEL'),
(4, 'Lane Violation',      'claim_lane not in allowed set',        'INVALID_LANE');
