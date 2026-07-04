-- ============================================================
-- Paper 79 — Unified Governance 2 First Routing Implementation
-- Domain: Routing / MCP Bridge
-- Cross-references: Paper 78 (governance), Paper 28 (service),
--                   Paper 80 (2-category L)
-- ============================================================

-- Table: first_routing_implementation
-- Role: First-routing as MCP bridge. Universal normal-form intake.
CREATE TABLE IF NOT EXISTS first_routing_implementation (
    route_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    route_name      TEXT NOT NULL,
    mcp_bridge_type TEXT,
    intake_format   TEXT,                  -- canonical form
    blocker_status  INTEGER DEFAULT 0,     -- Monster ceiling blocker
    operational     INTEGER DEFAULT 0
);

-- Table: universal_normal_form
-- Role: Conversion to canonical form for intake
CREATE TABLE IF NOT EXISTS universal_normal_form (
    unf_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    input_format    TEXT NOT NULL,
    canonical_form  TEXT NOT NULL,
    conversion_rule TEXT,
    verified        INTEGER DEFAULT 0
);

-- Seed data: first routing
INSERT INTO first_routing_implementation (route_name, mcp_bridge_type, intake_format, blocker_status) VALUES
('MCP bridge v1', 'local_conversation', '2-category_L_normal_form', 1);

-- ============================================================
-- NEW: Unmapped file claims harvested 2026-07-04
-- ============================================================

-- Table: ribbon_cycle_metrics
-- Role: Cycle 7 metrics from FORWARD_PLAN.md
CREATE TABLE IF NOT EXISTS ribbon_cycle_metrics (
    cycle_id    INTEGER NOT NULL,
    metric_name TEXT NOT NULL,
    value       INTEGER NOT NULL,
    source_file TEXT NOT NULL,
    source_date TEXT NOT NULL
);

INSERT INTO ribbon_cycle_metrics (cycle_id, metric_name, value, source_file, source_date) VALUES
(7, 'timeline_graph_nodes', 3662, 'FORWARD_PLAN.md', '2026-06-30'),
(7, 'honest_assemble', 39, 'FORWARD_PLAN.md', '2026-06-30'),
(7, 'reroute', 85, 'FORWARD_PLAN.md', '2026-06-30'),
(7, 'discovery', 324, 'FORWARD_PLAN.md', '2026-06-30'),
(7, 'closure_applied', 5427, 'FORWARD_PLAN.md', '2026-06-30'),
(7, 'cmplx_standards_models', 5, 'FORWARD_PLAN.md', '2026-06-30'),
(7, 'registry_paths', 9392, 'FORWARD_PLAN.md', '2026-06-30'),
(7, 'obligation_rows', 1105, 'FORWARD_PLAN.md', '2026-06-30');

-- Table: lane3_recovery
-- Role: Lane 3 infrastructure recovery findings
CREATE TABLE IF NOT EXISTS lane3_recovery (
    recovery_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_text  TEXT NOT NULL,
    source_file TEXT NOT NULL,
    source_date TEXT NOT NULL
);

INSERT INTO lane3_recovery (claim_text, source_file, source_date) VALUES
('159 historical definitions scanned; 143 missing in active tree', 'lane3_agrm_infrastructure_recovery_report.md', '2026-07-03'),
('AGRMConfig phi_scale=1.618, target_load=0.70, floors=3, rooms=64', 'lane3_agrm_infrastructure_recovery_report.md', '2026-07-03'),
('fnv1a64 hash function present in historical AGRM but absent from active', 'lane3_agrm_infrastructure_recovery_report.md', '2026-07-03');

CREATE INDEX IF NOT EXISTS idx_ribbon_cycle ON ribbon_cycle_metrics(cycle_id, metric_name);
