def Find_Max_Min(Numbers = []):
    Min = None
    Max = None
    Run_Count = 0
    for Nums in Numbers:
        Run_Count = Run_Count + 1
        if Run_Count == 1:
            Min = Nums
            Max = Nums
        if Min > Nums:
            Min = Nums
        if Max < Nums:
            Max = Nums
    print("Max:", Max, "Min:", Min)
def Filter_Even_Numbers(Numbers = []):
    Even=[]
    for Nums in Numbers:
        if Nums % 2 == 0:
            Even.append(Nums)
    print("Original:", Numbers)
    print("Even", Even)
def Sum_Calculator(Numbers = []):
    Variable1 = 0   
    for Nums in Numbers:
        Variable1 = Variable1 + Nums
    print("Original:", Numbers)
    print("Sum:", Variable1)

Find_Max_Min([1,2,3,4,5,6,7,8,9,10])
print("Filtered Evens")
Filter_Even_Numbers([1,2,3,4,5,6,7,8,9,10])
Sum_Calculator([1,2,3,4,5])