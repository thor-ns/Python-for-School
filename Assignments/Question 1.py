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