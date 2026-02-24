from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
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
        return render_template("index.html")
    else:
        return render_template("welcome.html")


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

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered!", "error")
            return redirect(url_for('signup'))

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully!", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')


# ---- Login Route ----
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Login successful!", "success")
            return redirect(url_for('home'))
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