"""

Definition: The Fibonacci Sequence is a series of numbers where the next number is found by adding up the two numbers before it.
The first two numbers of the Fibonacci Sequence are 0 and 1. The third number is 0 + 1 = 1, the fourth number is 1 + 1 = 2, the fifth number is 1 + 2 = 3, and so on.

"""

# Algorithms to find fibonacci numbers :

# Naive algorithm (time complexity: O(2^n), space complexity: O(n)) / Top-down approach
def naive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return naive_fibonacci(n-1) + naive_fibonacci(n-2)

# Efficient algorithm (time complexity: O(n), space complexity: O(n)) / Bottom-up approach
def efficient_fibonacci(n):
    if n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

# Efficient algorithm with memoization (time complexity: O(n), space complexity: O(n))
def efficient_fibonacci_memoization(n, memo=None):
    if memo is None:
        memo = [None] * (n + 1)
    if n < 2:
        return n
    if memo[n] is not None:
        return memo[n]
    else:
        memo[n] = efficient_fibonacci_memoization(n-1, memo) + efficient_fibonacci_memoization(n-2, memo)
        return memo[n]


# Efficient algorithm with space optimization (time complexity: O(n), space complexity: O(1))
def efficient_fibonacci_space_optimized(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

# Efficient algorithm with space optimization and modulo (time complexity: O(n), space complexity: O(1))
def efficient_fibonacci_space_optimized_modulo(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = (a + b) % 10
            a = b
            b = c
        return b

