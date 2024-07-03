import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import smtplib

engine = pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Good Morning")
    elif hour>12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Divid assistant and I am your personal assistant. How can I help you?")

def takeCommand():
    #it take microphones input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")    
    except Exception as  e:
        print(e)

        print("Please repeat again...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtplib.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("VAISHNAVI.PATIL043@svkmmumbai.onmicrosoft.com","Karmad@2004")
    server.sendmail("VAISHNAVI.PATIL043@svkmmumbai.onmicrosoft.com",to,content)
    server.close()

if __name__== "__main__":
    speak("hello vaishnavi")
    wishMe()
    while True:
            query=takeCommand().lower()

           #logic for execution task based on uesr choice
            if 'wikipedia' in query:
                print("Searching in wikipedia...")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia..")
                print(results)
                speak(results)
            elif "open youtube" in query:
                webbrowser.open("youtube.com")

            elif "open google" in query:
                webbrowser.open("google.com")
       
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
            
            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"mam,The time is {strTime}")

            elif 'open code' in query:
                codePath="C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'open gmail' in query:
                webbrowser.open('gmail.com')
            elif 'play Music' in query:
                music_dir="C:\\Users\\Admin\\Desktop\\music"
                songs=os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))

            elif 'send email to vaishu' in query:
                try:
                    speak("What Should I write in Email Mam?")
                    content=takeCommand()
                    to="VAISHNAVI.PATIL043@svkmmumbai.onmicrosoft.com"
                    sendEmail(content,to)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry Vaishnavi Behen I am Not Able To send this email please Mujje Maff kar do ")

