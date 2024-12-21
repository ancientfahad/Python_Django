# Author: Fahad Chowdhury
# Date: 2024-11-27
# Program: Triplet Sum Finder
# Description: This program finds a triplet in an array that sums up to a given integer P.

# def find_triplet_sum(arr, N, P):
#     # Sort the array to enable efficient searching
#     arr.sort()
    
#     # Iterate through the array
#     for i in range(N - 2):
#         # Use two-pointer technique for the remaining part of the array
#         left = i + 1
#         right = N - 1
        
#         while left < right:
#             current_sum = arr[i] + arr[left] + arr[right]
            
#             # If the triplet is found
#             if current_sum == P:
#                 return (f"{arr[i]} {arr[left]} {arr[right]}")
#             elif current_sum < P:
#                 left += 1  # Move the left pointer to increase the sum
#             else:
#                 right -= 1  # Move the right pointer to decrease the sum
    
#     return None  # No triplet found

# # Input
# try:
#     N = int(input(""))
#     if N <= 0:
#         print("The array size should be greater than 0.")
#     else:
#         arr = list(map(int, input().split()))
#         if len(arr) != N:
#             print("Error: The number of integers does not match the specified size.")
#         else:
#             P = int(input())
            
#             # Find the triplet
#             result = find_triplet_sum(arr, N, P)
            
#             # Output the result
#             if result:
#                 print(result)
#             else:
#                 print("No triplet found.")
# except ValueError:
#     print("Error: Invalid input. Please enter integers only.")


# Author: Fahad Chowdhury
# Date: 2024-11-27
# Program: Lone Zero Counter
# Description: This program counts the number of lone zeroes in a given integer.
# Constraints: The input integer N must satisfy 0 ≤ N ≤ 100000.

# def countLoneZeroes(num):
#     count = 0
#     strNum = str(num)

#     for i in range(len(strNum)):
#         if(strNum[i] == '0'):
#             if(i == '0' and strNum[i+1] != '0'):
#                 count += 1
#             elif(strNum[i - 1] != '0' and strNum[i+1] != '0'):
#                 count += 1
    
#     print(count)

# def main():
#     num = int(input())
#     countLoneZeroes(num)

# if __name__ == "__main__":
#     main()

# def count_lone_zeroes(N):
#     # Convert the number to a string for easier indexing
#     number_str = str(N)
#     count = 0
    
#     # Iterate through the string to check for lone zeroes
#     for i in range(len(number_str)):
#         if number_str[i] == '0':
#             # Check if the 0 is lone
#             if (i == 0 or number_str[i - 1] != '0') and (i == len(number_str) - 1 or number_str[i + 1] != '0'):
#                 count += 1
    
#     return count

# # Input
# try:
#     N = int(input())
    
#     if N < 0 or N > 100000:
#         print("Error: The number must be between 0 and 100000.")
#     else:
#         # Output the number of lone zeroes
#         print(count_lone_zeroes(N))
# except ValueError:
#     print("Error: Please enter a valid integer.")
