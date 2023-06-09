"""
Implement Bubble Sort.
-> Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order.

Time = O(n^2)
Space = O(1)
"""

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        if not swapped:
            break 
    return arr


arr = [2,4,1,64,26,21,3,6,77,8,19]
print(bubble_sort(arr))