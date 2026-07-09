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
        'cam_hash_table': None,
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
    # Match paper-XX or paper_XX where XX is 0-100
    m = re.match(r'paper[-_]?(\d+)', s)
    if m:
        try:
            num = int(m.group(1))
            if 0 <= num <= 100:
                return f'paper-{num:02d}' if num < 100 else f'paper-{num}'
        except ValueError:
            pass
    # Try to parse as raw number 0-100
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
    text = text.replace('B_family', 'A_family')
    text = text.replace('B-family', 'A-family')
    text = text.replace('B family', 'A family')
    text = text.replace('B-Family', 'A-Family')
    text = text.replace('B FAMILY', 'A FAMILY')
    text = text.replace('B_family_lattice_forge', 'A_family_lattice_forge')
    text = text.replace('B_family_forge', 'A_family_forge')
    return text

def get_db_connection(db_path):
    if not os.path.exists(db_path):
        return None
    try:
        return sqlite3.connect(db_path)
    except Exception:
        return None

def read_gap_matrix():
    with open(r'D:\Paper Ecology\gap_matrix_raw.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def read_paper_indices():
    indices = {}
    # paper_index_00_25.json is a dict keyed by "00", "01", etc.
    path = r'D:\Paper Ecology\paper_index_00_25.json'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for k, v in data.items():
            pn = normalize_paper_number(v.get('paper_number', k))
            indices[pn] = v
    
    # paper_index_51_75.json is a list
    path = r'D:\Paper Ecology\paper_index_51_75.json'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            pn = normalize_paper_number(item.get('paper_number'))
            if pn:
                indices[pn] = item
    
    # PaperLib_Index_76-100.json is a list
    path = r'D:\Paper Ecology\PaperLib_Index_76-100.json'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            pn = normalize_paper_number(item.get('paper_number'))
            if pn:
                indices[pn] = item
    
    return indices

def build_meta_db():
    # Remove existing meta db if present
    if os.path.exists(META_DB_PATH):
        os.remove(META_DB_PATH)
    
    meta_conn = sqlite3.connect(META_DB_PATH)
    meta_cur = meta_conn.cursor()
    
    # Create tables
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
            continue
        
        cur = conn.cursor()
        
        # Get tables
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [r[0] for r in cur.fetchall()]
        tables_str = ','.join(tables)
        
        # Count total rows
        total_rows = 0
        for t in tables:
            try:
                cur.execute(f"SELECT COUNT(*) FROM {t}")
                total_rows += cur.fetchone()[0]
            except:
                pass
        
        # Paper coverage
        paper_coverage = 0
        if lib_info['paper_table']:
            try:
                cur.execute(f"SELECT COUNT(DISTINCT paper_number) FROM {lib_info['paper_table']}")
                paper_coverage = cur.fetchone()[0]
            except:
                pass
        
        # Claim coverage
        claim_coverage = 0
        if lib_info['claim_table']:
            try:
                cur.execute(f"SELECT COUNT(*) FROM {lib_info['claim_table']}")
                claim_coverage = cur.fetchone()[0]
            except:
                pass
        
        status = 'active' if conn else 'missing'
        
        meta_cur.execute('''
            INSERT INTO meta_libs (lib_name, lib_path, db_path, tables, rows, paper_coverage, claim_coverage, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (lib_name, lib_path, db_path, tables_str, total_rows, paper_coverage, claim_coverage, status))
        
        conn.close()

def count_claims_from_db(lib_name, lib_info):
    """Return dict of {paper_number: {status: count}} for claims in this lib."""
    conn = get_db_connection(lib_info['db_path'])
    if not conn or not lib_info['claim_table']:
        return {}
    
    cur = conn.cursor()
    results = defaultdict(lambda: defaultdict(int))
    try:
        cur.execute(f"SELECT paper_number, claim_status FROM {lib_info['claim_table']}")
        for row in cur.fetchall():
            pn = normalize_paper_number(row[0])
            status = (row[1] or 'U').upper()
            if pn:
                results[pn][status] += 1
    except Exception as e:
        print(f"Warning: could not count claims from {lib_name}.{lib_info['claim_table']}: {e}")
    
    conn.close()
    return results

def extract_claims_from_db(lib_name, lib_info):
    """Return list of claim dicts from this lib."""
    conn = get_db_connection(lib_info['db_path'])
    if not conn or not lib_info['claim_table']:
        return []
    
    cur = conn.cursor()
    claims = []
    try:
        cur.execute(f"PRAGMA table_info({lib_info['claim_table']})")
        cols = [c[1] for c in cur.fetchall()]
        
        # Find relevant columns
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

def extract_cross_refs_from_db(lib_name, lib_info):
    """Return list of cross-ref dicts from this lib."""
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
        type_col = type_col or ('type' if 'type' in cols else None)
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
    """Return list of cam_hash dicts from this lib."""
    conn = get_db_connection(lib_info['db_path'])
    if not conn:
        return []
    
    cur = conn.cursor()
    hashes = []
    
    # Try dedicated cam_hashes table first
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
    
    # If no dedicated table or no results, extract from other tables with cam_hash column
    if not hashes:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [r[0] for r in cur.fetchall()]
        for t in tables:
            try:
                cur.execute(f"PRAGMA table_info({t})")
                cols = [c[1] for c in cur.fetchall()]
                if 'cam_hash' in cols:
                    # Get distinct cam_hash values with a rowid/content identifier
                    id_col = [c for c in cols if c in ['rowid', 'id', 'claim_id', 'ref_id', 'paper_number']]
                    id_col = id_col[0] if id_col else cols[0]
                    cur.execute(f"SELECT DISTINCT cam_hash, {id_col} FROM {t} WHERE cam_hash IS NOT NULL AND cam_hash != ''")
                    for row in cur.fetchall():
                        if row[0] and row[0] not in [h['cam_hash'] for h in hashes]:
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

def get_paper_title_from_paperlib(pn):
    conn = get_db_connection(LIBS['PaperLib']['db_path'])
    if not conn:
        return None
    cur = conn.cursor()
    try:
        cur.execute("SELECT title FROM papers WHERE paper_number = ?", (pn,))
        row = cur.fetchone()
        if row:
            return strip_b_family(row[0])
    except:
        pass
    conn.close()
    return None

def get_paper_cam_hash_from_paperlib(pn):
    conn = get_db_connection(LIBS['PaperLib']['db_path'])
    if not conn:
        return None
    cur = conn.cursor()
    try:
        cur.execute("SELECT cam_hash FROM papers WHERE paper_number = ?", (pn,))
        row = cur.fetchone()
        if row:
            return row[0]
    except:
        pass
    conn.close()
    return None

def main():
    print("Building Paper Ecology Meta-Database...")
    
    gap_matrix = read_gap_matrix()
    gap_by_paper = {normalize_paper_number(p['paper']): p for p in gap_matrix}
    
    paper_indices = read_paper_indices()
    
    meta_conn, meta_cur = build_meta_db()
    
    # Populate meta_libs
    print("Populating meta_libs...")
    populate_meta_libs(meta_cur)
    meta_conn.commit()
    
    # Collect all paper data
    all_papers = set()
    for p in gap_matrix:
        all_papers.add(normalize_paper_number(p['paper']))
    
    # Also collect papers from databases
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
    print(f"Found {len(all_papers)} unique papers across all libraries.")
    
    # Count claims per paper per lib
    lib_claim_counts = {}
    for lib_name, lib_info in LIBS.items():
        lib_claim_counts[lib_name] = count_claims_from_db(lib_name, lib_info)
    
    # Extract all claims for meta_claims
    all_claims = []
    for lib_name, lib_info in LIBS.items():
        claims = extract_claims_from_db(lib_name, lib_info)
        all_claims.extend(claims)
    
    # Extract all cross refs for meta_cross_refs
    all_refs = []
    for lib_name, lib_info in LIBS.items():
        refs = extract_cross_refs_from_db(lib_name, lib_info)
        all_refs.extend(refs)
    
    # Extract all cam hashes
    all_hashes = []
    for lib_name, lib_info in LIBS.items():
        hashes = extract_cam_hashes_from_db(lib_name, lib_info)
        all_hashes.extend(hashes)
    
    # Populate meta_papers
    print("Populating meta_papers...")
    for pn in all_papers:
        # Title
        title = get_paper_title_from_paperlib(pn)
        if not title and pn in paper_indices:
            title = paper_indices[pn].get('title')
        if title:
            title = strip_b_family(title)
        else:
            title = f"Paper {pn.replace('paper-', '')}"
        
        # Status
        gap = gap_by_paper.get(pn, {})
        code_status = gap.get('CodeLib_status', 'I')
        if code_status == 'X':
            status = 'stub'
        elif code_status == 'I':
            status = 'partial'
        else:
            status = 'real'
        
        # Claim counts
        total_claims = 0
        d_claims = 0
        i_claims = 0
        x_claims = 0
        
        # Aggregate from all libs
        for lib_name, counts in lib_claim_counts.items():
            if pn in counts:
                total_claims += sum(counts[pn].values())
                d_claims += counts[pn].get('D', 0)
                i_claims += counts[pn].get('I', 0)
                x_claims += counts[pn].get('X', 0)
        
        # Add CMPLX-Standards counts from gap_matrix if available
        if gap:
            total_claims += gap.get('CMPLX_D', 0) + gap.get('CMPLX_I', 0) + gap.get('CMPLX_X', 0)
            d_claims += gap.get('CMPLX_D', 0)
            i_claims += gap.get('CMPLX_I', 0)
            x_claims += gap.get('CMPLX_X', 0)
        
        # Also add from paper indices for missing papers
        if pn in paper_indices:
            idx = paper_indices[pn]
            if 'd_count' in idx:
                # Only add if we haven't already counted from databases
                # This is tricky because the paper_index counts might overlap with CMPLX-Standards
                # We already added CMPLX from gap_matrix. For paper_index 00-25, the d_count/i_count/x_count
                # might be from CMPLX-Standards. So skip if gap_matrix already has them.
                pass
            elif 'claim_status_counts' in idx:
                # Same concern - skip to avoid double counting
                pass
        
        # Libs covering
        covering_libs = []
        for lib_name, lib_info in LIBS.items():
            if lib_name == 'CMPLX-Standards':
                if gap.get('CMPLX_Standards') == 'YES':
                    covering_libs.append(lib_name)
            elif lib_name == 'CodeLib':
                if gap.get('CodeLib') == 'YES':
                    covering_libs.append(lib_name)
            elif lib_name == 'SQLLib':
                if gap.get('SQLLib') == 'YES':
                    covering_libs.append(lib_name)
            elif lib_name == 'CrystalLib':
                if gap.get('CrystalLib_CAM') == 'YES':
                    covering_libs.append(lib_name)
            elif lib_name == 'ReForge_ForgeLib':
                if gap.get('ReForge') == 'YES':
                    covering_libs.append(lib_name)
            elif lib_name == 'SystemsLib':
                if gap.get('SystemsLib') == 'YES':
                    covering_libs.append(lib_name)
            elif lib_name == 'TileLib':
                if gap.get('TileLib') == 'YES':
                    covering_libs.append(lib_name)
            elif lib_name == 'cqekernel':
                if gap.get('cqekernel') == 'YES':
                    covering_libs.append(lib_name)
            elif lib_name == 'PaperLib':
                if gap.get('PaperLib') == 'YES':
                    covering_libs.append(lib_name)
        
        libs_covering_str = ','.join(covering_libs) if covering_libs else ''
        
        # Primary lib: the one with most claims
        primary_lib = None
        max_claims = 0
        for lib_name, counts in lib_claim_counts.items():
            if pn in counts:
                lib_total = sum(counts[pn].values())
                if lib_total > max_claims:
                    max_claims = lib_total
                    primary_lib = lib_name
        
        # If no claims anywhere, use PaperLib if available, or the first covering lib
        if not primary_lib:
            if 'PaperLib' in covering_libs:
                primary_lib = 'PaperLib'
            elif covering_libs:
                primary_lib = covering_libs[0]
        
        # CAM hash
        cam_hash = get_paper_cam_hash_from_paperlib(pn)
        if not cam_hash:
            # Try other libs
            for lib_name, lib_info in LIBS.items():
                if lib_info['paper_table']:
                    conn = get_db_connection(lib_info['db_path'])
                    if not conn:
                        continue
                    cur = conn.cursor()
                    try:
                        cur.execute(f"SELECT cam_hash FROM {lib_info['paper_table']} WHERE paper_number = ?", (pn,))
                        row = cur.fetchone()
                        if row and row[0]:
                            cam_hash = row[0]
                            break
                    except:
                        pass
                    conn.close()
        
        meta_cur.execute('''
            INSERT INTO meta_papers (paper_number, title, status, total_claims, d_claims, i_claims, x_claims, libs_covering, primary_lib, cam_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (pn, title, status, total_claims, d_claims, i_claims, x_claims, libs_covering_str, primary_lib, cam_hash))
    
    meta_conn.commit()
    
    # Populate meta_claims
    print(f"Populating meta_claims with {len(all_claims)} claims...")
    for claim in all_claims:
        meta_cur.execute('''
            INSERT INTO meta_claims (paper_number, claim_text, claim_status, source_lib, source_table, cam_hash)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (claim['paper_number'], claim['claim_text'], claim['claim_status'], claim['source_lib'], claim['source_table'], claim['cam_hash']))
    
    meta_conn.commit()
    
    # Populate meta_cross_refs
    print(f"Populating meta_cross_refs with {len(all_refs)} references...")
    for ref in all_refs:
        meta_cur.execute('''
            INSERT INTO meta_cross_refs (from_paper, to_paper, ref_type, source_lib, cam_hash)
            VALUES (?, ?, ?, ?, ?)
        ''', (ref['from_paper'], ref['to_paper'], ref['ref_type'], ref['source_lib'], ref['cam_hash']))
    
    meta_conn.commit()
    
    # Populate meta_gaps
    print("Populating meta_gaps...")
    for pn in all_papers:
        gap = gap_by_paper.get(pn, {})
        
        # Check for no_lib gap
        coverage = gap.get('coverage', 0)
        if coverage < 5:
            meta_cur.execute('''
                INSERT INTO meta_gaps (paper_number, gap_type, severity, recommendation)
                VALUES (?, ?, ?, ?)
            ''', (pn, 'no_lib', 'medium', f"Expand coverage beyond {coverage} libraries"))
        
        # Check no_d_claims
        meta_cur.execute("SELECT d_claims FROM meta_papers WHERE paper_number = ?", (pn,))
        d_count = meta_cur.fetchone()[0]
        if d_count == 0:
            meta_cur.execute('''
                INSERT INTO meta_gaps (paper_number, gap_type, severity, recommendation)
                VALUES (?, ?, ?, ?)
            ''', (pn, 'no_d_claims', 'high', 'Add data-backed (D) claims to this paper'))
        
        # Check no_cross_ref
        meta_cur.execute("SELECT COUNT(*) FROM meta_cross_refs WHERE from_paper = ? OR to_paper = ?", (pn, pn))
        ref_count = meta_cur.fetchone()[0]
        if ref_count == 0:
            meta_cur.execute('''
                INSERT INTO meta_gaps (paper_number, gap_type, severity, recommendation)
                VALUES (?, ?, ?, ?)
            ''', (pn, 'no_cross_ref', 'medium', 'Add cross-references to/from this paper'))
        
        # Check no_std
        if gap.get('CMPLX_Standards') != 'YES':
            meta_cur.execute('''
                INSERT INTO meta_gaps (paper_number, gap_type, severity, recommendation)
                VALUES (?, ?, ?, ?)
            ''', (pn, 'no_std', 'high', 'Map paper to CMPLX-Standards contract'))
    
    meta_conn.commit()
    
    # Populate cam_hashes
    print(f"Populating cam_hashes with {len(all_hashes)} hashes...")
    seen_hashes = set()
    for h in all_hashes:
        if h['cam_hash'] and h['cam_hash'] not in seen_hashes:
            seen_hashes.add(h['cam_hash'])
            meta_cur.execute('''
                INSERT OR IGNORE INTO cam_hashes (cam_hash, content_type, content_id, source_lib, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (h['cam_hash'], h['content_type'], h['content_id'], h['source_lib'], h['created_at']))
    
    meta_conn.commit()
    
    # Export schema
    print(f"Exporting schema to {META_SCHEMA_PATH}...")
    with open(META_SCHEMA_PATH, 'w', encoding='utf-8') as f:
        for line in meta_conn.iterdump():
            f.write(line + '\n')
    
    meta_conn.close()
    print("Done!")

if __name__ == '__main__':
    main()
