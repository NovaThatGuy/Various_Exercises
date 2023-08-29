Letters = {}
Answer = input("What would you like to say: ")
for characters in Answer:
    characters = characters.lower()
    if characters != ' ':
        if characters in Letters:
            Letters[characters] += 1
        else:
            Letters[characters] = 1
for characters, freq in Letters.items():
    print(f"{characters}: {freq}")