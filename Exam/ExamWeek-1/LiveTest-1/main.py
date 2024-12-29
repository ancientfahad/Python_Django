# Author: Al Fahad Chowdhury
# Date: 19 Sep, 2024

# Calculate ticket price
def calculateTicketPrice(age, showtime):
    # Determine ticket price based on age
    if age <= 10:
        price = 300
    elif age > 10 and age <= 25:
        price = 500
    elif age > 25 and age <= 60:
        price = 800
    else:
        price = 400
    
    # Check if discount applicable based on showtime
    if showtime < 1700:
        discount = price * 0.10
        discountPrice = price - discount
        
        print(f"Ticket Price    :   {price} BDT")
        print(f"Discount        :   {discount:.2f} BDT")
        print(f"Discounted Price:   {discountPrice:.2f} BDT")
    
    else:
        discount = 0
        discountPrice = price - discount
        
        print(f"Ticket Price    :   {price} BDT")
        print(f"Discount        :   {discount:.2f} BDT")
        print(f"Discounted Price:   {discountPrice:.2f} BDT")

# Validate age
def isValidAge(age):
    if age <= 0:
        print(f"Age must be greater than 0.\n")
        return False
    else:
        return True

# Validate showtime
def isValidShowtime(showtime):
    # 24-hour format can't be less than 0000 (12:00am) or greater than 2359 (11:59pm)
    # showtime % 100 determines the minutes (1930 % 100 = 30) and minutes can't be greater than 59
    if showtime < 0 or showtime > 2359 or showtime % 100 > 59:
        print(f"Showtime should be in 24-hour format (HHMM). For example: 1930.\n")
        return False
    else:
        return True

def main():
    # Validate age
    while True:    
        try:
            age = int(input("Enter your age: "))
            if isValidAge(age):
                break
        except Exception:
            print(f"Invalid input! Please enter a valid numeric value for age.\n")
    
    print()
    
    # Validate showtime
    while True:
        try:
            showtime = int(input("Enter your preferred showtime in 24-hour format (HHMM): "))
            if isValidShowtime(showtime):
                break
        except Exception:
            print(f"Invalid input! Please enter a valid numeric value for showtime in 24-hour format (HHMM).\n")
    
    print()
    
    calculateTicketPrice(age, showtime)
    
main()