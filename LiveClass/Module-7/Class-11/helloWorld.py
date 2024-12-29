import requests
import matplotlib.pyplot as plt

# Step 1: Fetch data from the API
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

# Step 2: Check if the request was successful
if response.status_code == 200:
    print("Success!")
    data = response.json()  # Converting JSON data into a Python dictionary
else:
    print("Failed to retrieve data. Status code:", response.status_code)
    exit()

# Step 3: Extracting astronaut names and their spacecraft
astronauts = data['people']
for astronaut in astronauts:
    print(f"{astronaut['name']} is on the {astronaut['craft']}")

# Step 4: Count astronauts per spacecraft
craft_counts = {}
for astronaut in astronauts:
    craft = astronaut['craft']
    if craft in craft_counts:
        craft_counts[craft] += 1
    else:
        craft_counts[craft] = 1
print(craft_counts)

# Step 5: Prepare data for plotting
crafts = list(craft_counts.keys())
counts = list(craft_counts.values())

# Step 6: Create the bar chart
plt.bar(crafts, counts, color='skyblue')
plt.xlabel('Spacecraft')
plt.ylabel('Number of Astronauts')
plt.title('Number of Astronauts on Each Spacecraft')
plt.show()

