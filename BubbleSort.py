import random
import time

list_a = []
while(len(list_a) <= 1000) :list_a.append(random.randint(1, 1000))
print(list_a)

def bubble(arr):
    n = len(arr)
    # if the array is already sorted, it doesn't need to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return

t0 = time.time()
bubble(list_a)
t1 = time.time()
print(list_a)
print(t1 - t0)