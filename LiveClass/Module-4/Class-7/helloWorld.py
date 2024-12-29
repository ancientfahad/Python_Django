import random

numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 100))

print(numbers)

#numbers = [1, 6, 3, 2, 6, 2, 10, 1, 5, 9]
max_number = float('-inf')

for n in numbers:
    if n > max_number:
        max_number = n

print(max_number)
print(max(numbers))

# print(dir(random))
# print(help(random.sample))