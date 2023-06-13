import tkinter as tk
from tkinter import ttk

from .constants import LABEL_FONT

from login_controller import LoginController

class LoginFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)
        
        self.title_label = tk.Label(self, text="Σύνδεση", font=LABEL_FONT)
        self.title_label.pack(fill=tk.X, pady=10, padx=5)

        self.message_label = tk.Label(self, text="", fg='red')
        self.message_label.pack(anchor=tk.W, pady=10, padx=5)

        self.username_label = tk.Label(self, text="Όνομα εργαζομένου")
        self.username_label.pack(anchor=tk.W, pady=10, padx=5)

        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.pack(anchor=tk.W, padx=10, pady=5)

        self.password_label = tk.Label(self, text='Κωδικός πρόσβασης')
        self.password_label.pack(anchor=tk.W, padx=10, pady=5)

        self.password_entry = tk.Entry(self, width=30, show='*')
        self.password_entry.pack(anchor=tk.W, padx=10, pady=5)

        self.submit_button = tk.Button(self, text='Σύνδεση', command=self.on_submit)
        self.submit_button.pack(anchor=tk.W, padx=10, pady=5)

    
    def on_submit(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # result = self.do_login(username, password)
        result = LoginController().do_login(username, password)
        if not result:
            self.show_error_message("Λάθος username η password!")



    def show_error_message(self, message):
        self.message_label.config(text=message)


    def hide_error_message(self):
        self.message_label.config(text="")

   

