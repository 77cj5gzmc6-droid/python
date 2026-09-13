import json
import os

FILE = os.path.join(os.path.dirname(__file__), "finances.json")

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as ft:
            return json.load(ft)
    else:
        return {
            "salary": 0,
            "payday": 0,
            "budgets": {},
            "expenses": [],
            "last_opened": "",
            "last_payday": "",
            "money": 0
        }

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)