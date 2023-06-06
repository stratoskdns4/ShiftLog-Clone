import tkinter as tk

from .constants import LABEL_FONT


class RouletteCalculatorFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.title_label = tk.Label(self, text="Roulette Calculator", font=LABEL_FONT, justify=tk.LEFT)
        self.title_label.pack(padx=5, pady=5, anchor=tk.NW)

        self.roulette_grid = tk.Frame(self)
        self.roulette_grid.rowconfigure(tuple(range(3)), weight=1)
        self.roulette_grid.columnconfigure(tuple(range(13)), weight=1)
        self.buttons = []

        #special zero button
        b = tk.Button(self.roulette_grid, text='0', bg='green', font=LABEL_FONT, height=2, relief=tk.FLAT, borderwidth=1)
        b.grid(row=0, column=0, rowspan=3, sticky=tk.NSEW)

        #Παραγωγή των κουμπιών προγραμματιστικά
        for i in range(36):
            arithmos = i+1
            r = i%3
            col =i//3+1
            if arithmos %2==0:
                bcol = "black"
                fcol = "yellow" # "red"
            else:
                bcol = "red"
                fcol = "black"
            
            b = tk.Button(self.roulette_grid, text=str(arithmos), bg=bcol, fg=fcol, font=LABEL_FONT, height=2, relief=tk.FLAT, borderwidth=1)
            b.grid(row=r, column=col, sticky=tk.NSEW)
            self.buttons.append(b)

        self.roulette_grid.pack(padx=5, pady=5, fill=tk.X)




    def refresh(self):
        """On re-render hook"""


# Use this to test your frame as a single app
if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(RouletteCalculatorFrame)
