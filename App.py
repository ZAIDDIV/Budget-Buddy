from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
app.config['SECRET_KEY'] = Config.SECRET_KEY
db = SQLAlchemy(app)

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email    = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    budgets  = db.relationship('Budget',  backref='owner', lazy=True)
    assets   = db.relationship('Asset',   backref='owner', lazy=True)
    expenses = db.relationship('Expense', backref='owner', lazy=True)
    loans    = db.relationship('Loan',    backref='owner', lazy=True)

class Budget(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(100), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    user_id      = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Asset(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    amount   = db.Column(db.Float, nullable=False)
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Expense(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    amount   = db.Column(db.Float, nullable=False)
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Loan(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    loan_type   = db.Column(db.String(10), nullable=False)  # 'gave' or 'took'
    person      = db.Column(db.String(100), nullable=False)
    amount      = db.Column(db.Float, nullable=False)
    due_date    = db.Column(db.String(20), nullable=True)
    description = db.Column(db.String(200), nullable=True)
    status      = db.Column(db.String(10), default='unpaid')  # 'paid' or 'unpaid'
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/')
def home():
    if "user_id" in session:
        return redirect(url_for('assets'))
    return render_template("welcome.html")

@app.route("/assets", methods=["GET", "POST"])
def assets():
    if "user_id" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        form_type = request.form.get("form_type")
        category  = request.form.get("category")
        amount    = request.form.get("amount")
        if category == "Other":
            category = request.form.get("custom_label", "Other").strip()
        if not category or not amount:
            flash("Please fill all fields.", "error")
            return redirect(url_for("assets"))
        if form_type == "expense":
            db.session.add(Expense(category=category, amount=float(amount), user_id=session["user_id"]))
            flash("Expense added!", "success")
        else:
            db.session.add(Asset(category=category, amount=float(amount), user_id=session["user_id"]))
            flash("Asset added!", "success")
        db.session.commit()
        return redirect(url_for("assets"))
    user_assets   = Asset.query.filter_by(user_id=session["user_id"]).all()
    user_expenses = Expense.query.filter_by(user_id=session["user_id"]).all()
    user_loans    = Loan.query.filter_by(user_id=session["user_id"]).all()
    return render_template("assets.html", assets=user_assets, expenses=user_expenses, loans=user_loans)

@app.route("/delete_asset/<int:asset_id>", methods=["POST"])
def delete_asset(asset_id):
    if "user_id" not in session: return redirect(url_for("login"))
    asset = Asset.query.get_or_404(asset_id)
    if asset.user_id != session["user_id"]: return redirect(url_for("assets"))
    db.session.delete(asset); db.session.commit()
    flash("Asset deleted.", "success")
    return redirect(url_for("assets"))

@app.route("/delete_expense/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    if "user_id" not in session: return redirect(url_for("login"))
    expense = Expense.query.get_or_404(expense_id)
    if expense.user_id != session["user_id"]: return redirect(url_for("assets"))
    db.session.delete(expense); db.session.commit()
    flash("Expense deleted.", "success")
    return redirect(url_for("assets"))

@app.route("/add_loan", methods=["POST"])
def add_loan():
    if "user_id" not in session: return redirect(url_for("login"))
    loan_type   = request.form.get("loan_type")
    person      = request.form.get("person", "").strip()
    amount      = request.form.get("amount")
    due_date    = request.form.get("due_date", "")
    description = request.form.get("description", "").strip()
    if not person or not amount or not loan_type:
        flash("Please fill all required fields.", "error")
        return redirect(url_for("assets"))
    db.session.add(Loan(
        loan_type=loan_type, person=person, amount=float(amount),
        due_date=due_date or None, description=description or None,
        status="unpaid", user_id=session["user_id"]
    ))
    db.session.commit()
    flash("Loan added!", "success")
    return redirect(url_for("assets"))

@app.route("/toggle_loan/<int:loan_id>", methods=["POST"])
def toggle_loan(loan_id):
    if "user_id" not in session: return redirect(url_for("login"))
    loan = Loan.query.get_or_404(loan_id)
    if loan.user_id != session["user_id"]: return redirect(url_for("assets"))
    loan.status = "paid" if loan.status == "unpaid" else "unpaid"
    db.session.commit()
    flash("Loan status updated.", "success")
    return redirect(url_for("assets"))

@app.route("/delete_loan/<int:loan_id>", methods=["POST"])
def delete_loan(loan_id):
    if "user_id" not in session: return redirect(url_for("login"))
    loan = Loan.query.get_or_404(loan_id)
    if loan.user_id != session["user_id"]: return redirect(url_for("assets"))
    db.session.delete(loan); db.session.commit()
    flash("Loan deleted.", "success")
    return redirect(url_for("assets"))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        terms = request.form.get('terms')
        if not username or not email or not password or not confirm_password:
            flash("All fields are required.", "error"); return redirect(url_for('signup'))
        if not terms:
            flash("You must accept the Terms & Conditions.", "error"); return redirect(url_for('signup'))
        if password != confirm_password:
            flash("Passwords do not match!", "error"); return redirect(url_for('signup'))
        if len(password) < 8:
            flash("Password must be at least 8 characters.", "error"); return redirect(url_for('signup'))
        if User.query.filter_by(email=email).first():
            flash("Email already registered!", "error"); return redirect(url_for('signup'))
        db.session.add(User(username=username, email=email, password=generate_password_hash(password)))
        db.session.commit()
        flash("Account created! Please login.", "success")
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if not email or not password:
            flash("Please fill in all fields.", "error"); return redirect(url_for('login'))
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            flash(f"Welcome back, {user.username}!", "success")
            return redirect(url_for('assets'))
        flash("Invalid email or password!", "error")
        return redirect(url_for('login'))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for('home'))

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)