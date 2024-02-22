"""
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write some code to calculate the number of ways to represent n cents.
"""

# Bottom-up approach with dp
def count_change(denoms, amount):
    """
    Finds the number of ways that the given number of cents can be represented.
    :param denoms: Values of the coins available
    :param denoms_length: Number of denoms
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """

    dp = [[0 for _ in range(amount + 1)] for _ in range(len(denoms) + 1)]

    for i in range(len(denoms) + 1):
        dp[i][0] = 1

    for i in range(1, len(denoms) + 1):
        for j in range(1, amount + 1):
            if j - denoms[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - denoms[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(denoms)][amount]


# One dp solution
def count_change_one_dp(denoms, amount):
    """
    Finds the number of ways that the given number of cents can be represented.
    :param denoms: Values of the coins available
    :param denoms_length: Number of denoms
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1

    for i in denoms:
        for j in range(i, amount + 1):
            dp[j] += dp[j - i]

    return dp[amount]


# recursive approach
def count_change_recursive(denoms, amount):
    """
    Finds the number of ways that the given number of cents can be represented.
    :param denoms: Values of the coins available
    :param denoms_length: Number of denoms
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """
    memo = {}
    def helper(amount, index):
        if amount == 0:
            return 1
        if amount < 0 or index >= len(denoms):
            return 0
        if (amount, index) in memo:
            return memo[amount, index]

        with_coin = helper(amount - denoms[index], index)
        without_coin = helper(amount, index + 1)

        memo[(amount, index)] = with_coin + without_coin
        return memo[(amount, index)]

    return helper(amount, 0)


# Driver code to test the above function
if __name__ == '__main__':

    denoms = [25, 10, 5, 1]
    print(count_change(denoms, 10))