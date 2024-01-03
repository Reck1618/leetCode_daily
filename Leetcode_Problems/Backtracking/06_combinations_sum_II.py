"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]
"""

class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()

        def backtrack(start=0, cur_set=[]):
            if sum(cur_set) == target:
                result.append(cur_set[:])

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if sum(cur_set) + candidates[i] > target:
                    break

                cur_set.append(candidates[i])
                backtrack(i+1, cur_set)
                cur_set.pop()

        backtrack()
        return result