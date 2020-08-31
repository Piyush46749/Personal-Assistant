import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
from selenium import webdriver

print('Loading your AI personal assistant - Chitti Robot')

voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate', 190)
# engine.setProperty('voice','voices[1].id')
engine.setProperty('voice',voice_id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening") 
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

wishMe()
speak("Your personal assistant Chitti Robot is here to help you")

if __name__=='__main__':


    while True:
        speak("How can I help you today?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement or "stop" in statement:
            speak('Okay bye. See you soon.')
            print('your personal assistant Chitti Robot is shutting down,Good bye')
            break