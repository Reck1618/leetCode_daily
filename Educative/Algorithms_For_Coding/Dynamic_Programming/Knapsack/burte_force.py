"""
Given two integer arrays to represent weights and profits of N items, we need to find a
subset of these items which will give us maximum profit such that their cumulative weight
is not more than a given number C. Each item can only be selected once, which means either
we put an item in the knapsack or we skip it.
"""

def solve_knapsack(profits, weights, capacity):

    def solve(cap, index):
        if cap <= 0 or index >= len(profits):
            return 0

        profit_1 = 0
        if weights[index] <= cap:
            profit_1 = profits[index] + solve(cap - weights[index], index + 1)

        profit_2 = solve(cap, index + 1)
        return max(profit_1, profit_2)

    return solve(capacity, 0)



if __name__ == "__main__":
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))