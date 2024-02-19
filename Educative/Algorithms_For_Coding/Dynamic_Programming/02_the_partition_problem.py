"""
Given a list of integers, write a function to find if any two subsets of the input list exist—such that the sum of both subsets is equal. 
You can assume that the list will only consist of positive integers.
"""
# recursive top-down approach
def can_partition_one(nums):
    if sum(nums) % 2:
        return False

    target = sum(nums) // 2
    memo = {}

    def solve(target, ind):
        if (target, ind) in memo:
            return memo[(target, ind)]

        if target == 0:
            return True

        if target < 0 or ind >= len(nums):
            return False

        memo[(target, ind)] = solve(target - nums[ind], ind + 1) or solve(target, ind + 1)
        return memo[(target, ind)]

    return solve(target, 0)


# One dp soulution
def can_partition_two(nums):
    """
    Checks if two sub-lists has equal sum or not
    :param set: Integer list having positive numbers only
    :return: returns True if two sub-lists have equal sum, otherwise False
    """

    if sum(nums) % 2:
        return False

    target = sum(nums) // 2
    dp = [False for _ in range(target + 1)]

    dp[0] = True

    for j in range(target + 1):
        if nums[0] == j:
            dp[j] = True

    for i in range(1, len(nums)):
        for j in range(1, target + 1):
            if not dp[j] or j >= nums[i]:
                dp[j] = dp[j - nums[i]]

    return dp[target]


# Regular bottom up solution
def can_partition_three(nums):
    if sum(nums) % 2:
        return False

    target = sum(nums) // 2
    dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = True

    for j in range(target + 1):
        if nums[0] == j:
            dp[0][j] = True

    for i in range(1, len(nums)):
        for j in range(1, target + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]

    return dp[len(nums) - 1][target]


# Driver code to test the above function
if __name__ == '__main__':
    set1 = [1, 2, 3, 4]
    print(can_partition_one(set1))

    set2 = [1, 1, 3, 4, 7]
    print(can_partition_two(set2))

    set3 = [2, 3, 4, 6]
    print(can_partition_three(set3))