-- ============================================================
-- Paper 99 — Unified Applied Forge Validation
-- Domain: Forge Validation / Receipt-Bound Verification
-- Cross-references: Paper 21-24 (forge systems), Paper 39 (standards)
-- ============================================================

-- Table: forge_validation
-- Role: Forge reader validated by comparison to known results.
--       Each validation step produces a receipt.
CREATE TABLE IF NOT EXISTS forge_validation (
    validation_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    forge_id        INTEGER NOT NULL,
    test_case       TEXT NOT NULL,
    expected_result TEXT,
    actual_result   TEXT,
    comparison_pass INTEGER DEFAULT 0,
    receipt_hash    TEXT,
    FOREIGN KEY (forge_id) REFERENCES forge_systems(forge_id)
);

-- Table: validation_receipts
-- Role: Receipt-bound validation records
CREATE TABLE IF NOT EXISTS validation_receipts (
    receipt_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    validation_id   INTEGER NOT NULL,
    receipt_hash    TEXT NOT NULL,
    validation_status TEXT,
    FOREIGN KEY (validation_id) REFERENCES forge_validation(validation_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_val_forge ON forge_validation(forge_id);

-- ============================================================
-- NEW MAPPED CLAIMS: Paper 99
-- ============================================================

CREATE TABLE IF NOT EXISTS mapped_claims_p99 (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_ref TEXT NOT NULL,
    claim_text TEXT NOT NULL,
    status TEXT NOT NULL,
    source_file TEXT NOT NULL
);

INSERT INTO mapped_claims_p99 (claim_ref, claim_text, status, source_file) VALUES
('99.1', '- Paper 99 (Applied Forge Validation) — the validation of the applied forge against the observer', 'I', 'mapped_file_claims_report.md');
