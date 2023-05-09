"""
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        for i in range(len(matrix)):
            c = len(matrix[i])-1
            if target <= matrix[i][c]:
                l,r = 0, c
                while l <= r:
                    mid = (l+r)//2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
        return False

        # Binary Search Solution
        # L,R = 0, len(matrix)-1
        # while L <= R:
        #     m_mid = (L+R)//2
        #     if matrix[m_mid][0] > target:
        #         R = m_mid - 1
        #     elif matrix[m_mid][-1] < target:
        #         L = m_mid + 1
        #     else:
        #         break

        # if not L <= R:
        #     return False
                
        # l,r = 0, len(matrix[m_mid]) - 1
        # array = matrix[m_mid]
        # while l <= r:
        #     arr_mid = (l+r)//2
        #     if array[arr_mid] == target:
        #         return True
        #     elif array[arr_mid] > target:
        #         r = arr_mid - 1
        #     else:
        #         l = arr_mid + 1

        # return False
