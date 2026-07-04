-- ============================================================
-- Paper 06 — Unified Causal Link And Obligation Ledger
-- Domain: Causal Structure / Obligation Graphs
-- Cross-references: Paper 05 (carrier), Paper 07 (bridge),
--                   Paper 10 (master receipt), Paper 11 (admission gates)
-- ============================================================

-- Table: causal_links
-- Role: Typed causal edges between carrier states.
--       Each edge has a verdict (positive/negative) and obligation status.
CREATE TABLE IF NOT EXISTS causal_links (
    link_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    from_state      INTEGER NOT NULL,
    to_state        INTEGER NOT NULL,
    link_type       TEXT NOT NULL CHECK (link_type IN ('dependency','causal','obligation','negative_verdict')),
    verdict         TEXT NOT NULL CHECK (verdict IN ('positive','negative','pending')),
    status_class    TEXT NOT NULL CHECK (status_class IN ('closed_now','open_derived','staged_open')),
    ledger_entry_id INTEGER,
    weight          REAL DEFAULT 1.0,
    FOREIGN KEY (from_state) REFERENCES lcr_states(state_id),
    FOREIGN KEY (to_state)   REFERENCES lcr_states(state_id)
);

-- Table: obligation_ledger
-- Role: Master ledger of all obligations (1,105+ rows in full system)
CREATE TABLE IF NOT EXISTS obligation_ledger (
    ledger_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    obligation_id   INTEGER NOT NULL,
    paper_num       INTEGER NOT NULL,
    lane_id         INTEGER NOT NULL,
    status          TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open','closed','staged','forbidden')),
    assembly_tag    TEXT,                  -- e.g., "assemble/39"
    record_count    INTEGER,
    explicit_unknown INTEGER DEFAULT 0 CHECK (explicit_unknown IN (0,1)),
    FOREIGN KEY (paper_num) REFERENCES papers(paper_num),
    FOREIGN KEY (lane_id) REFERENCES claim_lanes(lane_id)
);

-- Table: status_classifications
-- Role: The 3-status classification system
CREATE TABLE IF NOT EXISTS status_classifications (
    status_code     TEXT PRIMARY KEY CHECK (status_code IN ('closed_now','open_derived','staged_open')),
    status_name     TEXT NOT NULL,
    description     TEXT NOT NULL,
    promotion_rule  TEXT                   -- how to promote to next status
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_link_from    ON causal_links(from_state);
CREATE INDEX IF NOT EXISTS idx_link_status  ON causal_links(status_class);
CREATE INDEX IF NOT EXISTS idx_ledger_paper ON obligation_ledger(paper_num);
CREATE INDEX IF NOT EXISTS idx_ledger_status ON obligation_ledger(status);

-- Seed data: status classifications
INSERT INTO status_classifications (status_code, status_name, description, promotion_rule) VALUES
('closed_now',   'Closed Now',     'Claim is proven and closed in current paper', 'None — terminal'),
('open_derived', 'Open Derived',   'Claim is derived but not yet closed', 'Requires external calibration or proof'),
('staged_open',  'Staged Open',    'Claim is intentionally left open for future work', 'Promoted when dependency closes');

-- Seed data: sample causal links
INSERT INTO causal_links (from_state, to_state, link_type, verdict, status_class, weight) VALUES
(0, 1, 'causal', 'positive', 'closed_now', 1.0),
(0, 2, 'causal', 'positive', 'closed_now', 1.0),
(1, 4, 'dependency', 'positive', 'closed_now', 1.0),
(4, 7, 'obligation', 'pending', 'open_derived', 0.5),
(7, 0, 'negative_verdict', 'negative', 'staged_open', 1.0);

-- ============================================================
-- NEW: Unmapped file claims harvested 2026-07-04
-- ============================================================

-- Table: mannyai_infrastructure
-- Role: MannyAI infrastructure claims from unmapped files
CREATE TABLE IF NOT EXISTS mannyai_infrastructure (
    infra_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_text  TEXT NOT NULL,
    source_file TEXT NOT NULL,
    source_date TEXT NOT NULL
);

INSERT INTO mannyai_infrastructure (claim_text, source_file, source_date) VALUES
('MannyAI daemon ring (ring.py, 12,570 bytes) implements causal ring architecture', 'MannyAI/src/daemon/ring.py', '2026-07-03'),
('SpeedLight dedup (speedlight.py, 9,409 bytes) eliminates redundant causal computations', 'MannyAI/src/speedlight/speedlight.py', '2026-07-03'),
('MannyAI MCP plugin system (plugins/__init__.py, 4,831 bytes) provides 45+ tools', 'MannyAI/src/manny_mcp/plugins/__init__.py', '2026-07-04');

CREATE INDEX IF NOT EXISTS idx_mannyai_source ON mannyai_infrastructure(source_file);
