import tkinter as tk
from applog import setup_logging
from frames.main_frame import MainFrame
from frames.login_frame import LoginFrame
from login_controller import LoginController


DEBUG = True


class App:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Καταγραφη!")
        self.window.geometry("1200x700")
        
        self.main_frame = None
        self.login_frame = None

    def go_to_main_view(self):
        if self.login_frame is not None:
            self.login_frame.destroy()
        self.main_frame = MainFrame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

    def go_to_login_view(self):
        if self.main_frame is not None:
            self.main_frame.destroy()
        self.login_frame = LoginFrame(self.window)
        self.login_frame.pack(anchor=tk.CENTER, expand=True)

    def run(self):
        self.go_to_login_view()
        lc = LoginController(self.go_to_main_view, self.go_to_login_view)

        if DEBUG:
            lc.do_login('aaaa', 'bbbb')
        
        logger.warning('mainloop of app')
        self.window.mainloop()
    


if __name__ == '__main__':
    import os

    # fix dpi issues on windows
    if os.name == 'nt':
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)

        
    logger = setup_logging()
    logger.debug('app.py: STARTING')

    app = App()
    app.run()
