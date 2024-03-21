import sqlite3
from datetime import date
from models import Base, Expense, Saving, Accounts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

today_date = date.today()

engine = create_engine('sqlite:///budget_db.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

new_accounts = [
    Accounts(account="Pekao", balance = 14000.00, date=today_date),
    Accounts(account="Revolut", balance = 11000.00, date=today_date),
    Accounts(account="Etoro", balance = 5400.00, date=today_date),
    Accounts(account="Xtb", balance = 500.00, date=today_date),
    Accounts(account="Cash", balance = 3300.00, date=today_date),
    Accounts(account="ViennaLife", balance = 58000.00, date=today_date),
]

session.add_all(new_accounts)
session.commit()
session.close()