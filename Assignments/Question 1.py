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