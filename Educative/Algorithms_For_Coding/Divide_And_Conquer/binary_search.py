"""
Implement binary search in a sorted array of integers.
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2 #Avoiding Integer Overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Time complexity: O(log n)
# Space complexity: O(1)

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    print(binary_search(nums, target))  # 4