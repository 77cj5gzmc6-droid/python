from datetime import datetime, date
from database import load_data, save_data
from expenses import add, remove, modify, search, namemake, view
from budget import set_budget, view_budgets, modify_budget, delete_budget
from statistics import largest, total_money, total_categories, biggestc, graph

#######################################################################################################################################################################################################################################################
## Welcome and setup
#######################################################################################################################################################################################################################################################

today = datetime.now()
print("Welcome ! Today is", today.strftime("%d/%m/%Y"))

data = load_data()
expenses = data["expenses"]

if data["salary"]==0:
    salary = float(input("What is your monthly salary? "))
    payday = float(input("On what day of the month do you get paid? (Type 1 if its on the first of the month)"))
    data["salary"] = salary
    data["payday"] = payday
    save_data(data)
else:
    salary = data["salary"]
    print("Your monthly salary is", salary, "pounds.")

money = salary - sum(
    expense["amount"] for expense in expenses
)
print ( "You have", money, "pounds left this month.")

#######################################################################################################################################################################################################################################################
## All functions
#######################################################################################################################################################################################################################################################

while True:
    first_menu = input("What are we doing today? (Expenses (e)/ Money (m) / Budget (b) / Statistics (s) / Quit (q)) ")


    #Sub-menu


    if first_menu == "e":
        second_menu = input("New expense (n) / Delete expense (d) / Edit expense (e) / Search for expense (s) / View all expenses (ve) ")
        action = second_menu

    elif first_menu == "m":
        second_menu = input("View money left (l) / Add money (a) / Modify salary (ms)")
        action = second_menu

    elif first_menu == "b":
        second_menu = input("Set budget (b) / View budgets (vb) / Modify budget (mb) / Delete a budget (db) ")
        action = second_menu

    elif first_menu == "s":
        action = "stats"

    elif first_menu == "q":
        print("Thank you for using our application. Have a nice day!")
        break


    # Actions


    if action == "n":
        name = input("What is the name of your expense? ")
        category = input("What is the category of your expense? ")
        data = load_data()
        if category not in data["budgets"]:
            print("Warning: You have not set a budget for this category.")
        name = namemake(name, expenses)
        amount = float(input("What is the amount of your expense? "))
        if category in data["budgets"]:
            tcv = 0
            for expense in expenses:
                if expense["category"] == category:
                    tcv += expense["amount"]
            if tcv > data["budgets"][category]:
                print("Warning; you have exceeded your budget for this category. Your total spending for this category is", tcv, "pounds, while your budget is", data["budgets"][category], "pounds.")
        date = input("What is the date of your expense (DD/MM/YYYY)? Press enter if it's today. ")
        if date == "":
            date = datetime.now().strftime("%d/%m/%Y")
        add(name, category, date, amount)

    elif action == "d":
        data = load_data()
        expenses = data["expenses"]
        view()
        name = input("What is the name of the expense you would like to delete?")
        remove(name)

    elif action == "e":
        data = load_data()
        expenses = data["expenses"]
        view()
        name = input("What is the name of the expense you want to modify?")
        modify(name)
    
    elif action == "s":
        data = load_data()
        expenses = data["expenses"]
        name = input("What is the name of the expense you want to search for?")
        search(name)

    elif action == "ve":
        data = load_data()
        expenses = data["expenses"]
        view()
    
    elif action == "l":
        data = load_data()
        expenses = data["expenses"]
        print ("You have", money, "pounds left this month.")
    
    elif action == "a":
        data = load_data()
        expenses = data["expenses"]
        amount_added = float(input("How much money do you want to add? "))
        money += amount_added
        print("You have added", amount_added, "pounds. You have", money, "pounds left this month.")

    elif action == "ms":
        data = load_data()
        expenses = data["expenses"]
        salary = float(input("What is your new monthly salary?"))
        data["salary"] = salary
        save_data(data)
        print("Your new monthly salary is now", salary, "pounds.")

    elif action == "b":
        data = load_data()
        expenses = data["expenses"]
        set_budget()

    elif action == "mb":
        modb = input("Which budget would yu like to change?")
        modify_budget(modb)

    elif action == "db":
        delb = input("Which budget would you like to delete?")
        delete_budget(delb)

    elif action == "db":
        delb = input("Which budget would you like to delete?")
        delete_budget(delb)

    elif action == "vb":
        view_budgets()

    elif action == "stats":
        data = load_data()
        expenses = data["expenses"]
        timeframe = input("View all time (a) / View this month (m) / View this week (w) / View today (t) ")
        if timeframe not in ["a", "m", "w", "t"]:
            print("Invalid timeframe. Please try again.")
            continue
        total_spent = total_money(timeframe)
        largest_expense = largest(timeframe)
        biggest_category = biggestc(timeframe)
        print("You've spent a total of", total_spent, "pounds.")
        view()
        print("Your largest expense was '", largest_expense["name"], "' at", largest_expense["amount"], "pounds.")
        print("The category in which you spent the most money is", biggest_category, ".")
        graph(timeframe)

    else:
        print("Invalid action. Please try again.")
