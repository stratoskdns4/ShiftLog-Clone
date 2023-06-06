import tkinter as tk
from tkinter import ttk

from applog import setup_logging

from frames.register_event_frame import RegisterEventFrame
from frames.chip_fill_frame import ChipFillFrame
from frames.tables_frame import TablesFrame
from frames.events_frame import EventsFrame
from frames.personel_frame import PersonelFrame
from frames.jackpot_frame import JackpotFrame
from frames.cash_out_frame import CashoutFrame
from frames.roulette_calculator_frame import RouletteCalculatorFrame
from frames.information_frame import InformationFrame
from frames.watched_frame import WatchedFrame
from frames.plot_frame import PlotFrame
from frames.breaks_frame import BreaksFrame




logger = setup_logging()
logger.debug('app.py: STARTING')
pages = dict()


def on_tab_change(ev):
    """
    What to do when a tab changes. Right now, we only care about the EVENTS tab
    """
    idx = notebook.index(notebook.select())
    r = notebook.tab(idx)
    rtext = r['text'].lower()

    # rtext here is the key in the pages array
    # If we cared, we would put a focus method in all classes
    try:
        pages[rtext].refresh()
    except Exception as e:
        logger.warning(f'exception calling refresh! {e}')

def get_tab_idx_by_name(tabname):
    """
    Return the index of the given tab
    """

if __name__ == '__main__':
    logger.warning('mainloop of app')
    window = tk.Tk()
    window.title("Καταγραφη!")
    window.geometry("850x550")

    notebook = ttk.Notebook(window)
    notebook.pack(fill=tk.BOTH, expand=True)
    notebook.bind('<<NotebookTabChanged>>', on_tab_change)

    pages = {
        'register': RegisterEventFrame(notebook),
        'breaks': BreaksFrame(notebook),
        'tables': TablesFrame(notebook),
        'chip fill': ChipFillFrame(notebook),
        'personnel': PersonelFrame(notebook),
        'events': EventsFrame(notebook),
        'jackpot_call': JackpotFrame(notebook),
        'cashout_call': CashoutFrame(notebook),
        'roulette_calculator': RouletteCalculatorFrame(notebook),
        'information': InformationFrame(notebook),
        'watched': WatchedFrame(notebook),
        'plot': PlotFrame(notebook)
        
    }

    for k, v in pages.items():
        # make the string look good
        notebook.add(v, text=k.replace('_', ' ').title())

    notebook.select(3)
    window.mainloop()
