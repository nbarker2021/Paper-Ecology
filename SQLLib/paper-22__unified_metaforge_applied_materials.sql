
-- Table: claims
-- Role: Claim ledger entries from mapped file reports
CREATE TABLE IF NOT EXISTS claims (
    claim_id        TEXT PRIMARY KEY,
    paper_num       INTEGER NOT NULL,
    claim_text      TEXT NOT NULL,
    tag             TEXT CHECK (tag IN ('D','I','X')),
    source_file     TEXT,
    FOREIGN KEY (paper_num) REFERENCES papers(paper_num)
);

-- ============================================================
-- Paper 22 — Unified Metaforge Applied Materials
-- Domain: Materials / Meta-Material Design
-- Cross-references: Paper 21 (forge systems), Paper 34 (metamaterials),
--                   Paper 36 (condensed matter)
-- ============================================================

-- Table: metaforge_materials
-- Role: Materials candidates generated via lattice forge
CREATE TABLE IF NOT EXISTS metaforge_materials (
    material_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    material_name   TEXT NOT NULL,
    lattice_type    TEXT NOT NULL,         -- e.g., 'E8-derived', 'D4-derived'
    target_property TEXT,                  -- e.g., 'superconductivity', 'strength'
    forge_id        INTEGER,
    design_params   TEXT,                  -- JSON
    simulation_status TEXT NOT NULL DEFAULT 'designed' CHECK (simulation_status IN ('designed','simulated','fabricated','tested')),
    FOREIGN KEY (forge_id) REFERENCES forge_systems(forge_id)
);

-- Table: material_properties
-- Role: Computed/measured properties of metaforge materials
CREATE TABLE IF NOT EXISTS material_properties (
    property_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id     INTEGER NOT NULL,
    property_name   TEXT NOT NULL,
    property_value  REAL,
    unit            TEXT,
    computation_method TEXT,
    FOREIGN KEY (material_id) REFERENCES metaforge_materials(material_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_mat_lattice ON metaforge_materials(lattice_type);
CREATE INDEX IF NOT EXISTS idx_mat_status  ON metaforge_materials(simulation_status);

-- Added claims from mapped file report for paper-022
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (22, 22.10, 'Depth 3 = universal ceiling for all tile substitution operations', 'D', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (22, 22.11, 'Depth 3 = Universal Maximum — Tile Substitution Ceiling', 'I', '28_N_Dimensional_Game_Lattices.md');
INSERT INTO claims (paper_num, claim_id, claim_text, tag, source_file) VALUES (22, 22.12, 'Tier: Recursive Closure (20-23)', 'I', '28_N_Dimensional_Game_Lattices.md');
