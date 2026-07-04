-- ============================================================
-- Paper 66 — Unified GR Side 2 Black Hole Entropy
-- Domain: Black Hole Entropy / Information Paradox
-- Cross-references: Paper 14 (repair curvature), Paper 65 (EFE)
-- ============================================================

-- Table: black_hole_entropy
-- Role: Bekenstein-Hawking entropy from boundary repair.
--       Horizon = typed boundary. Entropy = receipt of repair.
CREATE TABLE IF NOT EXISTS black_hole_entropy (
    bh_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    bh_name         TEXT,
    mass_solar      REAL,
    horizon_area    REAL,                  -- Planck units
    entropy_s       REAL,                  -- S = A / 4G
    entropy_from_repair REAL,              -- FLCR derivation
    information_paradox_status TEXT DEFAULT 'resolved_by_receipt',
    receipt_hash    TEXT
);

-- Table: horizon_boundaries
-- Role: Typed boundaries at black hole horizons
CREATE TABLE IF NOT EXISTS horizon_boundaries (
    horizon_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    bh_id           INTEGER NOT NULL,
    boundary_type   TEXT CHECK (boundary_type IN ('event','apparent','Cauchy')),
    repair_curvature REAL,
    temperature_k   REAL,                  -- Hawking temperature
    FOREIGN KEY (bh_id) REFERENCES black_hole_entropy(bh_id)
);

-- Seed data: black hole entropy
INSERT INTO black_hole_entropy (bh_name, mass_solar, horizon_area, entropy_s, information_paradox_status) VALUES
('Schwarzschild M=1', 1.0, 1.0e77, 1.0e77, 'resolved_by_receipt'),
('Sagittarius A*',    4.0e6, 4.0e83, 1.0e84, 'resolved_by_receipt');
