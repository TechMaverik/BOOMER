#author:Akhil P Jacob
#HLDynamic-Integrations

from gtts import gTTS
import pygame
import pyttsx3
from playsound import playsound



def soundPlayer(location):
    try:
        playsound(location)
    except:
        return ("HLEngine:an issue in playing sound detected")


def saveAudio(param,location):
    try:
        mytext = param
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(location)
    except:
        return ("HLEngine:saveAudio issue detected")


def playAudio(location):
    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(location)
        pygame.mixer.music.play()
        pygame.event.wait()
    except:
        return ("HLEngine:playAudio issue detected")

def readText(param):
    try:
        engine = pyttsx3.init()
        engine.getProperty('rate')
        engine.setProperty('rate', 125)
        engine.say(param)
        engine.runAndWait()
    except:
        return ("HLEngine cannot load the required necessay files")



def readTextSpec(param):
    try:


        engine = pyttsx3.init()  # object creation

        """ RATE"""
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        print(rate)  # printing current voice rate
        engine.setProperty('rate', 125)  # setting up new voice rate

        """VOLUME"""
        volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        print(volume)  # printing current volume level
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

        """VOICE"""
        voices = engine.getProperty('voices')  # getting details of current voice
        # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female


        engine.say(param + str(rate))
        engine.runAndWait()
        engine.stop()

    except:

        return("HLEngine: An error occured in readAudioSpec")




