-- ============================================================
-- Paper 36 — Unified Condensed Matter Metamaterials
-- Domain: Metamaterials / Crystal Engineering
-- Cross-references: Paper 22 (metaforge), Paper 34 (condensed matter),
--                   Paper 35 (semiconductors)
-- ============================================================

-- Table: metamaterial_designs
-- Role: Engineered lattices with designed boundaries
CREATE TABLE IF NOT EXISTS metamaterial_designs (
    design_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    design_name     TEXT NOT NULL,
    crystal_lattice TEXT NOT NULL,         -- e.g., 'E8-derived'
    defect_pattern  TEXT,                  -- designed boundary pattern
    dislocation_type TEXT,                 -- repair type
    target_property TEXT,
    simulation_status TEXT DEFAULT 'designed'
);

-- Table: crystal_defects
-- Role: Defects as boundaries in crystal lattices
CREATE TABLE IF NOT EXISTS crystal_defects (
    defect_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    design_id       INTEGER NOT NULL,
    defect_type     TEXT NOT NULL CHECK (defect_type IN ('point','line','planar','volume')),
    boundary_curvature REAL,
    repair_operator TEXT,
    FOREIGN KEY (design_id) REFERENCES metamaterial_designs(design_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_design_lattice ON metamaterial_designs(crystal_lattice);
