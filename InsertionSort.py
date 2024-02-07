import random
import time

list = []
while(len(list) <= 1000) : list.append(random.randint(1, 1000))

def insertion_sort(list_a):
    length = range(1, len(list_a))#finds 
    for i in length:
        value_to_sort = list_a[i]
        while list_a[i-1] > value_to_sort and i>0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i-1
    return list_a

t0 = time.time()
list = insertion_sort(list)
t1 = time.time()
print(list)
print(t1 - t0)