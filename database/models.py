from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .connection import Base
import enum
from datetime import date
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship


# Enum for transaction types


class TransactionType(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"
    LOAN = "loan"

# User table


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    # Relationship to MonthPlans
    months = relationship("MonthPlan", back_populates="user")


# MonthPlan table
class MonthPlan(Base):
    __tablename__ = "month_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    month = Column(String, nullable=False)  # e.g., "January"
    year = Column(Integer, nullable=False)
    starting_assets = Column(Float, default=0.0)

    user = relationship("User", back_populates="months")
    transactions = relationship("Transaction", back_populates="month_plan")


# Transaction table (income, expense, loan)
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    month_plan_id = Column(Integer, ForeignKey("month_plans.id"))
    type = Column(Enum(TransactionType), nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String)
    date = Column(Date, default=date.today)

    month_plan = relationship("MonthPlan", back_populates="transactions")
