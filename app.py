import tkinter as tk
from tkinter import ttk

from register_event_frame import RegisterEventFrame
from chip_fill_frame import ChipFillFrame
from tables_frame import TablesFrame
from personel_frame import PersonelFrame

from logic import save_event

RESULT_VALUES = ("Saving", "Player", "Neutral", "Comercial Decision")

# κατασκευή αρχικού παραθύρου
window = tk.Tk()
# Αλλαγή τίτλου παραθύρου
window.title("Καταγραφη!")
# Αλλαγή αρχικού μεγέθους παραθύρου
window.geometry("850x550")

tab_view = ttk.Notebook(window)

register_frame = RegisterEventFrame(tab_view)
tab_view.add(register_frame, text="Καταγραφή Γεγονότος")

chipfill_frame = ChipFillFrame(tab_view)
tab_view.add(chipfill_frame, text='Chip Fill')

tables_frame = TablesFrame(tab_view)
tab_view.add(tables_frame, text="Tables")

personel_frame = PersonelFrame(tab_view)
tab_view.add(personel_frame, text="Προσωπικό")

tab_view.select(3)

# βάλε ότα τα tabs στο παράθυρο
tab_view.pack(fill=tk.BOTH, expand=True)

# εκίνηση του βρόγχου γεγονότων
window.mainloop()