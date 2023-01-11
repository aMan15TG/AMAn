import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import webbrowser

import wikipedia
from selenium import webdriver
r = sr.Recognizer()
engine = pyttsx3.init("voice")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume',7)

def talk(txt):
    engine.say(txt)
    engine.runAndWait()

def intro():
    currentTime = datetime.datetime.now()
    currentTime.hour
    hii=engine.say("hello")
    if currentTime.hour < 12:
        engine.say('Good morning ')
    elif 12 <= currentTime.hour < 18:
        engine.say('Good afternoon ')
    else:
        engine.say('Good evening sir')
    engine.say("I am your assistant. how can i help you")
    engine.runAndWait()
intro()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening your voice")
            audio = r.listen(source)
            command = r.recognize_google(audio)
            command = command.lower()
            print("please say something:",command)
            return command

    except:
        pass
def run_jarvis():
    command=take_command()
    if 'wikipedia' in command:
        talk('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=1)
        talk("According to Wikipedia")
        print(results)
        talk(results)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif "stop" in command:
        talk("thankyou")
        quit()

    elif "who are you" in command:
        talk(intro())

    elif "hello" in command:
        talk("hello i am your personal assistant")

    elif 'open google' in command:
        talk("opening google.com")
        webbrowser.open("google.com")

    elif 'open youtube' in command:
        talk("opening youtube.com")
        webbrowser.open("youtube.com")

    elif 'open facebook' in command:
        talk("facebook.com")
        webbrowser.open("facebook.com")
    else:
        talk('Please say the command again.')

while True:
    run_jarvis()