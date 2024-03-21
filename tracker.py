import sqlite3
from datetime import date
from models import Base, Expense, Saving, Accounts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Budget Tracker")



sidebar = ttk.Frame(root, width=200, height=500)
sidebar.pack(expand=False, fill='y', side='left', anchor='nw')




# Create buttons and add them to the sidebar frame
expense_button = ttk.Button(sidebar, text="Expense")
expense_button.pack(fill='x')

saving_button = ttk.Button(sidebar, text="Saving")
saving_button.pack(fill='x')

accounts_button = ttk.Button(sidebar, text="Accounts")
accounts_button.pack(fill='x')

# Main content area
main_content = ttk.Frame(root, width=600, height=500)
main_content.pack(expand=True, fill='both', side='right')

labels_text = ['Product', 'Price', 'Category', 'Importance', 'Account Name']
entries = {}

for i, text in enumerate(labels_text):
    label = tk.Label(main_content, text=text)
    label.grid(row=i, column=0, sticky='e', padx=5, pady=5)

    entry = tk.Entry(main_content)
    entry.grid(row=i, column=1, sticky="ew", padx=5, pady=5)
    entries["text"] = entry

today_date = date.today()

engine = create_engine('sqlite:///budget_db.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# new_accounts = [
#     Accounts(account="Pekao", balance = 14000.00, date=today_date),
#     Accounts(account="Revolut", balance = 11000.00, date=today_date),
#     Accounts(account="Etoro", balance = 5400.00, date=today_date),
#     Accounts(account="Xtb", balance = 500.00, date=today_date),
#     Accounts(account="Cash", balance = 3300.00, date=today_date),
#     Accounts(account="ViennaLife", balance = 58000.00, date=today_date),
# ]

# session.add_all(new_accounts)
# session.commit()
# session.close()


root.mainloop()