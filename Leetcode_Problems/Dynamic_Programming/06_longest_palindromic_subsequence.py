"""
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1, s2 = s, s[::-1]

        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s2) + 1)]

        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                if s2[i - 1] == s1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(s)][len(s)]