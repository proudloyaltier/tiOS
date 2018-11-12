#!/usr/bin/env python3

import os
import time

from datetime import datetime
from tkinter import *

import urllib.request

# Variables

version = "0.0.8"

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
	i = 0
	while i < len(tiles):
		Button(root, text = tiles[i]["title"] + "\n\n" + tiles[i]["text"], width = 30, height = 10, border = 0, font = "Roboto 12", bg = "white", command = lambda x=i: openTile(tiles[x])).pack(anchor = "w", padx = (10, 10), pady = (10, 10))
		i += 1
# Updater

update_request = urllib.request.urlopen("https://proudloyaltier.github.io/TiOS/latest.html")
latest_version = update_request.read().decode("utf-8").replace("\n", "")

print("Checking for updates...")

if (version != latest_version):
	print("Downloading latest version...")

	download_request = urllib.request.urlopen("https://proudloyaltier.github.io/TiOS/main.py")
	downloaded_code = download_request.read().decode("utf-8")

	main_file = open(__file__, "w")

	main_file.write(downloaded_code)

	main_file.close()
else:
	print("TiOS is up to date!")

# Main

print("\nWelcome to TiOS!\nVersion: " + version + "\n\nStarting GUI...")

root = Tk()

root.configure(background = "white")
root.attributes("-fullscreen", True)

root.title = "TiOS"

# Wallpaper

background_image = PhotoImage(file = "images/wallpapers/default.png")
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
