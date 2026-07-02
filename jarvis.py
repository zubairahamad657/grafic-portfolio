import speech_recognition as sr
import win32com.client
import webbrowser
import os
from datetime import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")
recognizer = sr.Recognizer()

speaker.Speak("Hello. I am your voice assistant.")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio).lower()
        print("You said:", text)

        if "open google" in text:
            webbrowser.open("https://www.google.com")
            speaker.Speak("Opening Google")

        elif "open youtube" in text:
            webbrowser.open("https://www.youtube.com")
            speaker.Speak("Opening YouTube")


          
        elif "open notepad" in text:
            os.system("notepad")
            speaker.Speak("Opening Notepad")

        
        elif "close edge" in text:
            os.system("taskkill /F /IM edge.exe")
            speaker.Speak("Closing microsoft Edge")

        elif "time" in text:
            current_time = datetime.now().strftime("%I:%M %p")
            speaker.Speak("The current time is " + current_time)

        elif "exit" in text or "goodbye" in text:
            speaker.Speak("Goodbye")
            break

        else:
            speaker.Speak("You said " + text)

    except Exception as e:
        print("Error:", e)