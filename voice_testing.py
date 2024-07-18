import speech_recognition as sr
import pyttsx3
import os
from datetime import datetime

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to list available voices
def list_voices():
    voices = tts_engine.getProperty('voices')
    for voice in voices:
        print(f"ID: {voice.id}\nName: {voice.name}\nLanguages: {voice.languages}\nGender: {voice.gender}\nAge: {voice.age}\n")

# Uncomment the following line to list all available voices
list_voices()