"""
Author: Fahad Chowdhury
Date: 15 Sep, 2024

Course: Full Stack Web Development with Python, Django & React
Batch: 2
Module: 5
Project: 2
Project Name: Number Guessing Game

Project Description:
This project is a command-line number guessing game where the user is prompted to
guess a randomly generated number between 1 and 100. The game provides feedback on
whether the guess is too high or too low and continues to prompt the user until the
correct number is guessed. The program tracks and displays the number of attempts taken
to guess the correct number. Input validation ensures that only numeric guesses are accepted.

Variables:
- secret_number: Stores the randomly generated number that the user needs to guess.
- attempts: Keeps track of the number of guesses the user has made.

Functions:
- number_guessing_game(): Main function that runs the game. It generates a random number,
prompts the user for guesses, provides feedback, counts the number of attempts, and
handles invalid inputs. The function continues to prompt the user until the correct number is guessed.
"""

import random  # Importing the random module (internal) to generate a random number
import sys # Importing sys module (internal) to handle program exit

# ANSI escape codes to style terminal output
RESET = "\033[0m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"

# Displaying author and project information
print(f"\n{GREEN}{'*' * 70}")
print(f"{GREEN}{'Author'}  {':'}   {'Fahad Chowdhury'}")
print(f"{GREEN}{'Date'}    {':'}   {'16 Sep, 2024'}")
print(f"{GREEN}{'Course'}  {':'}   {'Full Stack Web Development with Python, Django & React'}")
print(f"{GREEN}{'Batch'}   {':'}   {'2'}")
print(f"{GREEN}{'Module'}  {':'}   {'5'}")
print(f"{GREEN}{'Project'} {':'}   {'2'}")
print(f"{GREEN}{'Name'}    {':'}   {'Number Guessing Game'}")
print(f"{GREEN}{'*' * 70}")


# Main function to handle the number guessing game
def number_guessing_game():
    """
    Main function that runs a number guessing game. The user must guess a random
    number between 1 and 100. The program provides feedback on whether the guess is
    too high or too low and continues until the correct number is guessed.
    Error handling ensures valid inputs are provided.
    """

    print()
    print(f"{GREEN}*** Welcome to the Number Guessing Game ***{RESET}")

    print()
    print(f"{GREEN}Try to guess the number between 1 and 100.{RESET}")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)  # Random number for the game
    attempts = 0  # Counter to track the number of attempts made by the user

    while True:
        # Game loop continues until the user guesses the correct number
        try:
            # User input for the guess, converted to integer
            print()
            guess = int(input(f"{YELLOW}Enter your guess: {RESET}"))
            attempts += 1  # Incrementing attempt count for each guess

            # Checking if the guess is lower than the secret number
            if guess < secret_number:
                print(f"{RED}Too low! Try again.{RESET}")

            # Checking if the guess is higher than the secret number
            elif guess > secret_number:
                print(f"{RED}Too high! Try again.{RESET}")

            # If the guess is correct, the user wins and the game ends
            else:
                print(f"\n{GREEN}*** Congratulations! You've guessed the number in {attempts} attempts!***{RESET}")
                break  # Exit the loop as the correct guess is made

        # Exception handling for invalid inputs that aren't integers
        except ValueError:
            print(f"{RED}Invalid input! Please enter a valid number.{RESET}")

# Running the number guessing game
number_guessing_game()