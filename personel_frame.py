import tkinter as tk
from tkinter import ttk

from constants import LABEL_FONT


COLUMN_NAMES = ("Κωδικός", "Επώνυμο", "Όνομα", "Ιδιότητα")

class PersonelFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.title_label = tk.Label(self, text="Προσωπικό", font=LABEL_FONT, justify=tk.LEFT, anchor=tk.W)
        self.title_label.pack(fill=tk.X, anchor=tk.W, padx=10, pady=5)

        self.personel_treeview = ttk.Treeview(self, columns=COLUMN_NAMES)

        for column in COLUMN_NAMES:
            self.personel_treeview.heading(column, text=column, anchor=tk.W)
            self.personel_treeview.column(column, width=1, anchor=tk.W, stretch=True)

        self.personel_treeview.column("#0", width=1, stretch=False)
        self.personel_treeview.pack(fill=tk.BOTH, expand=True, padx=5, pady=5, anchor=tk.NW)




if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(PersonelFrame)