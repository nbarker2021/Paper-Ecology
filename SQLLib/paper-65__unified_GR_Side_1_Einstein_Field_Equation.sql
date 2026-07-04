-- ============================================================
-- Paper 65 — Unified GR Side 1 Einstein Field Equation
-- Domain: EFE / Repair Curvature Derivation
-- Cross-references: Paper 14 (repair curvature), Paper 34 (GR continuum),
--                   Paper 66 (BH entropy)
-- ============================================================

-- Table: einstein_tensor
-- Role: Einstein tensor as continuum limit of repair curvature
CREATE TABLE IF NOT EXISTS einstein_tensor (
    tensor_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    metric_name     TEXT NOT NULL,
    g_mu_nu         TEXT,                  -- JSON metric tensor
    ricci_scalar    REAL,
    einstein_g      TEXT,                  -- G_μν as JSON
    repair_source   TEXT,                  -- stress-energy as repair source
    status          TEXT DEFAULT 'deferred'
);

-- Table: stress_energy_tensor
-- Role: Stress-energy tensor as source of repair curvature
CREATE TABLE IF NOT EXISTS stress_energy_tensor (
    tensor_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    metric_id       INTEGER,
    t_mu_nu         TEXT,                  -- JSON
    energy_density  REAL,
    pressure        REAL,
    FOREIGN KEY (metric_id) REFERENCES einstein_tensor(tensor_id)
);

-- Table: efe_derivation_steps
-- Role: Derivation steps from repair curvature to EFE
CREATE TABLE IF NOT EXISTS efe_derivation_steps (
    step_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    step_order      INTEGER NOT NULL,
    step_name       TEXT NOT NULL,
    from_paper      INTEGER,
    to_paper        INTEGER DEFAULT 65,
    status          TEXT DEFAULT 'open'
);

-- Seed data: EFE derivation steps
INSERT INTO efe_derivation_steps (step_order, step_name, from_paper, status) VALUES
(1, 'Repair curvature K(v) at vertex', 14, 'proven'),
(2, 'Continuum limit of K(v)', 34, 'deferred'),
(3, 'Ricci scalar identification', 65, 'open'),
(4, 'Stress-energy as repair source', 65, 'open'),
(5, 'G_μν + Λg_μν = 8πT_μν', 65, 'open');
