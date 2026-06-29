import sqlite3

conn = sqlite3.connect(
    "data.db",
    check_same_thread=False
)

conn.execute("""
CREATE TABLE IF NOT EXISTS records(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

conn.commit()