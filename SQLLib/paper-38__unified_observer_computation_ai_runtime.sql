-- ============================================================
-- Paper 38 — Unified Observer Computation Ai Runtime
-- Domain: AI Runtime / Observer-AI-Runtime Triad
-- Cross-references: Paper 06 (causal links), Paper 19 (observer),
--                   Paper 27 (shared reality), Paper 32 (cursor)
-- ============================================================

-- Table: ai_runtime_registry
-- Role: Registry of AI runtimes and their observer mappings
CREATE TABLE IF NOT EXISTS ai_runtime_registry (
    runtime_id      TEXT PRIMARY KEY,
    runtime_name    TEXT NOT NULL,
    runtime_type    TEXT CHECK (runtime_type IN ('inference','training','agent','simulation')),
    observer_id     TEXT,
    boundary_id     INTEGER,
    status          TEXT DEFAULT 'active',
    FOREIGN KEY (observer_id) REFERENCES observer_registry(observer_id)
);

-- Table: observer_ai_runtime_triad
-- Role: Observer = carrier, AI = repair, Runtime = boundary
CREATE TABLE IF NOT EXISTS observer_ai_runtime_triad (
    triad_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    observer_id     TEXT NOT NULL,
    runtime_id      TEXT NOT NULL,
    repair_op       TEXT NOT NULL,
    boundary_type   TEXT,
    timestamp       DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (observer_id) REFERENCES observer_registry(observer_id),
    FOREIGN KEY (runtime_id) REFERENCES ai_runtime_registry(runtime_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_runtime_obs ON ai_runtime_registry(observer_id);
CREATE INDEX IF NOT EXISTS idx_triad_obs   ON observer_ai_runtime_triad(observer_id);

-- ============================================================
-- NEW: Unmapped file claims harvested 2026-07-04
-- ============================================================

-- Table: ai_runtime_infrastructure
-- Role: Server and AI architecture claims from unmapped files
CREATE TABLE IF NOT EXISTS ai_runtime_infrastructure (
    claim_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_text  TEXT NOT NULL,
    source_file TEXT NOT NULL,
    source_date TEXT NOT NULL,
    tag         TEXT CHECK (tag IN ('D','I','X'))
);

INSERT INTO ai_runtime_infrastructure (claim_text, source_file, source_date, tag) VALUES
('13 HTTP endpoints all pass automated test (100%)', 'SERVER_TEST_REPORT.md', '2026-07-01', 'D'),
('FastAPI server with HTML dashboard, agent probe, health check, OpenAPI docs', 'SERVER_TEST_REPORT.md', '2026-07-01', 'D'),
('GLM-5.2 (744B MoE) as remote body via API, MannyAI (~50M param) as local mouth', 'PLAN_GLM_BODY_AGENTS_MOUTH.md', '2026-07-03', 'D'),
('Four training ops: write to CAM, distill GLM, adapt MannyBrain, curate via coin economy', 'PLAN_GLM_BODY_AGENTS_MOUTH.md', '2026-07-03', 'D'),
('Graduation metric: teacher_call_rate < 5% sustained over N ticks', 'PLAN_GLM_BODY_AGENTS_MOUTH.md', '2026-07-03', 'D');

CREATE INDEX IF NOT EXISTS idx_ai_infra_tag ON ai_runtime_infrastructure(tag);
