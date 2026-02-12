# 💰 Personal Finance Manager

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=flat-square)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange?style=flat-square)

A comprehensive, intelligent financial management system built entirely in Python. Take control of your finances with budget tracking, expense categorization, debt management, and intelligent analytics.

[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [30-Day Development Roadmap](#-30-day-development-roadmap)
- [Usage Guide](#-usage-guide)
- [Database Schema](#-database-schema)
- [Contributing](#-contributing)
- [Roadmap](#-roadmap)
- [License](#-license)
- [Support](#-support)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 Project Overview

**Personal Finance Manager** is a comprehensive financial management system that empowers users to take complete control of their finances. Built entirely in Python with a modern web-based interface, it combines powerful tracking capabilities with intelligent analytics to help users make better financial decisions.

### Key Highlights

✨ **Comprehensive Financial Tracking** - Monitor income, expenses, budgets, and debt all in one place  
📊 **Advanced Analytics** - Visualize spending patterns with interactive charts and detailed reports  
🤖 **Smart Features** - OCR receipt scanning, CSV bank imports, AI-powered recommendations  
📱 **User-Friendly Interface** - Intuitive Streamlit web application accessible from any device  
🔐 **Secure & Private** - All data stored locally with optional PostgreSQL support  

### Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Modern web-based user interface |
| **SQLite/PostgreSQL** | Database management |
| **ReportLab** | PDF generation and reporting |
| **openpyxl** | Excel file export |
| **Matplotlib/Plotly** | Interactive data visualization |
| **pytesseract** | Optical Character Recognition (OCR) |
| **pandas** | Data analysis and manipulation |

---

## ✨ Features

### 💵 Core Money Management

- **Monthly Budget Setup** - Create flexible budgets with customizable spending limits
- **Multiple Income Sources** - Track various income streams (salary, freelance, investments, etc.)
- **Expense Categorization** - Organize spending across predefined categories:
  - 🏠 Housing (rent, mortgage, utilities)
  - 🍔 Food & Dining
  - 🚗 Transportation
  - 🏥 Healthcare & Medical
  - 📱 Subscriptions & Services
  - 📚 Education
  - 💄 Personal Care
  - 🎬 Entertainment
  - 💳 Debt Payments
  - 🎯 Savings Contributions
  - 📦 Miscellaneous

### 📍 Smart Tracking

- **Recurring Expense Automation** - Set automatic recurring transactions
- **One-Time Expense Logging** - Quick addition of individual expenses
- **Planned vs Actual Comparison** - Track budget performance with visual comparisons
- **Bill Reminders** - Automated notifications for upcoming bills
- **Overspending Alerts** - Real-time warnings when approaching or exceeding budget limits
- **Transaction Search & Filter** - Advanced search across all financial records

### 💳 Debt Management

- **Multiple Loan Tracking** - Monitor multiple debts simultaneously
- **Payoff Timeline Calculations** - Project debt-free dates based on payment plans
- **Interest Computation** - Accurate interest calculation for various loan types
- **Payoff Strategies** - Snowball and avalanche method comparisons
- **Payment Scheduling** - Track and schedule debt payments

### 🎯 Savings Goals

- **Goal Creation & Management** - Set specific, measurable financial goals
- **Progress Tracking** - Visual representation of savings progress
- **Achievement Predictions** - AI estimates on goal completion dates
- **Goal Milestones** - Track intermediate checkpoints
- **Goal Prioritization** - Manage multiple goals with urgency levels

### 📊 Analytics & Insights

- **Monthly Trends** - Analyze spending patterns over time
- **Category Breakdowns** - Visual pie charts and bar graphs by category
- **Cash Flow Visualization** - Income vs expense trends
- **Year-over-Year Comparisons** - Compare financial metrics across periods
- **Spending Patterns** - Machine learning-based anomaly detection
- **Financial Health Score** - Automated assessment of financial status

### 📄 Reports & Exports

- **PDF Statements** - Professional monthly/quarterly statements
- **Excel Exports** - Detailed Excel workbooks with formatted data
- **Yearly Tax Summary** - Pre-formatted tax reporting documents
- **Custom Date Range Reports** - Generate reports for any time period
- **Print-Friendly Formats** - Optimized layouts for printing

### 🚀 Advanced Features

- **Budget Recommendations** - 50/30/20 rule and personalized suggestions
- **Expense Predictions** - Forecast future spending based on historical data
- **Anomaly Detection** - Identify unusual spending patterns
- **Receipt OCR Scanning** - Extract data from receipt images automatically
- **Bank CSV Import** - Import transactions from various bank formats
- **Data Insights** - Personalized financial recommendations
- **Budget Variance Analysis** - Detailed explanations of budget deviations

---

## 💻 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (comes with Python)
- **Git** - [Download Git](https://git-scm.com/)
- **Virtual Environment** - Recommended for isolated Python environments
- **Tesseract OCR** (optional) - [Download Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

### Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/personal-finance-manager.git
cd personal-finance-manager
```

#### 2. Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Environment Variables Configuration

Create a `.env` file in the project root:

```bash
# Database Configuration
DATABASE_URL=sqlite:///./finance_manager.db
# For PostgreSQL: postgresql://user:password@localhost:5432/finance_db

# Application Settings
APP_SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=False
LOG_LEVEL=INFO

# OCR Settings (optional)
PYTESSERACT_PATH=/path/to/tesseract

# Email Notifications (optional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
```

#### 5. Initialize the Database

```bash
python database/init_db.py
```

This will:
- Create necessary database tables
- Set up default categories
- Initialize default settings

#### 6. Run the Application

```bash
streamlit run app.py
```

The application will start at `http://localhost:8501`

---

## 🚀 Quick Start

### First Launch

1. **Create Your Account** - Set up username, email, and secure password
2. **Configure Basic Settings** - Set currency, timezone, and financial year
3. **Add Income Sources** - Enter your primary and secondary income streams
4. **Set Monthly Budget** - Allocate budget to each spending category
5. **Add First Transaction** - Manually add an expense to familiarize yourself

### Common Tasks

#### Adding an Expense

```python
# Navigate to "Add Expense" tab
1. Select date of transaction
2. Choose expense category
3. Enter amount
4. Add description (optional)
5. Click "Save Transaction"
```

#### Creating a Savings Goal

```
1. Go to "Goals" section
2. Click "Create New Goal"
3. Set goal name and target amount
4. Select deadline date
5. Set priority level
6. Track progress automatically
```

#### Generating Reports

```
1. Navigate to "Reports" section
2. Select report type (Monthly, Quarterly, Yearly, Custom)
3. Choose date range
4. Select export format (PDF or Excel)
5. Download generated report
```

#### Importing Bank Data

```
1. Go to "Import Data" section
2. Select your bank from the list
3. Upload CSV file
4. Review and confirm transactions
5. Auto-categorize expenses
```

---

## 📁 Project Structure

```
personal-finance-manager/
│
├── app.py                          # Main Streamlit application entry point
├── config.py                       # Application configuration settings
├── requirements.txt                # Python package dependencies
├── .env.example                    # Environment variables template
├── README.md                       # Project documentation
│
├── database/                       # Database layer
│   ├── __init__.py
│   ├── connection.py              # Database connection management
│   ├── schema.py                  # Database schema definitions
│   ├── models.py                  # SQLAlchemy ORM models
│   ├── init_db.py                 # Database initialization script
│   └── migrations/                # Database migration files
│
├── modules/                       # Core business logic modules
│   ├── __init__.py
│   ├── auth.py                   # User authentication & session management
│   ├── expenses.py               # Expense tracking functionality
│   ├── income.py                 # Income management
│   ├── budget.py                 # Budget creation & tracking
│   ├── analytics.py              # Data analysis & insights
│   ├── goals.py                  # Savings goals management
│   ├── debt.py                   # Debt tracking & payoff calculations
│   └── recurring.py              # Recurring transaction handling
│
├── utils/                        # Utility functions & helpers
│   ├── __init__.py
│   ├── pdf_generator.py         # PDF report generation (ReportLab)
│   ├── excel_export.py          # Excel file export (openpyxl)
│   ├── calculations.py          # Financial calculations & formulas
│   ├── notifications.py         # Email & in-app notifications
│   ├── ocr_scanner.py           # Receipt OCR scanning
│   ├── csv_importer.py          # Bank CSV import handler
│   ├── validators.py            # Input validation functions
│   └── helpers.py               # Miscellaneous helper functions
│
├── pages/                        # Streamlit multi-page structure
│   ├── 🏠_Dashboard.py           # Main dashboard with overview
│   ├── 💸_Add_Expense.py         # Expense entry interface
│   ├── 💰_Add_Income.py          # Income entry interface
│   ├── 📊_Analytics.py           # Charts and analytics visualizations
│   ├── 🎯_Goals.py               # Savings goals management UI
│   ├── 💳_Debts.py               # Debt management interface
│   ├── 📄_Reports.py             # Report generation and export
│   ├── ⚙️_Settings.py            # User preferences and configurations
│   └── 📁_Import_Data.py         # Data import interface
│
├── assets/                       # Static assets
│   ├── logo.png                  # Application logo
│   ├── icons/                    # Category icons and UI elements
│   ├── styles.css                # Custom CSS styling
│   └── images/                   # Documentation images
│
├── data/                         # Data files & templates
│   ├── sample_transactions.csv   # Sample data for demos
│   ├── bank_formats/             # Bank-specific CSV templates
│   └── categories.json           # Default category configuration
│
└── tests/                        # Unit tests
    ├── __init__.py
    ├── test_budget.py
    ├── test_expenses.py
    ├── test_analytics.py
    ├── test_calculations.py
    └── conftest.py               # Pytest configuration
```

---

## 📅 30-Day Development Roadmap

### 🔨 Week 1: Foundation (Days 1-7)

| Day | Task | Deliverable |
|-----|------|-------------|
| 1-2 | Project setup, environment config, dependency installation | Working dev environment |
| 3-4 | Database schema design, SQLAlchemy models setup | Database models & migrations |
| 5 | User authentication system, login/signup UI | User auth module |
| 6-7 | Basic Streamlit UI structure, navigation setup | Multi-page app framework |

**Objectives:**
- ✅ Set up development environment
- ✅ Design database schema
- ✅ Implement user authentication
- ✅ Create UI framework

---

### 💪 Week 2: Core Features (Days 8-14)

| Day | Task | Deliverable |
|-----|------|-------------|
| 8-9 | Budget setup module, category configuration | Budget management system |
| 10-11 | Expense & income tracking modules | Transaction recording |
| 12 | Financial calculations module (taxes, interest, etc.) | Calculation engine |
| 13-14 | Dashboard with overview metrics | Main dashboard page |

**Objectives:**
- ✅ Implement budget management
- ✅ Build expense/income tracking
- ✅ Create calculation engine
- ✅ Build dashboard interface

---

### 📈 Week 3: Analytics (Days 15-21)

| Day | Task | Deliverable |
|-----|------|-------------|
| 15-17 | Chart generation (Matplotlib, Plotly), trend analysis | Analytics module |
| 18 | Budget vs actual comparison reports | Comparison analytics |
| 19 | Savings goals module with progress tracking | Goals management |
| 20-21 | Spending pattern analysis, anomaly detection | Advanced analytics |

**Objectives:**
- ✅ Implement data visualization
- ✅ Create analytics dashboards
- ✅ Build goals tracking system
- ✅ Add pattern analysis

---

### 🚀 Week 4: Advanced Features & Polish (Days 22-30)

| Day | Task | Deliverable |
|-----|------|-------------|
| 22-23 | PDF report generation, Excel export | Report generation |
| 24 | Bill reminder system | Notification system |
| 25 | Receipt OCR scanning integration | OCR module |
| 26 | Bank CSV import functionality | CSV importer |
| 27-28 | Comprehensive testing, bug fixes | Test suite |
| 29-30 | Documentation, deployment prep, final polish | Production-ready app |

**Objectives:**
- ✅ Implement report generation
- ✅ Add OCR functionality
- ✅ Build CSV import system
- ✅ Complete testing
- ✅ Deploy to production

---

## 📖 Usage Guide

### Dashboard Overview

The dashboard serves as your financial command center, displaying:

- **Monthly Summary** - Total income, expenses, and net balance
- **Budget Status** - Visual progress on each budget category
- **Recent Transactions** - Latest 10 transactions with filters
- **Upcoming Bills** - Reminders for scheduled payments
- **Financial Health Score** - Overall financial wellness indicator

### Adding Transactions

#### Method 1: Manual Entry

1. Navigate to "Add Expense" or "Add Income"
2. Select transaction date
3. Choose category
4. Enter amount
5. Add optional description and tags
6. Click "Save"

#### Method 2: Receipt Scanning

1. Go to "Import Data" → "Scan Receipt"
2. Upload receipt image
3. System auto-extracts amount and date using OCR
4. Review and confirm category
5. Click "Save"

#### Method 3: Bank Import

1. Go to "Import Data" → "Import Bank CSV"
2. Download transactions from your bank
3. Select bank format from dropdown
4. Upload CSV file
5. Review transaction list
6. Click "Import All" or select individual transactions

### Creating a Budget

1. Navigate to "Settings" → "Budget Configuration"
2. Click "Create New Budget"
3. For each category, enter:
   - Category name
   - Monthly limit
   - Alert threshold (%)
4. Review total allocation (recommended: don't exceed 100%)
5. Click "Save Budget"

### Managing Debt

1. Go to "Debts" section
2. Click "Add New Loan"
3. Enter loan details:
   - Creditor name
   - Original amount
   - Interest rate
   - Monthly payment
   - Expected payoff date
4. System calculates remaining payoff term
5. Track payments automatically

### Setting Savings Goals

1. Navigate to "Goals" section
2. Click "Create Goal"
3. Set goal parameters:
   - Goal name and description
   - Target amount
   - Deadline date
   - Auto-savings amount (monthly)
4. System predicts achievement date
5. View progress on dashboard

### Generating Reports

**Monthly Report:**
```
Reports → Monthly → Select Month → PDF/Excel → Download
```

**Yearly Tax Summary:**
```
Reports → Tax Summary → Select Year → PDF → Download
```

**Custom Report:**
```
Reports → Custom → Select Date Range → Choose Metrics → Export
```

---

## 🗄️ Database Schema

### Core Tables

#### **Users Table**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### **Categories Table**
```sql
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    icon VARCHAR(50),
    color VARCHAR(10),
    type VARCHAR(20),  -- 'expense' or 'income'
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

#### **Expenses Table**
```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    description VARCHAR(500),
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

#### **Income Table**
```sql
CREATE TABLE income (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    description VARCHAR(500),
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

#### **Budget Table**
```sql
CREATE TABLE budgets (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    category_id INTEGER,
    monthly_limit DECIMAL(12, 2) NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

#### **Goals Table**
```sql
CREATE TABLE goals (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    target_amount DECIMAL(12, 2) NOT NULL,
    current_amount DECIMAL(12, 2) DEFAULT 0,
    deadline DATE NOT NULL,
    priority VARCHAR(20),  -- 'high', 'medium', 'low'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

#### **Debts Table**
```sql
CREATE TABLE debts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    creditor VARCHAR(255) NOT NULL,
    original_amount DECIMAL(12, 2) NOT NULL,
    remaining_amount DECIMAL(12, 2) NOT NULL,
    interest_rate DECIMAL(5, 2) NOT NULL,
    monthly_payment DECIMAL(12, 2) NOT NULL,
    start_date DATE NOT NULL,
    expected_payoff_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

#### **Recurring Transactions Table**
```sql
CREATE TABLE recurring (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    frequency VARCHAR(20),  -- 'daily', 'weekly', 'monthly', 'yearly'
    start_date DATE NOT NULL,
    end_date DATE,
    description VARCHAR(500),
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

### Key Relationships

```
Users (1) ─── (*) Expenses
Users (1) ─── (*) Income
Users (1) ─── (*) Budgets
Users (1) ─── (*) Goals
Users (1) ─── (*) Debts
Users (1) ─── (*) Categories
Users (1) ─── (*) Recurring

Categories (*) ─── (1) Expenses
Categories (*) ─── (1) Income
Categories (*) ─── (1) Budgets
Categories (*) ─── (1) Recurring
```

---

## 🤝 Contributing

We welcome contributions from the community! Whether it's bug reports, feature requests, or code improvements, your help makes this project better.

### Getting Started

1. **Fork the Repository** - Click the fork button on GitHub
2. **Clone Your Fork** - `git clone https://github.com/yourusername/personal-finance-manager.git`
3. **Create a Feature Branch** - `git checkout -b feature/your-feature-name`
4. **Make Your Changes** - Implement your feature or fix
5. **Commit Changes** - `git commit -m "Add: Brief description of changes"`
6. **Push to Fork** - `git push origin feature/your-feature-name`
7. **Create Pull Request** - Submit PR with detailed description

### Code Style Guidelines

We follow [PEP 8](https://pep8.org/) style guidelines with some additions:

```python
# Use type hints where possible
def calculate_budget_remaining(budget_id: int, user_id: int) -> Dict[str, float]:
    """
    Calculate remaining budget for a specific category.
    
    Args:
        budget_id: The ID of the budget
        user_id: The ID of the user
        
    Returns:
        Dictionary with remaining amount and percentage
    """
    pass

# Use descriptive variable names
total_monthly_expenses = sum(expense.amount for expense in monthly_expenses)

# Include docstrings for all functions
# Comment complex logic
# Keep functions focused and single-responsibility
```

### Pull Request Process

1. **Update Documentation** - Update README and relevant docs
2. **Add Tests** - Include unit tests for new functionality
3. **Run Tests** - Ensure all tests pass: `pytest`
4. **Code Review** - Wait for maintainer review
5. **Make Revisions** - Address any reviewer comments
6. **Merge** - PR will be merged once approved

### Reporting Bugs

When reporting bugs, please include:

- **Description** - Clear explanation of the issue
- **Steps to Reproduce** - How to replicate the problem
- **Expected Behavior** - What should happen
- **Actual Behavior** - What actually happens
- **Environment** - Python version, OS, dependencies
- **Screenshots** - If applicable

**Create an issue:** [GitHub Issues](https://github.com/yourusername/personal-finance-manager/issues)

---

## 🗓️ Roadmap

### Phase 2 (6 months)
- [ ] Multi-currency support with live exchange rates
- [ ] Mobile app version (React Native)
- [ ] AI-powered financial advice engine
- [ ] Investment portfolio tracking
- [ ] Tax optimization recommendations
- [ ] Advanced budget forecasting
- [ ] Smartphone push notifications
- [ ] Dark mode UI theme

### Phase 3 (12 months)
- [ ] Real-time bank feed integration
- [ ] Cryptocurrency tracking
- [ ] Retirement planning calculator
- [ ] Credit score monitoring
- [ ] Insurance recommendations
- [ ] API for third-party integrations
- [ ] Social features (budget comparisons, tips sharing)
- [ ] Voice-activated transaction entry

### Community Suggestions
- Help us prioritize! Open an issue with your feature requests

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🆘 Support

Need help? We're here for you!

### Documentation
- 📚 **Full Documentation** - [Complete guides and tutorials](https://docs.example.com)
- 💡 **FAQ** - Answers to common questions
- 🎓 **Video Tutorials** - Step-by-step video guides

### Getting Help

1. **Check the FAQ** - Your question might already be answered
2. **Search Issues** - Look for similar issues in [GitHub Issues](https://github.com/yourusername/personal-finance-manager/issues)
3. **Create an Issue** - If you can't find an answer, open a new issue
4. **Discussion Board** - Join [GitHub Discussions](https://github.com/yourusername/personal-finance-manager/discussions)

### Contact

- 📧 **Email** - support@personfincancemamager.dev
- 💬 **Discord** - Join our [Discord Community](https://discord.gg/yourserver)
- 🐦 **Twitter** - Follow [@PersonalFinMgr](https://twitter.com/yourhandle)

---

## 🙏 Acknowledgments

### Built With

- [Streamlit](https://streamlit.io/) - For the amazing web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Powerful ORM
- [Plotly](https://plotly.com/) - Interactive visualizations
- [ReportLab](https://www.reportlab.com/) - PDF generation
- [pytesseract](https://github.com/madmaze/pytesseract) - OCR capabilities
- [pandas](https://pandas.pydata.org/) - Data analysis

### Contributors

Special thanks to all contributors who have helped make this project better!

- [@contributor1](https://github.com/contributor1) - Feature X
- [@contributor2](https://github.com/contributor2) - Bug fix Y
- [@contributor3](https://github.com/contributor3) - Documentation

### Inspiration

This project was inspired by the need for a simple, powerful, and privacy-aware personal finance management system.

---

## 📊 Project Stats

- 📦 **Total Dependencies**: 12 core packages
- 🧪 **Test Coverage**: Aiming for 80%+
- 📝 **Documentation**: Continuously updated
- 🐛 **Active Development**: Yes

---

<div align="center">

### ⭐ If you find this project helpful, please consider giving it a star!

Made with ❤️ by the Personal Finance Manager Community

[Top ↑](#-personal-finance-manager)

</div>
