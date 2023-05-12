"""
Implement linear search.
"""

def linear_search(array, target):
    length = len(array)
    for i in range(length):
        if array[i] == target:
            return True
    return False

arr = [1,3,4,5,6,7,8,9]
target = 9
print(linear_search(arr, target))