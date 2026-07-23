from datetime import datetime, date
from database import load_data, save_data
from expenses import money, expenses, add, remove

#########################
## Welcome
#########################

today = datetime.now()
print("Welcome ! Today is", today.strftime("%d/%m/%Y"))

data = load_data()
expenses = data["expenses"]

########################
## All functions
########################

while True:
    action = input("What would you like to do? (New expense (n) / Delete an expense (d) / Add money (a) / Modify an expense (me) / View my expenses (v) / Search for an expense (s) / Check remaining (re) / Modify my monthly salary (ms) / Quit (q)")
    
    if action == "n":
        name = input("What is the name of your expense? ")
        category = input("What is the category of your expense? ")
        date = input("What is the date of your expense? (dd/mm/yyyy) ")
        amount = float(input("What is the amount of your expense? "))
        add(name, category, date, amount)

    elif action == "d":
            name = input("What is the name of the expense you would like to delete?")
            remove(name)

    elif action == "v":
        print("Here is your list of expenses:")
        for expense in expenses:
            print(expense)
    
    elif action == "re":
        print ("You have", money, "pounds left this month.")
    
    elif action == "ms":
        salary = float(input("What is your new monthly salary?"))
        data["salary"] = salary
        save_data(data)
        print("Your new monthly salary is now", salary, "pounds.")
    
    elif action == "q":
        print("Thank you for using our application. Have a nice day!")
        break
        
    elif action == "me":
        name = input("What is the name of the expense you want to modify?")
        expense_found = False
        for expense in expenses:
            if expense["name"] == name:
                new_category = input("What is the new category of your expense? ")
                if new_category == "m":
                    new_category = expense["category"]
                new_name = input("What is the new name of your expense? Beware, it cannot be repeated ")
                if new_name == "m":
                    new_name = expense["name"]
                new_amount = float(input("What is the new amount of your expense? Press 0 if it's the same amount"))
                if new_amount == 0:
                    new_amount = expense["amount"]
                new_date = input("What is the new date of your expense? (dd/mm/yyyy) ")
                if new_date == "m":
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

    elif action == "s":
        name = input("What is the name of the expense you want to search for?")
        expense_found = False
        for expense in expenses:
            if expense["name"] == name:
                print("Expense found. Name =", expense["name"], "Category =", expense["category"], "Amount =", expense["amount"], "Date =", expense["date"])
                expense_found = True
                break
        if not expense_found:
                print("No results found.")

    elif action == "a":
        amount_added = float(input("How much money do you want to add? "))
        money += amount_added
        print("You have added", amount_added, "pounds. You have", money, "pounds left this month.")
  
    elif action == "md":
        name = input("What is the name of the expense you want to modify?")
        expense_found = False
        for expense in expenses:
            if expense["name"] == name:
                new_category = input("What is the new category of your expense? ")
                if new_category == "m":
                    new_category = expense["category"]
                new_name = input("What is the new name of your expense? Beware, it cannot be repeated ")
                if new_name == "m":
                    new_name = expense["name"]
                new_amount = float(input("What is the new amount of your expense? Press 0 if it's the same amount"))
                if new_amount == 0:
                    new_amount = expense["amount"]
                new_date = input("What is the new date of your expense? (dd/mm/yyyy) ")
                if new_date == "m":
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

    elif action == "r":
        name = input("What is the name of the expense you want to search for?")
        expense_found = False
        for expense in expenses:
            if expense["name"] == name:
                print("Expense found. Name =", expense["name"], "Category =", expense["category"], "Amount =", expense["amount"], "Date =", expense["date"])
                expense_found = True
                break
        if not expense_found:
                print("No results found.")

    elif action == "a":
        amount_added = float(input("How much money do you want to add? "))
        money += amount_added
        print("You have added", amount_added, "pounds. You have", money, "pounds left this month.")

    else:
        print("Invalid action. Please try again.")
