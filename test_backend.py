from database.connection import SessionLocal
from database.models import Base, User, MonthPlan, Transaction, TransactionType
from database.connection import engine
from sqlalchemy import func
from datetime import date

# 1️⃣ Create tables if not exist
Base.metadata.create_all(bind=engine)

# 2️⃣ Start session
db = SessionLocal()

# 3️⃣ Create or get test user
test_user = db.query(User).filter_by(email="zaid@test.com").first()
if not test_user:
    test_user = User(username="zaid", email="zaid@test.com",
                     password_hash="hashedpass")
    db.add(test_user)
    db.commit()
    db.refresh(test_user)

# 4️⃣ Create or get MonthPlan for this user
month_plan = (
    db.query(MonthPlan)
    .filter_by(user_id=test_user.id, month="February", year=2026)
    .first()
)

if not month_plan:
    month_plan = MonthPlan(
        user_id=test_user.id,
        month="February",
        year=2026,
        starting_assets=50000
    )
    db.add(month_plan)
    db.commit()
    db.refresh(month_plan)

# 5️⃣ Add Transactions (if they don't already exist)
existing_tx_count = db.query(Transaction).filter_by(
    month_plan_id=month_plan.id).count()

if existing_tx_count == 0:
    transactions = [
        Transaction(month_plan_id=month_plan.id, type=TransactionType.INCOME,
                    category="Salary", amount=30000, description="Monthly salary"),
        Transaction(month_plan_id=month_plan.id, type=TransactionType.EXPENSE,
                    category="Rent", amount=10000, description="Apartment rent"),
        Transaction(month_plan_id=month_plan.id, type=TransactionType.EXPENSE,
                    category="Grocery", amount=5000, description="Monthly groceries"),
        Transaction(month_plan_id=month_plan.id, type=TransactionType.LOAN,
                    category="Car Loan", amount=8000, description="Car loan installment")
    ]
    db.add_all(transactions)
    db.commit()

# 6️⃣ Calculate totals dynamically
total_income = (
    db.query(func.sum(Transaction.amount))
    .filter_by(month_plan_id=month_plan.id, type=TransactionType.INCOME)
    .scalar() or 0
)

total_expense = (
    db.query(func.sum(Transaction.amount))
    .filter_by(month_plan_id=month_plan.id, type=TransactionType.EXPENSE)
    .scalar() or 0
)

total_loans = (
    db.query(func.sum(Transaction.amount))
    .filter_by(month_plan_id=month_plan.id, type=TransactionType.LOAN)
    .scalar() or 0
)

net_balance = month_plan.starting_assets + \
    total_income - total_expense - total_loans

# 7️⃣ Print results
print(f"User: {test_user.username}")
print(f"Month: {month_plan.month} {month_plan.year}")
print(f"Starting Assets: {month_plan.starting_assets}")
print(f"Total Income: {total_income}")
print(f"Total Expenses: {total_expense}")
print(f"Total Loans: {total_loans}")
print(f"Net Balance: {net_balance}")

# 8️⃣ Close session
db.close()
