import tkinter as tk

def show_welcome():
    name = name_entry.get().strip()

    if name:
        welcome_label.config(
            text=f"🎉 WELCOME {name.upper()} 🎉"
        )

root = tk.Tk()
root.title("Welcome Screen")

# Full Screen
root.attributes("-fullscreen", True)

# Background
root.configure(bg="#1e1e1e")

# Exit Button
exit_btn = tk.Button(
    root,
    text="❌ Exit",
    font=("Arial", 14),
    command=root.destroy
)
exit_btn.pack(anchor="ne", padx=20, pady=20)

title = tk.Label(
    root,
    text="WELCOME APP",
    font=("Arial", 40, "bold"),
    fg="cyan",
    bg="#1e1e1e"
)
title.pack(pady=50)

name_entry = tk.Entry(
    root,
    font=("Arial", 20),
    width=20
)
name_entry.pack(pady=20)

welcome_btn = tk.Button(
    root,
    text="Show Welcome",
    font=("Arial", 18),
    command=show_welcome
)
welcome_btn.pack(pady=20)

welcome_label = tk.Label(
    root,
    text="",
    font=("Arial", 36, "bold"),
    fg="yellow",
    bg="#1e1e1e"
)
welcome_label.pack(pady=80)

root.mainloop()