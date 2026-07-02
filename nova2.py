import speech_recognition as sr
import win32com.client
import webbrowser
import os
from datetime import datetime

# Voice Engine
# Voice Engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Female Voice Set
for voice in speaker.GetVoices():
    if "zira" in voice.GetDescription().lower():
        speaker.Voice = voice
        break

recognizer = sr.Recognizer()
speaker = win32com.client.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()
speaker.Voice = voices.Item(1)   # Zira Female Voice
speaker.Rate = 0                 # Speed
speaker.Volume = 100             # Volume
recognizer = sr.Recognizer()

speaker.Speak("Nova assistant started.")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio, language="en-IN").lower()
        print("You Said:", command)

        # NOVA WAKE WORD
        if "nova" in command:

            speaker.Speak("Hi Zubair")
            speaker.Speak("Kaise ho mere dost")
            speaker.Speak("Aaj ka din kaisa ja raha hai")
            speaker.Speak("Waise aaj bahar kaafi garmi hai")
            speaker.Speak("Umeed hai tum paani peete reh rahe hoge")
            speaker.Speak("To batao aaj kya kar rahe ho")
            speaker.Speak("Coding, editing ya phir kuch naya seekh rahe ho")
            speaker.Speak("Main yahin hoon. Jab bhi meri zarurat ho mujhe Nova bula lena")

        # OPEN COMMANDS
        elif "open google" in command:
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

        elif "open chat g p t" in command or "open chatgpt" in command:
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

        elif "open chrome" in command:
            os.system("start chrome")
            speaker.Speak("Opening Chrome")

        # CLOSE COMMANDS
        elif "close chrome" in command:
            os.system("taskkill /F /IM chrome.exe")
            speaker.Speak("Closing Chrome")

        elif "close notepad" in command:
            os.system("taskkill /F /IM notepad.exe")
            speaker.Speak("Closing Notepad")

        elif "close calculator" in command:
            os.system("taskkill /F /IM CalculatorApp.exe")
            speaker.Speak("Closing Calculator")

        elif "close edge" in command:
            os.system("taskkill /F /IM msedge.exe")
            speaker.Speak("Closing Edge")

        elif "close all applications" in command:
            os.system("taskkill /F /IM chrome.exe")
            os.system("taskkill /F /IM msedge.exe")
            os.system("taskkill /F /IM notepad.exe")
            os.system("taskkill /F /IM Code.exe")
            speaker.Speak("Closing all applications")

        # TIME
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speaker.Speak("Current time is " + current_time)

        # DATE
        elif "date" in command:
            current_date = datetime.now().strftime("%d %B %Y")
            speaker.Speak("Today is " + current_date)

        # FRIENDLY COMMANDS
        elif "how are you" in command:
            speaker.Speak("I am fine boss. Thank you for asking.")

        elif "may i know your name" in command:
            speaker.Speak("My name is Nova.")

        elif "thank you" in command:
            speaker.Speak("You are welcome boss.")

        elif " morning" in command:
            speaker.Speak("Good Morning boss. Have a great day.")

        elif "good night" in command:
            speaker.Speak("Good Night boss. Sweet dreams.")

        # EXIT
        elif "goodbye" in command or "exit" in command:
            speaker.Speak("Goodbye boss. Have a nice day.")
            break

        else:
            speaker.Speak("Sorry boss. I did not understand your accent.")

    except Exception as e:
        print("Error:", e)