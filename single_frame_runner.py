import tkinter as tk

def single_frame_runner(frame_cls, frame_opts=None, dimensions=(500, 350), **options):
    root = tk.Tk(**options)
    root.geometry("{}x{}".format(*dimensions))
    
    if frame_opts is None:
        frame_opts = {}
    
    frame_cls(root, **frame_opts).pack(fill=tk.BOTH, expand=True)
    root.mainloop()