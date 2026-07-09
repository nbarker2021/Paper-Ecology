"""
build_crystal_cache.py — ONE-TIME dump of all D-claims from CrystalLib into a
local JSON cache so the resynthesis pass doesn't hit the slow/locked 415k-row DB
on every query.

Output: crystal_d_cache.json  -> list of {id, paper, text}
Run once (may take ~30-60s on the locked DB). Then resynthesis_pass uses the cache.
"""
import sqlite3, json, os

CRYSTAL = r"D:/Paper Ecology/CrystalLib/crystal_lib.db"
OUT = r"D:/Paper Ecology/ProofLib/DerivationLedger/crystal_d_cache.json"

def main():
    print("Connecting (read-only, 60s busy timeout)...")
    con = sqlite3.connect(CRYSTAL, timeout=60)
    con.execute("PRAGMA busy_timeout=60000")
    con.execute("PRAGMA query_only=1")
    cur = con.cursor()
    print("Querying all D-claims (this can take a bit on the locked DB)...")
    cur.execute("SELECT claim_id, paper_number, claim_text FROM claims WHERE claim_status='D'")
    rows = [{"id": r[0], "paper": r[1], "text": (r[2] or "")} for r in cur.fetchall()]
    con.close()
    json.dump(rows, open(OUT, "w"))
    total_chars = sum(len(r["text"]) for r in rows)
    print(f"Cached {len(rows)} D-claims -> {OUT}")
    print(f"Total text chars: {total_chars:,}")

if __name__ == "__main__":
    main()
