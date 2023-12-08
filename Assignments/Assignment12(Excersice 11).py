import random
passwordList = []
#empty list so that the random character/number can be appended to the list
lenOfPass = input("How long do you want your password to be: ")
lenOfPass = int(lenOfPass)
if -abs(lenOfPass) == lenOfPass:
    print("Error, please enter a positive natural number")
    exit()
#if the user input is a negative number an error message is printed and the program is stopped

x = 0
while x < lenOfPass:
#This loop randomizes every aspect of the password everytime it runs
    randomNumber = random.randint(0, 9)
    #generates the random number for the password
    alphaNum = random.randint(0, 25)
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    randomLetter = alphabet[alphaNum]
    #generates a random lowercase letter for the password
    alphaUppercaseNum = random.randint(0, 25)
    alphabetUppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    randomUppercaseLetter = alphabet[alphaUppercaseNum]
    #generates a random uppercase letter for the password
    randomBool = random.randint(0, 2)
    if randomBool == 1:
        passwordList.append(randomNumber)
    elif randomBool == 0:
        passwordList.append(randomLetter)
    elif randomBool == 2:
        passwordList.append(randomUppercaseLetter.upper())
    #randomly decides if a character should be a lowercase letter, uppercase letter, or number
    x += 1

def list_to_string(list):
    i = 0
    password = ""
    while i < len(list):
        password = password + str(list[i])
        i += 1
    print(f"Your randomly generated password is: {password}")
#This function coverts the password stored in a list into a *single line* string that then gets printed to the console

list_to_string(passwordList)
