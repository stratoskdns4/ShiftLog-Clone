import tkinter as tk
from tkinter import ttk
from constants import LABEL_FONT


class JackpotFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.title_label = tk.Label(self, text="JACKPOT CALL", font=LABEL_FONT, justify=tk.LEFT)
        self.title_label.pack(padx=5, pady=5, anchor=tk.NW)
        
        self.text_frame = tk.Frame(self)

        self.description_label = tk.Label(self.text_frame, text = "Περιγραφή")
        self.description_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.description_text = tk.Text(self.text_frame, width=30)
        self.description_text.pack(fill=tk.BOTH, padx=5, pady=5)


        self.submit_button = tk.Button(self, text="Καταχώρηση")
        self.submit_button.pack(side=tk.BOTTOM, padx=15, pady=5, anchor=tk.SE)

        self.text_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=15, anchor=tk.NW)


        self.amount_label = tk.Label(self, text="Ποσό")
        self.amount_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.amount_entry = tk.Entry(self, width=30)
        self.amount_entry.pack(padx=5, pady=5, anchor=tk.NW)

        self.customer_name_label= tk.Label(self, text="'Ονομα Πελάτη")
        self.customer_name_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.customer_name_entry = tk.Entry(self, width=30 )
        self.customer_name_entry.pack(padx=5, pady=5, anchor=tk.NW)

        self.jackpot_time_label = tk.Label(self, text="Jackpot Ώρα")
        self.jackpot_time_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.jackpot_time_entry = tk.Entry(self, width=30)
        self.jackpot_time_entry.pack(padx=5, pady=5, anchor=tk.NW)

        self.slot_machine_label= tk.Label(self, text="Μηχάνημα")
        self.slot_machine_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.slot_machine_entry = tk.Entry(self, width=30)
        self.slot_machine_entry.pack(padx=5, pady=5, anchor=tk.NW)

        




if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(JackpotFrame)
