import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import os
import pyaudio
import sys
import webbrowser
import time
import urllib.request

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name






def there_exists(terms):
    for term in terms:
        if term in statement:
            return True




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
engine.setProperty('volume',1.0)


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



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        statement = ''

        

        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading your AI personal assistant Bright")
speak("Loading your AI personal assistant Bright")
wishMe()
takeCommand()

if __name__=='__main__':


 while True:
     speak("how can I help you today ?")
     statement = takeCommand().lower()
     if statement==0:
         continue

     if "good bye" in statement or "ok bye" in statement or "stop" in statement or "shut down" in statement:
        speak('I am shutting down,Good bye')
        print('I am shutting down,Good bye')
        sys.exit()



     if 'wikipedia' in statement:
         speak('Searching Wikipedia...')
         statement = statement.replace("wikipedia", "")
         results = wikipedia.summary(statement, sentences=8)
         speak("According to Wikipedia")
         print(results)
         speak(results)


     if "open youtube" in statement:
         webbrowser.open_new_tab("https://www.youtube.com")
         speak("youtube is open now")
         time.sleep(5)

     if there_exists(["play on youtube"]):
         search_term = statement.split("for")[-1]
         url = "https://www.youtube.com/results?search_query=" + search_term
         webbrowser.get().open(url)
         speak("Here is what i found for" + search_term +"on youtube")



     if there_exists(["search for"]) and 'youtube' not in statement:
        search_term = statement.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        speak("Here is what I found for" + search_term + "on google")

     if there_exists(["play on spotify "]):
         search_term = statement.split("for")[-1]
         url = "https://open.spotify.com/search/" + search_term
         webbrowser.get().open(url)
         speak("You are listening to" + search_term + "enjoy sir")

