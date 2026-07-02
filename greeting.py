import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

name = input("may i know your name: ")

hour = datetime.now().hour

if hour < 12:
    greeting = f"Good Morning {name}"
elif hour < 18:
    greeting = f"Good Afternoon {name}"
else:
    greeting = f"Good Evening {name}"

print(greeting)
engine.say(greeting)
engine.runAndWait()