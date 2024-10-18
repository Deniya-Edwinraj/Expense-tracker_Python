import sqlite3
from database import create_connection

def add_expense(date, description, category, amount):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO expenses (date, description, category, amount) 
                      VALUES (?, ?, ?, ?)''', (date, description, category, amount))
    conn.commit()
    conn.close()

def view_expenses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()

def update_expense(expense_id, date, description, category, amount):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''UPDATE expenses 
                      SET date = ?, description = ?, category = ?, amount = ? 
                      WHERE id = ?''', (date, description, category, amount, expense_id))
    conn.commit()
    conn.close()
