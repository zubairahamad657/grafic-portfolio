import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("you said:", text)

    engine.say("you said " + text)
    engine.runAndWait()

except Exception as e:
    print(e)