import tkinter as tk
from tkinter import ttk

from register_event_frame import RegisterEventFrame
from chip_fill_frame import ChipFillFrame
from tables_frame import TablesFrame
from events_frame import EventsFrame
from applog import setup_logging


logger=setup_logging()
logger.debug('STARTING')

LABEL_FONT = ("Arial", 16, "bold")
RESULT_VALUES = ("Saving", "Player", "Neutral", "Comercial Decision")

def on_tab_change(ev):
    """
    What to do when a tab changes. Right now, we only care about the EVENTS tab
    """
    idx = notebook.index(notebook.select())
    r=notebook.tab(idx)
    rtext=r['text'].lower()

    page = pages[rtext]
    if rtext=='events':
        pages[rtext].refresh()
    logger.warning(f'on_tab_change called with event: {idx}')
    pass


if __name__ == '__main__':
    logger.warning('mainloop of app')
    window = tk.Tk()
    window.title("Καταγραφη!")
    window.geometry("850x550")

    notebook = ttk.Notebook(window)
    notebook.pack(fill=tk.BOTH, expand=True)
    notebook.bind('<<NotebookTabChanged>>', on_tab_change)

    pages={
        'register': RegisterEventFrame(notebook),
        'tables': TablesFrame(notebook),
        'chip fill': ChipFillFrame(notebook),
        'events': EventsFrame(notebook),
    }
    for k, v in pages.items():
        notebook.add(v, text=k.replace('_', ' ').title())

#    notebook.add(register_frame, text="Καταγραφή Γεγονότος")
#    notebook.add(chipfill_frame, text='Chip Fill')
#    notebook.add(tables_frame, text="Tables")
#    notebook.add(events_frame, text='EVENTS')

    notebook.select(2)
    window.mainloop()

