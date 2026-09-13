from database import load_data
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt

def get_expenses(timeframe):
    data = load_data()
    expenses = data["expenses"]
    filtered = []
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    for expense in expenses:
        expense_date = datetime.strptime(expense["date"], "%d/%m/%Y").date()
        if timeframe == "a":
            filtered.append(expense)
        elif timeframe == "m":
            if (
                expense_date.month == today.month
                and expense_date.year == today.year
            ):
                filtered.append(expense)
        elif timeframe == "w":
            if start_of_week <= expense_date <= end_of_week:
                filtered.append(expense)
        elif timeframe == "t":
            if expense_date == today:
                filtered.append(expense)
    return filtered

def total_money(timeframe):
    expenses = get_expenses(timeframe)
    return sum(
        expense["amount"]
        for expense in expenses
    )

def largest(timeframe):
    expenses = get_expenses(timeframe)
    if not expenses:
        return None
    return max(expenses,key=lambda expense: expense["amount"])

def total_categories(timeframe):
    expenses = get_expenses(timeframe)
    totals = {}
    for expense in expenses:
        category = expense["category"]
        if category not in totals:
            totals[category] = 0
        totals[category] += expense["amount"]
    return totals

def biggestc(timeframe):
    totals = total_categories(timeframe)
    if not totals:
        return None
    return max(totals,key=totals.get)

def graph(timeframe):
    totals = total_categories(timeframe)
    if not totals:
        print("No expenses to display.")
        return
    categories = list(totals.keys())
    amounts = list(totals.values())

    plt.figure(figsize=(8,5))
    plt.bar(categories, amounts, width=0.6)
    plt.title("Spending by category")
    plt.xlabel("Category")
    plt.ylabel("Amount (£)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()