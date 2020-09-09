import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
# from ecapture import ecapture as ec
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
        speak("Hello, Good Morning.")
        print("Hello, Good Morning.")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon.")
        print("Hello, Good Afternoon.")
    else:
        speak("Hello, Good Evening.") 
        print("Hello, Good Evening.")

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
speak("Your personal assistant Chitti Robot is here to help you!")

if __name__=='__main__':


    while True:
        speak("How can I help you today?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement or "stop" in statement:
            speak('Okay bye. See you soon.')
            print('Your personal assistant Chitti Robot is shutting down, good bye!')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open now.")
            time.sleep(4)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is open now.")
            time.sleep(4)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is open now.")
            time.sleep(4)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Chitti Robot version 1 point O your persoanl assistant. I am programmed to make your life easier and perform tasks such as, '
                  'opening youtube, google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement or "who developed you" in statement or "you were discovered by whom" in statement or "you were developed by whom" in statement or "you were built by whom" in statement:
            speak("I was built by Piyush")
            print("I was built by Piyush")

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India, Happy reading')
            time.sleep(5)

        # elif "camera" in statement or "take a photo" in statement:
        #     ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(4)

        elif 'calculate' in statement:
            speak('I can answer to computational and geographical questions. What question do you want to ask now?')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 seconds. Make sure you close all of your applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)