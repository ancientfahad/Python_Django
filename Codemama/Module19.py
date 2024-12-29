# # Author: Fahad Chowdhury
# # Date: 2024-12-24
# # Program: Leap Year
# # Description: This program identifies if the year entered is a leap year or not.
# # Constraints: -2^31 ≤ a, b ≤ 2^31 - 1

# def leap_year():
#     try:
#         # Input the year
#         year = int(input())
        
#         # Check constraints
#         if -2**31 <= year <= 2**31 - 1:
#             if year == 0:
#                 print("Error: Invalid year.")
#             else:
#                 # Check if the year is a leap year
#                 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#                     print(f"{year} is a leap year.")
#                 else:
#                     print(f"{year} is not a leap year.")
#         else:
#             print("Error: Numbers must be between -2^31 and 2^31 - 1.")
#     except ValueError:
#         print("Error: Please enter a valid integer.")

# # Run the function
# leap_year()

# # Author: Fahad Chowdhury
# # Date: 2024-12-27
# # Program: Distance Calculator
# # Description: This program calculates the distance between two points in a 2D space.
# # Output: The distance is printed with exactly two decimal points.

# import math

# def calculate_distance():
#     try:
#         # Input coordinates for two points
#         # print("Enter the coordinates of the first point (x1 y1):")
#         x1, y1 = map(float, input().split())
        
#         # print("Enter the coordinates of the second point (x2 y2):")
#         x2, y2 = map(float, input().split())
        
#         # Calculate distance using the distance formula
#         distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
#         # Output the result with two decimal points
#         print(f"Distance: {distance:.2f}")
#     except ValueError:
#         print("Error: Please enter valid floating-point numbers.")

# # Run the function
# calculate_distance()

# # Author: Fahad Chowdhury
# # Date: 2024-12-25
# # Program: Number Type Checker
# # Description: This program checks whether a number is positive, negative, or zero.

# def check_number_type():
#     try:
#         # Input an integer
#         num = int(input())
        
#         # Check constraints
#         if -2**31 <= num <= 2**31 - 1:
#             # Determine the type of number
#             if num > 0:
#                 print(f"{num} is a positive number.")
#             elif num < 0:
#                 print(f"{num} is a negative number.")
#             else:
#                 print("The number is zero.")
#         else:
#             print("Error: The number must be between -2^31 and 2^31 - 1.")
#     except ValueError:
#         print("Error: Please enter a valid integer.")

# # Run the function
# check_number_type()

# Author: Fahad Chowdhury
# Date: 2024-12-25
# Program: Swap Two Variables
# Description: This program swaps the values of two integers.

def swap_values():
    try:
        # Input two integers
        num1, num2 = map(int, input().split())
        
        # Check constraints
        if -2**31 <= num1 <= 2**31 - 1 and -2**31 <= num2 <= 2**31 - 1:
            # Display before swapping
            print(f"Before swapping: num1 = {num1}, num2 = {num2}")
            
            # Swap the values
            num1, num2 = num2, num1
            
            # Display after swapping
            print(f"After swapping: num1 = {num1}, num2 = {num2}")
        else:
            print("Error: Numbers must be between -2^31 and 2^31 - 1.")
    except ValueError:
        print("Error: Please enter valid integers.")

# Run the function
swap_values()