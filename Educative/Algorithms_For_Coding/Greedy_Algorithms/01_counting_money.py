"""
Given infinite quarters, dimes, nickels and pennies, calculate the minimum number of coins to represent a number v.
"""

def find_min_coins(v, coins_available):
    """
    This function finds the minimum number of coins
    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """

    # Write your code here!
    coins_available.sort(reverse=True)
    result = []

    for coin in coins_available:
        while coin <= v:
            v -= coin
            result.append(coin)

    return result


# Main program to test the above code
if __name__ == "__main__":

    coins_available = [1, 5, 10, 25] # The available coins are in increasing order
    assert find_min_coins(19, coins_available) == [10, 5, 1, 1, 1, 1], "Test case 1 failed"
    print("Test case 1 passed")
