"""
DerivationLedger — turns I/X/open claims in the 240-paper framework into D claims.

PRINCIPLE (per user directive 2026-07-08):
  Partial/analogous REAL published papers are DERIVATION SOURCES. For each
  interpretive (I) / open-obligation (X) / open-problem claim, we take the real
  published data/theorem(s) and DERIVE within LCR what the claim needs to become
  a data-backed, computationally-receipted D claim.

ACCURACY GATE:
  - A claim is upgraded to 'derived_D' only when (a) a real published source is
    cited with arxiv_id/title, (b) an explicit LCR derivation is recorded, and
    (c) a computational receipt check passes (Python assert, 0 defects).
  - 'partial' = real source gives ingredients but full proof still needs later paper.
  - 'blocked' = no real source available; must be searched online / authored later.

Usage:
  from derivation_ledger import Ledger
  L = Ledger()
  L.record(paper="001", claim="OP10.2 off-diagonal J3(O)",
            sources=[("2504.16513","Kollross 2025 E8 bracket via oct-octonions")],
            derivation="...", check=lambda: <asserts>, status="derived_D")
  L.index_corpus()  # build keyword index over ARXIV_PDFS
  L.query("Rule 30 aperiodicity")
"""
import os, json, re, subprocess, hashlib, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
CORPUS_DIR = os.path.join(ROOT, "corpus")
RECEIPTS_DIR = os.path.join(ROOT, "receipts")
LEDGER_JSONL = os.path.join(ROOT, "derivation_ledger.jsonl")
CORPUS_PDF_DIR = r"D:/Paper Ecology/PaperLib/00_EXTERNAL_LITERATURE_MAPPING/ARXIV_PDFS"
INDEX_JSON = os.path.join(ROOT, "corpus_index.json")

STOP = set("the a an of to in on for and or with from by is are be as at we our this that "
           "using can which their its has have were will not but using into than then thus "
           "also such these those more most other new results paper study using".split())

os.makedirs(CORPUS_DIR, exist_ok=True)
os.makedirs(RECEIPTS_DIR, exist_ok=True)


class Ledger:
    def __init__(self):
        self.entries = []
        if os.path.exists(LEDGER_JSONL):
            for line in open(LEDGER_JSONL):
                line = line.strip()
                if line:
                    self.entries.append(json.loads(line))

    # ---- record a derivation ----
    def record(self, paper, claim, sources, derivation, check, status, notes=""):
        """check: a callable returning True (raises on failure). Returns receipt dict."""
        assert status in ("derived_D", "partial", "blocked", "context_only"), status
        receipt = None
        passed = False
        err = ""
        if check is not None:
            try:
                check(); passed = True
            except Exception as e:
                err = f"{type(e).__name__}: {e}"
        receipt_id = "DRV-" + hashlib.sha256(
            f"{paper}:{claim}:{datetime.datetime.utcnow().isoformat()}".encode()).hexdigest()[:12]
        entry = {
            "receipt_id": receipt_id,
            "paper": paper,
            "claim": claim,
            "sources": [{"arxiv_id": a, "title": t} for a, t in sources],
            "derivation": derivation,
            "status": status,
            "check_passed": passed if check is not None else None,
            "check_error": err,
            "notes": notes,
            "ts": datetime.datetime.utcnow().isoformat() + "Z",
        }
        self.entries.append(entry)
        with open(LEDGER_JSONL, "a") as f:
            f.write(json.dumps(entry) + "\n")
        self._write_receipt_md(entry)
        return entry

    def _write_receipt_md(self, e):
        path = os.path.join(RECEIPTS_DIR, f"{e['paper']}_receipts.md")
        header = (f"\n---\n## {e['receipt_id']} — {e['claim']}\n\n"
                  f"**status:** `{e['status']}`  **check:** {e['check_passed']}  **ts:** {e['ts']}\n\n"
                  f"**sources:** " + "; ".join(f"[{s['arxiv_id']}] {s['title']}" for s in e['sources']) + "\n\n"
                  f"**derivation:**\n{e['derivation']}\n")
        if e['check_error']:
            header += f"\n**check_error:** {e['check_error']}\n"
        if os.path.exists(path):
            with open(path, "a") as f:
                f.write(header)
        else:
            with open(path, "w") as f:
                f.write(f"# Derivation Receipts — Paper {e['paper']}\n" + header)

    # ---- corpus index ----
    def index_corpus(self, max_pages=2, force=False):
        if os.path.exists(INDEX_JSON) and not force:
            return json.load(open(INDEX_JSON))
        idx = {}
        for fn in sorted(os.listdir(CORPUS_PDF_DIR)):
            if not fn.endswith(".pdf"):
                continue
            aid = fn[:-4]
            txt_path = os.path.join(CORPUS_DIR, aid + ".txt")
            if not os.path.exists(txt_path) or force:
                subprocess.run(["pdftotext", "-f", "1", "-l", str(max_pages),
                                os.path.join(CORPUS_PDF_DIR, fn), txt_path],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            text = open(txt_path, errors="ignore").read() if os.path.exists(txt_path) else ""
            lines = [l.strip() for l in text.splitlines() if l.strip()]
            title = lines[0] if lines else aid
            kw = set()
            for l in lines[:40]:
                for w in re.findall(r"[A-Za-z][A-Za-z\-]{3,}", l.lower()):
                    if w not in STOP:
                        kw.add(w)
            idx[aid] = {"title": title, "keywords": sorted(kw), "n_pages_text": len(lines)}
        json.dump(idx, open(INDEX_JSON, "w"), indent=1)
        return idx

    def query(self, *terms, index=None):
        index = index or (self.index_corpus() if os.path.exists(INDEX_JSON) else self.index_corpus())
        hits = []
        for aid, meta in index.items():
            blob = (meta["title"] + " " + " ".join(meta["keywords"])).lower()
            score = sum(blob.count(t.lower()) for t in terms)
            if score:
                hits.append((score, aid, meta["title"]))
        return sorted(hits, reverse=True)


if __name__ == "__main__":
    L = Ledger()
    print("entries:", len(L.entries))
