"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""

# Bottom-up approach with dp
class Solution:
    def coinChange(self, coins, amount):
        dp = [ float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for amount in range(coin, amount + 1):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


# Recursive approach
class Solution:
    def coinChange(self, coins, amount):
        memo = {}
        def helper(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return -1
            elif amount in memo:
                return memo[amount]

            min_coins = float("inf")
            for coin in coins:
                temp = helper(amount - coin)
                if temp >= 0:
                    min_coins = min(min_coins, 1 + temp)

            memo[amount] = min_coins
            return memo[amount]

        res = helper(amount)
        return res if res != float("inf") else -1