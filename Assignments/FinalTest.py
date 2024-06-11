#   Section B
#Question 1
#_________________________________________________________________________________________________________________
class Shapes():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calcArea(self):
        return (self.base * self.height)

class Rectangle(Shapes):
    def __init__(self, base, height):
        super().__init__(base, height)
    
    def calcArea(self):
        return ("the area of the rectangle is: ", super().calcArea())

class Square(Shapes):
    def __init__(self, base, height):
        super().__init__(base, height)
    
    def calcArea(self):
        return ("the area of the square is: ", super().calcArea())

class Triangle(Shapes):
    def __init__(self, base, height):
        super().__init__(base, height)
    
    def calcArea(self):
        return ("the area of the triangle is: ", (self.base*self.height)/2)

class Trapezoid(Shapes):
    def __init__(self, base, height, base2):
        super().__init__(base, height)
        self.base2 = base2
    
    def calcArea(self):
        return ("the area of the trapezoid is: ", ((self.base + self.base2)/2)*height)
    
base1 = int(input("What is the base: "))
base2 = int(input("What is the second base (trapezoid only): "))
height = int(input("What is the height: "))

t1 = Square(base1, height)
t2 = Trapezoid(base1, height, base2)
t3 = Triangle(base1, height)
t4 = Rectangle(base1, height)
print(t1.calcArea())
print(t2.calcArea())
print(t3.calcArea())
print(t4.calcArea())

#Question 2
#__________________________________________________________________________________________________________
def Division_By_3_Not_5(beg, end):
    numbers = []
    for i in range(beg, end+1):
        if i % 3 == 0:
            if i % 5 == 0:
                continue
            else:
                numbers.append(i)
    return numbers

#b = Division_By_3_Not_5(3000, 4200)
#print(b)

#Question 3
#__________________________________________________________________________________________________________
def SnapCrackle(num):
    if num % 3 == 0  and num % 5 == 0:
        print("number inputted:", num)
        return "SnapCrackle"
    elif num % 3 == 0:
        print("number inputted:", num)
        return "Crackle"
    elif num % 5 == 0:
        print("number inputted:", num)
        return "Snap"
    else:
        print("number inputted:", num)
        return num

#c = SnapCrackle(9)
#print(c)

#Question 4
#______________________________________________________________________________________________________________
def Recursion_Power(b, p):
    if p == 0:
        return 1
    
    return b * Recursion_Power(b, p - 1)

#d = Recursion_Power(2, 3)
#print(d)