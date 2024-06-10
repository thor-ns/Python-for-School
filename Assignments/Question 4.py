#Question 4
#______________________________________________________________________________________________________________
def Recursion_Power(b, p):
    if p == 0:
        return 1
    
    return b * Recursion_Power(b, p - 1)

d = Recursion_Power(2, 3)
print(d)