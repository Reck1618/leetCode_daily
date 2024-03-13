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

