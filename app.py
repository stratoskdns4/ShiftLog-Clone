import tkinter as tk
from tkinter import ttk

from applog import setup_logging

from frames.main_frame import MainFrame
from frames.login_frame import LoginFrame




logger = setup_logging()
logger.debug('app.py: STARTING')






if __name__ == '__main__':
    logger.warning('mainloop of app')
    window = tk.Tk()
    window.title("Καταγραφη!")
    window.geometry("850x550")

    def do_login(username, password):
        if username == 'Stratos' and password == '1234':
            print('Succesfull')
            login_frame.destroy()
            main_frame.pack(fill=tk.BOTH, expand=True)
            return True
        else:
            return False

    main_frame = MainFrame(window)
    login_frame = LoginFrame(window, do_login)

    login_frame.pack(anchor=tk.CENTER, expand=True)
    
    window.mainloop()
