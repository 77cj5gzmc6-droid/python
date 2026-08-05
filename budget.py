from database import load_data, save_data
from statistics import total_categories

data = load_data()
budgets = data["budgets"]

def set_budget():
    category = input("What category is your budget for?")
    budget_amount = float(input(f"What's the budget for {category}? "))
    budgets["category"] = float(budget_category)
    data["budgets"] = budgets
    save_data(data)
    print("Your budget for", category, "has been set to", budget\_amount, "pounds.")
