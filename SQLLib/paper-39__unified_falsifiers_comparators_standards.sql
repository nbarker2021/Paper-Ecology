-- ============================================================
-- Paper 39 — Unified Falsifiers Comparators Standards
-- Domain: Standards / Evidence Framework
-- Cross-references: Paper 11 (admission gates), Paper 37 (falsifiers),
--                   Paper 78-79 (governance)
-- ============================================================

-- Table: claim_harvesters
-- Role: Automated claim harvesting and typing
CREATE TABLE IF NOT EXISTS claim_harvesters (
    harvester_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    harvester_name  TEXT NOT NULL,
    target_paper    INTEGER NOT NULL,
    claims_found    INTEGER DEFAULT 0,
    claims_typed_d  INTEGER DEFAULT 0,
    claims_typed_i  INTEGER DEFAULT 0,
    claims_typed_x  INTEGER DEFAULT 0,
    harvest_status  TEXT DEFAULT 'running',
    FOREIGN KEY (target_paper) REFERENCES papers(paper_num)
);

-- Table: provenance_tests
-- Role: Provenance tests for evidence chain validation
CREATE TABLE IF NOT EXISTS provenance_tests (
    test_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    test_name       TEXT NOT NULL,
    test_type       TEXT CHECK (test_type IN ('hash','signature','chain','timestamp','receipt')),
    target_receipt  TEXT,
    test_result     TEXT CHECK (test_result IN ('pass','fail','pending')),
    run_at          DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table: standards_of_evidence
-- Role: The 5 standards of evidence
CREATE TABLE IF NOT EXISTS standards_of_evidence (
    standard_id     INTEGER PRIMARY KEY CHECK (standard_id BETWEEN 1 AND 5),
    standard_name   TEXT NOT NULL,
    description     TEXT NOT NULL,
    conformance_required INTEGER NOT NULL DEFAULT 1
);

-- Table: cam_rows
-- Role: 9 CAM rows + 1 NSIT row as content-addressed receipts
CREATE TABLE IF NOT EXISTS cam_rows (
    row_id          INTEGER PRIMARY KEY CHECK (row_id BETWEEN 1 AND 10),
    row_type        TEXT NOT NULL CHECK (row_type IN ('CAM','NSIT')),
    content_hash    TEXT NOT NULL,
    receipt_hash    TEXT,
    nsit_flag       INTEGER DEFAULT 0 CHECK (nsit_flag IN (0,1))
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_harvester_paper ON claim_harvesters(target_paper);
CREATE INDEX IF NOT EXISTS idx_prov_test ON provenance_tests(test_result);

-- Seed data: 5 standards of evidence
INSERT INTO standards_of_evidence (standard_id, standard_name, description, conformance_required) VALUES
(1, 'Lane',      'Claim is assigned to a valid claim lane', 1),
(2, 'Source',    'Source paper exists and is published',    1),
(3, 'Receipt',   'Receipt is content-addressed and valid',  1),
(4, 'Comparator','External calibration or citation exists', 1),
(5, 'Falsifier', 'Explicit falsifier condition is named',   1);

-- Seed data: 9 CAM rows + 1 NSIT row
INSERT INTO cam_rows (row_id, row_type, content_hash, nsit_flag) VALUES
(1, 'CAM',  'sha256:cam01', 0),
(2, 'CAM',  'sha256:cam02', 0),
(3, 'CAM',  'sha256:cam03', 0),
(4, 'CAM',  'sha256:cam04', 0),
(5, 'CAM',  'sha256:cam05', 0),
(6, 'CAM',  'sha256:cam06', 0),
(7, 'CAM',  'sha256:cam07', 0),
(8, 'CAM',  'sha256:cam08', 0),
(9, 'CAM',  'sha256:cam09', 0),
(10,'NSIT', 'sha256:nsit0', 1);

-- ============================================================
-- NEW: Unmapped file claims harvested 2026-07-04
-- ============================================================

-- Table: capability_verification
-- Role: Verified capabilities from gap_analysis.md
CREATE TABLE IF NOT EXISTS capability_verification (
    claim_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_text      TEXT NOT NULL,
    verified_count  INTEGER DEFAULT 0,
    source_file     TEXT NOT NULL,
    source_date     TEXT NOT NULL,
    tag             TEXT CHECK (tag IN ('D','I','X'))
);

INSERT INTO capability_verification (claim_text, verified_count, source_file, source_date, tag) VALUES
('81 capabilities are both documented and implemented', 81, 'gap_analysis.md', '2026-07-03', 'D'),
('0 capabilities are claimed but have no matching code module', 0, 'gap_analysis.md', '2026-07-03', 'D'),
('77 substantial code modules exist but are not claimed in any README', 77, 'gap_analysis.md', '2026-07-03', 'D'),
('Rule 30 function corpus spans 249 verified files', 249, 'gap_analysis.md', '2026-07-03', 'D'),
('Lattice math engine spans 4,632 verified files', 4632, 'gap_analysis.md', '2026-07-03', 'D');

-- Table: orphaned_code_modules
-- Role: 77 orphaned modules from gap_analysis.md
CREATE TABLE IF NOT EXISTS orphaned_code_modules (
    module_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    module_path     TEXT NOT NULL,
    classification  TEXT NOT NULL,
    size_kb         REAL NOT NULL,
    description     TEXT
);

INSERT INTO orphaned_code_modules (module_path, classification, size_kb, description) VALUES
('MannyAI/src/manny_mcp/plugins/tmn_legacy.py', 'python_module', 81.2, 'Python module: implements specific functionality'),
('MannyAI/src/carrier_cem.py', 'carrier', 20.2, 'Carrier: 4-bit encoding, binary boundary, LCR correction'),
('MannyAI/src/learner.py', 'python_module', 14.9, 'Python module: implements specific functionality'),
('MannyAI/src/agents/agent.py', 'agent', 7.7, 'Agent framework: multi-agent workflows, task delegation'),
('MannyAI/src/daemon/loop.py', 'python_module', 8.5, 'Python module: implements specific functionality'),
('repo_harvest/_CAM/governance_scale.py', 'python_module', 7.5, 'Python module: implements specific functionality'),
('repo_harvest/_CAM/write_synthesis_final.py', 'python_module', 6.8, 'Python module: implements specific functionality');

-- Indexes for new tables
CREATE INDEX IF NOT EXISTS idx_cap_verification_tag ON capability_verification(tag);
CREATE INDEX IF NOT EXISTS idx_orphaned_class ON orphaned_code_modules(classification);
