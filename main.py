import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning !")
    elif 12 <= hour < 18:
        speak("Good Afternoon !")
    else:
        print("Good Evening !")
    speak("I am jarvis Sir or Mam. Please tell me how may I help you.")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .......")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognizing .....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please ........")
        return "None"
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia ......')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com", new=2)
        elif 'open google' in query:
            webbrowser.open("google.com", new=2)
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com", new=2)
        elif 'tell time' in query or 'tell the time' in query:
            strTime = datetime.datetime.now().strftime('%H-%M-%S %d %B %y ')
            print(f"The current time is {strTime}")
            speak(strTime)
        elif 'open vs code' in query:
            speak("Opening VS code")
            os.startfile('C:\\Users\\Omkar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
        elif 'open pycharm' in query:
            speak("Opening Pycharm")
            os.startfile('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.3.3\\bin\\pycharm64.exe')
        elif 'open edge' in query:
            speak("Opening Edge")
            os.startfile('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
        else:
            print("No command found for your input.")
