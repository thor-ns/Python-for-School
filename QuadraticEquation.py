from math import *

#a = input("Enter a: ")
#b = input("Enter b: ")
#c = input("Enter c: ")

def positive_quadratic_equation(a, b, c):
    if c > 0:
        print(str(a) + "x^2 + " + str(b) + "x +" + str(c))
    else:
        print(str(a) + "x^2 + " +  str(b) + "x " + str(c))

    if a == 0:
        print("Error, number must not be equal to 0")
        exit()
    
    root1 = (-b + sqrt(((b**2) - (4*a*c)))) / (2*a)
    print("the first root is " + str(root1))
    
def negative_quadratic_equation(a, b, c):

    if a == 0:
        print("Error, number must not be equal to 0")
        exit()
    root2 = (-b - sqrt(((b**2) - (4*a*c)))) / (2*a)
    print("The second root is " + str(root2))

positive_quadratic_equation()
positive_quadratic_equation()
positive_quadratic_equation()

#positive_quadratic_equation(int(a), int(b), int(c))
#negative_quadratic_equation(int(a), int(b), int(c))