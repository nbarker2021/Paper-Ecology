"""
build_crystal_lib.py
CrystalLib SQLite Database Builder
A-family paper series (paper-00 through paper-100)
LCR kernel, D/I/X claim taxonomy, CAM hashes, SHA-256 content addressing
"""

import sqlite3
import hashlib
import json
from datetime import datetime
from pathlib import Path

DB_PATH = Path("D:/Paper Ecology/CrystalLib/crystal_lib.db")
SCHEMA_SQL_PATH = Path("D:/Paper Ecology/CrystalLib/crystal_lib_schema.sql")

SCHEMA = """
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
"""


def sha256_content(text: str) -> str:
    """Compute SHA-256 content address for CAM."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def init_database():
    """Create the SQLite database and schema."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Apply schema
    cursor.executescript(SCHEMA)
    conn.commit()
    print(f"[OK] Schema applied to {DB_PATH}")

    # Save schema to SQL file for reference
    SCHEMA_SQL_PATH.write_text(SCHEMA, encoding="utf-8")
    print(f"[OK] Schema written to {SCHEMA_SQL_PATH}")

    return conn, cursor


def populate_papers(cursor):
    """Populate the papers table with the 101 A-family entries (paper-00 to paper-100)."""
    rows = []
    for i in range(101):
        paper_num = f"paper-{i:02d}"
        title = f"A-family paper {i:02d} — placeholder title"
        word_count = 0
        band = "A"
        status = "open"
        disposition = "active"
        rows.append((paper_num, title, word_count, band, status, disposition))

    cursor.executemany(
        """
        INSERT INTO papers (paper_number, title, word_count, band, status, disposition)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(paper_number) DO NOTHING;
        """,
        rows,
    )
    print(f"[OK] Inserted/updated {len(rows)} papers (paper-00 to paper-100).")


def populate_demo_claims(cursor, conn):
    """Insert a few demo claims to show D/I/X taxonomy and CAM hashes."""
    demo_claims = [
        ("paper-00", "Claim: The LCR kernel forms an 8-state space.", "D", "kernel-8-state"),
        ("paper-00", "Interpretation: shell grading correlates with proof depth.", "I", "shell-depth-corr"),
        ("paper-01", "Data: carrier reversal flips L_state polarity.", "D", "reversal-polarity"),
        ("paper-01", "Fabrication: ribbons encode quantum amplitudes.", "X", "quantum-ribbons"),
    ]
    for paper_number, claim_text, claim_status, tag in demo_claims:
        cam_hash = sha256_content(f"{paper_number}:{claim_text}:{tag}")
        cursor.execute(
            """
            INSERT INTO claims (paper_number, claim_text, claim_status, cam_hash, code_source, sql_source, verifier, status, disposition)
            VALUES (?, ?, ?, ?, NULL, NULL, 'system', 'open', 'active')
            ON CONFLICT(cam_hash) DO NOTHING;
            """,
            (paper_number, claim_text, claim_status, cam_hash),
        )
    conn.commit()
    print(f"[OK] Inserted {len(demo_claims)} demo claims.")


def populate_demo_crystals(cursor, conn):
    """Insert demo crystals linked to claims."""
    cursor.execute("SELECT claim_id, cam_hash, paper_number FROM claims LIMIT 4;")
    claims = cursor.fetchall()
    for claim_id, claim_hash, paper_number in claims:
        content = json.dumps({"note": "Demo crystal", "claim_hash": claim_hash})
        cam_hash = sha256_content(content)
        cursor.execute(
            """
            INSERT INTO crystals (cam_hash, content, paper_number, claim_id, status)
            VALUES (?, ?, ?, ?, 'active')
            ON CONFLICT(cam_hash) DO NOTHING;
            """,
            (cam_hash, content, paper_number, claim_id),
        )
    conn.commit()
    print(f"[OK] Inserted {len(claims)} demo crystals.")


def populate_demo_carriers(cursor, conn):
    """Insert demo carriers to illustrate LCR 8-state space."""
    demos = [
        ("paper-00", 0, 0, 0, 0, 0),  # state 0
        ("paper-00", 0, 0, 1, 1, 0),  # state 1
        ("paper-00", 0, 1, 0, 0, 1),  # state 2, reversal
        ("paper-00", 1, 1, 1, 2, 0),  # state 7, shell 2
    ]
    for paper_number, L, C, R, shell, reversal in demos:
        cursor.execute(
            """
            INSERT INTO carriers (paper_number, L_state, C_state, R_state, shell, reversal, status)
            VALUES (?, ?, ?, ?, ?, ?, 'active')
            ON CONFLICT DO NOTHING;
            """,
            (paper_number, L, C, R, shell, reversal),
        )
    conn.commit()
    print(f"[OK] Inserted {len(demos)} demo carriers.")


def populate_demo_ribbons(cursor, conn):
    """Insert demo ribbons with 8-slot vectors."""
    demos = [
        ("paper-00", 1, 0, 1, 0, 1, 0, 1, 0, 4),  # arity 4
        ("paper-00", 1, 1, 1, 1, 0, 0, 0, 0, 4),  # arity 4
    ]
    for paper_number, *slots, arity in demos:
        slot_str = "".join(str(s) for s in slots)
        hash_val = sha256_content(f"{paper_number}:{slot_str}")
        cursor.execute(
            """
            INSERT INTO ribbons (paper_number, slot_0, slot_1, slot_2, slot_3, slot_4, slot_5, slot_6, slot_7, arity, hash, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'active')
            ON CONFLICT DO NOTHING;
            """,
            (paper_number, *slots, arity, hash_val),
        )
    conn.commit()
    print(f"[OK] Inserted {len(demos)} demo ribbons.")


def populate_demo_obligations(cursor, conn):
    """Insert demo obligations."""
    demos = [
        ("paper-00", "Define the LCR kernel formalism in full.", "open", "architect"),
        ("paper-01", "Prove that reversal flips L_state correctly.", "open", "architect"),
    ]
    for paper_number, desc, status, owner in demos:
        cursor.execute(
            """
            INSERT INTO obligations (paper_number, description, status, owner)
            VALUES (?, ?, ?, ?)
            ON CONFLICT DO NOTHING;
            """,
            (paper_number, desc, status, owner),
        )
    conn.commit()
    print(f"[OK] Inserted {len(demos)} demo obligations.")


def populate_demo_theorems(cursor, conn):
    """Insert demo theorems."""
    demos = [
        ("paper-00", "LCR Completeness", "The LCR kernel spans all 8 states.", "Proof by enumeration of L_state x C_state x R_state.", "proven"),
    ]
    for paper_number, name, statement, proof, status in demos:
        cursor.execute(
            """
            INSERT INTO theorems (paper_number, theorem_name, statement, proof, status)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT DO NOTHING;
            """,
            (paper_number, name, statement, proof, status),
        )
    conn.commit()
    print(f"[OK] Inserted {len(demos)} demo theorems.")


def populate_demo_cross_references(cursor, conn):
    """Insert demo cross-references."""
    demos = [
        ("paper-00", "paper-01", None, "depends_on"),
        ("paper-01", "paper-00", None, "cites"),
    ]
    for from_paper, to_paper, claim_id, type_ in demos:
        cursor.execute(
            """
            INSERT INTO cross_references (from_paper, to_paper, claim_id, type)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(from_paper, to_paper, claim_id, type) DO NOTHING;
            """,
            (from_paper, to_paper, claim_id, type_),
        )
    conn.commit()
    print(f"[OK] Inserted {len(demos)} demo cross-references.")


def verify_schema(cursor):
    """Print table names and row counts for verification."""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    tables = [row[0] for row in cursor.fetchall()]
    print("\n--- Schema Verification ---")
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table};")
        count = cursor.fetchone()[0]
        print(f"  {table:25s} | {count:5d} rows")
    print("--- End Verification ---\n")


def main():
    print("=" * 60)
    print("CrystalLib Database Builder")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 60)

    conn, cursor = init_database()

    populate_papers(cursor)
    conn.commit()

    populate_demo_claims(cursor, conn)
    populate_demo_crystals(cursor, conn)
    populate_demo_carriers(cursor, conn)
    populate_demo_ribbons(cursor, conn)
    populate_demo_obligations(cursor, conn)
    populate_demo_theorems(cursor, conn)
    populate_demo_cross_references(cursor, conn)

    verify_schema(cursor)

    conn.close()
    print(f"[DONE] Database ready at: {DB_PATH}")
    print(f"[DONE] Schema SQL saved at: {SCHEMA_SQL_PATH}")


if __name__ == "__main__":
    main()
