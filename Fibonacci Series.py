def Fibonacci(User_Input):
    Next = 0
    last_input = 0
    current_input = 0
    for Numbers in range(0, User_Input):
        if current_input + last_input < User_Input:
            Next = current_input + last_input
            #print("Count:", Numbers, "| Math: ", last_input, "+", current_input, "=", Next)
            if Next == 1:
                print("1")
            print(Next)
            last_input = current_input
            current_input = Next
            if current_input <= 0:
                current_input = current_input + 1
Fibonacci(User_Input=int(input("Enter a Number: ")) + 1)