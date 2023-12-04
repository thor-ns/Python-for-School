def palindrome_reader(word):
    length = len(word)
    if(word[0] == word[-1]):
        return(True)
    elif(word[1] == word[-2]):
        return(True)
    elif(len(word)):
        return(True)

def palindrome_reader_V2(word):
    for i in word:
        print(i)

palindrome_reader_V2("tacocat")








Fruits = ["Banana", "Cherry", "Blueberry", "Apple"]
Veggies = ["Vegemite", "Carrot", "Beet", "Thyme"]
Adjectives = ["Sweet", "Juicy", "Amazing", "Big"]

for x in Fruits:
    for y in Veggies:
        for z in Adjectives:
            print(x, y, z)