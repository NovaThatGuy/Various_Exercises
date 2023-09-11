file = open('Number List.txt', 'r')
Lowest_Number = 0
Highest_Number = 0
print("All Numbers: ")
for line in file:
    line = int(line)
    if Lowest_Number > line or Lowest_Number == 0:
        Lowest_Number = line
    if Highest_Number < line:
        Highest_Number = line
    line = str(line)
    print(line.strip())
print("Highest Number:", Highest_Number)
print("Lowest Number:", Lowest_Number)

file.close()