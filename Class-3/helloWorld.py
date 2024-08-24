print("Hello", "World")

print(10 / 3) #normal division
print(10 // 3) #integer division

# Loop
for i in range(10):
    print(i)
    
for i in range(10):
    print("*" * i)
    
for i in range(10):
    print("*" * (i+1))

# if - else
num = input("Enter your number: ")
print(type(num))

num = int(num)
print(type(num))

if num % 2 == 0:
    print("Even")

else:
    print("Odd")

