import tkinter as tk
from tkinter import ttk

from .camera_frame import CameraFrame
from .register_event_frame import RegisterEventFrame
from .chip_fill_frame import ChipFillFrame
from .tables_frame import TablesFrame
from .events_frame import EventsFrame
from .personel_frame import PersonelFrame
from .jackpot_frame import JackpotFrame
from .cash_out_frame import CashoutFrame
from .roulette_calculator_frame import RouletteCalculatorFrame
from .information_frame import InformationFrame
from .watched_frame import WatchedFrame
from .plot_frame import PlotFrame
from .breaks_frame import BreaksFrame

from applog import setup_logging

from login_controller import LoginController
logger = setup_logging()


class MainFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)
        self.pages = dict()

       
        username = LoginController().get_logged_in_user()
        self.status_bar = tk.Frame(self)
        self.status_label = tk.Label(self.status_bar, text=f"Logged in as {username}")
        self.status_label.pack(side=tk.LEFT, anchor=tk.W)

       
        self.logout_button = tk.Button(self.status_bar, text='Αποσύνδεση', command=LoginController().do_logout)
        self.logout_button.pack(side=tk.RIGHT)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.notebook.bind('<<NotebookTabChanged>>', self.on_tab_change)


        self.pages = {
            'camera': CameraFrame(self.notebook),
            'register': RegisterEventFrame(self.notebook),
            'breaks': BreaksFrame(self.notebook),
            'tables': TablesFrame(self.notebook),
            'chip_fill': ChipFillFrame(self.notebook),
            'personnel': PersonelFrame(self.notebook),
            'events': EventsFrame(self.notebook),
            'jackpot_call': JackpotFrame(self.notebook),
            'cashout_call': CashoutFrame(self.notebook),
            'roulette_calculator': RouletteCalculatorFrame(self.notebook),
            'information': InformationFrame(self.notebook),
            'watched': WatchedFrame(self.notebook),
            'plot': PlotFrame(self.notebook)
            
        }

        for k, v in self.pages.items():
            # make the string look good
            self.notebook.add(v, text=k.replace('_', ' ').title())

        self.notebook.select(3)

    def on_tab_change(self, ev):
        """
        What to do when a tab changes. Right now, we only care about the EVENTS tab
        """
        idx = self.notebook.index(self.notebook.select())
        r = self.notebook.tab(idx)
        rtext = r['text'].replace(' ', '_').lower()

        # rtext here is the key in the pages array
        # If we cared, we would put a focus method in all classes
        try:
            
            self.pages[rtext].refresh()
        except Exception as e:
            logger.warning(f'exception calling refresh! {type(e)} {e}')

    def get_tab_idx_by_name(self, tabname):
        """
        Return the index of the given tab
        """
            
        