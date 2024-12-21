# # Author: Fahad Chowdhury
# # Date: 2024-11-27
# # Program: Remainder Calculator
# # Description: This program calculates the remainder of two integers using the modulo operation.
# # Constraints: -2^31 ≤ a, b ≤ 2^31 - 1

# def calculate_remainder():
#     try:
#         # Input two integers
#         a, b = map(int, input().split())
        
#         # Check constraints
#         if -2**31 <= a <= 2**31 - 1 and -2**31 <= b <= 2**31 - 1:
#             if b == 0:
#                 print("Error: Division by zero is not allowed.")
#             else:
#                 # Calculate remainder
#                 remainder = a % b
#                 # Output the result
#                 print(remainder)
#         else:
#             print("Error: Numbers must be between -2^31 and 2^31 - 1.")
#     except ValueError:
#         print("Error: Please enter valid integers.")

# # Run the function
# calculate_remainder()

# Author: Fahad Chowdhury
# Date: 2024-11-27
# Program: Quotient Calculator
# Description: This program calculates the quotient of two integers using integer division.
# Constraints: -2^31 ≤ a, b ≤ 2^31 - 1

def calculate_quotient():
    try:
        # Input two integers
        a, b = map(int, input().split())
        
        # Check constraints
        if -2**31 <= a <= 2**31 - 1 and -2**31 <= b <= 2**31 - 1:
            if b == 0:
                print("Error: Division by zero is not allowed.")
            else:
                # Calculate quotient using integer division
                quotient = a // b
                # Output the result
                print(quotient)
        else:
            print("Error: Numbers must be between -2^31 and 2^31 - 1.")
    except ValueError:
        print("Error: Please enter valid integers.")

# Run the function
calculate_quotient()