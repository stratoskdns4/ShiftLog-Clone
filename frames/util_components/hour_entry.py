import tkinter as tk
import datetime

class HourEntry(tk.Entry):

    def __init__(self, root, **options):
        super().__init__(root, **options)
        self.bind('<Visibility>', self.update)
    

    def update(self, evt=None):
        self.delete(0, tk.END)
        self.insert(0, datetime.datetime.now().strftime('%H:%M'))