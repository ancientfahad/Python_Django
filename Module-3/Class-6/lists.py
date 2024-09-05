# Lists
fruits = ["apple", "banana", "cherry", 1, True]
fruits1 = ["apple1", "banana1", "cherry1", 2, False]
print(id(fruits))

fruits.append("mango")
fruits.insert(0, "test")
print(id(fruits))

fruits.extend(fruits1)
print(fruits)

fruits.remove("apple")
print(fruits)

lastItem = fruits.pop()
print(lastItem)
print(fruits)

indexNum = fruits.index("apple1")
print(indexNum)

countApple = fruits.count("apple1")
print(countApple)

fruits.clear()
print(fruits)

grade = [90, 100, 95, 75, 85]
grade.sort()
print(grade)

grade.reverse()
print(grade)

length = len(grade)
print(length)

# Running loop within a list
for eachGrades in grade:
    print(eachGrades)