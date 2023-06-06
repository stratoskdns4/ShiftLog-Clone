import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import random
from matplotlib import pyplot as plt
import datetime

def create_fake_year_data(initial_value):
    N = 12
    K = [initial_value]

    for i in range(N-1):
        allagh = random.randint(-100, 85)
        prohgoumeni_timi = K[-1]
        nea_timi = prohgoumeni_timi + allagh
        K.append(nea_timi)

    return K


def add_noise(data):
    noisy = []
    for e in data:
        noisy.append(e + random.randint(-40, 40))

    return noisy



class PlotFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        # Place your wigdets here
        
        
        self.fig = Figure(figsize=(18.5, 10.5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        trend = create_fake_year_data(1000)

        for year in range(2017, 2024):
            data = create_fake_year_data(1000)
            # data = add_noise(trend)

            months = [datetime.date(year, item, 1).strftime('%b') for item in range(1, 13)]
            self.ax.plot(months, data, '.-', label= str(year))
            self.ax.set_xlabel("Month")
            self.ax.set_ylabel("Year")


        self.ax.set_title("Drop")
        self.ax.grid()
        self.ax.legend()
        # plt.show()


        self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
        self.canvas.draw()
        #self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.pack(side=tk.BOTTOM, fill=tk.X, pady=2)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def refresh(self):
        """On re-render hook"""
        pass



# Use this to test your frame as a single app
if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(PlotFrame)
