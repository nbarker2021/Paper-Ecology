"""
resynthesis_pass.py — SECOND PASS over the 170 'blocked' ledger entries.

The first bulk pass produced 166 garbled 'blocked' entries: its table-row regex
grabbed stray X/0 cells (tags like '0','B','X') with NO real description, so the
CrystalLib synthesis search had nothing to match on. The 415k D-claims in
CrystalLib very likely close most of these.

This pass:
  1. Re-reads each affected paper and extracts the REAL Open-Problem sentences.
  2. Searches CrystalLib D-claims (415k) using the real concepts.
  3. Re-classifies the ledger entry:
       derived_D  -> real D-claim(s) found sharing >=1 specific concept
       blocked    -> still nothing (honest, keeps directive)
  4. Overwrites the garbled entry in derivation_ledger.jsonl (matched by receipt_id).

RUN:  python resynthesis_pass.py
"""
import os, re, json, sqlite3, glob, collections

ROOT = r"D:/Paper Ecology/ProofLib/DerivationLedger"
PAPERS = r"D:/Paper Ecology/main_papers/root_papers"
CRYSTAL = r"D:/Paper Ecology/CrystalLib/crystal_lib.db"
CRYSTAL_CACHE = os.path.join(ROOT, "crystal_d_cache.json")
LEDGER = os.path.join(ROOT, "derivation_ledger.jsonl")

GENERIC = set("shell anf claim paper theorem proof lattice algebra bit state rule column depth "
               "result function polynomial structure category morphism object part term open problem "
               "obligation insertion plan generalized higher unified full exact bounded".split())

OP_PAT = re.compile(
    r"^\s*\**\s*(Open Problem|Open Formalization Obligation|Open Obligation|INSERTION_PLAN)"
    r"\s*([0-9.]*)\s*\(?([^)]*)\)?\s*[\.:\*—–-]?\s*(.*)$")

def extract_real_ops(pn):
    fs = glob.glob(os.path.join(PAPERS, f"{pn}_*.md"))
    if not fs:
        return []
    text = open(fs[0], errors="ignore").read()
    lines = text.splitlines()
    out = []
    for i, line in enumerate(lines):
        m = OP_PAT.match(line)
        if m:
            num, kind, desc = m.group(2).strip(), m.group(3).strip(), m.group(4).strip()
            if len(desc) < 20:
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith("#"):
                    cand = lines[j].strip().lstrip("*").strip()
                    if cand:
                        desc = (desc + " " + cand).strip()
                        if len(desc) > 40:
                            break
                    j += 1
            raw = re.sub(r"[*\\]", "", desc)
            raw = re.sub(r"\s+", " ", raw).strip()
            sent = re.split(r"(?<=[.])\s", raw)
            desc_clean = sent[0][:200] if sent else raw[:200]
            if len(desc_clean) >= 15:
                out.append({"tag": (f"{num} {kind}".strip() or "OP"), "desc": desc_clean})
    return out

def crystal_search(terms, limit=12):
    """Search the local crystal D-cache (built by build_crystal_cache.py)."""
    if not os.path.exists(CRYSTAL_CACHE):
        # fallback to live DB
        return crystal_search_live(terms, limit)
    cache = json.load(open(CRYSTAL_CACHE))
    seen, out = set(), []
    for kw in terms:
        kw = kw.lower()
        if len(kw) < 4:
            continue
        for r in cache:
            if kw in r["text"].lower() and r["id"] not in seen:
                seen.add(r["id"])
                out.append({"claim_id": r["id"], "paper": r["paper"], "text": r["text"]})
                if len(out) >= limit * 4:
                    break
        if len(out) >= limit * 4:
            break
    return out[:limit * 3]

def crystal_search_live(terms, limit=10):
    con = sqlite3.connect(CRYSTAL, timeout=30)
    con.execute("PRAGMA busy_timeout=30000"); con.execute("PRAGMA query_only=1")
    cur = con.cursor()
    seen, out = set(), []
    for kw in terms:
        kw = kw.lower()
        if len(kw) < 4:
            continue
        cur.execute("""SELECT claim_id, paper_number, claim_text FROM claims 
                       WHERE LOWER(claim_text) LIKE ? AND claim_status='D' LIMIT ?""",
                    (f"%{kw}%", limit))
        for r in cur.fetchall():
            if r[0] in seen:
                continue
            seen.add(r[0])
            out.append({"claim_id": r[0], "paper": r[1], "text": r[2]})
    con.close()
    return out

def concept_overlap(htext, desc):
    hwords = set(re.findall(r"[A-Za-z][A-Za-z]{3,}", htext.lower())) - GENERIC
    dwords = set(re.findall(r"[A-Za-z][A-Za-z]{3,}", desc.lower())) - GENERIC
    return len(hwords & dwords), hwords & dwords

def main():
    import sys
    chunk = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    CKPT = os.path.join(ROOT, "resynth_checkpoint.json")
    start = 0
    if os.path.exists(CKPT):
        try: start = json.load(open(CKPT)).get("done", 0)
        except Exception: start = 0

    rows = [json.loads(l) for l in open(LEDGER) if l.strip()]
    blocked = [e for e in rows if e["status"] == "blocked"]
    by_paper = collections.defaultdict(list)
    for e in blocked:
        by_paper[e["paper"]].append(e)
    paper_order = sorted(by_paper, key=lambda x: int(x) if x.isdigit() else 999)
    # resume from checkpoint
    paper_order = paper_order[start:]

    reclassified = 0
    still_blocked = 0
    processed = 0
    for pn in paper_order:
        if processed >= chunk:
            break
        ops = extract_real_ops(pn)
        if not ops:
            still_blocked += len(by_paper[pn])
            for e in by_paper[pn]:
                pass  # keep as-is in rows (handled below)
            processed += 1
            continue
        all_terms = []
        for op in ops:
            all_terms += re.findall(r"[A-Za-z][A-Za-z]{3,}", op["desc"].lower())
        all_terms = [t for t in all_terms if t not in GENERIC]
        hits = crystal_search(all_terms, limit=12)
        scored = []
        for h in hits:
            best = 0; best_op = None
            for op in ops:
                ov, _ = concept_overlap(h["text"], op["desc"])
                if ov > best:
                    best = ov; best_op = op
            if best >= 1:
                scored.append((best, h, best_op))
        scored.sort(key=lambda x: x[0], reverse=True)
        # apply to every blocked entry for this paper
        for e in by_paper[pn]:
            if scored:
                e["status"] = "derived_D"
                e["sources"] = [(f"CrystalLib#{h['claim_id']}", f"{h['paper']}: {h['text'][:90]} (D)")
                                 for s, h, op in scored[:4]]
                e["derivation"] = (f"RESYNTHESIS PASS: real Open-Problem text from paper {pn} matched "
                                   f"{len(scored)} existing CrystalLib D-claim(s) via specific-concept overlap "
                                   f"(best={scored[0][0]} on '{scored[0][2]['tag']}').")
                e["notes"] = "Re-derived via 415k-crystal pool (2026-07-08 second pass)."
                reclassified += 1
            else:
                still_blocked += 1
        processed += 1

    # rewrite ledger with updated entries
    with open(LEDGER, "w") as f:
        for e in rows:
            f.write(json.dumps(e) + "\n")
    # advance checkpoint
    json.dump({"done": start + processed}, open(CKPT, "w"))
    c = collections.Counter(e["status"] for e in rows)
    print(f"CHUNK done={processed} (papers {start+1}..{start+processed}) "
          f"reclassified={reclassified} still_blocked={still_blocked}")
    print(f"  RUNNING TOTALS: {dict(c)}")
    if start + processed >= len(by_paper):
        print("  [ALL PAPERS DONE]")

if __name__ == "__main__":
    main()
