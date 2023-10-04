import csv

with open('Grants.csv', newline='') as file:
    reader = csv.reader(file)

    for row in reader:
        Submission_Time, NameOfOrg, Date, Name, Address, Zip, Email, Dollar, Number, Explain = row
        print({Submission_Time}, {NameOfOrg})