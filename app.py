import tkinter as tk
from tkinter import ttk

from applog import setup_logging

from frames.main_frame import MainFrame
from frames.login_frame import LoginFrame

from login_controller import LoginController

DEBUG = True

logger = setup_logging()
logger.debug('app.py: STARTING')


if __name__ == '__main__':
    import os

    # fix dpi issues on windows
    if os.name == 'nt':
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)

    logger.warning('mainloop of app')
    window = tk.Tk()
    window.title("Καταγραφη!")
    window.geometry("1200x700")

    # window.tk.call('tk', 'scaling', 2.0)
    
    main_frame = None
    login_frame = None

    def go_to_main_view():
        global main_frame
        if login_frame is not None:
            login_frame.destroy()
        main_frame = MainFrame(window)
        main_frame.pack(fill=tk.BOTH, expand=True)

    def go_to_login_view():
        global login_frame
        if main_frame is not None:
            main_frame.destroy()
        login_frame = LoginFrame(window)
        login_frame.pack(anchor=tk.CENTER, expand=True)


    go_to_login_view()
    lc = LoginController(go_to_main_view, go_to_login_view)

    if DEBUG:
        lc.do_login('aaaa', 'bbbb')

    window.mainloop()
