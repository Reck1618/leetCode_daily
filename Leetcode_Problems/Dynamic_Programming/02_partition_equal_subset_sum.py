"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

# Recursive top-down approach
class Solution:
    def canPartition(self, nums):
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        memo = {}

        def solve(target, ind):
            if (target, ind) in memo:
                return memo[(target, ind)]

            if target == 0:
                return True

            if target < 0 or ind >= len(nums):
                return False

            memo[(target, ind)] = solve(target - nums[ind], ind + 1) or solve(target, ind + 1)
            return memo[(target, ind)]

        return solve(target, 0)


# NeetCode Solution
class Solution:
    def canPartition(self, nums):
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            newDP = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                newDP.add(t + nums[i])
                newDP.add(t)
                dp = newDP

        return False


# Space optimized bottom-up approach
class Solution:
    def canPartition(self, nums):
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for j in range(target + 1):
            if nums[0] == j:
                dp[j] = True

        for i in range(1, len(nums)):
            for j in range(target, -1, -1):
                if not dp[j] and j >= nums[i]:
                    dp[j] = dp[j - nums[i]]

        return dp[target]


# another bottom-up approach
class Solution:
    def canPartition(self, nums):
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True

        for j in range(target + 1):
            if nums[0] == j:
                dp[0][j] = True

        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                elif j >= nums[i]:
                    dp[i][j] = dp[i - 1][j - nums[i]]

        return dp[len(nums) - 1][target]
