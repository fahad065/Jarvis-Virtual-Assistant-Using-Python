import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It take microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mohammedfahad065@gmail.com', 'fahadabdulfaheem')
    server.sendmail('mohammedfahad065@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open google chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'email to fahad' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mohammedfahad065@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email at this moment")

        elif 'quit' in query:
            exit()
