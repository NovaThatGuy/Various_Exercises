Number_List = []
Largest_Num = None
Smallest_Num = None
file = open("NumberList.txt", 'r')
for line in file:
    print(line.strip())
    Number_List.append(line)
    line = int(line)
    if Largest_Num == None or line > Largest_Num:
        Largest_Num = line
    if Smallest_Num == None or line < Smallest_Num:
        Smallest_Num = line
file.close()
print("Largest Number:", Largest_Num)
print("Smallest Number:", Smallest_Num)

