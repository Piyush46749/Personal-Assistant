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
