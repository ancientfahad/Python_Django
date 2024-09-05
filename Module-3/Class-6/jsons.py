import json
from textwrap import indent

"""

billObject = {
    "name":"Bill Gates",
    "age":65,
    "country":"USA",
    "occupation":"Business",
    "gender":"Male"
}

# billJSON = json.dumps(billObject)
billJSON = json.dumps(billObject, indent = 4)
print(billJSON)

billJSON = '{"name": "Bill Gates", "age": 65, "country": "USA", "occupation": "Business", "gender": "Male"}'
billObject = json.loads(billJSON)

print(billObject)

"""

users = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 30},
    {"name": "C", "age": 40},
    {"name": "D", "age": 50},
]

usersJSONArray = json.dumps(users, indent = 4)
print(usersJSONArray)

