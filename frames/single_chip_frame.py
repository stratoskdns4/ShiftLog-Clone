import tkinter as tk
from tkinter import ttk
import os

from .constants import LABEL_FONT, ENTRY_FONT


class SingleChipFrame(tk.Frame):

    def __init__(self, root, chip_value=5000, **options):
        super().__init__(root, **options)

        self.chip_value = chip_value
        self.chip_count_intvar = tk.IntVar()

        self.config(highlightbackground="black", highlightthickness=1)

        # ισόρρoπησε το grid
        self.rowconfigure(tuple(range(4)), weight=1)
        self.columnconfigure(tuple(range(3)), weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(0, weight=2)

        image_number = "{:.2f}".format(float(self.chip_value)).replace('.', '_')
        image_name = f"chip_{image_number}.png"

        image_path = f"images/{image_name}"

        if not os.path.isfile(image_path):
            image_path = "images/chip_5000_00.png"

        self.chip_image = tk.PhotoImage(file=image_path).subsample(4, 4)
        self.image_label = tk.Label(self, image=self.chip_image)
        self.image_label.grid(columnspan=3)

        if type(self.chip_value) is int:
            self.chip_label_text = "{:d}€".format(self.chip_value)
        else:
            self.chip_label_text = "{:.2f}€".format(self.chip_value)


        self.chip_label = tk.Label(self, text=self.chip_label_text, font=LABEL_FONT)
        self.chip_label.grid(row=1, column=0, columnspan=3, sticky=tk.S)
        

        self.integer_vcmd = (self.register(self.integer_validator))

        # num field
        self.chip_count_entry = tk.Entry(self, font=ENTRY_FONT, textvariable=self.chip_count_intvar, justify=tk.RIGHT, width=8, validate='all', validatecommand=(self.integer_vcmd, '%P'))
        self.chip_count_entry.grid(row=2, column=1)

        #self.update_count_entry()

        self.decrement_button = tk.Button(self, text='-', justify=tk.CENTER, command=self.decrement_chip_count)
        self.decrement_button.grid(row=2, column=0)

        self.increment_button = tk.Button(self, text='+', justify=tk.CENTER, command=self.increment_chip_count)
        self.increment_button.grid(row=2, column=2)


    def decrement_chip_count(self):
        if self.chip_count_intvar.get() <= 0:
            return

        self.chip_count_intvar.set(self.chip_count_intvar.get()-1)

    def increment_chip_count(self):
        self.chip_count_intvar.set(self.chip_count_intvar.get()+1)
    
    def integer_validator(self, P):
        return str.isdigit(P) or P == ""

    def reset_count(self):
        self.chip_count_intvar.set(0)

    def get_total_value(self):
        try:
            return int(self.chip_count_intvar.get()) * self.chip_value
        except:
            return 0
        



if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(SingleChipFrame, dimensions=(250, 180))