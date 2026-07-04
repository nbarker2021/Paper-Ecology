import sqlite3
import hashlib
import json
from datetime import datetime
import os

DB_PATH = r"D:\Paper Ecology\SystemsLib\systems_lib.db"
SCHEMA_PATH = r"D:\Paper Ecology\SystemsLib\systems_lib_schema.sql"

def sha256_content(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def now() -> str:
    return datetime.utcnow().isoformat() + "Z"

def build_database():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # ============================================================
    # 1. systems
    # ============================================================
    c.execute("""
    CREATE TABLE IF NOT EXISTS systems (
        system_id INTEGER PRIMARY KEY AUTOINCREMENT,
        system_name TEXT NOT NULL UNIQUE,
        description TEXT,
        paper_number TEXT,
        status TEXT,
        dependencies TEXT,
        storage_needs TEXT,
        created_at TEXT,
        cam_hash TEXT
    )
    """)

    # ============================================================
    # 2. obligations
    # ============================================================
    c.execute("""
    CREATE TABLE IF NOT EXISTS obligations (
        obligation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        paper_number TEXT,
        description TEXT,
        status TEXT,
        owner TEXT,
        source_path TEXT,
        created_at TEXT,
        resolved_at TEXT,
        cam_hash TEXT,
        honesty_flag TEXT
    )
    """)

    # ============================================================
    # 3. agents
    # ============================================================
    c.execute("""
    CREATE TABLE IF NOT EXISTS agents (
        agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_name TEXT NOT NULL UNIQUE,
        description TEXT,
        system_id INTEGER,
        routing_rules TEXT,
        status TEXT,
        created_at TEXT,
        cam_hash TEXT,
        FOREIGN KEY (system_id) REFERENCES systems(system_id)
    )
    """)

    # ============================================================
    # 4. docker_services
    # ============================================================
    c.execute("""
    CREATE TABLE IF NOT EXISTS docker_services (
        service_id INTEGER PRIMARY KEY AUTOINCREMENT,
        service_name TEXT NOT NULL,
        compose_file TEXT,
        description TEXT,
        paper_number TEXT,
        status TEXT,
        ports TEXT,
        created_at TEXT,
        cam_hash TEXT
    )
    """)

    # ============================================================
    # 5. external_sources
    # ============================================================
    c.execute("""
    CREATE TABLE IF NOT EXISTS external_sources (
        source_id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_name TEXT NOT NULL,
        description TEXT,
        data_type TEXT,
        paper_number TEXT,
        lane_type TEXT,
        status TEXT,
        url TEXT,
        created_at TEXT,
        cam_hash TEXT
    )
    """)

    # ============================================================
    # 6. paper_sources
    # ============================================================
    c.execute("""
    CREATE TABLE IF NOT EXISTS paper_sources (
        mapping_id INTEGER PRIMARY KEY AUTOINCREMENT,
        paper_number TEXT,
        source_path TEXT,
        file_count INTEGER,
        size_bytes INTEGER,
        collection_name TEXT,
        status TEXT,
        created_at TEXT,
        cam_hash TEXT
    )
    """)

    # ============================================================
    # 7. routing_rules
    # ============================================================
    c.execute("""
    CREATE TABLE IF NOT EXISTS routing_rules (
        rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_paper TEXT,
        to_paper TEXT,
        rule_type TEXT,
        agent_id INTEGER,
        description TEXT,
        status TEXT,
        created_at TEXT,
        cam_hash TEXT,
        FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
    )
    """)

    # ============================================================
    # 8. storage_needs
    # ============================================================
    c.execute("""
    CREATE TABLE IF NOT EXISTS storage_needs (
        need_id INTEGER PRIMARY KEY AUTOINCREMENT,
        system_id INTEGER,
        storage_type TEXT,
        capacity TEXT,
        usage TEXT,
        paper_number TEXT,
        status TEXT,
        created_at TEXT,
        cam_hash TEXT,
        FOREIGN KEY (system_id) REFERENCES systems(system_id)
    )
    """)

    # ============================================================
    # Populate systems
    # ============================================================
    systems_data = [
        ("LCR Kernel", "LCR kernel substrate: 8-state carrier, shell grading, reversal involution. stdlib with zero dependencies.", "paper-00", "active", "none", "kernel-level minimal", now()),
        ("PartsFactory", "Service details, MCP routes, hard constraints, ring/runbook. Forge runtime wrapper.", "paper-10-paper-30", "active", "LCR Kernel", "medium", now()),
        ("1T-Production", "Product placement rules, forge routing, fourpack product surfaces.", "paper-40-paper-60", "active", "PartsFactory", "medium", now()),
        ("GaussHaus", "Gaussian / Hausdorff product surface lane.", "paper-45", "active", "1T-Production", "small", now()),
        ("Standards", "Validator/grading surface, D-verification lab, proof lab.", "paper-70", "active", "LCR Kernel", "small", now()),
        ("Workbench", "Paper pipeline tooling, registry, dev loops. SQLite/fs preferred.", "paper-90", "active", "Standards", "small", now()),
        ("Showroom", "Master showroom navigation, reference surface, capstone index.", "paper-100", "reference", "Workbench", "minimal", now()),
        ("CAM Crystal", "Content Addressed Memory projector and MannyAI runtime.", "paper-26", "active", "PartsFactory", "large", now()),
        ("Proof Lab", "D-verification lab, receipt service, claim verification.", "paper-70", "active", "Standards", "medium", now()),
        ("Receipt Service", "Claim receipt service for verifier outputs.", "paper-20", "active", "Proof Lab", "small", now()),
    ]
    c.executemany("""
        INSERT INTO systems (system_name, description, paper_number, status, dependencies, storage_needs, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, systems_data)

    # Add CAM hashes to systems
    c.execute("SELECT system_id, system_name, description, paper_number, status, dependencies, storage_needs, created_at FROM systems")
    for row in c.fetchall():
        content = json.dumps(row[1:], sort_keys=True)
        cam = sha256_content(content)
        c.execute("UPDATE systems SET cam_hash = ? WHERE system_id = ?", (cam, row[0]))

    # ============================================================
    # Populate obligations
    # ============================================================
    obligations_data = [
        # Explicit obligations from OBLIGATIONS_CATALOG.md
        ("unassigned", "O1.weyl_lookup_table — Weyl E8 subtable (1M of 696M records). Oracle Chart formal verification.", "partial", "system", r"D:\CQE_CMPLX\.cqe\irl\o1-weyl-e8-subtable\weyl_e8_subtable.manifest.json", now(), None, "PARTIAL"),
        # Implicit obligations (mapped to A-family)
        ("paper-21", "MorphForge / PolyForge / MorphoniX (T_MORPHIC) — open obligations from verify_morphforge_ribbon.py", "open", "paper-21", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-21\verify_morphforge_ribbon.py", now(), None, "OPEN"),
        ("paper-22", "Astro-MetaForge (T_ASTRO) — validation obligations from verify_astro_metaforge_package.py", "validation", "paper-22", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-22\verify_astro_metaforge_package.py", now(), None, "VALIDATION"),
        ("paper-22", "Astro-MetaForge materials submodule — open obligations from verify_metaforge_materials.py", "open", "paper-22", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-22\verify_metaforge_materials.py", now(), None, "OPEN"),
        ("paper-23", "FoldForge (T_FOLD) — open obligations from verify_foldforge_descriptor.py", "open", "paper-23", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-23\verify_foldforge_descriptor.py", now(), None, "OPEN"),
        ("paper-24", "KnightForge CA / Spinor Walk (T_KNIGHT) — open obligations from verify_knightforge_ca.py", "open", "paper-24", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-24\verify_knightforge_ca.py", now(), None, "OPEN"),
        ("paper-25", "Energetic Traversal (T_ENERGY) — open obligations from verify_energetic_traversal.py", "open", "paper-25", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-25\verify_energetic_traversal.py", now(), None, "OPEN"),
        ("paper-26", "Z-Pinch Shear Horizon (T_ZPINCH) — open obligations from verify_zpinch_shear_horizon.py", "open", "paper-26", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-26\verify_zpinch_shear_horizon.py", now(), None, "OPEN"),
        ("paper-27", "Observer Delay / Shared Reality (T_DELAY) — interpretive obligations from verify_observer_delay_shared_reality.py", "interpretive", "paper-27", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-27\verify_observer_delay_shared_reality.py", now(), None, "INTERPRETIVE"),
        ("paper-28", "Conway Glider / Oloid Emitter (T_GLIDER) — open obligations from verify_nd_game_lattices.py", "open", "paper-28", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-28\verify_nd_game_lattices.py", now(), None, "OPEN"),
        ("paper-29", "LMFDB Moonshine Anchor (T_LMFDB) — quarantined hypotheses from verify_monster_energy_bound_hypotheses.py", "quarantined", "paper-29", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-29\verify_monster_energy_bound_hypotheses.py", now(), None, "QUARANTINED"),
        ("paper-30", "Grand Ribbon Meta-Framer (T_GRAND_RIBBON) — packaging obligations from verify_grand_ribbon_meta_framer.py", "packaging", "paper-30", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-30\verify_grand_ribbon_meta_framer.py", now(), None, "PACKAGING"),
        ("paper-32", "Supervisor Cursor (T_SUPERVISOR / T_OBSERVATION) — minimality obligations from verify_supervisor_cursor_schedule.py", "minimality", "paper-32", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-32\verify_supervisor_cursor_schedule.py", now(), None, "MINIMALITY"),
        # Unassigned formal S-paper obligations
        ("unassigned", "CQE-paper-formal-S10 — verify_3_conjugate_moonshine.py open obligations", "open", "unassigned", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-formal-S10\verify_3_conjugate_moonshine.py", now(), None, "OPEN"),
        ("unassigned", "CQE-paper-formal-S12 — verify_barker_market_engine_s12.py open obligations", "open", "unassigned", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-formal-S12\verify_barker_market_engine_s12.py", now(), None, "OPEN"),
        ("unassigned", "CQE-paper-formal-S16 — verify_algebraic_closure_s16.py open obligations", "open", "unassigned", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-formal-S16\verify_algebraic_closure_s16.py", now(), None, "OPEN"),
        ("unassigned", "CQE-paper-formal-S24 — verify_timecube_modal_s24.py open obligations", "open", "unassigned", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-formal-S24\verify_timecube_modal_s24.py", now(), None, "OPEN"),
        ("unassigned", "CQE-paper-formal-S25 — verify_hard_riemann_cross_walk_s25.py open obligations", "open", "unassigned", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-formal-S25\verify_hard_riemann_cross_walk_s25.py", now(), None, "OPEN"),
        ("unassigned", "CQE-paper-formal-S26 — verify_barker_v3_s26.py open obligations", "open", "unassigned", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-formal-S26\verify_barker_v3_s26.py", now(), None, "OPEN"),
        ("unassigned", "CQE-paper-formal-S28 — verify_multi_window_s28.py open obligations", "open", "unassigned", r"D:\CQE_CMPLX\.cqe\receipts\CQE-paper-formal-S28\verify_multi_window_s28.py", now(), None, "OPEN"),
    ]
    c.executemany("""
        INSERT INTO obligations (paper_number, description, status, owner, source_path, created_at, resolved_at, honesty_flag)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, obligations_data)

    c.execute("SELECT obligation_id, paper_number, description, status, owner, source_path, created_at, resolved_at, honesty_flag FROM obligations")
    for row in c.fetchall():
        content = json.dumps(row[1:], sort_keys=True)
        cam = sha256_content(content)
        c.execute("UPDATE obligations SET cam_hash = ? WHERE obligation_id = ?", (cam, row[0]))

    # ============================================================
    # Populate agents
    # ============================================================
    # Map system_id values
    c.execute("SELECT system_id, system_name FROM systems")
    system_map = {name: sid for sid, name in c.fetchall()}

    agents_data = [
        ("LCR Kernel Agent", "Kernel CLI agent: observe, run, replay, verify, workbook, firmware, packet, witness, d4.", system_map.get("LCR Kernel"), json.dumps({"cli_subcommands": ["observe","run","replay","verify","workbook","firmware","packet","witness","d4"], "preferred_routes": ["/api/global","/call-plan"]}, sort_keys=True), "active", now()),
        ("PartsFactory Agent", "MCP route agent for service details, hard constraints, ring/runbook.", system_map.get("PartsFactory"), json.dumps({"cli_subcommands": [], "preferred_routes": ["direct_upstream"], "surface": "service_details"}, sort_keys=True), "active", now()),
        ("1T Production Agent", "Forge routing and product placement agent.", system_map.get("1T-Production"), json.dumps({"surface": "product_placement", "target": "src/products/"}, sort_keys=True), "active", now()),
        ("GaussHaus Agent", "Gaussian/Hausdorff lane product agent.", system_map.get("GaussHaus"), json.dumps({"surface": "gauss_hausdorff"}, sort_keys=True), "active", now()),
        ("Standards Agent", "Validator/grading surface agent. D-verification lab.", system_map.get("Standards"), json.dumps({"surface": "verification", "trigger": "make boot validate paper00"}, sort_keys=True), "active", now()),
        ("Workbench Agent", "Paper pipeline tooling and dev-loop agent.", system_map.get("Workbench"), json.dumps({"surface": "tooling", "storage": "sqlite_fs"}, sort_keys=True), "active", now()),
        ("Showroom Agent", "Master showroom navigation agent. Capstone reference.", system_map.get("Showroom"), json.dumps({"surface": "showroom", "edit_policy": "read_only"}, sort_keys=True), "reference", now()),
        ("CAM Crystal Agent", "MannyAI runtime and crystal projector agent.", system_map.get("CAM Crystal"), json.dumps({"surface": "cam_projection", "runtime": "mannyai"}, sort_keys=True), "active", now()),
        ("Proof Lab Agent", "D-verification and receipt generation agent.", system_map.get("Proof Lab"), json.dumps({"surface": "proof_verification", "ports": [8871,8872]}, sort_keys=True), "active", now()),
        ("Receipt Service Agent", "Claim receipt service agent.", system_map.get("Receipt Service"), json.dumps({"surface": "receipt_service", "port": 8010}, sort_keys=True), "active", now()),
    ]
    c.executemany("""
        INSERT INTO agents (agent_name, description, system_id, routing_rules, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, agents_data)

    c.execute("SELECT agent_id, agent_name, description, system_id, routing_rules, status, created_at FROM agents")
    for row in c.fetchall():
        content = json.dumps(row[1:], sort_keys=True)
        cam = sha256_content(content)
        c.execute("UPDATE agents SET cam_hash = ? WHERE agent_id = ?", (cam, row[0]))

    # ============================================================
    # Populate docker_services
    # ============================================================
    docker_data = [
        # PartsFactory (paper-10–paper-30)
        ("receipt-service", "docker-compose.receipt.yml", "Claim receipt service", "paper-20", "active", "8010", now()),
        ("speedlight", "docker-compose.speedlight.yml", "SpeedLight service", "paper-25", "active", "8843", now()),
        ("tarpit", "docker-compose.tarpit.yml", "TarPit service", "paper-25", "active", "8844", now()),
        ("snap", "docker-compose.snap.yml", "SNAP service", "paper-25", "active", "8823", now()),
        ("lattice-forge", "docker-compose.lattice-forge.yml", "Lattice Forge witness substrate", "paper-10-paper-30", "active", "8845", now()),
        ("proof-lab", "docker-compose.proof-lab.yml", "D-verification lab", "paper-70", "active", "8871-8872", now()),
        ("repo-kernel", "docker-compose.repo-kernel.yml", "LCR kernel control plane", "paper-00", "active", "8786", now()),
        ("web", "docker-compose.web.yml", "Web surface", "paper-10-paper-30", "active", "", now()),
        ("server", "docker-compose.server.yml", "Server runtime", "paper-10-paper-30", "active", "", now()),
        ("cmplx-discord", "docker-compose.cmplx-discord.yml", "Discord integration", "paper-10-paper-30", "active", "", now()),
        ("cmplxmcp-runtime", "docker-compose.cmplxmcp-runtime.yml", "MCP runtime", "paper-10-paper-30", "active", "", now()),
        ("backwalk-builder", "docker-compose.backwalk-builder.yml", "Backwalk builder", "paper-10-paper-30", "active", "", now()),
        ("backwalk-lattice-space", "docker-compose.backwalk-lattice-space.yml", "Backwalk lattice space", "paper-10-paper-30", "active", "", now()),
        ("backwalk-weyl-bond", "docker-compose.backwalk-weyl-bond.yml", "Backwalk Weyl bond", "paper-10-paper-30", "active", "", now()),
        ("gitnexus-three-space", "docker-compose.gitnexus-three-space.yml", "GitNexus three-space", "paper-10-paper-30", "active", "", now()),
        ("morphon-graph", "docker-compose.morphon-graph.yml", "Morphon graph", "paper-10-paper-30", "active", "", now()),
        ("dind", "docker-compose.dind.yml", "Docker-in-Docker bootstrap", "paper-10-paper-30", "active", "", now()),
        ("partsfactory-umbrella", "docker-compose.yml", "Top-level umbrella orchestration", "paper-10-paper-30", "active", "", now()),
        # 1T-Production (paper-40–paper-60)
        ("1t-production-umbrella", "docker-compose.yml", "1T-Production umbrella", "paper-40-paper-60", "active", "", now()),
        ("fourpack-v1", "docker-compose.fourpack.yml", "Fourpack product v1", "paper-40-paper-60", "active", "", now()),
        ("fourpack-v2", "docker-compose.fourpack.v2.yml", "Fourpack product v2", "paper-40-paper-60", "active", "", now()),
        ("fourpack-unified", "docker-compose.unified.yml", "Fourpack unified", "paper-40-paper-60", "active", "", now()),
        ("gausshaus", "docker-compose.yml", "GaussHaus product surface", "paper-45", "active", "", now()),
        # Kernel & Proof Validated Suite (paper-00, paper-70)
        ("kernel-dind", "kernel/deploy/docker/docker-compose.kernel-dind.yml", "Kernel DIND bootstrap", "paper-00", "active", "", now()),
        ("kernel-socket", "kernel/deploy/docker/docker-compose.kernel-socket.yml", "Kernel socket bootstrap", "paper-00", "active", "", now()),
        ("kernel-validated", "kernel/docker-compose-kernel-validated.yml", "Kernel validated suite", "paper-00", "active", "", now()),
        ("kernel-opencode", "kernel/docker-compose-kernel-with-opencode.yml", "Kernel + opencode", "paper-00", "active", "", now()),
        ("meta-material-system", "kernel/lib-forge/meta_material_system/docker-compose.yml", "Meta-material system", "paper-20-paper-30", "active", "", now()),
        ("odysseus-base", "kernel/lib-forge/odysseus/docker-compose.yml", "Odysseus base", "paper-20-paper-30", "active", "", now()),
        ("odysseus-amd", "kernel/lib-forge/odysseus/docker-compose.gpu-amd.yml", "Odysseus AMD GPU", "paper-20-paper-30", "active", "", now()),
        ("odysseus-nvidia", "kernel/lib-forge/odysseus/docker-compose.gpu-nvidia.yml", "Odysseus NVIDIA GPU", "paper-20-paper-30", "active", "", now()),
        ("meta-material-modules", "kernel/modules/meta_material_system/docker-compose.yml", "Meta-material system (modules)", "paper-20-paper-30", "active", "", now()),
        # Production Mirror
        ("meta-material-mirror", "lib-forge/meta_material_system/docker-compose.yml", "Meta-material system mirror", "paper-20-paper-30", "mirror", "", now()),
        ("odysseus-base-mirror", "lib-forge/odysseus/docker-compose.yml", "Odysseus base mirror", "paper-20-paper-30", "mirror", "", now()),
        ("odysseus-amd-mirror", "lib-forge/odysseus/docker-compose.gpu-amd.yml", "Odysseus AMD GPU mirror", "paper-20-paper-30", "mirror", "", now()),
        ("odysseus-nvidia-mirror", "lib-forge/odysseus/docker-compose.gpu-nvidia.yml", "Odysseus NVIDIA GPU mirror", "paper-20-paper-30", "mirror", "", now()),
        # Unassigned Container Experiments
        ("container-advanced", "docker-compose-advanced.yml", "Unassigned container experiment", "unassigned", "experimental", "", now()),
        ("container-complete-stack", "docker-compose-complete-stack.yml", "Unassigned container experiment", "unassigned", "experimental", "", now()),
        ("container-hardened", "docker-compose-hardened.yml", "Unassigned container experiment", "unassigned", "experimental", "", now()),
        ("container-minimal", "docker-compose-minimal.yml", "Unassigned container experiment", "unassigned", "experimental", "", now()),
        ("container-with-databases", "docker-compose-with-databases.yml", "Unassigned container experiment", "unassigned", "experimental", "", now()),
        ("container-working", "docker-compose-working.yml", "Unassigned container experiment", "unassigned", "experimental", "", now()),
    ]
    c.executemany("""
        INSERT INTO docker_services (service_name, compose_file, description, paper_number, status, ports, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, docker_data)

    c.execute("SELECT service_id, service_name, compose_file, description, paper_number, status, ports, created_at FROM docker_services")
    for row in c.fetchall():
        content = json.dumps(row[1:], sort_keys=True)
        cam = sha256_content(content)
        c.execute("UPDATE docker_services SET cam_hash = ? WHERE service_id = ?", (cam, row[0]))

    # ============================================================
    # Populate external_sources
    # ============================================================
    external_data = [
        ("SRC-PDG-2026", "Particle Data Group Review of Particle Physics 2026 — Particle properties, SM reviews, summary tables, gauge boson/Higgs/lepton/quark data", "physics_review", "paper-01", "D", "active", "https://pdg.lbl.gov/2026/", now()),
        ("SRC-PDG-2024", "Review of Particle Physics 2024/2025, Phys. Rev. D 110, 030001 — Stable citable PDG review for particle data and evaluated measurements", "physics_review", "paper-01", "D", "active", "https://pdg.lbl.gov/2024/", now()),
        ("SRC-CODATA-2022", "CODATA Recommended Values of the Fundamental Physical Constants: 2022 — Units-bearing constants and exact SI constants for calibration rows", "constants_table", "paper-00", "I", "active", "https://physics.nist.gov/cuu/Constants/", now()),
        ("SRC-ATLAS-HIGGS-2012", "ATLAS observation of a new particle in the search for the Standard Model Higgs boson — Higgs discovery evidence and mass-scale calibration surface", "experiment_paper", "paper-02", "I", "active", "https://arxiv.org/abs/1207.7214", now()),
        ("SRC-CMS-HIGGS-2012", "CMS observation of a new boson at a mass of 125 GeV — Independent Higgs discovery evidence and mass-scale calibration surface", "experiment_paper", "paper-02", "I", "active", "https://arxiv.org/abs/1207.7235", now()),
        ("SRC-NOBEL-NEUTRINO-2015", "Nobel advanced information: Neutrino Oscillations — Neutrino oscillation evidence and beyond-minimal Standard Model boundary", "prize_document", "paper-03", "D", "active", "https://www.nobelprize.org/prizes/physics/2015/advanced-information/", now()),
        ("SRC-PHYS-CONSTANTS", "Fundamental Physical Constants extensive listing — Numerical constants, units, and uncertainty metadata for calibration tables", "constants_table", "paper-00", "I", "active", "", now()),
        ("SRC-EXCITON-SPRINGER", "Excitons reference entry, Springer Nature — Electron-hole, exciton, Wannier-Mott/Frenkel, binding-energy and dielectric/effective-mass formalism", "reference_entry", "paper-20-paper-30", "D", "active", "https://link.springer.com/referenceworkentry/10.1007/978-3-642-35943-9_2-1", now()),
        ("SRC-EXCITON-2D", "Excitons in two-dimensional materials, arXiv:1911.00087 — Modern exciton review and material-dependent exciton evidence boundary", "arxiv_paper", "paper-20-paper-30", "D", "active", "https://arxiv.org/abs/1911.00087", now()),
        ("SRC-ALPHA-2022", "CODATA inverse fine-structure constant — Numerical alpha inverse calibration value: 137.035999177 with standard uncertainty 0.000000021", "constant_value", "paper-00", "I", "active", "", now()),
        ("SRC-CODATA-WALLET-2022", "CODATA 2022 wallet card — Compact units and constants reference for calibration tables", "constants_table", "paper-00", "I", "active", "", now()),
        ("SRC-CARRIER-DYNAMICS", "Carrier dynamics by ultrafast time-resolved terahertz spectroscopy — Exciton/electron-hole separation, recombination, free carrier dynamics, and optoelectronic metrology lane", "research_paper", "paper-20-paper-30", "I", "active", "", now()),
        ("SRC-PV-EXCITON", "Optoelectrical characterization of photovoltaic materials and devices — Materials lane for exciton separation into free electrons and holes at heterojunction interfaces", "research_paper", "paper-20-paper-30", "I", "active", "", now()),
        ("SRC-GR-HYPERBOLIC", "Living Reviews in Relativity: Hyperbolic Methods for Einstein's Equations — GR/continuum formalism boundary for Einstein equations as PDE/hyperbolic systems after gauge and constraint handling", "review_article", "paper-50", "D", "active", "https://link.springer.com/article/10.12942/lrr-2010-1", now()),
        ("SRC-PLASMA-MAGNETIC", "PPPL fusion/plasma magnetic confinement testimony — Plasma boundary row for charged-particle motion and magnetic confinement", "testimony", "paper-60", "D", "active", "", now()),
        ("SRC-PLASMA-DIAGNOSTICS-2026", "PPPL Plasma Diagnostics lecture notes — Plasma definition/calibration row: plasma consists of particles and fields; diagnostics are required for measured claims", "lecture_notes", "paper-60", "I", "active", "", now()),
    ]
    c.executemany("""
        INSERT INTO external_sources (source_name, description, data_type, paper_number, lane_type, status, url, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, external_data)

    c.execute("SELECT source_id, source_name, description, data_type, paper_number, lane_type, status, url, created_at FROM external_sources")
    for row in c.fetchall():
        content = json.dumps(row[1:], sort_keys=True)
        cam = sha256_content(content)
        c.execute("UPDATE external_sources SET cam_hash = ? WHERE source_id = ?", (cam, row[0]))

    # ============================================================
    # Populate paper_sources
    # ============================================================
    # From MASTER_INDEX_CATALOG.md collection inventory
    paper_sources_data = [
        ("paper-00-paper-103", "D:\\CQE_CMPLX\\papers\\UFT0-100", 108, 11312722, "UFT 100-Paper Series", "canonical", now()),
        ("paper-00-paper-32", "D:\\CQE_CMPLX\\CQECMPLX-Production\\papers", 165, 17301536, "CQE-Production", "duplicate_variant", now()),
        ("paper-02-paper-04", "D:\\CQE_CMPLX\\CQECMPLX-Production\\REAL-PAPERS", 14, 1468006, "REAL-PAPERS", "duplicate_variant", now()),
        ("paper-02-paper-31", "D:\\CQE_CMPLX\\CQECMPLX-ProofValidatedSuite\\EXPOSE-PAPERS", 40, 4194304, "EXPOSE-Papers", "duplicate_variant", now()),
        ("paper-00-paper-32", "D:\\CQE_CMPLX\\kernel\\staging\\papers", 2460, 51589939, "Kernel Staging", "duplicate_variant", now()),
        ("paper-00-paper-80", "D:\\CQE_CMPLX\\flcr_peer_review_work\\publication_series", 679, 14260633, "FLCR Peer Review", "duplicate_variant", now()),
        ("paper-00-paper-32", "D:\\CQE_CMPLX\\CQE-CMPLX-1T-Production\\src\\papers", 741, 15518924, "1T Production", "duplicate_variant", now()),
        ("paper-00-paper-32", "D:\\repo_harvest", 1019, 21390950, "Repo Harvest", "duplicate", now()),
        ("paper-00-paper-32", "D:\\_Archive", 257, 5387059, "Archive", "duplicate_variant", now()),
        ("paper-00-paper-80", "D:\\Paper Reworks", 11, 230686, "Paper Reworks", "duplicate_variant", now()),
        ("paper-00-paper-37", "D:\\MannyAI", 46, 964689, "MannyAI", "partially_unique", now()),
        ("unassigned", "Various (AirLock, R30, Forge, PDF_MASTER, etc.)", 797, 16724787, "Small Collections", "duplicate_variant", now()),
    ]
    c.executemany("""
        INSERT INTO paper_sources (paper_number, source_path, file_count, size_bytes, collection_name, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, paper_sources_data)

    c.execute("SELECT mapping_id, paper_number, source_path, file_count, size_bytes, collection_name, status, created_at FROM paper_sources")
    for row in c.fetchall():
        content = json.dumps(row[1:], sort_keys=True)
        cam = sha256_content(content)
        c.execute("UPDATE paper_sources SET cam_hash = ? WHERE mapping_id = ?", (cam, row[0]))

    # ============================================================
    # Populate routing_rules
    # ============================================================
    # Get agent_id map
    c.execute("SELECT agent_id, agent_name FROM agents")
    agent_map = {name: aid for aid, name in c.fetchall()}

    routing_data = [
        ("paper-00", "paper-00", "control_plane", agent_map.get("LCR Kernel Agent"), "Prefer Repo-Kernel /api/global/... and /call-plan routes over direct upstream ports. Kernel-level I-calibration inputs.", "active", now()),
        ("paper-10-paper-30", "paper-10-paper-30", "service_route", agent_map.get("PartsFactory Agent"), "MCP routes, service details, hard constraints. Forge runtime wrapper substrate.", "active", now()),
        ("paper-40-paper-60", "paper-40-paper-60", "product_route", agent_map.get("1T Production Agent"), "Product placement rules, forge routing, fourpack surfaces. Product surfaces belong in src/products/.", "active", now()),
        ("paper-45", "paper-45", "product_route", agent_map.get("GaussHaus Agent"), "Gaussian / Hausdorff lane product surface routing.", "active", now()),
        ("paper-70", "paper-70", "verification_route", agent_map.get("Standards Agent"), "D-verification lab, validator/grading surface. make boot validate paper00 triggers paper-00 smoke test.", "active", now()),
        ("paper-90", "paper-90", "tool_route", agent_map.get("Workbench Agent"), "Paper pipeline tooling, registry, dev loops. Prefer SQLite/fs for discovery, receipts, caches.", "active", now()),
        ("paper-100", "paper-100", "showroom_route", agent_map.get("Showroom Agent"), "Master showroom navigation, capstone reference. Not a production edit target.", "reference", now()),
        ("paper-26", "paper-26", "cam_route", agent_map.get("CAM Crystal Agent"), "MannyAI runtime and CAM crystal projector. Forge substrate for reasoning tasks.", "active", now()),
        ("paper-20-paper-30", "paper-20-paper-30", "exciton_route", None, "Exciton/materials formalism spans D_claim_citation_bound and I_calibration_input lanes.", "active", now()),
        ("paper-50", "paper-50", "gr_route", None, "GR hyperbolic methods provide citation-bound formalism boundary. D_claim_citation_bound.", "active", now()),
        ("paper-60", "paper-60", "plasma_route", None, "Plasma magnetic confinement and diagnostics. Mixed D_claim_citation_bound + I_calibration_input.", "active", now()),
        ("paper-01", "paper-01", "citation_route", None, "PDG reviews are citation-bound claims for particle data. D_claim_citation_bound.", "active", now()),
        ("paper-02", "paper-02", "calibration_route", None, "Higgs discovery evidence provides mass-scale calibration surfaces. I_calibration_input.", "active", now()),
        ("paper-03", "paper-03", "boundary_route", None, "Neutrino oscillation evidence sets boundary for beyond-minimal claims. D_claim_citation_bound.", "active", now()),
    ]
    c.executemany("""
        INSERT INTO routing_rules (from_paper, to_paper, rule_type, agent_id, description, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, routing_data)

    c.execute("SELECT rule_id, from_paper, to_paper, rule_type, agent_id, description, status, created_at FROM routing_rules")
    for row in c.fetchall():
        content = json.dumps(row[1:], sort_keys=True)
        cam = sha256_content(content)
        c.execute("UPDATE routing_rules SET cam_hash = ? WHERE rule_id = ?", (cam, row[0]))

    # ============================================================
    # Populate storage_needs
    # ============================================================
    storage_data = [
        (system_map.get("LCR Kernel"), "filesystem", "minimal", "kernel-level", "paper-00", "active", now()),
        (system_map.get("PartsFactory"), "docker_volumes", "medium", "service orchestration", "paper-10-paper-30", "active", now()),
        (system_map.get("1T-Production"), "docker_volumes", "medium", "product surfaces", "paper-40-paper-60", "active", now()),
        (system_map.get("GaussHaus"), "docker_volumes", "small", "product lane", "paper-45", "active", now()),
        (system_map.get("Standards"), "docker_volumes", "small", "verification lab", "paper-70", "active", now()),
        (system_map.get("Workbench"), "sqlite", "small", "dev loops and caches", "paper-90", "active", now()),
        (system_map.get("Showroom"), "filesystem", "minimal", "read-only reference", "paper-100", "reference", now()),
        (system_map.get("CAM Crystal"), "docker_volumes", "large", "CAM projection and runtime", "paper-26", "active", now()),
        (system_map.get("Proof Lab"), "docker_volumes", "medium", "proof verification and receipts", "paper-70", "active", now()),
        (system_map.get("Receipt Service"), "docker_volumes", "small", "claim receipt storage", "paper-20", "active", now()),
        (None, "irl_binary", "245000000 bytes", "O1 Weyl E8 subtable (1M of 696M records)", "unassigned", "partial", now()),
        (None, "aggregate", "232785920 bytes", "Total canonical + duplicate file storage across all collections", "paper-00-paper-100", "active", now()),
    ]
    c.executemany("""
        INSERT INTO storage_needs (system_id, storage_type, capacity, usage, paper_number, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, storage_data)

    c.execute("SELECT need_id, system_id, storage_type, capacity, usage, paper_number, status, created_at FROM storage_needs")
    for row in c.fetchall():
        content = json.dumps(row[1:], sort_keys=True)
        cam = sha256_content(content)
        c.execute("UPDATE storage_needs SET cam_hash = ? WHERE need_id = ?", (cam, row[0]))

    conn.commit()

    # ============================================================
    # Export schema to SQL file
    # ============================================================
    with open(SCHEMA_PATH, "w", encoding="utf-8") as f:
        for line in conn.iterdump():
            f.write(line + "\n")

    # ============================================================
    # Summary
    # ============================================================
    tables = ["systems", "obligations", "agents", "docker_services", "external_sources", "paper_sources", "routing_rules", "storage_needs"]
    summary = {}
    for t in tables:
        c.execute(f"SELECT COUNT(*) FROM {t}")
        summary[t] = c.fetchone()[0]

    conn.close()
    print("Database built successfully.")
    print(f"Database path: {DB_PATH}")
    print(f"Schema path: {SCHEMA_PATH}")
    print("Row counts:")
    for t, count in summary.items():
        print(f"  {t}: {count}")
    return summary

def main(ctx):
    return build_database()
