"""
Implement Binary Search.
-> Binary Search is a searching algorithm for finding an element's position in a sorted array. In this approach, the element is always searched in the middle of a portion of an array.
    - Binary search can be implemented only on a sorted list of items. If the elements are not sorted already, we need to sort them first

Time - O(log n)
Space - O(1)
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False


arr = [1,2,3,4,5,6,7,8,9,10]
target = 6
print(binary_search(arr, target))