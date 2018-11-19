#!/usr/bin/env python3
import houndify
import sys
import os
import random
import time
import aiy.audio

CLIENT_ID = "bPmtPn-lV_rFXuxrww2GOw=="
CLIENT_KEY = "Vl56r8ewBSDhEdTfpFIWwuxhOqA01lF3aopxGH6aKOAEx9u8DMDpzsPFFed3M5-QaaiDGiMIlo-0p6Zk_1YfTQ=="
BUFFER_SIZE = 512
hasConversationState = False

exists = os.path.isfile('TiPodAuth.txt')
if exists:
    existFile = open("TiPodAuth.txt", "r")
    AUTHVAL = existFile.read()
else:
    file = open("TiPodAuth.txt","w")
    AUTHVAL = random.randint(1,99999999999999999999999999999999999999999999999999999999)    
    file.write(str(AUTHVAL)) 
    file.close()


def setTimer(timeToStart):
    timeRemaining = timeToStart;
    while timeRemaining > 0:
        timeRemaining -= 1
        time.sleep(1)
    aiy.audio.say("Time is up.")
    print("Time is up")
    finalResponse = "Time is up"
    
class TiriListener(houndify.HoundListener):
  def onPartialTranscript(self, transcript):
    print("Partial transcript: " + transcript)
  def onFinalResponse(self, response):
      print("#########################################")
      print("Final Response")
      if response["AllResults"][0]["CommandKind"] != "TimerCommand":
          aiy.audio.say(response["AllResults"][0]["SpokenResponseLong"])
          finalResponse = response["AllResults"][0]["SpokenResponseLong"]
      else:
          aiy.audio.say(response["AllResults"][0]["ClientActionSucceededResult"]["SpokenResponseLong"])
          finalResponse = response["AllResults"][0]["ClientActionSucceededResult"]["SpokenResponseLong"]
          setTimer(response["AllResults"][0]["NativeData"]["Timer"]["DurationInSeconds"])
      if response["AllResults"][0]["ConversationState"] != None:
          conversationStateFile = open("TiPodConversationState.txt","w")
          conversationStateFile.write(str(response["AllResults"][0]["ConversationState"]))
          conversationStateFile.close() 
      else:
          os.remove("TiPodConversationState.txt")
        
  def onError(self, err):
    print("Error: " + str(err))



client = houndify.StreamingHoundClient(CLIENT_ID, CLIENT_KEY, str(AUTHVAL))

client.setLocation(37.388309, -121.973968)

if os.path.isfile('TiPodConversationState.txt'):
    conversationStateFile = open("TiPodConversationState.txt","r")
    client.setConversationState(eval(conversationStateFile.read()))
    conversationStateFile.close()

client.start(TiriListener())

while True:
  samples = sys.stdin.buffer.read(BUFFER_SIZE)
  if len(samples) == 0: break
  if client.fill(samples): break
  
client.finish()
import main
