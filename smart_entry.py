from time import sleep
from tkinter import Entry

class SmartEntry(Entry):
    def __init__(self, master = None, text="Placeholder", font=('arial', 16), show=None, fg="white") -> None:
        super().__init__(master=master, font=font, show=show, fg=fg)
        self.text = text
        self.set_input()
        
    def set_input(self) -> None:
        self.insert('end', self.text)
        self.bind('<FocusIn>', self.focus_in)
        self.bind('<FocusOut>', self.focus_out)
        self['fg'] = "#C2C2C2"
        
    def focus_in(self, *args) -> None:
        self['fg'] = "#000000"
        if self.get() == self.text or self.get() == "":
            self.delete(0, 'end')
        
    def focus_out(self, *args) -> None:
        if self.get() == self.text or self.get() == "":
            self.delete(0, 'end')
            self.insert('end', self.text)
            self['fg'] = "#C2C2C2"
            
    def error(self) -> None:
        self['bg'] = 'red'
        self.after(2000, self.normalize)
        
    def normalize(self) -> None:
        self['bg'] = 'black'