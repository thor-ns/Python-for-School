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

b = Division_By_3_Not_5(3000, 4200)
print(b)