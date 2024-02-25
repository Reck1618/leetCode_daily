"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

# Neetcode solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for i in range(len(s)):
            #for odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

            #for even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        return res


# Sliding window solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = []
        for i in reversed(range(len(s))):
            left = 0
            right = i
            while right < len(s):
                if s[left:right+1] == s[left:right+1][::-1]:
                    return s[left:right+1]
                else:
                    left += 1
                    right += 1


# Optimial Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def LP(l, r):
            while l >= 0 and r < n:
                if s[l] != s[r]: break
                l -= 1
                r += 1
            return l + 1 , r # l + 1 because we want the last matching alpha

        start, end = 0, 0
        for i in range(n):
            l, r = LP(i,i)
            if end - start < r - l:
                start  = l
                end = r

            l, r = LP(i, i + 1)
            if end - start < r - l:
                start = l
                end = r

        return s[start:end]

