"""
Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target.
Return TRUE if three such integers exist in the array. Otherwise, return FALSE.
"""

def find_sum_of_three(nums, target):
    """
    Finds if there are three numbers in the given list that add up to the target value.

    Args:
    - nums: A list of integers.
    - target: The target sum.

    Returns:
    - True if there are three numbers that add up to the target sum, False otherwise.
    """
    nums.sort()
    for i in range(len(nums)-2):
        if helper(nums[i], nums[i+1:], target):
            return True
    return False


def helper(cur_val, new_nums, target):
   l, r = 0, len(new_nums) - 1
   while l < r:
      cur_sum = cur_val + new_nums[l] + new_nums[r]

      if cur_sum == target:
         return True
      elif cur_sum > target:
         r -= 1
      else:
         l += 1

   return False


# Driver code
def main():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_three(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-"*100)

if __name__ == '__main__':
    main()
