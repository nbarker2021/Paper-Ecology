
-- ============================================================
-- CrystalLib Database Schema
-- A-family paper series (paper-00 through paper-100)
-- LCR kernel, D/I/X claim taxonomy, CAM hashes, SHA-256
-- ============================================================

-- Papers: the 101 paper A-family series
CREATE TABLE IF NOT EXISTS papers (
    paper_number TEXT PRIMARY KEY CHECK (paper_number GLOB 'paper-[0-9][0-9]*'),
    title TEXT NOT NULL,
    word_count INTEGER DEFAULT 0,
    band TEXT CHECK (band IN ('A', 'B', 'C', 'D', 'E', 'F')),
    status TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'closed', 'archived', 'hold')),
    disposition TEXT NOT NULL DEFAULT 'active' CHECK (disposition IN ('active', 'superseded', 'withdrawn', 'merged')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Claims: D/I/X taxonomy (Data-backed / Interpretation / Fabrication)
CREATE TABLE IF NOT EXISTS claims (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL REFERENCES papers(paper_number) ON DELETE CASCADE,
    claim_text TEXT NOT NULL,
    claim_status TEXT NOT NULL DEFAULT 'D' CHECK (claim_status IN ('D', 'I', 'X')),
    cam_hash TEXT NOT NULL UNIQUE,  -- SHA-256 content address
    code_source TEXT,               -- reference to code artifact
    sql_source TEXT,                -- reference to SQL/query artifact
    verifier TEXT,                  -- who verified this claim
    status TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'verified', 'disputed', 'resolved', 'retracted')),
    disposition TEXT NOT NULL DEFAULT 'active' CHECK (disposition IN ('active', 'superseded', 'withdrawn')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crystals: content-addressed memory entries (CAM)
CREATE TABLE IF NOT EXISTS crystals (
    crystal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cam_hash TEXT NOT NULL UNIQUE,  -- SHA-256 of content
    content TEXT NOT NULL,          -- serialized crystal content (JSON or plain text)
    paper_number TEXT REFERENCES papers(paper_number) ON DELETE CASCADE,
    claim_id INTEGER REFERENCES claims(claim_id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'frozen', 'deprecated', 'purged'))
);

-- Receipts: verified / harvested / mapped / open
CREATE TABLE IF NOT EXISTS receipts (
    receipt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cam_hash TEXT NOT NULL REFERENCES crystals(cam_hash) ON DELETE CASCADE,
    crystal_id INTEGER REFERENCES crystals(crystal_id) ON DELETE SET NULL,
    status TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'verified', 'harvested', 'mapped', 'rejected')),
    verifier TEXT,
    checked_at TIMESTAMP,
    result TEXT,                    -- outcome or notes from verification
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Carriers: LCR kernel (L/C/R states, 8-state space, shell grading)
CREATE TABLE IF NOT EXISTS carriers (
    carrier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL REFERENCES papers(paper_number) ON DELETE CASCADE,
    L_state INTEGER NOT NULL DEFAULT 0 CHECK (L_state IN (0, 1)),  -- Left / Logic
    C_state INTEGER NOT NULL DEFAULT 0 CHECK (C_state IN (0, 1)),  -- Center / Constraint
    R_state INTEGER NOT NULL DEFAULT 0 CHECK (R_state IN (0, 1)),  -- Right / Result
    shell INTEGER NOT NULL DEFAULT 0 CHECK (shell >= 0),          -- shell grading (depth/nesting)
    reversal INTEGER NOT NULL DEFAULT 0 CHECK (reversal IN (0, 1)), -- polarity reversal flag
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'terminated')),
    -- 8-state space is encoded as LCR bits (0-7): shell provides additional grading
    state_code INTEGER GENERATED ALWAYS AS (L_state * 4 + C_state * 2 + R_state) STORED,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Ribbons: 8-slot state vectors (slot_0..slot_7), arity, hash
CREATE TABLE IF NOT EXISTS ribbons (
    ribbon_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL REFERENCES papers(paper_number) ON DELETE CASCADE,
    slot_0 INTEGER DEFAULT 0 CHECK (slot_0 IN (0, 1)),
    slot_1 INTEGER DEFAULT 0 CHECK (slot_1 IN (0, 1)),
    slot_2 INTEGER DEFAULT 0 CHECK (slot_2 IN (0, 1)),
    slot_3 INTEGER DEFAULT 0 CHECK (slot_3 IN (0, 1)),
    slot_4 INTEGER DEFAULT 0 CHECK (slot_4 IN (0, 1)),
    slot_5 INTEGER DEFAULT 0 CHECK (slot_5 IN (0, 1)),
    slot_6 INTEGER DEFAULT 0 CHECK (slot_6 IN (0, 1)),
    slot_7 INTEGER DEFAULT 0 CHECK (slot_7 IN (0, 1)),
    arity INTEGER NOT NULL DEFAULT 0 CHECK (arity >= 0 AND arity <= 8),  -- number of active slots
    hash TEXT NOT NULL,  -- SHA-256 of the slot vector
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'frozen', 'void')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Ledgers: event log for papers and claims
CREATE TABLE IF NOT EXISTS ledgers (
    ledger_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type TEXT NOT NULL CHECK (event_type IN (
        'claim_added', 'claim_verified', 'claim_disputed', 'claim_resolved',
        'crystal_created', 'receipt_issued', 'carrier_updated', 'ribbon_woven',
        'obligation_created', 'obligation_resolved', 'snapshot_taken', 'theorem_proven',
        'cross_ref_added', 'paper_status_changed', 'paper_merged'
    )),
    paper_number TEXT REFERENCES papers(paper_number) ON DELETE SET NULL,
    claim_id INTEGER REFERENCES claims(claim_id) ON DELETE SET NULL,
    event_data TEXT,  -- JSON blob of event details
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Obligations: open obligations with owners and paper references
CREATE TABLE IF NOT EXISTS obligations (
    obligation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT REFERENCES papers(paper_number) ON DELETE SET NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'in_progress', 'blocked', 'resolved', 'cancelled')),
    owner TEXT NOT NULL,  -- who owns this obligation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP
);

-- Snapshots: point-in-time captures of paper data
CREATE TABLE IF NOT EXISTS snapshots (
    snapshot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL REFERENCES papers(paper_number) ON DELETE CASCADE,
    data TEXT NOT NULL,  -- JSON snapshot of relevant state
    hash TEXT NOT NULL,  -- SHA-256 of data
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Theorems: formal theorem statements and proofs
CREATE TABLE IF NOT EXISTS theorems (
    theorem_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL REFERENCES papers(paper_number) ON DELETE CASCADE,
    theorem_name TEXT NOT NULL,
    statement TEXT NOT NULL,
    proof TEXT,
    status TEXT NOT NULL DEFAULT 'conjecture' CHECK (status IN ('conjecture', 'proven', 'disproven', 'pending_review')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cross-references: linking between papers and claims
CREATE TABLE IF NOT EXISTS cross_references (
    xref_id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_paper TEXT NOT NULL REFERENCES papers(paper_number) ON DELETE CASCADE,
    to_paper TEXT NOT NULL REFERENCES papers(paper_number) ON DELETE CASCADE,
    claim_id INTEGER REFERENCES claims(claim_id) ON DELETE SET NULL,
    type TEXT NOT NULL DEFAULT 'general' CHECK (type IN (
        'general', 'cites', 'depends_on', 'supersedes', 'contradicts', 'extends', 'proves'
    )),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (from_paper, to_paper, claim_id, type)
);

-- Indexes for common query patterns
CREATE INDEX IF NOT EXISTS idx_claims_paper ON claims(paper_number);
CREATE INDEX IF NOT EXISTS idx_claims_status ON claims(claim_status);
CREATE INDEX IF NOT EXISTS idx_crystals_paper ON crystals(paper_number);
CREATE INDEX IF NOT EXISTS idx_crystals_claim ON crystals(claim_id);
CREATE INDEX IF NOT EXISTS idx_receipts_status ON receipts(status);
CREATE INDEX IF NOT EXISTS idx_carriers_paper ON carriers(paper_number);
CREATE INDEX IF NOT EXISTS idx_carriers_state ON carriers(state_code);
CREATE INDEX IF NOT EXISTS idx_ribbons_paper ON ribbons(paper_number);
CREATE INDEX IF NOT EXISTS idx_ledgers_paper ON ledgers(paper_number);
CREATE INDEX IF NOT EXISTS idx_ledgers_event ON ledgers(event_type);
CREATE INDEX IF NOT EXISTS idx_obligations_status ON obligations(status);
CREATE INDEX IF NOT EXISTS idx_obligations_owner ON obligations(owner);
CREATE INDEX IF NOT EXISTS idx_snapshots_paper ON snapshots(paper_number);
CREATE INDEX IF NOT EXISTS idx_theorems_paper ON theorems(paper_number);
CREATE INDEX IF NOT EXISTS idx_xrefs_from ON cross_references(from_paper);
CREATE INDEX IF NOT EXISTS idx_xrefs_to ON cross_references(to_paper);
