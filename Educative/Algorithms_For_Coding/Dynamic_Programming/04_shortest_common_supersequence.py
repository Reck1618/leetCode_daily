"""
Given two strings, write a function to find the length of their shortest common superstring. A superstring is a string which has both input strings as substrings.
"""

# Bottom-up approach with dp
def shortest_common_supersequence(s1, s2):
    """
    Finds the shortest common super sequence length
    :param s1: First string
    :param s2: Second string
    :return: Length of shortest common superstring
    """

    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return len(s1) + len(s2) - (dp[len(s1)][len(s2)])


# Bottom-up approach with dp, different approach
def shortest_common_supersequence_length(s1, s2):
    """
    Finds a shortest common supersequence length
    :param s1: First string
    :param s2: Second string
    :return: Length of shortest common supersequence
    """
    if not s1 or not s2:
        return 0

    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    return dp[len(s1)][len(s2)]
