import csv
import datetime as dt
balance = 1000

while (True):
    print("===== BANK LOGIN =====")
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
            balance = balance + amount

            now = dt.datetime.now()

            with open("transactions.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Deposit", amount, balance, now])
                

            print("Deposit Successful!")
            print("New Balance:", balance)

    elif choice == "3":
            amount = float(input("Enter Withdraw Amount: "))

            if amount <= balance:
                balance = balance  - amount

                now = dt.datetime.now()

                with open("transactions.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([ "Withdraw", amount, balance, now])
                    

                print("Withdrawal Successful!")
                print("Remaining Balance:", balance)

            else:
                print("Insufficient Balance!")

       