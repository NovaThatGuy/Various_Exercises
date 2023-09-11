import random
NumberList = []
def Generator(NumberAmt):
    for Numbers in range(0, NumberAmt):
        RandNum = random.randrange(0, 101)
        NumberList.append(RandNum)
    print(NumberList)
Generator(int(input("How many numbers do you want to generate:")))
def Write_File(filename, NumberList):
    file = open(filename, 'w')
    for Numbs in NumberList:
        file.write(str(Numbs) + '\n')
    file.close()
Write_File("NumberList.txt", NumberList)