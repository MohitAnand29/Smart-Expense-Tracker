import sys
from models import User, Expense, Budget
from database import init_db
from analytics import generate_category_pie_chart, generate_monthly_bar_chart, get_summary_stats
from utils import clear_screen, validate_date, get_current_date, get_current_month
try:
    from tabulate import tabulate
except ImportError:
    tabulate = None

CURRENT_USER_ID = None

def print_table(data, headers):
    if tabulate:
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        # Fallback if tabulate is not installed
        print(" | ".join(headers))
        print("-" * 30)
        for row in data:
            print(" | ".join(map(str, row)))

def login_menu():
    global CURRENT_USER_ID
    while True:
        print("\n=== Smart Expense Tracker ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            user_id = User.login(username, password)
            if user_id:
                CURRENT_USER_ID = user_id
                print("Login successful!")
                return
            else:
                print("Invalid credentials.")
        elif choice == '2':
            username = input("New Username: ")
            password = input("New Password: ")
            if User.create_user(username, password):
                print("Registration successful! Please login.")
            else:
                print("Username already exists or error occurred.")
        elif choice == '3':
            sys.exit()
        else:
            print("Invalid option.")

def expense_menu():
    while True:
        print("\n--- Expense Management ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Delete Expense")
        print("5. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            amount = float(input("Amount: "))
            category = input("Category (Food, Travel, Bills, etc.): ")
            date = input(f"Date (YYYY-MM-DD) [default: {get_current_date()}]: ") or get_current_date()
            if not validate_date(date):
                print("Invalid date format.")
                continue
            description = input("Description: ")
            Expense.add_expense(CURRENT_USER_ID, amount, category, date, description)
            print("Expense added!")

        elif choice == '2':
            expenses = Expense.get_expenses(CURRENT_USER_ID)
            if expenses:
                data = [[e['id'], e['date'], e['category'], e['amount'], e['description']] for e in expenses]
                print_table(data, ["ID", "Date", "Category", "Amount", "Description"])
            else:
                print("No expenses found.")

        elif choice == '3':
            category = input("Enter category to filter: ")
            expenses = Expense.get_expenses(CURRENT_USER_ID, filters={'category': category})
            if expenses:
                data = [[e['id'], e['date'], e['category'], e['amount'], e['description']] for e in expenses]
                print_table(data, ["ID", "Date", "Category", "Amount", "Description"])
            else:
                print("No expenses found in this category.")
        
        elif choice == '4':
            expense_id = input("Enter Expense ID to delete: ")
            Expense.delete_expense(expense_id)
            print("Expense deleted (if it existed).")

        elif choice == '5':
            break

def budget_menu():
    while True:
        print("\n--- Budget Management ---")
        print("1. Set Monthly Budget")
        print("2. Check Budget Status")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            month = input(f"Month (YYYY-MM) [default: {get_current_month()}]: ") or get_current_month()
            amount = float(input("Budget Amount: "))
            Budget.set_budget(CURRENT_USER_ID, month, amount)
            print("Budget set!")

        elif choice == '2':
            month = input(f"Month (YYYY-MM) [default: {get_current_month()}]: ") or get_current_month()
            budget_amount = Budget.get_budget(CURRENT_USER_ID, month)
            
            # Calculate total expenses for that month
            expenses = Expense.get_expenses(CURRENT_USER_ID, filters={'month': month})
            total_spent = sum(e['amount'] for e in expenses)
            
            print(f"\nBudget for {month}: ${budget_amount:.2f}")
            print(f"Total Spent: ${total_spent:.2f}")
            print(f"Remaining: ${budget_amount - total_spent:.2f}")
            
            if total_spent > budget_amount:
                print("⚠️  WARNING: You have exceeded your budget!")
            elif total_spent > 0.8 * budget_amount:
                print("⚠️  Warning: You are approaching your budget limit.")

        elif choice == '3':
            break

def analytics_menu():
    print("\n--- Analytics & Reports ---")
    stats = get_summary_stats(CURRENT_USER_ID)
    print(f"Total Transactions: {stats['transaction_count']}")
    print(f"Total Spent: ${stats['total_spent']:.2f}")

    print("\nGenerating charts...")
    msg1 = generate_category_pie_chart(CURRENT_USER_ID)
    msg2 = generate_monthly_bar_chart(CURRENT_USER_ID)
    print(msg1)
    print(msg2)

def main_menu():
    while True:
        print(f"\n=== Main Menu ===")
        print("1. Manage Expenses")
        print("2. Manage Budget")
        print("3. View Analytics")
        print("4. Logout")
        choice = input("Select an option: ")

        if choice == '1':
            expense_menu()
        elif choice == '2':
            budget_menu()
        elif choice == '3':
            analytics_menu()
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    init_db()
    while True:
        login_menu()
        main_menu()
