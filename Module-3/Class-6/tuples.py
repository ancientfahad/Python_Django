#Tuples
from itertools import count
from operator import index

cities = ("Dhaka", "Khulna", "Chittagong")
print(id(cities))

cities = ("Dhaka", "Khulna", "Chittagong")
print(id(cities))

cities = ("Dhaka", "Khulna")
print(id(cities))

cities = ("Dhaka", "Khulna", "Chittagong", "Dhaka", 1, True, 1, "Dhaka")
print(cities)

countDhaka = cities.count("Dhaka")
print(countDhaka)

indexOfDhaka = cities.index("Dhaka")
print(indexOfDhaka)

for city in cities:
    print(city)
