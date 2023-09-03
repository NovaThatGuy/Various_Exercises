import random

Repeat = None
Ready = 0
Cards = {}

for card_number in range(1, 13):
    if card_number < 11 and card_number != 1:
        Cards[card_number] = f"{card_number}"
    elif card_number == 11:
        Cards[card_number] = "Jack"
    elif card_number == 12:
        Cards[card_number] = "Queen"
    elif card_number == 13:
        Cards[card_number] = "King"
    elif card_number == 1:
        Cards[card_number] = "Ace"

Card_Type = {
    1: "of Clubs",
    2: "of Diamonds",
    3: "of Spades",
    4: "of Hearts"
}
#   Single Card
def OneCard(Player_Answer):
    Chosen_Card = random.randint(1, len(Cards))
    Chosen_Card_Type = random.randint(1, len(Card_Type))
    Card_Num = Cards.get(Chosen_Card)
    Card_Type_Answer = Card_Type.get(Chosen_Card_Type)
    if Player_Answer == Card_Num:
        print(f"Congrats you chose the right card!", Card_Num, Card_Type_Answer)
    else:
        print(f"That is incorrect, the card was: ", Card_Num, Card_Type_Answer)
#   Two Card
def TwoCard(Player_Answer):
    Chosen_Card = random.randint(1, len(Cards))
    Chosen_Card2 = random.randint(1, len(Cards))
    Chosen_Card_Type = random.randint(1, len(Card_Type))
    Chosen_Card_Type2 = random.randint(1, len(Card_Type))
    Card_Num = Cards.get(Chosen_Card)
    Card_Num2 = Cards.get(Chosen_Card2)
    Card_Type_Answer = Card_Type.get(Chosen_Card_Type)
    Card_Type_Answer2 = Card_Type.get(Chosen_Card_Type2)
    if Player_Answer == Card_Num or Player_Answer == Card_Num2:
        print(f"Congrats you chose one the right card!", Card_Num, Card_Type_Answer, "and", Card_Num2, Card_Type_Answer2)
    else:
        print(f"That is incorrect, the cards were: ", Card_Num, Card_Type_Answer, "and", Card_Num2, Card_Type_Answer2)
#   Interface
print("Welcome to the Card Game Hub")
while True:
    print("Please select a Game to play!")
    print("[1] Single Card Guessing")
    print("[2] Two Card Guessing")
    print("[3] Exit Program")
    Ready = 0
    Option = int(input ())

    if Option == 1:
        while Ready != 1:
            OneCard(Player_Answer=input("Enter a number: "))
            Repeat = input("Want to play again? [y/n]").lower()
            while Repeat != "y" and Repeat != "n":
                print("Invalid Option")
                Repeat = input("Want to play again? [y/n]").lower()
            if Repeat == "n":
                print("Returning to Main Menu")
                Ready = 1
    elif Option == 2:
        while Ready != 1:
            TwoCard(Player_Answer=input("Enter a number: "))
            Repeat = input("Want to play again? [y/n]").lower()
            while Repeat != "y" and Repeat != "n":
                print("Invalid Option")
                Repeat = input("Want to play again? [y/n]").lower()
            if Repeat == "n":
                print("Returning to Main Menu")
                Ready = 1
    elif Option == 3:
        print("Thanks for Playing!")
        break
    else:
        print("Invalid Option")