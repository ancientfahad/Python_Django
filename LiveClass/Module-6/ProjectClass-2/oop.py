# OOP
    # Encapsulation - class | object | method
    # Inheritance - 
    # Polymorphism - 
    # Abstraction - 
    # String Concatenation
    
import sys
import time
import itertools

# Function to display loading animation
def loading_animation():
    animation = itertools.cycle(['|', '/', '-', '\\'])  # Loading symbols
    for _ in range(30):  # Adjust the range for the duration of the animation
        sys.stdout.write(f'\rLoading {next(animation)}')
        sys.stdout.flush()
        time.sleep(0.1)  # Delay between each animation frame
    sys.stdout.write('\rLoading complete!\n')

# Run the loading animation
loading_animation()

import sys
import time

# Function to display loading bar
def loading_bar():
    total_steps = 50  # Number of steps in the loading bar
    for i in range(total_steps + 1):
        percent = int((i / total_steps) * 100)  # Calculate percentage
        bar = ('#' * i).ljust(total_steps)  # Create loading bar
        sys.stdout.write(f'\r[{bar}] {percent}%')  # Display bar with percentage
        sys.stdout.flush()
        time.sleep(0.1)  # Simulate work with a delay
    sys.stdout.write('\n')

# Run the loading bar
loading_bar()


    
firstName = "Fahad"
lastName = "Chowdhury"
age = "30"

fullName1 = f"{firstName} {lastName}"
fullName2 = "{} {} {}".format(lastName, firstName, age)

print(fullName1)
print(fullName2)

"""
Author: Al Fahad Chowdhury
Date: 22 Sep, 2024

Project Description:
This project is a command-line banking system that manages account holders.
Users can create, read, update, and delete accounts, as well as handle deposits
and withdrawals. The system performs input validation and provides appropriate
feedback based on user actions.

Variables:
- banking_system: An instance of the BankingSystem class that manages multiple accounts.

Classes:
- AccountHolder: Represents an individual bank account holder with methods for deposits, withdrawals,
               and balance checks.
- BankingSystem: Manages multiple AccountHolder instances, allowing account creation, retrieval, 
               updates, deletions, and transaction handling.

Functions:
- get_valid_account_number(): Prompts the user for a valid account number.
- get_valid_amount(): Prompts the user for a valid deposit or withdrawal amount.
- main(): The main function that drives the user interface and handles user choices.
"""
"""

import json
import getpass

class AccountHolder:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} BDT deposited. New balance: {self.balance} BDT")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"{amount} BDT withdrawn. New balance: {self.balance} BDT")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance} BDT"


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name):
        if account_number in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[account_number] = AccountHolder(account_number, name)
            print("Account created successfully!")

    def read_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found!")

    def update_account(self, account_number, new_name):
        account = self.accounts.get(account_number)
        if account:
            account.name = new_name
            print("Account updated successfully!")
        else:
            print("Account not found!")

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully!")
        else:
            print("Account not found!")

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Current balance: {account.get_balance()} BDT")
        else:
            print("Account not found!")

    def deposit_amount(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found!")

    def withdraw_amount(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found!")

    def display_accounts_as_json(self):
        try:
            accounts_list = {account_number: {
                "name": account.name,
                "balance": account.get_balance()
            } for account_number, account in self.accounts.items()}
            
            # Convert to JSON and pretty print
            json_data = json.dumps(accounts_list, indent=4)
            print(json_data)
        except Exception as e:
            print(f"Error displaying accounts: {e}")


def get_valid_account_number():
    while True:
        account_number = input("Enter account number: ")
        if account_number.isalnum():  # Account number must be alphanumeric
            return account_number
        print("Invalid account number! Please enter an alphanumeric value.")


def get_valid_amount():
    while True:
        amount = input("Enter amount (in BDT): ")
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            return amount
        except ValueError as e:
            print(f"Invalid amount! {e}")


def main():
    banking_system = BankingSystem()
    
    while True:
        print("\n1. Create Account Holder")
        print("2. Read Account Holder")
        print("3. Update Account Holder")
        print("4. Delete Account Holder")
        print("5. Check Balance")
        print("6. Deposit Amount")
        print("7. Withdraw Amount")
        print("8. Admin - View All Accounts (Protected)")
        print("9. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            account_number = get_valid_account_number()
            name = input("Enter account holder name: ")
            banking_system.create_account(account_number, name)
            input("Press Enter to continue...")  # Wait for user input before returning to the menu
        elif choice == '2':
            account_number = get_valid_account_number()
            banking_system.read_account(account_number)
            input("Press Enter to continue...")
        elif choice == '3':
            account_number = get_valid_account_number()
            new_name = input("Enter new name: ")
            banking_system.update_account(account_number, new_name)
            input("Press Enter to continue...")
        elif choice == '4':
            account_number = get_valid_account_number()
            banking_system.delete_account(account_number)
            input("Press Enter to continue...")
        elif choice == '5':
            account_number = get_valid_account_number()
            banking_system.check_balance(account_number)
            input("Press Enter to continue...")
        elif choice == '6':
            account_number = get_valid_account_number()
            amount = get_valid_amount()
            banking_system.deposit_amount(account_number, amount)
            input("Press Enter to continue...")
        elif choice == '7':
            account_number = get_valid_account_number()
            amount = get_valid_amount()
            banking_system.withdraw_amount(account_number, amount)
            input("Press Enter to continue...")
        elif choice == '8':
            password = getpass.getpass("Enter admin password: ")
            if password == "admin":
                banking_system.display_accounts_as_json()
            else:
                print("Incorrect password!")
            input("Press Enter to continue...")
        elif choice == '9':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please try again.")
            input("Press Enter to continue...")  # Ensure the user presses Enter even after an invalid option


if __name__ == "__main__":
    main()

"""

