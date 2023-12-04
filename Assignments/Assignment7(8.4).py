number = input("Enter a positive integer: ")
if abs(int(number)) == -abs(int(number)):
    exit()
    

def factor_of_positive_integer(number):
    x = 1
    while x <= int(number):
        if int(number) % x == 0:
            factor = int(number) / x
            print(f"{int(factor)} is a factor of {number}")
        x = x + 1

factor_of_positive_integer(number)