def check_requirements (price, brand, color, mileage):

    car1Price = 30000
    car1Brand = "BMW"
    car1Color = "Blue"
    car1Mileage = 40000

    car2Price = 20000
    car2Brand = "Toyota"
    car2Color = "Black"
    car2Mileage = 30000

    if (
        (car1Price <= price) and
        (car1Brand == brand) and
        (car1Color == color) and
        (car1Mileage <= mileage)):
        return "Car 1"
    elif (
        (car2Price <= price) and
        (car2Brand == brand) and
        (car2Color == color) and
        (car2Mileage <= mileage)):
        return "Car 2"
    else:
        return False


print("*** Welcome to our Car Shop! ***\n\n")
print("Enter your requirements below:\n")

customerPrefPrice = int(input("What is your budget? (usd) : "))
customerPrefBrand = input("What is your favorite brand? : ").title()
customerPrefColor = input("What color do you prefer? : ")
customerPrefMileage = int(input("What is your maximum mileage preference? (kms) : "))

result = check_requirements(customerPrefPrice, customerPrefBrand, customerPrefColor, customerPrefMileage)

if result == False:
    print("Unfortunately, our car's didn't meet your requirements!")
else:
    print("You can consider our ", result)

today = input("What day is today? : ").title()
public_holiday = input("Is it a public holiday? (Y/N) : ").upper()
is_sick_today = input("Are you sick today? (Y/N) : ").upper()


if today == "Sunday" or today == "Saturday":
    print("No office today")
elif public_holiday == "Y":
    print("No office today")
elif is_sick_today == "N":
    print("No office today")
else:
    print("You have to go to office today")
