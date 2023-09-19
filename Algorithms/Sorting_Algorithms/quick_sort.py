"""
Implement Quick Sort.
-> Quicksort is a sorting algorithm based on the divide and conquer approach where
    - An array is divided into subarrays by selecting a pivot element (element selected from the array).
    - While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.
    - The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.
    - At this point, elements are already sorted. Finally, elements are combined to form a sorted array.

Time - O(n^2)
Space - O(log n)    
"""
# simple version
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    left, right, equal = [], [], []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)
    
    return quick_sort(left) + equal + quick_sort(right)

arr = [2,4,1,64,26,21,3,6,77,8,19]
print(quick_sort(arr))


# efficient version (less space complexity)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
    

def eff_quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        eff_quick_sort(arr, low, pivot - 1)
        eff_quick_sort(arr, pivot + 1, high)
    return arr

arr = [2,4,1,64,26,21,3,6,77,8,19]
print(eff_quick_sort(arr, 0, len(arr) - 1))
