import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
from controllers.expense_controller import add_new_expense, get_all_expenses, calculate_total_expenses
from database import create_table 
import matplotlib.pyplot as plt

class ExpenseTrackerApp:
    def __init__(self):
        create_table()  
        self.root = tk.Tk()
        self.root.title("Expense Tracker")
        self.root.geometry("800x600") 
        self.root.configure(bg="#ECEFF4")  
        self.root.resizable(False, False)

        self.main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        self.main_frame.pack(expand=True)  
        self.main_frame.pack_propagate(0)  

        self.build_ui()

    def build_ui(self):
        try:
            self.logo = PhotoImage(file="assets/logo.png")
            logo_label = ttk.Label(self.main_frame, image=self.logo)
            logo_label.grid(row=0, column=0, pady=20, columnspan=2)
        except Exception as e:
            print(f"Error loading logo: {e}")

        ttk.Label(self.main_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, sticky=tk.E, padx=10, pady=10)
        self.entry_date = ttk.Entry(self.main_frame, width=30)
        self.entry_date.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.main_frame, text="Description:").grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)
        self.entry_description = ttk.Entry(self.main_frame, width=30)
        self.entry_description.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.main_frame, text="Category:").grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)
        self.combo_category = ttk.Combobox(self.main_frame, values=["Food", "Transport", "Rent", "Entertainment", "Other"], width=28)
        self.combo_category.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(self.main_frame, text="Amount:").grid(row=4, column=0, sticky=tk.E, padx=10, pady=10)
        self.entry_amount = ttk.Entry(self.main_frame, width=30)
        self.entry_amount.grid(row=4, column=1, padx=10, pady=10)

        self.button_add = ttk.Button(self.main_frame, text="Add Expense", command=self.add_expense)
        self.button_add.grid(row=5, columnspan=2, pady=20)

        self.button_load = ttk.Button(self.main_frame, text="Load Expenses", command=self.load_expenses)
        self.button_load.grid(row=6, columnspan=2, pady=10)

        self.button_chart = ttk.Button(self.main_frame, text="View Chart", command=self.show_expense_chart)
        self.button_chart.grid(row=7, columnspan=2, pady=10)

        self.button_total = ttk.Button(self.main_frame, text="Total Expenses", command=self.show_total_expenses)
        self.button_total.grid(row=8, columnspan=2, pady=10)

    def add_expense(self):
        date = self.entry_date.get()
        description = self.entry_description.get()
        category = self.combo_category.get()
        amount = self.entry_amount.get()

        if date and description and category and amount:
            try:
                add_new_expense(date, description, category, float(amount))
                messagebox.showinfo("Success", "Expense added successfully")
                self.clear_inputs()
            except ValueError:
                messagebox.showerror("Error", "Amount must be a number")
        else:
            messagebox.showerror("Error", "All fields are required")

    def load_expenses(self):
        expenses = get_all_expenses()
        
        expenses_window = tk.Toplevel(self.root)
        expenses_window.title("All Expenses")
        expenses_window.geometry("600x400")

        tree = ttk.Treeview(expenses_window, columns=("Date", "Description", "Category", "Amount"), show='headings')
        tree.heading("Date", text="Date")
        tree.heading("Description", text="Description")
        tree.heading("Category", text="Category")
        tree.heading("Amount", text="Amount")
        tree.pack(expand=True, fill='both')

        for expense in expenses:
            tree.insert("", tk.END, values=expense[1:])  

    def show_expense_chart(self):
        expenses = get_all_expenses()
        categories = {}
        
        for expense in expenses:
            category = expense[3]  
            amount = expense[4]  
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

        plt.figure(figsize=(10, 6))
        plt.bar(categories.keys(), categories.values(), color='skyblue')
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def show_total_expenses(self):
        total = calculate_total_expenses()
        messagebox.showinfo("Total Expenses", f"Total expenses: {total}")

    def clear_inputs(self):
        self.entry_date.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)

    def run(self):
        self.root.mainloop()
