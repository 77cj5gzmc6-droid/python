from database import load_data, save_data
from statistics import total_categories

def set_budget():
    data = load_data()
    expenses = data["expenses"]
    category = input("What category is your budget for?")
    budget_amount = float(input(f"What's the budget for {category}? "))
    budgets[category] = budget_amount
    data["budgets"] = budgets
    save_data(data)
    print("Your budget for", category, "has been set to", budget_amount, "pounds.")
