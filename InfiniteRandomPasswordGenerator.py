import random
passwordList = []
x = 0
while x < 5:
    randomNumber = random.randint(0, 9)
    alphaNum = random.randint(0, 25)
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    randomLetter = alphabet[alphaNum]
    passwordList.append(randomNumber)
    passwordList.append(randomLetter)
    print(passwordList)