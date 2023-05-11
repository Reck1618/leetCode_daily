"""
Implement Merge Sort.
-> Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.

Time - O(n log n)
Space - O(n)
"""

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    centre = len(arr) // 2
    left = arr[:centre]
    right = arr[centre:]

    return merge(merge_sort(left),merge_sort(right))

def merge(left, right):
    l = r = 0
    ans = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            ans.append(left[l])
            l += 1
        else:
            ans.append(right[r])
            r += 1
    return ans + left[l:] + right[r:]

arr = [2,4,1,64,26,21,3,6,77,8,19]
print(merge_sort(arr))