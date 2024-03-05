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
