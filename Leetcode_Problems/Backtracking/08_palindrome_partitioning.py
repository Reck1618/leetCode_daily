"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""

class Solution:
    def partition(self, s):
        result = []

        def backtrack(start=0, cur_set=[]):
            if start >= len(s):
                result.append(cur_set[:])
                return

            for i in range(start, len(s)):
                # If the substring is a palindrome, add it to the current set and backtrack
                if s[start:i+1] == s[start:i+1][::-1]:
                    cur_set.append(s[start:i+1])
                    backtrack(i+1, cur_set)
                    cur_set.pop()

        backtrack()
        return result