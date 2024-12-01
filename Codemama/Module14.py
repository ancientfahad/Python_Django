# ### Personalized greeting

# # Author: Fahad Chowdhury
# # Date: 2024-11-27
# # Program: Personalized Greeting
# # Description: This program asks the user for their name and prints a personalized greeting.
# # Constraints: The input string S must be between 1 and 1000 characters.

# def personalized_greeting():
#     name = input().strip()
    
#     # Check constraints
#     if 1 <= len(name) <= 1000:
#         print(f"Hello, {name}! Nice to meet you.")
#     else:
#         print("Error: Name length must be between 1 and 1000 characters.")

# ### Simple Summation
# # personalized_greeting()

# # Author: Fahad Chowdhury
# # Date: 2024-11-27
# # Program: Sum of Two Numbers
# # Description: This program calculates and prints the sum of two integers entered by the user.
# # Constraints: Each integer must satisfy -2^31 ≤ integer ≤ 2^31 - 1.

# def sum_of_two_numbers():
#     try:
#         a, b = map(int, input().split())
        
#         if -2**31 <= a <= 2**31 - 1 and -2**31 <= b <= 2**31 - 1:
#             result = a + b
            
#             print(result)
#         else:
#             print("Error: Each number must be between -2^31 and 2^31 - 1.")
#     except ValueError:
#         print("Error: Please enter valid integers separated by space.")

# # Run the function
# sum_of_two_numbers()

# ### Even or Odd

# # Author: Fahad Chowdhury
# # Date: 2024-11-27
# # Program: Even or Odd Checker
# # Description: This program checks if an integer entered by the user is even or odd.
# # Constraints: The input integer must satisfy -2^31 ≤ integer ≤ 2^31 - 1.

# def even_or_odd():
#     try:
#         number = int(input().strip())
        
#         # Check constraints
#         if -2**31 <= number <= 2**31 - 1:
#             if number % 2 == 0:
#                 print(f"{number} is an even number.")
#             else:
#                 print(f"{number} is an odd number.")
#         else:
#             print("Error: The number must be between -2^31 and 2^31 - 1.")
#     except ValueError:
#         print("Error: Please enter a valid integer.")

# # Run the function
# even_or_odd()

### Counting Characters

# Author: Fahad Chowdhury
# Date: 2024-11-27
# Program: Character Counter
# Description: This program counts the number of characters in a string entered by the user.
# Constraints: The output will always be an unsigned integer.

def count_characters():
    user_input = input("")
    character_count = len(user_input)
    print(character_count)

count_characters()