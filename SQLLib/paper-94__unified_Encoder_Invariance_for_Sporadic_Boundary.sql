-- ============================================================
-- Paper 94 — Unified Encoder Invariance For Sporadic Boundary
-- Domain: Encoder Invariance / Application Band
-- Cross-references: Paper 76 (encoder invariance), Paper 11 (admission)
-- ============================================================

-- Table: encoder_invariance_theorem
-- Role: FLCR substrate invariant under encoder choice.
--       D4 codec canonical. Arf-matching + D12 action proof.
CREATE TABLE IF NOT EXISTS encoder_invariance_theorem (
    theorem_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    theorem_name    TEXT NOT NULL DEFAULT 'Encoder Invariance Theorem',
    statement       TEXT NOT NULL,
    canonical_basis TEXT DEFAULT 'D4_axis_sheet',
    arf_matching_proof INTEGER DEFAULT 1,
    d12_equivariant INTEGER DEFAULT 1,
    structural_proof INTEGER DEFAULT 1,
    full_formal_proof INTEGER DEFAULT 0,
    status          TEXT DEFAULT 'structural_proof'
);

-- Table: d4_encoder_invariance_tests
-- Role: Explicit D4 encoder invariance tests
CREATE TABLE IF NOT EXISTS d4_encoder_invariance_tests (
    test_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    encoder_variant TEXT NOT NULL,
    arf_invariant   INTEGER DEFAULT 1,
    d12_equivariant INTEGER DEFAULT 1,
    admissibility_preserved INTEGER DEFAULT 1
);

-- Seed data
INSERT INTO encoder_invariance_theorem (statement, status) VALUES
('The FLCR substrate is invariant under the choice of D4-equivariant encoder', 'structural_proof');

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 94
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p94 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p94 (claim_ref, claim_text, status, source_file) VALUES
('94.1', 'Each rung of the ladder corresponds to a layer of Spectre tiles with increasing complexi', 'I', 'mapped_file_claims_report.md');
INSERT INTO mapped_claims_p94 (claim_ref, claim_text, status, source_file) VALUES
('94.2', 'Papers 90–95: the McKay-Thompson mapping (Paper 90) is bounded empirical (CONJ); the Niemeier glue (Paper 91) is structural proposal (CONJ); the F4 universality (Paper 92) is open; the cold-start terminal (Paper 93) is bounded (O(log n)); the encoder invariance (Paper 94) is bounded (crystal structure); the SPINOR observation (Paper 95) is bounded (quantum gate simulation)', 'I', 'mapped_file_claims_report.md');
