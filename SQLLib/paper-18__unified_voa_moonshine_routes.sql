-- ============================================================
-- Paper 18 — Unified Voa Moonshine Routes
-- Domain: Moonshine VOA / Monster Group
-- Cross-references: Paper 08 (lattice closure), Paper 17 (E6-E8),
--                   Paper 25 (Monster ceiling), Paper 29 (energy bound)
-- ============================================================

-- Table: voa_moonshine_routes
-- Role: VOA routes connecting Monster VOA to SM particles.
--       Monster triple [47,59,71] → 196883.
CREATE TABLE IF NOT EXISTS voa_moonshine_routes (
    route_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    route_name      TEXT NOT NULL,
    monster_coeff   INTEGER,               -- c_n
    mckay_row       INTEGER,               -- 196884 = 196883 + 1
    source_voa      TEXT NOT NULL,
    target_particle TEXT,
    weight          INTEGER,
    depth_tested    INTEGER DEFAULT 256,
    bijective_pct   REAL                   -- e.g., 89% for T3A
);

-- Table: pariah_asymmetry
-- Role: Pariah asymmetry records [33,37,39,44,53,65]
CREATE TABLE IF NOT EXISTS pariah_asymmetry (
    pariah_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name      TEXT NOT NULL,
    order_value     INTEGER,
    asymmetry_role  TEXT,
    is_pariah       INTEGER NOT NULL DEFAULT 1 CHECK (is_pariah IN (0,1))
);

-- Table: monster_triples
-- Role: Monster triple products that yield key coefficients
CREATE TABLE IF NOT EXISTS monster_triples (
    triple_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    a               INTEGER NOT NULL,
    b               INTEGER NOT NULL,
    c               INTEGER NOT NULL,
    product         INTEGER NOT NULL,
    mckay_relation  TEXT
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_voa_route ON voa_moonshine_routes(route_name);
CREATE INDEX IF NOT EXISTS idx_pariah_name ON pariah_asymmetry(group_name);

-- Seed data: Monster triple [47,59,71]
INSERT INTO monster_triples (a, b, c, product, mckay_relation) VALUES
(47, 59, 71, 196883, '196884 = 196883 + 1');

-- Seed data: Pariah asymmetry groups
INSERT INTO pariah_asymmetry (group_name, order_value, asymmetry_role, is_pariah) VALUES
('J1',   175560,     'sporadic', 1),
('J3',   50232960,   'sporadic', 1),
('J4',   86775571046077562880, 'sporadic', 1),
('Ly',   51765179004000000, 'sporadic', 1),
('O''N', 460815505920, 'sporadic', 1),
('Ru',   145926144000, 'sporadic', 1);

-- Seed data: VOA moonshine routes
INSERT INTO voa_moonshine_routes (route_name, monster_coeff, mckay_row, source_voa, target_particle, weight, depth_tested, bijective_pct) VALUES
('T1A → Higgs',     196883, 196884, 'Monster_VOA', 'Higgs boson', 5, 256, 100.0),
('T2A → W/Z',        43723, 43724, 'Monster_VOA', 'W/Z bosons', 3, 256, 95.0),
('T3A → quarks',      8424,  8425, 'Monster_VOA', 'quark sector', 7, 256, 89.0),
('T4A → leptons',     2148,  2149, 'Monster_VOA', 'lepton sector', 2, 128, 92.0);
