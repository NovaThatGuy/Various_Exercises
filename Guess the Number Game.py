import random

target_number = random.randint(1, 100)
attempts = 0

print("!!!Welcome to Random Number Game!!!")
while True:
    answer = int(input("Please Enter a Number: "))
    attempts += 1
    if answer > target_number:
        print("You are too high")
    elif answer < target_number:
        print("You are too low")
    else:
        print("That was the answer! ", target_number)
        print('It took you ', attempts, " tries!")
        break

