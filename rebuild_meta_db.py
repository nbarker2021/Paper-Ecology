"""
rebuild_meta_db.py
Rebuild the unified Paper Ecology meta-database from all 9 Libs.
Uses latest data from SQLite databases in each Lib directory.
Strip ALL B-family identity; enforce A-family naming only.
"""

import sqlite3
import os
import json
import re
from datetime import datetime
from collections import defaultdict, Counter

META_DB_PATH = r"D:\Paper Ecology\PAPER_ECOLOGY_META.db"
META_SCHEMA_PATH = r"D:\Paper Ecology\paper_ecology_meta_schema.sql"

LIBS = {
    'CMPLX-Standards': {
        'db_path': r'D:\Paper Ecology\CMPLX-Standards\cmplx_standards.db',
        'lib_path': r'D:\Paper Ecology\CMPLX-Standards',
        'claim_table': None,
        'cross_ref_table': None,
        'cam_hash_table': 'cam_hashes',
        'paper_table': 'standards_papers',
    },
    'CodeLib': {
        'db_path': r'D:\Paper Ecology\CodeLib\code_lib.db',
        'lib_path': r'D:\Paper Ecology\CodeLib',
        'claim_table': 'code_claims',
        'cross_ref_table': None,
        'cam_hash_table': 'cam_hashes',
        'paper_table': 'code_papers',
    },
    'CrystalLib': {
        'db_path': r'D:\Paper Ecology\CrystalLib\crystal_lib.db',
        'lib_path': r'D:\Paper Ecology\CrystalLib',
        'claim_table': 'claims',
        'cross_ref_table': 'cross_references',
        'cam_hash_table': 'cam_hashes',
        'paper_table': 'papers',
    },
    'PaperLib': {
        'db_path': r'D:\Paper Ecology\PaperLib\paper_lib.db',
        'lib_path': r'D:\Paper Ecology\PaperLib',
        'claim_table': 'claims',
        'cross_ref_table': 'cross_references',
        'cam_hash_table': 'cam_hashes',
        'paper_table': 'papers',
    },
    'ReForge_ForgeLib': {
        'db_path': r'D:\Paper Ecology\ReForge_ForgeLib\reforge_forge_lib.db',
        'lib_path': r'D:\Paper Ecology\ReForge_ForgeLib',
        'claim_table': 'forge_claims',
        'cross_ref_table': None,
        'cam_hash_table': None,
        'paper_table': 'forge_papers',
    },
    'SQLLib': {
        'db_path': r'D:\Paper Ecology\SQLLib\sql_lib.db',
        'lib_path': r'D:\Paper Ecology\SQLLib',
        'claim_table': 'sql_claims',
        'cross_ref_table': None,
        'cam_hash_table': 'cam_hashes',
        'paper_table': 'sql_papers',
    },
    'SystemsLib': {
        'db_path': r'D:\Paper Ecology\SystemsLib\systems_lib.db',
        'lib_path': r'D:\Paper Ecology\SystemsLib',
        'claim_table': None,
        'cross_ref_table': 'routing_rules',
        'cam_hash_table': None,
        'paper_table': 'paper_sources',
    },
    'TileLib': {
        'db_path': r'D:\Paper Ecology\TileLib\tile_lib.db',
        'lib_path': r'D:\Paper Ecology\TileLib',
        'claim_table': 'tile_claims',
        'cross_ref_table': None,
        'cam_hash_table': None,
        'paper_table': 'tile_papers',
    },
    'cqekernel': {
        'db_path': r'D:\Paper Ecology\cqekernel\cqekernel.db',
        'lib_path': r'D:\Paper Ecology\cqekernel',
        'claim_table': 'kernel_claims',
        'cross_ref_table': 'cross_lib_refs',
        'cam_hash_table': 'cam_hashes',
        'paper_table': 'kernel_papers',
    },
}


def normalize_paper_number(pn):
    """Normalize paper number to paper-XX format. Only accepts valid paper numbers 0-100."""
    if pn is None:
        return None
    if isinstance(pn, int):
        if 0 <= pn <= 100:
            return f'paper-{pn:02d}' if pn < 100 else f'paper-{pn}'
        return None
    s = str(pn).strip().lower()
    m = re.match(r'paper[-_]?(\d+)', s)
    if m:
        try:
            num = int(m.group(1))
            if 0 <= num <= 100:
                return f'paper-{num:02d}' if num < 100 else f'paper-{num}'
        except ValueError:
            pass
    try:
        num = int(s)
        if 0 <= num <= 100:
            return f'paper-{num:02d}' if num < 100 else f'paper-{num}'
    except ValueError:
        pass
    return None


def strip_b_family(text):
    """Replace B-family identity with A-family naming."""
    if text is None:
        return None
    if not isinstance(text, str):
        text = str(text)
    # Core B-family variants
    text = text.replace('B_family', 'A_family')
    text = text.replace('B-family', 'A-family')
    text = text.replace('B family', 'A family')
    text = text.replace('B-Family', 'A-Family')
    text = text.replace('B FAMILY', 'A FAMILY')
    text = text.replace('B_family_lattice_forge', 'A_family_lattice_forge')
    text = text.replace('B_family_forge', 'A_family_forge')
    # Additional B-family identities found in corpus
    text = text.replace('CrystalForge', 'Forge')
    text = text.replace('FLCR', 'LCR')
    text = text.replace('TMN', 'A-Network')
    return text


def get_db_connection(db_path):
    if not os.path.exists(db_path):
        return None
    try:
        return sqlite3.connect(db_path)
    except Exception:
        return None


def build_meta_db():
    if os.path.exists(META_DB_PATH):
        os.remove(META_DB_PATH)

    meta_conn = sqlite3.connect(META_DB_PATH)
    meta_cur = meta_conn.cursor()

    meta_cur.execute('''
        CREATE TABLE meta_papers (
            paper_number TEXT PRIMARY KEY,
            title TEXT,
            status TEXT,
            total_claims INTEGER DEFAULT 0,
            d_claims INTEGER DEFAULT 0,
            i_claims INTEGER DEFAULT 0,
            x_claims INTEGER DEFAULT 0,
            libs_covering TEXT,
            primary_lib TEXT,
            cam_hash TEXT
        )
    ''')

    meta_cur.execute('''
        CREATE TABLE meta_libs (
            lib_name TEXT PRIMARY KEY,
            lib_path TEXT,
            db_path TEXT,
            tables TEXT,
            rows INTEGER DEFAULT 0,
            paper_coverage INTEGER DEFAULT 0,
            claim_coverage INTEGER DEFAULT 0,
            status TEXT
        )
    ''')

    meta_cur.execute('''
        CREATE TABLE meta_claims (
            claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
            paper_number TEXT,
            claim_text TEXT,
            claim_status TEXT,
            source_lib TEXT,
            source_table TEXT,
            cam_hash TEXT
        )
    ''')

    meta_cur.execute('''
        CREATE TABLE meta_cross_refs (
            ref_id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_paper TEXT,
            to_paper TEXT,
            ref_type TEXT,
            source_lib TEXT,
            cam_hash TEXT
        )
    ''')

    meta_cur.execute('''
        CREATE TABLE meta_gaps (
            gap_id INTEGER PRIMARY KEY AUTOINCREMENT,
            paper_number TEXT,
            gap_type TEXT,
            severity TEXT,
            recommendation TEXT
        )
    ''')

    meta_cur.execute('''
        CREATE TABLE cam_hashes (
            cam_hash TEXT PRIMARY KEY,
            content_type TEXT,
            content_id TEXT,
            source_lib TEXT,
            created_at TEXT
        )
    ''')

    meta_conn.commit()
    return meta_conn, meta_cur


def populate_meta_libs(meta_cur):
    for lib_name, lib_info in LIBS.items():
        db_path = lib_info['db_path']
        lib_path = lib_info['lib_path']
        conn = get_db_connection(db_path)
        if not conn:
            meta_cur.execute('''
                INSERT INTO meta_libs (lib_name, lib_path, db_path, tables, rows, paper_coverage, claim_coverage, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (lib_name, lib_path, db_path, '', 0, 0, 0, 'missing'))
            continue

        cur = conn.cursor()

        # Get tables (excluding sqlite_sequence)
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [r[0] for r in cur.fetchall() if r[0] != 'sqlite_sequence']
        tables_str = ','.join(tables)

        total_rows = 0
        for t in tables:
            try:
                cur.execute(f"SELECT COUNT(*) FROM {t}")
                total_rows += cur.fetchone()[0]
            except:
                pass

        paper_coverage = 0
        if lib_info['paper_table']:
            try:
                cur.execute(f"SELECT COUNT(DISTINCT paper_number) FROM {lib_info['paper_table']}")
                paper_coverage = cur.fetchone()[0]
            except:
                pass

        claim_coverage = 0
        if lib_info['claim_table']:
            try:
                cur.execute(f"SELECT COUNT(*) FROM {lib_info['claim_table']}")
                claim_coverage = cur.fetchone()[0]
            except:
                pass

        meta_cur.execute('''
            INSERT INTO meta_libs (lib_name, lib_path, db_path, tables, rows, paper_coverage, claim_coverage, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (lib_name, lib_path, db_path, tables_str, total_rows, paper_coverage, claim_coverage, 'active'))

        conn.close()


def extract_claims_from_db(lib_name, lib_info):
    conn = get_db_connection(lib_info['db_path'])
    if not conn or not lib_info['claim_table']:
        return []

    cur = conn.cursor()
    claims = []
    try:
        cur.execute(f"PRAGMA table_info({lib_info['claim_table']})")
        cols = [c[1] for c in cur.fetchall()]

        claim_id_col = 'claim_id' if 'claim_id' in cols else (cols[0] if cols else None)
        paper_col = 'paper_number' if 'paper_number' in cols else None
        text_col = 'claim_text' if 'claim_text' in cols else None
        status_col = 'claim_status' if 'claim_status' in cols else None
        cam_col = 'cam_hash' if 'cam_hash' in cols else None

        if paper_col and text_col:
            select_cols = [claim_id_col, paper_col, text_col, status_col, cam_col]
            select_cols = [c for c in select_cols if c]
            sql = f"SELECT {', '.join(select_cols)} FROM {lib_info['claim_table']}"
            cur.execute(sql)
            for row in cur.fetchall():
                claim = {
                    'paper_number': normalize_paper_number(row[1] if len(row) > 1 else None),
                    'claim_text': strip_b_family(row[2]) if len(row) > 2 else None,
                    'claim_status': (row[3] or 'U').upper() if len(row) > 3 else 'U',
                    'source_lib': lib_name,
                    'source_table': lib_info['claim_table'],
                    'cam_hash': row[4] if len(row) > 4 else None,
                }
                claims.append(claim)
    except Exception as e:
        print(f"Warning: could not extract claims from {lib_name}.{lib_info['claim_table']}: {e}")

    conn.close()
    return claims


def get_paper_number_int(pn):
    """Extract integer from normalized paper-number string, or return as-is if already int."""
    if pn is None:
        return None
    if isinstance(pn, int):
        return pn
    m = re.match(r'paper-(\d+)', str(pn))
    if m:
        return int(m.group(1))
    try:
        return int(pn)
    except ValueError:
        return None


def extract_cross_refs_from_db(lib_name, lib_info):
    conn = get_db_connection(lib_info['db_path'])
    if not conn or not lib_info['cross_ref_table']:
        return []

    cur = conn.cursor()
    refs = []
    try:
        cur.execute(f"PRAGMA table_info({lib_info['cross_ref_table']})")
        cols = [c[1] for c in cur.fetchall()]

        from_col = 'from_paper' if 'from_paper' in cols else None
        to_col = 'to_paper' if 'to_paper' in cols else None
        type_col = 'ref_type' if 'ref_type' in cols else None
        if not type_col:
            type_col = 'type' if 'type' in cols else None
        cam_col = 'cam_hash' if 'cam_hash' in cols else None

        if from_col and to_col:
            select_cols = [from_col, to_col, type_col, cam_col]
            select_cols = [c for c in select_cols if c]
            sql = f"SELECT {', '.join(select_cols)} FROM {lib_info['cross_ref_table']}"
            cur.execute(sql)
            for row in cur.fetchall():
                ref = {
                    'from_paper': normalize_paper_number(row[0]),
                    'to_paper': normalize_paper_number(row[1]),
                    'ref_type': row[2] if len(row) > 2 and row[2] else 'ref',
                    'source_lib': lib_name,
                    'cam_hash': row[3] if len(row) > 3 else None,
                }
                refs.append(ref)
    except Exception as e:
        print(f"Warning: could not extract cross refs from {lib_name}.{lib_info['cross_ref_table']}: {e}")

    conn.close()
    return refs


def extract_cam_hashes_from_db(lib_name, lib_info):
    conn = get_db_connection(lib_info['db_path'])
    if not conn:
        return []

    cur = conn.cursor()
    hashes = []

    if lib_info['cam_hash_table']:
        try:
            cur.execute(f"SELECT cam_hash, content_type, content_id, created_at FROM {lib_info['cam_hash_table']}")
            for row in cur.fetchall():
                hashes.append({
                    'cam_hash': row[0],
                    'content_type': strip_b_family(row[1]) if len(row) > 1 else None,
                    'content_id': strip_b_family(str(row[2])) if len(row) > 2 else None,
                    'source_lib': lib_name,
                    'created_at': row[3] if len(row) > 3 else None,
                })
        except Exception as e:
            pass

    if not hashes:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [r[0] for r in cur.fetchall()]
        for t in tables:
            if t == 'sqlite_sequence':
                continue
            try:
                cur.execute(f"PRAGMA table_info({t})")
                cols = [c[1] for c in cur.fetchall()]
                if 'cam_hash' in cols:
                    id_col = [c for c in cols if c in ['rowid', 'id', 'claim_id', 'ref_id', 'paper_number']]
                    id_col = id_col[0] if id_col else cols[0]
                    cur.execute(f"SELECT DISTINCT cam_hash, {id_col} FROM {t} WHERE cam_hash IS NOT NULL AND cam_hash != ''")
                    for row in cur.fetchall():
                        if row[0] and row[0] not in {h['cam_hash'] for h in hashes}:
                            hashes.append({
                                'cam_hash': row[0],
                                'content_type': t,
                                'content_id': str(row[1]) if len(row) > 1 else None,
                                'source_lib': lib_name,
                                'created_at': None,
                            })
            except:
                pass

    conn.close()
    return hashes


def get_paper_title(pn):
    conn = get_db_connection(LIBS['PaperLib']['db_path'])
    if not conn:
        return None
    cur = conn.cursor()
    try:
        cur.execute("SELECT title FROM papers WHERE paper_number = ?", (pn,))
        row = cur.fetchone()
        if row and row[0]:
            return strip_b_family(row[0])
    except:
        pass
    conn.close()

    # Fallback to CrystalLib
    conn = get_db_connection(LIBS['CrystalLib']['db_path'])
    if not conn:
        return None
    cur = conn.cursor()
    try:
        cur.execute("SELECT title FROM papers WHERE paper_number = ?", (pn,))
        row = cur.fetchone()
        if row and row[0]:
            return strip_b_family(row[0])
    except:
        pass
    conn.close()
    return None


def get_paper_cam_hash(pn):
    conn = get_db_connection(LIBS['PaperLib']['db_path'])
    if not conn:
        return None
    cur = conn.cursor()
    try:
        cur.execute("SELECT cam_hash FROM papers WHERE paper_number = ?", (pn,))
        row = cur.fetchone()
        if row and row[0]:
            return row[0]
    except:
        pass
    conn.close()
    return None


def main():
    print("=" * 60)
    print("Paper Ecology Meta-Database Rebuild")
    print(f"Started: {datetime.now().isoformat()}")
    print("=" * 60)

    meta_conn, meta_cur = build_meta_db()

    # 1. Populate meta_libs
    print("\n[1/6] Populating meta_libs...")
    populate_meta_libs(meta_cur)
    meta_conn.commit()
    print("  Done.")

    # Collect all unique papers
    all_papers = set()
    for i in range(101):
        all_papers.add(f'paper-{i:02d}' if i < 100 else f'paper-{i}')

    # Also gather from databases
    for lib_name, lib_info in LIBS.items():
        conn = get_db_connection(lib_info['db_path'])
        if not conn:
            continue
        cur = conn.cursor()
        if lib_info['paper_table']:
            try:
                cur.execute(f"SELECT DISTINCT paper_number FROM {lib_info['paper_table']}")
                for row in cur.fetchall():
                    if row[0]:
                        all_papers.add(normalize_paper_number(row[0]))
            except:
                pass
        if lib_info['claim_table']:
            try:
                cur.execute(f"SELECT DISTINCT paper_number FROM {lib_info['claim_table']}")
                for row in cur.fetchall():
                    if row[0]:
                        all_papers.add(normalize_paper_number(row[0]))
            except:
                pass
        conn.close()

    all_papers = sorted([p for p in all_papers if p is not None])
    print(f"\n  Total canonical papers: {len(all_papers)}")

    # 2. Extract claims from all libs
    print("\n[2/6] Extracting claims...")
    all_claims = []
    lib_claim_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for lib_name, lib_info in LIBS.items():
        claims = extract_claims_from_db(lib_name, lib_info)
        all_claims.extend(claims)
        for c in claims:
            pn = c['paper_number']
            if pn:
                lib_claim_counts[lib_name][pn][c['claim_status']] += 1
    print(f"  Total claims extracted: {len(all_claims)}")

    # 3. Extract cross-references
    print("\n[3/6] Extracting cross-references...")
    all_refs = []
    for lib_name, lib_info in LIBS.items():
        refs = extract_cross_refs_from_db(lib_name, lib_info)
        all_refs.extend(refs)
    print(f"  Total cross-references extracted: {len(all_refs)}")

    # 4. Extract CAM hashes
    print("\n[4/6] Extracting CAM hashes...")
    all_hashes = []
    for lib_name, lib_info in LIBS.items():
        hashes = extract_cam_hashes_from_db(lib_name, lib_info)
        all_hashes.extend(hashes)
    print(f"  Total CAM hash records extracted: {len(all_hashes)}")

    # 5. Populate meta_papers
    print("\n[5/6] Populating meta_papers...")
    for pn in all_papers:
        title = get_paper_title(pn)
        if not title:
            title = f"Paper {pn.replace('paper-', '')}"

        # Determine status from CodeLib (or default to stub if no verifier)
        has_verifier = False
        for lib_name, lib_info in LIBS.items():
            if lib_name != 'CodeLib':
                continue
            conn = get_db_connection(lib_info['db_path'])
            if not conn:
                continue
            cur = conn.cursor()
            try:
                int_pn = get_paper_number_int(pn)
                cur.execute("SELECT COUNT(*) FROM code_files WHERE paper_number IN (?, ?) AND status = 'real'", (pn, int_pn))
                if cur.fetchone()[0] > 0:
                    has_verifier = True
                cur.execute("SELECT COUNT(*) FROM code_papers WHERE paper_number IN (?, ?) AND status = 'real'", (pn, int_pn))
                if cur.fetchone()[0] > 0:
                    has_verifier = True
            except:
                pass
            conn.close()

        status = 'real' if has_verifier else 'stub'

        # Aggregate claim counts across ALL libs
        total_claims = 0
        d_claims = 0
        i_claims = 0
        x_claims = 0
        covering_libs = []
        primary_lib = None
        max_claims = 0

        for lib_name, lib_info in LIBS.items():
            pn_counts = lib_claim_counts[lib_name].get(pn, {})
            if pn_counts:
                lib_total = sum(pn_counts.values())
                total_claims += lib_total
                d_claims += pn_counts.get('D', 0)
                i_claims += pn_counts.get('I', 0)
                x_claims += pn_counts.get('X', 0)
                covering_libs.append(lib_name)
                if lib_total > max_claims:
                    max_claims = lib_total
                    primary_lib = lib_name
            else:
                # Check if paper exists in paper_table without claims
                conn = get_db_connection(lib_info['db_path'])
                if conn and lib_info['paper_table']:
                    cur = conn.cursor()
                    try:
                        int_pn = get_paper_number_int(pn)
                        cur.execute(f"SELECT COUNT(*) FROM {lib_info['paper_table']} WHERE paper_number IN (?, ?)", (pn, int_pn))
                        if cur.fetchone()[0] > 0:
                            covering_libs.append(lib_name)
                    except:
                        pass
                    conn.close()

        libs_covering_str = ','.join(sorted(set(covering_libs))) if covering_libs else ''
        if not primary_lib and covering_libs:
            primary_lib = covering_libs[0]

        cam_hash = get_paper_cam_hash(pn)

        meta_cur.execute('''
            INSERT INTO meta_papers (paper_number, title, status, total_claims, d_claims, i_claims, x_claims, libs_covering, primary_lib, cam_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (pn, title, status, total_claims, d_claims, i_claims, x_claims, libs_covering_str, primary_lib, cam_hash))

    meta_conn.commit()
    print(f"  {len(all_papers)} papers inserted.")

    # 6. Populate meta_claims
    print("\n[6/6] Populating meta_claims, meta_cross_refs, meta_gaps, cam_hashes...")
    for claim in all_claims:
        meta_cur.execute('''
            INSERT INTO meta_claims (paper_number, claim_text, claim_status, source_lib, source_table, cam_hash)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (claim['paper_number'], claim['claim_text'], claim['claim_status'], claim['source_lib'], claim['source_table'], claim['cam_hash']))
    meta_conn.commit()
    print(f"  meta_claims: {len(all_claims)} rows")

    for ref in all_refs:
        meta_cur.execute('''
            INSERT INTO meta_cross_refs (from_paper, to_paper, ref_type, source_lib, cam_hash)
            VALUES (?, ?, ?, ?, ?)
        ''', (ref['from_paper'], ref['to_paper'], ref['ref_type'], ref['source_lib'], ref['cam_hash']))
    meta_conn.commit()
    print(f"  meta_cross_refs: {len(all_refs)} rows")

    # CAM hashes (deduplicated)
    seen_hashes = set()
    cam_inserted = 0
    for h in all_hashes:
        if h['cam_hash'] and h['cam_hash'] not in seen_hashes:
            seen_hashes.add(h['cam_hash'])
            meta_cur.execute('''
                INSERT OR IGNORE INTO cam_hashes (cam_hash, content_type, content_id, source_lib, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (h['cam_hash'], h['content_type'], h['content_id'], h['source_lib'], h['created_at']))
            cam_inserted += 1
    meta_conn.commit()
    print(f"  cam_hashes: {cam_inserted} unique rows")

    # GAP ANALYSIS
    print("\n[Gap Analysis]")
    gap_checks = {
        'no_d_claims': 0,
        'no_receipts': 0,
        'no_std': 0,
        'no_code_verifier': 0,
    }

    # 1. Papers with no D-claims in any Lib
    for pn in all_papers:
        has_d = False
        for lib_name in LIBS:
            if lib_claim_counts[lib_name].get(pn, {}).get('D', 0) > 0:
                has_d = True
                break
        if not has_d:
            gap_checks['no_d_claims'] += 1
            meta_cur.execute('''
                INSERT INTO meta_gaps (paper_number, gap_type, severity, recommendation)
                VALUES (?, ?, ?, ?)
            ''', (pn, 'no_d_claims', 'high', 'Add data-backed (D) claims to this paper'))

    # 2. Papers with no receipts in CrystalLib
    conn = get_db_connection(LIBS['CrystalLib']['db_path'])
    if conn:
        cur = conn.cursor()
        receipt_papers = set()
        try:
            cur.execute('''
                SELECT DISTINCT c.paper_number
                FROM crystals c
                JOIN receipts r ON c.crystal_id = r.crystal_id
                WHERE c.paper_number IS NOT NULL
            ''')
            for row in cur.fetchall():
                p = normalize_paper_number(row[0])
                if p:
                    receipt_papers.add(p)
        except Exception as e:
            print(f"  Warning: Could not query CrystalLib receipts: {e}")
        conn.close()
        for pn in all_papers:
            if pn not in receipt_papers:
                gap_checks['no_receipts'] += 1
                meta_cur.execute('''
                    INSERT INTO meta_gaps (paper_number, gap_type, severity, recommendation)
                    VALUES (?, ?, ?, ?)
                ''', (pn, 'no_receipts', 'high', 'Generate CrystalLib receipt for this paper'))

    # 3. Papers with empty CMPLX-Standards
    conn = get_db_connection(LIBS['CMPLX-Standards']['db_path'])
    if conn:
        cur = conn.cursor()
        std_papers = set()
        try:
            cur.execute("SELECT DISTINCT paper_number FROM standards_papers WHERE paper_number IS NOT NULL")
            for row in cur.fetchall():
                p = normalize_paper_number(row[0])
                if p:
                    std_papers.add(p)
        except Exception as e:
            print(f"  Warning: Could not query CMPLX-Standards: {e}")
        conn.close()
        for pn in all_papers:
            if pn not in std_papers:
                gap_checks['no_std'] += 1
                meta_cur.execute('''
                    INSERT INTO meta_gaps (paper_number, gap_type, severity, recommendation)
                    VALUES (?, ?, ?, ?)
                ''', (pn, 'no_std', 'high', 'Map paper to CMPLX-Standards contract'))

    # 4. Papers with no code verifier
    conn = get_db_connection(LIBS['CodeLib']['db_path'])
    if conn:
        cur = conn.cursor()
        verifier_papers = set()
        try:
            cur.execute("SELECT DISTINCT paper_number FROM code_files WHERE status IS NOT NULL")
            for row in cur.fetchall():
                p = normalize_paper_number(row[0])
                if p:
                    verifier_papers.add(p)
            cur.execute("SELECT DISTINCT paper_number FROM code_papers WHERE status IS NOT NULL")
            for row in cur.fetchall():
                p = normalize_paper_number(row[0])
                if p:
                    verifier_papers.add(p)
        except Exception as e:
            print(f"  Warning: Could not query CodeLib: {e}")
        conn.close()
        for pn in all_papers:
            if pn not in verifier_papers:
                gap_checks['no_code_verifier'] += 1
                meta_cur.execute('''
                    INSERT INTO meta_gaps (paper_number, gap_type, severity, recommendation)
                    VALUES (?, ?, ?, ?)
                ''', (pn, 'no_code_verifier', 'high', 'Add or register code verifier for this paper'))

    meta_conn.commit()
    print(f"  no_d_claims gaps: {gap_checks['no_d_claims']}")
    print(f"  no_receipts gaps: {gap_checks['no_receipts']}")
    print(f"  no_std gaps: {gap_checks['no_std']}")
    print(f"  no_code_verifier gaps: {gap_checks['no_code_verifier']}")
    print(f"  Total gaps recorded: {sum(gap_checks.values())}")

    # Export schema
    print(f"\n[Export] Writing schema to {META_SCHEMA_PATH}...")
    with open(META_SCHEMA_PATH, 'w', encoding='utf-8') as f:
        for line in meta_conn.iterdump():
            f.write(line + '\n')
    print("  Done.")

    # Final stats
    print("\n" + "=" * 60)
    print("Rebuild Complete")
    print("=" * 60)
    for table in ['meta_papers', 'meta_libs', 'meta_claims', 'meta_cross_refs', 'meta_gaps', 'cam_hashes']:
        meta_cur.execute(f"SELECT COUNT(*) FROM {table}")
        count = meta_cur.fetchone()[0]
        print(f"  {table}: {count} rows")

    meta_conn.close()
    print(f"\nFinished: {datetime.now().isoformat()}")


if __name__ == '__main__':
    main()
