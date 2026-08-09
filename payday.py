from datetime import date
from calendar import monthrange
from database import load_data, save_data


def get_payday_date(year, month, payday):
    last_day = monthrange(year, month)[1]
    day = min(payday, last_day)
    return date(year, month, day)


def check_paydays():
    data = load_data()
    salary = data["salary"]
    payday = int(data["payday"])
    today = date.today()
    last_payday_string = data.get("last_payday", "")

    if last_payday_string == "":
        print("No previous payday recorded.")
        return 0

    last_payday = date.fromisoformat(last_payday_string)
    missed_paydays = 0
    year = last_payday.year
    month = last_payday.month

    while True:

        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

        possible_payday = get_payday_date(year, month, payday)

        if possible_payday > today:
            break
        missed_paydays += 1

        if possible_payday == today:
            break

    if missed_paydays == 0:
        return 0
    money_added = salary * missed_paydays
    current_payday = get_payday_date(
        today.year,
        today.month,
        payday
    )

    if current_payday > today:
        if today.month == 1:
            previous_year = today.year - 1
            previous_month = 12
        else:
            previous_year = today.year
            previous_month = today.month - 1
        current_payday = get_payday_date(
            previous_year,
            previous_month,
            payday
        )

    data["last_payday"] = current_payday.isoformat()
    save_data(data)
    print(f"You missed {missed_paydays} payday(s).")
    print(f"{money_added:.2f} £ has been added to your account.")
    return money_added