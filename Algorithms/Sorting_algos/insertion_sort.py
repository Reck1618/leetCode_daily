"""
Implement Insertion Sort.
-> Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration, we take an element (key) and campare it to the previous element.

Time - O(n^2)
Space - O(1)
"""

def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

arr = [2,4,1,64,26,21,3,6,77,8,19]
print(insertion_sort(arr))