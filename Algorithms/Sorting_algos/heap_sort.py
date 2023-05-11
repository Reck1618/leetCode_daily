"""
Implement Heap Sort.
-> Heap Sort is a comparison-based sorting algorithm that uses the concept of a heap data structure to sort elements in an array.
    - The array is first converted into a binary heap, a special type of binary tree where the value of each node is greater than or equal to its child nodes
    - The largest element (the root node) is removed and placed at the end of the array. The heap is then reconstructed with the remaining elements, 
      And the next largest element is removed and placed at the second-last position of the array. This process is repeated until all elements are sorted

Time - O(n^2)
Space - O(log n)    
"""

def heapify(arr, len_arr, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < len_arr and arr[left] > arr[largest]:
        largest = left
    
    if right < len_arr and arr[right] > arr[largest]:
        largest = right
    
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, len_arr, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

arr = [2,4,1,64,26,21,3,6,77,8,19]
print(heap_sort(arr))
