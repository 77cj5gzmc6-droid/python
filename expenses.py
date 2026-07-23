from database import load_data, save_data
from datetime import datetime, date

data = load_data()
expenses = data["expenses"]

if data["salary"]==0:
    salary = float(input("What is your monthly salary? "))
    payday = float(input("What is your payday? Please enter the day of the month (eg. 1 if its on the first of the month)"))
    data["salary"] = salary
    data["payday"] = payday
    save_data(data)
else:
    salary = data["salary"]
    print("Your monthly salary is", salary, "pounds.")

if date.today().day == 1:
    print("It's the first day of the month! Your expenses have been reset.")
    expenses = []
    data["expenses"] = expenses
    save_data(data)

money = salary - sum(
    expense["amount"] for expense in expenses
)
print ( "You have", money, "pounds left this month.")

if date.today().day == data["payday"]:
    print("It's payday! Your salary has been added to your account.")
    money += salary
    print ( "You have", money, "pounds left this month.")

def add(name, category, date, amount):
    global money
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

def remove(name):
    global money
    for expense in expenses:
        if expense["name"] == name:
            expenses.remove(expense)
            data["expenses"] = expenses
            save_data(data)
            money += expense["amount"]
            print("Your expense has been removed successfully. You have", money, "pounds left this month.")
            return
        else:
            print("No expense found with that name.")

            
