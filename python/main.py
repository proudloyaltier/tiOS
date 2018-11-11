# TiOS v0.0.5 Alpha

import os
import time

from datetime import datetime
from tkinter import *

version = "0.0.5 Alpha"

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
	tile_title = Label(tile_frame, text = tile["title"], font = "Roboto 24")
	tile_text = Label(tile_frame, text = tile["text"], font = "Roboto 14")
	tile_back_button = Button(tile_frame, text = "Back")

	tile_back_button.configure(command = lambda: closeTile(tile_frame, tile_title, tile_text, tile_back_button))

	tile_frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)

	tile_title.grid()
	tile_text.grid()
	tile_back_button.grid()

def closeTile(frame, title, text, button):
	frame.destroy()
	title.destroy()
	text.destroy()
	button.destroy()

def updateTiles():
	for tile in tiles:
		tile_button = Button(root, text = tile["title"] + "\n\n" + tile["text"], font = "Roboto", width = 50, height = 20, command = lambda: openTile(tile))
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

clock = Label(root, text = "?:??", font = "Roboto 24", anchor = "center")
clock.grid(padx = (1, 1), pady = (1, 1))

def tick():
	current_time = time.strftime("%H:%M:%S")

	clock.config(text = current_time)
	clock.after(1000, tick)

tick()

updateTiles()
