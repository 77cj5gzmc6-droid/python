from database import load_data

data = load_data()
expenses = data["expenses"]

def largest_expense():
  return max(expenses, key=lambda expense: expense["amount"])

def total_spent():
  print("Youve spent a total of", sum(expense["amount"] for expense in expenses), "this month.")

def category_totals ():
  totals = {}
  for expense in expenses:
    category = expense["category"]
    if category not in totals:
      totals[category] = 0
    totals[category] += expense["amount"]
  return totals

def biggest_category():
  totals = category_totals()
  return max(totals, key=totals.get) 
