import csv

with open('TestCSV.csv', newline='') as file:
    reader = csv.reader(file)

    header = next(reader, None)

    for row in reader:
        name, age , location = row
        print(f"Name: {name}, Age: {age}, Location: {location}")