from database import load_data, save_data
from datetime import datetime, date

def calculate_money(salary, expenses):
    data = load_data()
    expenses = data["expenses"]
    return salary - sum(expense["amount"] for expense in expenses)

def add(name, category, date, amount):
    data = load_data()
    expenses = data["expenses"]
    money = calculate_money(data["salary"], expenses)
    expense = {
        "name": name,
        "category": category,
        "date": date,
        "amount": amount
    }
    expenses.append(expense)
    data["expenses"] = expenses
    save_data(data)
    money -= amount
    print("Your expense has been added successfully. You have", money, "pounds left this month.")

def namemake(name,expenses):
    data = load_data()
    expenses = data["expenses"]
    counter = 1
    original_name = name
    existing_names = [expense["name"] for expense in expenses]
    while name in existing_names:
        name = original_name + " " + str(counter)
        counter += 1
    return name

def remove(name):
    data = load_data()
    expenses = data["expenses"]
    money = calculate_money(data["salary"], expenses)
    for expense in expenses:
        if expense["name"] == name:
            expenses.remove(expense)
            data["expenses"] = expenses
            save_data(data)
            money += expense["amount"]
            print("Your expense has been removed successfully. You have", money, "pounds left this month.")
            return
    print("No expense found with that name.")

def modify(name):
    data = load_data()
    expenses = data["expenses"]
    money = calculate_money(data["salary"], expenses)
    expense_found = False
    for expense in expenses:
        if expense["name"] == name:
            new_category = input("What is the new category of your expense? Press s if it's the same as before.")
            if new_category == "s":
                new_category = expense["category"]
            new_name = input("What is the new name of your expense? Press s if it's the same as before.")
            if new_name == "s":
                new_name = expense["name"]
            new_amount = float(input("What is the new amount of your expense? Press 0 if it's the same amount as before."))
            if new_amount == 0:
                new_amount = expense["amount"]
            new_date = input("What is the new date of your expense (DD/MM/YYYY)? Press s if it's the same as before. ")
            if new_date == "s":
                new_date = expense["date"]
            money += expense["amount"] - new_amount
            expense["category"] = new_category
            expense["name"] = new_name
            expense["amount"] = new_amount
            expense["date"] = new_date
            data["expenses"] = expenses
            save_data(data)
            print("The expense has been modified successfully. You have", money, "pounds left this month.")
            expense_found = True
            break
    if not expense_found:
        print("No expense found with that name.")

def search(name):
    data = load_data()
    expenses = data["expenses"]
    expense_found = False
    for expense in expenses:
        if expense["name"] == name:
            print("Expense found. Name =", expense["name"], "Category =", expense["category"], "Amount =", expense["amount"], "Date =", expense["date"])
            expense_found = True
            break
    if not expense_found:
        print("No results found.")

def view():
    data = load_data()
    expenses = data["expenses"]
    if not expenses:
        print("You have no expenses recorded.")
        return
    print("\nYour expenses:")
    print("-" * 75)
    print(
        f"{'Date':<12}"
        f"{'Name':<25}"
        f"{'Category':<20}"
        f"{'Amount':>10}"
    )
    print("-" * 75)
    for expense in expenses:
        print(
            f"{expense['date']:<12}"
            f"{expense['name']:<25}"
            f"{expense['category']:<20}"
            f"£{expense['amount']:>8.2f}"
        )
    print("-" * 75)