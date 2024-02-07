"""
Write a function that takes a string as input and checks whether it can be a valid palindrome by removing at most one character from it.
"""

def is_palindrome(s):

  def helper(left, right):
    while left <= right:
      if s[left] != s[right]:
        return False
      left += 1
      right -= 1
    return True

  l, r = 0, len(s) - 1
  while l <= r:
    if s[l] != s[r]:
      return helper(l+1, r) or helper(l, r-1)

    l += 1
    r -= 1

  return True


def main():
    inputs = ["aba", "abca", "abc", "deeee", "abccba", "abccbaa", "abccbaaa", "abccbaaaa", "abccbaaaaa", "abccbaaaaaa"]

    for i in range(len(inputs)):
        print(i + 1, ".\tstring:", inputs[i],
              "\n\n\tThe string is a valid palindrome after removing at most one character:", is_palindrome(inputs[i]))
        print("-" * 100)

if __name__ == "__main__":
    main()