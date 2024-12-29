import os
import json
import getpass
from tabulate import tabulate

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and macOS
    else:
        os.system('clear')

class AccountHolder:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount:,.2f} BDT deposited. New balance: {self.balance:,.2f} BDT")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"{amount:,.2f} BDT withdrawn. New balance: {self.balance:,.2f} BDT")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance:,.2f} BDT"


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
            # Prepare table data with formatted balance
            table_data = [
                ["Account Number", "Name", "Balance (BDT)"],
                [account.account_number, account.name, f"{account.balance:,.2f}"]
            ]
            # Display the table
            print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
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
            print(f"Current balance: {account.get_balance():,.2f} BDT")
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
                "balance": f"{account.get_balance():,.2f}"  # Format the balance
            } for account_number, account in self.accounts.items()}
            
            # Convert to JSON and pretty print
            json_data = json.dumps(accounts_list, indent=4)
            print("\n--- Account Details (JSON) ---")
            print(json_data)

            # Display in table format
            print("\n--- Account Details (Table) ---")
            table_data = [["Account Number", "Name", "Balance (BDT)"]]
            for account_number, account in self.accounts.items():
                table_data.append([account_number, account.name, f"{account.get_balance():,.2f}"])
            print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
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
        clear_terminal()

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
            input("Press Enter to continue...")
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
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()

