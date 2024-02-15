"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a function to count the number of possible ways that the child can run up the stairs.
"""

# Recursive top-down approach
def count_ways_one(n):
    """
    Calculates the number of ways a stair can be climbed
    :param n: Number of stairs
    :return: Number of ways to climb a stair
    """
    if n == 0:
        return 1
    if n < 0:
        return 0

    return count_ways_one(n - 1) + count_ways_one(n - 2) + count_ways_one(n - 3)


# Recursive top-down approach with memoization
def count_ways_two(n):
    """
    Calculates the number of ways a stair can be climbed
    :param n: Number of stairs
    :return: Number of ways to climb a stair
    """
    memo = {}

    def solve(n, memo):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n in memo:
            return memo[n]

        memo[n] = solve(n - 1, memo) + solve(n - 2, memo) + solve(n - 3, memo)
        return memo[n]

    return solve(n, memo)


# Bottom-up approach with space optimization
def count_ways_three(n):
    """
    Calculates the number of ways a stair can be climbed
    :param n: Number of stairs
    :return: Number of ways to climb a stair
    """
    if n == 0:
        return 1
    if n <= 2:
        return n

    a, b, c = 1, 1, 2

    for i in range(3, n + 1):
        total = a + b + c
        a = b
        b = c
        c = total

    return total



if __name__ == "__main__":
    print(count_ways_one(3))  # 4
    print(count_ways_two(4))  # 7
    print(count_ways_three(5))  # 13
    print(count_ways_two(6))  # 24


