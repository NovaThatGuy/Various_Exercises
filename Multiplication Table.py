'''
A simple Python program running through the 1 - 10 mulitpliers of a given number
'''
Number = int(input("Please enter a number: "))
for Multiplier in range(1, 11):
    Answer = Number * Multiplier
    print (Number, " * ", Multiplier, " = ", Answer)