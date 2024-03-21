from sqlalchemy import create_engine, Column, Float, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Expense(Base):  # Adjusted class name for consistency
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    product = Column(String)
    price = Column(Float)
    category = Column(String)
    importance = Column(Integer)
    account_name = Column(String, ForeignKey('accounts.account'))

    account_detail = relationship("Accounts", back_populates="expenses")  # Adjusted to match class name

    def __repr__(self):
        return f'ID: {self.id}, date: {self.date}, product: {self.product}, category: {self.category}, importance: {self.importance}, account: {self.account_name}'

class Saving(Base):
    __tablename__ = 'savings'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    product = Column(String)
    price = Column(Float)
    account_name = Column(String, ForeignKey('accounts.account'))

    account_detail = relationship("Accounts", back_populates="savings")  # Adjusted to match class name

    def __repr__(self):
        return f'ID: {self.id}, date: {self.date}, product: {self.product}, Money saved: {self.price}, account: {self.account_name}'
    
class Accounts(Base):  # Adjusted class name for consistency
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    account = Column(String, unique=True)
    balance = Column(Float)
    date = Column(Date, nullable=False)

    expenses = relationship("Expense", back_populates="account_detail")  # Now matches attribute name in Expense
    savings = relationship("Saving", back_populates="account_detail")  # Now matches attribute name in Saving

    def __repr__(self):
        return f"Account(id={self.id}, account='{self.account}', balance={self.balance}, date={self.date.isoformat()})"
