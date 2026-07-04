-- ============================================================
-- Paper 73 — Unified Calibration Protocols 3 Closure Stability Sampling
-- Domain: Closure-Stability / Sampling Validation
-- Cross-references: Paper 08 (lattice closure), Paper 71 (calibration)
-- ============================================================

-- Table: closure_stability_sampling
-- Role: Validates closure of FLCR substrate under repeated sampling
CREATE TABLE IF NOT EXISTS closure_stability_sampling (
    sample_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    rung_id         INTEGER NOT NULL,
    sample_depth    INTEGER NOT NULL,
    closure_achieved INTEGER NOT NULL DEFAULT 0 CHECK (closure_achieved IN (0,1)),
    terminal_address TEXT,
    FOREIGN KEY (rung_id) REFERENCES lattice_closure_ladder(rung_id)
);

-- Table: closure_hierarchy
-- Role: Closure hierarchy from lattice code chain
CREATE TABLE IF NOT EXISTS closure_hierarchy (
    hierarchy_level INTEGER PRIMARY KEY,
    rung_id         INTEGER NOT NULL,
    closure_criterion TEXT,
    FOREIGN KEY (rung_id) REFERENCES lattice_closure_ladder(rung_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_css_rung ON closure_stability_sampling(rung_id);
