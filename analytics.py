import matplotlib.pyplot as plt
from models import Expense
import os

def generate_category_pie_chart(user_id):
    """Generates a pie chart of expenses by category for the current user."""
    expenses = Expense.get_expenses(user_id)
    if not expenses:
        return "No expenses found to generate chart."

    category_totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        category_totals[category] = category_totals.get(category, 0) + amount

    labels = list(category_totals.keys())
    values = list(category_totals.values())

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category')
    
    filename = f"category_pie_chart_user_{user_id}.png"
    plt.savefig(filename)
    plt.close()
    return f"Chart saved as {filename}"

def generate_monthly_bar_chart(user_id):
    """Generates a bar chart of monthly expenses."""
    expenses = Expense.get_expenses(user_id)
    if not expenses:
        return "No expenses found to generate chart."

    monthly_totals = {}
    for expense in expenses:
        # Date is YYYY-MM-DD, slice to get YYYY-MM
        month = expense['date'][:7]
        amount = expense['amount']
        monthly_totals[month] = monthly_totals.get(month, 0) + amount

    # Sort by month
    sorted_months = sorted(monthly_totals.keys())
    values = [monthly_totals[m] for m in sorted_months]

    plt.figure(figsize=(10, 6))
    plt.bar(sorted_months, values, color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Total Amount')
    plt.title('Monthly Expenses')
    plt.xticks(rotation=45)
    plt.tight_layout()

    filename = f"monthly_bar_chart_user_{user_id}.png"
    plt.savefig(filename)
    plt.close()
    return f"Chart saved as {filename}"

def get_summary_stats(user_id):
    """Returns a dictionary of summary statistics."""
    expenses = Expense.get_expenses(user_id)
    total_spent = sum(e['amount'] for e in expenses)
    count = len(expenses)
    
    return {
        "total_spent": total_spent,
        "transaction_count": count
    }
