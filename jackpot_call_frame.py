import tkinter as tk
from tkinter import ttk

from constants import LABEL_FONT


class JackpotCallFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)



        

if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(JackpotCallFrame)