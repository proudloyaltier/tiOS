#!/usr/bin/env python3

import os
import time
import subprocess
from datetime import datetime
from tkinter import *

# Tkinter Window Configuration

tiles = []
root = Tk()
root.configure(background = "white", cursor = "none")
root.attributes("-fullscreen", True)
root.title("TiOS")

button = PhotoImage(file = "Button.png")
tiriMic = PhotoImage(file = "microphone.png")
tiriMicSpeaking = PhotoImage(file = "microphoneActivated.png")
tiriResponse = PhotoImage(file = "TiriResponse.png")
tiriResponsePowerHelp = PhotoImage(file = "PowerHelp.png")
tiriResponseWifiHelp = PhotoImage(file = "WifiHelp.png")
tiriResponseHelp = PhotoImage(file = "StartTiri.png")
power = PhotoImage(file = "power.png")
wifi = PhotoImage(file = "wifiReset.png")
startTiriButton = Button(root, relief="flat", highlightthickness=0, activebackground="white", borderwidth=0, bg = "white", image=tiriMic, compound=CENTER, command = lambda: startTiri())
startTiriButton.pack(anchor="w", side=TOP)
realtimeSpeaking = Label(root, text = "", font = "Roboto 24", bg = "white")
realtimeSpeaking.pack(anchor="center", side=TOP)
cardFrame = Frame(root)

# Tiri Card
def loadTiles():
	for widget in cardFrame.winfo_children():
	    widget.destroy()
	if len(tiles) >= 5:
		lengthOfFor = 5
	else:
		lengthOfFor = len(tiles)
	for i in range(0, lengthOfFor):
		tiriCard = Button(cardFrame, relief="flat", highlightthickness=0, activebackground="white", borderwidth=0, bg = "white", image=tiriResponse, font = "Roboto 24", anchor="center", text="Hi! I'm Tiri!", compound=CENTER, command = lambda x=i: openCard(x))
		tiriCard.pack(side=LEFT)
		if (len(tiles[i]) > 5):
			tiriCard['text'] = tiles[i][0:5] + "..."
		else:
			tiriCard['text'] = tiles[i]
	cardFrame.pack()
	
def openCard(i):
	expanded_frame = Frame(root, bg = "white")
	expanded_frame.pack()
	tile_title = Label(expanded_frame, text = "Tiri Response", font = "Roboto 24", bg = "white")
	tile_text = Label(expanded_frame, text = tiles[i], font = "Roboto 14", bg = "white")
	tile_button = Button(expanded_frame, relief="flat", highlightthickness=0, activebackground="white", borderwidth=0, text = "Back", font = "Roboto 24", bg = "white", image=button, anchor="center", compound=CENTER, command = lambda: closeCard(expanded_frame, tile_title, tile_text, tile_button))
	expanded_frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)
	tile_title.grid(padx = (25, 25), pady = (25, 25))
	tile_text.grid(padx = (25, 25))
	tile_button.grid()
	
def closeCard(frame, title, text, button):
	frame.destroy()
	title.destroy()
	text.destroy()
	button.destroy()
	
	
# Time Label

clockFrame = Frame(root, bg="white")
powerOffButton = Button(clockFrame, relief="flat", highlightthickness=0, activebackground="white", borderwidth=0, bg = "white", image=power, compound=CENTER, command = lambda: powerOff())
powerOffButton.pack(side=LEFT)

wifiButton = Button(clockFrame, relief="flat", highlightthickness=0, activebackground="white", borderwidth=0, bg = "white", image=wifi, compound=CENTER, command = lambda: resetWifi())
wifiButton.pack(side=RIGHT)
clock = Label(clockFrame, text = "?:??", font = "Roboto 54", bg = "white")
clock.pack(pady = (5, 5))
clockFrame.pack()

def tick():
	clock.configure(text = time.strftime("%H:%M:%S"))
	clock.after(1000, tick)

tick()

def startTiri():
	startTiriButton.configure(image = tiriMicSpeaking)
	startTiriButton.image = tiriMicSpeaking
	subprocess.Popen("arecord -t raw -c 1 -r 16000 -f S16_LE | ./TiriUI.py", shell = True)


def powerOff():
	subprocess.Popen("sudo shutdown now", shell = True)


def resetWifi():
	subprocess.Popen("sudo python3 /usr/lib/raspiwifi/reset_device/manual_reset.py", shell = True)



def updateSpeaking():
	if os.path.isfile('TiPodTranscription.txt'):
		response = open("TiPodTranscription.txt", "r")
		readResponseTrans = response.read()
		response.close()
		startTiriButton.configure(image = tiriMicSpeaking)
		startTiriButton.image = tiriMicSpeaking
		if readResponseTrans == "":
			startTiriButton.configure(image = tiriMic)
			startTiriButton.image = tiriMic
		if (len(readResponseTrans) > 50):
			realtimeSpeaking['text'] = readResponseTrans[0:47] + "..."
		else:
			realtimeSpeaking['text'] = readResponseTrans
	else:
		
		startTiriButton.configure(image = tiriMic)
		startTiriButton.image = tiriMic
		realtimeSpeaking['text'] = ""
	realtimeSpeaking.after(1, updateSpeaking)
	
updateSpeaking()

def updateCard():
	if os.path.isfile('TiPodFinalResponse.txt'):
		response = open("TiPodFinalResponse.txt", "r")
		readResponse = response.read()
		response.close()
		if len(readResponse) > 1:
			tiles.append(readResponse)
			response = open("TiPodFinalResponse.txt", "w")
			response.write("")
			response.close()
			cardFrame.pack_forget()
			loadTiles()
	realtimeSpeaking.after(1, updateCard)

updateCard()

if __name__ == '__main__':
	root.mainloop()
