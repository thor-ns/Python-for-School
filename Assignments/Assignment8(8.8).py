import random
numberOfHeads = 0
numberOfTails = 0
tailsAfterHead = 0

x = 0
while x < 100000:
    x = x + 1
    randomNumber = random.randint(0, 1)
    if randomNumber == 0:
        numberOfHeads = numberOfHeads + 1
    elif randomNumber == 1:
        numberOfTails = numberOfTails + 1
    if numberOfHeads == 1:
        tailsAfterHead = tailsAfterHead + 1
    

averageOfHeads = numberOfHeads / x
averageOfTails = numberOfTails / x
print(f"The average of heads is {averageOfHeads} over {x} trials")
print(f"The average of tails is {averageOfTails} over {x} trials")
print(f"The number of tails after the first head is {tailsAfterHead}")