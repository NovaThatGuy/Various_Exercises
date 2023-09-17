import random

def D20(roll_count):
    print("Rolling", roll_count, "D20")
    rolls = []
    counter = 0
    while counter < roll_count:
        number = random.randrange(1, 21)
        rolls.append(number)
        counter += 1
    print(rolls)

def D4(roll_count):
    print("Rolling", roll_count, "D4")
    rolls = []
    counter = 0
    while counter < roll_count:
        number = random.randrange(1, 5)
        rolls.append(number)
        counter += 1
    print(rolls)

def D6(roll_count):
    print("Rolling", roll_count, "D6")
    rolls = []
    counter = 0
    while counter < roll_count:
        number = random.randrange(1, 7)
        rolls.append(number)
        counter += 1
    print(rolls)

def D8(roll_count):
    print("Rolling", roll_count, "D8")
    rolls = []
    counter = 0
    while counter < roll_count:
        number = random.randrange(1, 9)
        rolls.append(number)
        counter += 1
    print(rolls)

def D10(roll_count):
    print("Rolling", roll_count, "D10")
    rolls = []
    counter = 0
    while counter < roll_count:
        number = random.randrange(1, 11)
        rolls.append(number)
        counter += 1
    print(rolls)

def D12(roll_count):
    print("Rolling", roll_count, "D12")
    rolls = []
    counter = 0
    while counter < roll_count:
        number = random.randrange(1, 13)
        rolls.append(number)
        counter += 1
    print(rolls)

def D100(roll_count):
    print("Rolling", roll_count, "D100")
    rolls = []
    counter = 0
    while counter < roll_count:
        number = random.randrange(1, 101)
        rolls.append(number)
        counter += 1
    print(rolls)

while True:
    print("Welcome to the Dice Roller!")
    Dice_Type = int(input("What kind of dice would you like to roll?\n1: D20\n2: D4\n3: D6\n4: D8\n5: D10\n6: D12\n7: D100\n8: End Program\nEnter a Number: "))
    if Dice_Type == 1:
        D20(roll_count=int(input("How many would you like to roll: ")))
    if Dice_Type == 2:
        D4(roll_count=int(input("How many would you like to roll: ")))
    if Dice_Type == 3:
        D6(roll_count=int(input("How many would you like to roll: ")))
    if Dice_Type == 4:
        D8(roll_count=int(input("How many would you like to roll: ")))
    if Dice_Type == 5:
        D10(roll_count=int(input("How many would you like to roll: ")))
    if Dice_Type == 6:
        D12(roll_count=int(input("How many would you like to roll: ")))
    if Dice_Type == 7:
        D100(roll_count=int(input("How many would you like to roll: ")))
    if Dice_Type == 8:
        break
    elif Dice_Type > 8 or Dice_Type < 1:
        print("Invalid Response")