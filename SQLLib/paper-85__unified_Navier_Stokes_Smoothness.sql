-- ============================================================
-- Paper 85 — Unified Navier Stokes Smoothness
-- Domain: Navier-Stokes / Clay Millennium
-- Cross-references: Paper 07 (bridge), Paper 16 (continuum edge)
-- ============================================================

-- Table: navier_stokes_smoothness
-- Role: NS equations as continuum limit of lattice dynamics.
--       Existence and smoothness from bridge properties.
CREATE TABLE IF NOT EXISTS navier_stokes_smoothness (
    problem_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    dimension       INTEGER NOT NULL DEFAULT 3,
    claim           TEXT NOT NULL,
    bridge_approach INTEGER DEFAULT 1,
    lattice_substrate TEXT DEFAULT 'FLCR',
    structural_approach INTEGER DEFAULT 1,
    full_proof      INTEGER DEFAULT 0,
    status          TEXT DEFAULT 'structural_approach'
);

-- Table: ns_bridge_properties
-- Role: Bridge properties that imply smoothness
CREATE TABLE IF NOT EXISTS ns_bridge_properties (
    property_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    property_name   TEXT NOT NULL,
    implies_smoothness INTEGER DEFAULT 1
);

-- Seed data
INSERT INTO navier_stokes_smoothness (dimension, claim, status) VALUES
(3, 'Navier-Stokes existence and smoothness in 3D', 'structural_approach');

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 85
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p85 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p85 (claim_ref, claim_text, status, source_file) VALUES
('85.1', 'Paper 85 maps the Navier-Stokes smoothness (partial regularity, bounded)', 'I', 'mapped_file_claims_report.md');
