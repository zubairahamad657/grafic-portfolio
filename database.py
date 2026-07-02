import csv
import random
import os
import uuid
import datetime as dt

# CSV File Name
FILE_NAME = "accounts.csv"


# -----------------------------
# Create CSV File
# -----------------------------
def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["AccountNo", "Name", "PIN", "Balance"])


# -----------------------------
# Generate Account Number
# -----------------------------
def generate_account():

    return random.randint(100000, 999999)


# -----------------------------
# Create Account
# -----------------------------
def create_account():

    name = input("Enter Name : ")

    while True:

        pin = input("Create 4 Digit PIN : ")

        if len(pin) == 4 and pin.isdigit():
            break

        print("PIN must be exactly 4 digits.")

    while True:

        try:

            balance = float(input("Enter Opening Balance : "))

            if balance < 0:
                print("Balance cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid amount.")

    account = generate_account()

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([account, name, pin, balance])

    print("\nAccount Created Successfully")
    print("Account Number :", account)


# -----------------------------
# Login
# -----------------------------
def login():

    attempts = 3

    while attempts > 0:

        account = input("Enter Account Number : ")
        pin = input("Enter PIN : ")

        with open(FILE_NAME, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if row["AccountNo"] == account and row["PIN"] == pin:

                    print("\nLogin Successful")
                    print("Welcome", row["Name"])

                    return row

        attempts -= 1

        print("Wrong Account Number or PIN")
        print("Remaining Attempts :", attempts)

    print("\nToo Many Attempts")
    return None
def update_balance(account_no, new_balance):

    rows = []

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["AccountNo"] == account_no:
                row["Balance"] = str(new_balance)

            rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:

        fieldnames = ["AccountNo", "Name", "PIN", "Balance"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(rows)

def deposit(user):

    try:

        amount = float(input("Enter Deposit Amount : "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        balance = float(user["Balance"])

        balance += amount

        user["Balance"] = str(balance)

        update_balance(user["AccountNo"], balance)

        save_transaction(
            user["AccountNo"],
            "Deposit",
            amount,
            balance
        )

        print("Deposit Successful")
        print("Current Balance :", balance)

    except ValueError:

        print("Invalid Amount")
def withdraw(user):

    try:

        amount = float(input("Enter Withdraw Amount : "))

        balance = float(user["Balance"])

        if amount <= 0:
            print("Amount must be greater than 0.")

        elif amount > balance:
            print("Insufficient Balance")

        else:

            balance -= amount

            user["Balance"] = str(balance)

            update_balance(user["AccountNo"], balance)

            save_transaction(
                user["AccountNo"],
                "Withdraw",
                amount,
                balance
            )

            print("Withdraw Successful")
            print("Remaining Balance :", balance)

    except ValueError:

        print("Invalid Amount")
def check_balance(user):

    print("\nCurrent Balance :", user["Balance"]) 

def save_transaction(account_no, t_type, amount, balance):

    transaction_id = str(uuid.uuid4())[:8]

    now = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("transactions.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            transaction_id,
            account_no,
            t_type,
            amount,
            balance,
            now
        ])     

def transaction_history(user):

    print("\n========== TRANSACTION HISTORY ==========\n")

    found = False

    with open("transactions.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            if row[1] == user["AccountNo"]:

                print(
                    f"ID : {row[0]}"
                )
                print(
                    f"Type : {row[2]}"
                )
                print(
                    f"Amount : ₹{row[3]}"
                )
                print(
                    f"Balance : ₹{row[4]}"
                )
                print(
                    f"Date : {row[5]}"
                )
                print("-" * 40)

                found = True

    if not found:

        print("No Transactions Found")

def find_account(account_no):

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["AccountNo"] == account_no:
                return row

    return None

def transfer(user):

    receiver = input("Enter Receiver Account Number : ")

    receiver_data = find_account(receiver)

    if receiver_data is None:

        print("Receiver Account Not Found")
        return

    if receiver == user["AccountNo"]:

        print("You cannot transfer to your own account")
        return

    try:

        amount = float(input("Enter Amount : "))

        if amount <= 0:

            print("Invalid Amount")
            return

        sender_balance = float(user["Balance"])

        if amount > sender_balance:

            print("Insufficient Balance")
            return

        receiver_balance = float(receiver_data["Balance"])

        sender_balance -= amount
        receiver_balance += amount

        update_balance(user["AccountNo"], sender_balance)
        update_balance(receiver, receiver_balance)

        user["Balance"] = str(sender_balance)

        save_transaction(
            user["AccountNo"],
            "Transfer Sent",
            amount,
            sender_balance
        )

        save_transaction(
            receiver,
            "Transfer Received",
            amount,
            receiver_balance
        )

        print("Transfer Successful")

    except ValueError:

        print("Invalid Amount")

def change_pin(user):

    old_pin = input("Enter Current PIN : ")

    if old_pin != user["PIN"]:

        print("Wrong PIN")
        return

    while True:

        new_pin = input("Enter New 4 Digit PIN : ")

        if len(new_pin) == 4 and new_pin.isdigit():
            break

        print("PIN must be exactly 4 digits.")

    rows = []

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["AccountNo"] == user["AccountNo"]:

                row["PIN"] = new_pin

            rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:

        fieldnames = ["AccountNo", "Name", "PIN", "Balance"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(rows)

    user["PIN"] = new_pin

    print("PIN Changed Successfully")

def mini_statement(user):

    print("\n========== MINI STATEMENT ==========\n")

    transactions = []

    with open("transactions.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            if row[1] == user["AccountNo"]:

                transactions.append(row)

    if len(transactions) == 0:

        print("No Transactions Found")
        return

    for row in transactions[-5:]:

        print(
            f"{row[2]} | ₹{row[3]} | Balance ₹{row[4]} | {row[5]}"
        )                                   