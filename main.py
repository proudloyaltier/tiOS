from tkinter import *

class TiOS:
	def __init__(self, master):
		self.master = master
		master.title = "TiOS"

root = Tk()

root.configure(background = "white")
root.attributes("-fullscreen", True)

gui = TiOS(root)
