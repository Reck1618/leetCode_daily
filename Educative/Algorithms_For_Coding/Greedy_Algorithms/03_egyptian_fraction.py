"""
Given a positive fraction, break it down into its Egyptian fraction's denominators.
"""

import math

def egyptian_fraction(numerator, denominator):
    """
    Finds the egyptian fraction denominators
    :param numerator: Numerator of the fraction
    :param denominator: Denominator of the fraction
    :return: A list of denominators of the egyptian fraction
    """

    result = []

    while numerator != 0:
        x = math.ceil(denominator / numerator)
        result.append(x)

        numerator = x * numerator - denominator
        denominator = x * denominator

    return result


# Driver code to test above function
if __name__ == '__main__':

    print(egyptian_fraction(6, 14))
    print(egyptian_fraction(2, 3))
    print(egyptian_fraction(4, 7))
