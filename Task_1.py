import time

# Simulate an ATM Machine with basic functionalities
def atm_machine():
    # Initialize account details
    account_balance = 0
    pin = 1122
    transaction_history = []

    # Function to display the main menu
    def display_menu():
        print("""                                                           Cabin Bank Of Cabin
    
                                                ****** Welcome To The Cabin Bank ATM ******""")
        print("""
        ======== Cabin Bank ATM Menu ========
        1. Balance Inquiry
        2. Withdraw Amount
        3. Deposit Amount 
        4. Change PIN
        5. View Transaction History
        6. Exit
        ==========================
        """)

    # Function to check balance
    def check_balance():
        print("-----------------------------------------------------------")
        print(f"Available Balance: ₹{account_balance}")
        print("-----------------------------------------------------------")

    # Function to withdraw money
    def withdraw():
        nonlocal account_balance
        try:
            print("Note: You can only withdraw amounts in multiples of 100, 200, 500, or 2000.")
            withdraw_amount = int(input("Enter the amount to withdraw: ₹"))

            if withdraw_amount <= account_balance and withdraw_amount > 0:
                if withdraw_amount % 100 == 0 or withdraw_amount % 200 == 0 or withdraw_amount % 500 == 0 or withdraw_amount % 2000 == 0:
                    account_balance -= withdraw_amount
                    transaction_history.append(f"Withdraw: -₹{withdraw_amount}")
                    print("-----------------------------------------------------------")
                    print(f"₹{withdraw_amount} debited from your account.")
                    check_balance()
                else:
                    print("-----------------------------------------------------------")
                    print("Invalid amount. Please enter a multiple of 100, 200, 500, or 2000.")
            else:
                print("-----------------------------------------------------------")
                print("Insufficient balance or invalid amount.")
        except ValueError:
            print("-----------------------------------------------------------")
            print("Invalid input. Please enter a numerical value.")

    # Function to deposit money
    def deposit():
        nonlocal account_balance
        try:
            deposit_amount = int(input("Enter the amount to deposit: ₹"))
            if deposit_amount > 0:
                account_balance += deposit_amount
                transaction_history.append(f"Deposit: +₹{deposit_amount}")
                print("-----------------------------------------------------------")
                print(f"₹{deposit_amount} credited to your account.")
                check_balance()
            else:
                print("-----------------------------------------------------------")
                print("Invalid deposit amount.")
        except ValueError:
            print("-----------------------------------------------------------")
            print("Invalid input. Please enter a numerical value.")

    # Function to change PIN
    def change_pin():
        nonlocal pin
        try:
            current_pin = int(input("Enter your current PIN: "))
            if current_pin == pin:
                new_pin = int(input("Enter your new PIN: "))
                confirm_pin = int(input("Confirm your new PIN: "))
                if new_pin == confirm_pin:
                    pin = new_pin
                    print("-----------------------------------------------------------")
                    print("PIN changed successfully.")
                else:
                    print("-----------------------------------------------------------")
                    print("PINs do not match. Try again.")
            else:
                print("-----------------------------------------------------------")
                print("Incorrect current PIN.")
        except ValueError:
            print("-----------------------------------------------------------")
            print("Invalid input. Please enter a numerical value.")

    # Function to view transaction history
    def view_transaction_history():
        print("-----------------------------------------------------------")
        if transaction_history:
            print("Transaction History:")
            for transaction in transaction_history:
                print(transaction)
        else:
            print("No transactions found.")
        print("-----------------------------------------------------------")

    # Simulate card insertion
    print("""
                                                            Cabin Bank Of Cabin
    
                                                ****** Welcome To The Cabin Bank ATM ******""")
    print("Please insert your card...")
    time.sleep(2)

    # User PIN verification
    try:
        entered_pin = int(input("Enter PIN: "))
        if entered_pin == pin:
            while True:
                display_menu()
                try:
                    option = int(input("Please enter your option: "))
                    if option == 1:
                        check_balance()
                    elif option == 2:
                        withdraw()
                    elif option == 3:
                        deposit()
                    elif option == 4:
                        change_pin()
                    elif option == 5:
                        view_transaction_history()
                    elif option == 6:
                        print("Thank you for using our ATM. Please Visit Again!")
                        break
                    else:
                        print("Invalid option. Please choose a valid menu option.")
                    time.sleep(2)  # Wait for 2 seconds before displaying the menu again
                except ValueError:
                    print("Invalid input. Please enter a numerical value.")
                    time.sleep(2)  # Wait for 2 seconds before displaying the menu again
        else:
            print("Incorrect PIN. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

# Run the ATM machine simulation
atm_machine()