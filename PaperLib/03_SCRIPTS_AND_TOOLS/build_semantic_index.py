import os
import re
import math
import sqlite3
import json
import hashlib
from pathlib import Path

PAPERLIB = r"D:\PaperLib"

def tokenize(text):
    """Simple tokenization - lowercase, alphanumeric tokens only."""
    return re.findall(r'\b[a-zA-Z][a-zA-Z0-9_\-]{2,}\b', text.lower())

def compute_tf(tokens):
    """Compute term frequency."""
    tf = {}
    total = len(tokens)
    for t in tokens:
        tf[t] = tf.get(t, 0) + 1
    for t in tf:
        tf[t] = tf[t] / total
    return tf

def compute_idf(documents):
    """Compute inverse document frequency."""
    N = len(documents)
    df = {}
    for doc_tokens in documents:
        seen = set(doc_tokens)
        for t in seen:
            df[t] = df.get(t, 0) + 1
    
    idf = {}
    for t, freq in df.items():
        idf[t] = math.log(N / freq)
    return idf

def compute_tfidf_vector(tokens, idf):
    """Compute TF-IDF vector for a document."""
    tf = compute_tf(tokens)
    vec = {}
    for t, freq in tf.items():
        if t in idf:
            vec[t] = freq * idf[t]
    return vec

def cosine_similarity(vec1, vec2):
    """Compute cosine similarity between two sparse vectors."""
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

def build_semantic_index():
    """Build TF-IDF semantic index for all papers."""
    print("=== Building Semantic Search Index ===")
    
    # Load all papers
    papers = {}
    for f in os.listdir(PAPERLIB):
        if not f.endswith('.md') or not f.startswith('paper-'):
            continue
        m = re.match(r'paper-(\d{2,3})__', f)
        if not m:
            continue
        num = int(m.group(1))
        path = os.path.join(PAPERLIB, f)
        with open(path, 'r', encoding='utf-8') as fh:
            content = fh.read()
        papers[num] = {
            'filename': f,
            'title': content.split('\n')[0].strip('# '),
            'content': content
        }
    
    print(f"Loaded {len(papers)} papers")
    
    # Tokenize
    docs = {}
    for num, p in papers.items():
        # Use abstract + first 2000 chars for semantic indexing
        text = p['content'][:4000]
        docs[num] = tokenize(text)
    
    # Compute IDF
    idf = compute_idf(docs.values())
    
    # Compute TF-IDF vectors
    vectors = {}
    for num, tokens in docs.items():
        vectors[num] = compute_tfidf_vector(tokens, idf)
    
    # Store in SQLite
    db_path = os.path.join(PAPERLIB, 'cmplx_semantic.db')
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    conn.execute('PRAGMA journal_mode=WAL')
    
    conn.execute('''
        CREATE TABLE semantic_vectors (
            id INTEGER PRIMARY KEY,
            canonical_id TEXT UNIQUE,
            title TEXT,
            filename TEXT,
            vector_json TEXT
        )
    ''')
    
    conn.execute('''
        CREATE TABLE vocabulary (
            term TEXT PRIMARY KEY,
            idf REAL
        )
    ''')
    
    for num, vec in vectors.items():
        canonical_id = f"Paper {num}"
        conn.execute(
            'INSERT INTO semantic_vectors (canonical_id, title, filename, vector_json) VALUES (?, ?, ?, ?)',
            (canonical_id, papers[num]['title'], papers[num]['filename'], json.dumps(vec))
        )
    
    for term, idf_val in idf.items():
        conn.execute('INSERT INTO vocabulary (term, idf) VALUES (?, ?)', (term, idf_val))
    
    conn.commit()
    conn.close()
    
    print(f"Semantic index built: {db_path}")
    print(f"Vocabulary size: {len(idf)}")
    
    return db_path, vectors, idf

def semantic_search(query, db_path, top_k=10):
    """Search papers by semantic similarity."""
    conn = sqlite3.connect(db_path)
    
    # Load vocabulary
    vocab = dict(conn.execute('SELECT term, idf FROM vocabulary').fetchall())
    
    # Query vector
    query_tokens = tokenize(query)
    query_vec = compute_tfidf_vector(query_tokens, vocab)
    
    # Score all papers
    results = []
    for row in conn.execute('SELECT canonical_id, title, vector_json FROM semantic_vectors'):
        paper_vec = json.loads(row[2])
        score = cosine_similarity(query_vec, paper_vec)
        results.append((row[0], row[1], score))
    
    results.sort(key=lambda x: -x[2])
    conn.close()
    return results[:top_k]

def main():
    db_path, vectors, idf = build_semantic_index()
    
    # Test queries
    test_queries = [
        "Riemann hypothesis critical line",
        "Yang-Mills mass gap lattice QCD",
        "Rule 30 non-periodicity Wolfram",
        "Monster VOA moonshine",
        "Navier-Stokes smoothness boundary repair",
        "Hodge conjecture algebraic cycles",
        "P vs NP complexity",
        "black hole entropy Bekenstein",
        "cosmic microwave background CMB",
        "Higgs mechanism vacuum stability"
    ]
    
    print("\n=== Test Semantic Searches ===")
    for query in test_queries:
        results = semantic_search(query, db_path, top_k=5)
        print(f"\nQuery: '{query}'")
        for rank, (cid, title, score) in enumerate(results, 1):
            print(f"  {rank}. {cid}: {title[:50]}... (score: {score:.4f})")
    
    return {"status": "complete", "db_path": db_path, "vocab_size": len(idf)}

if __name__ == '__main__':
    main()
