#!/usr/bin/env python3
"""CMPLX Unified Paper Suite — Query Tool

Usage:
    python query_papers.py search <query>     # Full-text search
    python query_papers.py get <Paper N>       # Get paper details
    python query_papers.py refs <Paper N>     # Show cross-references
    python query_papers.py hash <Paper N>      # Show content hash
    python query_papers.py stats               # Show suite statistics
"""
import sqlite3
import sys
import os

PAPERLIB = r"D:\PaperLib"
DB_PATH = os.path.join(PAPERLIB, "cmplx_unified.db")

def get_conn():
    return sqlite3.connect(DB_PATH)

def has_fts5(conn):
    try:
        conn.execute("SELECT 1 FROM papers_fts LIMIT 1")
        return True
    except:
        return False

def search(query):
    conn = get_conn()
    fts = has_fts5(conn)
    
    if fts:
        rows = conn.execute(
            "SELECT p.canonical_id, p.title, p.band "
            "FROM papers p JOIN papers_fts fts ON p.canonical_id = fts.canonical_id "
            "WHERE papers_fts MATCH ? LIMIT 20",
            (query,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT canonical_id, title, band FROM papers "
            "WHERE full_text LIKE ? LIMIT 20",
            (f'%{query}%',)
        ).fetchall()
    
    if not rows:
        print(f"No results for: {query}")
    else:
        print(f"Results for: {query}\n")
        for row in rows:
            print(f"  {row[0]}: {row[1]} ({row[2]})")
    conn.close()

def get_paper(paper_id):
    conn = get_conn()
    row = conn.execute('SELECT * FROM papers WHERE canonical_id = ?', (paper_id,)).fetchone()
    if not row:
        print(f"Paper {paper_id} not found")
        return
    
    print(f"{'='*60}")
    print(f"ID:         {row[1]}")
    print(f"Title:      {row[2]}")
    print(f"Band:       {row[5]}")
    print(f"Content Hash (SHA-256):")
    print(f"            {row[6]}")
    print(f"Size:       {row[7]} bytes")
    print(f"Theorems:   {row[8]}")
    print(f"Claims:     D={row[9]} | I={row[10]} | X={row[11]}")
    print(f"Open Obl:   {row[12]}")
    print(f"{'='*60}")
    
    refs = conn.execute(
        'SELECT to_canonical_id FROM cross_references WHERE from_canonical_id = ?',
        (paper_id,)
    ).fetchall()
    if refs:
        print(f"\nReferences ({len(refs)}):")
        for r in refs:
            print(f"  → {r[0]}")
    
    backrefs = conn.execute(
        'SELECT from_canonical_id FROM cross_references WHERE to_canonical_id = ?',
        (paper_id,)
    ).fetchall()
    if backrefs:
        print(f"\nReferenced by ({len(backrefs)}):")
        for r in backrefs:
            print(f"  ← {r[0]}")
    
    conn.close()

def show_refs(paper_id):
    conn = get_conn()
    refs = conn.execute(
        'SELECT to_canonical_id FROM cross_references WHERE from_canonical_id = ?',
        (paper_id,)
    ).fetchall()
    backrefs = conn.execute(
        'SELECT from_canonical_id FROM cross_references WHERE to_canonical_id = ?',
        (paper_id,)
    ).fetchall()
    
    print(f"{paper_id} Cross-Reference Graph:")
    print(f"  Outgoing: {len(refs)}")
    print(f"  Incoming: {len(backrefs)}")
    
    if refs:
        print(f"\n  → {', '.join(r[0] for r in refs)}")
    if backrefs:
        print(f"\n  ← {', '.join(r[0] for r in backrefs)}")
    conn.close()

def show_hash(paper_id):
    conn = get_conn()
    row = conn.execute(
        'SELECT content_hash, filename FROM papers WHERE canonical_id = ?',
        (paper_id,)
    ).fetchone()
    if not row:
        print(f"Paper {paper_id} not found")
        return
    
    print(f"{paper_id}:")
    print(f"  SHA-256: {row[0]}")
    print(f"  File: {row[1]}")
    print(f"\nVerify with:")
    print(f"  python -c \"import hashlib; print(hashlib.sha256(open('{row[1]}','rb').read()).hexdigest())\"")
    conn.close()

def show_stats():
    conn = get_conn()
    total = conn.execute('SELECT COUNT(*) FROM papers').fetchone()[0]
    total_size = conn.execute('SELECT SUM(size_bytes) FROM papers').fetchone()[0]
    total_thm = conn.execute('SELECT SUM(theorem_count) FROM papers').fetchone()[0]
    total_d = conn.execute('SELECT SUM(claim_d_count) FROM papers').fetchone()[0]
    total_i = conn.execute('SELECT SUM(claim_i_count) FROM papers').fetchone()[0]
    total_x = conn.execute('SELECT SUM(claim_x_count) FROM papers').fetchone()[0]
    total_open = conn.execute('SELECT SUM(open_obligation_count) FROM papers').fetchone()[0]
    total_refs = conn.execute('SELECT COUNT(*) FROM cross_references').fetchone()[0]
    
    print(f"{'='*60}")
    print(f"CMPLX Unified Paper Suite — Statistics")
    print(f"{'='*60}")
    print(f"Papers:           {total}")
    print(f"Total Size:       {total_size/1024/1024:.2f} MB")
    print(f"Theorems:         {total_thm}")
    print(f"Claims:           D={total_d} | I={total_i} | X={total_x}")
    print(f"Open Obligations: {total_open}")
    print(f"Cross-References: {total_refs}")
    print(f"{'='*60}")
    
    print(f"\nTop 5 Hub Papers (most references):")
    hubs = conn.execute(
        'SELECT from_canonical_id, COUNT(*) as c FROM cross_references '
        'GROUP BY from_canonical_id ORDER BY c DESC LIMIT 5'
    ).fetchall()
    for hub in hubs:
        print(f"  {hub[0]}: {hub[1]} references")
    
    print(f"\nTop 5 Referenced Papers:")
    refs = conn.execute(
        'SELECT to_canonical_id, COUNT(*) as c FROM cross_references '
        'GROUP BY to_canonical_id ORDER BY c DESC LIMIT 5'
    ).fetchall()
    for ref in refs:
        print(f"  {ref[0]}: {ref[1]} incoming references")
    
    conn.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == 'search' and len(sys.argv) > 2:
        search(sys.argv[2])
    elif cmd == 'get' and len(sys.argv) > 2:
        get_paper(sys.argv[2])
    elif cmd == 'refs' and len(sys.argv) > 2:
        show_refs(sys.argv[2])
    elif cmd == 'hash' and len(sys.argv) > 2:
        show_hash(sys.argv[2])
    elif cmd == 'stats':
        show_stats()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
