import csv
import datetime as dt

class account:

    def __init__(self, n, a, b):
        self.name = n
        self.accountno = a
        self.balance = float(b)

    def show(self):
        print("\nName :", self.name)
        print("Account Number :", self.accountno)
        print("Balance :", self.balance)

    def deposit(self):
        amount = float(input("Enter Deposit Amount : "))
        self.balance += amount
        print("Deposit Successful")
        print("Balance :", self.balance)

        with open("transaction.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Deposit",amount,self.balance,dt.datetime.now()])

    def withdraw(self):
        amount = float(input("Enter Withdraw Amount : "))

        if amount < self.balance:
            self.balance -= amount
            print("Withdraw Successful")
            print("Balance :", self.balance)

            with open("transaction.csv","a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Withdraw",amount,self.balance,dt.datetime.now()])


# ---------------- Login ----------------

x = input("Enter Account Number : ")

with open("accountt.csv","r") as file:

    reader = csv.DictReader(file)

    user = None

    for row in reader:

        if row["account_num"] == x:

            user = account(row["name"],
                           row["account_num"],
                           row["balance"])
            

if user is None:
    print("Account Not Found")

else:

    print("Login Successful")
    user.show()

    while True:

        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter Choice : ")

        if choice=="1":
            print("Balance :",user.balance)

        elif choice=="2":
            user.deposit()

        elif choice=="3":
            user.withdraw()

        elif choice=="4":
            print("Thank You")
            break

        else:
            print("Invalid Choice")