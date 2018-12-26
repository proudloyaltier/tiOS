#!/usr/bin/env python3

import os
import time
import subprocess
from datetime import datetime
from tkinter import *

# Tkinter Window Configuration

root = Tk()
root.configure(background = "white", cursor = "none")
root.attributes("-fullscreen", True)
root.title("TiOS")

# Tiri Card
button = PhotoImage(file = "Button.png")
tiriMic = PhotoImage(file = "microphone.png")
tiriMicSpeaking = PhotoImage(file = "microphoneActivated.png")
tiriResponse = PhotoImage(file = "TiriResponse.png")
power = PhotoImage(file = "power.png")
wifi = PhotoImage(file = "wifiReset.png")
startTiriButton = Button(root, relief="flat", highlightthickness=0, activebackground="white", borderwidth=0, bg = "white", image=tiriMic, compound=CENTER, command = lambda: startTiri())
startTiriButton.pack(anchor="w", side=TOP)
realtimeSpeaking = Label(root, text = "", font = "Roboto 24", bg = "white")
realtimeSpeaking.pack(anchor="center", side=TOP)
tiriCard = Button(root, relief="flat", highlightthickness=0, activebackground="white", borderwidth=0, bg = "white", image=tiriResponse, font = "Roboto 24", anchor="center", text="Hi! I'm Tiri!", compound=CENTER, command = lambda: openCard())
tiriCard.pack(pady=(0,0))
    
def openCard():
	response = open("TiPodFinalResponse.txt", "r")
	readResponseOpen = response.read()
	if (len(readResponseOpen) > 50):
		readResponseOpen = '\n'.join(readResponseOpen[i:i+50] for i in range(0, len(readResponseOpen), 50))
	response.close()
	expanded_frame = Frame(root, bg = "white")
	expanded_frame.pack()
	tile_title = Label(expanded_frame, text = "Tiri Response", font = "Roboto 24", bg = "white")
	tile_text = Label(expanded_frame, text = readResponseOpen, font = "Roboto 14", bg = "white")
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
	
def updateCard():
	if os.path.isfile('TiPodFinalResponse.txt'):
		response = open("TiPodFinalResponse.txt", "r")
		readResponse = response.read()
		response.close()
		if (len(readResponse) > 18):
			tiriCard['text'] = readResponse[0:15] + "..."
		else:
			tiriCard['text'] = readResponse
	else:
		tiriCard['text'] = "Hello! I'm Tiri!"
	tiriCard.after(1, updateCard)

updateCard()
	
# Time Label

clock = Label(root, text = "?:??", font = "Roboto 54", bg = "white")

clock.pack(pady = (5, 5))
powerOffButton = Button(root, relief="flat", highlightthickness=0, activebackground="white", borderwidth=0, bg = "white", image=power, compound=CENTER, command = lambda: powerOff())
powerOffButton.pack(side=LEFT)

wifiButton = Button(root, relief="flat", highlightthickness=0, activebackground="white", borderwidth=0, bg = "white", image=wifi, compound=CENTER, command = lambda: resetWifi())
wifiButton.pack(side=RIGHT)


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


if __name__ == '__main__':
	root.mainloop()
