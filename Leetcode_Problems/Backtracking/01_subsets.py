"""
Given an integer array nums of unique elements, return all possible
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Time Complexity: O(N * 2^N)
Space Complexity: O(N * 2^N)
"""

class Solution:
    def subsets(self, nums):
        result = []
        def backtrack(start=0, cur_set=[]):
            if len(cur_set) == length:
                result.append(cur_set[:])
                return
            for i in range(start, len(nums)):
                cur_set.append(nums[i])
                backtrack(i+1, cur_set)
                cur_set.pop()

        for length in range(len(nums) + 1):
            backtrack()

        return result


# Another solution
class Solutions:
    def subsets(self, nums):
        result = []

        def backtrack(start=0, cur_set=[]):
            result.append(cur_set[:])

            for i in range(start, len(nums)):
                cur_set.append(nums[i])
                backtrack(i+1, cur_set)
                cur_set.pop()

        backtrack()
        return result