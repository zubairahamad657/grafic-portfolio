import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
r = sr.Recognizer()

speaker.Speak("i am ready to talk with you")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        text = r.recognize_google(audio)
        print("You:", text)

        if text.lower() == "bye":
            speaker.Speak("Goodbye")
            break

        speaker.Speak("you said" + text)

    except Exception as e:
        print("Error:", e)
        speaker.Speak("actually i am confused what you said")