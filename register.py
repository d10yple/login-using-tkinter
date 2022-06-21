from clickable_label import closeWindowLabel
from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk
from smart_entry import SmartEntry

class Register(Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.title('Register to foobar')
        self.resizable(0, 0)
        self.geometry(f"290x430+{int(Toplevel.winfo_screenwidth(self)//2.4)}+{int(Toplevel.winfo_screenheight(self)//3.5)}")
        self.logo_image = ImageTk.PhotoImage(Image.open('images/logo.png').resize((200, 150)))
        self.logo_label = Label(self, image=self.logo_image)
        self.logo_label.place(x=40, y=0)
        self.title_label = Label(self, text="Register", font=('arial', 20))
        self.title_label.place(x=100, y=150)
        self.subtitle_label = Label(self, text="Enter your informations", fg="#C2C2C2")
        self.subtitle_label.place(x=60, y=177)
        self.email_entry = SmartEntry(self, text="Email here", font=('Arial', 17))
        self.email_entry.place(x=35, y=215)
        self.password_entry = SmartEntry(self, text="Password", font=('Arial', 17), show="*")
        self.password_entry.place(x=35, y=250)
        self.repeat_password_label = Label(self, text="Repeat your password below:")
        self.repeat_password_label.place(x=35, y=290)
        self.password_repeat_entry = SmartEntry(self, text="Password", font=('Arial', 17), show="*")
        self.password_repeat_entry.place(x=35, y=315)
        self.register_button = Button(self, text="Register")
        self.register_button.place(x=160, y=350)
        self.register_close_label = closeWindowLabel(self, text="I have an account!", fg="#C2C2C2")
        self.register_close_label.place(x=35, y=353)