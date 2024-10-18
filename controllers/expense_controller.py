from models.expense_model import add_expense, view_expenses, delete_expense, update_expense

def add_new_expense(date, description, category, amount):
    add_expense(date, description, category, amount)

def get_all_expenses():
    return view_expenses()

def remove_expense(expense_id):
    delete_expense(expense_id)

def modify_expense(expense_id, date, description, category, amount):
    update_expense(expense_id, date, description, category, amount)

def calculate_total_expenses():
    expenses = get_all_expenses()
    return sum([expense[4] for expense in expenses])  # Summing the amount column
