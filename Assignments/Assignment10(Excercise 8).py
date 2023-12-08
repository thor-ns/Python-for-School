number = input("Enter an integer to check if it's prime: ")

def prime_number(number):
    x = 1
    primeNumber = False
    if int(number) == 1 or int(number) == 2:
         primeNumber = True
         print(f"is {number} a prime number? {primeNumber}")
         exit()
    #1 and 2 are prime but won't work with the patter below
    factor = [] 
    while x <= int(number):             
        if int(number) % x == 0:
            factor.append(int(number) / x)
            #a print statement could be added here to debug or just to list the factors before saying if it's prime or not
        x += 2
    if len(factor) > 3:
        primeNumber = False
        print(f"Is {number} a prime number? {primeNumber}")
    elif len(factor) == 2:
        primeNumber = True
        print(f"Is {number} a prime number? {primeNumber}")
    else:
        print("Error")
        exit


prime_number(number)
