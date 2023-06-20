import tkinter as tk
import tkcalendar
import datetime

class DateEntry(tkcalendar.DateEntry):

    def __init__(self, root, **options):
        super().__init__(root, **options)
        self.bind('<Visibility>', self.update)
    

    def update(self, evt=None):
        self.delete(0, tk.END)
        self.insert(0, datetime.datetime.now().strftime('%d/%m/%Y'))