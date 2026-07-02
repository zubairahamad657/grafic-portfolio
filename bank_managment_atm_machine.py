import csv
import datetime as dt

ACCOUNT_NO = "12345"
PIN = "1234"
balance = 5000

print("===== BANK LOGIN =====")

acc = input("Enter Account Number: ")
pin = input("Enter PIN: ")

if acc == ACCOUNT_NO and pin == PIN:

    while True:
        print("\n===== BANK MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            print("Current Balance:", balance)

        elif choice == "2":
            amount = float(input("Enter Deposit Amount: "))
            balance += amount

            now = dt.datetime.now()

            with open("transactions.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [acc, "Deposit", amount, balance, now]
                )

            print("Deposit Successful!")
            print("New Balance:", balance)

        elif choice == "3":
            amount = float(input("Enter Withdraw Amount: "))

            if amount <= balance:
                balance -= amount

                now = dt.datetime.now()

                with open("transactions.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        [acc, "Withdraw", amount, balance, now]
                    )

                print("Withdrawal Successful!")
                print("Remaining Balance:", balance)

            else:
                print("Insufficient Balance!")

        elif choice == "4":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

else:
    print("Invalid Account Number or PIN!")