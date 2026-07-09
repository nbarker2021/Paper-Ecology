"""
summary.py — aggregate the DerivationLedger into DERIVATION_SUMMARY.md (the baseline view).

Groups by paper and status:
  derived_D  : claim resolved to data-backed via real source (in-folder PDF or CrystalLib D-claim)
  partial    : candidate match, needs manual LCR derivation write-up
  blocked    : no real source found -> carries an ONLINE SEARCH DIRECTIVE (never faked)
Also prints a totals block + the full gap-list (blocked) for your online-search pass.
"""
import os, json, collections

ROOT = r"D:/Paper Ecology/ProofLib/DerivationLedger"
LEDGER = os.path.join(ROOT, "derivation_ledger.jsonl")
OUT = os.path.join(ROOT, "DERIVATION_SUMMARY.md")

def load():
    rows = []
    if os.path.exists(LEDGER):
        for ln in open(LEDGER):
            ln = ln.strip()
            if ln:
                rows.append(json.loads(ln))
    return rows

def main():
    rows = load()
    by_paper = collections.defaultdict(list)
    for e in rows:
        by_paper[e["paper"]].append(e)
    status_count = collections.Counter(e["status"] for e in rows)
    total = len(rows)

    L = []
    L.append("# DerivationLedger — Baseline Summary\n")
    L.append(f"**Generated:** {__import__('datetime').datetime.utcnow().isoformat()}Z  ")
    L.append(f"**Total claims processed:** {total}  ")
    L.append(f"**derived_D:** {status_count.get('derived_D',0)}  "
             f"**partial:** {status_count.get('partial',0)}  "
             f"**blocked:** {status_count.get('blocked',0)}  "
             f"**other:** {status_count.get('error',0)+status_count.get('ambiguous',0)}\n")
    L.append("---\n")

    # per-paper table
    L.append("## Per-paper status\n")
    L.append("| Paper | Claims | derived_D | partial | blocked |")
    L.append("|-------|--------|-----------|---------|---------|")
    for pn in sorted(by_paper, key=lambda x: int(x) if x.isdigit() else 999):
        es = by_paper[pn]
        c = collections.Counter(e["status"] for e in es)
        L.append(f"| {pn} | {len(es)} | {c.get('derived_D',0)} | {c.get('partial',0)} | {c.get('blocked',0)} |")
    L.append("\n---\n")

    # gap list (blocked) — the online-search pass
    L.append("## Gap list (blocked — need ONLINE published proof)\n")
    blocked = [e for e in rows if e["status"] == "blocked"]
    if not blocked:
        L.append("_None blocked — all claims resolved or partial._\n")
    else:
        for e in blocked:
            L.append(f"- **{e['paper']}** `{e['receipt_id']}`: {e['claim'][:140]}")
            if e.get("notes"):
                L.append(f"    - directive: {e['notes'][:200]}")
    L.append("\n---\n")

    # partial list (need manual LCR derivation write-up)
    L.append("## Partial (candidate matches — need manual LCR derivation)\n")
    partials = [e for e in rows if e["status"] == "partial"]
    if not partials:
        L.append("_None partial._\n")
    else:
        for e in partials:
            L.append(f"- **{e['paper']}** `{e['receipt_id']}`: {e['claim'][:140]}")
            for s in e.get("sources", [])[:2]:
                L.append(f"    - src: {s}")
    L.append("")

    open(OUT, "w").write("\n".join(L))
    print(f"Wrote {OUT}")
    print(f"  total={total} derived_D={status_count.get('derived_D',0)} "
          f"partial={status_count.get('partial',0)} blocked={status_count.get('blocked',0)}")
    print(f"  papers covered: {len(by_paper)}")

if __name__ == "__main__":
    main()
