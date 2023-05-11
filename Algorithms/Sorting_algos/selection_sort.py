"""
Implement Selection Sort.
-> Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.

Time - O(n^2)
Space - O(1)
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                min = j
        
        arr[min], arr[i] = arr[i], arr[min]
    return arr


arr = [2,4,1,64,26,21,3,6,77,8,19]
print(selection_sort(arr))