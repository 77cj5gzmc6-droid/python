def add_expense(expenses):
    category = input("Category: ")
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    date = input("Date (dd/mm/yyyy): ")
    expense = {
        "category": category,
        "name": name,
        "amount": amount,
        "date": date
    }
    expenses.append(expense)


def view_expenses(expenses):
    print("Expenses:\n")
    for expense in expenses:
        print(expense)

def delete_expense(expenses):
    name = input("Expense to delete: ")
    for expense in expenses:
        if expense["name"] == name:
            expenses.remove(expense)
            print("Expense deleted.")
            return
    print("Expense not found.")

def modify_expense(expenses):
    name = input("Expense to modify: ")
    for expense in expenses:
        if expense["name"] == name:
            category = input(
                f"Category ({expense['category']}): "
            )

            if category:
                expense["category"] = category

            new_name = input(
                f"Name ({expense['name']}): "
            )

            if new_name:
                expense["name"] = new_name

            amount = input(
                f"Amount ({expense['amount']}): "
            )

            if amount:
                expense["amount"] = float(amount)

            new_date = input(
                f"Date ({expense['date']}): "
            )

            if new_date:
                expense["date"] = new_date

            print("Expense updated.")

            return

    print("Expense not found.")


def search_expense(expenses):

    name = input("Expense name: ")

    for expense in expenses:

        if expense["name"] == name:

            print(expense)

            return

    print("Expense not found.")
