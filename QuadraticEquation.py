from math import *
def positive_quadratic_equation(a, b, c):
    if c > 0:
        print(str(a) + "x**2 + " + str(b) + "x +" + str(c))
    else:
        print(str(a) + "x**2 + " +  str(b) + "x " + str(c))

    """if a == 0:
        print("Error, number must not be equal to 0")"""
    return(-b + sqrt(((b**2) - (4*a*c))) / (2*a))
    
print(positive_quadratic_equation(3, 5, -7))