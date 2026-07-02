import database

# Create accounts.csv if it doesn't exist
database.create_file()

while True:

    print("\n" + "=" * 45)
    print("      BANK MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Your Choice : ")

    # -----------------------------------
    # Create Account
    # -----------------------------------
    if choice == "1":

        database.create_account()

    # -----------------------------------
    # Login
    # -----------------------------------
    elif choice == "2":

        user = database.login()

        if user:

            while True:

                print("\n" + "=" * 45)
                print("              ATM MENU")
                print("=" * 45)
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transaction History")
                print("5. Transfer Money")
                print("6. Change PIN")
                print("7. Mini Statement")
                print("8. Logout")

                ch = input("Enter Your Choice : ")

                # -----------------------------
                # Check Balance
                # -----------------------------
                if ch == "1":

                    database.check_balance(user)

                # -----------------------------
                # Deposit
                # -----------------------------
                elif ch == "2":

                    database.deposit(user)

                # -----------------------------
                # Withdraw
                # -----------------------------
                elif ch == "3":

                    database.withdraw(user)

                # -----------------------------
                # Transaction History
                # -----------------------------
                elif ch == "4":

                    database.transaction_history(user)

                # -----------------------------
                # Transfer Money
                # -----------------------------
                elif ch == "5":

                    database.transfer(user)

                # -----------------------------
                # Change PIN
                # -----------------------------
                elif ch == "6":

                    database.change_pin(user)

                # -----------------------------
                # Mini Statement
                # -----------------------------
                elif ch == "7":

                    database.mini_statement(user)

                # -----------------------------
                # Logout
                # -----------------------------
                elif ch == "8":

                    print("\nLogout Successful...")
                    break

                else:

                    print("Invalid Choice!")

    # -----------------------------------
    # Exit
    # -----------------------------------
    elif choice == "3":

        print("\nThank You For Using Our Bank ❤️")
        break

    else:

        print("Invalid Choice!")