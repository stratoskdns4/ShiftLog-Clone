import tkinter as tk
from tkinter.messagebox import showerror
from db import Event
from prom import Error

from constants import LABEL_FONT


class EditPopFrame(tk.Frame):

    def __init__(self, root, event_object, **options):
        super().__init__(root, **options)

        self.root = root
        self.event_object = event_object

        self.title_label = tk.Label(self, text="Επεξεργασία", font=LABEL_FONT, justify=tk.LEFT)
        self.title_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.employee_name_label = tk.Label(self, text="Όνομα Υπαλλήλου", anchor=tk.NW)
        self.employee_name_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.employee_name_entry = tk.Entry(self)
        self.employee_name_entry.insert(tk.END, self.event_object.employee_name)
        self.employee_name_entry.pack(padx=5, pady=5, anchor=tk.NW)

        self.event_result_label = tk.Label(self, text="Αποτέλεσμα", justify=tk.LEFT)
        self.event_result_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.event_result_entry = tk.Entry(self)
        self.event_result_entry.insert(tk.END, self.event_object.event_result)
        self.event_result_entry.pack(padx=5, pady=5, anchor=tk.NW)  

        self.event_description_label = tk.Label(self, text="Περιγραφή", justify=tk.LEFT)
        self.event_description_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.event_description_text =tk.Text(self, height=3)
        self.event_description_text.insert(tk.END, self.event_object.event_description)
        self.event_description_text.pack(padx=5, pady=5, fill=tk.X, anchor=tk.NW)

        self.update_button = tk.Button(self, text="Ενημέρωση", command=self.update_record)
        self.update_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=5, pady=5)

        
    def update_record(self):
        self.event_object.employee_name = self.employee_name_entry.get()
        self.event_object.event_result = self.event_result_entry.get()
        self.event_object.event_description = self.event_description_text.get("1.0", tk.END)

        try:
            self.event_object.save()
            self.root.destroy()
        except Error as er:
            showerror("Σφάλμα", "Σφάλμα κατά την ενημέρωση της εγγραφής")







