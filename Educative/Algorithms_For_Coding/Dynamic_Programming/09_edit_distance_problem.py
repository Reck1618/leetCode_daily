"""
Given two strings, write code to calculate how many minimum Levenshtein distance operations are needed to convert one into the other.

Note - The Levenshtein distance operations are : removal, insertion, or substitution of a character in the string
"""

def min_edit_dist(str1, str2):
    """
    Calculates minimum Levenshtein distance operations
    :param str1: String 1
    :param str2: String 2
    :return: minimum Levenshtein distance operations
    """

    # Write your code here!
    dp = [[float("inf") for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    for i in range(len(str1) + 1):
        dp[i][0] = i

    for j in range(len(str2) + 1):
        dp[0][j] = j

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

    return dp[len(str1)][len(str2)]



if __name__ == '__main__':

    str1 = "sunday"
    str2 = "saturday"

    print(min_edit_dist(str1, str2))