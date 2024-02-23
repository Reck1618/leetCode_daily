"""
Given a string, find the length of its longest palindromic subsequence. In a palindromic subsequence, elements read the same, backward and forward.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""

# Backtracking solution - O(2^n) time | O(n) space
def longest_palindromic_subsequence_backtracking(s):
    """
    Finds the longest palindromic subsequence length
    :param s: Input string
    :return: Length of shortest common superstring
    """
    res = 0

    def backtrack(start=0, cur_set=[]):
        nonlocal res
        if cur_set == cur_set[::-1]:
            res = max(res, len(cur_set))

        for i in range(start, len(s)):
            cur_set.append(s[i])
            backtrack(i + 1, cur_set)
            cur_set.pop()

    backtrack()
    return res


# Dynamic programming solution - O(n^2) time | O(n^2) space

def longest_palindromic_subsequence(s):
    """
    Finds the longest palindromic subsequence length
    :param s: Input string
    :return: Length of shortest common superstring
    """
    s1, s2 = s, s[::-1]

    dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s1) + 1)]

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s2[i - 1] == s1[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(s)][len(s)]