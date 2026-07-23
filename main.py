from datetime import datetime, date
import json
import os
from database import load_data, save_data

today = datetime.now()
print("Welcome ! Today is", today.strftime("%d/%m/%Y"))

data = load_data()
expenses = data["expenses"]

while True:
  print("""
  1. Add expense
  2. Statistics (coming soon)
  3. Exit
  """)
  choice=input("> ")

if choice=="1":
  expenses = add_expense(expenses)
  data["expenses"] = expenses
  save_data(data)

elif choice=="3":
  break
