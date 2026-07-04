-- ============================================================
-- Paper 78 — Unified Governance 1 Bibliography Taxonomy Governance
-- Domain: Governance / Claim-Layer Framework
-- Cross-references: Paper 39 (standards), Paper 79 (routing),
--                   Paper 80 (2-category L)
-- ============================================================

-- Table: governance_framework
-- Role: Every claim typed, every receipt content-addressed,
--       every falsifier named, every gap open.
CREATE TABLE IF NOT EXISTS governance_framework (
    framework_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_name       TEXT NOT NULL,
    rule_description TEXT NOT NULL,
    enforcement_level TEXT CHECK (enforcement_level IN ('mandatory','recommended','informational'))
);

-- Table: bibliography_taxonomy
-- Role: Taxonomy of all sources and citations
CREATE TABLE IF NOT EXISTS bibliography_taxonomy (
    bib_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    citation_key    TEXT NOT NULL,
    source_type     TEXT CHECK (source_type IN ('paper','book','dataset','software','personal_communication')),
    claim_lanes     TEXT,                  -- JSON array of lane_ids
    verified        INTEGER DEFAULT 0
);

-- Seed data: governance rules
INSERT INTO governance_framework (rule_name, rule_description, enforcement_level) VALUES
('Claim Typing', 'Every claim must be typed D/I/X', 'mandatory'),
('Receipt CA',   'Every receipt must be content-addressed', 'mandatory'),
('Falsifier Naming', 'Every claim must have a named falsifier', 'mandatory'),
('Gap Tracking', 'Every open gap must be explicitly tracked', 'mandatory'),
('Lane Assignment', 'Every claim must be assigned to a claim lane', 'mandatory');
