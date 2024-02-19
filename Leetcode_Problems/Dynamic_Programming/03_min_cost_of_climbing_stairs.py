"""
"""

# NeetCode
class Solution:
    def minCostClimbingStairs(self, cost):
        for i in range(len(cost) - 3 , -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


# Recursive 1
class Solution:
    def minCostClimbingStairs(self, cost):
        memo = {}

        def solve(index):
            if index in memo:
                return memo[index]

            if index >= len(cost):
                return 0

            a = solve(index + 1)
            b = solve(index + 2)
            memo[index] = cost[index] + min(a, b)
            return memo[index]

        return min(solve(0), solve(1))


# Recursive top down approach 2
class Solution:
    def minCostClimbingStairs(self, cost):
        memo = {}

        def solve(index):
            if index in memo:
                return memo[index]

            if index < 0:
                return 0

            a = solve(index - 1)
            b = solve(index - 2)
            memo[index] = cost[index] + min(a, b)
            return memo[index]

        return min(solve(len(cost) - 1), solve(len(cost) - 2))


# Bottom up approach
class Solution:
    def minCostClimbingStairs(self, cost):
        l = len(cost) - 1

        dp = [0] * (l + 1)

        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, l + 1):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[l], dp[l - 1])