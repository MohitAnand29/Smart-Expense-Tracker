# 💰 Smart Expense Tracker

A CLI-based Smart Expense Tracker built using Python and SQLite.  
This application allows users to manage daily expenses, set monthly budgets, and generate analytics reports with visual charts.

---

## 🚀 Features

### 👤 User Authentication
- Register new users
- Secure login system
- User-specific expense tracking

### 💳 Expense Management
- Add expenses with category, date, and description
- View all expenses
- Filter expenses by category
- Delete expenses
- Monthly expense filtering

### 📊 Budget Management
- Set monthly budget
- Track total spending
- Budget remaining calculation
- Warning alerts when exceeding or approaching limit

### 📈 Analytics & Reports
- Total spending summary
- Transaction count
- Category-wise expense distribution (Pie Chart)
- Monthly expense comparison (Bar Chart)
- Charts saved as PNG files

---

## 🛠 Tech Stack

- **Python 3**
- **SQLite** (Database)
- **Matplotlib** (Data Visualization)
- **Tabulate** (CLI Table Formatting)

---

## 📂 Project Structure
SmartExpenseTracker/
│
├── main.py # CLI interface and menu handling
├── database.py # Database connection and table initialization
├── models.py # Business logic (User, Expense, Budget)
├── analytics.py # Data analysis and chart generation
├── utils.py # Helper functions
├── requirements.txt # Project dependencies
└── README.md


---

## 🗄 Database Design

### Users
- id (Primary Key)
- username (Unique)
- password

### Expenses
- id (Primary Key)
- user_id (Foreign Key)
- amount
- category
- date
- description

### Budgets
- id (Primary Key)
- user_id (Foreign Key)
- month
- amount

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/MohitAnand29/Smart-Expense-Tracker.git
cd Smart-Expense-Tracker
python -m venv venv
venv\Scripts\activate   # Windows


---

# 🔥 This README Makes Your Repo Look:

✔ Structured  
✔ Professional  
✔ Recruiter-ready  
✔ Not beginner-level  

---

Now next step:

Go to your repo → Edit README → Paste this → Commit changes.

After that tell me…

Do you want to:
1️⃣ Upgrade security  
2️⃣ Convert to Flask Web App  
3️⃣ Start a new advanced project  

Your level is increasing now 🚀


