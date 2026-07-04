-- ============================================================
-- Paper 29 — Unified Monster Universal Energy Bound Hypotheses
-- Domain: Monster VOA / Energy Bounds
-- Cross-references: Paper 18 (moonshine), Paper 25 (Monster ceiling),
--                   Paper 80 (2-category L)
-- ============================================================

-- Table: monster_energy_bounds
-- Role: Largest invariants of Monster VOA bound the FLCR substrate.
--       c_max ≈ 8.0×10³³.
CREATE TABLE IF NOT EXISTS monster_energy_bounds (
    bound_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    bound_name      TEXT NOT NULL,
    bound_value     REAL,
    bound_formula   TEXT,
    monster_coefficient INTEGER,
    status          TEXT NOT NULL DEFAULT 'hypothesis' CHECK (status IN ('hypothesis','verified','refuted'))
);

-- Table: mckay_thompson_coefficients
-- Role: McKay-Thompson coefficients as transition rules
CREATE TABLE IF NOT EXISTS mckay_thompson_coefficients (
    mt_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    conjugacy_class TEXT NOT NULL,         -- e.g., '1A', '2A', '3A'
    coefficient_n   INTEGER NOT NULL,
    coefficient_value INTEGER NOT NULL,
    transition_rule TEXT
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_mt_class ON mckay_thompson_coefficients(conjugacy_class);
CREATE INDEX IF NOT EXISTS idx_mt_n     ON mckay_thompson_coefficients(coefficient_n);

-- Seed data: Monster energy bound
INSERT INTO monster_energy_bounds (bound_name, bound_value, bound_formula, monster_coefficient, status) VALUES
('Monster Ceiling c_max', 8.0e33, 'max(Monster_coefficients)', 196883, 'hypothesis');

-- Seed data: selected McKay-Thompson coefficients
INSERT INTO mckay_thompson_coefficients (conjugacy_class, coefficient_n, coefficient_value, transition_rule) VALUES
('1A', 1, 196884, 'identity'),
('2A', 1, 43724,  'W/Z boson coupling'),
('3A', 1, 8424,   'quark sector coupling'),
('4A', 1, 2148,   'lepton sector coupling');
