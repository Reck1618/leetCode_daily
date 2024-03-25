"""
Given three strings m, n, and p, write a function to find out if p has been formed by interleaving m and n.
p should be considered to be an interleaved form of m and n, if it contains all the letters from m and n in a preserved order.
"""

# Memoization solution
def find_strings_interleaving(m, n, p):
    """
    Find the interleaving strings
    :param m: String 1
    :param n: String 2
    :param p: String 3
    :return: True if the strings are interleaving, otherwise False
    """
    memo = {}

    def helper(i, j, k):
        if i == len(m) and j == len(n) and k == len(p):
            return True

        if (i, j, k) in memo:
            return memo[(i, j, k)]

        if i < len(m) and k < len(p) and m[i] == p[k]:
            if helper(i + 1, j, k + 1):
                memo[(i, j, k)] = True
                return True

        if j < len(n) and k < len(p) and n[j] == p[k]:
            if helper(i, j + 1, k + 1):
                memo[(i, j, k)] = True
                return True

        memo[(i, j, k)] = False
        return False

    return helper(0, 0, 0)

# Bottom-up solution -> Start form the beginning of the strings
def find_strings_interleaving_one(m, n, p):
    """
    Find the interleaving strings
    :param m: String 1
    :param n: String 2
    :param p: String 3
    :return: True if the strings are interleaving, otherwise False
    """
    if len(m) + len(n) != len(p):
        return False

    dp = [[False for _ in range(len(n) + 1)] for _ in range(len(m) + 1)]

    for i in range(0, len(m) + 1):
        for j in range(0, len(n) + 1):
            if i == 0 and j == 0:
                dp[i][j] = True

            elif i and j and m[i-1] == p[i + j - 1] and n[j-1] == p[i + j - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

            elif i and m[i - 1] == p[i + j - 1]:
                dp[i][j] = dp[i - 1][j]

            elif j and n[j - 1] == p[i + j - 1]:
                dp[i][j] = dp[i][j - 1]

    return dp[len(m)][len(n)]


# Bottom-up solution -> Start form the end of the strings (NeetCode)
def find_strings_interleaving_two(m, n, p):
    """
    Find the interleaving strings
    :param m: String 1
    :param n: String 2
    :param p: String 3
    :return: True if the strings are interleaving, otherwise False
    """
    if len(m) + len(n) != len(p):
        return False

    dp = [[False for _ in range(len(n) + 1)] for _ in range(len(m) + 1)]
    dp[len(m)][len(n)] = True

    for i in range(len(m), -1, -1):
        for j in range(len(n), -1, -1):
            if i < len(m) and m[i] == p[i + j] and dp[i + 1][j]:
                dp[i][j] = True

            if j < len(n) and n[j] == p[i + j] and dp[i][j + 1]:
                dp[i][j] = True

    return dp[0][0]



# Driver code to test the above function
if __name__ == '__main__':

    print(find_strings_interleaving("abd", "cef", "adcbef"))
    print(find_strings_interleaving("abc", "def", "abdccf"))
    print(find_strings_interleaving("abcdef", "mnop", "mnaobcdepf"))