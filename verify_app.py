import os
import sys
from database import init_db
from models import User, Expense, Budget
from analytics import generate_category_pie_chart, generate_monthly_bar_chart

def verify():
    print("Initializing Database...")
    init_db()

    print("\nTesting User Creation...")
    username = "testuser"
    password = "password123"
    
    # Clean up previous run if exists
    conn = User.create_user(username, password) # Returns True if created, False if exists
    
    user_id = User.login(username, password)
    assert user_id is not None, "Login failed"
    print(f"User '{username}' logged in with ID: {user_id}")

    print("\nTesting Expense Addition...")
    Expense.add_expense(user_id, 50.0, "Food", "2023-10-01", "Lunch")
    Expense.add_expense(user_id, 20.0, "Transport", "2023-10-02", "Bus")
    Expense.add_expense(user_id, 100.0, "Shopping", "2023-10-05", "Groceries")
    
    expenses = Expense.get_expenses(user_id)
    assert len(expenses) >= 3, "Expenses not added correctly"
    print(f"Added {len(expenses)} expenses.")

    print("\nTesting Budget...")
    Budget.set_budget(user_id, "2023-10", 500.0)
    budget = Budget.get_budget(user_id, "2023-10")
    assert budget == 500.0, "Budget not set correctly"
    print(f"Budget set for 2023-10: {budget}")

    print("\nTesting Analytics...")
    msg1 = generate_category_pie_chart(user_id)
    msg2 = generate_monthly_bar_chart(user_id)
    
    print(msg1)
    print(msg2)

    assert os.path.exists(f"category_pie_chart_user_{user_id}.png"), "Pie chart not created"
    assert os.path.exists(f"monthly_bar_chart_user_{user_id}.png"), "Bar chart not created"
    
    print("\nVerification Successful!")

if __name__ == "__main__":
    verify()
