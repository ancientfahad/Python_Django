# ### Check if text contains Vowel

# def checkText(text):
#     vowels = ['A', 'E', 'I', 'O', 'U']

#     for character in text:
#         if character in vowels:
#             return 'The string contains a vowel.'

#     return 'The string does not contain any vowel.'

# text = input("Enter a string\n").upper()
# print(checkText(text))

### BMI Calculator

# def bmiCalculator(weight, height):

#     bmi = float(weight / (height ** 2))
#     print('BMI:', round(bmi, 2))

#     if bmi < 18.5:
#         print('Underweight')
#     elif bmi >= 18.5 and bmi < 25.0:
#         print('Normal weight')
#     elif bmi >= 25.0 and bmi < 30.0:
#         print('Overweight')
#     else:
#         print('Obese')

# data = input()

# height = float(data.split()[0])
# weight = float(data.split()[1])

# bmiCalculator(weight, height)

### Find Next Number
# def findNextNumber(a, b, c):

#     common_difference1 = b - a
#     common_difference2 = c - b

#     if common_difference1 == common_difference2:
#         next_number = c + common_difference1
#     else:
#         next_number = c + common_difference2
    
#     return next_number

# num = input()
# a = int(num.split()[0])
# b = int(num.split()[1])
# c = int(num.split()[2])
    
# print(findNextNumber(a, b, c))