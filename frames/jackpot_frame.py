import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from frames.constants import LABEL_FONT
from logic import add_jackpot
from .util_components import HourEntry
from .util_components import UsernameEntry
from .util_components import DateEntry

from .change_style import change_style

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

class JackpotFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.title_label = tk.Label(self, text="JACKPOT CALL", font=LABEL_FONT, justify=tk.LEFT)
        self.title_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.config(bg='lightblue')
        
        self.data_frame = tk.Frame(self)
        self.data_frame.columnconfigure(list(range(3)), weight=1)
        self.data_frame.rowconfigure(list(range(6)), weight=1)


        self.amount_label = tk.Label(self.data_frame, text="Ποσό")
        self.amount_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NW)
        self.amount_entry = tk.Entry(self.data_frame, width=30)
        self.amount_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NW)

        self.customer_name_label= tk.Label(self.data_frame, text="'Ονομα Πελάτη")
        self.customer_name_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NW)
        self.customer_name_entry = tk.Entry(self.data_frame, width=30)
        self.customer_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NW)

        self.jackpot_time_label = tk.Label(self.data_frame, text="Jackpot Ώρα")
        self.jackpot_time_label.grid(row=0, column=2, padx=5, pady=5, sticky=tk.NW)
        self.jackpot_time_entry = HourEntry(self.data_frame, width=30)
        self.jackpot_time_entry.grid(row=1, column=2, padx=5, pady=5, sticky=tk.NW)

        self.slot_machine_label= tk.Label(self.data_frame, text="Μηχάνημα")
        self.slot_machine_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NW)
        self.slot_machine_entry = tk.Entry(self.data_frame, width=30)
        self.slot_machine_entry.grid(row=3, column=0, padx=5, pady=5, sticky=tk.NW)

        self.cash_desk_label = tk.Label(self.data_frame, text="Παράθυρο")
        self.cash_desk_label.grid(row=2, column=1, padx=5, pady=5, sticky=tk.NW)
        self.cash_desk_entry = tk.Entry(self.data_frame, width=30)
        self.cash_desk_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.NW)

        self.employee_name_label = tk.Label(self.data_frame, text="Υπάλληλος")
        self.employee_name_label.grid(row=2, column=2, padx=5, pady=5, sticky=tk.NW)
        self.employee_name_entry = UsernameEntry(self.data_frame, width=30)
        self.employee_name_entry.grid(row=3, column=2, padx=5, pady=5, sticky=tk.NW)

        self.date_label = tk.Label(self.data_frame, text="Ημερομηνία")
        self.date_label.grid(row=2, column=4, padx=5, pady=5, sticky=tk.NW)
        self.date_entry = DateEntry(self.data_frame, width=30)
        self.date_entry.grid(row=3, column=4, padx=5, pady=5, sticky=tk.NW)


        self.data_frame.pack(fill=tk.X, padx=15, anchor=tk.NW)

        self.description_label = tk.Label(self, text="Περιγραφή")
        self.description_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.description_text = tk.Text(self, width=30, height=5)
        self.description_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5, anchor=tk.NW)

        self.submit_button = tk.Button(self, text="Καταχώρηση", command=self.on_submit)
        self.submit_button.pack(side=tk.BOTTOM, padx=15, pady=5, anchor=tk.SE)

        change_style(self, theme)
    
    def on_submit(self):
        jackpot_data = {
            "slot":self.slot_machine_entry.get(),
            "name":self.customer_name_entry.get(),
            "amount":float(self.amount_entry.get()),
            "time":self.jackpot_time_entry.get(),
            "description":self.description_text.get("1.0", tk.END)
        }

        add_jackpot(jackpot_data)
        showinfo("Καταγραφή", "Η καταγραφή καταχωρήθηκε με επιτυχία!")
        self.clear_all()


    def clear_all(self):
        self.amount_entry.delete(0, tk.END)
        self.jackpot_time_entry.delete(0, tk.END)
        self.slot_machine_entry.delete(0, tk.END)
        self.customer_name_entry.delete(0, tk.END)
        self.description_text.delete("1.0", tk.END)


if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(JackpotFrame)
