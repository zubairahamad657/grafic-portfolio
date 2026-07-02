import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from datetime import datetime

# Voice Engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print("Nova:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        command = recognizer.recognize_google(audio, language="en-IN")
        print("You:", command)
        return command.lower()

    except sr.WaitTimeoutError:
        return ""

    except Exception:
        return ""

# Welcome Message
speak("Nova assistant start ho gayi hai.")

while True:

    command = take_command()

    if not command:
        continue

    # Friendly Conversation
    if "nova" in command:

        speak("Hi Zubair!")
        speak("Kaise ho mere dost?")
        speak("Aaj ka din kaisa ja raha hai?")
        speak("Waise aaj bahar kaafi garmi hai.")
        speak("Umeed hai tum paani peete reh rahe hoge.")
        speak("To batao, aaj kya kar rahe ho?")
        speak("Coding, editing ya phir kuch naya seekh rahe ho?")
        speak("Main yahin hoon, jab bhi meri zarurat ho mujhe Nova bula lena.")

    elif "kaise ho" in command:
        speak("Main bilkul badhiya hoon. Tum kaise ho dost?")

    elif "tumhara naam kya hai" in command:
        speak("Mera naam Nova hai.")

    elif "time" in command or "samay" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"Abhi samay hai {current_time}")

    elif "date" in command:
        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Aaj ki date hai {current_date}")

    elif "youtube kholo" in command:
        webbrowser.open("https://www.youtube.com")
        speak("YouTube khol diya hai.")

    elif "google kholo" in command:
        webbrowser.open("https://www.google.com")
        speak("Google khol diya hai.")

    elif "instagram kholo" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Instagram khol diya hai.")

    elif "chrome kholo" in command:
        os.system("start chrome")
        speak("Chrome khol diya hai.")

    elif "chrome band karo" in command:
        os.system("taskkill /f /im chrome.exe")
        speak("Chrome band kar diya hai.")

    elif "thank you" in command or "shukriya" in command:
        speak("Koi baat nahi dost. Main hamesha madad ke liye yahan hoon.")

    elif "good morning" in command:
        speak("Good Morning Zubair. Aaj ka din shandaar rahe.")

    elif "good night" in command:
        speak("Good Night Zubair. Achhe se aaram karna.")

    elif "band ho jao" in command or "exit" in command:
        speak("Goodbye Zubair. Phir milte hain.")
        break

    else:
        speak("Maaf karna dost, main ye command abhi nahi samajh paayi.")