import tkinter as tk
import random
import pyttsx3

person_name = "Ayesha"

engine = pyttsx3.init()
engine.setProperty("rate", 150)

root = tk.Tk()
root.title("Proposal ❤️")
root.attributes("-fullscreen", True)

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

hearts = []
def create_heart():
    x = random.randint(0, root.winfo_screenwidth())

    heart = canvas.create_text(
        x, -20,
        text="❤️",
        fill="red",
        font=("Arial", 20)
    )

    hearts.append(heart)

def animate_hearts():

    if random.randint(1, 3) == 1:
        create_heart()

    for heart in hearts[:]:

        canvas.move(heart, 0, 4)

        pos = canvas.coords(heart)

        if pos and pos[1] > root.winfo_screenheight():
            canvas.delete(heart)
            hearts.remove(heart)

    root.after(50, animate_hearts)

def romantic_hearts():

    x = random.randint(0, root.winfo_screenwidth())

    heart = canvas.create_text(
        x, -20,
        text="❤️",
        fill="white",
        font=("Arial", random.randint(15, 35))
    )

    def fall(obj):

        canvas.move(obj, 0, 5)

        pos = canvas.coords(obj)

        if pos and pos[1] < root.winfo_screenheight():
            root.after(50, lambda: fall(obj))
        else:
            canvas.delete(obj)

    fall(heart)

    root.after(150, romantic_hearts)


def move_no(event=None):
    x = random.randint(
        100,
        root.winfo_screenwidth() - 250
    )

    y = random.randint(
        150,
        root.winfo_screenheight() - 200
    )
    no_btn.place(x=x, y=y)


def page_four():
    user_text = msg_entry.get()

    msg_entry.place_forget()
    submit_btn.place_forget()

    canvas.delete("all")
    canvas.configure(bg="#ff1493")

    final_message = f"""
Dear {person_name}

Thank you for being part of this beautiful moment.

Your smile is precious.
Your happiness matters.

Every memory with you is unforgettable.

Forever & Always ❤️
"""

    engine.say(final_message)
    engine.runAndWait()

    canvas.create_text(
        root.winfo_screenwidth()//2,
        100,
        text="❤️ Thank You ❤️",
        fill="white",
        font=("Arial", 38, "bold")
    )

    canvas.create_text(
        root.winfo_screenwidth()//2,
        220,
        text=f"Your Message:\n\n{user_text}",
        fill="yellow",
        font=("Arial", 18)
    )

    canvas.create_text(
        root.winfo_screenwidth()//2,
        450,
        text=final_message,
        fill="white",
        font=("Arial", 18),
        justify="center"
    )

    romantic_hearts()


def page_three():
    global msg_entry
    global continue_btn

    try:
        continue_btn.place_forget()
    except:
        pass

    canvas.delete("all")
    canvas.configure(bg="#ff69b4")

    canvas.create_text(
        root.winfo_screenwidth()//2,
        120,
        text="💖 One Last Thing 💖",
        fill="white",
        font=("Arial", 34, "bold")
    )

    canvas.create_text(
        root.winfo_screenwidth()//2,
        250,
        text="""
Before we move forward...

I want you to know that every moment
spent thinking about you makes me smile.

Leave a message below ❤️
""",
        fill="white",
        font=("Arial", 18),
        justify="center"
    )

    msg_entry = tk.Entry(
        root,
        font=("Arial", 18),
        width=40
    )

    msg_entry.place(
        x=root.winfo_screenwidth()//2 - 250,
        y=400
    )

    submit_btn.place(
        x=root.winfo_screenwidth()//2 - 70,
        y=470
    )


def yes_clicked():

    speech = f"""
Dear {person_name},

You are one of the most special people in my life.

Your smile brightens my day.
Your presence makes every moment beautiful.

Thank you for being here.

I Love You Forever.
"""

    engine.say(speech)
    engine.runAndWait()

    yes_btn.place_forget()
    no_btn.place_forget()

    canvas.delete("all")
    canvas.configure(bg="#ff1493")

    canvas.create_text(
        root.winfo_screenwidth()//2,
        100,
        text=f"I Love You {person_name} ❤️",
        fill="white",
        font=("Arial", 40, "bold")
    )

    love_message = f"""
Dear {person_name} ❤️

From the moment you came into my life,
everything started feeling more beautiful.

Your smile brightens my day.

Your presence makes every moment special.

Thank you for being such a wonderful person.

🌹 I Love You Forever 🌹
"""

    canvas.create_text(
        root.winfo_screenwidth()//2,
        330,
        text=love_message,
        fill="white",
        font=("Arial", 18),
        justify="center"
    )

    romantic_hearts()

    global continue_btn

    continue_btn = tk.Button(
        root,
        text="Continue ❤️",
        font=("Arial", 16, "bold"),
        command=page_three
    )

    continue_btn.place(
        x=root.winfo_screenwidth()//2 - 80,
        y=650
    )


# -------- FIRST PAGE --------

canvas.create_text(
    root.winfo_screenwidth()//2,
    150,
    text=f"{person_name}, Will You Be My Partner? ❤️",
    fill="white",
    font=("Arial", 30, "bold")
)

canvas.create_text(
    root.winfo_screenwidth()//2,
    220,
    text="You are the most special person in my life ❤️",
    fill="pink",
    font=("Arial", 20)
)

yes_btn = tk.Button(
    root,
    text="YES ❤️",
    font=("Arial", 18, "bold"),
    bg="lightgreen",
    command=yes_clicked
)

yes_btn.place(x=500, y=350)

no_btn = tk.Button(
    root,
    text="NO 💔",
    font=("Arial", 18, "bold"),
    bg="tomato"
)

no_btn.place(x=750, y=350)
no_btn.bind("<Enter>", move_no)

submit_btn = tk.Button(
    root,
    text="Submit ❤️",
    font=("Arial", 16, "bold"),
    command=page_four
)

exit_btn = tk.Button(
    root,
    text="❌ Exit",
    command=root.destroy
)

exit_btn.place(x=20, y=20)

animate_hearts()

root.mainloop()