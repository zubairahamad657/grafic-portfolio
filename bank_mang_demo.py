import csv
import datetime as dt
balance = 1000
while (True):
    print ("BANK MENU")
    print ("1. check balance")
    print ("2. deposit")
    print ("3. withdraw")
    print ("4. Exit")

    choice = input ("enter choice")
    if choice == "1":
        print ("balance:", balance)
    elif choice == "2":
        amount = float (input("enter deposit amount"))
        balance = balance + amount

        now = dt.datetime.now()
        with open ("transationn.csv", "a") as file:
            writer = csv.writer (file)
            writer.writerow(["deposit", amount, balance, now])

        print ("deposit succesful")
        print ("new balance", balance)

    elif choice == "3":
        amount = float(input("enter withdraw amount"))

        if amount <= balance:
            balance = balance - amount

            now = dt.datetime.now()
            with open ("transationn.csv", "a") as file:
                 writer = csv.writer (file)
                 writer.writerow(["withdraw", amount, balance, now])

            print("withdraw successful")
            print ("remaining balance", balance) 

        else:
            print ("low balance")        





      