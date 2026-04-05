# 💰 Budget Buddy

> **Your personal finance companion — track income, expenses, loans, and stay on top of your money.**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-red?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/status-active--development-orange?style=flat-square)

---

## 📸 Overview

Budget Buddy is a lightweight, self-hosted personal finance web app built with **Python + Flask**. It helps you get a real-time picture of your financial health — what you own, what you spend, and who owes who — all in one clean dashboard.

No subscriptions. No ads. Just your data, under your control.

---

## ✨ Current Features

### 🔐 Auth System
- Secure signup & login with hashed passwords (Werkzeug)
- Session-based authentication
- Per-user data isolation — your finances are yours only

### 📊 Dashboard
- Total assets, total expenses, and **net balance** at a glance
- Overview of all unpaid loans
- Smart empty state for new users

### 💼 Assets & Expenses
- Log income sources, savings, or anything you own as **assets**
- Log daily spending as **expenses**
- Categorize with presets or a custom label
- Edit or delete any entry anytime

### 🤝 Loan Tracker
- Track money you **gave** to someone or **took** from someone
- Set due dates and descriptions per loan
- Toggle loans between **paid / unpaid** status
- Full edit and delete support

### 🧾 Transactions View
- Unified chronological feed of all assets, expenses, and loans
- Sorted by date — newest first
- Summary totals: assets, expenses, loans gave & took

---

## 🛣️ Roadmap

This is just the beginning. Here's the full vision for Budget Buddy:

### 🔜 Coming Soon
- [ ] 📈 **Dashboard Analytics** — Charts and graphs for spending trends over time
- [ ] 🔔 **Spend Alerts** — Get notified when you cross a budget threshold
- [ ] 💬 **In-App Notifications** — Pop-up alerts for due loans and overspending
- [ ] 📅 **Monthly Budget Goals** — Set limits per category and track progress
- [ ] 📤 **Export Reports** — Download your data as CSV or PDF
- [ ] 🌙 **Dark Mode** — Easy on the eyes, especially at night
- [ ] 📱 **Mobile-Responsive UI** — Smooth experience on any screen size
- [ ] 🔁 **Recurring Transactions** — Auto-log monthly bills or salaries
- [ ] 🏷️ **Tags & Filters** — Filter transactions by category, date range, type

### 📧 Gmail Integration *(Planned)*
- [ ] Connect your Gmail account to Budget Buddy
- [ ] Auto-detect and parse bank transaction emails
- [ ] Automatically log expenses and income from email receipts
- [ ] Support for major bank email formats
- [ ] Smart categorization of transactions from email data
- [ ] Alert emails when your spending exceeds set limits

### 🏦 Mobile Banking & App Integrations *(Future Vision)*
> The big one. The goal is to make Budget Buddy a **central hub** for all your financial activity — automatically synced, zero manual entry.

- [ ] 🔗 **Bank Account Sync** — Connect directly to your mobile banking app and pull all transactions automatically
- [ ] 💳 **Card Transaction Tracking** — Every debit/credit card spend logged in real time
- [ ] 📲 **SMS & Notification Parsing** — Read bank SMS alerts and auto-log transactions
- [ ] 🏧 **Multi-Bank Support** — Works across multiple banks and accounts simultaneously
- [ ] 📊 **Unified Financial Dashboard** — See ALL your accounts, cards, and cash in one place
- [ ] 🤖 **AI Spending Insights** — Smart suggestions based on your spending patterns
- [ ] 🔄 **Auto Reconciliation** — Match your logged expenses with actual bank transactions
- [ ] 🌍 **Multi-Currency Support** — For users with accounts in different currencies
- [ ] 📉 **Overspend Detection** — Real-time warnings when you're about to exceed your budget
- [ ] 🗓️ **Bill Reminders** — Never miss a payment with automated due date reminders

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/ZAIDDIV/Budget-Buddy.git
cd Budget-Buddy

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your environment variables
cp .env.example .env
# Edit .env with your config (see below)

# 5. Run the app
python App.py
```

Then open your browser at **http://127.0.0.1:5000**

---

## ⚙️ Configuration

Edit your `.env` file:

```env
DATABASE_URL=sqlite:///finance.db
SECRET_KEY=your-secret-key-here

# Email config (Gmail integration — coming soon)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your@gmail.com
EMAIL_PASSWORD=your-app-password
```

---

## 🗂️ Project Structure

```
Budget-Buddy/
├── App.py                  # Main Flask app — routes & models
├── config.py               # Config loader (env vars)
├── requirements.txt        # Python dependencies
├── .env.example            # Sample environment file
├── database/
│   ├── connection.py
│   ├── models.py
│   └── init_db.py
└── templates/
    ├── welcome.html
    ├── login.html
    ├── signup.html
    ├── dashboard.html
    ├── assets.html
    ├── transactions.html
    └── index.html
```

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite (via SQLAlchemy) |
| Auth | Werkzeug password hashing |
| Templating | Jinja2 |
| Config | python-dotenv |
| Email *(planned)* | Gmail API / SMTP |
| Banking *(planned)* | Open Banking APIs |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 👨‍💻 Author

**Zaid** — [@ZAIDDIV](https://github.com/ZAIDDIV)

---

## 📄 License

This project is licensed under the MIT License.

---

> ⭐ If you find this useful, drop a star on the repo — it helps a lot!
>
> 🚧 This project is actively being built. Big things coming — watch the repo to stay updated.
