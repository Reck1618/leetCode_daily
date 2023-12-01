"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""

class Solution:
    def permute(self, nums):
        result = []

        def backtrack(cur_set=[]):
            if len(cur_set) == len(nums):
                result.append(cur_set[:])
                return

            for num in nums:
                if num not in cur_set:
                    cur_set.append(num)
                    backtrack(cur_set)
                    cur_set.pop()

        backtrack()
        return result