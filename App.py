from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

# ---- App Setup ----
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
app.config['SECRET_KEY'] = Config.SECRET_KEY

db = SQLAlchemy(app)

# ---- Database Models ----
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    budgets = db.relationship('Budget', backref='owner', lazy=True)
    assets = db.relationship('Asset', backref='owner', lazy=True)


class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# ---- Home Route ----
@app.route('/')
def home():
    if "user_id" in session:
        return redirect(url_for('assets'))  # logged in → go straight to assets
    return render_template("welcome.html")  # not logged in → welcome page


# ---- Assets Route ----
@app.route("/assets", methods=["GET", "POST"])
def assets():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        category = request.form.get("category")
        amount = request.form.get("amount")

        if not category or not amount:
            flash("Please fill all fields.", "error")
            return redirect(url_for("assets"))

        new_asset = Asset(
            category=category,
            amount=float(amount),
            user_id=session["user_id"]
        )

        db.session.add(new_asset)
        db.session.commit()

        flash("Asset added successfully!", "success")
        return redirect(url_for("assets"))

    user_assets = Asset.query.filter_by(user_id=session["user_id"]).all()
    return render_template("assets.html", assets=user_assets)


# ---- Signup Route ----
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        terms = request.form.get('terms')

        # Validate all fields filled
        if not username or not email or not password or not confirm_password:
            flash("All fields are required.", "error")
            return redirect(url_for('signup'))

        # Validate terms accepted
        if not terms:
            flash("You must accept the Terms & Conditions to register.", "error")
            return redirect(url_for('signup'))

        # Validate passwords match
        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return redirect(url_for('signup'))

        # Validate password length
        if len(password) < 8:
            flash("Password must be at least 8 characters long.", "error")
            return redirect(url_for('signup'))

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered! Please login.", "error")
            return redirect(url_for('signup'))

        # Hash password and save user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please login.", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')


# ---- Login Route ----
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Please fill in all fields.", "error")
            return redirect(url_for('login'))

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            flash(f"Welcome back, {user.username}!", "success")
            return redirect(url_for('assets'))  # login → go straight to assets
        else:
            flash("Invalid email or password!", "error")
            return redirect(url_for('login'))

    return render_template("login.html")


# ---- Logout Route ----
@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for('home'))


# ---- Create Database Tables ----
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)