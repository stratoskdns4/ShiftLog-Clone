import tkinter as tk
import random
import time

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

        self.previous_button = None
        self.previous_color = None
        self.previous_label = None

        self.last_numbers = []

        #special zero button
        b = tk.Button(self.roulette_grid, text='0', fg='#eee', bg='green', font=LABEL_FONT, height=2, relief=tk.FLAT, borderwidth=1)
        b.grid(row=0, column=0, rowspan=3, sticky=tk.NSEW)
        self.buttons.append(b)

        #Παραγωγή των κουμπιών προγραμματιστικά
        for i in range(36):
            arithmos = i+1
            row = i%3
            col = i//3+1

            # αντιστροφή 1ης και 3ης γραμμής
            if row == 0:
                row = 2
            elif row == 2:
                row = 0    

            if arithmos %2==0:
                bcol = "black"
                fcol = "#eee" # "red"
            else:
                bcol = "#de1f12"
                fcol = "#eee"
            
            b = tk.Button(self.roulette_grid, text=str(arithmos), bg=bcol, fg=fcol, font=LABEL_FONT, height=2, relief=tk.FLAT, borderwidth=1)
            b.grid(row=row, column=col, sticky=tk.NSEW)
            self.buttons.append(b)

        self.roulette_grid.pack(padx=5, pady=5, fill=tk.X)

        self.last_numbers_title = tk.Label(self,  text='Tελευταίες κληρώσεις:')
        self.last_numbers_title.pack(anchor=tk.W, pady=5, padx=25)

        # self.last_numbers_label = tk.Label(self,  text='NO DATA', font=LABEL_FONT)
        # self.last_numbers_label.pack(anchor=tk.W, pady=5, padx=25)
        self.last_numbers_frame = tk.Frame(self)
        self.last_numbers_frame.config(bg='#444') #, height=150)
        self.last_numbers_frame.pack(fill=tk.X, padx=5, pady=5, ipadx=2)

    

        self.pick_random_button = tk.Button(self, text='κλήρωση', command=self.lotery)
        self.pick_random_button.pack(anchor=tk.E, padx=5, pady=5)


    def pick_random_box(self):
        if self.previous_button:
            self.previous_button.config(bg=self.previous_color)

        
        button: tk.Button = random.choice(self.buttons)
        self.previous_color = button['bg']
        self.previous_fg_color = button['fg']
        self.previous_button = button

        button.config(bg='blue')


    def lotery(self):
        jumps = random.randint(8, 20)
        for i in range(jumps):
            self.pick_random_box()
            self.update()
            time.sleep(0.1)

        lucky_number = str(self.previous_button['text']) # format(self.previous_button['text'], '>2s')
        bg_col = self.previous_color
        fg_col = self.previous_fg_color
        # self.last_numbers.append(lucky_number)

        # if len(self.last_numbers) > 20:
        #     self.last_numbers.pop(0) # βγάλε το πιο παλαιό στοιχείο

        # new_label_text = ' '.join(reversed(self.last_numbers))
        # self.last_numbers_label.config(text=new_label_text)
            
        new_label = tk.Label(self.last_numbers_frame, text=lucky_number, font=LABEL_FONT, bg=bg_col, fg=fg_col, width=5, height=3)
        new_label.pack(side=tk.LEFT, before=self.previous_label, fill=tk.Y, padx=2, pady=4)
        self.previous_label = new_label
        new_label.pack()

        if len(self.last_numbers_frame.children) > 20:
            self.last_numbers_frame.winfo_children()[0].destroy()

    
    def refresh(self):
        """On re-render hook"""


# Use this to test your frame as a single app
if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(RouletteCalculatorFrame)
