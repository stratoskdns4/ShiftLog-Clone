import tkinter as tk

from constants import LABEL_FONT


class InformationReceivedFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        # Place your wigdets here

        self.title_label = tk.Label(self, text="INFORMATION RECEIVED", font=LABEL_FONT, justify=tk.LEFT)
        self.title_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.text_frame = tk.Frame(self)

        self.description_label = tk.Label(self.text_frame, text = "Περιγραφή")
        self.description_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.description_text = tk.Text(self.text_frame, width=30)
        self.description_text.pack(fill=tk.BOTH, padx=5, pady=5)

        self.submit_button = tk.Button(self, text="Καταχώρηση", command=self.on_submit)
        self.submit_button.pack(side=tk.BOTTOM, padx=15, pady=5, anchor=tk.SE)

        self.text_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=15, anchor=tk.NW)

        self.user_name_label = tk.Label(self, text="'Ονομα χρήστη")
        self.user_name_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.user_name_entry = tk.Entry(self, width=30)
        self.user_name_entry.pack(padx=5, pady=5, anchor=tk.NW)
        

        self.date_label = tk.Label(self, text="Ημερομηνία")
        self.date_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.date_entry = tk.Entry(self, width=30)
        self.date_entry.pack(padx=5, pady=5, anchor=tk.NW)

        self.time_call_label = tk.Label(self, text="'Ωρα πληροφορίας")
        self.time_call_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.time_call_entry = tk.Entry(self, width=30)
        self.time_call_entry.pack(padx=5, pady=5, anchor=tk.NW)

        self.reason_label = tk.Label(self, text="Λόγος τηλεφωνήματος")
        self.reason_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.reason_entry = tk.Entry(self, width=30)
        self.reason_entry.pack(padx=5, pady=5, anchor=tk.NW)
        
        
        self.customer_name_label = tk.Label(self, text="'Ονομα Πελάτη")
        self.customer_name_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.customer_name_entry = tk.Entry(self, width=30 )
        self.customer_name_entry.pack(padx=5, pady=5, anchor=tk.NW)

        self.employee_name_label = tk.Label(self, text= "'Ονομα υπαλλήλου")
        self.employee_name_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.employee_name_entry = tk.Entry(self, width=30)
        self.employee_name_entry.pack(padx=5, pady=5, anchor=tk.NW)

        self.area_label = tk.Label(self, text= "Περιοχή περιστατικού")
        self.area_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.area_entry = tk.Entry(self, width=30)
        self.area_entry.pack(padx=5, pady=5, anchor=tk.NW)
        
        
        self.time_label = tk.Label(self, text="Ώρα")
        self.time_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.time_entry = tk.Entry(self, width=30)
        self.time_entry.pack(padx=5, pady=5, anchor=tk.NW)


        self.amount_label = tk.Label(self, text="Ποσό")
        self.amount_label.pack(padx=5, pady=5, anchor=tk.NW)
        self.amount_entry = tk.Entry(self, width=30)
        self.amount_entry.pack(padx=5, pady=5, anchor=tk.NW)


   
       
    def on_submit(self):
        information_received_data = {
            "user":self.user_name_entry.get(),
            "date":self.date_entry.get(),
            "time_call":self.time_call_entry.get(),
            "reason":self.reason_entry.get(),
            "name":self.customer_name_entry.get(),
            "name":self.employee_name_entry.get(),
            "time":self.information_received_time_entry.get(),
            "amount":float(self.amount_entry.get()),
            "description":self.description_text.get("1.0", tk.END)
        }



    def refresh(self):
        """On re-render hook"""


# Use this to test your frame as a single app
        if __name__ == "__main__":
            from single_frame_runner import single_frame_runner

            single_frame_runner(InformationReceivedFrame)
