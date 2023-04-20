import json
import csv

# Generate data
data = []
for i in range(1, 501):
    title = f"english{i}"
    language = f"english{i % 10}"
    genre = f"fiction{i % 5}"
    # Create an object with the generated data
    obj = {
        "title": title,
        "author": {
            "name": f"sky{i}",
            "bio": "created the author"
        },
        "language": {
            "name": language
        },
        "genre": {
            "name": genre
        },
        "publisher": {
            "name": f"skyward{i}",
            "address": f"Bangalore{i}"
        },
        "min_age": 20,
        "price": i * 1,
        "stock": i * 10,
        "description": "created for reading"
    }
    data.append(obj)

# Print data from one to one lakh
for i, obj in enumerate(data):
    print(f"Object {i + 1}: {obj}")

# Write data to a JSON file
with open('output.json', 'w') as file:
    json.dump(data, file)

# Write data to a CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
