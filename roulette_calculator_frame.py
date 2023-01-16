import tkinter as tk

from constants import LABEL_FONT


class RouletteCalculatorFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.title_label = tk.Label(self, text="Roulette Calculator", font=LABEL_FONT, justify=tk.LEFT)
        self.title_label.pack(padx=5, pady=5, anchor=tk.NW)


    def refresh(self):
        """On re-render hook"""


# Use this to test your frame as a single app
if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(RouletteCalculatorFrame)
