import random
import time

list = []
while(len(list) <= 1000) : list.append(random.randint(1, 1000))

def quickSort(sequence) :
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

t0 = time.time()
list = quickSort(list)
t1 = time.time()
print(list)
print(t1 - t0)