import customtkinter as ctk
from database import load_data

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

      #Window title and size
        self.title("Finance Manager")
        self.geometry("1000x650")
        self.minsize(800,600)
        self.maxsize(1200,800)

      #Grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

      #Sidebar
        self.sidebar =ctk.CTkFrame(self)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

      #Main content
        self.logo = ctk.CTkLabel(self.sidebar, text="Finance Manager", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo.pack(padx=20, pady=(20, 10))

      #Navigation buttons
        self.dashboard_button = ctk.CTkButton(self.sidebar, text="Dashboard", command=self.show_dashboard)
        self.dashboard_button.pack(padx=20, pady=10, fill="x")
        self.expenses_button = ctk.CTkButton(self.sidebar, text="Expenses", command=self.show_expenses)
        self.expenses_button.pack(padx=20, pady=10, fill="x")
        self.budget_button = ctk.CTkButton(self.sidebar, text="Budget", command=self.show_budget)
        self.budget_button.pack(padx=20, pady=10, fill="x")
        self.statistics_button = ctk.CTkButton(self.sidebar, text="Statistics", command=self.show_statistics)
        self.statistics_button.pack(padx=20, pady=10, fill="x")

      #Theme toggle
        self.theme_toggle = ctk.CTkSwitch(self.sidebar, text="Dark Mode", command=self.toggle_theme)
        self.theme_toggle.pack(padx=20, pady=10)
        self.theme_toggle.select()

      #Main content frame
        self.main_content = ctk.CTkFrame(self, corner_radius=10)
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_content.grid_columnconfigure((0,1), weight=1)
        self.main_content.grid_rowconfigure(3, weight=1)
        self.show_dashboard()

  #Dashboard
    def show_dashboard(self):
        self.clear_main_content()
        data = load_data()
        money = data["money"]
        salary = data["salary"]
        payday = data["payday"]
        last_payday = data.get("last_payday", "N/A")
        if last_payday == "":
            last_payday = "N/A"

        dashboard_label = ctk.CTkLabel(self.main_content, text="Dashboard", font=ctk.CTkFont(size=20, weight="bold"))
        dashboard_label.grid(row=0, column=0, columnspan=2, pady=20)

        money_label = ctk.CTkLabel(self.main_content, text=f"Money left this month: {money:.2f} £", font=ctk.CTkFont(size=16))
        money_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        salary_label = ctk.CTkLabel(self.main_content, text=f"Monthly salary: {salary:.2f} £", font=ctk.CTkFont(size=16))
        salary_label.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        payday_label = ctk.CTkLabel(self.main_content, text=f"Payday: the {int(payday)} of the month", font=ctk.CTkFont(size=16))
        payday_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        last_payday_label = ctk.CTkLabel(self.main_content, text=f"Last payday: {last_payday}", font=ctk.CTkFont(size=16))
        last_payday_label.grid(row=2, column=1, padx=20, pady=10, sticky="w")

      #Balance
        balance_card = ctk.CTkFrame(self.main_content, corner_radius=10)
        balance_card.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

        balance_title = ctk.CTkLabel(balance_card, text="Balance", font=ctk.CTkFont(size=16, weight="bold"))
        balance_title.pack(padx=20, pady=10)

        balance = ctk.CTkLabel(balance_card, text=f"{money:.2f} £", font=ctk.CTkFont(size=20))
        balance.pack(padx=20, pady=10)

      #Salary
        salary_card = ctk.CTkFrame(self.main_content, corner_radius=10)
        salary_card.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")

        salary_title = ctk.CTkLabel(salary_card, text="Salary", font=ctk.CTkFont(size=16, weight="bold"))
        salary_title.pack(padx=20, pady=10)

        salary_amount = ctk.CTkLabel(salary_card, text=f"{salary:.2f} £", font=ctk.CTkFont(size=20))
        salary_amount.pack(padx=20, pady=10)

      #Recent expenses
        expenses_frame = ctk.CTkFrame(self.main_content, corner_radius=10)
        expenses_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        recent_title = ctk.CTkLabel(expenses_frame, text="Recent Expenses", font=ctk.CTkFont(size=16, weight="bold"))
        recent_title.pack(anchor="w", padx=20, pady=10)

        expenses = data["expenses"]

        for expense in expenses[-5:][::-1]:
            expense_label = ctk.CTkLabel(expenses_frame, text=f"{expense['date']} - {expense['name']} - {expense['category']} - {expense['amount']:.2f} £", font=ctk.CTkFont(size=14))
            expense_label.pack(anchor="w", padx=20, pady=5)

  #Expenses
    def show_expenses(self):
        self.clear_main_content()

        expenses_label = ctk.CTkLabel(self.main_content, text="Expenses", font=ctk.CTkFont(size=20, weight="bold"))
        expenses_label.pack(pady=20)

        data = load_data()
        expenses = data["expenses"]

        for expense in expenses:
            expense_label = ctk.CTkLabel(self.main_content, text=f"{expense['date']} - {expense['name']} - {expense['category']} - {expense['amount']:.2f} £", font=ctk.CTkFont(size=14))
            expense_label.pack(anchor="w", padx=20, pady=5)

  #Budget
    def show_budget(self):
        self.clear_main_content()

        budget_label = ctk.CTkLabel(self.main_content, text="Budget", font=ctk.CTkFont(size=20, weight="bold"))
        budget_label.pack(pady=20)

        data = load_data()
        budgets = data["budgets"]

        for category, amount in budgets.items():
            budget_item_label = ctk.CTkLabel(self.main_content, text=f"{category}: {amount:.2f} £", font=ctk.CTkFont(size=14))
            budget_item_label.pack(anchor="w", padx=20, pady=5)

  #Statistics
    def show_statistics(self):
        self.clear_main_content()

        statistics_label = ctk.CTkLabel(self.main_content, text="Statistics", font=ctk.CTkFont(size=20, weight="bold"))
        statistics_label.pack(pady=20)

  #Clear main content
    def clear_main_content(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

  #Theme toggle
    def toggle_theme(self):
        if self.theme_toggle.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

if __name__ == "__main__":
  app = App()
  app.mainloop()