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
    
base = int(input("What is the base: "))
height = int(input("What is the height: "))
t1 = Square(base, height)
print(t1.calcArea())

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