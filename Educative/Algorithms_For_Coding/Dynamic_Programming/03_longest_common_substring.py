"""
Given two strings, s1 and s2, write a function that finds and returns the length of the longest substring of s2 in s1 (if any exists).
"""

# Bottom-up approach with dp

def longest_common_substr_length(s1, s2):
    """
    Finds a longest common substring length
    :param s1: First string
    :param s2: Second string
    :return: Length of longest common substring
    """

    if not s1 or not s2:
        return 0

    dp = [[0 for _ in range(len(s1))] for _ in range(len(s2))]

    res = 0

    for i in range(len(s1)):
        if s1[i] == s2[0]:
            dp[0][i] = 1
            res = max(res, dp[0][i])

    for i in range(len(s2)):
        if s2[i] == s1[0]:
            dp[i][0] = 1
            res = max(res, dp[0][i])

    for i in range(1, len(s2)):
        for j in range(1, len(s1)):
            if s2[i] == s1[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])

    return res


# One dp solution
def longest_common_substr_length_one_dp(s1, s2):
    """
    Finds a longest common substring length
    :param s1: First string
    :param s2: Second string
    :return: Length of longest common substring
    """

    if not s1 or not s2:
        return 0

    dp = [0 for _ in range(len(s1))]

    res = 0

    for i in range(len(s1)):
        if s1[i] == s2[0]:
            dp[i] = 1

    for i in range(1, len(s2)):
        for j in range(len(s1) - 1 , -1, -1):
            if s2[i] == s1[j]:
                dp[j] = dp[j - 1] + 1
            else:
                dp[j] = 0

            res = max(res, dp[j])

    return res


# Driver code to test the above function
if __name__ == '__main__':
    S1 = "0abc321"
    S2 = "123abcdef"
    print(longest_common_substr_length(S1, S2))

    S1 = "www.educative.io/explore"
    S2 = "educative.io/edpresso"
    print(longest_common_substr_length(S1, S2))

    S1 = ""
    S2 = ""
    print(longest_common_substr_length(S1, S2))

    S1 = "abdke"
    S2 = "bd"
    print(longest_common_substr_length(S1, S2))