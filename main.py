from datetime import datetime, date
from database import load_data, save_data
from expenses import add, remove, modify, search, namemake, view
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

#######################################################################################################################################################################################################################################################
## All functions
#######################################################################################################################################################################################################################################################

while True:
    first_menu = input("What are we doing today? (Manage expenses (e)/ Manage money (m) / Statistics (s) / Quit (q)) ")
    if first_menu == "e":
        second_menu = input("Add expense (n) / Delete expense (d) / Modify expense (m) / Search for expense (s) / View all expenses (v) ")
        action = second_menu

    elif first_menu == "m":
        second_menu = input("View money left (l) / Add money (a) / Modify salary (ms) ")
        action = second_menu

    elif first_menu == "s":
        action = "stats"

    if action == "n":
        name = input("What is the name of your expense? ")
        category = input("What is the category of your expense? ")
        name = namemake(name, expenses)
        amount = float(input("What is the amount of your expense? "))
        date = input("What is the date of your expense? (dd/mm/yyyy) ")
        add(name, category, date, amount)

    elif action == "d":
            name = input("What is the name of the expense you would like to delete?")
            remove(name)

    elif action == "m":
        name = input("What is the name of the expense you want to modify?")
        modify(name)
    
    elif action == "s":
        name = input("What is the name of the expense you want to search for?")
        search(name)

    elif action == "v":
        view()
    
    elif action == "l":
        print ("You have", money, "pounds left this month.")
    
    elif action == "a":
        amount_added = float(input("How much money do you want to add? "))
        money += amount_added
        print("You have added", amount_added, "pounds. You have", money, "pounds left this month.")

    elif action == "ms":
        salary = float(input("What is your new monthly salary?"))
        data["salary"] = salary
        save_data(data)
        print("Your new monthly salary is now", salary, "pounds.")

    elif action == "stats":
        total_spent = total_money()
        largest_expense = largest()
        biggest_category = biggestc()
        print("You've spent a total of", total_spent, "this month.")
        print("Your largest expense was", largest_expense,".")
        print("The category in which you spent the most money is", biggest_category, ".")
        graph()

    elif action == "q":
        print("Thank you for using our application. Have a nice day!")
        break

    else:
        print("Invalid action. Please try again.")
