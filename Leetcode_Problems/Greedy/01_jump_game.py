"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

# Solution 1
class Solution:
    def canJump(self, nums):
        nums_len = len(nums) - 1
        total = nums[0]
        i = 0

        while total >= i and total < nums_len:
            total = max(total, nums[i] + i)
            i += 1

        return total >= nums_len


# Solution 2
class Solution:
    def canJump(self, nums):
        nums_len = len(nums)
        total = nums[0]
        i = 0

        if nums_len <= 1:
            return True

        while total > 0 and i < nums_len:
            total = max(total - 1, nums[i])
            i += 1

        return i >= nums_len
