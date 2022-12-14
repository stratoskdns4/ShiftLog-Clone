import tkinter as tk
from tkinter import ttk

from register_event_frame import RegisterEventFrame
from chip_fill_frame import ChipFillFrame
from tables_frame import TablesFrame
from events_frame import EventsFrame
from applog import setup_logging
from personel_frame import PersonelFrame
from jackpot_frame import JackpotFrame

# Αυτό είναι το πρώτο comment από το νέο laptop


logger=setup_logging()
logger.debug('app.py: STARTING')
pages = dict()

RESULT_VALUES = ("Saving", "Player", "Neutral", "Comercial Decision")

def on_tab_change(ev):
    """
    What to do when a tab changes. Right now, we only care about the EVENTS tab
    """
    idx = notebook.index(notebook.select())
    r=notebook.tab(idx)
    rtext=r['text'].lower()

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
        'tables': TablesFrame(notebook),
        'chip fill': ChipFillFrame(notebook),
        'personnel': PersonelFrame(notebook),
        'events': EventsFrame(notebook),
        'jackpot_call': JackpotFrame(notebook)
    }

    for k, v in pages.items():
        # make the string look good
        notebook.add(v, text=k.replace('_', ' ').title())

    notebook.select(3)
    window.mainloop()

