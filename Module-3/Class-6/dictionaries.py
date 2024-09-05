# bill = {"a", "b", "c", "d"} #set

bill = {
    "name":"Bill Gates",
    "age":65,
    "country":"USA",
    "occupation":"Business",
    "gender":"Male"
}

print("Dictionary: ", bill)
print("Keys: ", bill.keys())
print("Values: ", bill.values())
print("Specific: ", bill['name'])
print("Get: ", bill.get('name'))

bill.update(
    {
        "age":75,
        "occupation":"Charity"
    }
)
print("Update: ", bill)

bill.clear()
print("Clear: ", bill)