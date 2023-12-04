#1: input a number, then it gets rounded to 2 decimal places (hundredths)
kk = float(input("Enter any number: "))
num = round(kk, 2)
print(str(kk) + " rounded to 2 decimal places is " + str(num))
#2: input a number, gives the absolute value of the number
from math import *
a = input("Enter any number: ")
absolute = abs(float(a))
print("The absolute value of " + a + " is " + str(absolute))
#3: input 2 numbers, says wether or not the difference is an integer
x = input("First number: ")
y = input("Second number: ")
z = float(x) - float(y)
print("Is " + x + " - " + y + " an integer? " + str(z.is_integer()))