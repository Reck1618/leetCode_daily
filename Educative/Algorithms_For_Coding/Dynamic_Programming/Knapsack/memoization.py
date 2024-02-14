"""
Given two integer arrays to represent weights and profits of N items, we need to find a
subset of these items which will give us maximum profit such that their cumulative weight
is not more than a given number C. Each item can only be selected once, which means either
we put an item in the knapsack or we skip it.
"""

def solve_knapsack(profits, profits_length, weights, capacity):
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]

    def solve(cap, index):
        nonlocal dp
        if cap <= 0 or index >= profits_length:
            return 0

        if dp[index][cap] != -1:
            return dp[index][cap]

        profit_1, profit_2 = 0, 0
        if weights[index] <= cap:
            profit_1 = profits[index] + solve(cap - weights[index], index + 1)

        profit_2 = solve(cap, index + 1)

        dp[index][cap] = max(profit_1, profit_2)
        return dp[index][cap]

    return solve(capacity, 0)



if __name__ == "__main__":
    print(solve_knapsack([1, 6, 10, 16], 4, [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], 4, [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], 4, [1, 2, 3, 5], 7))