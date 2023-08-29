import tkinter as tk
from tkinter import ttk

from .single_chip_frame import SingleChipFrame

from .constants import LABEL_FONT
from .change_style import change_style

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

CHIP_VALUES = [5000, 1000, 500, 100, 25, 10, 5, 2.5] #, 1.25]
SINGLE_CHIP_THEMES = [{'font-color': 'black', 'empty-background': {'bg': 'brown'}, 'filled-background': {'bg': '#385905', 'fg': 'black'}}, {'font-color': 'black', 'empty-background': {'bg': 'brown'}, 'filled-background': {'bg': '#7f7e79', 'fg': 'black'}}, {'font-color': 'black', 'empty-background': {'bg': 'brown'}, 'filled-background': {'bg': '#dbba22', 'fg': 'black'}}, {'font-color': 'white', 'empty-background': {'bg': 'brown'}, 'filled-background': {'bg': '#14151a', 'fg': 'white'}}, {'font-color': 'black', 'empty-background': {'bg': 'brown'}, 'filled-background': {'bg': '#5da663', 'fg': 'black'}}, {'font-color': 'black', 'empty-background': {'bg': 'brown'}, 'filled-background': {'bg': '#e07bd7', 'fg': 'black'}}, {'font-color': 'black', 'empty-background': {'bg': 'brown'}, 'filled-background': {'bg': '#d92c20', 'fg': 'black'}}, {'font-color': 'white', 'empty-background': {'bg': 'brown'}, 'filled-background': {'bg': '#4c5849', 'fg': 'white'}}]

class ChipFillFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.N_ROWS = 3
        self.N_COLS = 4

        self.rowconfigure(tuple(range(self.N_ROWS)), weight=2, minsize=200)
        self.rowconfigure(2, weight=1, minsize=100)
        self.columnconfigure(tuple(range(self.N_COLS)), weight=1, minsize=200)

        self.single_chip_comps = []

        for i, chip_value in enumerate(CHIP_VALUES):
            rw, cl = divmod(i, self.N_COLS)

            scf = SingleChipFrame(self, chip_value=chip_value)
            self.single_chip_comps.append(scf)

            # bind events
            scf.chip_count_intvar.trace_add("write", self.update_label)
            scf.grid(row=rw, column=cl, sticky=tk.EW, padx=10, pady=10)

        self.total_label = tk.Label(self, text="Σύνολο", font=LABEL_FONT, justify=tk.LEFT)
        self.total_label.grid(row=self.N_ROWS-1, column=self.N_COLS-1, sticky=tk.W)

        self.reset_button = tk.Button(self, text="Επαναφορά", command=self.reset_all_counts)
        self.reset_button.grid(row=self.N_ROWS-1, column=0)

        change_style(self, theme)
        
        for chip_frame, chip_theme in zip(self.single_chip_comps, SINGLE_CHIP_THEMES):
            change_style(chip_frame, chip_theme)

        self.update_label()

      

    def update_label(self, *args):
        total_chip_value = 0
        for scf in self.single_chip_comps:
            total_chip_value += scf.get_total_value()
        
        text = "Σύνολο: {:7.2f}€".format(float(total_chip_value))
        self.total_label.config(text=text)

    def reset_all_counts(self):
        for scf in self.single_chip_comps:
            scf.reset_count()



if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(ChipFillFrame)
  
