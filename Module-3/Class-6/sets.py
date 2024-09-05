countries = {"Bangladesh", "Pakistan", "China", "Philippines"}
print(countries)
print(id(countries))

countries.add("USA")
print("Add: ", countries)

countries.add("USA")
print("Add", countries)

countries.remove("USA")
print("Remove: ", countries)

countries.update(['A', 'B'])
print("Update: ", countries)

lastItem = countries.pop()
print("Pop: ", lastItem)

city = {"Dhaka", "Karachi", "Beijing", "Manila", "A"}
result = countries.union(city)
print("Union: ", result)

result = countries.intersection(city)
print(result)

countries.clear()
print("Clear: ", countries)