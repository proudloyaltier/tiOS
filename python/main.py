# TiOS v0.0.2 Alpha

import os
import time

from datetime import datetime
from tkinter import *

version = "0.0.2 Alpha"

print("Welcome to TiOS!\nVersion: " + version)

time.sleep(1)

print("\nStarting GUI...")

root = Tk()

root.configure(background = "white", cursor = "none")
root.attributes("-fullscreen", True)

root.title = "TiOS"

# Wallpaper

background_image = PhotoImage(file = "../images/wallpaper.png")
background_label = Label(root, image = background_image)

background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
background_label.image = background_image

# Time Label

current_time = datetime.now().time()

time_label = Label(root, text = current_time)
time_label.pack()
