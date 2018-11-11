# TiOS v0.0.4 Alpha

import os
import time

from datetime import datetime
from tkinter import *

version = "0.0.4 Alpha"

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
	tile_frame = Frame(root, bg = "white")
	tile_label = Label(tile_frame, text = tile["title"], font = "Times 24")
	tile_back_button = Button(tile_frame, text = "Back")

	tile_back_button.configure(command = lambda: closeTile(tile_frame, tile_label, tile_back_button))

	tile_frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)

	tile_label.grid()
	tile_back_button.grid()

def closeTile(frame, label, button):
	root.grid_remove()
	label.grid_remove()
	button.grid_remove()

def updateTiles():
	for tile in tiles:
		tile_button = Button(root, text = tile["title"] + "\n\n" + tile["text"], width = 50, height = 20, command = lambda: openTile(tile))
		tile_button.grid(padx = (10, 10), pady = (10, 10))

# Main

print("Welcome to TiOS!\nVersion: " + version + "\n\nStarting GUI...")

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

clock = Label(root, text = "?:??", font = "Times 54", anchor = "center")
clock.grid(padx = (1, 1), pady = (1, 1))

def tick():
	current_time = time.strftime("%H:%M:%S")

	clock.config(text = current_time)
	clock.after(1000, tick)

tick()

updateTiles()
