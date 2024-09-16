import json
import os

DictionaryData = {
    "name": "Ostad",
    "age": True,
    "city": "Dhaka",
    "titles": ["Python", "Django", "React"]    
}

JsonString = json.dumps(DictionaryData, indent=4)
print(JsonString)

with open("new.json", "w") as file:
    json.dump(DictionaryData, file, indent=4)
    print("Completed!")

with open("new.json", "r") as file:
    DictionaryDataFromJson = json.load(file)
    print(DictionaryDataFromJson)
    print(DictionaryDataFromJson['name'])



