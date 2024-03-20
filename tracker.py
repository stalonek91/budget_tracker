import pandas as pd
import sqlite3
from datetime import date
from models import Expenses, Saving
import tkinter

today_date = date.today()

new_expense = Expenses(
    date = today_date,
    product = "Laptop",
    category = "Electronics",
    importance = "Must have")

print(new_expense)