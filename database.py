FILE = "/Users/joshuawhite-labbe/Documents/GitHub/python/finances.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as ft:
            return json.load(ft)
    else:
        return {
            "salary": 0,
            "expenses": []
        }

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
