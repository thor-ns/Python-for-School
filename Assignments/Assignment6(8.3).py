word = input("Enter a word: ")

def length_of_word(word):
    if len(word) > 5:
        print(f"Your word {word} is greater than 5 characters")
    elif len(word) < 5:
        print(f"Your word {word} is less than 5 characters")
    else:
        print(f"Your word {word} is equal to 5 characters")
    
length_of_word(word)