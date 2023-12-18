#start of accessory functions
def second_greeting(): #Used as the "main page" to select which function you want. Hosts the logic for which operation the user wants to use and then calls the respective function
    operation = input("Enter the corresponding number for the function you want to use: ")
    if operation == "1":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")
        addition(x, y)
    elif operation == "2":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")
        subtraction(x, y)
    elif operation == "3":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")
        multiply(x, y)
    elif operation == "4":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")
        division(x, y)
    elif operation == "5":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")  
        MOD(x, y)
    elif operation == "6":
        x = input("Enter your first number: ")
        y = input("Enter your second number: ")
        power(x, y)
    elif operation == "7":
        x = input("Enter your first number: ")
        squareRoot(x)
    elif operation == "8":
        x = input("Which number do you want to find the factorial of: ")
        factorial(x)   
    elif operation == "9":
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        GCF(x, y)
    elif operation == "10":
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        LCM(x, y)
    elif operation == "exit":
        Exit()
    else:
        print("Not a valid function of the calculator!")
        second_greeting()

def Exit():
    print("Are you sure you want to quit the \"Calculator\"")
    leaving = input("Type Y to quit and N go back: ")
    if leaving == "Y":
        exit()
    elif leaving == "y":
        exit()
    elif leaving == "N":
        second_greeting()
    elif leaving == "n":
        second_greeting()
    else:
        print("Please enter Y or N")
        Exit()
#I made exiting a function so that I could call itself again. Exit() is my function name, not to be confused with the other exit() function

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
        print("""Restrictions: both numbers must be POSITIVE whole number""")
    elif question == "GCF":
        print("finds the (GCF) greatest common factor between the 2 given numbers")
        print("""Restrictions: both numbers must be POSITIVE whole numbers that are greater than 0""")
    elif question == "LCM":
        print("finds the (LCM) lowest common multiple between the 2 given numbers")
    else:
        print("Error, not a function of the calculator")
#ends of accessory functions

#start of all the mathematical functions
def addition(x, y):
    try:
        x = float(x)
        y = float(y)
        add = x + y
        print(f"{x} + {y} is equal to {add}")
    except TypeError:
        print("Error, please enter a numeric value")
    except ValueError:
        print("Error, not a number")
    except:
        print("Error")
    finally:
        second_greeting()
    #addition function

def subtraction(x, y):
    try:
        x = float(x)
        y = float(y)
        sub = x - y
        print(f"{x} - {y} is equal to {sub}")
    except TypeError:
        print("Error, please enter a numeric value")
    except ValueError:
        print("Error, not a number")
    except:
        print("Error")
    finally:
        second_greeting()
    #subtraction function


def multiply(x, y):
    try:
        x = float(x)
        y = float(y)
        mul = x * y
        print(f"{x} * {y} is equal to {mul}")
    except TypeError:
        print("Error, please enter a numeric value")
    except ValueError:
        print("Error, not a number")
    except:
        print("Error")
    finally:
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
    except TypeError:
        print("Error, please enter a numeric value")
    except ValueError:
        print("Error, not a number")
    except:
        print("Error")
    finally:
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
    except TypeError:
        print("Error, please enter a numeric value")
    except ValueError:
        print("Error, not a number")
    except:
        print("Error")
    finally:
        second_greeting()
    #remainder function

def power(x, y):
    try:
        x = float(x)
        if y.find("/"):
            y = y.split("/")
            p = float(y[0])
            q = float(y[1])
            pow = (x) ** (p/q)
            print(f"{x} to the power of {p} / {q} is equal to {pow}")
        else:
            y = float(y)
            pow = (x) ** y
            print(f"{x} to the power of {y} is equal to {pow}")
    except TypeError:
        print("Error, please enter a numeric value")
    except ValueError:
        print("Error, not a number")
    except:
        print("Error")
    finally:
        second_greeting()
    #power function. If y is a fraction it puts it into fractional form otherwise just floats y and powers y to x

def squareRoot(x):
    try:
        x = float(x)
        root = x ** (1 / 2)
        if type(root) == type(1j):
            print("The number you want to square root cannot be negative!")
        else:
            print(f"The square root of {x} is equal to {root}")
    except TypeError:
        print("Error, must be a numeric value")
    except ValueError:
        print("Error, not a number")
    except:
        print("Error")
    finally:
        second_greeting()
    #square root function. Takes the square root of the user input

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
    except ValueError:
        print("Error, not a number")
    except:
        print("Error")
    finally:
        second_greeting()  
    #factorial function. Uses a while loop to continue multiplying until it reaches x, the number the user inputed

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
    except TypeError:
        print("Error, please enter a numeric value")
    except ValueError:
        print("Error, not a number")
    except:
        print("Error")
    finally:
        second_greeting()
    #greatest common factor function. 


def LCM(x, y):
    try:
        x = int(x)
        y = int(y)
        if x == 0:
            print("Error, cannot be 0")
        elif y == 0:
            print("Error, cannot be 0")
        elif x == y:
            print(f"The LCM of {x} and {y} is {x}")
        elif x == -abs(x):
            print("Please enter positive integers")
        elif y == -abs(y):
            print("Please enter positive integers")
        else:
            place = x
            while place > 0:
                if x % place == 0 and y % place == 0:
                    commonFactor = place
                    break
                place -= 1
            lcm = ((x*y)/commonFactor)
            print(commonFactor)
            print(f"The LCM of {x} and {y} is {lcm}") 
    except TypeError:
        print("Error, must enter a numeric value")
    except ValueError:
        print("Error, not a number")
    except:
        print("Error")
    finally:
        second_greeting()
#Lowest common multiple function. Uses this formula: lcm = (x*y)/gcf
#end of all mathematical functions 

def main(): #This main function is simply here in case I would need to call it somewhere
    print("""Welcome to Dom's calculator, the functions available are: 
        1: Addition
        2: Subtraction
        3: Division
        4: Multiplication
        5: MOD
        6: Power
        7: Square Root
        8: Factorial
        9: GCF
        10: LCM""")
    print("If you need help with any of the functions type \"help\"")
    print("Type \"exit\" if you want to quit the application")
    second_greeting()
main()