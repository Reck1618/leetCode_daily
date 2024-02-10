"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for  i in range(len(nums)-2):
            # To Avoide duplication
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            temp = self.findSum(nums[i + 1:], nums[i])
            if temp:
                ans += temp
        return ans

    def findSum(self, nums, cur):
        l, r = 0, len(nums) - 1
        temp = []

        while l < r:
            total = cur + nums[l] + nums[r]

            if total == 0:
                temp.append([cur, nums[l], nums[r]])
                l += 1
                r -= 1

                # To Avoide Duplication
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1

            elif total > 0:
                r -= 1
            else:
                l += 1

        return temp
