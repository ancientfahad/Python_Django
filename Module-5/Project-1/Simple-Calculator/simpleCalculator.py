"""
Author: Al Fahad Chowdhury
Date: 15 Sep, 2024

Course: Full Stack Web Development with Python, Django & React
Batch: 2
Module: 5
Project: 1
Project Name: Simple Calculator

Project Description:
This project is a simple command-line calculator that allows users to perform basic arithmetic
operations such as addition, subtraction, multiplication, division, and modulus. It also handles
error cases like division by zero, invalid numeric inputs, and invalid operation selections. The 
program continues to ask for inputs until the user chooses to exit.

ANSI Color Codes:
- RESET, YELLOW, GREEN, RED, BLUE: ANSI escape codes used to style terminal text, improving user
  experience by providing colored feedback in the command-line interface (CLI).

Variables:
- choice: Stores the user's selected operation (1-6).
- num1, num2: The two numbers input by the user for calculations.
- next_calculation: Used to determine whether the user wants to perform another calculation or exit.

Functions:
- add(x, y): Returns the sum of x and y.
- subtract(x, y): Returns the difference between x and y.
- multiply(x, y): Returns the product of x and y.
- divide(x, y): Returns the quotient of x divided by y, or an error message if division by zero occurs.
- modulus(x, y): Returns the remainder when x is divided by y.
- get_valid_number(prompt): Continuously prompts the user for a valid number and returns a float 
  once valid input is provided.
- calculator(): Main function that handles user interactions, performs the chosen arithmetic operations,
  and continues until the user opts to exit.
"""

import sys  # Importing sys module (internal library) to handle program exit

# ANSI color codes to style terminal output
RESET = "\033[0m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"

# Displaying author and project information
print(f"\n{GREEN}{'*' * 70}")
print(f"{GREEN}{'Author'}  {':'}   {'Al Fahad Chowdhury'}")
print(f"{GREEN}{'Date'}    {':'}   {'15 Sep, 2024'}")
print(f"{GREEN}{'Course'}  {':'}   {'Full Stack Web Development with Python, Django & React'}")
print(f"{GREEN}{'Batch'}   {':'}   {'2'}")
print(f"{GREEN}{'Module'}  {':'}   {'5'}")
print(f"{GREEN}{'Project'} {':'}   {'1'}")
print(f"{GREEN}{'Name'}    {':'}   {'Simple Calculator'}")
print(f"{GREEN}{'*' * 70}")

# Arithmetic functions
def add(x, y):
    """
    Adds two numbers and returns the result.
    :param x: first number
    :param y: second number
    :return: sum of x and y
    """
    return x + y

def subtract(x, y):
    """
    Subtracts the second number from the first and returns the result.
    :param x: first number
    :param y: second number
    :return: difference of x and y
    """
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers and returns the result.
    :param x: first number
    :param y: second number
    :return: product of x and y
    """
    return x * y

def divide(x, y):
    """
    Divides the first number by the second and handles division by zero.
    :param x: first number
    :param y: second number
    :return: quotient of x and y, or error message if division by zero
    """
    if y == 0:
        return f"{RED}Error! Division by zero.{RESET}"
    else:
        return x / y

def modulus(x, y):
    """
    Calculates the modulus of two numbers and returns the result.
    :param x: first number
    :param y: second number
    :return: remainder of x divided by y
    """
    return x % y

# Function to validate user input as a numeric value
def get_valid_number(prompt):
    """
    Prompts the user for a number and validates the input.
    If the input is not a valid number, it keeps asking until a valid number is entered.
    :param prompt: The message to display to the user.
    :return: A valid float number.
    """
    while True:
        try:
            return float(input(prompt))
        except Exception:
            print(f"{RED}Invalid input! Please enter numeric values.{RESET}\n")

# Main function to handle user input and operations
def calculator():
    """
    Main function presents a menu to the user, receives input, and performs the chosen arithmetic operation.
    The program continues until the user decides to exit.
    """
    print(f"\n{GREEN}*** Welcome to the Simple Calculator ***")

    while True:
        # Displaying operation options
        print()
        print(f"{GREEN}Select operation:")
        print(f"{GREEN}[1] Add")
        print(f"{GREEN}[2] Subtract")
        print(f"{GREEN}[3] Multiply")
        print(f"{GREEN}[4] Divide")
        print(f"{GREEN}[5] Modulus")
        print(f"{RED}[6] Exit")

        # Taking user's choice of operation
        print()
        choice = input(f"{YELLOW}Enter choice [1/2/3/4/5/6]: {RESET}")

        # Validating user choice
        if choice in ['1', '2', '3', '4', '5']:

            # Using the get_valid_number function to get valid input for both numbers
            print()
            num1 = get_valid_number(f"{YELLOW}Enter first number: {RESET}")
            num2 = get_valid_number(f"{YELLOW}Enter second number: {RESET}")

            # Performing the selected operation
            if choice == '1':
                print(f"\n{BLUE}Addition: {num1} + {num2} = {GREEN}{add(num1, num2)}{RESET}\n")
            elif choice == '2':
                print(f"\n{BLUE}Subtraction: {num1} - {num2} = {GREEN}{subtract(num1, num2)}{RESET}\n")
            elif choice == '3':
                print(f"\n{BLUE}Multiplication: {num1} * {num2} = {GREEN}{multiply(num1, num2)}{RESET}\n")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"\n{BLUE}Division: {num1} / {num2} = {GREEN}{result}{RESET}\n")
            elif choice == '5':
                print(f"\n{BLUE}Modulus: {num1} % {num2} = {GREEN}{modulus(num1, num2)}{RESET}\n")

        # Exit option
        elif choice == '6':
            print(f"\n{GREEN}*** Thank you for using the Simple Calculator! ***{RESET}\n")
            sys.exit()  # Terminating the program

        else:
            # Handling invalid menu choice
            print(f"{RED}Invalid input! Please enter numeric values [1/2/3/4/5/6].{RESET}\n")
            continue  # Restart the loop to prompt for valid input

        # Asking if the user wants to perform another calculation
        while True:
            next_calculation = input(f"{YELLOW}Do you want to perform another calculation? (y/n): {RESET}").upper()

            # If the user enters 'Y', continue the loop for another calculation
            if next_calculation == 'Y':
                break
            # If the user enters 'N', exit the program
            elif next_calculation == 'N':
                print(f"\n{GREEN}*** Thank you for using the Simple Calculator! ***{RESET}\n")
                sys.exit()  # Terminating the program
            else:
                # Handling invalid input continuation choice
                print(f"{RED}Invalid choice! Please enter 'y' for Yes or 'n' for No.{RESET}\n")
                continue  # Restart the loop to prompt for valid input

# Running the calculator
calculator()