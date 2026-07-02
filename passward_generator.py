import random
import string

print("=== Password Generator ===")

letters_count = int(input("How many letters? : "))
numbers_count = int(input("How many numbers? : "))
symbols_count = int(input("How many symbols? : "))

password_list = []

for i in range(letters_count):
    password_list.append(random.choice(string.ascii_letters))

for i in range(numbers_count):
    password_list.append(random.choice(string.digits))

for i in range(symbols_count):
    password_list.append(random.choice(string.punctuation))

# Password ko shuffle karenge
random.shuffle(password_list)

# List ko string me convert karenge
password = "".join(password_list)

print("\nGenerated Password:")
print(password)

# File me save karna
with open("passwords.txt", "a") as file:
    file.write(password + "\n")

print("\nPassword saved in  passwords.txt .")