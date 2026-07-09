import sqlite3, os, json

root = r"D:\Paper Ecology"

dbs = {
    'CodeLib': os.path.join(root, 'CodeLib', 'code_lib.db'),
    'CrystalLib': os.path.join(root, 'CrystalLib', 'crystal_lib.db'),
    'CMPLX-Standards': os.path.join(root, 'CMPLX-Standards', 'cmplx_standards.db'),
    'SystemsLib': os.path.join(root, 'SystemsLib', 'systems_lib.db'),
}

for name, path in dbs.items():
    print(f"=== {name} ===")
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    for row in cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall():
        t = row[0]
        cur2 = conn.cursor()
        cur2.execute(f"PRAGMA table_info({t})")
        cols = [c[1] for c in cur2.fetchall()]
        print(f"  {t}: {cols}")
    conn.close()
    print()
