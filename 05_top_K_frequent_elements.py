"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = collections.Counter(nums)
        freq = [[] for i in range(len(nums)+1)]

        for i,v in temp.items():
            freq[v].append(i)
   
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res