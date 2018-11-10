# TiOS v0.0.3 Alpha

import os
import time

from datetime import datetime
from tkinter import *

version = "0.0.3 Alpha"

# Variables

tiles = [{
	"title": "Test Tile",
	"text": "This is a random tile!"
}, {
	"title": "Another Tile",
	"text": "Why not have two?"
}]

# Tile Functions

def openTile(tile):
	frame = Frame(root, width = 1920, height = 1080, bg = "white")
	label = Label(text = tile["title"])
  
	frame.grid()
	label.grid(padx = (10, 10), pady = (10, 10))

def updateTiles():
	for tile in tiles:
		button = Button(root, text = tile["title"] + "\n\n" + tile["text"], width = 50, height = 20, command = lambda: openTile(tile))
		button.grid(padx = (10, 10), pady = (10, 10))

# Main

print("Welcome to TiOS!\nVersion: " + version)

time.sleep(1)

print("\nStarting GUI...")

root = Tk()

#root.configure(background = "white", cursor = "none")
root.attributes("-fullscreen", True)

root.title = "TiOS"

# Wallpaper

background_image = PhotoImage(file = "wallpaper.png")
background_label = Label(root, image = background_image)

background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
background_label.image = background_image

# Time Label

#current_time = datetime.now().time()

#time_label = Label(root, text = current_time)
#time_label.grid()

updateTiles()
