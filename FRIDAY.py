import datetime
from http import server
from sqlite3 import Date
from unicodedata import name
from unittest import result
import wikipedia 
import webbrowser
import random
import os
import pyttsx3
import speech_recognition as sr
import smtplib
import weather1
import Timetable 
engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
# print(voice[0].id)
engine.setProperty('voice',voice[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("How can I help you sir?")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Say that again please... ")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("nairaaryan37@gamil.com","aa377@10")
    server.sendmail("nairaarayn37@gmail.com",to,content)
    server.close()
if __name__ == "__main__":
    while True:
        query=takeCommand().lower()
        if "friday are you there" in query:
            wishMe()  
        elif "sleep" in query:
            speak("Good Night Sir!")
        elif "today's schedule" in query:
            Timetable.tell()  
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("Accoring to wikipedia")
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/?hl=en")
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")
        elif "play music offline" in query:
            speak("Your Collection of offline music is been accessed.")
            music_dir="D:\\My\\songs"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,random.choice(songs)))
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is:{strTime}")
        elif "movie" in query:
            d="D:\\My\\Entertainment"
            os.startfile(d)
            speak("your collection of Movies has been accessed")
        elif "open vs code" in query:
            codepath="C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "python practice" in query:
            c="C:\\python programming\\hello.py\\Python Practice (Aashish code)"
            os.startfile(c)
        elif "infosys practice" in query:
            a="C:\\python programming\\hello.py"
            os.startfile(a)
        elif "infosys website" in query:
            webbrowser.open("https://infytq.onwingspan.com/en/page/home")
        elif "upsc study material" in query:
            a="D:\\My\\UPSC"
            os.startfile(a)
        elif "hindu analysis" in query:
            webbrowser.open("https://www.youtube.com/results?search_query=the+hindu+analysis+raj+malhotra")
        elif "send email" in query:
            try:
                speak("what should i send?")
                content=takeCommand()
                to="nairaarayn23@gmail.com"
                sendEmail(to,content)
                speak("Email has been send.")
            except Exception as e:
                print(e)
                speak("unable to send email.")
        elif "play music online" in query:
            webbrowser.open("https://open.spotify.com/playlist/196bFh93s3znoam2k4KfCJ")
            speak("your collection of online Music has been accessed")
        # elif "location" in query:
        #     speak(weather1.get_location())
        elif "weather" in query:
            speak(weather1.get_weather())
        elif "analysis of stocks" in query:
            webbrowser.open("https://www.tradingview.com/chart/owjzBcCb/")
            speak("i have opened trading view for you.")
        elif "remember that" in query:
            m=query.replace("Friday remember that I","")
            speak("ok sir")
            a=open("data.txt","w")
            a.write(m)
            a.close()
        elif "what are my reminders" in query:
            a=open("data.txt","r")
            speak("your reminders are: "+a.read())
        elif "schedule now" in query:
            speak(Timetable.time())