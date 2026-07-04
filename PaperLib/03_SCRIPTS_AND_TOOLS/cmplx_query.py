import sqlite3
import json
import os
import re
import math

PAPERLIB = r"D:\PaperLib"
DB_PATH = os.path.join(PAPERLIB, 'cmplx_unified.db')
SEM_DB_PATH = os.path.join(PAPERLIB, 'cmplx_semantic.db')

def tokenize(text):
    return re.findall(r'\b[a-zA-Z][a-zA-Z0-9_\-]{2,}\b', text.lower())

def compute_tfidf_vector(tokens, vocab):
    tf = {}
    total = len(tokens)
    for t in tokens:
        tf[t] = tf.get(t, 0) + 1
    vec = {}
    for t, freq in tf.items():
        if t in vocab:
            vec[t] = (freq / total) * vocab[t]
    return vec

def cosine_similarity(vec1, vec2):
    dot = 0.0
    norm1 = 0.0
    norm2 = 0.0
    for t, v in vec1.items():
        norm1 += v * v
        if t in vec2:
            dot += v * vec2[t]
    for t, v in vec2.items():
        norm2 += v * v
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (math.sqrt(norm1) * math.sqrt(norm2))

def semantic_search(query, top_k=10):
    """Search papers by semantic similarity using TF-IDF."""
    conn = sqlite3.connect(SEM_DB_PATH)
    vocab = dict(conn.execute('SELECT term, idf FROM vocabulary').fetchall())
    query_tokens = tokenize(query)
    query_vec = compute_tfidf_vector(query_tokens, vocab)
    
    results = []
    for row in conn.execute('SELECT canonical_id, title, vector_json FROM semantic_vectors'):
        paper_vec = json.loads(row[2])
        score = cosine_similarity(query_vec, paper_vec)
        results.append((row[0], row[1], score))
    
    results.sort(key=lambda x: -x[2])
    conn.close()
    return results[:top_k]

def fulltext_search(query, top_k=20):
    """Search papers by FTS5 full-text search."""
    conn = sqlite3.connect(DB_PATH)
    try:
        rows = conn.execute(
            "SELECT p.canonical_id, p.title, p.band FROM papers p "
            "JOIN papers_fts fts ON p.canonical_id = fts.canonical_id "
            "WHERE papers_fts MATCH ? LIMIT ?",
            (query, top_k)
        ).fetchall()
    except:
        rows = conn.execute(
            "SELECT canonical_id, title, band FROM papers "
            "WHERE full_text LIKE ? LIMIT ?",
            (f'%{query}%', top_k)
        ).fetchall()
    conn.close()
    return rows

def get_paper(canonical_id):
    """Get full paper details."""
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute('SELECT * FROM papers WHERE canonical_id = ?', (canonical_id,)).fetchone()
    if not row:
        conn.close()
        return None
    
    refs = conn.execute(
        'SELECT to_canonical_id FROM cross_references WHERE from_canonical_id = ?',
        (canonical_id,)
    ).fetchall()
    backrefs = conn.execute(
        'SELECT from_canonical_id FROM cross_references WHERE to_canonical_id = ?',
        (canonical_id,)
    ).fetchall()
    conn.close()
    
    return {
        'id': row[1],
        'title': row[2],
        'band': row[5],
        'hash': row[6],
        'size': row[7],
        'theorems': row[8],
        'claims_d': row[9],
        'claims_i': row[10],
        'claims_x': row[11],
        'open': row[12],
        'refs': [r[0] for r in refs],
        'backrefs': [r[0] for r in backrefs]
    }

def show_stats():
    """Show suite statistics."""
    conn = sqlite3.connect(DB_PATH)
    total = conn.execute('SELECT COUNT(*) FROM papers').fetchone()[0]
    total_size = conn.execute('SELECT SUM(size_bytes) FROM papers').fetchone()[0]
    total_thm = conn.execute('SELECT SUM(theorem_count) FROM papers').fetchone()[0]
    total_d = conn.execute('SELECT SUM(claim_d_count) FROM papers').fetchone()[0]
    total_i = conn.execute('SELECT SUM(claim_i_count) FROM papers').fetchone()[0]
    total_x = conn.execute('SELECT SUM(claim_x_count) FROM papers').fetchone()[0]
    total_open = conn.execute('SELECT SUM(open_obligation_count) FROM papers').fetchone()[0]
    total_refs = conn.execute('SELECT COUNT(*) FROM cross_references').fetchone()[0]
    
    print(f"{'='*60}")
    print(f"CMPLX Unified Paper Suite")
    print(f"{'='*60}")
    print(f"Papers:           {total}")
    print(f"Total Size:       {total_size/1024/1024:.2f} MB")
    print(f"Theorems:         {total_thm}")
    print(f"Claims:           D={total_d} | I={total_i} | X={total_x}")
    print(f"Open Obligations: {total_open}")
    print(f"Cross-References: {total_refs}")
    print(f"{'='*60}")
    
    print(f"\nTop 5 Hub Papers:")
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

def search(query, top_k=10, use_semantic=True, use_fulltext=True):
    """Combined search: semantic + fulltext."""
    results = []
    seen = set()
    
    if use_semantic:
        sem_results = semantic_search(query, top_k=top_k)
        for cid, title, score in sem_results:
            if cid not in seen:
                seen.add(cid)
                results.append((cid, title, score, 'semantic'))
    
    if use_fulltext:
        ft_results = fulltext_search(query, top_k=top_k)
        for row in ft_results:
            cid = row[0]
            if cid not in seen:
                seen.add(cid)
                results.append((cid, row[1], 0.5, 'fulltext'))
    
    results.sort(key=lambda x: -x[2])
    return results[:top_k]

def main():
    import sys
    if len(sys.argv) < 2:
        print("""CMPLX Unified Paper Suite — Unified Query Interface

Usage:
    python cmplx_query.py search <query>         # Combined semantic + fulltext search
    python cmplx_query.py semantic <query>      # Semantic search only
    python cmplx_query.py fulltext <query>      # Fulltext search only
    python cmplx_query.py get <Paper N>         # Get paper details
    python cmplx_query.py refs <Paper N>        # Show cross-references
    python cmplx_query.py stats                 # Show suite statistics
    python cmplx_query.py verify <Paper N>      # Verify content hash
""")
        return
    
    cmd = sys.argv[1]
    if cmd == 'search' and len(sys.argv) > 2:
        results = search(' '.join(sys.argv[2:]))
        print(f"Results for: {' '.join(sys.argv[2:])}\n")
        for rank, (cid, title, score, method) in enumerate(results, 1):
            print(f"  {rank}. {cid}: {title[:60]}... ({method}, score: {score:.4f})")
    elif cmd == 'semantic' and len(sys.argv) > 2:
        results = semantic_search(' '.join(sys.argv[2:]))
        print(f"Semantic results for: {' '.join(sys.argv[2:])}\n")
        for rank, (cid, title, score) in enumerate(results, 1):
            print(f"  {rank}. {cid}: {title[:60]}... (score: {score:.4f})")
    elif cmd == 'fulltext' and len(sys.argv) > 2:
        results = fulltext_search(' '.join(sys.argv[2:]))
        print(f"Fulltext results for: {' '.join(sys.argv[2:])}\n")
        for rank, (cid, title, band) in enumerate(results, 1):
            print(f"  {rank}. {cid}: {title[:60]}... (band: {band})")
    elif cmd == 'get' and len(sys.argv) > 2:
        paper = get_paper(sys.argv[2])
        if paper:
            print(f"{'='*60}")
            print(f"ID:         {paper['id']}")
            print(f"Title:      {paper['title']}")
            print(f"Band:       {paper['band']}")
            print(f"Hash:       {paper['hash']}")
            print(f"Size:       {paper['size']} bytes")
            print(f"Theorems:   {paper['theorems']}")
            print(f"Claims:     D={paper['claims_d']} | I={paper['claims_i']} | X={paper['claims_x']}")
            print(f"Open:       {paper['open']}")
            print(f"Refs:       {len(paper['refs'])}")
            print(f"Backrefs:   {len(paper['backrefs'])}")
            print(f"{'='*60}")
        else:
            print(f"Paper {sys.argv[2]} not found")
    elif cmd == 'refs' and len(sys.argv) > 2:
        paper = get_paper(sys.argv[2])
        if paper:
            print(f"{paper['id']} Cross-Reference Graph:")
            print(f"  Outgoing: {len(paper['refs'])}")
            print(f"  Incoming: {len(paper['backrefs'])}")
            if paper['refs']:
                print(f"  -> {', '.join(paper['refs'][:20])}")
            if paper['backrefs']:
                print(f"  <- {', '.join(paper['backrefs'][:20])}")
        else:
            print(f"Paper {sys.argv[2]} not found")
    elif cmd == 'verify' and len(sys.argv) > 2:
        import hashlib
        paper = get_paper(sys.argv[2])
        if paper:
            path = os.path.join(PAPERLIB, paper['id'].replace(' ', '-').lower() + '__*.md')
            import glob
            files = glob.glob(path)
            if files:
                with open(files[0], 'rb') as f:
                    h = hashlib.sha256(f.read()).hexdigest()
                print(f"Stored hash:   {paper['hash']}")
                print(f"Computed hash: {h}")
                print(f"Match: {'YES' if h == paper['hash'] else 'NO'}")
            else:
                print(f"File not found for {paper['id']}")
        else:
            print(f"Paper {sys.argv[2]} not found")
    elif cmd == 'stats':
        show_stats()
    else:
        print(f"Unknown command: {cmd}")

if __name__ == '__main__':
    main()
