sA = input("Enter side A: ")
sB = input("Enter side B: ")
sC = input("Enter side C: ")
int(sA)
int(sB)
int(sC)

def tri(a, b, c):
    isTriangle = True
    if int(a) <= (int(b) + int(c)) and int(b) <= (int(a) + int(c)) and int(c) <= (int(a) + int(b)):
        isTriangle = True
        print(f"{isTriangle}, these sides make a triangle")
    else:
        isTriangle = False
        print(f"{isTriangle}, these sides do not make a triangle")

tri(sA, sB, sC)