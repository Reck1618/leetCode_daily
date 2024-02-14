"""
Given two integer arrays to represent weights and profits of N items, we need to find a
subset of these items which will give us maximum profit such that their cumulative weight
is not more than a given number C. Each item can only be selected once, which means either
we put an item in the knapsack or we skip it.
"""

def solve_knapsack(profits, weights, capacity):
    n = len(profits)

    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [0 for _ in range(capacity + 1)]

    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[c] = profits[0]

    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit_1, profit_2 = 0, 0
            if weights[i] <= c:
                profit_1 = profits[i] + dp[c - weights[i]]

            profit_2 = dp[c]

            dp[c] = max(profit_1, profit_2)

    return dp[capacity]



if __name__ == "__main__":
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))