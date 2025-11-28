import sqlite3, sys

db = 'db.sqlite3'
try:
    conn = sqlite3.connect(db)
    c = conn.cursor()
    tables = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()]
    print('TABLES:', tables)
    for t in tables:
        try:
            cnt = c.execute(f'SELECT COUNT(*) FROM "{t}"').fetchone()[0]
        except Exception as e:
            cnt = f'ERROR: {e}'
        print('\nTABLE', t, '— rows:', cnt)
        if isinstance(cnt, int) and cnt > 0:
            try:
                sample = c.execute(f'SELECT * FROM "{t}" LIMIT 3').fetchall()
                print('SAMPLE ROWS:')
                for row in sample:
                    print(row)
            except Exception as e:
                print('SAMPLE ERROR:', e)
    conn.close()
except Exception as e:
    print('ERROR opening database:', e)
    sys.exit(1)
