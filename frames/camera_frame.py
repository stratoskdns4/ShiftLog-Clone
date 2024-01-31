import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk

VIDEO_PATH = r'C:\Users\User\Documents\python_projects\human_detection\images\slotter.jpg'


class  MyVideoCapture:
	"""docstring for  MyVideoCapture"""
	def __init__(self, video_source=0):
		self.vid = cv2.VideoCapture(video_source)
		if not self.vid.isOpened():
			raise ValueError("unable open video source", video_source)

		self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

	def get_frame(self):
		if self.vid.isOpened():
			ret, frame = self.vid.read()
			if ret:
				return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
			else:
				return (ret, None)
		else:
			return (ret,None)

	def close(self):
		if self.vid.isOpened():
			self.vid.release()



class CameraFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)
        self.vid = MyVideoCapture(VIDEO_PATH)
		
        self.controls_frame = tk.Frame(self, height=30)
        self.controls_frame.config(bg='green')
        self.controls_frame.pack(fill=tk.X, padx=5, pady=5)
       

        self.list_frame = tk.Frame(self)
        self.slot_label = tk.Label(self.list_frame, text="Slot")
        self.slot_label.pack()

        self.slot_stringvar = tk.StringVar()
        self.slot_stringvar.set((1,2,3,4))
        self.slot_list_box = tk.Listbox(self.list_frame, listvariable=self.slot_stringvar)
        self.slot_list_box.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.list_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        self.canvas = tk.Canvas(self, width=500, height=300, bg='red')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        ret, frame = self.vid.get_frame()
		
        self.frame = frame
        self.update()
        self.bind("<Configure>", self.update)
        self.vid.close()

    def update(self, event=None):
        

        # if not ret:
        #     return
        self.canvas.update()
        image = PIL.Image.fromarray(self.frame)
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        image = image.resize((w, h))
        self.photo = PIL.ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # self.window.after(self.delay, self.update)


    def refresh(self):
        pass


if __name__ == "__main__":
    def single_frame_runner(frame_cls, frame_opts=None, dimensions=(500, 350), **options):
        root = tk.Tk(**options)
        root.geometry("{}x{}".format(*dimensions))
        
        if frame_opts is None:
            frame_opts = {}
        
        frame_cls(root, **frame_opts).pack(fill=tk.BOTH, expand=True)
        root.mainloop()

    single_frame_runner(CameraFrame)