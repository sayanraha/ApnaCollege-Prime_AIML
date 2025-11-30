'''
Create  a Python dictionary of 3 cities and their populations. Save it to "cities.json".
1. Then load the JSON and print each city and its population
2. Ask the user for a new city & its population - update this info in the json file.

'''


import json

# --- Step 1: Create and save initial dictionary ---
cities = {
    "Kolkata": "10 crore",
    "Delhi": "8 crore",
    "Mumbai": "15 crore"
}

# Convert Python dict → JSON string and save to file
with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)

print("Initial data saved successfully!")

# --- Step 2: Load JSON and print all cities ---
with open("cities.json", "r") as f:
    data = json.load(f)

print("\nCurrent cities and populations:")
for city, pop in data.items():
    print(f"{city} : {pop}")

# --- Step 3: Ask user for city + population and update JSON file ---
new_city = input("\nEnter new city name: ")
new_population = input("Enter population: ")

data[new_city] = new_population  # update dictionary

# Save updated dictionary back to JSON file
with open("cities.json", "w") as f:
    json.dump(data, f, indent=4)

print("\nCity added and file updated successfully!")





