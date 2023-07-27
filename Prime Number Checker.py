'''
Simple program to check whether or not a number is a Prime Number
THIS DOES NOT WORK, NEEDS TO BE REDONE
'''
Number = int(input("Input a number: "))

for Check in range(1, Number):
    if Check % 2 or Check == 1:
        if Check == Number:
            print(Number, " is a Prime Number")
    elif Check != Number:
        continue
    else:
        print(Number, " is not a Prime Number")