import random

print("🎮 Number Guessing Game 🎮")
print("Maine 1 se 100 ke beech ek number socha hai.")

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Apna guess enter karo: "))

    if guess < secret_number:
        print("📉 Bahut chhota number!")
    elif guess > secret_number:
        print("📈 Bahut bada number!")
    else:
        print("🎉 Congratulations! Aap jeet gaye.")
        break