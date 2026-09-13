import customtkinter as ctk

# Set global visual theme
ctk.set_appearance_mode("Dark")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"


class App(ctk.CTk):

  def __init__(self):
    super().__init__()

    # Configure main window
    self.title("Starter Dashboard")
    self.geometry("700x450")

    # Configure grid layout (1 row, 2 columns)
    self.grid_rowconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)

    # ------------------ SIDEBAR FRAME ------------------
    self.sidebar = ctk.CTkFrame(self, width=160, corner_radius=0)
    self.sidebar.grid(row=0, column=0, sticky="nsew")

    self.logo_label = ctk.CTkLabel(
        self.sidebar, text="My App", font=ctk.CTkFont(size=20, weight="bold")
    )
    self.logo_label.pack(padx=20, pady=(20, 10))

    self.btn_nav1 = ctk.CTkButton(
        self.sidebar, text="Home", command=self.nav_home
    )
    self.btn_nav1.pack(padx=20, pady=10)

    self.theme_switch = ctk.CTkSwitch(
        self.sidebar, text="Dark Mode", command=self.toggle_theme
    )
    self.theme_switch.pack(padx=20, pady=(40, 10), side="bottom")
    self.theme_switch.select()

    # ------------------ MAIN CONTENT FRAME ------------------
    self.main_frame = ctk.CTkFrame(self, corner_radius=10)
    self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    self.title_label = ctk.CTkLabel(
        self.main_frame,
        text="Welcome Back",
        font=ctk.CTkFont(size=24, weight="bold"),
    )
    self.title_label.pack(padx=20, pady=(20, 10))

    self.entry_input = ctk.CTkEntry(
        self.main_frame, placeholder_text="Type something here...", width=250
    )
    self.entry_input.pack(padx=20, pady=10)

    self.btn_action = ctk.CTkButton(
        self.main_frame, text="Submit", command=self.handle_submit
    )
    self.btn_action.pack(padx=20, pady=10)

    self.result_label = ctk.CTkLabel(self.main_frame, text="")
    self.result_label.pack(padx=20, pady=10)

  # ------------------ EVENT HANDLERS ------------------
  def handle_submit(self):
    user_text = self.entry_input.get()
    self.result_label.configure(text=f"You entered: {user_text}")

  def nav_home(self):
    self.result_label.configure(text="Navigated to Home")

  def toggle_theme(self):
    if self.theme_switch.get() == 1:
      ctk.set_appearance_mode("Dark")
    else:
      ctk.set_appearance_mode("Light")


if __name__ == "__main__":
  app = App()
  app.mainloop()