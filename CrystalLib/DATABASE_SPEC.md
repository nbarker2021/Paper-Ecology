# CrystalLib Database Specification

**Version:** 1.0  
**Date:** 2026-07-04  
**Workspace:** `D:\Paper Ecology\CrystalLib`  
**Source:** `CRYSTAL_CAM_PROJECTOR_SUPPLEMENT` (CQE_CMPLX active-rework corpus)  
**Convention:** A-family naming (`paper-00` through `paper-100`)  
**Kernel:** LCR triality (`L_state`, `C_state`, `R_state`)  
**Claim Taxonomy:** D / I / X  
**Content Addressing:** SHA-256 (`cam_hash`)

---

## 1. Purpose & Scope

This document defines the canonical SQLite schema for **CrystalLib**, the data home for crystal CAM (Content-Addressed Memory) memory files. The schema is derived from the **CRYSTAL CAM PROJECTOR SUPPLEMENT** (2,366-line archive/mirror intake log and spine routing registry) and is designed to be fully compatible with the existing A-family naming conventions established in `PaperLib`, `CAMLib`, `CodeLib`, and `SQLLib`.

### 1.1 What the Supplement Contains

The `CRYSTAL_CAM_PROJECTOR_SUPPLEMENT` is the master routing surface for the CQE_CMPLX corpus. It records:

- **Primary spine papers:** 06, 10, 12, 20, 30, 32 (causal edges, T10 receipt, CA prediction, Layer-2 synthesis, Grand Ribbon, Supervisor Cursor).
- **Operating model:** Enumerate addressable faces → project through editable playbook → write vignettes and CAM receipts → route next algorithms (obligation router, verifier reconciler, variant incorporator, receipt auditor).
- **Archive/mirror intake log:** ~200+ source cards, each with `source_path`, `archive_score` (60–101), `what_it_contributes`, `routed_spine_papers`, and `integration_action`.
- **Status taxonomy:** `pass`, `pass_with_open_obligations`, `pass_with_open_lifts`, `pass_with_open_packaging_obligations`, `pass_with_validation_obligations`, `pass_with_interpretive_obligations`, `real_data_bound_hypothesis_tested_and_refuted`, `open_deferred_until_lab_dataset`, etc.
- **Claim contract taxonomy:** Every paper has a `.50` claim contract that defines what promotions are allowed vs. rejected (e.g., `candidate_estimate` → `measured_material_property` is forbidden).
- **LCR kernel:** The 8-state `(L, C, R)` chart is the universal carrier; shell grading provides depth; the `2 + 6` VOA sector pattern and `S3` anneal closure (`≤ 3` steps) are invariant.
- **Grand Ribbon 8-slot schema:** `C, L, R, B, T, O, W, A` (center, left, right, boundary rule, tool transform, obligation set, workbook analogue, anchor).
- **Open obligations manifest:** A complete empirical platform diagnostic system tracking 2×2 failure points.
- **Receipt discipline:** Every claim must carry a SHA-256 content-addressed receipt, a verifier path, and a falsifier.

### 1.2 B-Family Strip & Map Rules

All B-family identifiers in the supplement are mapped to A-family equivalents in this schema:

| B-family source | A-family mapping | Action |
|---|---|---|
| `CQE-paper-NN` | `paper-NN` | Strip prefix, zero-pad to 2 digits |
| `CQE-paper-NN.XX` | `paper-NN` (supplement) | Store as `paper_number` + `variant` suffix in `archive_intake` |
| `Paper_NN_Title` | `paper-NN` | Normalize via regex extraction |
| `CQE-PAPER-0NN` | `paper-0NN` | Direct zero-pad mapping |
| `ΣN` / `SIGMA` papers | `paper-30` meta-framer | Route through `spine_routing` table |
| `FORMAL_UNIFICATION_CHARTER` | `paper-00` axioms | Charter is intake evidence, not a separate paper |
| `block-NN-dyad-XX-YY` | `paper-XX`, `paper-YY` | Expand into cross-references |
| `receipt.json` (raw) | `receipts` table | Ingest with SHA-256 cam_hash |
| `CLAIM_CROSSWALK.csv` | `claims` + `cross_references` | Normalize claim IDs to A-family |
| `OPEN_OBLIGATIONS.csv` | `obligations` table | Ingest row-by-row with owner=`system` |
| Archive scores (60–101) | `archive_intake.archive_score` | Preserved as metadata, not primary key |
| `status=computed` / `promoted` | `claims.status='verified'` / `papers.status='closed'` | Map to A-family status enum |
| `status=open_deferred_until_*` | `obligations.status='open'` | Route to obligations table |

**Forbidden in schema:** Any column name, table name, or enum value that embeds `CQE-`, `CMPLX-`, `B-`, `Sigma`, or legacy B-family band labels. Only `paper-00` through `paper-100` are valid paper references.

---

## 2. Entity Relationship Overview

```text
papers (1) ───< claims (N)
   │
   ├──< crystals (N) ──< receipts (N)
   │
   ├──< carriers (N)        [LCR kernel state]
   │
   ├──< ribbons (N)         [8-slot vectors]
   │
   ├──< snapshots (N)       [point-in-time capture]
   │
   ├──< obligations (N)     [open/closed obligations]
   │
   ├──< theorems (N)        [formal theorem registry]
   │
   ├──< faces (N)           [enumerated addressable faces]
   │
   ├──< vignettes (N)       [vignette enumeration]
   │
   └──< transport_obligations (N) [typed transport rows]

claims (1) ──< crystals (N)
claims (1) ──< cross_references (N)

cam_hashes (1) ──< crystals (N) [content-addressed registry]
cam_hashes (1) ──< claims (N)

spine_routing (N) ──> papers (1) [spine owner]
archive_intake (N) ──> papers (M) [via routed_spine_papers JSON]

ledgers (N) ──> papers (1) [event log]
ledgers (N) ──> claims (1) [event log]
```

---

## 3. SQLite Schema Definition

### 3.1 papers — The 101 Paper A-Family Series

Maps the A-family spine (`paper-00` through `paper-100`). This is the root table; every other table references it via `paper_number`.

```sql
CREATE TABLE IF NOT EXISTS papers (
    paper_number TEXT PRIMARY KEY
        CHECK (paper_number GLOB 'paper-[0-9][0-9]*'),
    title TEXT NOT NULL DEFAULT 'Untitled',
    word_count INTEGER DEFAULT 0,
    band TEXT CHECK (band IN ('A', 'B', 'C', 'D', 'E', 'F')),
    status TEXT NOT NULL DEFAULT 'open'
        CHECK (status IN ('open', 'closed', 'archived', 'hold')),
    disposition TEXT NOT NULL DEFAULT 'active'
        CHECK (disposition IN ('active', 'superseded', 'withdrawn', 'merged')),
    archive_score INTEGER CHECK (archive_score BETWEEN 0 AND 101),
    source_path TEXT,               -- original source file path (read-only audit)
    spine_owner INTEGER DEFAULT 0   -- 1 if this paper is a primary spine owner
        CHECK (spine_owner IN (0, 1)),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Notes:**
- `archive_score` is imported from the supplement's intake log (range 60–101 in the source; normalized to 0–101).
- `spine_owner` flags the six primary spine papers (06, 10, 12, 20, 30, 32) as identified in the supplement.
- `source_path` preserves the original B-family path for auditability without polluting the A-family namespace.

---

### 3.2 claims — D / I / X Claim Taxonomy

Each claim row is content-addressed by `cam_hash` and tagged with the D/I/X taxonomy derived from the supplement's claim-contract discipline:

- **D** = Data-backed (exact, finite, verified)
- **I** = Interpretation (honest but not yet proven)
- **X** = Fabrication / rejected promotion (explicitly forbidden by claim contract)

```sql
CREATE TABLE IF NOT EXISTS claims (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    claim_number TEXT,              -- e.g., "C-06.1" for Paper 06 Claim 1
    claim_text TEXT NOT NULL,
    claim_status TEXT NOT NULL DEFAULT 'D'
        CHECK (claim_status IN ('D', 'I', 'X')),
    cam_hash TEXT NOT NULL UNIQUE,  -- SHA-256 content address of claim_text
    code_source TEXT,               -- reference to CodeLib artifact
    sql_source TEXT,                -- reference to SQLLib artifact
    verifier TEXT,                  -- verifier name / script path
    receipt_path TEXT,              -- path to JSON receipt file
    falsifier TEXT,                 -- falsification condition (from claim contract)
    boundary TEXT,                  -- explicit boundary note (e.g., "open lift")
    status TEXT NOT NULL DEFAULT 'open'
        CHECK (status IN ('open', 'verified', 'disputed', 'resolved', 'retracted')),
    disposition TEXT NOT NULL DEFAULT 'active'
        CHECK (disposition IN ('active', 'superseded', 'withdrawn')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Notes:**
- `claim_number` is optional but recommended for tracking claim IDs like `O-32.1` from the supplement.
- `falsifier` and `boundary` are drawn directly from the supplement's claim-contract entries (e.g., Paper 29.50's physical-claim-flag and falsifier requirements).
- `receipt_path` stores the JSON receipt location (e.g., `production/formal-papers/CQE-paper-10/t10_master_receipt.json` mapped to A-family path).

---

### 3.3 cam_hashes — Content-Addressed Memory Registry

Central registry for all SHA-256 content addresses. Every crystal, claim, receipt, and snapshot must register its hash here for integrity auditing.

```sql
CREATE TABLE IF NOT EXISTS cam_hashes (
    cam_hash TEXT PRIMARY KEY,      -- SHA-256 hex digest (64 chars)
    content_type TEXT NOT NULL
        CHECK (content_type IN ('crystal', 'claim', 'receipt', 'snapshot', 'theorem', 'face', 'vignette')),
    byte_size INTEGER DEFAULT 0,
    source_path TEXT,               -- original file path (audit trail)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Notes:**
- This is the canonical CAM table referenced by the supplement's "CAM writeback and receipt discipline."
- All `cam_hash` columns in other tables are foreign keys to this table (enforced via application logic; SQLite does not support foreign keys across columns that are not PRIMARY KEY or UNIQUE in the referenced table without `REFERENCES` clause, which we enforce here since `cam_hash` is PK).

---

### 3.4 crystals — Content-Addressed Memory Entries

A **crystal** is a serialized content object (JSON, plain text, or binary blob) stored by its SHA-256 hash. Crystals are the core CAM artifact in the supplement's operating model.

```sql
CREATE TABLE IF NOT EXISTS crystals (
    crystal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cam_hash TEXT NOT NULL UNIQUE
        REFERENCES cam_hashes(cam_hash) ON DELETE CASCADE,
    content TEXT NOT NULL,          -- serialized crystal content
    paper_number TEXT
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    claim_id INTEGER
        REFERENCES claims(claim_id) ON DELETE SET NULL,
    face_id INTEGER,                -- link to enumerated face (if applicable)
    vignette_id INTEGER,            -- link to vignette (if applicable)
    status TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'frozen', 'deprecated', 'purged')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Notes:**
- `content` is the raw serialized form. For large binaries, store a base64 encoding or an external path reference.
- `face_id` and `vignette_id` link to the `faces` and `vignettes` tables defined in §3.12–3.13.

---

### 3.5 receipts — Verification Receipts

Receipts track the verification status of crystals. The supplement uses a rich receipt taxonomy (e.g., `pass_with_open_obligations`, `pass_with_open_lifts`). This table captures that taxonomy.

```sql
CREATE TABLE IF NOT EXISTS receipts (
    receipt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cam_hash TEXT NOT NULL
        REFERENCES cam_hashes(cam_hash) ON DELETE CASCADE,
    crystal_id INTEGER
        REFERENCES crystals(crystal_id) ON DELETE SET NULL,
    claim_id INTEGER
        REFERENCES claims(claim_id) ON DELETE SET NULL,
    status TEXT NOT NULL DEFAULT 'open'
        CHECK (status IN (
            'open',
            'verified',
            'harvested',
            'mapped',
            'rejected',
            'pass',
            'pass_with_open_obligations',
            'pass_with_open_lifts',
            'pass_with_open_packaging_obligations',
            'pass_with_validation_obligations',
            'pass_with_interpretive_obligations',
            'partial',
            'fail'
        )),
    verifier TEXT,                  -- verifier script or agent name
    checked_at TIMESTAMP,
    result TEXT,                    -- JSON or free-text outcome
    open_obligations_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Notes:**
- The extended `status` enum maps directly to the supplement's receipt statuses (e.g., `pass_with_open_obligations` from Paper 21, `pass_with_open_lifts` from Paper 20, etc.).
- `open_obligations_count` is pre-computed from the receipt for fast querying.

---

### 3.6 carriers — LCR Kernel States

The **carrier** is the LCR triality state: `(L_state, C_state, R_state)` ∈ `{0,1}³` (8-state chart). The supplement defines shell grading, reversal, and `S3` anneal closure.

```sql
CREATE TABLE IF NOT EXISTS carriers (
    carrier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    L_state INTEGER NOT NULL DEFAULT 0
        CHECK (L_state IN (0, 1)),  -- Left / Logic / Pre-state
    C_state INTEGER NOT NULL DEFAULT 0
        CHECK (C_state IN (0, 1)),  -- Center / Constraint / Active coordinate
    R_state INTEGER NOT NULL DEFAULT 0
        CHECK (R_state IN (0, 1)),  -- Right / Result / Post-state
    shell INTEGER NOT NULL DEFAULT 0
        CHECK (shell >= 0 AND shell <= 24),  -- shell grading: 0,1,2,3...24 (K_max=9, extensible)
    reversal INTEGER NOT NULL DEFAULT 0
        CHECK (reversal IN (0, 1)),  -- rho(L,C,R) = (R,C,L)
    anneal_steps INTEGER DEFAULT 0
        CHECK (anneal_steps >= 0 AND anneal_steps <= 3),  -- S3 anneal bound: ≤ 3
    rest_state INTEGER DEFAULT 0
        CHECK (rest_state IN (0, 1)),  -- 1 if L = R (Lie-conjugate attractor)
    state_code INTEGER GENERATED ALWAYS AS (
        L_state * 4 + C_state * 2 + R_state
    ) STORED,  -- 0..7 encoding
    status TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'suspended', 'terminated')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Notes:**
- `shell` is bounded to 24 in the schema to match the supplement's lattice chain (`1 → 3 → 7 → 8 → 24 → 72`), with `K_max = 9` as a practical working bound.
- `anneal_steps` captures the supplement's `≤ 3` S3 transposition closure bound.
- `rest_state` is 1 when `L_state = R_state` (the four Lie-conjugate attractors).

---

### 3.7 ribbons — 8-Slot Grand Ribbon Vectors

The supplement's **Grand Ribbon** (Paper 30) uses an 8-slot structure per paper position: `C, L, R, B, T, O, W, A`. This table stores ribbon state vectors.

```sql
CREATE TABLE IF NOT EXISTS ribbons (
    ribbon_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    -- 8-slot schema: C, L, R, B, T, O, W, A
    slot_C INTEGER DEFAULT 0 CHECK (slot_C IN (0, 1)),  -- Center / active coordinate
    slot_L INTEGER DEFAULT 0 CHECK (slot_L IN (0, 1)),  -- Left boundary
    slot_R INTEGER DEFAULT 0 CHECK (slot_R IN (0, 1)),  -- Right boundary
    slot_B INTEGER DEFAULT 0 CHECK (slot_B IN (0, 1)),  -- Boundary rule
    slot_T INTEGER DEFAULT 0 CHECK (slot_T IN (0, 1)),  -- Tool transform
    slot_O INTEGER DEFAULT 0 CHECK (slot_O IN (0, 1)),  -- Obligation set
    slot_W INTEGER DEFAULT 0 CHECK (slot_W IN (0, 1)),  -- Workbook analogue
    slot_A INTEGER DEFAULT 0 CHECK (slot_A IN (0, 1)),  -- Anchor / provenance
    arity INTEGER NOT NULL DEFAULT 0
        CHECK (arity >= 0 AND arity <= 8),  -- number of active (filled) slots
    hash TEXT NOT NULL,  -- SHA-256 of the canonical slot vector string
    status TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'frozen', 'void')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Notes:**
- Slot names are mapped to the supplement's explicit 8-slot vocabulary (`C, L, R, B, T, O, W, A`) rather than generic `slot_0..slot_7` for semantic clarity.
- `hash` is the SHA-256 of the canonical ordered vector `(slot_C, slot_L, slot_R, slot_B, slot_T, slot_O, slot_W, slot_A)`.

---

### 3.8 ledgers — Event Log

The **Layer-2 Synthesis Ledger** (Paper 20) aggregates all lower-paper events into a single auditable log. This table implements that ledger.

```sql
CREATE TABLE IF NOT EXISTS ledgers (
    ledger_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type TEXT NOT NULL
        CHECK (event_type IN (
            'claim_added', 'claim_verified', 'claim_disputed', 'claim_resolved',
            'crystal_created', 'receipt_issued', 'carrier_updated', 'ribbon_woven',
            'obligation_created', 'obligation_resolved', 'snapshot_taken', 'theorem_proven',
            'cross_ref_added', 'paper_status_changed', 'paper_merged',
            'face_enumerated', 'vignette_written', 'playbook_projected',
            'transport_checked', 'spine_routed'
        )),
    paper_number TEXT
        REFERENCES papers(paper_number) ON DELETE SET NULL,
    claim_id INTEGER
        REFERENCES claims(claim_id) ON DELETE SET NULL,
    crystal_id INTEGER
        REFERENCES crystals(crystal_id) ON DELETE SET NULL,
    receipt_id INTEGER
        REFERENCES receipts(receipt_id) ON DELETE SET NULL,
    event_data TEXT,  -- JSON blob of event details
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 3.9 obligations — Open Obligations

The supplement contains an **Open Obligations Manifest** (Summary Paper IX). This table tracks every open obligation with owner, status, and resolution timestamp.

```sql
CREATE TABLE IF NOT EXISTS obligations (
    obligation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT
        REFERENCES papers(paper_number) ON DELETE SET NULL,
    claim_id INTEGER
        REFERENCES claims(claim_id) ON DELETE SET NULL,
    description TEXT NOT NULL,
    obligation_type TEXT NOT NULL DEFAULT 'open'
        CHECK (obligation_type IN (
            'open', 'open_lift', 'open_bridge', 'open_packaging',
            'deferred_until_lab', 'deferred_until_measurement',
            'in_progress', 'blocked', 'resolved', 'cancelled'
        )),
    status TEXT NOT NULL DEFAULT 'open'
        CHECK (status IN ('open', 'in_progress', 'blocked', 'resolved', 'cancelled')),
    owner TEXT NOT NULL,  -- who owns this obligation (e.g., 'architect', 'system', verifier name)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP
);
```

**Notes:**
- `obligation_type` maps the supplement's rich taxonomy (`open_lift`, `open_bridge`, `deferred_until_lab_dataset`, etc.) to a normalized enum.

---

### 3.10 snapshots — Point-in-Time Captures

**Snapshots** are immutable point-in-time captures of paper state, used for rollback and audit.

```sql
CREATE TABLE IF NOT EXISTS snapshots (
    snapshot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    snapshot_type TEXT NOT NULL DEFAULT 'full'
        CHECK (snapshot_type IN ('full', 'claim_subset', 'carrier_state', 'ribbon_state')),
    data TEXT NOT NULL,  -- JSON snapshot of relevant state
    hash TEXT NOT NULL,  -- SHA-256 of data (registered in cam_hashes)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 3.11 theorems — Formal Theorem Registry

The supplement's **32 Theorems Registry** (Summary Paper V) and the **Complete Recursive Closure Map** are tracked here.

```sql
CREATE TABLE IF NOT EXISTS theorems (
    theorem_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    theorem_name TEXT NOT NULL,
    theorem_code TEXT,  -- e.g., "T-10.1", "O-32.1"
    statement TEXT NOT NULL,
    proof TEXT,
    status TEXT NOT NULL DEFAULT 'conjecture'
        CHECK (status IN ('conjecture', 'proven', 'disproven', 'pending_review')),
    verifier_path TEXT,  -- path to verifier script
    receipt_id INTEGER
        REFERENCES receipts(receipt_id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 3.12 cross_references — Paper-to-Paper Links

Tracks typed dependencies between papers and claims, implementing the supplement's **causal code** (Paper 06) edge discipline.

```sql
CREATE TABLE IF NOT EXISTS cross_references (
    xref_id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_paper TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    to_paper TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    claim_id INTEGER
        REFERENCES claims(claim_id) ON DELETE SET NULL,
    type TEXT NOT NULL DEFAULT 'general'
        CHECK (type IN (
            'general', 'cites', 'depends_on', 'supersedes', 'contradicts',
            'extends', 'proves', 'obligates', 'transports', 'repairs', 'verifies'
        )),
    receipt TEXT,  -- edge receipt (JSON or path)
    status TEXT NOT NULL DEFAULT 'open'
        CHECK (status IN ('open', 'closed', 'deferred', 'rejected')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (from_paper, to_paper, claim_id, type)
);
```

**Notes:**
- Edge types `obligates`, `transports`, `repairs`, `verifies` are drawn from the supplement's causal-edge taxonomy (Paper 06).
- `receipt` stores the edge-specific receipt or JSON boundary data.

---

### 3.13 faces — Enumerated Addressable Faces

Maps the supplement's **face enumeration** step: each paper, code module, receipt, ledger, or adapter exposes addressable faces that the projector shines across.

```sql
CREATE TABLE IF NOT EXISTS faces (
    face_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    face_name TEXT NOT NULL,  -- e.g., "FORMAL", "TOOL", "WORKBOOK", "SOURCE", "README"
    face_kind TEXT NOT NULL
        CHECK (face_kind IN ('paper', 'code', 'receipt', 'ledger', 'catalog', 'adapter')),
    source_path TEXT,  -- original file path (audit)
    content_hash TEXT  -- SHA-256 of face content (registered in cam_hashes)
        REFERENCES cam_hashes(cam_hash) ON DELETE SET NULL,
    status TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'projected', 'written', 'routed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 3.14 vignettes — CAM Vignettes

A **vignette** is the written output of projecting a face through the playbook. It is stored as a crystal and linked here for routing.

```sql
CREATE TABLE IF NOT EXISTS vignettes (
    vignette_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    face_id INTEGER NOT NULL
        REFERENCES faces(face_id) ON DELETE CASCADE,
    cam_hash TEXT NOT NULL
        REFERENCES cam_hashes(cam_hash) ON DELETE CASCADE,
    crystal_id INTEGER
        REFERENCES crystals(crystal_id) ON DELETE SET NULL,
    playbook_version TEXT,  -- which playbook edition produced this vignette
    route_target TEXT,      -- next algorithm routed to (e.g., "obligation_router")
    status TEXT NOT NULL DEFAULT 'draft'
        CHECK (status IN ('draft', 'projected', 'routed', 'archived')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 3.15 transport_obligations — Typed Transport Rows

Implements the supplement's **transport-obligation** rows: four typed rungs (`LCR → D4 → J3(O) → G2/F4 route → Niemeier landing forms`) with witness, classification, and explicit proof boundary.

```sql
CREATE TABLE IF NOT EXISTS transport_obligations (
    transport_id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    rung INTEGER NOT NULL
        CHECK (rung BETWEEN 1 AND 5),  -- 1:LCR, 2:D4, 3:J3(O), 4:G2/F4/T5A, 5:Niemeier
    rung_name TEXT NOT NULL
        CHECK (rung_name IN ('LCR', 'D4', 'J3O', 'G2F4T5A', 'Niemeier')),
    classification TEXT NOT NULL DEFAULT 'open'
        CHECK (classification IN (
            'demonstrated', 'bounded_local', 'bounded_external',
            'registered_landing_forms', 'open', 'forbidden', 'failed'
        )),
    witness TEXT,  -- witness function or verifier path
    boundary TEXT,  -- explicit proof boundary note
    receipt_id INTEGER
        REFERENCES receipts(receipt_id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Notes:**
- `classification` enum is taken verbatim from the supplement's transport-obligation taxonomy (e.g., Paper 10's master receipt).
- `rung` maps the supplement's code chain: `1 → 3 → 7 → 8 → 24 → 72` is abstracted to 5 transport rungs for the schema.

---

### 3.16 spine_routing — Spine Routing Registry

Implements the supplement's **Spine Routing** table, mapping topics to spine-owner papers and supplement roles.

```sql
CREATE TABLE IF NOT EXISTS spine_routing (
    route_id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT NOT NULL,  -- e.g., "Typed causal edges and obligations"
    spine_owner TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    supplement_role TEXT NOT NULL,  -- e.g., "CAM writeback and receipt discipline"
    status TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'routed', 'closed', 'superseded')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 3.17 archive_intake — Archive/Mirror Intake Log

Captures the supplement's **Archive/Mirror Supplement Intake** cards. Each row is a source card that preserves routing, contribution, and claim-boundary use.

```sql
CREATE TABLE IF NOT EXISTS archive_intake (
    intake_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_label TEXT NOT NULL,  -- e.g., "CQE-paper-13.50" (B-family, preserved for audit)
    a_family_paper TEXT NOT NULL
        REFERENCES papers(paper_number) ON DELETE CASCADE,
    source_path TEXT NOT NULL,
    archive_score INTEGER CHECK (archive_score BETWEEN 0 AND 101),
    contributes TEXT NOT NULL,  -- "what it contributes" text
    routed_spine_papers TEXT,  -- JSON array of paper numbers ["paper-06", "paper-10"]
    integration_action TEXT NOT NULL DEFAULT 'keep'
        CHECK (integration_action IN (
            'keep', 'upgrade_claim', 'close_obligation', 'merge', 'reject'
        )),
    cam_hash TEXT  -- SHA-256 of the source card content (audit)
        REFERENCES cam_hashes(cam_hash) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Notes:**
- `source_label` preserves the original B-family label for audit but does not participate in foreign keys.
- `a_family_paper` is the normalized A-family reference.
- `routed_spine_papers` is a JSON array to avoid many-to-many complexity for intake logs.

---

## 4. Indexes

```sql
-- Papers
CREATE INDEX IF NOT EXISTS idx_papers_status ON papers(status);
CREATE INDEX IF NOT EXISTS idx_papers_spine ON papers(spine_owner);

-- Claims
CREATE INDEX IF NOT EXISTS idx_claims_paper ON claims(paper_number);
CREATE INDEX IF NOT EXISTS idx_claims_status ON claims(claim_status);
CREATE INDEX IF NOT EXISTS idx_claims_number ON claims(claim_number);

-- CAM hashes
CREATE INDEX IF NOT EXISTS idx_cam_hashes_type ON cam_hashes(content_type);

-- Crystals
CREATE INDEX IF NOT EXISTS idx_crystals_paper ON crystals(paper_number);
CREATE INDEX IF NOT EXISTS idx_crystals_claim ON crystals(claim_id);
CREATE INDEX IF NOT EXISTS idx_crystals_face ON crystals(face_id);
CREATE INDEX IF NOT EXISTS idx_crystals_vignette ON crystals(vignette_id);

-- Receipts
CREATE INDEX IF NOT EXISTS idx_receipts_status ON receipts(status);
CREATE INDEX IF NOT EXISTS idx_receipts_claim ON receipts(claim_id);
CREATE INDEX IF NOT EXISTS idx_receipts_checked ON receipts(checked_at);

-- Carriers
CREATE INDEX IF NOT EXISTS idx_carriers_paper ON carriers(paper_number);
CREATE INDEX IF NOT EXISTS idx_carriers_state ON carriers(state_code);
CREATE INDEX IF NOT EXISTS idx_carriers_shell ON carriers(shell);
CREATE INDEX IF NOT EXISTS idx_carriers_rest ON carriers(rest_state);

-- Ribbons
CREATE INDEX IF NOT EXISTS idx_ribbons_paper ON ribbons(paper_number);
CREATE INDEX IF NOT EXISTS idx_ribbons_hash ON ribbons(hash);

-- Ledgers
CREATE INDEX IF NOT EXISTS idx_ledgers_paper ON ledgers(paper_number);
CREATE INDEX IF NOT EXISTS idx_ledgers_event ON ledgers(event_type);
CREATE INDEX IF NOT EXISTS idx_ledgers_claim ON ledgers(claim_id);
CREATE INDEX IF NOT EXISTS idx_ledgers_receipt ON ledgers(receipt_id);

-- Obligations
CREATE INDEX IF NOT EXISTS idx_obligations_status ON obligations(status);
CREATE INDEX IF NOT EXISTS idx_obligations_owner ON obligations(owner);
CREATE INDEX IF NOT EXISTS idx_obligations_type ON obligations(obligation_type);

-- Snapshots
CREATE INDEX IF NOT EXISTS idx_snapshots_paper ON snapshots(paper_number);
CREATE INDEX IF NOT EXISTS idx_snapshots_hash ON snapshots(hash);

-- Theorems
CREATE INDEX IF NOT EXISTS idx_theorems_paper ON theorems(paper_number);
CREATE INDEX IF NOT EXISTS idx_theorems_code ON theorems(theorem_code);

-- Cross-references
CREATE INDEX IF NOT EXISTS idx_xrefs_from ON cross_references(from_paper);
CREATE INDEX IF NOT EXISTS idx_xrefs_to ON cross_references(to_paper);
CREATE INDEX IF NOT EXISTS idx_xrefs_type ON cross_references(type);

-- Faces
CREATE INDEX IF NOT EXISTS idx_faces_paper ON faces(paper_number);
CREATE INDEX IF NOT EXISTS idx_faces_kind ON faces(face_kind);

-- Vignettes
CREATE INDEX IF NOT EXISTS idx_vignettes_paper ON vignettes(paper_number);
CREATE INDEX IF NOT EXISTS idx_vignettes_face ON vignettes(face_id);

-- Transport obligations
CREATE INDEX IF NOT EXISTS idx_transport_paper ON transport_obligations(paper_number);
CREATE INDEX IF NOT EXISTS idx_transport_rung ON transport_obligations(rung);
CREATE INDEX IF NOT EXISTS idx_transport_class ON transport_obligations(classification);

-- Archive intake
CREATE INDEX IF NOT EXISTS idx_intake_paper ON archive_intake(a_family_paper);
CREATE INDEX IF NOT EXISTS idx_intake_score ON archive_intake(archive_score);
```

---

## 5. Data Integrity & Application Rules

1. **A-family exclusivity:** Any insert into `papers.paper_number` must match `paper-[0-9][0-9]*`. B-family labels (`CQE-paper-NN`, `Paper_NN`, etc.) must be stored only in `archive_intake.source_label` or `archive_intake.source_path`.

2. **CAM hash registration:** Before inserting a `cam_hash` into `crystals`, `claims`, `receipts`, `snapshots`, `faces`, or `vignettes`, the application must first insert it into `cam_hashes` to ensure the registry is complete.

3. **D/I/X enforcement:** `claims.claim_status` must be one of `D`, `I`, or `X`. The application layer should enforce that:
   - `D` claims require a `verifier` and a `receipt_path`.
   - `I` claims require a `boundary` note.
   - `X` claims require a `falsifier` and must be linked to an `obligations` row explaining the rejection.

4. **Receipt taxonomy:** `receipts.status` must use the extended enum. The application must not invent new statuses; new supplement statuses must be added to the enum via schema migration.

5. **Spine owner constraint:** Only papers 06, 10, 12, 20, 30, 32 may have `spine_owner = 1` (enforced by application, not SQLite CHECK, to allow future spine extensions).

6. **Cross-reference acyclicity:** The `cross_references` table must remain acyclic for `type IN ('depends_on', 'proves', 'transports')`. The application layer must verify this before insert.

7. **Transport obligation rung order:** For a given `paper_number`, `transport_obligations.rung` values must be populated in order (1 before 2, etc.). Gaps are allowed only if the rung is classified as `open` or `forbidden`.

8. **Shell bound:** `carriers.shell` is bounded to 24. Papers above shell 9 (the supplement's `K_max`) must be flagged in `obligations` as requiring external calibration.

---

## 6. Compatibility Matrix

| CrystalLib Table | PaperLib | CAMLib | CodeLib | SQLLib |
|---|---|---|---|---|
| `papers` | `paper_number` PK | — | — | — |
| `claims` | `paper_number` FK | `cam_hash` | `code_source` | `sql_source` |
| `cam_hashes` | — | `cam_hash` PK | — | — |
| `crystals` | `paper_number` FK | `cam_hash` FK | — | — |
| `receipts` | — | `cam_hash` FK | — | — |
| `carriers` | `paper_number` FK | — | — | — |
| `ribbons` | `paper_number` FK | — | — | — |
| `ledgers` | `paper_number` FK | — | — | — |
| `obligations` | `paper_number` FK | — | — | — |
| `snapshots` | `paper_number` FK | `hash` | — | — |
| `theorems` | `paper_number` FK | — | — | — |
| `cross_references` | `from_paper`, `to_paper` | — | — | — |
| `faces` | `paper_number` FK | `content_hash` | — | — |
| `vignettes` | `paper_number` FK | `cam_hash` | — | — |
| `transport_obligations` | `paper_number` FK | — | — | — |
| `spine_routing` | `spine_owner` FK | — | — | — |
| `archive_intake` | `a_family_paper` FK | `cam_hash` | — | — |

All `paper_number` columns use the identical `TEXT` format (`paper-NN`) and foreign-key constraints to `papers(paper_number)`, ensuring referential compatibility across the A-family ecosystem.

---

## 7. Schema Migration Notes

This schema is a ** superset** of the existing `crystal_lib_schema.sql` (v1.0) found in `D:\Paper Ecology\CrystalLib`. The changes are:

- **Added `cam_hashes` table:** Centralized registry for all SHA-256 content addresses.
- **Added `archive_score`, `source_path`, `spine_owner` to `papers`:** To ingest supplement metadata.
- **Added `claim_number`, `receipt_path`, `falsifier`, `boundary` to `claims`:** To support claim-contract discipline.
- **Added `anneal_steps`, `rest_state` to `carriers`:** To capture the supplement's S3 closure and attractor semantics.
- **Renamed `slot_0..slot_7` to `slot_C..slot_A` in `ribbons`:** To match the supplement's explicit Grand Ribbon 8-slot vocabulary.
- **Added `crystal_id`, `receipt_id` to `ledgers`:** For richer event tracing.
- **Added `claim_id`, `obligation_type` to `obligations`:** To link obligations to claims and preserve the supplement's taxonomy.
- **Added `snapshot_type` to `snapshots`:** To distinguish full vs. subset captures.
- **Added `theorem_code`, `verifier_path`, `receipt_id` to `theorems`:** To map the 32 Theorems Registry.
- **Added `receipt`, `status` to `cross_references`:** To support causal-edge receipts (Paper 06).
- **Added `faces`, `vignettes`, `transport_obligations`, `spine_routing`, `archive_intake`:** To implement the supplement's operating model (face enumeration, vignette writeback, transport rows, spine routing, intake log).
- **Extended `receipts.status` enum:** To include the supplement's rich receipt taxonomy (`pass_with_open_obligations`, etc.).

---

*End of CrystalLib Database Specification*
