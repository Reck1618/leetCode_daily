"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

class Solution:
    def exist(self, board, word):

        def backtrack(i, j, word):
            if not word:
               return True

            # If the current cell is out of bounds or doesn't match the first letter of the word, return False
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[0]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            # Check all 4 directions for the next letter in the word
            result = (
                    backtrack(i + 1, j, word[1:]) or
                    backtrack(i - 1, j, word[1:]) or
                    backtrack(i, j + 1, word[1:]) or
                    backtrack(i, j - 1, word[1:])
            )
            board[i][j] = temp
            return result

        # Iterate through the board and check if the first letter of the word matches the current cell
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, word):
                    return True
        return False