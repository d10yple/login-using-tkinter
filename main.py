# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Button, messagebox
from smart_entry import SmartEntry
from clickable_label import RegisterLabel
from PIL import Image, ImageTk
from hashlib import sha256
from data_processing import DataProcessing
from register import Register

user_data_path = "data/users.json"
        
class Application(Tk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title("Login to Foobar")
        self.resizable(0, 0)
        self.geometry(f"290x380+{int(Tk.winfo_screenwidth(self)//2.5)}+{int(Tk.winfo_screenheight(self)//3.9)}")
        self.logo_image = ImageTk.PhotoImage(Image.open('images/logo.png').resize((200, 150)))
        self.logo_label = Label(image=self.logo_image)
        self.logo_label.place(x=40, y=0)
        self.title_label = Label(text="Login to your account", font=('arial', 20))
        self.title_label.place(x=40, y=150)
        self.subtitle_label = Label(text="Please enter your creditentials to log-in", fg="#C2C2C2")
        self.subtitle_label.place(x=20, y=177)
        self.email_entry = SmartEntry(self, text="Email", font=('Arial', 17), fg="black")
        self.email_entry.place(x=35, y=215)
        self.password_entry = SmartEntry(self, text="Password", font=('Arial', 17), show="*", fg="black")
        self.password_entry.place(x=35, y=250)
        self.log_in_button = Button(self, text="Log in", command=lambda: self.log_in(self.email_entry.get(), sha256(self.password_entry.get().encode('utf-8')).hexdigest()))
        self.log_in_button.place(x=175, y=285)
        self.register_label = RegisterLabel(self, text="Or maybe register", fg="#C2C2C2")
        self.register_label.place(x=35, y=288)
        
    def log_in(self, email: str, password: str) -> None:
        data_processing = DataProcessing(data_path=user_data_path)
        if data_processing.log_user(email, password):
            messagebox.showerror(message=f"Welcome! {email}")
        else:
            self.email_entry.error()
            self.password_entry.error()
            # messagebox.showerror(message="Bad creditentials!")
        
    def pop_up_register(self) -> None:
        register = Register()
        register.mainloop()
        
if __name__ == "__main__":
    app = Application()
    app.mainloop()