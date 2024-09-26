"""

x = 5
y = 5.6
z = False

print(type(x))
print(type(y))
print(type(z))

print(dir(x))
print(x.numerator)
print(x.denominator)
print(x.bit_length())

my_list = [1, 2, 3]

print(type(my_list))
print(dir(my_list))

class MyClass:
    total = 6
    
    def say_hello():
        print("Hello!!!")
        
print(MyClass.total)
MyClass.say_hello()

class MyClass:
    pass

obj1 = MyClass()
print(obj1)

"""

import math

class Fraction:
    def __init__(self, num, denom): # Constructor
        self.numerator = num
        self.denominator = denom
    
    def __str__(self) -> str: # Double Underscore / Magic Method
        return "{} / {}".format(self.numerator, self.denominator)
    
    def simplify(self):
        g = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator / g
        self.denominator = self.denominator / g
        
    def add(self, f):
        denom = math.lcm(self.denominator, f.denominator)
        num = (denom // self.denominator) * self.numerator + \
            (denom // f.denominator) * f.numerator
        
        self.numerator = num
        self.denominator = denom
        
    def __add__(self, f):
        denom = math.lcm(self.denominator, f.denominator)
        num = (denom // self.denominator) * self.numerator + \
            (denom // f.denominator) * f.numerator
        
        return Fraction(num, denom)
        
    
f1 = Fraction(20, 40)
f2 = Fraction(10, 40)
f3 = f1 + f2

print(f3)
# print(dir(f3))

# print(f1.numerator, f1.denominator)
# print(f1.__str__())

# print(f1)
# f1.simplify()
# print(f1)