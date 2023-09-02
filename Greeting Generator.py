import random

def Generator (Name, Greet_Dictionary = None, Question_Dictionary = None):
    if Greet_Dictionary is None:
        Greet_Dictionary = {
            1: "Hello",
            2: "Greetings",
            3: "Good Day",
            4: "Hi",
            5: "Howdy"
        }
    if Question_Dictionary is None:
        Question_Dictonary = {
            1: "I hope you are having a wonderful day!",
            2: "how are you today?",
            3: "I hope the weather is nice today.",
            4: "remember to make the most of your day.",
            5: "remember nothing is impossible."
        }
    
    Greet_Option = random.randint(1, len(Greet_Dictionary))
    Question_Option = random.randint(1, len(Question_Dictonary))
    
    Greet = Greet_Dictionary.get(Greet_Option)
    Question = Question_Dictonary.get(Question_Option)
    
    print(Greet, Name, Question)

Name = input("Hello what's your name? ")
Generator(Name)

