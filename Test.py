def add_numbers(num1, num2):
    print(num1 + num2)

def subtract_numbers(num1, num2):
    print(num1 - num2)

def power(num1, num2):
    print(num1 ** num2)

def multiply_numbers(num1, num2):
    print(num1 * num2)

def square_root(num1):
    print(num1 ** 1 / 2)

input1 = input()

def factorial(input1):
    if(input1 == "1" or input1 == "0"):
        return(1)
    else:
        return(float(input1) ** (float(input1)-1))
    
factorial(input1)
from math import pi

print(pi)