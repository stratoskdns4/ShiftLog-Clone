import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from tkinter import filedialog as fd
import json

from constants import LABEL_FONT

from logic import save_event

RESULT_VALUES = ("Saving", "Player", "Neutral", "Comercial Decision")


class RegisterEventFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.opened_filepath = None

        self.my_label = tk.Label(self, text="Καταγραφη Γεγονότος", font=LABEL_FONT, anchor=tk.W)
        self.my_label.pack(fill=tk.X, pady=10, padx=5)

        # Πεδίο εισαγωγης ονόματος υπαλήλου
        self.employee_label = tk.Label(self, text="Όνομα εργαζομένου", anchor=tk.W)
        self.employee_label.pack(fill=tk.X, pady=10, padx=5)

        self.employee_entry = tk.Entry(self, width=30)
        self.employee_entry.pack(anchor=tk.W, padx=5)

        # Κατασκευάζω μια περιοχή (Frame), στην οποία θα τοποθετήσω
        # μόνο τα 3 κουμπία. Έτσι, θα μπορέσω να τα βάλω στην ίδια
        # σειρά χρησιμοποιώντας το pack()
        self.buttons_frame = tk.Frame(self)

        # Στο buttons_frame, τοποθετώ τα 3 κουμπιά
        self.submit_button = tk.Button(self.buttons_frame, text="Καταχώρηση", command=self.on_submit)
        self.submit_button.pack(side=tk.RIGHT, anchor=tk.E, padx=5, pady=5)

        self.clear_button = tk.Button(self.buttons_frame, text="Εκκαθάριση", command=self.clear_all)
        self.clear_button.pack(side=tk.RIGHT, anchor=tk.E, padx=5, pady=5)

        self.edit_button = tk.Button(self.buttons_frame, text="Επεξεργασία", command=self.on_edit)
        self.edit_button.pack(side=tk.LEFT, anchor=tk.W, padx=5, pady=5)

        self.buttons_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

        # πεδίο κειμένου
        self.desc_label = tk.Label(self, text="Περιγραφή", anchor=tk.W)
        self.desc_label.pack(fill=tk.X, pady=10, padx=5)

        # επιλογή απόφασης
        self.result_box = ttk.Combobox(self, values=RESULT_VALUES, state="readonly")
        self.result_box.current(0)
        self.result_box.pack(side=tk.BOTTOM, anchor=tk.W, padx=5)

        self.result_label = tk.Label(self, text="Απόφαση", anchor=tk.W)
        self.result_label.pack(side=tk.BOTTOM, fill=tk.X, pady=10, padx=5)

        self.description_text = tk.Text(self)
        self.description_text.pack(fill=tk.BOTH, expand=True, padx=5)

    def clear_all(self):
        """
        Καθαρίζει το περιεχόμενο όλων των πεδίων εισαγωγής κειμένου.
        Άκόμα, καθαρίζει το όνομα αρχείου.
        """
        self.opened_filepath = None

        # καθαρισμος entries και textbox
        self.employee_entry.delete(0, tk.END)
        self.description_text.delete("1.0", tk.END)

        # επαναφορά combobox
        self.result_box.current(0)

    def on_submit(self):
        """
        Καταχωρεί τα δεδομένα με χρήση της συνάρτησης save_event().
        """
        # Πέρνω τα δεδομένα από τη φόρμα
        event_dict = {
            "employee_name": self.employee_entry.get(),
            "event_description": self.description_text.get("1.0", tk.END),
            "event_result": self.result_box.get()
        }

        save_event(event_dict, self.opened_filepath)
        showinfo("Καταγραφή", "Η καταγραφή καταχωρήθηκε με επιτυχία!")

        self.clear_all()

    def on_edit(self):
        """
        Ανοίγει ένα νέο παράθυρο επιλογής αρχείου.
        Αν επιλεχθεί ένα αρχείο με επιτυχία, και είναι και κατάλληλου τύπου,
        θέτει τα περιεχόμενα των πεδίων συύμφωνα με το αρχείο.
        Ακόμα, βάζει τιμή στη μεταβλητή opened_filepath.
        """
        FILE_TYPES = (("JSON log files", "*.json"), ('All files', '*.*'))
        self.opened_filepath = fd.askopenfilename(title="Επιλέξτε αρχείο καταγραφής",
            initialdir="logs",
            filetypes=FILE_TYPES)

        print(f"Filename selected: {self.opened_filepath}")
        
        # ανάγνωση αρχείου για επεξεργασία
        

        # ενημέρωση των πεδίων
        # Σε περίπτωση λάθους, εμφανίζεται κατάλληλο μήνυμα και
        # καθαρίζει το παράθυρο.
        try:
            fp = open(self.opened_filepath, 'r')
            event_data = json.load(fp)
            fp.close()
            self.employee_entry.insert(0, event_data["employee_name"])
            self.description_text.insert("1.0", event_data["event_description"])
            self.result_box.current(RESULT_VALUES.index(event_data["event_result"]))
        except (KeyError, IndexError, ValueError, OSError, FileNotFoundError):
            showerror("Σφάλμα", "Σφάλμα κατά την ανάγνωση του αρχείου!")
            self.clear_all()


if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(RegisterEventFrame)