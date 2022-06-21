from tkinter import Label

class ClickableLabel(Label):
    def __init__(self, master=None, text="Clickable Label", fg="#000000", font=('arial', 13, 'underline')) -> None:
        self.master = master
        super().__init__(master=master, text=text, fg=fg, font=font)
        self.bind('<Button-1>', self.click)
        
class RegisterLabel(ClickableLabel):
    def click(self, *args) -> None:
        self.master.pop_up_register()
        
class closeWindowLabel(ClickableLabel):
    def click(self, master=None, *args) -> None:
        self.master.destroy()