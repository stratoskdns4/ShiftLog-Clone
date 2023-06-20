import tkinter as tk
from login_controller import LoginController

class UsernameEntry(tk.Entry):

    def __init__(self, root, **options):
        super().__init__(root, **options)
        self.bind('<Visibility>', self.update)
    

    def update(self, evt=None):
        self.delete(0, tk.END)
        self.insert(0, LoginController().get_logged_in_user())