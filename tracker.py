import pandas as pd
import sqlite3
from datetime import date
from sqlalchemy import create_engine, Column, Float, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Expenses(Base):
    __tablename__ = 'expenses'

    id = Column("id", Integer, primary_key=True)
    date = Column("date", Date)
    product = Column("product", String)
    category = Column("category", String)
    importance = Column("importance", String)

    def __repr__(self):
        return f'ID: {self.id}, date: {self.date}, product: {self.product}, category: {self.category}, importance: {self.importance}'


new_expense = Expenses(
    date = date(2024, 3, 7),
    product = "Laptop",
    category = "Electronics",
    importance = "Must have")

print(new_expense)