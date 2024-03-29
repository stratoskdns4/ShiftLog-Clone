import tkinter as tk
from tkinter.messagebox import showinfo
from logic import add_cashout
from .util_components import UsernameEntry, DateEntry, HourEntry
from .change_style import change_style
from third_party.tk_rich_editor import RichTextEditor
from .constants import LABEL_FONT

theme = {
    "font-color": "black",
    "empty-background" : {
        'bg':'brown'
    },
    "filled-background": {
        'bg': '#eda682',
        'fg': 'black'
    }
}


class CashoutFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.title_label = tk.Label(self, text="CASHOUT", font=LABEL_FONT, justify=tk.LEFT, bg='brown')
        self.title_label.pack(padx=5, pady=5, anchor=tk.NW)
        # self.config(bg='brown')
        
        self.text_frame = tk.Frame(self)

        self.description_label = tk.Label(self.text_frame, text = "Περιγραφή")
        self.description_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.description_text = RichTextEditor(self.text_frame, width=10)
        self.description_text.pack(fill=tk.Y, padx=5, pady=5)

        self.submit_button = tk.Button(self, text="Καταχώρηση", command=self.on_submit)
        self.submit_button.pack(side=tk.BOTTOM, padx=15, pady=5, anchor=tk.SE)

        self.text_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=15, anchor=tk.NW)
        self.text_frame.config(width=20)

        self.date_label = tk.Label(self, text="Ημερομηνία")
        self.date_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.date_entry = DateEntry(self, width=30)
        self.date_entry.pack(padx=5, pady=5, anchor=tk.NW)

        self.cashout_time_label = tk.Label(self, text="Cashout Ώρα")
        self.cashout_time_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.cashout_time_entry = HourEntry(self, width=30)
        self.cashout_time_entry.pack(padx=5, pady=5, anchor=tk.NW)
        
        self.amount_label = tk.Label(self, text="Ποσό")
        self.amount_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.amount_entry = tk.Entry(self, width=30)
        self.amount_entry.pack(padx=5, pady=5, anchor=tk.NW)

        self.employee_label = tk.Label(self, text='Όνομα Υπαλλήλου')
        self.employee_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.employee_entry = UsernameEntry(self, width=30)
        self.employee_entry.pack(padx=5, pady=5, anchor=tk.NW)

        self.customer_name_label = tk.Label(self, text="'Ονομα Πελάτη")
        self.customer_name_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.customer_name_entry = tk.Entry(self, width=30 )
        self.customer_name_entry.pack(padx=5, pady=5, anchor=tk.NW)

       

        self.cash_desk_window_label = tk.Label(self, text="Παράθυρο")
        self.cash_desk_window_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.cash_desk_window_entry = tk.Entry(self, width=30)
        self.cash_desk_window_entry.pack(padx=5, pady=5, anchor=tk.NW)

        change_style(self, theme)
    

    def refresh(self):
        """On re-render hook"""
        self.description_text.destroy()
        self.description_text = RichTextEditor(self.text_frame, width=10)
        self.description_text.pack(after=self.description_label, fill=tk.Y, expand=True, padx=5, pady=5, anchor=tk.NW)
        change_style(self, theme)

    def on_submit(self):
        cashout_data = {
            'date':self.date_entry.get(),
            'employee':self.employee_entry.get(),
            "window":self.cash_desk_window_entry.get(),
            "name":self.customer_name_entry.get(),
            "amount":float(self.amount_entry.get()),
            "time":self.cashout_time_entry.get(),
            "description":self.description_text.get_text_widget().get("1.0", tk.END)
        }

        add_cashout(cashout_data)
        showinfo("Καταγραφή", "Η καταγραφή καταχωρήθηκε με επιτυχία!")
        self.clear_all()


    def clear_all(self):
        self.amount_entry.delete(0, tk.END)
        self.cashout_time_entry.delete(0, tk.END)
        self.cash_desk_window_entry.delete(0, tk.END)
        self.customer_name_entry.delete(0, tk.END)
        self.description_text.get_text_widget().delete("1.0", tk.END)


if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(CashoutFrame)
