from math import *

a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")


def positive_quadratic_equation(a, b, c):
#positive root of the quadratic equation in a function

    if c > 0:
        print(str(a) + "x^2 + " + str(b) + "x + " + str(c))
    else:
        print(str(a) + "x^2 + " +  str(b) + "x " + str(c))
    #prints the standard equation. 2 variants for a positive and negative constant

    if a == 0:
        print("Error, \"a\" must not be equal to 0")
        exit()
    #checks if a is equal to 0. If true then it stops the program
    
    root1 = (-b + sqrt(((b**2) - (4*a*c)))) / (2*a)
    print("the first root is " + str(root1))
    

def negative_quadratic_equation(a, b, c):
#negative root of the quadratic equation in a function

    if a == 0:
        print("Error, \"a\" must not be equal to 0")
        exit()
    #another a = 0 checker

    root2 = (-b - sqrt(((b**2) - (4*a*c)))) / (2*a)
    print("The second root is " + str(root2))


def combined_quadratics(positive, negative):
    return(positive, negative)

combined_quadratics(positive_quadratic_equation(int(a), int(b), int(c)), negative_quadratic_equation(int(a), int(b), int(c)))