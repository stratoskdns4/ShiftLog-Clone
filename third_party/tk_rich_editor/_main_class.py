from tkinter import *
import tkinter as tk
import tkinter.filedialog as filedialog # filedialog allows user to select where they want to save the file.
import tkinter.font
import tkinter.colorchooser as colorchooser
import tkinter.ttk
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import os
import tkinter.messagebox as messagebox
from tkinter.filedialog import askopenfilename

# os.chdir(os.path.dirname(__file__))
# creating the root of the window.
# master = Tk()
# master.title("Untitled* - Script Editor")
# master.geometry("600x550")

# setting resizable window
# master.resizable(True, True)
# master.minsize(600, 550) # minimimum size possible

ASSETS = {}

def ImageOpenAsset(path, *args, **kwargs):
	if path in ASSETS:
		return ASSETS[path]
	path = os.path.join(os.path.dirname(__file__), path)
	img = Image.open(path, *args, **kwargs)
	img = img.resize((18, 18), Image.ANTIALIAS)
	ASSETS[path] = img
	return img


def PhotoImageAsset(img):
	path = os.path.join(os.path.dirname(__file__), "icons/copy.png")
	# return ImageTk.PhotoImage(Image.open(path).resize((18, 18), Image.ANTIALIAS), )
	# return ImageTk.PhotoImage(file=path)
	
	phimg = ImageTk.PhotoImage(img)

	#ASSETS.append(phimg)
	return phimg


class RichTextEditor(Frame):

		
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		# --------------- METHODS ---------------- #

		# MAIN MENU METHODS 

		self.file_name = "" # Current file name.
		self.current_font_family = "Liberation Mono"
		self.current_font_size = 12
		self.fontColor ='#000000'
		self.fontBackground= '#FFFFFF'

		
		# ------------- CREATING - MENUBAR AND ITS MENUS, TOOLS BAR, FORMAT BAR, STATUS BAR AND TEXT AREA -----------#
		
		# TOOLBAR
		self.toolbar = Frame(self, pady=2)

		# TOOLBAR BUTTONS
		# new
		self.new_button = Button(name="toolbar_b2", borderwidth=1, command=self.new, width=20, height=20)
		self.photo_new = ImageOpenAsset("icons/new.png")
		# photo_new = photo_new.resize((18, 18), Image.ANTIALIAS)
		self.image_new = PhotoImageAsset(self.photo_new)
		self.new_button.config(image=self.image_new)
		self.new_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

		# save
		self.save_button = Button(name="toolbar_b1", borderwidth=1, command=self.save, width=20, height=20)
		self.photo_save = ImageOpenAsset("icons/save.png")
		# photo_save = photo_save.resize((18, 18), Image.ANTIALIAS)
		self.image_save = PhotoImageAsset(self.photo_save)
		self.save_button.config(image=self.image_save)
		self.save_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

		#open
		self.open_button = Button(name="toolbar_b3", borderwidth=1, command=self.open_file, width=20, height=20)
		self.photo_open = ImageOpenAsset("icons/open.png")
		# photo_open = photo_open.resize((18, 18), Image.ANTIALIAS)
		self.image_open = PhotoImageAsset(self.photo_open)
		self.open_button.config(image=self.image_open)
		self.open_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

		# copy
		self.copy_button = Button(name="toolbar_b4", borderwidth=1, command=self.copy, width=20, height=20)
		self.photo_copy = ImageOpenAsset("icons/copy.png")
		# photo_copy = photo_copy.resize((18, 18), Image.ANTIALIAS)
		self.image_copy = PhotoImageAsset(self.photo_copy)
		self.copy_button.config(image=self.image_copy)
		self.copy_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

		#cut
		self.cut_button = Button(name="toolbar_b5", borderwidth=1, command=self.cut, width=20, height=20)
		self.photo_cut = ImageOpenAsset("icons/cut.png")
		# photo_cut = photo_cut.resize((18, 18), Image.ANTIALIAS)
		self.image_cut = PhotoImageAsset(self.photo_cut)
		self.cut_button.config(image=self.image_cut)
		self.cut_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

		# paste
		self.paste_button = Button(name="toolbar_b6", borderwidth=1, command=self.paste, width=20, height=20)
		self.photo_paste = ImageOpenAsset("icons/paste.png")
		# photo_paste = photo_paste.resize((18, 18), Image.ANTIALIAS)
		self.image_paste = PhotoImageAsset(self.photo_paste)
		self.paste_button.config(image=self.image_paste)
		self.paste_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

		# redo
		self.redo_button = Button(name="toolbar_b7", borderwidth=1, command=self.redo, width=20, height=20)
		self.photo_redo = ImageOpenAsset("icons/redo.png")
		# photo_redo = photo_redo.resize((18, 18), Image.ANTIALIAS)
		self.image_redo = PhotoImageAsset(self.photo_redo)
		self.redo_button.config(image=self.image_redo)
		self.redo_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

		# undo
		self.undo_button = Button(name="toolbar_b8", borderwidth=1, command=self.undo, width=20, height=20)
		self.photo_undo = ImageOpenAsset("icons/undo.png")
		# photo_undo = photo_undo.resize((18, 18), Image.ANTIALIAS)
		self.image_undo = PhotoImageAsset(self.photo_undo)
		self.undo_button.config(image=self.image_undo)
		self.undo_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

		# find
		self.find_button = Button(name="toolbar_b9", borderwidth=1, command=self.find_text, width=20, height=20)
		self.photo_find = ImageOpenAsset("icons/find.png")
		# photo_find = photo_find.resize((18, 18), Image.ANTIALIAS)
		self.image_find = PhotoImageAsset(self.photo_find)
		self.find_button.config(image=self.image_find)
		self.find_button.pack(in_=self.toolbar, side="left", padx=4, pady=4)

		# FORMATTING BAR
		self.formattingbar = Frame(self, padx=2, pady=2)

		# FORMATTING BAR COMBOBOX - FOR FONT AND SIZE
		# font combobox
		self.all_fonts = StringVar()
		self.font_menu = tkinter.ttk.Combobox(self.formattingbar, textvariable=self.all_fonts , state = "readonly")
		self.font_menu.pack(in_=self.formattingbar, side="left", padx=4, pady=4)
		self.font_menu['values'] = ( 'Courier', 'Helvetica', 'Liberation Mono', 'OpenSymbol', 'Century Schoolbook L', 'DejaVu Sans Mono', 'Ubuntu Condensed', 'Ubuntu Mono', 'Lohit Punjabi', 'Mukti Narrow', 'Meera', 'Symbola', 'Abyssinica SIL')
		self.font_menu.bind('<<ComboboxSelected>>', self.change_font)
		self.font_menu.current(2)

		# size combobox
		self.all_size = StringVar()
		self.size_menu = tkinter.ttk.Combobox(self.formattingbar, textvariable=self.all_size , state='readonly', width=5)
		self.size_menu.pack(in_=self.formattingbar, side="left", padx=4, pady=4)
		self.size_menu['values'] = ('10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30')
		self.size_menu.bind('<<ComboboxSelected>>', self.change_size)
		self.size_menu.current(1)

		# FORMATBAR BUTTONS
		#bold
		self.bold_button = Button(name="formatbar_b1", borderwidth=1, command=self.bold, width=20, height=20, pady=10, padx=10)
		self.photo_bold = ImageOpenAsset("icons/bold.png")
		# photo_bold = photo_bold.resize((18, 18), Image.ANTIALIAS)
		self.image_bold = PhotoImageAsset(self.photo_bold)
		self.bold_button.config(image=self.image_bold)
		self.bold_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

		# italic
		self.italic_button = Button(name="formatbar_b2", borderwidth=1, command=self.italic, width=20, height=20)
		self.photo_italic = ImageOpenAsset("icons/italic.png")
		# photo_italic = photo_italic.resize((18, 18), Image.ANTIALIAS)
		self.image_italic = PhotoImageAsset(self.photo_italic)
		self.italic_button.config(image=self.image_italic)
		self.italic_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

		# underline
		self.underline_button = Button(name="formatbar_b3", borderwidth=1, command=self.underline, width=20, height=20)
		self.photo_underline = ImageOpenAsset("icons/underline.png")
		# photo_underline = photo_underline.resize((18, 18), Image.ANTIALIAS)
		self.image_underline = PhotoImageAsset(self.photo_underline)
		self.underline_button.config(image=self.image_underline)
		self.underline_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

		# strike
		self.strike_button = Button(name="formatbar_b4", borderwidth=1, command=self.strike, width=20, height=20)
		self.photo_strike = ImageOpenAsset("icons/strike.png")
		# photo_strike = photo_strike.resize((18, 18), Image.ANTIALIAS)
		self.image_strike = PhotoImageAsset(self.photo_strike)
		self.strike_button.config(image=self.image_strike)
		self.strike_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

		# font_color
		self.font_color_button = Button(name="formatbar_b5", borderwidth=1, command=self.change_color, width=20, height=20)
		self.photo_font_color = ImageOpenAsset("icons/font-color.png")
		# photo_font_color = photo_font_color.resize((18, 18), Image.ANTIALIAS)
		self.image_font_color = PhotoImageAsset(self.photo_font_color)
		self.font_color_button.config(image=self.image_font_color)
		self.font_color_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

		# highlight
		self.highlight_button = Button(name="formatbar_b6", borderwidth=1, command=self.highlight, width=20, height=20)
		self.photo_highlight = ImageOpenAsset("icons/highlight.png")
		# photo_highlight = photo_highlight.resize((18, 18), Image.ANTIALIAS)
		self.image_highlight = PhotoImageAsset(self.photo_highlight)
		self.highlight_button.config(image=self.image_highlight)
		self.highlight_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

		# align_center
		self.align_center_button = Button(name="formatbar_b7", borderwidth=1, command=self.align_center, width=20, height=20)
		self.photo_align_center = ImageOpenAsset("icons/align-center.png")
		# photo_align_center = photo_align_center.resize((18, 18), Image.ANTIALIAS)
		self.image_align_center = PhotoImageAsset(self.photo_align_center)
		self.align_center_button.config(image=self.image_align_center)
		self.align_center_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

		# align_justify
		self.align_justify_button = Button(name="formatbar_b8", borderwidth=1, command=self.align_justify, width=20, height=20)
		self.photo_align_justify = ImageOpenAsset("icons/align-justify.png")
		# photo_align_justify = photo_align_justify.resize((18, 18), Image.ANTIALIAS)
		self.image_align_justify = PhotoImageAsset(self.photo_align_justify)
		self.align_justify_button.config(image=self.image_align_justify)
		self.align_justify_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

		# align_left
		self.align_left_button = Button(name="formatbar_b9", borderwidth=1, command=self.align_left, width=20, height=20)
		self.photo_align_left = ImageOpenAsset("icons/align-left.png")
		# photo_align_left = photo_align_left.resize((18, 18), Image.ANTIALIAS)
		self.image_align_left = PhotoImageAsset(self.photo_align_left)
		self.align_left_button.config(image=self.image_align_left)
		self.align_left_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

		# align_right
		self.align_right_button = Button(name="formatbar_b10", borderwidth=1, command=self.align_right, width=20, height=20)
		self.photo_align_right = ImageOpenAsset("icons/align-right.png")
		# photo_align_right = photo_align_right.resize((18, 18), Image.ANTIALIAS)
		self.image_align_right = PhotoImageAsset(self.photo_align_right)
		self.align_right_button.config(image=self.image_align_right)
		self.align_right_button.pack(in_=self.formattingbar, side="left", padx=4, pady=4)

		# STATUS BAR
		self.status = tk.Label(self, text="", bd=1, relief=SUNKEN, anchor=W)

		# CREATING TEXT AREA - FIRST CREATED A FRAME AND THEN APPLIED TEXT OBJECT TO IT.
		self.text_frame = tk.Frame(self, borderwidth=1, relief="sunken")
		self.text = tk.Text(wrap="word", font=("Liberation Mono", 12), background="white", borderwidth=0, highlightthickness=0 , undo= True)
		self.text.pack(in_=self.text_frame, side="left", fill="both", expand=True) # pack text object.

		# PACK TOOLBAR, FORMATBAR, STATUSBAR AND TEXT FRAME.
		self.toolbar.pack(side="top", fill="x")
		self.formattingbar.pack(side="top", fill="x")
		self.status.pack(side="bottom", fill="x")
		self.text_frame.pack(side="bottom", fill="both", expand=True)
		self.text.focus_set()

		# MENUBAR CREATION

		# menu = Menu(master)
		# master.config(menu=menu)

		# # File menu.
		# file_menu = Menu(menu)
		# menu.add_cascade(label="File", menu=file_menu, underline=0)

		# file_menu.add_command(label="New", command=new, compound='left', image=image_new, accelerator='Ctrl+N', underline=0) # command passed is here the method defined above.
		# file_menu.add_command(label="Open", command=open_file, compound='left', image=image_open, accelerator='Ctrl+O', underline=0)
		# file_menu.add_separator()
		# file_menu.add_command(label="Save", command=save, compound='left', image=image_save, accelerator='Ctrl+S', underline=0)
		# file_menu.add_command(label="Save As", command=save_as, accelerator='Ctrl+Shift+S', underline=1)
		# file_menu.add_command(label="Rename", command=rename, accelerator='Ctrl+Shift+R', underline=0)
		# file_menu.add_separator()
		# file_menu.add_command(label="Close", command=close, accelerator='Alt+F4', underline=0)

		# # Edit Menu.
		# edit_menu = Menu(menu)
		# menu.add_cascade(label="Edit", menu=edit_menu, underline=0)

		# edit_menu.add_command(label="Undo", command=undo, compound='left', image=image_undo, accelerator='Ctrl+Z', underline=0)
		# edit_menu.add_command(label="Redo", command=redo, compound='left', image=image_redo, accelerator='Ctrl+Y', underline=0)
		# edit_menu.add_separator()
		# edit_menu.add_command(label="Cut", command=cut, compound='left', image=image_cut, accelerator='Ctrl+X', underline=0)
		# edit_menu.add_command(label="Copy", command=copy, compound='left', image=image_copy, accelerator='Ctrl+C', underline=1)
		# edit_menu.add_command(label="Paste", command=paste, compound='left', image=image_paste, accelerator='Ctrl+P', underline=0)
		# edit_menu.add_command(label="Delete", command=delete, underline=0)
		# edit_menu.add_separator()
		# edit_menu.add_command(label="Select All", command=select_all, accelerator='Ctrl+A', underline=0)
		# edit_menu.add_command(label="Clear All", command=delete_all, underline=6)

		# #Tool Menu
		# tool_menu = Menu(menu)
		# menu.add_cascade(label="Tools", menu=tool_menu, underline=0)

		# tool_menu.add_command(label="Change Color", command=change_color)
		# tool_menu.add_command(label="Search", command=find_text, compound='left', image=image_find, accelerator='Ctrl+F')

		# Help Menu
		def about(event=None):
			messagebox.showinfo("About", "Text Editor\nCreated in Python using Tkinter\nCopyright with Amandeep and Harmanpreet, 2017")

		# help_menu = Menu(menu)
		# menu.add_cascade(label="Help", menu=help_menu, underline=0)
		# help_menu.add_command(label="About", command=about, accelerator='Ctrl+H', underline=0)

		# ----- BINDING ALL KEYBOARD SHORTCUTS ---------- #
		self.text.bind('<Control-n>', self.new)
		self.text.bind('<Control-N>', self.new) 

		self.text.bind('<Control-o>', self.open_file)
		self.text.bind('<Control-O>', self.open_file)

		self.text.bind('<Control-s>', self.save)
		self.text.bind('<Control-S>', self.save)

		self.text.bind('<Control-Shift-s>', self.save_as)
		self.text.bind('<Control-Shift-S>', self.save_as)

		self.text.bind('<Control-r>', self.rename)
		self.text.bind('<Control-R>', self.rename)

		self.text.bind('<Alt-F4>', self.close)
		self.text.bind('<Alt-F4>', self.close)

		self.text.bind('<Control-x>', self.cut)
		self.text.bind('<Control-X>', self.cut)

		self.text.bind('<Control-c>', self.copy)
		self.text.bind('<Control-C>', self.copy)

		self.text.bind('<Control-p>', self.paste)
		self.text.bind('<Control-P>', self.paste)

		self.text.bind('<Control-a>', self.select_all)
		self.text.bind('<Control-A>', self.select_all)

		self.text.bind('<Control-h>', about)
		self.text.bind('<Control-H>', about)

		self.text.bind('<Control-f>', self.find_text)
		self.text.bind('<Control-F>', self.find_text)

		self.text.bind('<Control-Shift-i>', self.italic)
		self.text.bind('<Control-Shift-I>', self.italic)

		self.text.bind('<Control-b>', self.bold)
		self.text.bind('<Control-B>', self.bold)

		self.text.bind('<Control-u>', self.underline)
		self.text.bind('<Control-U>', self.underline)

		self.text.bind('<Control-Shift-l>', self.align_left)
		self.text.bind('<Control-Shift-L>', self.align_left)

		self.text.bind('<Control-Shift-r>', self.align_right)
		self.text.bind('<Control-Shift-R>', self.align_right)

		self.text.bind('<Control-Shift-c>', self.align_center)
		self.text.bind('<Control-Shift-C>', self.align_center)

		# ---------- SETTING EVENTS FOR THE STATUS BAR -------------- #
		def on_enter(event, str):
			self.status.configure(text=str)


		def on_leave(event):
			self.status.configure(text="")

		self.new_button.bind("<Enter>", lambda event , str="New, Command - Ctrl+N":on_enter(event , str))
		self.new_button.bind("<Leave>", on_leave)

		self.save_button.bind("<Enter>", lambda event , str="Save, Command - Ctrl+S":on_enter(event , str))
		self.save_button.bind("<Leave>", on_leave)

		self.open_button.bind("<Enter>", lambda event , str="Open, Command - Ctrl+O":on_enter(event , str))
		self.open_button.bind("<Leave>", on_leave)

		self.copy_button.bind("<Enter>", lambda event , str="Copy, Command - Ctrl+C":on_enter(event , str))
		self.copy_button.bind("<Leave>", on_leave)

		self.cut_button.bind("<Enter>", lambda event , str="Cut, Command - Ctrl+X":on_enter(event , str))
		self.cut_button.bind("<Leave>", on_leave)

		self.paste_button.bind("<Enter>", lambda event , str="Paste, Command - Ctrl+P":on_enter(event , str))
		self.paste_button.bind("<Leave>", on_leave)

		self.undo_button.bind("<Enter>", lambda event , str="Undo, Command - Ctrl+Z":on_enter(event , str))
		self.undo_button.bind("<Leave>", on_leave)

		self.redo_button.bind("<Enter>", lambda event , str="Redo, Command - Ctrl+Y":on_enter(event , str))
		self.redo_button.bind("<Leave>", on_leave)

		self.find_button.bind("<Enter>", lambda event , str="Find, Command - Ctrl+F":on_enter(event , str))
		self.find_button.bind("<Leave>", on_leave)

		self.bold_button.bind("<Enter>", lambda event , str="Bold, Command - Ctrl+B":on_enter(event , str))
		self.bold_button.bind("<Leave>", on_leave)

		self.italic_button.bind("<Enter>", lambda event , str="Italic, Command - Ctrl+Shift+I":on_enter(event , str))
		self.italic_button.bind("<Leave>", on_leave)

		self.underline_button.bind("<Enter>", lambda event , str="Underline, Command - Ctrl+U":on_enter(event , str))
		self.underline_button.bind("<Leave>", on_leave)

		self.align_justify_button.bind("<Enter>", lambda event , str="Justify":on_enter(event , str))
		self.align_justify_button.bind("<Leave>", on_leave)

		self.align_left_button.bind("<Enter>", lambda event , str="Align Left, Command - Control-Shift-L":on_enter(event , str))
		self.align_left_button.bind("<Leave>", on_leave)

		self.align_right_button.bind("<Enter>", lambda event , str="Align Right, Command - Control-Shift-R":on_enter(event , str))
		self.align_right_button.bind("<Leave>", on_leave)

		self.align_center_button.bind("<Enter>", lambda event , str="Align Center, Command - Control-Shift-C":on_enter(event , str))
		self.align_center_button.bind("<Leave>", on_leave)

		self.strike_button.bind("<Enter>", lambda event , str="Strike":on_enter(event , str))
		self.strike_button.bind("<Leave>", on_leave)

		self.font_color_button.bind("<Enter>", lambda event , str="Font Color":on_enter(event , str))
		self.font_color_button.bind("<Leave>", on_leave)

		self.highlight_button.bind("<Enter>", lambda event , str="Highlight":on_enter(event , str))
		self.highlight_button.bind("<Leave>", on_leave)

		self.strike_button.bind("<Enter>", lambda event , str="Strike":on_enter(event , str))
		self.strike_button.bind("<Leave>", on_leave)

		
	def make_tag(self):
		current_tags = self.text.tag_names()
		if "bold" in current_tags:
			weight = "bold"
		else:
			weight = "normal"

		if "italic" in current_tags:
			slant = "italic"
		else:
			slant = "roman"

		if "underline" in current_tags:
			underline = 1
		else:
			underline = 0

		if "overstrike" in current_tags:
			overstrike = 1
		else:
			overstrike = 0

		big_font = tkinter.font.Font(self.text, self.text.cget("font"))
		big_font.configure(slant= slant , weight= weight , underline= underline , overstrike= overstrike , family= self.current_font_family , size= self.current_font_size )
		self.text.tag_config("BigTag", font=big_font , foreground= self.fontColor , background= self.fontBackground) 
		if "BigTag" in  current_tags:
			self.text.tag_remove("BigTag" , 1.0 , END)
		self.text.tag_add("BigTag" , 1.0 , END)

	def new(self, event=None):
		file_name = ""
		ans = messagebox.askquestion(title="Save File" , message="Would you like to save this file")
		if ans is True:
			self.save()
		self.delete_all()

	def open_file(self, event=None):
		self.new()
		file = filedialog.askopenfile()
		self.file_name = file.name
		self.text.insert(INSERT , file.read())

	def save(self, event=None):
		if self.file_name == "":
			path = filedialog.asksaveasfilename()
			self.file_name = path
		# self.title(self.file_name + " - Script Editor")
		write = open(self.file_name, mode='w')
		write.write(self.text.get("1.0", END))

	def save_as(self, event=None):
		if self.file_name == "":
			self.save()
			return "break"
		f = filedialog.asksaveasfile(mode='w')
		if f is None: 
			return
		text2save = str(self.text.get(1.0, END)) 
		f.write(text2save)
		f.close() 

	new_name = ""  # Used for renaming the file

	def rename(self, event=None):
		if self.file_name == "":
			self.open_file()

		arr = self.file_name.split('/')
		path = ""
		for i in range(0 , len(arr) -1):
			path = path + arr[i] + '/'
		
		new_name = simpledialog.askstring("Rename", "Enter new name")
		os.rename(file_name , str(path) + str(new_name))
		file_name = str(path) + str(new_name)
		# self.title(file_name + " - Script Editor")


	def close(self, event=None):
		self.save()
		self.quit()

	# EDIT MENU METHODS

	def cut(self, event=None):
		# first clear the previous text on the clipboard.
		self.clipboard_clear()
		self.text.clipboard_append(string=self.text.selection_get())
		#index of the first and yhe last letter of our selection.
		self.text.delete(index1=SEL_FIRST, index2=SEL_LAST)


	def copy(self, event=None):
		# first clear the previous text on the clipboard.
		print(self.text.index(SEL_FIRST))
		print(self.text.index(SEL_LAST))
		self.clipboard_clear()
		self.text.clipboard_append(string=self.text.selection_get())

	def paste(self, event=None):
		# get gives everyting from the clipboard and paste it on the current cursor position
		# it does'nt removes it from the clipboard.
		self.text.insert(INSERT, self.clipboard_get())

	def delete(self):
		self.text.delete(index1=SEL_FIRST, index2=SEL_LAST)

	def undo(self):
		self.text.edit_undo()

	def redo(self):
		self.text.edit_redo()

	def select_all(self, event=None):
		self.text.tag_add(SEL, "1.0", END)

	def delete_all(self):
		self.text.delete(1.0, END)

	# TOOLS MENU METHODS

	def change_color(self):
		color = colorchooser.askcolor(initialcolor='#ff0000')
		color_name = color[1]
		self.fontColor = color_name
		current_tags = self.text.tag_names()
		if "font_color_change" in current_tags:
			# first char is bold, so unbold the range
			self.text.tag_delete("font_color_change", 1.0 , END)
		else:
			# first char is normal, so bold the whole selection
			self.text.tag_add("font_color_change", 1.0 , END)
		self.make_tag()

	# Adding Search Functionality

	def check(self, value):
		self.text.tag_remove('found', '1.0', END)
		self.text.tag_config('found', foreground='red')
		list_of_words = value.split(' ')
		for word in list_of_words:
			idx = '1.0'
			while idx:
				idx = self.text.search(word, idx, nocase=1, stopindex=END)
				if idx:
					lastidx = '%s+%dc' % (idx, len(word))
					self.text.tag_add('found', idx, lastidx)
					print(lastidx)
					idx = lastidx

	# implementation of search dialog box - calling the check method to search and find_text_cancel_button to close it
	def find_text(self, event=None):
		search_toplevel = Toplevel(self)
		search_toplevel.title('Find Text')
		search_toplevel.transient(self)
		search_toplevel.resizable(False, False)
		Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
		search_entry_widget = Entry(search_toplevel, width=25)
		search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
		search_entry_widget.focus_set()
		Button(search_toplevel, text="Ok", underline=0, command=lambda: self.check( search_entry_widget.get())).grid(row=0, column=2, sticky='e' +'w', padx=2, pady=5)
		Button(search_toplevel, text="Cancel", underline=0, command=lambda: self.find_text_cancel_button(search_toplevel)).grid(row=0, column=4, sticky='e' +'w', padx=2, pady=2)

	# remove search tags and destroys the search box
	def find_text_cancel_button(self, search_toplevel):
		self.text.tag_remove('found', '1.0', END)
		search_toplevel.destroy()
		return "break"

	# FORMAT BAR METHODS

	def bold(self, event=None):
		current_tags = self.text.tag_names()
		if "bold" in current_tags:
			# first char is bold, so unbold the range
			self.text.tag_delete("bold",  1.0, END)
		else:
			# first char is normal, so bold the whole selection
			self.text.tag_add("bold", 1.0, END)
		self.make_tag()

	def italic(self, event=None):
		current_tags = self.text.tag_names()
		if "italic" in current_tags:
			self.text.tag_add("roman",  1.0, END)
			self.text.tag_delete("italic", 1.0, END)
		else:
			self.text.tag_add("italic",  1.0, END)
		self.make_tag()

	def underline(self, event=None):
		current_tags = self.text.tag_names()
		if "underline" in current_tags:
			self.text.tag_delete("underline",  1.0, END)
		else:
			self.text.tag_add("underline",  1.0, END)
		self.make_tag()

	def strike(self):
		current_tags = self.text.tag_names()
		if "overstrike" in current_tags:
			self.text.tag_delete("overstrike" ,"1.0", END)
			
		else:
			self.text.tag_add("overstrike" , 1.0, END)
		
		self.make_tag()

	def highlight(self):
		color = colorchooser.askcolor(initialcolor='white')
		color_rgb = color[1]
		global fontBackground
		fontBackground= color_rgb
		current_tags = self.text.tag_names()
		if "background_color_change" in current_tags:
			self.text.tag_delete("background_color_change", "1.0", END)
		else:
			self.text.tag_add("background_color_change", "1.0", END)
		self.make_tag()


	# To make align functions work properly
	def remove_align_tags(self):
		all_tags = self.text.tag_names(index=None)
		if "center" in all_tags:
			self.text.tag_remove("center", "1.0", END)
		if "left" in all_tags:
			self.text.tag_remove("left", "1.0", END)
		if "right" in all_tags:
			self.text.tag_remove("right", "1.0", END)

	# align_center
	def align_center(self, event=None):
		self.remove_align_tags()
		self.text.tag_configure("center", justify='center')
		self.text.tag_add("center", 1.0, "end")

	# align_justify
	def align_justify(self):
		self.remove_align_tags()

	# align_left
	def align_left(self, event=None):
		self.remove_align_tags()
		self.text.tag_configure("left", justify='left')
		self.text.tag_add("left", 1.0, "end")

	# align_right
	def align_right(self, event=None):
		self.remove_align_tags()
		self.text.tag_configure("right", justify='right')
		self.text.tag_add("right", 1.0, "end")

	# Font and size change functions - BINDED WITH THE COMBOBOX SELECTION
	# change font and size are methods binded with combobox, calling fontit and sizeit
	# called when <<combobox>> event is called

	def change_font(self, event):
		f = self.all_fonts.get()
		self.current_font_family = f
		self.make_tag()

	def change_size(self, event):
		sz = int(self.all_size.get())
		self.current_font_size = sz
		self.make_tag()

	
	def get_text_widget(self):
		return self.text



if __name__ == "__main__":
	# creating the root of the window.
	self = Tk()
	self.title("Untitled* - Script Editor")
	self.geometry("600x550")

	# setting resizable window
	self.resizable(True, True)
	self.minsize(600, 550) # minimimum size possible

	editor = RichTextEditor(self)
	editor.pack(fill=BOTH)
	self.mainloop()