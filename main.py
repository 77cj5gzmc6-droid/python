from datetime import datetime, date
import json
import os
from database import load_data, save_data

today = datetime.now()
print("Welcome ! Today is", today.strftime("%d/%m/%Y"))

data = load_data()
expenses = data["expenses"]
