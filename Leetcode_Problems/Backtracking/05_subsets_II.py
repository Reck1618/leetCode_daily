"""
Given an integer array nums that may contain duplicates, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsetsWithDup(self, nums):
        result = []
        nums.sort()

        def backtrack(start=0, cur_set=[]):
            if cur_set not in result:
                result.append(cur_set[:])

            for i in range(start, len(nums)):
                cur_set.append(nums[i])
                backtrack(i+1, cur_set)
                cur_set.pop()

        backtrack()
        return result


class Solution:
    def subsetsWithDup(self, nums):
        result = []
        nums.sort()

        def backtrack(start=0, cur_set=[]):
            result.append(cur_set[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                cur_set.append(nums[i])
                backtrack(i+1, cur_set)
                cur_set.pop()