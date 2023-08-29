import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import datetime

from logic import add_break
from login_controller import LoginController
from .constants import LABEL_FONT

from .util_components import UsernameEntry, HourEntry, DateEntry
from third_party.tk_rich_editor import RichTextEditor

from .change_style import change_style

INFORMATION_TYPES = ("Βγήκα για διάλειμμα", "Γύρισα από διάλειμμα", 'Βγήκα για τσιγάρο', 'Γύρισα από τσιγάρο')


theme = {
    "font-color": "black",
    "empty-background" : {
        'bg':'lightgreen'
    },
    "filled-background": {
        'bg': 'lightgreen',
        'fg': 'black'
    }
}


class BreaksFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        # Place your wigdets here
        self.title_label = tk.Label(self, text="ΔΙΑΛΕΙΜΜΑΤΑ", font=LABEL_FONT, justify=tk.LEFT)
        self.title_label.pack(padx=5, pady=5, anchor=tk.NW)
        
        self.data_frame = tk.Frame(self)
        self.data_frame.columnconfigure(list(range(2)), weight=1)
        self.data_frame.rowconfigure(list(range(3)), weight=1)

        self.info_type_label=tk.Label(self, text="Τύπος πληροφορίας")
        self.info_type_label.pack(padx=5, pady=5, anchor=tk.W)

        self.info_type_box = ttk.Combobox(self, values=INFORMATION_TYPES, state="readonly")
        self.info_type_box.current(0)
        self.info_type_box.pack(padx=5, pady=5, anchor=tk.W)

        self.user_name_label = tk.Label(self.data_frame, text="'Ονομα χρήστη")
        self.user_name_label.grid(row=0, column=0,padx=5, pady=5, sticky=tk.NW)
       

        self.user_name_entry = UsernameEntry(self.data_frame, width=30)
        self.user_name_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NW)


        self.date_label = tk.Label(self.data_frame, text="Ημερομηνία")
        self.date_label.grid(row=0, column=1,padx=5, pady=5, sticky=tk.NW)
        
        self.date_entry = DateEntry(self.data_frame, width=30)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NW)

        self.time_label = tk.Label(self.data_frame, text="Ώρα")
        self.time_label.grid(row=4, column=1, padx=5, pady=5, sticky=tk.NW)
        self.time_entry = HourEntry(self.data_frame, width=30)
        self.time_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.NW)

        
        self.data_frame.pack(padx=5, pady=5, fill=tk.X, anchor=tk.NW)
        
        self.description_label = tk.Label(self, text = "Περιγραφή")
        self.description_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.description_text = RichTextEditor(self)
        self.description_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5, anchor=tk.NW)

        self.submit_button = tk.Button(self, text="Καταχώρηση", command=self.on_submit)
        self.submit_button.pack(side=tk.BOTTOM, padx=5, pady=5, anchor=tk.SE)
     
        change_style(self, theme)

    def refresh(self):
        """On re-render hook"""
        self.description_text.destroy()
        self.description_text = RichTextEditor(self)
        self.description_text.pack(after=self.description_label, fill=tk.BOTH, expand=True, padx=5, pady=5, anchor=tk.NW)
        
        change_style(self, theme)

    def on_submit(self):
        d = self.date_entry.get().strip()
        t = self.time_entry.get().strip()

        try:
            event_datetime = datetime.datetime.strptime(d+" "+t , "%d/%m/%Y %H:%M")
        except ValueError:
            event_datetime = datetime.datetime.now()
        
        breaks_data = {
            "employee_name": self.user_name_entry.get(),
            "event_timestamp": event_datetime.timestamp(),
            "event_result": '',
            "event_description": self.description_text.get_text_widget().get("1.0", tk.END)
        }
        
        add_break(breaks_data)
        showinfo('Η καταγραφή', 'Η καταγραφή καταχωρήθηκε με επιτυχία!')



# Use this to test your frame as a single app
if __name__ == "__main__":
    from single_frame_runner import single_frame_runner
    
    single_frame_runner(BreaksFrame)

