"""
Given the number of digits and the sum of the digits, find the largest number that can be created.
"""

def find_largest_number(number_of_digits, sum_of_digits):
    """
    Finds the largest number with given number of digits and sum of Digits
    :param number_of_digits: Number of digits
    :param sum_of_digits: Sum of digits
    :return: Possible largest number
    """

    if sum_of_digits > 9 * number_of_digits:
        return [-1]

    result = [0] * number_of_digits
    remaning_sum = sum_of_digits

    for i in range(number_of_digits):
        digit = min(9, remaning_sum)
        result[i] = digit
        remaning_sum -= digit

    return result
