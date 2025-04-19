import sqlite3

conn = sqlite3.connect("db")
cursor = conn.cursor()
cursor.executemany("INSERT INTO items (name) VALUES (?)", [("Яблоко",), ("Груша",), ("Банан",)])
conn.commit()
conn.close()