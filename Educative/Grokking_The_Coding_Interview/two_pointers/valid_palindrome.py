"""
Write a function that takes a string, s, as an input and determines whether or not it is a palindrome.
"""

def is_palindrome(s):

  # Replace this placeholder return statement with your code
  l, r = 0, len(s) - 1

  while l <= r:
    if s[l] != s[r]:
      return False
    l += 1
    r -= 1
  return True

# Driver code
def main():
    test_cases = ["RACECAR", "ABBA", "TART"]
    i = 1
    for s in test_cases:
        print("Test Case #", i)
        print(is_palindrome(s))
        print("-" * 100, end="\n\n")
        i = i + 1

if __name__ == '__main__':
    main()
