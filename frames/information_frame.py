import tkinter as tk
from tkinter import ttk

from .constants import LABEL_FONT

from .util_components import UsernameEntry, DateEntry, HourEntry

from .change_style import change_style

from third_party.tk_rich_editor import RichTextEditor

theme = {
    "font-color": "black",
    "empty-background" : {
        'bg':'lightblue'
    },
    "filled-background": {
        'bg': 'white',
        'fg': 'black'
    }
}


INFORMATION_TYPES = ("General Information", "Information Given", "Information Received")

class InformationFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        # Place your wigdets here
        self.title_label = tk.Label(self, text="INFORMATION", font=LABEL_FONT, justify=tk.LEFT)
        self.title_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.config(bg='lightblue')
        
        self.data_frame = tk.Frame(self)
        self.data_frame.columnconfigure(list(range(3)), weight=1)
        self.data_frame.rowconfigure(list(range(6)), weight=1)

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

        self.time_call_label = tk.Label(self.data_frame, text="'Ωρα πληροφορίας")
        self.time_call_label.grid(row=0, column=2, padx=5, pady=5, sticky=tk.NW)
        self.time_call_entry = HourEntry(self.data_frame, width=30)
        self.time_call_entry.grid(row=1, column=2, padx=5, pady=5, sticky=tk.NW)

        self.reason_label = tk.Label(self.data_frame, text="Λόγος τηλεφωνήματος")
        self.reason_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NW)
        self.reason_entry = tk.Entry(self.data_frame, width=30)
        self.reason_entry.grid(row=3, column=0, padx=5, pady=5, sticky=tk.NW)
        
        self.customer_name_label = tk.Label(self.data_frame, text="'Ονομα Πελάτη")
        self.customer_name_label.grid(row=2, column=1, padx=5, pady=5, sticky=tk.NW)
        self.customer_name_entry = tk.Entry(self.data_frame, width=30)
        self.customer_name_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.NW)

        self.employee_name_label = tk.Label(self.data_frame, text= "'Ονομα υπαλλήλου")
        self.employee_name_label.grid(row=2, column=2, padx=5, pady=5, sticky=tk.NW)
        self.employee_name_entry = tk.Entry(self.data_frame, width=30)
        self.employee_name_entry.grid(row=3, column=2, padx=5, pady=5, sticky=tk.NW)

        self.area_label = tk.Label(self.data_frame, text= "Περιοχή περιστατικού")
        self.area_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.NW)
        self.area_entry = tk.Entry(self.data_frame, width=30)
        self.area_entry.grid(row=5, column=0, padx=5, pady=5, sticky=tk.NW)
        
        
        self.time_label = tk.Label(self.data_frame, text="Ώρα")
        self.time_label.grid(row=4, column=1, padx=5, pady=5, sticky=tk.NW)
        self.time_entry = HourEntry(self.data_frame, width=30)
        self.time_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.NW)

        self.amount_label = tk.Label(self.data_frame, text="Ποσό")
        self.amount_label.grid(row=4, column=2, padx=5, pady=5, sticky=tk.NW)
        self.amount_entry = tk.Entry(self.data_frame, width=30)
        self.amount_entry.grid(row=5, column=2, padx=5, pady=5, sticky=tk.NW)

        self.data_frame.pack(padx=5, pady=5, fill=tk.X, anchor=tk.NW)
        
        self.description_label = tk.Label(self, text = "Περιγραφή")
        self.description_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.description_text = RichTextEditor(self, width=30, height=5)
        self.description_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5, anchor=tk.NW)

        self.submit_button = tk.Button(self, text="Καταχώρηση", command=self.on_submit)
        self.submit_button.pack(side=tk.BOTTOM, padx=5, pady=5, anchor=tk.SE)

        change_style(self, theme)


    def on_submit(self):
        information_data = {
            "user":self.user_name_entry.get(),
            "date":self.date_entry.get(),
            "time_call":self.time_call_entry.get(),
            "reason":self.reason_entry.get(),
            "name":self.customer_name_entry.get(),
            "name":self.employee_name_entry.get(),
            "time":self.time_entry.get(),
            "amount":float(self.amount_entry.get()),
            "description":self.description_text.get_text_widget().get("1.0", tk.END)
        }


    def refresh(self):
        """On re-render hook"""
        
        self.description_text.destroy()
        self.description_text = RichTextEditor(self, width=30, height=5)
        self.description_text.pack(after=self.description_label, fill=tk.BOTH, expand=True, padx=5, pady=5, anchor=tk.NW)
        change_style(self, theme)


# Use this to test your frame as a single app
if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(InformationFrame)

