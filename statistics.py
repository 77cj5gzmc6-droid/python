from database import load_data
import matplotlib.pyplot as plt

data = load_data()
expenses = data["expenses"]

def largest():
  return max(expenses, key=lambda expense: expense["amount"])

def total():
  print("Youve spent a total of", sum(expense["amount"] for expense in expenses), "this month.")

def categories():
  totals = {}
  for expense in expenses:
    category = expense["category"]
    if category not in totals:
      totals[category] = 0
    totals[category] += expense["amount"]
  return totals

def biggestc():
  totals = category_totals()
  return max(totals, key=totals.get) 

def graph():
  totals = category_totals()
  categories = list(totals.keys())
  amounts = list(totals.values())
  plt.bar(categories, amounts)
  plt.title("Monthly spending by category")
  plt.xlabel("Category")
  plt.ylabel("Amount spent")
  plt.show()