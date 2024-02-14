"""
Given two integer arrays to represent weights and profits of N items, we need to find a
subset of these items which will give us maximum profit such that their cumulative weight
is not more than a given number C. Each item can only be selected once, which means either
we put an item in the knapsack or we skip it.
"""

# Using the improved bottom-up approach i.e. using only two rows of the dp array

def solve_knapsack(profits, weights, capacity):

    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for i in range(capacity + 1)] for j in range(2)]

    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = dp[1][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0

            if weights[i] <= c:
                profit1 = profits[i] + dp[(i-1)%2][c - weights[i]]

            profit2 = dp[(i - 1)%2][c]

            dp[i % 2][c] = max(profit1, profit2)

    return dp[(n - 1) % 2][capacity]




if __name__ == "__main__":
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))