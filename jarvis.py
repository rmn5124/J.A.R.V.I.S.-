import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

def openweb(link):
	chromedir= 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
	webbrowser.get(chromedir).open(link)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morining!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    
    else:
        speak("Good evening ")
    
    speak("How may i help you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognising...")
        query= r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again Please...")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak('According to Wikipedia')
            speak(results)

        elif 'open youtube' in query:
            openweb("youtube.com")

        elif 'open codeforces' in query:
            webbrowser.open("codeforces.com")

        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'F:\\Jarvis\\mus'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , The time is {strTime}")
            
        elif 'open vs code' in query:
            codePath = '"C:\\Users\\SUMAN BHARATI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codePath)

        elif 'turn off' in query:
            exit()
