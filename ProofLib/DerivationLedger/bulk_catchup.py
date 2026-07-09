"""
bulk_catchup.py — processes all REMAINING framework papers in one pass to establish
the baseline (your 2026-07-08 directive: define a baseline, reduce time per action).

Same honest 4-stage pipeline as batch_driver.py (in-folder PDF -> internal-synthesis
-> online directive -> blocked). Loops via PROGRESS.json until [STOP] (paper 240 done
or no file). Each paper's receipts appended to derivation_ledger.jsonl.

Run:  python bulk_catchup.py
Prints a running summary; safe to Ctrl-C (PROGRESS persists).
"""
import os, sys, subprocess, time, datetime

ROOT = r"D:/Paper Ecology/ProofLib/DerivationLedger"
PY = r"D:/Paper Ecology/EnvLib/.venv/Scripts/python.exe"
PROGRESS = os.path.join(ROOT, "PROGRESS.json")
DRIVER = os.path.join(ROOT, "batch_driver.py")

def get_last():
    if os.path.exists(PROGRESS):
        try:
            return int(json.load(open(PROGRESS)).get("last", 0))
        except Exception:
            return 0
    return 0

import json

def main():
    count = 0
    while True:
        last = get_last()
        nxt = f"{last+1:03d}"
        # check file exists
        import glob
        if not glob.glob(os.path.join(r"D:/Paper Ecology/main_papers/root_papers", f"{nxt}_*.md")):
            print(f"[STOP] no paper file for {nxt} — baseline complete at {last}.")
            break
        t0 = time.time()
        proc = subprocess.run([PY, DRIVER, "--paper", nxt], cwd=ROOT,
                              capture_output=True, text=True)
        dt = time.time() - t0
        # parse summary line
        out = proc.stdout
        for line in out.splitlines():
            if line.startswith("[PROGRESS]"):
                print(f"[{datetime.datetime.now():%H:%M:%S}] {nxt} ({dt:.1f}s) | {line.strip()}")
        if proc.returncode != 0:
            print(f"[ERROR] {nxt} exited {proc.returncode}: {proc.stderr[:300]}")
            break
        count += 1
        if last + 1 >= 240:
            print(f"[STOP] reached paper 240. Baseline complete ({count} papers this run).")
            break
    print(f"\nBulk catch-up done. Papers processed this run: {count}. Ledger at {get_last()}.")

if __name__ == "__main__":
    main()
