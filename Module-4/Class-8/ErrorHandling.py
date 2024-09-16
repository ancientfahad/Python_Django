import json

try:
    with open("new1.json", "r") as file:
        data = json.load(file)
        print(data)
except Exception as error:
    print(error)
finally:
    print("Stop the loading animation......")