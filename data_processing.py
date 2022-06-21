# -*- coding: utf-8 -*-

from json import load, dump
from datetime import datetime
from tkinter import messagebox

class DataProcessing:
    def __init__(self, data_path: str) -> None:
        try:
            self.data_path = data_path
            
            with open(self.data_path, 'r', encoding='utf-8') as data_file:
                self.data = load(data_file)['users']
                
        except FileNotFoundError:
            messagebox.showerror('Oops', 'Oops, data file cannot be found. Restart the program.')
        
    def log_user(self, email: str, password: str) -> bool:
        """_summary_

        Args:
            email (str): _description_
            password (str): _description_

        Returns:
            bool: _description_
        """
        try:
            for user in self.data:
                return True if user['email'] == email and user['password'] == password else False
        except AttributeError:
            # because self.data is not set
            pass
            
    def register_user(self, email: str, password: str) -> None:
        if not self.log_user(email, password):
            new_user = {
                "email": email,
                "password": password,
                "register_date": datetime.now().strftime("%d/%m/%Y")
            }
            
            self.data.append(new_user)
            self.save_data()
            
    def save_data(self) -> None:
        with open(self.data_path, 'w', encoding='utf-8') as data_file:
            dump(self.data, data_file, indent=4)
    
    