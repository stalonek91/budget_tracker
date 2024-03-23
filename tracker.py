import sqlite3
from datetime import date
from models import Base, Expense, Saving, Accounts
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
import tkinter as tk
from tkinter import ttk


today_date = date.today()

engine = create_engine('sqlite:///budget_db.db')
inspector = inspect(engine)

Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_table_names(table_name):
    columns = inspector.get_columns(table_name)
    column_names = list([column['name'] for column in columns])
    if table_name == 'accounts':
            return column_names
    return column_names[1:]

def clear_content():

    global tree

    print(f'Function clear content triggered')
    for widget in main_content.winfo_children():
        widget.destroy()
    try:
        tree.destroy()
        tree = None
    except NameError:
        pass

def create_fields(labels: list):
    entries = {}

    for i, text in enumerate(labels):
        label = tk.Label(main_content, text=text, bg=main_content_bg, fg="black")
        label.grid(row=i, column=0, sticky='e', padx=5, pady=5)

        entry = tk.Entry(main_content)
        entry.grid(row=i, column=1, sticky="ew", padx=5, pady=5)
        entries["text"] = entry 


def show_saving():
    print(f'Function show saving')
    clear_content()

    labels_text = get_table_names('savings')
    create_fields(labels_text)


def show_accounts():
    print(f'We are in show accounts function')
    clear_content()

    accounts_from_db = session.query(Accounts).all()
    columns = get_table_names('accounts')
    tree = ttk.Treeview(root, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col.title())

    for account in accounts_from_db:
        tree.insert('', tk.END, values=(account.id, account.account, account.balance, account.date))

    tree.pack(fill='both', expand=True)


def show_expense():
    print(f'We are in show expense function')
    clear_content()

    labels_text = get_table_names('expenses')
    create_fields(labels_text)


root = tk.Tk()
root.title("Budget Tracker")
root.geometry("1000x500")


sidebar = ttk.Frame(root, width=200, height=500)
sidebar.pack(expand=False, fill='y', side='left', anchor='nw')


# Create buttons and add them to the sidebar frame
expense_button = ttk.Button(sidebar, text="Expense", command=show_expense)
expense_button.pack(fill='x')

saving_button = ttk.Button(sidebar, text="Saving", command=show_saving)
saving_button.pack(fill='x')

accounts_button = ttk.Button(sidebar, text="Accounts",command=show_accounts)
accounts_button.pack(fill='x')

# Main content area
main_content_bg = "#d3d3d3"  # Light gray color for the main content area
main_content = tk.Frame(root, width=600, height=500, bg=main_content_bg)
main_content.pack(expand=True, fill='both', side='right')

root.mainloop()