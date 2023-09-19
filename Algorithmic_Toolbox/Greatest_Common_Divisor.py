"""

Definition: Greatest common divisor (GCD) of two integers is the largest integer that divides both numbers without leaving a remainder.
To find the GCD efficiently, we use the Euclidean algorithm.

We find the GCD of two numbers a and b, where a >= b, by repeatedly dividing a by b and setting a to b and b to the remainder until the remainder is 0.
The remainder of a and b is called a prime and is denoted by a' (a_prime). The GCD will be the last non-zero remainder.

"""

# Algorithms to find GCD of two numbers :

# Naive algorithm (time complexity: O(min(a, b)), space complexity: O(1))
def naive_gcd(a, b):
    best = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            best = i
    return best

# Euclidean algorithm (recursive) (time complexity: O(log(a + b)), space complexity: O(1))
def euclidean_gcd(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return euclidean_gcd(b, a_prime)

# Euclidean algorithm (iterative) (time complexity: O(log(a + b)), space complexity: O(1))
def euclidean_gcd_iterative(a, b):
    while b != 0:
        a_prime = a % b
        a = b
        b = a_prime
    return a

