import speech_recognition as sr
import win32com.client
import webbrowser
import os
from datetime import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")
recognizer = sr.Recognizer()

speaker.Speak("Hello. I am  jarvis . How can I help you?")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        # OPEN COMMANDS
        if"open google" in command:
            webbrowser.open("https://www.google.com")
            speaker.Speak("Opening Google")

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            speaker.Speak("Opening YouTube")

        elif "open instagram" in command:
            webbrowser.open("https://www.instagram.com")
            speaker.Speak("Opening Instagram")

        elif "open facebook" in command:
            webbrowser.open("https://www.facebook.com")
            speaker.Speak("Opening Facebook")

        elif "open github" in command:
            webbrowser.open("https://github.com")
            speaker.Speak("Opening GitHub")

        elif "open chatgpt" in command:
            webbrowser.open("https://chatgpt.com")
            speaker.Speak("Opening Chat GPT")

        elif "open notepad" in command:
            os.system("notepad")
            speaker.Speak("Opening Notepad")

        elif "open calculator" in command:
            os.system("calc")
            speaker.Speak("Opening Calculator")

        elif "open command prompt" in command:
            os.system("start cmd")
            speaker.Speak("Opening Command Prompt")

        # CLOSE COMMANDS
        elif "close notepad" in command:
            os.system("taskkill /F /IM notepad.exe")
            speaker.Speak("Closing Notepad")

        elif "close calculator" in command:
            os.system("taskkill /F /IM CalculatorApp.exe")
            speaker.Speak("Closing Calculator")

        elif "close chrome" in command:
            os.system("taskkill /F /IM chrome.exe")
            speaker.Speak("Closing Chrome")

        elif "close edge" in command:
            os.system("taskkill /F /IM msedge.exe")
            speaker.Speak("Closing Edge")

        elif "close browser" in command:
            os.system("taskkill /F /IM chrome.exe")
            os.system("taskkill /F /IM msedge.exe")
            speaker.Speak("Closing Browser")

        elif "close instagram" in command:
            os.system("taskkill /F /IM chrome.exe")
            os.system("taskkill /F /IM msedge.exe")
            speaker.Speak("Closing Instagram")

        elif "close facebook" in command:
            os.system("taskkill /F /IM chrome.exe")
            os.system("taskkill /F /IM msedge.exe")
            speaker.Speak("Closing Facebook")

        elif "close all applications" in command:
            os.system("taskkill /F /IM notepad.exe")
            os.system("taskkill /F /IM chrome.exe")
            os.system("taskkill /F /IM msedge.exe")
            os.system("taskkill /F /IM Code.exe")
            speaker.Speak("Closing all applications")

        # TIME & DATE
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speaker.Speak("The current time is " + current_time)

        elif "date" in command:
            current_date = datetime.now().strftime("%d %B %Y")
            speaker.Speak("Today is " + current_date)

        # EXIT
        elif "goodbye" in command or "exit" in command:
            speaker.Speak("Goodbye. Have a nice day.")
            break

        else:
            speaker.Speak("Please start your command with 'open' or 'close'.")

    except Exception as e:
        print("Error:", e)