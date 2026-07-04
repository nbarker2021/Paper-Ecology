-- ============================================================
-- Paper 14 — Unified Gr Boundary Repair Curvature
-- Domain: GR Curvature / Repair-Curvature Ledger
-- Cross-references: Paper 04 (boundary repair), Paper 33 (GR continuum),
--                   Paper 65 (EFE), Paper 66 (BH entropy)
-- ============================================================

-- Table: repair_curvature_ledger
-- Role: Tracks firing density of corrections as curvature proxy.
--       Curvature = boundary-repair demand.
CREATE TABLE IF NOT EXISTS repair_curvature_ledger (
    ledger_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    vertex_id       TEXT NOT NULL,         -- lattice vertex
    firing_density  REAL NOT NULL,         -- local curvature K(v)
    boundary_type   TEXT CHECK (boundary_type IN ('type_preserving','arf_matching','idempotent','curvature_driven')),
    residue_mass    REAL,                  -- mass residue at vertex
    paper_ref       INTEGER NOT NULL DEFAULT 14,
    FOREIGN KEY (paper_ref) REFERENCES papers(paper_num)
);

-- Table: curvature_bounds
-- Role: Firing density bounds and conservation laws
CREATE TABLE IF NOT EXISTS curvature_bounds (
    bound_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    bound_name      TEXT NOT NULL,
    bound_type      TEXT NOT NULL CHECK (bound_type IN ('upper','lower','conservation')),
    bound_value     REAL,
    applies_to      TEXT                   -- e.g., 'all_vertices', 'horizon'
);

-- Table: einstein_field_equation_deferred
-- Role: EFE deferred status — open obligation
CREATE TABLE IF NOT EXISTS einstein_field_equation_deferred (
    deferral_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_deferred_from INTEGER NOT NULL DEFAULT 14,
    paper_target    INTEGER NOT NULL DEFAULT 65,
    status          TEXT NOT NULL DEFAULT 'deferred' CHECK (status IN ('deferred','in_progress','resolved')),
    analogy_note    TEXT,                  -- structural analogy with Riemann
    FOREIGN KEY (paper_deferred_from) REFERENCES papers(paper_num),
    FOREIGN KEY (paper_target) REFERENCES papers(paper_num)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_curv_vertex ON repair_curvature_ledger(vertex_id);
CREATE INDEX IF NOT EXISTS idx_curv_paper  ON repair_curvature_ledger(paper_ref);

-- Seed data: curvature bounds
INSERT INTO curvature_bounds (bound_name, bound_type, bound_value, applies_to) VALUES
('Firing Density Upper', 'upper', 1.0, 'all_vertices'),
('Repair Charge Conservation', 'conservation', NULL, 'closed_boundaries'),
('Horizon Bound', 'lower', 0.0, 'horizon');

-- Seed data: EFE deferral
INSERT INTO einstein_field_equation_deferred (paper_deferred_from, paper_target, status, analogy_note) VALUES
(14, 65, 'deferred', 'Riemann curvature ↔ repair curvature (structural analogy)');

-- === BATCH GROUP 1 CLAIMS (paper-14) ===
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (14, '14.1', '137 continuation surfaces include Paper 014, E8 roots, SM bosons, Fibonacci, triality', 'D', 'CAM_ROUTED_NETWORK_MAP.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (14, '14.2', 'Riemann continuation surfaces include Paper 14, Riemann tensor, boundary-repair operator, torsion', 'D', 'CAM_ROUTED_NETWORK_MAP.md');
INSERT INTO claim_ledger (paper_num, claim_id, claim_text, classification, source_file) VALUES (14, '14.3', 'T_D12_CHAIN: 17 non-trivial idempotent sequences (R30 Paper 14)', 'D', 'CAM_ROUTED_NETWORK_MAP.md');
