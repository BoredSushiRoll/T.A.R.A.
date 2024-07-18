import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import wolframalpha
import webbrowser
import ctypes
import psutil
import pyautogui
import os
import sys
import subprocess
import random

opera_path = 'C:\\Users\\rares\\AppData\\Local\\Programs\\Opera GX\\launcher.exe'
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('U28AEV-J53JXH4L9K')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetings():
    current_hour = int(datetime.now().hour)
    if 0 <= current_hour < 12:
        return "Good morning boss!"
    elif 12 <= current_hour < 18:
        return "Hello boss!"
    else:
        return "Evening boss!"


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"You Said: {query}\n", )

    except Exception as e:
        print("Please say that Again...!")
        return takeCommand()
    return query


if __name__ == "__main__":
    greeting = greetings()
    speak(greeting)
    speak("How can I help you?")
    while True:
        query = takeCommand().lower()

        if 'open youtube' in query:
            speak('right away')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open facebook' in query:
            speak('sure thing!')
            webbrowser.open("facebook.com")

        elif 'open opera' in query:
            speak('got it !')
            os.startfile('C:\\Users\\rares\\AppData\\Local\\Programs\\Opera GX\\launcher.exe')

        elif 'play me something' in query:
            speak('Sure !')
            music_dir = 'E:\\Music\\'
            songs = os.listdir(music_dir)
            random_songs = music_dir + random.choice(songs)
            os.startfile(random_songs)

        elif 'what build are you' in query:
            speak('Currently I am in Alpha 001!')
            speak('Looking forward for updates boss!')

        elif 'lock PC' in query:
            speak('As You Wish')
            ctypes.windll.user32.LockWorkStation()

        elif 'screenshot' in query:
            speak('sure thing boss!')
            pic = pyautogui.screenshot()
            speak('ok it\'s done, i saved it on your desktop')
            pic.save('C:\\Users\\rares\\Desktop\\Screenshot.png')

        elif "what's up" in query or 'how are you TARA' in query:
            stMsgs = ['Just doing my thing!', 'I am fine !', 'Good !', 'Ready to take on the day with you !']
            speak(random.choice(stMsgs))

        elif 'hey' in query or 'Tara' in query:
            speak('Yes sir !, What can i do for you ? ')

        elif 'what is your name' in query:
            speak('My name is TARA or the long version: The Automated Remarkable Assistant!')

        elif 'who made you' in query:
            speak("I was created by BoredSushiRoll")

        elif 'bye TARA' in query or 'take a break' in query:
            speak('Bye sir ! have a great day !')
            sys.exit()

        else:
            query = query
            print("...")
            speak("Searching")
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    print(results)
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('According to wikipedia - ')
                    print(results)
                    speak(results)

            except:
                webbrowser.open('www.google.com')