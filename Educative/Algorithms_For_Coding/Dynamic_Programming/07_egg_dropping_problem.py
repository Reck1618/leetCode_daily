"""
Given a tall skyscraper and a few eggs, write a function to figure out how many tries it would take to find which floor of the skyscraper from which the eggs can be safely dropped without breaking. Here are some rules;

An egg that survives a fall can be used again. A broken egg must be discarded
The effect of a fall is the same for all eggs
If an egg breaks when dropped, then, it would break if dropped from a higher floor
If an egg survives a fall, then it would survive a shorter fall
"""

def egg_drop(eggs, floors):
    memo = {}

    def solve(eggs, floors):
        if eggs <= 0:
            return 0

        if eggs == 1 or floors <= 1:
            return floors

        if (eggs, floors) in memo:
            return memo[(eggs, floors)]

        min_drops = float("inf")
        for f in range(1, floors + 1):
            min_drops = min(min_drops, 1 + max(solve(eggs - 1, f - 1), solve(eggs, floors - f)))

        memo[(eggs, floors)] = min_drops
        return min_drops

    return solve(eggs, floors)


# Botttom-up approach
def egg_drop_2(eggs, floors):
    if eggs <= 0:
        return 0
    if eggs == 1 or floors <= 1:
        return floors

    dp = [[0 for _ in range(floors + 1)] for _ in range(eggs + 1)]

    for floor in range(1, floors + 1):
        dp[1][floor] = floor

    for egg in range(1, eggs + 1):
        dp[egg][1] = 1

    for egg in range(2, eggs + 1):
        for floor in range(2, floors + 1):
            dp[egg][floor] = float('inf')
            for f in range(1, floor + 1):
                dp[egg][floor] = min(dp[egg][floor], 1 + max(dp[egg - 1][f - 1], dp[egg][floor - f]))

    return dp[eggs][floors]


# Optimized bottom-up approach
def egg_drop_3(eggs, floors):
    if eggs <= 0:
        return eggs

    if floors <= 1 or eggs == 1:
        return floors

    dp = [[0 for _ in range(eggs + 1)] for _ in range(floors + 1)]

    for f in range(1, floors + 1):
        for e in range(1, eggs + 1):
            dp[f][e] = dp[f - 1][e - 1] + dp[f - 1][e] + 1
        if dp[f][eggs] >= floors:
            return f


# Binary search approach

def egg_drop_4(eggs, floors):
    """
    Figures out which floor of the skyscraper that the eggs can be safely dropped from without breaking.
    :param eggs: Number of stories of the skyscraper
    :param floors: Number of eggs
    :return: Return the floor
    """

    def binomial_coeff(x, n, k):
        """
        Find sum of binomial coefficients xCi (where i varies from 1 to n).
        If the sum becomes more than K
        :param x: Mid point
        :param n: Eggs
        :param k: Floor
        :return: Binomial Coefficient
        """

        sum = 0
        term = 1

        for i in range(1, n + 1):
            if sum < k:
                term *= x - i + 1
                term //= i
                sum += term

        return sum


    # If there are no eggs, then there can't be any tries
    if eggs <= 0:
        return 0

    # If there are no floors, then no trials needed. OR if there is
    # one floor, one trial needed.
    if floors == 1 or floors == 0:
        return floors

    # We need k trials for one egg and k floors
    if eggs == 1:
        return floors

        # Initialize low and high as 1st
    # and last floors
    low = 1
    high = floors

    # Do binary search, for every mid,
    # find sum of binomial coefficients and
    # check if the sum is greater than k or not.
    while low < high:

        mid = (low + high) // 2

        if binomial_coeff(mid, eggs, floors) < floors:
            low = mid + 1
        else:
            high = mid

    return low


# Driver code to test the above function
if __name__ == '__main__':

    print(egg_drop_4(2, 13))