import csv

"""

myResults = [
    ['Name', 'Subject', 'Group', 'Language'],
    ['Fahad', 'Python', 'Science', 'English'],
    ['Anannya', 'Medicine', 'Science', 'English'],
    ['A', 'A', 'A', 'A'],
    ['B', 'B', 'B', 'B'],
    ['C', 'C', 'C', 'C']
]

with open("report.csv", "w") as file:
    lekhok = csv.writer(file)
    lekhok.writerows(myResults)
    print("Completed!")

"""

myResults = []

with open("report.csv", "r") as file:
    pathok = csv.reader(file)

    for row in pathok:
        myResults.append(row)
        print(row)
    
    print(myResults)


