"""class Profile:
    name = "Fahad Chowdhury"
    age = 30

    # init is a default function within a class
    def __init__(self, num1, num2, ageValue, dobValue) -> None:
        sum = num1 + num2
        print(sum)

        self.age = ageValue

        self.dob = dobValue

    # self is a mandatory parameter for all functions within a class
    def aboutMe(self, city):
        print(f"My name is {self.name} and I am {self.age} years old. I live in {city}. My date of birth is {self.dob}.")

profileObj = Profile(5, 10, 21, "07/13/1994")
profileObj.aboutMe("Dhaka")

class Father:

    x = 10
    y = 20

    def add(self):
        sum = self.x + self.y
        print(sum)

class Mother:

    a = 30
    b = 40

    def subtract(self):
        sub = self.a - self.b
        print(sub)

class Son(Father):
    pass



obj = Son()

# From Father
print(obj.x)
print(obj.y)

obj.add()

objMain = Father()
print(objMain.x)
print(objMain.y)

obj.add()

class GrandFather:
    x = 10

class Father(GrandFather):
    pass

class Myself(Father):
    pass

grandFatherObj = GrandFather()
fatherObj = Father()
myObj = Myself()

print(grandFatherObj.x, fatherObj.x, myObj.x)

class Father:
    def vote(self):
        print("ভোট পেয়েছে 70000000")


class Daughter(Father):

    # Overriding
    def vote(self):
        print("ভোট চুরি করেছে")

obj = Daughter()
obj.vote()

from abc import ABC, abstractmethod


class Father(ABC):
    num1 = 200
    num2 = 300

    @abstractmethod
    def add(self):
        sum = self.num1 + self.num2
        print(f"Sum is {sum}")

    @abstractmethod
    def subtract(self):
        sub = self.num1 - self.num2
        print(f"Sub is {sub}")

    @abstractmethod
    def divison(self):
        div = self.num1 / self.num2
        print(f"Div is {div}")

    @abstractmethod
    def multiplication(self):
        mul = self.num1 * self.num2
        print(f"Mul is {mul}")


class Son(Father):

    def add(self):
        sum = self.num1 + self.num2
        print(f"Sum is {sum}")


    def subtract(self):
        sub = self.num1 - self.num2
        print(f"Sub is {sub}")


    def divison(self):
        div = self.num1 / self.num2
        print(f"Div is {div}")


    def multiplication(self):
        mul = self.num1 * self.num2
        print(f"Mul is {mul}")

obj = Son()
obj.add()
obj.subtract()
obj.divison()
obj.multiplication()

class Bangladesh:

    # By using default params
    def dhaka(self, a = 0, b = 0, c = 0, d = 0):
        print(a + b + c + d)
    
    # Variable length argument
    def shahbag(self, *andolon):
        print(andolon)

obj = Bangladesh()
obj.dhaka(10)
obj.dhaka(10, 10)
obj.dhaka(10, 10, 10)
obj.dhaka(10, 10, 10, 10)

obj.shahbag("a")
obj.shahbag("a", "b")
obj.shahbag("a", "b", "c")
obj.shahbag("a", "b", "c", "d")
obj.shahbag("a", "b", "c", "d", "e")
obj.shahbag("a", "b", "c", "d", "e", "f")
obj.shahbag("a", "b", "c", "d", "e", "f", "g")

class OloshClass:
    x = 10
    y = 20

    @staticmethod
    def add():
        sum = OloshClass.x + OloshClass.y
        print(sum)

OloshClass.add()

class Family:
    
    Husband = "X"
    _Wife = "Y"
    __Son = "Z"

    def func1(self):
        print(self.Husband)
        print(self._Wife)
        print(self.__Son)

class RelativeFamily:
    
    def func2(self):
        print(self.Husband)

obj = Family()
obj.func1()

obj1 = RelativeFamily()
obj1.func2()

class SCB:
    
    __balance = 0

    def deposit(self, taka):
        if taka <= 0:
            print("Invalid deposit amount!")
        else:
            self.__balance += taka
            print("Deposit successful!")

    def withdraw(self, taka):
        if taka <= 0:
            print("Invalid withdraw amount!")
        elif taka >= self.__balance:
            print("Insufficiant fund!")
        else:
            self.__balance -= taka
            print("Withdrawal successful!")

    def check(self):
        print(f"Balance is {self.__balance}")

obj = SCB()

obj.check()
obj.deposit(100)
obj.check()
obj.withdraw(50)
obj.check()"""

class Family:
    
    Husband = "X"
    _Wife = "Y"
    __Son = "Z"

    def func1(self):
        print(self.Husband)
        print(self._Wife)
        print(self.__Son)

class RelativeFamily(Family):
    
    def func2(self):
        print(self.Husband)

obj = Family()
obj.func1()

obj1 = RelativeFamily()
obj1.func2()