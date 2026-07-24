from database import load_data
import matplotlib.pyplot as plt

data = load_data()
expenses = data["expenses"]

def total_money():
  return sum(expense["amount"] for expense in expenses)

def largest():
  return max(expenses, key=lambda expense: expense["amount"])

def total_categories():
  totals = {}
  for expense in expenses:
    category = expense["category"]
    if category not in totals:
      totals[category] = 0
    totals[category] += expense["amount"]
  return totals

def biggestc():
  totals = total_categories()
  return max(totals, key=totals.get) 

def graph():
  totals = total_categories()
  categories = list(totals.keys())
  amounts = list(totals.values())
  plt.figure(figsize=(8,5))
  plt.bar(categories, amounts, color=plt.cm.Set3.colors)
  plt.title("Monthly spending by category")
  plt.xlabel("Category")
  plt.ylabel("Amount (£)")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()