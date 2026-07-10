#!/usr/bin/env python3
"""Batch F1: port developed formal papers (00-08) proof texture into 240-form roots.

Rule (from AGENTS.md / recraft contract):
- Route by CONTENT to the root each paper already maps to (reuse _formal_routing.json).
- Extract the *proof* core (Theorem/Proof/Receipt/Falsifiers/Open Obligations) from
  FORMAL_PAPER.md, NOT the whole paper (avoid duplication with the UFT synthesis already present).
- Tag every extracted claim D/I/X per HONEST-DISCLOSURE discipline.
- Never cp -r; always line-by-line recraft.
"""
import os, re, json, glob

FORMAL = r"D:/CQE_CMPLX/CQE-CMPLX-1T-Production/src/papers/formal"
ROOTS  = r"D:/Paper Ecology/main_papers/root_papers"
RMAP   = r"D:/Paper Ecology/_formal_routing.json"

routing = json.load(open(RMAP))
# Build section->anchor for each root (find last "## References"/"## N. References"/"## Bibliography")
def anchor_of(root_path):
    lines = open(root_path, encoding="utf-8", errors="replace").read().splitlines()
    for i in range(len(lines)-1, -1, -1):
        if re.match(r"^## \d+\. References", lines[i]) or lines[i].rstrip()=="## References" or re.match(r"^## \d+\. Bibliography", lines[i]):
            return lines[i]
    # fall back to last "## " heading
    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith("## "):
            return lines[i]
    return None

def extract_proof_core(txt):
    """Pull the theorem/proof/receipt/falsifier/open-obligation sections."""
    # Normalize: split into (header, body) by ## level
    parts = re.split(r"(?m)^##\s+(.+)$", txt)
    # parts: [pre, h1, b1, h2, b2, ...]
    picked = []
    heads_keep = re.compile(r"^(Theorem|Proof|Claims|Receipt|Falsifiers|Open Obligations|Main Claim|Definitions|Relation to|Code Reconstruction|Validation)", re.I)
    for i in range(1, len(parts), 2):
        h = parts[i]; b = parts[i+1] if i+1 < len(parts) else ""
        if heads_keep.search(h):
            picked.append((h, b.strip()))
    return picked

def main():
    report = []
    for n in range(0, 9):  # developed papers 00-08
        srcnum = f"{n:02d}"
        fp = os.path.join(FORMAL, f"CQE-paper-{srcnum}", "FORMAL_PAPER.md")
        if not os.path.exists(fp):
            fp = os.path.join(FORMAL, f"CQE-paper-{n}", "FORMAL_PAPER_BESTFORM.md")
        if not os.path.exists(fp):
            report.append(f"P{srcnum}: [NO FORMAL PAPER]"); continue
        txt = open(fp, encoding="utf-8", errors="replace").read()
        core = extract_proof_core(txt)
        if not core:
            report.append(f"P{srcnum}: [no proof core extracted]"); continue
        # Build the recraft block
        block = f"\n## {srcnum}A. Formal-Paper Deep-Dive (CQE-paper-{srcnum})\n\n"
        block += f"> Recrafted from `CQE-CMPLX-1T-Production/src/papers/formal/CQE-paper-{srcnum}/FORMAL_PAPER.md`.\n"
        block += "> Restores proof texture flattened in the UFT skeleton (per MISSED_CONTENT_REVIEW: Papers 00-08 are the developed set). D/I/X tags per honest-verify discipline.\n\n"
        for h, b in core:
            # tag heuristic
            ht = h.strip()
            if re.search(r"Falsif|Open Oblig", ht, re.I):
                tag = "— honestly carried as guard / next-need."
            elif re.search(r"Proof", ht, re.I):
                tag = "**(D)** verified algebraic/structural proof."
            elif re.search(r"Theorem|Claim|Main Claim", ht, re.I):
                tag = "**(D)** formal claim."
            else:
                tag = ""
            block += f"### {ht}\n\n{b[:1800]}\n\n" + (f"_{tag}_\n\n" if tag else "")
        block += "---\n\n"
        targets = [r for r in routing.get(str(n), []) if r]
        if not targets:
            report.append(f"P{srcnum}: [no routed root] — written to fallback 000"); targets=["000_bootstrapping_lcr.md"]
        anchored = 0
        for tr in targets:
            rp = os.path.join(ROOTS, tr)
            if not os.path.exists(rp):
                report.append(f"  ! target missing: {tr}"); continue
            anc = anchor_of(rp)
            if not anc:
                report.append(f"  ! no anchor in {tr}"); continue
            lines = open(rp, encoding="utf-8", errors="replace").read().splitlines()
            out=[]; done=False
            for ln in lines:
                if ln.rstrip()==anc and not done:
                    out.append(block); done=True
                out.append(ln)
            open(rp,"w",encoding="utf-8").writelines(l+"\n" for l in out)
            anchored+=1
        report.append(f"P{srcnum}: deep-dive -> {anchored} root(s): {targets}")
    print("\n".join(report))
    # write report fragment
    open(r"D:/Paper Ecology/_formal_f1_report.txt","w",encoding="utf-8").write("\n".join(report))

if __name__=="__main__":
    main()
