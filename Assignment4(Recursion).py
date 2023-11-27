#recursion is basically taking the problem/concept and using a simpler or previous version of itself to solve the harder version
#The formula for the fibonaci sequence is Fn = Fn-1 + Fn-2, where n > 1. This sequence is observed in tons of natural objects like the branching patterns in trees and leaves
#The golden ratio is a ratio between the 2 nummbers that add up to 1.618

"""a = 0
b = 1  

n = 10"""
#this variable is the stopping condition for the sequence, otherwise it would go on forever
#whenever the sequence equals this number, it stops

"""while b < n:

    print(b)

    a, b = b, a+b"""

def rec(n):
    if n <= 1:
        return(n)
    else:
        return(rec(n-1) + rec(n-2))
    
numOfTerms = 1000000000000000000000
if numOfTerms <= 0:
    print("Enter a positive number")
else:
    print("The Fibonacci sequence up to that term is: ")
    for i in range(numOfTerms):
        print(rec(i))