'''
Exericse about For Loops and Continues
'''
Inputs = 0
AllNumbers = []
while Inputs < 5:
    Number = int(input("Input a number: "))
    AllNumbers.append(Number)
    Inputs += 1
for Odds in AllNumbers:
    if Odds % 2 == 0:
        continue
    print(Odds)