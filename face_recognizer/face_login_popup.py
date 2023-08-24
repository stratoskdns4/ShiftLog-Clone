import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import time

from .recognize_faces import load_facial_data, recongnize_from_cv2_video_frame
from login_controller import LoginController
import os

class FaceLoginPopup:

	def __init__(self, master, window_title='Face Login', video_source=0):
		self.window = tk.Toplevel(master)
		self.window.title = window_title
		self.video_source = video_source
		self.TARGET_FPS = 5

		face_fb_path = os.path.join(os.path.dirname(__file__), 'face_db')
		face_dir_path = os.path.join(os.path.dirname(__file__), 'known_faces')
		self.facial_data = load_facial_data(face_fb_path, fallback_face_dir=face_dir_path)

		self.vid = MyVideoCapture(self.video_source)
		self.canvas = tk.Canvas(self.window, width=self.vid.width, height=self.vid.height)
		self.canvas.pack()


		btn_frame = tk.Frame(self.window, background=self.from_rgb((117, 123, 129)))
		btn_frame.place(x=0,y=0, anchor="nw", width=self.vid.width+4)

		# self.btn_snapshot=tkinter.Button(btn_frame, text="Snapshot",width=20, command=self.snapshot, bg=self.from_rgb((52, 61, 70)), fg="white")
		# self.btn_snapshot.pack(side="left", padx=10, pady=10)

		# self.btn_proses=tkinter.Button(btn_frame, text="Proses", width=10, command=None, bg=self.from_rgb((52, 61, 70)), fg="white")
		# self.btn_proses.pack(side="left", padx=10, pady=10)

		# self.btn_about=tkinter.Button(btn_frame, text="About", width=10, command=None, bg=self.from_rgb((52, 61, 70)), fg="white")
		# self.btn_about.pack(side="right", padx=10, pady=10)

		self.delay = 1000 // self.TARGET_FPS
		self.update()
		
		self.window.mainloop()

	def snapshot(self):
		ret, frame=self.vid.get_frame()

		if ret:
			cv2.imwrite("frame-"+time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) )

	def update(self):
		ret, frame = self.vid.get_frame()

		if not ret:
			return
		
		results = recongnize_from_cv2_video_frame(frame, self.facial_data)
		self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
		self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

		# if a know face is found, try to log the coresponding user in
		if results:
			try:
				user_id = int(results[0])
				if LoginController().log_user_by_id(user_id):
					self.vid.close()
					self.window.destroy()
					return
			except ValueError:
				pass

		self.window.after(self.delay, self.update)

	def from_rgb(self,rgb):
		return "#%02x%02x%02x" % rgb


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

	# def __del__(self):
	# 	pass


if __name__ == '__main__':
	import os

	os.chdir(os.path.dirname(__file__))
	root = tk.Tk()
	FaceLoginPopup(root)
	root.mainloop()