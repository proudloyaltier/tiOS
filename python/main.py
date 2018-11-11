# TiOS v0.0.6 Alpha

import os
import time

from datetime import datetime
from tkinter import *

version = "0.0.6 Alpha"

# Variables

tiles = [{
	"title": "Test Tile",
	"text": "This is a random tile!"
}, {
	"title": "Another Tile",
	"text": "Why not have two?"
}]

tiles_screen = []

# Tile Functions

def openTile(tile):
	tile_frame = Frame(root, bg = "white")
	tile_title = Label(tile_frame, text = tile["title"], font = "Roboto 24", bg = "white")
	tile_text = Label(tile_frame, text = tile["text"], font = "Roboto 14", bg = "white")
	tile_back_button = Button(tile_frame, text = "Back", border = 0, font = "Roboto 12")

	tile_back_button.configure(command = lambda: closeTile(tile_frame, tile_title, tile_text, tile_back_button))

	tile_frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)

	tile_title.grid(padx = (25, 25), pady = (25, 25))
	tile_text.grid(padx = (25, 25))
	tile_back_button.grid()

def closeTile(frame, title, text, button):
	frame.destroy()
	title.destroy()
	text.destroy()
	button.destroy()

def updateTiles():
	for tile in tiles:
		tile_button = Button(root, text = tile["title"] + "\n\n" + tile["text"], width = 30, height = 10, border = 0, font = "Roboto 12", bg = "white", command = lambda: openTile(tile))

		tile_button.pack(anchor = "w", padx = (10, 10), pady = (10, 10))

# Main

print("Welcome to TiOS!\nVersion: " + version + "\n\nStarting GUI...")

root = Tk()

root.configure(background = "white")
root.attributes("-fullscreen", True)

root.title = "TiOS"

# Wallpaper

background_image = PhotoImage(file = "wallpaper.png")
background_label = Label(root, image = background_image)

background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Time Label

clock = Label(root, text = "?:??", font = "Roboto 54", bg = "white")

clock.pack(pady = (25, 25))

def tick():
	clock.configure(text = time.strftime("%H:%M:%S"))
	clock.after(1000, tick)

tick()

updateTiles()
