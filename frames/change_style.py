import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar

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

def change_style(element, theme):
    if element is None:
        return
    
    if isinstance(element, (tkcalendar.DateEntry, ttk.Treeview, ttk.Combobox)):
        return
    
    if isinstance(element, (tk.Label)):
        element.config(**theme['empty-background'])
        element.config(fg=theme['font-color'])
    elif isinstance(element, (tk.Tk, tk.Frame)):
        element.config(**theme['empty-background'])
    elif isinstance(element, (tk.Entry, tk.Button, tk.OptionMenu, tk.Text)):
        element.config(**theme['filled-background'])


    children = element.winfo_children()
    for child in children:
        change_style(child, theme)
