-- ============================================================
-- Paper 04 — Unified Boundary Repair
-- Domain: Boundary Repair / Typed Obligations
-- Cross-references: Paper 03 (triality/Arf), Paper 05 (oloid carrier),
--                   Paper 14 (GR curvature), Paper 65 (EFE)
-- ============================================================

-- Table: boundary_repair_constraints
-- Role: Typed boundary repair constraints: type-preserving, idempotent,
--       Arf-matching. Each constraint is a 5-tuple obligation row.
CREATE TABLE IF NOT EXISTS boundary_repair_constraints (
    constraint_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    constraint_name TEXT NOT NULL,
    lane_id         INTEGER NOT NULL,
    source_paper    INTEGER NOT NULL,
    evidence_type   TEXT NOT NULL CHECK (evidence_type IN ('D','I','X')),
    residue_desc    TEXT,                  -- what remains open
    is_type_preserving INTEGER NOT NULL DEFAULT 1 CHECK (is_type_preserving IN (0,1)),
    is_idempotent   INTEGER NOT NULL DEFAULT 1 CHECK (is_idempotent IN (0,1)),
    arf_matches     INTEGER NOT NULL DEFAULT 1 CHECK (arf_matches IN (0,1)),
    repair_curvature REAL,                 -- local curvature K(v)
    FOREIGN KEY (lane_id) REFERENCES claim_lanes(lane_id),
    FOREIGN KEY (source_paper) REFERENCES papers(paper_num)
);

-- Table: repair_operations
-- Role: Log of all boundary repair operations performed
CREATE TABLE IF NOT EXISTS repair_operations (
    operation_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    from_state      INTEGER NOT NULL,
    to_state        INTEGER NOT NULL,
    repair_type     TEXT NOT NULL CHECK (repair_type IN ('type_match','arf_match','idempotent','curvature')),
    timestamp       DATETIME DEFAULT CURRENT_TIMESTAMP,
    obligation_id   INTEGER,
    receipt_hash    TEXT,                  -- content-addressed receipt
    FOREIGN KEY (from_state) REFERENCES lcr_states(state_id),
    FOREIGN KEY (to_state)   REFERENCES lcr_states(state_id)
);

-- Table: obligation_rows
-- Role: 5-tuple obligation structure (id, lane, source, evidence, residue)
CREATE TABLE IF NOT EXISTS obligation_rows (
    obligation_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    lane_id         INTEGER NOT NULL,
    source_paper    INTEGER NOT NULL,
    evidence        TEXT NOT NULL,
    residue         TEXT,
    status          TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open','closed','staged')),
    FOREIGN KEY (lane_id) REFERENCES claim_lanes(lane_id),
    FOREIGN KEY (source_paper) REFERENCES papers(paper_num)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_repair_lane ON boundary_repair_constraints(lane_id);
CREATE INDEX IF NOT EXISTS idx_repair_paper ON boundary_repair_constraints(source_paper);
CREATE INDEX IF NOT EXISTS idx_op_type    ON repair_operations(repair_type);
CREATE INDEX IF NOT EXISTS idx_obl_status ON obligation_rows(status);

-- Seed data: sample boundary repair constraints
INSERT INTO boundary_repair_constraints (constraint_id, constraint_name, lane_id, source_paper, evidence_type, residue_desc, is_type_preserving, is_idempotent, arf_matches, repair_curvature) VALUES
(1, 'Type Preservation Axiom', 1, 4, 'D', NULL, 1, 1, 1, 0.0),
(2, 'Arf Matching Criterion', 3, 4, 'D', NULL, 1, 1, 1, 0.0),
(3, 'Idempotent Repair', 1, 4, 'I', 'Full proof pending formalization', 1, 1, 1, 0.5),
(4, 'GR Curvature Bridge', 2, 14, 'I', 'EFE deferred to Paper 65', 1, 0, 1, 1.0);
