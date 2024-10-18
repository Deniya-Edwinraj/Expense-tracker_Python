import sqlite3

def create_connection():
    conn = sqlite3.connect('expenses.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT NOT NULL,
                        description TEXT NOT NULL,
                        category TEXT NOT NULL,
                        amount REAL NOT NULL
                     )''')
    conn.commit()
    conn.close()
