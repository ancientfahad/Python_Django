current_temp = 31
reference_temp = 28

# Greater than
current_temp > reference_temp

# Greater than or equals
current_temp >= reference_temp

# Less than
current_temp < reference_temp

# Less than or equals
current_temp <= reference_temp

# Comparision Operator | Equals
current_temp == reference_temp

# Assign Operator
# current_temp = reference_temp

# Not Equals
current_temp != reference_temp

# Mod
current_temp % 2 == 0

result = current_temp % 2 == 0

print(result)
print(type(result))

if result == True:
    print(current_temp, "is an even number")
else:
    print(current_temp, "is an odd number")

