#Used as the "main page" to select which function you want
def second_greeting():
    operation = input("Which function of the calculator do you want to use?: ")
    if operation == "addition":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")
        addition(x, y)
    elif operation == "subtraction":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")
        subtraction(x, y)
    elif operation == "multiplication":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")
        multiply(x, y)
    elif operation == "division":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")
        division(x, y)
    elif operation == "MOD":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")  
        MOD(x, y)
    elif operation == "power":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")
        power(x, y)
    elif operation == "square root":
        x = input("Enter your first number: ")
        squareRoot(x)
    elif operation == "factorial":
        x = input("Which number do you want to find the factorial of: ")
        factorial(x)   
    elif operation == "GCF":
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        GCF(x, y)
    elif operation == "exit":
        print("Are you sure you want to quit the \"Calculator\"")
        leaving = input("Type Y to quit and N go back: ")
        if leaving == "Y":
            exit()
        elif leaving == "N":
            second_greeting()
        else:
            print("Please enter Y or N")
    elif operation == "help":
        help()
    else:
        print("Error, not a function of the calculator")
        second_greeting()

def help():
    question = input("Which function do you need help with? ")
    if question == "addition":
        print("adds the second number to the first number Ex) first + second")
        print("""Restrictions: first number must be an integer
                               second number must be an integer""")
    elif question == "subtraction":
        print("subtracts the second number from the first number Ex) first - second)")
        print("""Restrictions: first number must be an integer
                               second number must be an integer""")
    elif question == "multiplication":
        print("multiplies first number by the second number Ex) first x second")
        print("""Restrictions: first number must be an integer
                               second number must be an integer""")
    elif question == "division":
        print("divides the first number by the second number Ex) first ÷ second")
        print("""Restrictions: first number must be an integer
                               second number must be an integer
                               second number cannot be 0""")
    elif question == "MOD":
        print("divides the first number by the second number (first ÷ second) but the remainder aka what is left, will be displayed")
        print("""Restrictions: first number must be an integer
                               second number must be an integer
                               second number cannot be 0""")
    elif question == "power":
        print("puts the first number to the power of the second number (first ^ second)")
        print("""Restrictions: first number must be an integer
                               second number must be a whole number""")
    elif question == "square root":
        print("finds the square root of the first number")
        print("""Restrictions: first number must be an integer""")
    elif question == "factorial":
        print("finds the factorial the number given ex. 20x19x18...3x2x1")
        print("""Restrictions: number must be a POSITIVE whole number""")
    elif question == "GCF":
        print("finds the (GCF) greatest common factor between the 2 given numbers")
    else:
        print("Error, not a function of the calculator")
    
#start of all the mathematical functions
def addition(x, y):
    try:
        x = float(x)
        y = float(y)
        add = x + y
        print(f"{x} + {y} is equal to {add}")
    except:
        print("Error, please enter a numeric value")
    second_greeting()
    #addition function

def subtraction(x, y):
    try:
        x = float(x)
        y = float(y)
        sub = x - y
        print(f"{x} - {y} is equal to {sub}")
    except:
        print("Error, please enter a numeric value")
    second_greeting()
    #subtraction function


def multiply(x, y):
    try:
        x = float(x)
        y = float(y)
        mul = x * y
        print(f"{x} * {y} is equal to {mul}")
    except:
        print("Error, please enter a numeric value")
    second_greeting()
    #multiplication function

def division(x, y):
    try:
        x = float(x)
        y = float(y)
        div = x / y
        print(f"{x} / {y} is equal to {div}")
    except ZeroDivisionError:
        print("Error, y cannot be zero")
    except:
        print("Error, please enter a numeric value")
    second_greeting()
    #division function

def MOD(x, y):
    try:
        x = float(x)
        y = float(y)
        mod = x % y
        print(f"the MOD of {x} / {y} is {mod}")
    except ZeroDivisionError:
        print("Error, y cannot be zero")
    except:
        print("Error, please enter a numeric value")
    second_greeting()
    #remainder function

def power(x, y):
    try:
        x = float(x)
        y = y.split("/")
        p = float(y[0])
        q = float(y[1])
        pow = x ** (p/q)
        print(f"{x} to the power of {p} / {q} is equal to {pow}")
    except:
        print("Error, please enter a numeric value")
    second_greeting()
    #power function

def squareRoot(x):
    try:
        x = float(x)
        root = x ** (1 / 2)
        if type(root) == type(1j):
            print("The answer is a complex number")
        else:
            print(f"The square root of {x} is equal to {root}")
    except TypeError:
        print("Error, must be a numeric value")
    second_greeting()
    #square root function

def factorial(x):
    try:
        x = int(x)
        if x < 0:
            print("Error, must be 0 or a higher integer")
            second_greeting()
        elif x == 0:
            print(f"The factorial of 0 is 1")
            second_greeting()
        else:
            lim = 1
            output = x
            while lim < x:
                output = output * lim 
                lim += 1
            print(f"The factorial of {x} is {output}") 
    except TypeError:
        print("Error, must be a numeric value")
    second_greeting()  
    #factorial function

def GCF(x, y):
    try:
        x = int(x)
        y = int(y)
        if x == 0 and y == 0:
            print("Both numbers cannot be 0")
        elif x == 0:
            print(f"The GCF of {x} and {y} is {y}")
        elif y == 0:
            print(f"The GCF of {x} and {y} is {x}")
        elif x == -abs(x):
            print("Please enter positive values")
        else:
            place = x
            while place > 0:
                if x % place == 0 and y % place == 0:
                    commonFactor = place
                    print(f"the common factor of {x} and {y} is {commonFactor}")
                    break
                place -= 1
    except:
        print("Error, please enter a numeric value")
    second_greeting()
    #greatest common factor function
#end of all mathematical functions 

print("""Welcome to the calculator, the functions available are: addition, subtraction, division, multiplication, MOD, power, square root, 
factorial""")
print("If you need help with any of the functions type \"help\"")
second_greeting()