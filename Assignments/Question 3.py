#Question 3
#__________________________________________________________________________________________________________
def SnapCrackle(num):
    if num % 3 == 0  and num % 5 == 0:
        print("number inputted:", num)
        return "SnapCrackle"
    elif num % 3 == 0:
        print("number inputted:", num)
        return "Crackle"
    elif num % 5 == 0:
        print("number inputted:", num)
        return "Snap"
    else:
        print("number inputted:", num)
        return num

c = SnapCrackle(9)
print(c)