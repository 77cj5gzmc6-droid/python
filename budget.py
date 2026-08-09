from database import load_data, save_data
from statistics import total_categories

def set_budget():
    data = load_data()
    budgets = data["budgets"]
    category = input("What category is your budget for?")
    budget_amount = float(input(f"What's the budget for {category}? "))
    budgets[category] = budget_amount
    data["budgets"] = budgets
    save_data(data)
    print("Your budget for", category, "has been set to", budget_amount, "pounds.")

def view_budgets():
    data = load_data()
    budgets = data["budgets"]
    if not budgets:
        print("No budgets have been set.")
        return
    print("\nYour budgets:")
    print("-" * 75)
    print(
        f"{'Category':<20}"
        f"{'Amount':>10}"
    )
    print("-" * 75)
    for category, amount in budgets.items():
        print(
            f"{category:<20}"
            f"{amount:>10}"
        )
    print("-" * 75)

def modify_budget(modb):
    data = load_data()
    budgets = data["budgets"]
    if not budgets:
        print("You don't have any budgets to modify.")
        return
    category = modb
    newb = float(input(f"What's the new budget for {category} ? "))
    budgets[category] = newb
    data["budgets"] = budgets
    save_data(data)
    print("Your budget for", category, "has been set.")

def delete_budget(delb):
    data = load_data()
    budgets = data["budgets"]
    if not budgets:
        print("You don't have any budgets to delete.")
        return
    category = delb
    budgets.pop(delb)
    data["budgets"] = budgets
    save_data(data)
    print("Your budget for", category, "has been deleted.")